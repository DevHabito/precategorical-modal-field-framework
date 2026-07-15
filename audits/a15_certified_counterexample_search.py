#!/usr/bin/env python3
"""
A15 — Certified Counterexample Search for the A14 Signature

Goal
----
Test whether the covariance-aware interval-abundance statistic from A14 is
sufficient for 1+1-dimensional Minkowski embeddability.

Construction
------------
Start with a genuine 2D Minkowski-order core and insert one or more disjoint
copies of the six-element standard example S_3:

    a_i < b_j  iff  i != j,  i,j in {0,1,2}.

S_3 has order dimension three. Because dimension is monotone under induced
subposets, any poset containing an induced S_3 cannot be a 2D order and hence
cannot be represented as a finite causal order in 1+1 Minkowski light-cone
coordinates.

To avoid a trivial density mismatch, core vertices are divided by their
Minkowski height into:
    - a prefix placed before every gadget element;
    - a middle sector incomparable with the gadgets;
    - a suffix placed after every gadget element.

The prefix/suffix cut is selected only to match the ordering fraction of an
independent paired Minkowski sprinkling. It is never selected using Q.

Prospective sizes
-----------------
Discovery: n = 96, 128
Prospective confirmation: n = 192

For each n, independent Minkowski samples are used for covariance estimation,
calibration, and holdout validation. No constructed adversary contributes to
the A14 model or threshold.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

from a13_analytic_interval_signature import (
    analytic_expectation,
    empirical_p_value,
    interval_abundance,
    relation_fraction,
    sample_minkowski_2d,
    wilson_interval,
)
from a14_covariance_interval_signature import (
    bin_vector,
    make_bins,
    quadratic_score,
)


SEED = 20260715
DISCOVERY_N = (96, 128)
CONFIRMATORY_N = 192
N_VALUES = DISCOVERY_N + (CONFIRMATORY_N,)

COVARIANCE_SAMPLES = 220
CALIBRATION_SAMPLES = 220
HOLDOUT_SAMPLES = 60

CANDIDATES_PER_GADGET_COUNT = 60
GADGET_COUNTS = (1, 2, 3)

ALPHA = 0.05
MAX_ORDERING_FRACTION_MISMATCH = 0.02


def json_safe(value):
    if isinstance(value, dict):
        return {
            str(key): json_safe(item)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def linear_extensions(relation: np.ndarray) -> list[tuple[int, ...]]:
    n = relation.shape[0]
    extensions = []

    for permutation in itertools.permutations(range(n)):
        position = np.empty(n, dtype=int)
        position[list(permutation)] = np.arange(n)

        if all(
            position[i] < position[j]
            for i, j in np.argwhere(relation)
        ):
            extensions.append(permutation)

    return extensions


def intersection_of_orders(
    first: tuple[int, ...],
    second: tuple[int, ...],
) -> np.ndarray:
    n = len(first)
    first_position = np.empty(n, dtype=int)
    second_position = np.empty(n, dtype=int)
    first_position[list(first)] = np.arange(n)
    second_position[list(second)] = np.arange(n)

    relation = (
        (first_position[:, None] < first_position[None, :])
        & (
            second_position[:, None]
            < second_position[None, :]
        )
    )
    np.fill_diagonal(relation, False)
    return relation


def is_dimension_at_most_two(relation: np.ndarray) -> bool:
    extensions = linear_extensions(relation)

    for first_index, first in enumerate(extensions):
        for second in extensions[first_index:]:
            if np.array_equal(
                intersection_of_orders(first, second),
                relation,
            ):
                return True

    return False


def standard_example_s3() -> np.ndarray:
    relation = np.zeros((6, 6), dtype=bool)

    for i in range(3):
        for j in range(3):
            if i != j:
                relation[i, 3 + j] = True

    return relation


def self_tests() -> dict[str, bool]:
    chain = np.triu(np.ones((6, 6), dtype=bool), k=1)
    antichain = np.zeros((6, 6), dtype=bool)
    s3 = standard_example_s3()

    return {
        "chain_dimension_at_most_two": (
            is_dimension_at_most_two(chain)
        ),
        "antichain_dimension_at_most_two": (
            is_dimension_at_most_two(antichain)
        ),
        "s3_not_dimension_at_most_two": (
            not is_dimension_at_most_two(s3)
        ),
    }


def sample_minkowski_core(
    n: int,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Return a 2D Minkowski order sorted by h=(u+v)/2. If x<y, h_x<h_y,
    so prefixes and suffixes respect the causal direction.
    """
    u = rng.random(n)
    v = rng.random(n)
    height = 0.5 * (u + v)
    order = np.argsort(height)
    u = u[order]
    v = v[order]

    relation = (
        (u[:, None] < u[None, :])
        & (v[:, None] < v[None, :])
    )
    np.fill_diagonal(relation, False)
    return relation, height[order]


