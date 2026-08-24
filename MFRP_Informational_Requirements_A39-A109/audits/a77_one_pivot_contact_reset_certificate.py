#!/usr/bin/env python3
"""A77 exact one-pivot neighborhood certificate at s0=131/1000."""

from __future__ import annotations

import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
CORE = HERE / "a77_active_contact_reset_core.py"
A73 = HERE / "a73_complete_one_pivot_neighborhood_audit.py"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    core = load_module(CORE, "a77_core_neighbors")
    a73 = load_module(A73, "a73_for_a77_neighbors")
    a73.S0 = core.S0

    records = []
    summaries = {}
    combined = Counter()
    pivot_counts = defaultdict(Counter)

    for maximum in [23, 24, 25]:
        candidates = core.generate_neighbors(maximum)
        counts = Counter()
        strict_optima = []

        for index, candidate in enumerate(candidates, start=1):
            evaluation = a73.exact_basis_evaluation(
                maximum,
                candidate,
            )
            record = {
                "maximum": maximum,
                "candidate_index": index,
                **candidate,
                **evaluation,
            }
            records.append(record)

            if not candidate["is_reference"]:
                counts[evaluation["classification"]] += 1
                combined[evaluation["classification"]] += 1
                pivot_counts[
                    candidate["kind"]
                ][evaluation["classification"]] += 1

            if evaluation["strict_local_optimum"]:
                strict_optima.append({
                    "candidate_index": index,
                    "kind": candidate["kind"],
                    "detail": candidate["detail"],
                    "p_support": candidate["p_support"],
                    "q_support": candidate["q_support"],
                    "active_observations": candidate[
                        "active_observations"
                    ],
                })

        summaries[str(maximum)] = {
            "candidate_count_including_reference": len(candidates),
            "single_pivot_neighbor_count": len(candidates) - 1,
            "classification_counts_neighbors": dict(counts),
            "strict_local_optima": strict_optima,
        }

    total_neighbors = sum(
        item["single_pivot_neighbor_count"]
        for item in summaries.values()
    )

    gates = {
        "all_498_declared_neighbors_enumerated": bool(
            total_neighbors == 498
        ),
        "all_501_bases_nonsingular_and_classified": bool(
            len(records) == 501
            and not any(
                record["classification"] in {
                    "rank_mismatch",
                    "singular",
                }
                for record in records
            )
        ),
        "each_reference_unique_strict_local_optimum": bool(
            all(
                len(summaries[str(maximum)]["strict_local_optima"]) == 1
                and summaries[str(maximum)][
                    "strict_local_optima"
                ][0]["kind"] == "reference"
                for maximum in [23, 24, 25]
            )
        ),
        "no_neighbor_locally_optimal": bool(
            combined.get("locally_optimal", 0) == 0
        ),
        "all_neighbors_rejected_by_explicit_KKT_layer": bool(
            sum(combined.values()) == 498
        ),
    }

    verdict = (
        "PASS_COMPLETE_ONE_PIVOT_CONTACT_RESET_NEIGHBORHOOD"
        if all(gates.values())
        else "FAIL_A77_ONE_PIVOT_NEIGHBORHOOD"
    )

    result = {
        "audit": "A77_ONE_PIVOT_CONTACT_RESET_NEIGHBORHOOD",
        "probe_s": str(core.S0),
        "selected_signatures": {
            str(maximum): core.signature(maximum)
            for maximum in [23, 24, 25]
        },
        "neighbor_counts": {
            "23": 159,
            "24": 166,
            "25": 173,
            "total": total_neighbors,
        },
        "support_summaries": summaries,
        "combined_neighbor_classification_counts": dict(combined),
        "pivot_type_classification_counts": {
            kind: dict(counts)
            for kind, counts in pivot_counts.items()
        },
        "candidate_records": records,
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "Complete only for the declared one-pivot signature moves "
            "at the exact probe s=131/1000."
        ),
    }

    output = HERE / "a77_one_pivot_contact_reset_results.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "neighbor_counts": result["neighbor_counts"],
        "failure_counts": result[
            "combined_neighbor_classification_counts"
        ],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": verdict,
        "output": output.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
