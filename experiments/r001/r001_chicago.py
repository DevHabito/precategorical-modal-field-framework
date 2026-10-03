from __future__ import annotations

import argparse
import hashlib
import io
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

API_URL = "https://data.cityofchicago.org/resource/sa9s-wkhk.csv"
PAGE_SIZE = 50000
ALPHA = 0.5
SEED = 20261003
N_BOOT = 10000
BOOT_BLOCK_WEEKS = 8

DEST_CLASSES = tuple(str(i) for i in range(1, 78)) + ("UNMAPPED",)
J = len(DEST_CLASSES)
DEST_INDEX = {b: i for i, b in enumerate(DEST_CLASSES)}

TARGET_START = pd.Timestamp("2024-04-22")
TARGET_WEEKS = tuple(
    TARGET_START + pd.Timedelta(days=7 * k)
    for k in range(36)
)
TARGET_END = pd.Timestamp("2024-12-30")

QUERY_START = pd.Timestamp("2024-01-01")
QUERY_END = TARGET_END

PERMITTED_COLUMNS = (
    "trip_id",
    "trip_start_timestamp",
    "pickup_community_area",
    "dropoff_community_area",
)


def source_area(value) -> int | None:
    try:
        x = int(float(value))
    except (TypeError, ValueError):
        return None
    return x if 1 <= x <= 77 else None


def dest_label(value) -> str:
    try:
        x = int(float(value))
    except (TypeError, ValueError):
        return "UNMAPPED"
    return str(x) if 1 <= x <= 77 else "UNMAPPED"


def add_vector(
    store: dict[pd.Timestamp, dict[tuple[int, int], np.ndarray]],
    week: pd.Timestamp,
    key: tuple[int, int],
    dest: str,
    n: float,
) -> None:
    if week not in store:
        store[week] = {}
    if key not in store[week]:
        store[week][key] = np.zeros(J, dtype=float)
    store[week][key][DEST_INDEX[dest]] += float(n)


def fetch_pages(
    cache_dir: Path,
) -> tuple[
    dict[pd.Timestamp, dict[tuple[int, int], np.ndarray]],
    dict,
]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "R001-chicago-replication/1.0"})

    where = (
        "trip_start_timestamp >= '2024-01-01T00:00:00.000' "
        "AND trip_start_timestamp < '2024-12-30T00:00:00.000'"
    )

    weekly: dict[pd.Timestamp, dict[tuple[int, int], np.ndarray]] = {}
    canonical_hash = hashlib.sha256()

    offset = 0
    pages = 0
    raw_rows = 0
    accepted_rows = 0
    excluded_missing_or_invalid_source = 0
    excluded_bad_timestamp = 0

    while True:
        params = {
            "$select": ",".join(PERMITTED_COLUMNS),
            "$where": where,
            "$order": "trip_start_timestamp,trip_id",
            "$limit": PAGE_SIZE,
            "$offset": offset,
        }

        last_error = None
        for attempt in range(5):
            try:
                resp = session.get(API_URL, params=params, timeout=120)
                resp.raise_for_status()
                last_error = None
                break
            except requests.RequestException as exc:
                last_error = exc
                time.sleep(2 ** attempt)

        if last_error is not None:
            raise RuntimeError(
                f"Chicago API failed at offset {offset}"
            ) from last_error

        if pages == 0:
            header = resp.text.splitlines()[0] if resp.text else ""
            got = tuple(x.strip('"') for x in header.split(","))
            if got != PERMITTED_COLUMNS:
                raise ValueError(
                    "Unexpected Chicago API schema. "
                    f"Expected {PERMITTED_COLUMNS}, got {got}."
                )

        page = pd.read_csv(io.StringIO(resp.text), dtype=str)
        if page.empty:
            break

        missing = [c for c in PERMITTED_COLUMNS if c not in page.columns]
        if missing:
            raise ValueError(f"Missing API fields: {missing}")

        pages += 1
        raw_rows += len(page)

        ts = pd.to_datetime(page["trip_start_timestamp"], errors="coerce")
        pu = page["pickup_community_area"].map(source_area)

        good_ts = ts.notna() & (ts >= QUERY_START) & (ts < QUERY_END)
        valid_source = pu.notna()

        excluded_bad_timestamp += int((~good_ts).sum())
        excluded_missing_or_invalid_source += int((good_ts & ~valid_source).sum())

        keep = good_ts & valid_source
        accepted = page.loc[keep, list(PERMITTED_COLUMNS)].copy()
        accepted_ts = ts[keep]
        accepted_pu = pu[keep].astype(int)

        accepted_rows += len(accepted)

        # Canonical accepted-row digest in deterministic API order.
        canonical_bytes = (
            accepted.fillna("")
            .astype(str)
            .to_csv(index=False, header=False, lineterminator="\n")
            .encode("utf-8")
        )
        canonical_hash.update(canonical_bytes)

        work = pd.DataFrame(
            {
                "ts": accepted_ts.to_numpy(),
                "pickup": accepted_pu.to_numpy(),
                "dropoff": accepted["dropoff_community_area"].map(dest_label).to_numpy(),
            }
        )
        day = work["ts"].dt.floor("D")
        work["week_start"] = day - pd.to_timedelta(work["ts"].dt.dayofweek, unit="D")
        work["how"] = work["ts"].dt.dayofweek * 24 + work["ts"].dt.hour

        agg = (
            work.groupby(
                ["week_start", "how", "pickup", "dropoff"],
                observed=True,
            )
            .size()
            .rename("n")
            .reset_index()
        )

        for row in agg.itertuples(index=False):
            add_vector(
                weekly,
                pd.Timestamp(row.week_start),
                (int(row.how), int(row.pickup)),
                str(row.dropoff),
                float(row.n),
            )

        if len(page) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    meta = {
        "api_url": API_URL,
        "query_start": str(QUERY_START),
        "query_end_exclusive": str(QUERY_END),
        "page_size": PAGE_SIZE,
        "pages": pages,
        "raw_rows_returned": raw_rows,
        "accepted_source_rows": accepted_rows,
        "excluded_missing_or_invalid_source": excluded_missing_or_invalid_source,
        "excluded_bad_timestamp": excluded_bad_timestamp,
        "accepted_rows_sha256": canonical_hash.hexdigest(),
    }

    return weekly, meta


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
) -> dict:
    uniform = np.full(J, 1.0 / J)
    ll_r = 0.0
    ll_s = 0.0
    drift_num = 0.0
    unseen_r = 0.0
    unseen_s = 0.0
    N = 0.0

    for key, y in target_counts.items():
        n = float(y.sum())
        if n <= 0:
            continue

        pr = p_recent.get(key, uniform)
        ps = p_stale.get(key, uniform)

        ll_r += float(-np.sum(y * np.log(pr)))
        ll_s += float(-np.sum(y * np.log(ps)))
        drift_num += n * float(np.sum(pr * np.log(pr / ps)))

        if key not in p_recent:
            unseen_r += n
        if key not in p_stale:
            unseen_s += n
        N += n

    if N <= 0:
        raise ValueError("Target week contains no accepted trips.")

    Lr = ll_r / N
    Ls = ll_s / N
    return {
        "N": int(N),
        "L_recent": float(Lr),
        "L_stale": float(Ls),
        "gain_rs": float(Ls - Lr),
        "drift_rs": float(drift_num / N),
        "unseen_recent": int(unseen_r),
        "unseen_stale": int(unseen_s),
    }


