from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

ALPHA = 0.5
SEED = 20261003
TRAIN_MONTHS = tuple(range(1, 7))
VALID_MONTHS = (7, 8)
ALLOWED_MONTHS = TRAIN_MONTHS + VALID_MONTHS
SOURCE_BOROUGHS = ("Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island")
ZONE_URL = "https://data.cityofnewyork.us/resource/8meu-9t5y.json"
TRIP_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-{month:02d}.parquet"
N_PERM = 999
N_BOOT = 10000


@dataclass
class Model:
    dest_classes: list[str]
    zone_probs: dict[tuple[int, int], np.ndarray]
    macro_probs: dict[tuple[str, int], np.ndarray]
    zone_to_borough: dict[int, str]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "P001-prevalidation/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r, path.open("wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)


def load_zone_lookup(path: Path) -> tuple[dict[int, str], list[str]]:
    z = pd.read_json(path)
    cols = {c.lower(): c for c in z.columns}
    loc_col = cols.get("locationid") or cols.get("location id")
    bor_col = cols.get("borough")
    if not loc_col or not bor_col:
        raise ValueError(f"Unexpected zone lookup columns: {list(z.columns)}")
    z = z[[loc_col, bor_col]].dropna(subset=[loc_col]).copy()
    z[loc_col] = pd.to_numeric(z[loc_col], errors="raise").astype(int)
    z[bor_col] = z[bor_col].fillna("UNMAPPED").astype(str)
    mapping = dict(zip(z[loc_col], z[bor_col]))
    dest_classes = sorted(set(mapping.values()) | {"UNMAPPED"})
    return mapping, dest_classes


def aggregate_month(
    path: Path,
    month: int,
    zone_to_borough: dict[int, str],
) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    # Only columns permitted by the preregistration are read.
    df = pd.read_parquet(
        path,
        columns=["tpep_pickup_datetime", "PULocationID", "DOLocationID"],
    )
    n_raw = len(df)
    pickup = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")
    pu = pd.to_numeric(df["PULocationID"], errors="coerce")
    do = pd.to_numeric(df["DOLocationID"], errors="coerce")

    start = pd.Timestamp(2023, month, 1)
    end = pd.Timestamp(2024, 1, 1) if month == 12 else pd.Timestamp(2023, month + 1, 1)
    in_month = pickup.notna() & (pickup >= start) & (pickup < end)
    valid_pu = pu.notna() & pu.astype("Int64").map(zone_to_borough).isin(SOURCE_BOROUGHS)
    keep = in_month & valid_pu

    work = pd.DataFrame(
        {
            "pickup": pickup[keep],
            "pulocationid": pu[keep].astype(int),
            "dolocationid": do[keep].astype("Int64"),
        }
    )
    work["hour"] = work["pickup"].dt.floor("h")
    work["how"] = work["pickup"].dt.dayofweek * 24 + work["pickup"].dt.hour

    # Input-only table: no destination column is used to construct rho_t.
    pickups = (
        work.groupby(["hour", "how", "pulocationid"], observed=True)
        .size()
        .rename("n_pickups")
        .reset_index()
    )

    dest_id = work["dolocationid"].astype("Int64")
    work["dest_macro"] = dest_id.map(zone_to_borough).fillna("UNMAPPED")
    outcomes = (
        work.groupby(["hour", "how", "pulocationid", "dest_macro"], observed=True)
        .size()
        .rename("n")
        .reset_index()
    )

    meta = {
        "month": month,
        "raw_rows": int(n_raw),
        "rows_in_declared_month": int(in_month.sum()),
        "rows_valid_source_zone": int(keep.sum()),
        "rows_excluded": int(n_raw - keep.sum()),
    }
    return pickups, outcomes, meta


def fit_model(
    train_pickups: pd.DataFrame,
    train_outcomes: pd.DataFrame,
    zone_to_borough: dict[int, str],
    dest_classes: list[str],
) -> Model:
    J = len(dest_classes)
    dindex = {b: k for k, b in enumerate(dest_classes)}
    zone_probs: dict[tuple[int, int], np.ndarray] = {}

    grouped = train_outcomes.groupby(["how", "pulocationid"], observed=True)
    for (how, i), g in grouped:
        counts = np.zeros(J, dtype=float)
        for row in g.itertuples(index=False):
            counts[dindex[row.dest_macro]] += float(row.n)
        probs = (counts + ALPHA) / (counts.sum() + ALPHA * J)
        zone_probs[(int(how), int(i))] = probs

    uniform = np.full(J, 1.0 / J)
    macro_probs: dict[tuple[str, int], np.ndarray] = {}
    tp = train_pickups.copy()
    tp["source_borough"] = tp["pulocationid"].map(zone_to_borough)
    for (A, how), g in tp.groupby(["source_borough", "how"], observed=True):
        n_total = float(g["n_pickups"].sum())
        if n_total <= 0:
            continue
        p = np.zeros(J, dtype=float)
        for row in g.itertuples(index=False):
            w = float(row.n_pickups) / n_total
            p += w * zone_probs.get((int(how), int(row.pulocationid)), uniform)
        p /= p.sum()
        macro_probs[(str(A), int(how))] = p

    return Model(dest_classes, zone_probs, macro_probs, zone_to_borough)