def choose_density_matching_cuts(
    core_relation: np.ndarray,
    total_n: int,
    gadget_count: int,
    target_fraction: float,
) -> tuple[int, int, float]:
    core_n = core_relation.shape[0]
    gadget_vertices = 6 * gadget_count
    target_count = (
        target_fraction * total_n * (total_n - 1) / 2.0
    )
    core_count = int(core_relation.sum())

    maximum_cut = core_n // 2
    best = None

    for prefix_size in range(maximum_cut + 1):
        maximum_suffix = min(
            maximum_cut,
            core_n - prefix_size,
        )

        for suffix_size in range(maximum_suffix + 1):
            if prefix_size and suffix_size:
                existing_prefix_suffix = int(
                    core_relation[
                        :prefix_size,
                        core_n - suffix_size :,
                    ].sum()
                )
            else:
                existing_prefix_suffix = 0

            total_count = (
                core_count
                + gadget_vertices * prefix_size
                + gadget_vertices * suffix_size
                + 6 * gadget_count
                + prefix_size * suffix_size
                - existing_prefix_suffix
            )
            error = abs(total_count - target_count)

            # Tie-break toward smaller external deformation.
            deformation = prefix_size + suffix_size
            candidate = (
                error,
                deformation,
                abs(prefix_size - suffix_size),
                prefix_size,
                suffix_size,
                total_count,
            )

            if best is None or candidate < best:
                best = candidate

    assert best is not None
    _, _, _, prefix_size, suffix_size, count = best
    achieved_fraction = (
        count / (total_n * (total_n - 1) / 2.0)
    )
    return (
        int(prefix_size),
        int(suffix_size),
        float(achieved_fraction),
    )


def build_s3_sandwich(
    total_n: int,
    gadget_count: int,
    target_fraction: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, dict[str, object]]:
    gadget_vertices = 6 * gadget_count
    core_n = total_n - gadget_vertices

    if core_n <= 0:
        raise ValueError("The gadget exceeds the total size.")

    core_relation, _ = sample_minkowski_core(
        core_n,
        rng,
    )
    (
        prefix_size,
        suffix_size,
        achieved_fraction,
    ) = choose_density_matching_cuts(
        core_relation,
        total_n,
        gadget_count,
        target_fraction,
    )

    relation = np.zeros(
        (total_n, total_n),
        dtype=bool,
    )
    relation[:core_n, :core_n] = core_relation

    gadget_start = core_n
    gadget_indices = np.arange(
        gadget_start,
        total_n,
    )

    prefix = np.arange(prefix_size)
    suffix = np.arange(
        core_n - suffix_size,
        core_n,
    )

    if prefix_size:
        relation[np.ix_(prefix, gadget_indices)] = True

    if suffix_size:
        relation[np.ix_(gadget_indices, suffix)] = True

    if prefix_size and suffix_size:
        relation[np.ix_(prefix, suffix)] = True

    s3 = standard_example_s3()
    gadget_ranges = []

    for gadget_index in range(gadget_count):
        start = gadget_start + 6 * gadget_index
        stop = start + 6
        relation[start:stop, start:stop] = s3
        gadget_ranges.append((start, stop))

    metadata = {
        "core_n": core_n,
        "gadget_count": gadget_count,
        "gadget_vertex_fraction": (
            gadget_vertices / total_n
        ),
        "prefix_size": prefix_size,
        "suffix_size": suffix_size,
        "target_ordering_fraction": (
            target_fraction
        ),
        "achieved_ordering_fraction": (
            achieved_fraction
        ),
        "ordering_fraction_mismatch": abs(
            achieved_fraction - target_fraction
        ),
        "gadget_ranges": gadget_ranges,
    }
    return relation, metadata