def centered_weighted_slope(
    N: np.ndarray,
    D: np.ndarray,
    G: np.ndarray,
) -> float:
    total = float(N.sum())
    mean_d = float(np.sum(N * D) / total)
    mean_g = float(np.sum(N * G) / total)

    num = float(np.sum(N * (D - mean_d) * (G - mean_g)))
    den = float(np.sum(N * (D - mean_d) ** 2))
    return num / den if den > 0 else float("nan")


def aggregate_metrics(weekly: pd.DataFrame) -> dict:
    N = weekly["N"].to_numpy(float)
    G = weekly["gain_rs"].to_numpy(float)
    D = weekly["drift_rs"].to_numpy(float)
    total = float(N.sum())

    return {
        "n_trips": int(total),
        "n_target_weeks": int(len(weekly)),
        "logloss_recent": float(np.sum(N * weekly["L_recent"].to_numpy(float)) / total),
        "logloss_stale": float(np.sum(N * weekly["L_stale"].to_numpy(float)) / total),
        "gain_recent_vs_stale": float(np.sum(N * G) / total),
        "weighted_drift_rs": float(np.sum(N * D) / total),
        "centered_slope": float(centered_weighted_slope(N, D, G)),
        "unseen_recent_fraction": float(weekly["unseen_recent"].sum() / total),
        "unseen_stale_fraction": float(weekly["unseen_stale"].sum() / total),
    }


