from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

ALPHA = 0.5
SEED = 20261003
N_BOOT = 10000
BOOT_BLOCK_WEEKS = 8
SOURCE_BOROUGHS = ("Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island")

ZONE_URL = "https://data.cityofnewyork.us/resource/8meu-9t5y.json"
TRIP_URL = (
    "https://d37ci6vzurychx.cloudfront.net/trip-data/"
    "yellow_tripdata_{year}-{month:02d}.parquet"
)

FROZEN_2023_MONTHS = (1, 2, 3, 4, 5, 6)
HISTORY_2023_MONTHS = (9, 10, 11, 12)
EVAL_2024_MONTHS = tuple(range(1, 13))

TARGET_START = pd.Timestamp("2024-01-01")
TARGET_WEEKS = tuple(
    TARGET_START + pd.Timedelta(days=7 * k)
    for k in range(52)
)
TARGET_END = pd.Timestamp("2024-12-30")


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
    req = urllib.request.Request(url, headers={"User-Agent": "P002-k-drift/1.0"})
    with urllib.request.urlopen(req, timeout=240) as r, path.open("wb") as f:
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

    z = z[[loc_col, bor_col]].copy()
    z[loc_col] = pd.to_numeric(z[loc_col], errors="raise").astype(int)
    z[bor_col] = z[bor_col].fillna("UNMAPPED").astype(str)

    mapping = dict(zip(z[loc_col], z[bor_col]))
    dest_classes = sorted(set(mapping.values()) | {"UNMAPPED"})
    return mapping, dest_classes


def month_bounds(year: int, month: int) -> tuple[pd.Timestamp, pd.Timestamp]:
    start = pd.Timestamp(year, month, 1)
    if month == 12:
        end = pd.Timestamp(year + 1, 1, 1)
    else:
        end = pd.Timestamp(year, month + 1, 1)
    return start, end


def aggregate_month_weekly(
    path: Path,
    year: int,
    month: int,
    zone_to_borough: dict[int, str],
) -> tuple[pd.DataFrame, dict]:
    df = pd.read_parquet(
        path,
        columns=["tpep_pickup_datetime", "PULocationID", "DOLocationID"],
    )
    n_raw = len(df)

    pickup = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")
    pu = pd.to_numeric(df["PULocationID"], errors="coerce")
    do = pd.to_numeric(df["DOLocationID"], errors="coerce")

    start, end = month_bounds(year, month)
    in_month = pickup.notna() & (pickup >= start) & (pickup < end)

    pu_int = pu.astype("Int64")
    valid_source = pu.notna() & pu_int.map(zone_to_borough).isin(SOURCE_BOROUGHS)
    keep = in_month & valid_source

    work = pd.DataFrame(
        {
            "pickup": pickup[keep],
            "pulocationid": pu[keep].astype(int),
            "dolocationid": do[keep].astype("Int64"),
        }
    )

    day = work["pickup"].dt.floor("D")
    work["week_start"] = day - pd.to_timedelta(work["pickup"].dt.dayofweek, unit="D")
    work["how"] = work["pickup"].dt.dayofweek * 24 + work["pickup"].dt.hour
    work["dest_macro"] = (
        work["dolocationid"].map(zone_to_borough).fillna("UNMAPPED").astype(str)
    )

    agg = (
        work.groupby(
            ["week_start", "how", "pulocationid", "dest_macro"],
            observed=True,
        )
        .size()
        .rename("n")
        .reset_index()
    )

    meta = {
        "year": year,
        "month": month,
        "raw_rows": int(n_raw),
        "rows_in_declared_month": int(in_month.sum()),
        "rows_valid_source_zone": int(keep.sum()),
        "rows_excluded": int(n_raw - keep.sum()),
    }
    return agg, meta