def verify_induced_s3(
    relation: np.ndarray,
    gadget_ranges: list[tuple[int, int]],
) -> bool:
    target = standard_example_s3()

    return all(
        np.array_equal(
            relation[start:stop, start:stop],
            target,
        )
        for start, stop in gadget_ranges
    )


def verify_transitive(relation: np.ndarray) -> bool:
    two_step = (
        relation.astype(np.int16)
        @ relation.astype(np.int16)
    ) > 0
    return not bool(
        np.any(two_step & ~relation)
    )


def normalized_profile(
    relation: np.ndarray,
    bins: list[tuple[int, int]],
) -> np.ndarray:
    counts = interval_abundance(relation)
    return bin_vector(counts, bins) / counts.sum()


def fit_minkowski_model(
    n: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    expected_counts, analytic_full_profile = (
        analytic_expectation(n)
    )
    bins = make_bins(expected_counts)
    analytic_profile = bin_vector(
        analytic_full_profile,
        bins,
    )

    estimation_profiles = np.vstack(
        [
            normalized_profile(
                sample_minkowski_2d(n, rng),
                bins,
            )
            for _ in range(COVARIANCE_SAMPLES)
        ]
    )
    covariance_model = LedoitWolf().fit(
        estimation_profiles
    )
    precision = covariance_model.precision_
    covariance = covariance_model.covariance_

    calibration_profiles = np.vstack(
        [
            normalized_profile(
                sample_minkowski_2d(n, rng),
                bins,
            )
            for _ in range(CALIBRATION_SAMPLES)
        ]
    )
    calibration_scores = np.asarray(
        [
            quadratic_score(
                profile,
                analytic_profile,
                precision,
            )
            for profile in calibration_profiles
        ],
        dtype=float,
    )

    return {
        "bins": bins,
        "analytic_profile": analytic_profile,
        "precision": precision,
        "calibration_scores": calibration_scores,
        "condition_number": float(
            np.linalg.cond(covariance)
        ),
        "minimum_eigenvalue": float(
            np.linalg.eigvalsh(covariance).min()
        ),
        "shrinkage": float(
            covariance_model.shrinkage_
        ),
    }


def score_relation(
    relation: np.ndarray,
    model: dict[str, object],
) -> tuple[float, float]:
    profile = normalized_profile(
        relation,
        model["bins"],
    )
    score = quadratic_score(
        profile,
        model["analytic_profile"],
        model["precision"],
    )
    p_value = empirical_p_value(
        score,
        model["calibration_scores"],
    )
    return float(score), float(p_value)


def main() -> None:
    output = Path("a15_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)
    tests = self_tests()

    candidate_rows: list[dict[str, object]] = []
    holdout_rows: list[dict[str, object]] = []
    size_results: list[dict[str, object]] = []

    all_model_pass = True
    all_certificate_pass = all(tests.values())
    all_density_pass = True

    for n in N_VALUES:
        model = fit_minkowski_model(n, rng)

        holdout_relations = [
            sample_minkowski_2d(n, rng)
            for _ in range(HOLDOUT_SAMPLES)
        ]
        target_fractions = [
            relation_fraction(relation)
            for relation in holdout_relations
        ]

        holdout_acceptances = []

        for sample_index, relation in enumerate(
            holdout_relations
        ):
            score, p_value = score_relation(
                relation,
                model,
            )
            accepted = p_value >= ALPHA
            holdout_acceptances.append(accepted)
            holdout_rows.append(
                {
                    "n": n,
                    "sample_index": sample_index,
                    "q_score": score,
                    "p_value": p_value,
                    "accepted": accepted,
                    "ordering_fraction": (
                        target_fractions[sample_index]
                    ),
                }
            )

        holdout_acceptance_rate = float(
            np.mean(holdout_acceptances)
        )
        model_pass = (
            model["minimum_eigenvalue"] > 0.0
            and model["condition_number"] <= 1e8
            and holdout_acceptance_rate >= 0.90
        )
        all_model_pass &= model_pass

        gadget_summaries = []

        for gadget_count in GADGET_COUNTS:
            accepted_values = []
            p_values = []
            q_scores = []
            mismatches = []
            transitivity_checks = []
            certificate_checks = []

            for candidate_index in range(
                CANDIDATES_PER_GADGET_COUNT
            ):
                target = target_fractions[
                    candidate_index
                    % len(target_fractions)
                ]
                relation, metadata = build_s3_sandwich(
                    n,
                    gadget_count,
                    target,
                    rng,
                )

                certificate = verify_induced_s3(
                    relation,
                    metadata["gadget_ranges"],
                )
                # Full transitivity is checked for every candidate.
                transitive = verify_transitive(relation)

                score, p_value = score_relation(
                    relation,
                    model,
                )
                accepted = p_value >= ALPHA

                accepted_values.append(accepted)
                p_values.append(p_value)
                q_scores.append(score)
                mismatches.append(
                    metadata[
                        "ordering_fraction_mismatch"
                    ]
                )
                transitivity_checks.append(transitive)
                certificate_checks.append(certificate)

                candidate_rows.append(
                    {
                        "n": n,
                        "phase": (
                            "prospective_confirmation"
                            if n == CONFIRMATORY_N
                            else "discovery"
                        ),
                        "candidate_index": candidate_index,
                        "gadget_count": gadget_count,
                        "gadget_vertex_fraction": (
                            metadata[
                                "gadget_vertex_fraction"
                            ]
                        ),
                        "core_n": metadata["core_n"],
                        "prefix_size": (
                            metadata["prefix_size"]
                        ),
                        "suffix_size": (
                            metadata["suffix_size"]
                        ),
                        "target_ordering_fraction": (
                            metadata[
                                "target_ordering_fraction"
                            ]
                        ),
                        "ordering_fraction": (
                            relation_fraction(relation)
                        ),
                        "ordering_fraction_mismatch": (
                            metadata[
                                "ordering_fraction_mismatch"
                            ]
                        ),
                        "induced_s3_certificate": (
                            certificate
                        ),
                        "transitive": transitive,
                        "q_score": score,
                        "p_value": p_value,
                        "accepted_by_a14": accepted,
                    }
                )

            acceptance_rate = float(
                np.mean(accepted_values)
            )
            accepted_count = int(
                np.count_nonzero(accepted_values)
            )
            interval = wilson_interval(
                accepted_count,
                CANDIDATES_PER_GADGET_COUNT,
            )

            gadget_summaries.append(
                {
                    "gadget_count": gadget_count,
                    "gadget_vertex_fraction": (
                        6 * gadget_count / n
                    ),
                    "number_candidates": (
                        CANDIDATES_PER_GADGET_COUNT
                    ),
                    "accepted_count": accepted_count,
                    "acceptance_rate": acceptance_rate,
                    "acceptance_wilson_95": interval,
                    "median_p_value": float(
                        np.median(p_values)
                    ),
                    "maximum_p_value": float(
                        np.max(p_values)
                    ),
                    "median_q_score": float(
                        np.median(q_scores)
                    ),
                    "maximum_ordering_fraction_mismatch": (
                        float(np.max(mismatches))
                    ),
                    "all_transitive": all(
                        transitivity_checks
                    ),
                    "all_induced_s3_certified": all(
                        certificate_checks
                    ),
                }
            )

            all_certificate_pass &= (
                all(transitivity_checks)
                and all(certificate_checks)
            )
            all_density_pass &= (
                max(mismatches)
                <= MAX_ORDERING_FRACTION_MISMATCH
            )

        size_results.append(
            {
                "n": n,
                "phase": (
                    "prospective_confirmation"
                    if n == CONFIRMATORY_N
                    else "discovery"
                ),
                "number_bins": len(model["bins"]),
                "covariance_condition_number": (
                    model["condition_number"]
                ),
                "covariance_minimum_eigenvalue": (
                    model["minimum_eigenvalue"]
                ),
                "ledoit_wolf_shrinkage": (
                    model["shrinkage"]
                ),
                "holdout_minkowski_acceptance_rate": (
                    holdout_acceptance_rate
                ),
                "model_gate_pass": model_pass,
                "gadget_results": gadget_summaries,
            }
        )

    pd.DataFrame(candidate_rows).to_csv(
        output / "a15_candidate_scores.csv",
        index=False,
    )
    pd.DataFrame(holdout_rows).to_csv(
        output / "a15_holdout_scores.csv",
        index=False,
    )

    flat_summary_rows = []
    for result in size_results:
        for gadget in result["gadget_results"]:
            flat_summary_rows.append(
                {
                    "n": result["n"],
                    "phase": result["phase"],
                    "holdout_minkowski_acceptance_rate": (
                        result[
                            "holdout_minkowski_acceptance_rate"
                        ]
                    ),
                    **gadget,
                }
            )

    pd.DataFrame(flat_summary_rows).to_csv(
        output / "a15_size_gadget_summary.csv",
        index=False,
    )

    one_gadget_by_n = {
        result["n"]: next(
            gadget
            for gadget in result["gadget_results"]
            if gadget["gadget_count"] == 1
        )
        for result in size_results
    }

    discovery_systematic = all(
        one_gadget_by_n[n]["acceptance_rate"] >= 0.50
        for n in DISCOVERY_N
    )
    prospective_systematic = (
        one_gadget_by_n[CONFIRMATORY_N][
            "acceptance_rate"
        ]
        >= 0.50
    )
    prospective_any = (
        one_gadget_by_n[CONFIRMATORY_N][
            "accepted_count"
        ]
        > 0
    )

    monotonic_detection = True
    for result in size_results:
        rates = [
            gadget["acceptance_rate"]
            for gadget in result["gadget_results"]
        ]
        if not all(
            later <= earlier
            for earlier, later in zip(
                rates,
                rates[1:],
            )
        ):
            monotonic_detection = False

    gates = {
        "G1_s3_dimension_self_tests": all(
            tests.values()
        ),
        "G2_minkowski_model_and_holdout": (
            all_model_pass
        ),
        "G3_all_candidates_transitive_and_certified": (
            all_certificate_pass
        ),
        "G4_ordering_fraction_mismatch_le_0_02": (
            all_density_pass
        ),
        "G5_systematic_one_gadget_false_positives_discovery": (
            discovery_systematic
        ),
        "G6_systematic_one_gadget_false_positives_n192": (
            prospective_systematic
        ),
        "G7_at_least_one_prospective_counterexample": (
            prospective_any
        ),
        "G8_detection_non_decreasing_with_gadget_burden": (
            monotonic_detection
        ),
    }

    if prospective_systematic:
        verdict = (
            "SYSTEMATIC_CERTIFIED_COUNTEREXAMPLES_FOUND_"
            "A14_NOT_SUFFICIENT"
        )
    elif prospective_any:
        verdict = (
            "ISOLATED_CERTIFIED_COUNTEREXAMPLE_FOUND_"
            "A14_NOT_SUFFICIENT"
        )
    else:
        verdict = (
            "NO_CERTIFIED_COUNTEREXAMPLE_FOUND_IN_A15"
        )

    summary = {
        "seed": SEED,
        "discovery_n": list(DISCOVERY_N),
        "prospective_confirmation_n": CONFIRMATORY_N,
        "covariance_samples_per_n": (
            COVARIANCE_SAMPLES
        ),
        "calibration_samples_per_n": (
            CALIBRATION_SAMPLES
        ),
        "holdout_samples_per_n": HOLDOUT_SAMPLES,
        "candidates_per_gadget_count_per_n": (
            CANDIDATES_PER_GADGET_COUNT
        ),
        "gadget_counts": list(GADGET_COUNTS),
        "alpha": ALPHA,
        "certificate": (
            "Every adversary contains an induced S3 standard "
            "example. S3 has order dimension 3, so the full poset "
            "cannot be a 2D order or an exact finite 1+1 Minkowski "
            "causal order."
        ),
        "construction": (
            "Minkowski core plus density-matched S3 sandwich; "
            "prefix and suffix cuts are chosen only by ordering "
            "fraction, never by Q."
        ),
        "self_tests": tests,
        "size_results": size_results,
        "gates": gates,
        "verdict": verdict,
        "interpretation_boundary": (
            "Finding a certified counterexample proves that the "
            "tested A14 global interval-abundance statistic is not "
            "a sufficient condition for exact 1+1-dimensional "
            "Minkowski embeddability. It does not invalidate its "
            "value as a global necessary-signature test."
        ),
    }

    (output / "a15_summary.json").write_text(
        json.dumps(json_safe(summary), indent=2),
        encoding="utf-8",
    )

    report_lines = [
        "# A15 — Certified Counterexample Search",
        "",
        "## Construction",
        "",
        (
            "Each adversary contains one or more induced copies "
            "of the six-element standard example S3 inside a "
            "Minkowski-order core."
        ),
        (
            "The prefix/suffix placement is chosen only to match "
            "the ordering fraction of a paired independent "
            "Minkowski sprinkling."
        ),
        "",
        "## Results",
        "",
    ]

    for result in size_results:
        report_lines.extend(
            [
                f"### n = {result['n']} ({result['phase']})",
                "",
                (
                    "- Minkowski holdout acceptance: "
                    f"{result['holdout_minkowski_acceptance_rate']:.4f}"
                ),
            ]
        )
        for gadget in result["gadget_results"]:
            report_lines.extend(
                [
                    (
                        f"- {gadget['gadget_count']} S3 gadget(s): "
                        f"acceptance={gadget['acceptance_rate']:.4f}, "
                        f"accepted={gadget['accepted_count']}/"
                        f"{gadget['number_candidates']}, "
                        f"max p={gadget['maximum_p_value']:.4f}, "
                        "max density mismatch="
                        f"{gadget['maximum_ordering_fraction_mismatch']:.6f}"
                    ),
                ]
            )
        report_lines.append("")

    report_lines.extend(
        [
            "## Gates",
            "",
            *[
                f"- {key}: {'PASS' if value else 'FAIL'}"
                for key, value in gates.items()
            ],
            "",
            "## Verdict",
            "",
            verdict,
            "",
            "## Boundary",
            "",
            (
                "The result addresses sufficiency of the A14 "
                "global signature for exact 1+1 embeddability. "
                "It does not erase the prior evidence that Q is "
                "a strong global manifoldlikeness diagnostic."
            ),
        ]
    )

    (output / "a15_report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(json.dumps(json_safe(summary), indent=2))
    print()
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