def moving_block_bootstrap(
    weekly: pd.DataFrame,
    rng: np.random.Generator,
) -> dict:
    n = len(weekly)
    if n != 36:
        raise ValueError(f"Expected 36 target weeks, found {n}.")

    L = BOOT_BLOCK_WEEKS
    N = weekly["N"].to_numpy(float)
    G = weekly["gain_rs"].to_numpy(float)
    D = weekly["drift_rs"].to_numpy(float)

    boot_gain = np.empty(N_BOOT, dtype=float)
    boot_slope = np.empty(N_BOOT, dtype=float)

    max_start = n - L

    for r in range(N_BOOT):
        idx: list[int] = []
        while len(idx) < n:
            start = int(rng.integers(0, max_start + 1))
            idx.extend(range(start, start + L))

        idx_arr = np.asarray(idx[:n], dtype=int)
        Nb = N[idx_arr]
        Gb = G[idx_arr]
        Db = D[idx_arr]

        boot_gain[r] = float(np.sum(Nb * Gb) / np.sum(Nb))
        boot_slope[r] = centered_weighted_slope(Nb, Db, Gb)

    slope_valid = boot_slope[np.isfinite(boot_slope)]

    return {
        "n_replicates": N_BOOT,
        "block_length_weeks": L,
        "seed": SEED,
        "ci95_gain_rs": [
            float(x)
            for x in np.quantile(boot_gain, [0.025, 0.975])
        ],
        "ci95_centered_slope": [
            float(x)
            for x in np.quantile(slope_valid, [0.025, 0.975])
        ],
    }


def verdict(summary: dict, bootstrap: dict) -> str:
    gain = float(summary["gain_recent_vs_stale"])
    lo = float(bootstrap["ci95_gain_rs"][0])

    if gain <= 0:
        return "FAILED_REPLICATION"
    if lo > 0:
        return "REPLICATED"
    return "INCONCLUSIVE"


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

    N = np.ones(4)
    D = np.array([1.0, 2.0, 3.0, 4.0])
    G = np.array([0.5, 1.0, 1.5, 2.0])
    slope = centered_weighted_slope(N, D, G)

    assert abs(gain_stationary) <= 1e-15
    assert abs(drift_stationary) <= 1e-15
    assert gain_drift > 0
    assert kl_drift > 0
    assert slope > 0

    for w in TARGET_WEEKS:
        recent_starts = tuple(
            w - pd.Timedelta(days=7 * k)
            for k in range(8, 0, -1)
        )
        stale_starts = tuple(
            w - pd.Timedelta(days=7 * k)
            for k in range(16, 8, -1)
        )
        assert len(recent_starts) == 8
        assert len(stale_starts) == 8
        assert recent_starts[0] == w - pd.Timedelta(days=56)
        assert recent_starts[-1] == w - pd.Timedelta(days=7)
        assert stale_starts[0] == w - pd.Timedelta(days=112)
        assert stale_starts[-1] == w - pd.Timedelta(days=63)

    assert TARGET_WEEKS[0] == pd.Timestamp("2024-04-22")
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
                "centered_slope_test": slope,
                "target_weeks": len(TARGET_WEEKS),
            },
            indent=2,
        )
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache-dir", default=".r001-cache")
    ap.add_argument("--output-dir", default="experiments/r001/results")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    assert len(TARGET_WEEKS) == 36
    assert TARGET_WEEKS[0] == pd.Timestamp("2024-04-22")
    assert TARGET_WEEKS[-1] == pd.Timestamp("2024-12-23")
    assert TARGET_END == pd.Timestamp("2024-12-30")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    week_dicts, source_meta = fetch_pages(Path(args.cache_dir))

    required_history = tuple(
        pd.Timestamp("2024-01-01") + pd.Timedelta(days=7 * k)
        for k in range(52)
    )

    missing = [w for w in required_history if w not in week_dicts]
    if missing:
        raise ValueError(
            "Missing complete Chicago weeks required by the protocol: "
            + ", ".join(str(x.date()) for x in missing)
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

        recent_counts = add_countdicts(
            [week_dicts[x] for x in recent_starts]
        )
        stale_counts = add_countdicts(
            [week_dicts[x] for x in stale_starts]
        )

        p_recent = probs_from_counts(recent_counts)
        p_stale = probs_from_counts(stale_counts)

        row = score_week(
            week_dicts[w],
            p_recent,
            p_stale,
        )
        row["week_start"] = w
        weekly_rows.append(row)

    weekly = (
        pd.DataFrame(weekly_rows)
        .sort_values("week_start")
        .reset_index(drop=True)
    )

    summary = aggregate_metrics(weekly)
    rng = np.random.default_rng(SEED)
    bootstrap = moving_block_bootstrap(weekly, rng)

    result = {
        "status": "R001_EXTERNAL_REPLICATION",
        "verdict": verdict(summary, bootstrap),
        "protocol_version": "1.0",
        "dataset": "City of Chicago Taxi Trips - 2024",
        "dataset_id": "sa9s-wkhk",
        "alpha_jeffreys": ALPHA,
        "destination_classes": J,
        "target_start": str(TARGET_START),
        "target_end_exclusive": str(TARGET_END),
        "recent_window_days": 56,
        "stale_window_days": 56,
        **summary,
        "bootstrap": bootstrap,
        "source_audit": source_meta,
    }

    (out_dir / "summary.json").write_text(
        json.dumps(result, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    weekly.to_csv(out_dir / "weekly_scores.csv", index=False)
    (out_dir / "source_audit.json").write_text(
        json.dumps(source_meta, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