def frame_to_countdict(
    frame: pd.DataFrame,
    dest_classes: list[str],
) -> dict[tuple[int, int], np.ndarray]:
    dindex = {b: k for k, b in enumerate(dest_classes)}
    J = len(dest_classes)
    out: dict[tuple[int, int], np.ndarray] = {}

    if frame.empty:
        return out

    for (how, i), g in frame.groupby(["how", "pulocationid"], observed=True):
        y = np.zeros(J, dtype=float)
        for row in g.itertuples(index=False):
            y[dindex[row.dest_macro]] += float(row.n)
        out[(int(how), int(i))] = y

    return out


def add_countdicts(
    dicts: list[dict[tuple[int, int], np.ndarray]],
) -> dict[tuple[int, int], np.ndarray]:
    out: dict[tuple[int, int], np.ndarray] = {}
    for d in dicts:
        for key, arr in d.items():
            if key not in out:
                out[key] = arr.copy()
            else:
                out[key] += arr
    return out


def probs_from_counts(
    counts: dict[tuple[int, int], np.ndarray],
    J: int,
) -> dict[tuple[int, int], np.ndarray]:
    out: dict[tuple[int, int], np.ndarray] = {}
    for key, y in counts.items():
        total = float(y.sum())
        out[key] = (y + ALPHA) / (total + ALPHA * J)
    return out


def score_week(
    target_counts: dict[tuple[int, int], np.ndarray],
    p_recent: dict[tuple[int, int], np.ndarray],
    p_stale: dict[tuple[int, int], np.ndarray],
    p_frozen: dict[tuple[int, int], np.ndarray],
    J: int,
) -> dict:
    uniform = np.full(J, 1.0 / J)
    ll_r = 0.0
    ll_s = 0.0
    ll_f = 0.0
    drift_rs_num = 0.0
    drift_rf_num = 0.0
    unseen_r = 0.0
    unseen_s = 0.0
    unseen_f = 0.0
    N = 0.0

    for key, y in target_counts.items():
        n = float(y.sum())
        if n <= 0:
            continue

        pr = p_recent.get(key, uniform)
        ps = p_stale.get(key, uniform)
        pf = p_frozen.get(key, uniform)

        ll_r += float(-np.sum(y * np.log(pr)))
        ll_s += float(-np.sum(y * np.log(ps)))
        ll_f += float(-np.sum(y * np.log(pf)))

        drift_rs_num += n * float(np.sum(pr * np.log(pr / ps)))
        drift_rf_num += n * float(np.sum(pr * np.log(pr / pf)))

        if key not in p_recent:
            unseen_r += n
        if key not in p_stale:
            unseen_s += n
        if key not in p_frozen:
            unseen_f += n

        N += n

    if N <= 0:
        raise ValueError("Target week contains no scored trips.")

    Lr = ll_r / N
    Ls = ll_s / N
    Lf = ll_f / N
    return {
        "N": int(N),
        "L_recent": float(Lr),
        "L_stale": float(Ls),
        "L_frozen": float(Lf),
        "gain_rs": float(Ls - Lr),
        "gain_rf": float(Lf - Lr),
        "drift_rs": float(drift_rs_num / N),
        "drift_rf": float(drift_rf_num / N),
        "unseen_recent": int(unseen_r),
        "unseen_stale": int(unseen_s),
        "unseen_frozen": int(unseen_f),
    }