def make_block_predictions(model: Model, val_pickups: pd.DataFrame) -> pd.DataFrame:
    J = len(model.dest_classes)
    uniform = np.full(J, 1.0 / J)
    vp = val_pickups.copy()
    vp["source_borough"] = vp["pulocationid"].map(model.zone_to_borough)
    rows = []

    for (hour, how, A), g in vp.groupby(
        ["hour", "how", "source_borough"],
        observed=True,
    ):
        N = float(g["n_pickups"].sum())
        if N <= 0:
            continue

        p_micro = np.zeros(J, dtype=float)
        unseen_pickups = 0.0
        for row in g.itertuples(index=False):
            rho = float(row.n_pickups) / N
            key = (int(how), int(row.pulocationid))
            if key not in model.zone_probs:
                unseen_pickups += float(row.n_pickups)
            p_micro += rho * model.zone_probs.get(key, uniform)

        p_micro /= p_micro.sum()
        p_macro = model.macro_probs.get((str(A), int(how)), uniform).copy()
        p_macro /= p_macro.sum()
        s_pred = float(np.sum(p_micro * np.log(p_micro / p_macro)))

        rows.append(
            {
                "hour": hour,
                "how": int(how),
                "source_borough": str(A),
                "N_pickups": int(N),
                "p_micro": p_micro,
                "p_macro": p_macro,
                "S_pred": s_pred,
                "unseen_pickups": int(unseen_pickups),
            }
        )

    return pd.DataFrame(rows)


def score_blocks(
    pred: pd.DataFrame,
    outcomes: pd.DataFrame,
    model: Model,
) -> pd.DataFrame:
    dindex = {b: k for k, b in enumerate(model.dest_classes)}
    out = outcomes.copy()
    out["source_borough"] = out["pulocationid"].map(model.zone_to_borough)
    agg = (
        out.groupby(
            ["hour", "how", "source_borough", "dest_macro"],
            observed=True,
        )["n"]
        .sum()
        .reset_index()
    )

    counts_by_key = {}
    J = len(model.dest_classes)
    for (hour, how, A), g in agg.groupby(
        ["hour", "how", "source_borough"],
        observed=True,
    ):
        y = np.zeros(J, dtype=float)
        for row in g.itertuples(index=False):
            y[dindex[row.dest_macro]] += float(row.n)
        counts_by_key[(hour, int(how), str(A))] = y

    scored = []
    for row in pred.itertuples(index=False):
        y = counts_by_key.get(
            (row.hour, int(row.how), str(row.source_borough))
        )
        if y is None or y.sum() <= 0:
            continue

        N = float(y.sum())
        assert int(N) == int(row.N_pickups), (
            row.hour,
            row.source_borough,
            N,
            row.N_pickups,
        )

        lm = float(-np.sum(y * np.log(row.p_micro)) / N)
        lM = float(-np.sum(y * np.log(row.p_macro)) / N)
        g = float(lM - lm)

        scored.append(
            {
                "hour": row.hour,
                "how": int(row.how),
                "source_borough": row.source_borough,
                "N": int(N),
                "L_micro": lm,
                "L_macro": lM,
                "gain": g,
                "S_pred": float(row.S_pred),
                "unseen_pickups": int(row.unseen_pickups),
                "p_micro": row.p_micro,
                "p_macro": row.p_macro,
                "y": y,
            }
        )

    return pd.DataFrame(scored)


def week_start(ts: pd.Timestamp) -> pd.Timestamp:
    return (ts - pd.Timedelta(days=ts.weekday())).floor("D")