def aggregate_metrics(weekly: pd.DataFrame) -> dict:
    N = weekly["N"].to_numpy(float)
    g_rs = weekly["gain_rs"].to_numpy(float)
    g_rf = weekly["gain_rf"].to_numpy(float)
    d_rs = weekly["drift_rs"].to_numpy(float)
    d_rf = weekly["drift_rf"].to_numpy(float)

    total = float(N.sum())
    G_rs = float(np.sum(N * g_rs) / total)
    G_rf = float(np.sum(N * g_rf) / total)

    den_rs = float(np.sum(N * d_rs * d_rs))
    den_rf = float(np.sum(N * d_rf * d_rf))

    beta_rs = float(np.sum(N * d_rs * g_rs) / den_rs) if den_rs > 0 else float("nan")
    beta_rf = float(np.sum(N * d_rf * g_rf) / den_rf) if den_rf > 0 else float("nan")

    return {
        "n_trips": int(total),
        "n_target_weeks": int(len(weekly)),
        "logloss_recent": float(np.sum(N * weekly["L_recent"].to_numpy(float)) / total),
        "logloss_stale": float(np.sum(N * weekly["L_stale"].to_numpy(float)) / total),
        "logloss_frozen": float(np.sum(N * weekly["L_frozen"].to_numpy(float)) / total),
        "gain_recent_vs_stale": G_rs,
        "gain_recent_vs_frozen": G_rf,
        "weighted_drift_rs": float(np.sum(N * d_rs) / total),
        "weighted_drift_rf": float(np.sum(N * d_rf) / total),
        "beta_rs": beta_rs,
        "beta_rf": beta_rf,
        "unseen_recent_fraction": float(weekly["unseen_recent"].sum() / total),
        "unseen_stale_fraction": float(weekly["unseen_stale"].sum() / total),
        "unseen_frozen_fraction": float(weekly["unseen_frozen"].sum() / total),
    }


def moving_block_bootstrap(
    weekly: pd.DataFrame,
    rng: np.random.Generator,
) -> dict:
    n = len(weekly)
    if n != 52:
        raise ValueError(f"Expected 52 target weeks, found {n}.")
    L = BOOT_BLOCK_WEEKS
    if n < L:
        raise ValueError("Not enough weeks for the declared block length.")

    N = weekly["N"].to_numpy(float)
    g_rs = weekly["gain_rs"].to_numpy(float)
    g_rf = weekly["gain_rf"].to_numpy(float)
    d_rs = weekly["drift_rs"].to_numpy(float)

    boot_g_rs = np.empty(N_BOOT, dtype=float)
    boot_g_rf = np.empty(N_BOOT, dtype=float)
    boot_beta_rs = np.empty(N_BOOT, dtype=float)

    max_start = n - L

    for r in range(N_BOOT):
        idx: list[int] = []
        while len(idx) < n:
            start = int(rng.integers(0, max_start + 1))
            idx.extend(range(start, start + L))
        idx_arr = np.asarray(idx[:n], dtype=int)

        Nb = N[idx_arr]
        grs = g_rs[idx_arr]
        grf = g_rf[idx_arr]
        drs = d_rs[idx_arr]

        total = float(Nb.sum())
        boot_g_rs[r] = float(np.sum(Nb * grs) / total)
        boot_g_rf[r] = float(np.sum(Nb * grf) / total)

        den = float(np.sum(Nb * drs * drs))
        boot_beta_rs[r] = (
            float(np.sum(Nb * drs * grs) / den)
            if den > 0
            else np.nan
        )

    beta_valid = boot_beta_rs[np.isfinite(boot_beta_rs)]
    return {
        "n_replicates": N_BOOT,
        "block_length_weeks": L,
        "seed": SEED,
        "ci95_gain_rs": [
            float(x)
            for x in np.quantile(boot_g_rs, [0.025, 0.975])
        ],
        "ci95_gain_rf": [
            float(x)
            for x in np.quantile(boot_g_rf, [0.025, 0.975])
        ],
        "ci95_beta_rs": [
            float(x)
            for x in np.quantile(beta_valid, [0.025, 0.975])
        ],
    }


def verdict(summary: dict, boot: dict) -> str:
    G_rs = float(summary["gain_recent_vs_stale"])
    lo_rs = float(boot["ci95_gain_rs"][0])
    beta = float(summary["beta_rs"])
    lo_beta = float(boot["ci95_beta_rs"][0])
    G_rf = float(summary["gain_recent_vs_frozen"])
    lo_rf = float(boot["ci95_gain_rf"][0])

    if G_rs <= 0:
        return "FAIL"
    if lo_rs <= 0:
        return "INCONCLUSIVE"
    if beta > 0 and lo_beta > 0 and G_rf > 0 and lo_rf > 0:
        return "PASS"
    return "PARTIAL"