def summarize(scored: pd.DataFrame, rng: np.random.Generator) -> dict:
    N = scored["N"].to_numpy(float)
    gain = scored["gain"].to_numpy(float)
    S = scored["S_pred"].to_numpy(float)

    total = N.sum()
    G = float(np.sum(N * gain) / total)
    Lmicro = float(
        np.sum(N * scored["L_micro"].to_numpy(float)) / total
    )
    Lmacro = float(
        np.sum(N * scored["L_macro"].to_numpy(float)) / total
    )
    Gpred = float(np.sum(N * S) / total)

    denom = float(np.sum(N * S * S))
    beta = float(np.sum(N * S * gain) / denom) if denom > 0 else float("nan")

    temp = scored[["hour", "N", "gain", "S_pred"]].copy()
    temp["week"] = temp["hour"].map(week_start)
    wk = (
        temp.groupby("week", observed=True)
        .apply(
            lambda g: pd.Series(
                {
                    "N": float(g["N"].sum()),
                    "num_gain": float(np.sum(g["N"] * g["gain"])),
                    "num_sg": float(
                        np.sum(g["N"] * g["S_pred"] * g["gain"])
                    ),
                    "den_s2": float(
                        np.sum(g["N"] * g["S_pred"] * g["S_pred"])
                    ),
                }
            ),
            include_groups=False,
        )
        .reset_index()
    )

    boots = []
    betas = []
    m = len(wk)
    for _ in range(N_BOOT):
        idx = rng.integers(0, m, size=m)
        b = wk.iloc[idx]

        denN = float(b["N"].sum())
        boots.append(float(b["num_gain"].sum() / denN))

        denb = float(b["den_s2"].sum())
        betas.append(
            float(b["num_sg"].sum() / denb)
            if denb > 0
            else np.nan
        )

    ci = [
        float(x)
        for x in np.quantile(np.asarray(boots), [0.025, 0.975])
    ]
    beta_arr = np.asarray([x for x in betas if np.isfinite(x)])
    beta_ci = (
        [
            float(x)
            for x in np.quantile(beta_arr, [0.025, 0.975])
        ]
        if len(beta_arr)
        else [None, None]
    )

    unseen = float(scored["unseen_pickups"].sum())

    return {
        "n_trips": int(total),
        "n_blocks": int(len(scored)),
        "n_weeks": int(m),
        "unseen_zone_hour_pickups": int(unseen),
        "unseen_zone_hour_pickup_fraction": float(unseen / total),
        "logloss_micro": Lmicro,
        "logloss_macro": Lmacro,
        "observed_gain_nats_per_trip": G,
        "bootstrap_95_ci_gain": ci,
        "predicted_kl_gain_nats_per_trip": Gpred,
        "weighted_structural_slope": beta,
        "bootstrap_95_ci_slope": beta_ci,
    }


def permutation_null(
    scored: pd.DataFrame,
    rng: np.random.Generator,
) -> dict:
    # Null: composition-derived MICRO predictions are reassigned among
    # validation hours having the same source borough and hour-of-week.
    base_macro_num = float(
        np.sum(scored["N"] * scored["L_macro"])
    )
    totalN = float(scored["N"].sum())
    observed = float(
        np.sum(scored["N"] * scored["gain"]) / totalN
    )

    y_matrix = np.vstack(
        scored["y"].map(
            lambda x: np.asarray(x, dtype=float)
        ).to_numpy()
    )
    log_micro = np.log(
        np.vstack(
            scored["p_micro"].map(
                lambda x: np.asarray(x, dtype=float)
            ).to_numpy()
        )
    )

    groups = [
        np.asarray(list(idxs), dtype=int)
        for idxs in scored.groupby(
            ["source_borough", "how"],
            observed=True,
        ).groups.values()
    ]

    null = np.empty(N_PERM, dtype=float)

    for r in range(N_PERM):
        ll_micro_num = 0.0

        for idxs in groups:
            perm = idxs.copy()
            rng.shuffle(perm)
            ll_micro_num += float(
                -np.sum(
                    y_matrix[idxs]
                    * log_micro[perm]
                )
            )

        null[r] = (
            base_macro_num - ll_micro_num
        ) / totalN

    p = (
        1 + int(np.sum(null >= observed))
    ) / (N_PERM + 1)

    return {
        "n_permutations": N_PERM,
        "null_mean_gain": float(null.mean()),
        "null_q99_gain": float(np.quantile(null, 0.99)),
        "one_sided_permutation_p": float(p),
        "observed_gain": observed,
    }

def self_test() -> None:
    # Non-lumpable: rows differ; shifted composition changes the macro row.
    p1 = np.array([0.9, 0.1])
    p2 = np.array([0.1, 0.9])
    macro = 0.5 * p1 + 0.5 * p2
    micro = 0.9 * p1 + 0.1 * p2
    y = np.array([820.0, 180.0])

    gain = float(
        np.sum(y * np.log(micro / macro)) / y.sum()
    )
    assert gain > 0.0, gain

    # Lumpable: identical rows imply exact occupancy invariance.
    q1 = np.array([0.7, 0.3])
    q2 = np.array([0.7, 0.3])
    macro2 = 0.5 * q1 + 0.5 * q2
    micro2 = 0.9 * q1 + 0.1 * q2

    assert np.allclose(
        macro2,
        micro2,
        rtol=0,
        atol=1e-15,
    )

    print(
        json.dumps(
            {
                "self_test": "PASS",
                "nonlumpable_gain": gain,
                "lumpable_max_abs_diff": float(
                    np.max(np.abs(macro2 - micro2))
                ),
            },
            indent=2,
        )
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--data-dir",
        default=".p001-data",
    )
    ap.add_argument(
        "--output-dir",
        default="experiments/p001/results/prevalidation",
    )
    ap.add_argument(
        "--self-test",
        action="store_true",
    )
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    # Hard safety boundary: prevalidation must never load Sep-Dec 2023.
    assert ALLOWED_MONTHS == tuple(range(1, 9))
    assert max(ALLOWED_MONTHS) == 8

    data_dir = Path(args.data_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    zone_path = data_dir / "nyc_taxi_zones.json"
    download(ZONE_URL, zone_path)
    zone_to_borough, dest_classes = load_zone_lookup(zone_path)

    pickups = []
    outcomes = []
    monthly_meta = []
    hashes = {
        "nyc_taxi_zones.json": sha256_file(zone_path)
    }

    for month in ALLOWED_MONTHS:
        p = (
            data_dir
            / f"yellow_tripdata_2023-{month:02d}.parquet"
        )
        download(TRIP_URL.format(month=month), p)
        hashes[p.name] = sha256_file(p)

        pk, oc, meta = aggregate_month(
            p,
            month,
            zone_to_borough,
        )
        pickups.append(pk)
        outcomes.append(oc)
        monthly_meta.append(meta)

    all_pk = pd.concat(pickups, ignore_index=True)
    all_oc = pd.concat(outcomes, ignore_index=True)

    train_pk = all_pk[
        all_pk["hour"].dt.month.isin(TRAIN_MONTHS)
    ].copy()
    train_oc = all_oc[
        all_oc["hour"].dt.month.isin(TRAIN_MONTHS)
    ].copy()

    val_pk = all_pk[
        all_pk["hour"].dt.month.isin(VALID_MONTHS)
    ].copy()
    val_oc = all_oc[
        all_oc["hour"].dt.month.isin(VALID_MONTHS)
    ].copy()

    assert train_pk["hour"].max() < pd.Timestamp("2023-07-01")
    assert val_pk["hour"].min() >= pd.Timestamp("2023-07-01")
    assert val_pk["hour"].max() < pd.Timestamp("2023-09-01")

    model = fit_model(
        train_pk,
        train_oc,
        zone_to_borough,
        dest_classes,
    )
    pred = make_block_predictions(
        model,
        val_pk,
    )
    scored = score_blocks(
        pred,
        val_oc,
        model,
    ).reset_index(drop=True)

    rng = np.random.default_rng(SEED)
    summary = summarize(
        scored,
        rng,
    )
    null = permutation_null(
        scored,
        rng,
    )

    # Validation is diagnostic only. It cannot confer PASS/FAIL on P-001.
    summary["status"] = "PREVALIDATION_ONLY"
    summary["primary_hypothesis"] = (
        "occupancy-preserving micro mixture has lower log-loss "
        "than occupancy-erasing macro mixture"
    )
    summary["alpha_jeffreys"] = ALPHA
    summary["seed"] = SEED
    summary["train_months"] = list(TRAIN_MONTHS)
    summary["validation_months"] = list(VALID_MONTHS)
    summary["holdout_loaded"] = False
    summary["destination_classes"] = dest_classes
    summary["permutation_null"] = null

    (out_dir / "summary.json").write_text(
        json.dumps(
            summary,
            indent=2,
            default=str,
        )
        + "\n",
        encoding="utf-8",
    )
    (out_dir / "data_manifest.json").write_text(
        json.dumps(
            {
                "hashes": hashes,
                "monthly": monthly_meta,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    public_cols = [
        "hour",
        "how",
        "source_borough",
        "N",
        "L_micro",
        "L_macro",
        "gain",
        "S_pred",
        "unseen_pickups",
    ]
    scored[public_cols].to_csv(
        out_dir / "block_scores.csv",
        index=False,
    )

    print(
        json.dumps(
            summary,
            indent=2,
            default=str,
        )
    )


if __name__ == "__main__":
    main()