def self_test() -> None:
    stationary = np.array([0.7, 0.3], dtype=float)
    y_stationary = np.array([700.0, 300.0])
    gain_stationary = float(
        np.sum(y_stationary * np.log(stationary / stationary))
        / y_stationary.sum()
    )
    drift_stationary = float(
        np.sum(stationary * np.log(stationary / stationary))
    )

    recent = np.array([0.2, 0.8], dtype=float)
    stale = np.array([0.8, 0.2], dtype=float)
    y_drift = np.array([200.0, 800.0])

    gain_drift = float(
        np.sum(y_drift * np.log(recent / stale))
        / y_drift.sum()
    )
    kl_drift = float(np.sum(recent * np.log(recent / stale)))

    assert abs(gain_stationary) <= 1e-15
    assert abs(drift_stationary) <= 1e-15
    assert gain_drift > 0
    assert kl_drift > 0

    for w in TARGET_WEEKS:
        r0 = w - pd.Timedelta(days=56)
        r1 = w
        s0 = w - pd.Timedelta(days=112)
        s1 = w - pd.Timedelta(days=56)
        assert (r1 - r0) == pd.Timedelta(days=56)
        assert (s1 - s0) == pd.Timedelta(days=56)
        assert s1 == r0
        assert r1 == w
        assert s1 <= w and r1 <= w

    assert TARGET_WEEKS[0] == pd.Timestamp("2024-01-01")
    assert TARGET_WEEKS[-1] == pd.Timestamp("2024-12-23")
    assert TARGET_WEEKS[-1] + pd.Timedelta(days=7) == TARGET_END

    print(
        json.dumps(
            {
                "self_test": "PASS",
                "stationary_gain": gain_stationary,
                "stationary_drift": drift_stationary,
                "drift_case_gain": gain_drift,
                "drift_case_kl": kl_drift,
                "target_weeks": len(TARGET_WEEKS),
            },
            indent=2,
        )
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=".p002-data")
    ap.add_argument("--output-dir", default="experiments/p002/results")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    # Frozen evaluation contract.
    assert len(TARGET_WEEKS) == 52
    assert TARGET_WEEKS[0] == pd.Timestamp("2024-01-01")
    assert TARGET_WEEKS[-1] == pd.Timestamp("2024-12-23")
    assert TARGET_END == pd.Timestamp("2024-12-30")

    data_dir = Path(args.data_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    zone_path = data_dir / "nyc_taxi_zones.json"
    download(ZONE_URL, zone_path)
    zone_to_borough, dest_classes = load_zone_lookup(zone_path)
    J = len(dest_classes)

    hashes: dict[str, str] = {
        "nyc_taxi_zones.json": sha256_file(zone_path)
    }
    monthly_meta: list[dict] = []

    frozen_frames: list[pd.DataFrame] = []
    adaptive_frames: list[pd.DataFrame] = []

    # Frozen P-001 law: Jan-Jun 2023.
    for month in FROZEN_2023_MONTHS:
        p = data_dir / f"yellow_tripdata_2023-{month:02d}.parquet"
        download(TRIP_URL.format(year=2023, month=month), p)
        hashes[p.name] = sha256_file(p)
        agg, meta = aggregate_month_weekly(
            p,
            2023,
            month,
            zone_to_borough,
        )
        frozen_frames.append(agg)
        monthly_meta.append(meta)

    # Adaptive history required before the first 2024 target week.
    for month in HISTORY_2023_MONTHS:
        p = data_dir / f"yellow_tripdata_2023-{month:02d}.parquet"
        download(TRIP_URL.format(year=2023, month=month), p)
        hashes[p.name] = sha256_file(p)
        agg, meta = aggregate_month_weekly(
            p,
            2023,
            month,
            zone_to_borough,
        )
        adaptive_frames.append(agg)
        monthly_meta.append(meta)

    # Untouched 2024 evaluation data.
    for month in EVAL_2024_MONTHS:
        p = data_dir / f"yellow_tripdata_2024-{month:02d}.parquet"
        download(TRIP_URL.format(year=2024, month=month), p)
        hashes[p.name] = sha256_file(p)
        agg, meta = aggregate_month_weekly(
            p,
            2024,
            month,
            zone_to_borough,
        )
        adaptive_frames.append(agg)
        monthly_meta.append(meta)

    frozen_all = pd.concat(frozen_frames, ignore_index=True)
    frozen_agg = (
        frozen_all.groupby(
            ["how", "pulocationid", "dest_macro"],
            observed=True,
        )["n"]
        .sum()
        .reset_index()
    )
    frozen_counts = frame_to_countdict(frozen_agg, dest_classes)
    p_frozen = probs_from_counts(frozen_counts, J)

    adaptive_all = pd.concat(adaptive_frames, ignore_index=True)
    adaptive_all = (
        adaptive_all.groupby(
            ["week_start", "how", "pulocationid", "dest_macro"],
            observed=True,
        )["n"]
        .sum()
        .reset_index()
    )

    # Only complete weeks needed by stale/recent/target windows are retained.
    earliest_needed = pd.Timestamp("2023-09-11")
    latest_needed_exclusive = TARGET_END
    adaptive_all = adaptive_all[
        (adaptive_all["week_start"] >= earliest_needed)
        & (adaptive_all["week_start"] < latest_needed_exclusive)
    ].copy()

    week_dicts: dict[pd.Timestamp, dict[tuple[int, int], np.ndarray]] = {}
    for week_start, g in adaptive_all.groupby("week_start", observed=True):
        week_dicts[pd.Timestamp(week_start)] = frame_to_countdict(
            g.drop(columns=["week_start"]),
            dest_classes,
        )

    weekly_rows: list[dict] = []

    for w in TARGET_WEEKS:
        recent_starts = tuple(
            w - pd.Timedelta(days=7 * k)
            for k in range(8, 0, -1)
        )
        stale_starts = tuple(
            w - pd.Timedelta(days=7 * k)
            for k in range(16, 8, -1)
        )

        assert recent_starts[0] == w - pd.Timedelta(days=56)
        assert recent_starts[-1] == w - pd.Timedelta(days=7)
        assert stale_starts[0] == w - pd.Timedelta(days=112)
        assert stale_starts[-1] == w - pd.Timedelta(days=63)

        missing_recent = [x for x in recent_starts if x not in week_dicts]
        missing_stale = [x for x in stale_starts if x not in week_dicts]
        if missing_recent or missing_stale:
            raise ValueError(
                f"Missing complete adaptive weeks for {w.date()}: "
                f"recent={missing_recent}, stale={missing_stale}"
            )
        if w not in week_dicts:
            raise ValueError(f"Missing target week {w.date()}")

        recent_counts = add_countdicts(
            [week_dicts[x] for x in recent_starts]
        )
        stale_counts = add_countdicts(
            [week_dicts[x] for x in stale_starts]
        )
        target_counts = week_dicts[w]

        p_recent = probs_from_counts(recent_counts, J)
        p_stale = probs_from_counts(stale_counts, J)

        row = score_week(
            target_counts,
            p_recent,
            p_stale,
            p_frozen,
            J,
        )
        row["week_start"] = w
        weekly_rows.append(row)

    weekly = pd.DataFrame(weekly_rows).sort_values("week_start").reset_index(drop=True)
    assert len(weekly) == 52

    summary = aggregate_metrics(weekly)
    rng = np.random.default_rng(SEED)
    boot = moving_block_bootstrap(weekly, rng)

    result = {
        "status": "P002_EVALUATION",
        "verdict": verdict(summary, boot),
        "protocol_version": "1.0",
        "alpha_jeffreys": ALPHA,
        "seed": SEED,
        "target_start": str(TARGET_START),
        "target_end_exclusive": str(TARGET_END),
        "recent_window_days": 56,
        "stale_window_days": 56,
        "frozen_period": ["2023-01-01", "2023-07-01"],
        "destination_classes": dest_classes,
        **summary,
        "bootstrap": boot,
    }

    (out_dir / "summary.json").write_text(
        json.dumps(result, indent=2, default=str) + "\n",
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
    weekly.to_csv(out_dir / "weekly_scores.csv", index=False)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
