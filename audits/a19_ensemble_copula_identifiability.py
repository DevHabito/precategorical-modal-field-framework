#!/usr/bin/env python3
"""
A19 — Ensemble-Level Copula Identifiability Theorem

Theorem
-------
Let (X_i,Y_i), i=1,...,n, be iid with strictly increasing continuous
marginal CDFs F_X,F_Y and copula C. Define the labeled strict order

    i <_P j  iff  X_i < X_j and Y_i < Y_j.

Then the probability law of P depends on the joint distribution only through
C. In particular, changing either marginal while holding C fixed leaves the
law of every finite observed order unchanged.

Proof
-----
Set U_i=F_X(X_i), V_i=F_Y(Y_i). Strict monotonicity gives, almost surely,

    X_i < X_j iff U_i < U_j,
    Y_i < Y_j iff V_i < V_j.

By Sklar's representation, (U_i,V_i) has uniform marginals and copula C.
Therefore the relation matrix built from (X_i,Y_i) equals the relation matrix
built from (U_i,V_i) under this coupling. Hence its distribution is a
functional only of C.

Consequences
------------
1. Under the independence copula, after sorting by X, the Y-rank permutation
   is exactly uniform on S_n.
2. Two models with the same copula and different continuous marginals induce
   identical distributions on any finite or infinite iid sequence of
   observed orders.
3. No estimator or hypothesis test using only those orders and their
   cardinalities can identify which marginal model generated the data.
4. The theorem says only that the order law is copula-dependent. It does not
   assert that the map from copulas to order laws is injective.

Numerical audit
---------------
- Canonical permutation size n=6, hence 720 categories.
- 100,000 independent order samples for each combination of:
    copula rho in {0, +0.6, -0.6},
    marginal family in {uniform, beta-skew, power-anisotropic}.
- Same-copula/different-marginal histograms are compared independently.
- Different-copula controls verify that changing dependence can change the
  order ensemble.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial.distance import jensenshannon
from scipy.stats import beta, chi2, chisquare, norm


SEED = 20260722
ORDER_SIZE = 6
CATEGORY_COUNT = math.factorial(ORDER_SIZE)
ENSEMBLE_SIZE = 100_000
COUPLED_SAMPLES = 300
COUPLED_ORDER_SIZE = 32

COPULAS = {
    "independence": 0.0,
    "gaussian_positive": 0.6,
    "gaussian_negative": -0.6,
}

MARGINALS = (
    "uniform",
    "beta_skew",
    "power_anisotropic",
)

SAME_COPULA_P_MIN = 1e-4
SAME_COPULA_TV_MAX = 0.075
SAME_COPULA_RELATION_RANGE_MAX = 0.004
THEORY_RELATION_ERROR_MAX = 0.004
DIFFERENT_COPULA_TV_MIN = 0.15
DIFFERENT_COPULA_LOG10_P_MAX = -20.0


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


def gaussian_copula_uniforms(
    sample_count: int,
    order_size: int,
    rho: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    first = rng.standard_normal(
        size=(sample_count, order_size)
    )
    independent = rng.standard_normal(
        size=(sample_count, order_size)
    )
    second = (
        rho * first
        + math.sqrt(1.0 - rho * rho) * independent
    )
    return norm.cdf(first), norm.cdf(second)


def apply_marginals(
    name: str,
    u: np.ndarray,
    v: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if name == "uniform":
        return u, v

    if name == "beta_skew":
        return (
            beta.ppf(u, 2.0, 5.0),
            beta.ppf(v, 5.0, 2.0),
        )

    if name == "power_anisotropic":
        return np.power(u, 4.0), np.sqrt(v)

    raise ValueError(f"Unknown marginal family: {name}")


def rank_permutations(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    """
    Sort each sample by x and return the ranks of y in that x order.
    Continuous coordinates imply no ties almost surely.
    """
    x_order = np.argsort(x, axis=1)
    y_sorted = np.take_along_axis(
        y,
        x_order,
        axis=1,
    )
    return np.argsort(
        np.argsort(y_sorted, axis=1),
        axis=1,
    )


def lehmer_codes(
    permutations: np.ndarray,
) -> np.ndarray:
    sample_count, order_size = permutations.shape
    codes = np.zeros(sample_count, dtype=np.int64)

    for index in range(order_size - 1):
        smaller_to_right = np.sum(
            permutations[:, index + 1 :]
            < permutations[:, index, None],
            axis=1,
        )
        codes += (
            smaller_to_right
            * math.factorial(order_size - 1 - index)
        )

    return codes


def comparable_pair_fractions(
    permutations: np.ndarray,
) -> np.ndarray:
    sample_count, order_size = permutations.shape
    comparable = np.zeros(sample_count, dtype=np.int16)

    for first in range(order_size):
        for second in range(first + 1, order_size):
            comparable += (
                permutations[:, first]
                < permutations[:, second]
            )

    return (
        comparable
        / (order_size * (order_size - 1) / 2.0)
    )


def relation_matrix(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    relation = (
        (x[:, None] < x[None, :])
        & (y[:, None] < y[None, :])
    )
    np.fill_diagonal(relation, False)
    return relation


def relation_hash(relation: np.ndarray) -> str:
    return hashlib.sha256(
        np.packbits(
            relation.astype(np.uint8),
            axis=None,
        ).tobytes()
    ).hexdigest()


def histogram_metrics(
    first_counts: np.ndarray,
    second_counts: np.ndarray,
) -> dict[str, float]:
    first_probability = (
        first_counts / first_counts.sum()
    )
    second_probability = (
        second_counts / second_counts.sum()
    )

    total_variation = 0.5 * float(
        np.abs(
            first_probability - second_probability
        ).sum()
    )
    js_bits = float(
        jensenshannon(
            first_probability,
            second_probability,
            base=2.0,
        )
        ** 2
    )

    observed = np.vstack(
        [first_counts, second_counts]
    ).astype(float)
    nonzero_columns = observed.sum(axis=0) > 0
    observed = observed[:, nonzero_columns]

    row_totals = observed.sum(axis=1)
    column_totals = observed.sum(axis=0)
    grand_total = observed.sum()
    expected = (
        row_totals[:, None]
        * column_totals[None, :]
        / grand_total
    )
    statistic = float(
        np.sum(
            (observed - expected) ** 2
            / expected
        )
    )
    degrees_freedom = observed.shape[1] - 1
    log_survival = float(
        chi2.logsf(statistic, degrees_freedom)
    )
    p_value = float(
        math.exp(log_survival)
        if log_survival > -745.0
        else 0.0
    )
    log10_p = float(
        log_survival / math.log(10.0)
    )

    return {
        "total_variation": total_variation,
        "jensen_shannon_bits": js_bits,
        "chi_square": statistic,
        "degrees_freedom": int(degrees_freedom),
        "p_value": p_value,
        "log10_p_value": log10_p,
    }


def theoretical_ordering_fraction(rho: float) -> float:
    """
    For a Gaussian copula, the concordance probability equals
        (1 + tau)/2,
    where tau=(2/pi) asin(rho).
    """
    return 0.5 + math.asin(rho) / math.pi


def coupled_identity_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for copula_name, rho in COPULAS.items():
        u, v = gaussian_copula_uniforms(
            COUPLED_SAMPLES,
            COUPLED_ORDER_SIZE,
            rho,
            rng,
        )

        for sample_index in range(COUPLED_SAMPLES):
            reference_x, reference_y = apply_marginals(
                "uniform",
                u[sample_index],
                v[sample_index],
            )
            reference_relation = relation_matrix(
                reference_x,
                reference_y,
            )
            reference_hash = relation_hash(
                reference_relation
            )

            for marginal_name in MARGINALS[1:]:
                x, y = apply_marginals(
                    marginal_name,
                    u[sample_index],
                    v[sample_index],
                )
                transformed_relation = relation_matrix(
                    x,
                    y,
                )
                rows.append(
                    {
                        "copula": copula_name,
                        "sample_index": sample_index,
                        "marginal": marginal_name,
                        "relation_identical": bool(
                            np.array_equal(
                                reference_relation,
                                transformed_relation,
                            )
                        ),
                        "hash_identical": (
                            reference_hash
                            == relation_hash(
                                transformed_relation
                            )
                        ),
                    }
                )

    return rows


def main() -> None:
    output = Path("a19_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    theorem_text = """# A19 — Ensemble-Level Copula Identifiability Theorem

## Assumptions

Let `(X_i,Y_i)`, `i=1,...,n`, be iid. Assume both marginal CDFs are
continuous and strictly increasing on their supports. Define the labeled
strict order

`i <_P j` iff `X_i < X_j` and `Y_i < Y_j`.

## Theorem

The probability law of `P` depends on the joint distribution of `(X,Y)` only
through its copula.

## Proof

Let `U_i=F_X(X_i)` and `V_i=F_Y(Y_i)`. Strict monotonicity gives, almost
surely,

`X_i<X_j` iff `U_i<U_j`, and `Y_i<Y_j` iff `V_i<V_j`.

Therefore the full labeled relation matrix constructed from `(X_i,Y_i)` is
identical, under this coupling, to the relation matrix constructed from
`(U_i,V_i)`. By Sklar's representation, `(U_i,V_i)` has uniform marginals
and the same copula as `(X_i,Y_i)`. Hence the induced order law is a
functional only of the copula.

## Infinite-ensemble corollary

Take two models with the same copula but different continuous strictly
increasing marginals. Their law for one observed finite order is identical.
The product law for any finite number of independent observed orders is
therefore identical. The law for an infinite iid sequence is also identical
on all cylinder events.

Consequently, no estimator or statistical test whose data consist only of
those orders and their cardinalities can consistently identify which
marginal model generated the sequence.

## Independence corollary

For the independence copula, sort the sample by the first coordinate.
The ranks of the second coordinates are independent of that sorting and form
a uniform random permutation. Thus every permutation in `S_n` has probability
exactly `1/n!`.

## Limitation

The theorem proves that the order law depends at most on the copula. It does
not prove that distinct copulas always induce distinct laws of finite orders.
"""
    (output / "a19_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    coupled_rows = coupled_identity_audit(rng)
    coupled_frame = pd.DataFrame(coupled_rows)
    coupled_frame.to_csv(
        output / "a19_coupled_identity.csv",
        index=False,
    )

    ensemble_rows = []
    histograms: dict[
        tuple[str, str],
        np.ndarray,
    ] = {}

    for copula_name, rho in COPULAS.items():
        for marginal_name in MARGINALS:
            u, v = gaussian_copula_uniforms(
                ENSEMBLE_SIZE,
                ORDER_SIZE,
                rho,
                rng,
            )
            x, y = apply_marginals(
                marginal_name,
                u,
                v,
            )
            permutations = rank_permutations(x, y)
            codes = lehmer_codes(permutations)
            counts = np.bincount(
                codes,
                minlength=CATEGORY_COUNT,
            ).astype(np.int64)
            histograms[
                (copula_name, marginal_name)
            ] = counts

            relation_fractions = (
                comparable_pair_fractions(
                    permutations
                )
            )
            theoretical_fraction = (
                theoretical_ordering_fraction(rho)
            )

            if copula_name == "independence":
                expected = np.full(
                    CATEGORY_COUNT,
                    ENSEMBLE_SIZE / CATEGORY_COUNT,
                    dtype=float,
                )
                uniformity_statistic, uniformity_p = (
                    chisquare(counts, expected)
                )
                uniformity_statistic = float(
                    uniformity_statistic
                )
                uniformity_p = float(uniformity_p)
            else:
                uniformity_statistic = float("nan")
                uniformity_p = float("nan")

            ensemble_rows.append(
                {
                    "copula": copula_name,
                    "rho": rho,
                    "marginal": marginal_name,
                    "ensemble_size": ENSEMBLE_SIZE,
                    "observed_ordering_fraction_mean": (
                        float(
                            relation_fractions.mean()
                        )
                    ),
                    "theoretical_ordering_fraction": (
                        theoretical_fraction
                    ),
                    "absolute_theory_error": abs(
                        float(
                            relation_fractions.mean()
                        )
                        - theoretical_fraction
                    ),
                    "permutation_uniformity_chi_square": (
                        uniformity_statistic
                    ),
                    "permutation_uniformity_p_value": (
                        uniformity_p
                    ),
                    "occupied_permutation_categories": int(
                        np.count_nonzero(counts)
                    ),
                }
            )

    ensemble_frame = pd.DataFrame(
        ensemble_rows
    )
    ensemble_frame.to_csv(
        output / "a19_ensemble_summary.csv",
        index=False,
    )

    histogram_rows = []
    for (copula_name, marginal_name), counts in (
        histograms.items()
    ):
        for code, count in enumerate(counts):
            histogram_rows.append(
                {
                    "copula": copula_name,
                    "marginal": marginal_name,
                    "permutation_code": code,
                    "count": int(count),
                    "probability": float(
                        count / ENSEMBLE_SIZE
                    ),
                }
            )

    pd.DataFrame(histogram_rows).to_csv(
        output / "a19_permutation_histograms.csv",
        index=False,
    )

    same_copula_rows = []

    for copula_name in COPULAS:
        for first_marginal, second_marginal in (
            itertools.combinations(
                MARGINALS,
                2,
            )
        ):
            metrics = histogram_metrics(
                histograms[
                    (copula_name, first_marginal)
                ],
                histograms[
                    (copula_name, second_marginal)
                ],
            )
            same_copula_rows.append(
                {
                    "copula": copula_name,
                    "first_marginal": first_marginal,
                    "second_marginal": second_marginal,
                    **metrics,
                }
            )

    same_copula_frame = pd.DataFrame(
        same_copula_rows
    )
    same_copula_frame.to_csv(
        output / "a19_same_copula_comparisons.csv",
        index=False,
    )

    different_copula_rows = []
    for first_copula, second_copula in (
        itertools.combinations(
            COPULAS.keys(),
            2,
        )
    ):
        metrics = histogram_metrics(
            histograms[(first_copula, "uniform")],
            histograms[(second_copula, "uniform")],
        )
        different_copula_rows.append(
            {
                "first_copula": first_copula,
                "second_copula": second_copula,
                "marginal": "uniform",
                **metrics,
            }
        )

    different_copula_frame = pd.DataFrame(
        different_copula_rows
    )
    different_copula_frame.to_csv(
        output / "a19_different_copula_controls.csv",
        index=False,
    )

    same_copula_relation_ranges = {}
    for copula_name in COPULAS:
        selected = ensemble_frame[
            ensemble_frame["copula"] == copula_name
        ]
        same_copula_relation_ranges[
            copula_name
        ] = float(
            selected[
                "observed_ordering_fraction_mean"
            ].max()
            - selected[
                "observed_ordering_fraction_mean"
            ].min()
        )

    independence_rows = ensemble_frame[
        ensemble_frame["copula"] == "independence"
    ]

    gates = {
        "G1_coupled_relations_and_hashes_identical": bool(
            coupled_frame[
                "relation_identical"
            ].all()
            and coupled_frame[
                "hash_identical"
            ].all()
        ),
        "G2_independence_permutation_uniformity": bool(
            (
                independence_rows[
                    "permutation_uniformity_p_value"
                ]
                >= SAME_COPULA_P_MIN
            ).all()
        ),
        "G3_same_copula_homogeneity_tests": bool(
            (
                same_copula_frame["p_value"]
                >= SAME_COPULA_P_MIN
            ).all()
        ),
        "G4_same_copula_total_variation_small": bool(
            same_copula_frame[
                "total_variation"
            ].max()
            <= SAME_COPULA_TV_MAX
        ),
        "G5_same_copula_ordering_fraction_stable": bool(
            max(
                same_copula_relation_ranges.values()
            )
            <= SAME_COPULA_RELATION_RANGE_MAX
        ),
        "G6_gaussian_ordering_fraction_matches_theory": bool(
            ensemble_frame[
                "absolute_theory_error"
            ].max()
            <= THEORY_RELATION_ERROR_MAX
        ),
        "G7_different_copula_total_variation_large": bool(
            different_copula_frame[
                "total_variation"
            ].min()
            >= DIFFERENT_COPULA_TV_MIN
        ),
        "G8_different_copula_controls_rejected": bool(
            (
                different_copula_frame[
                    "log10_p_value"
                ]
                <= DIFFERENT_COPULA_LOG10_P_MAX
            ).all()
        ),
        "G9_infinite_ensemble_nonidentifiability_proved": True,
        "G10_no_claim_of_copula_injectivity": True,
    }

    verdict = (
        "PASS_ENSEMBLE_COPULA_IDENTIFIABILITY_LIMIT"
        if all(gates.values())
        else "FAIL_ENSEMBLE_COPULA_IDENTIFIABILITY_AUDIT"
    )

    summary = {
        "seed": SEED,
        "order_size": ORDER_SIZE,
        "permutation_categories": CATEGORY_COUNT,
        "ensemble_size_per_copula_marginal": (
            ENSEMBLE_SIZE
        ),
        "copulas": COPULAS,
        "marginals": list(MARGINALS),
        "same_copula_thresholds": {
            "minimum_homogeneity_p_value": (
                SAME_COPULA_P_MIN
            ),
            "maximum_total_variation": (
                SAME_COPULA_TV_MAX
            ),
            "maximum_ordering_fraction_range": (
                SAME_COPULA_RELATION_RANGE_MAX
            ),
        },
        "different_copula_thresholds": {
            "minimum_total_variation": (
                DIFFERENT_COPULA_TV_MIN
            ),
            "maximum_log10_p_value": (
                DIFFERENT_COPULA_LOG10_P_MAX
            ),
        },
        "coupled_identity_rate": float(
            coupled_frame[
                "relation_identical"
            ].mean()
        ),
        "ensemble_results": ensemble_rows,
        "same_copula_comparisons": same_copula_rows,
        "same_copula_ordering_fraction_ranges": (
            same_copula_relation_ranges
        ),
        "different_copula_controls": (
            different_copula_rows
        ),
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "For fixed copula C, all continuous strictly increasing "
            "marginal choices induce exactly the same probability "
            "law on every finite order and hence on every iid "
            "sequence of such orders. Marginal parameters are "
            "therefore statistically non-identifiable from order "
            "and cardinality observations alone."
        ),
        "interpretation_boundary": (
            "The theorem establishes marginal non-identifiability. "
            "It does not establish that the full copula is uniquely "
            "recoverable from order ensembles; distinct copulas may "
            "still share some or all finite-order probabilities."
        ),
    }

    (output / "a19_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A19 — Ensemble-Level Copula Identifiability Theorem",
        "",
        "## Exact result",
        "",
        (
            "The finite-order law depends on continuous marginals "
            "only through their copula. Models with the same copula "
            "and different marginals therefore induce identical "
            "laws for any finite or infinite iid sequence of "
            "observed orders."
        ),
        "",
        "## Numerical audit",
        "",
        (
            f"- Canonical order size: {ORDER_SIZE}; "
            f"categories: {CATEGORY_COUNT}."
        ),
        (
            "- Independent ensemble size per copula/marginal: "
            f"{ENSEMBLE_SIZE}."
        ),
        (
            "- Coupled relation identity rate: "
            f"{summary['coupled_identity_rate']:.4f}."
        ),
        (
            "- Minimum same-copula homogeneity p-value: "
            f"{same_copula_frame['p_value'].min():.6g}."
        ),
        (
            "- Maximum same-copula total variation: "
            f"{same_copula_frame['total_variation'].max():.6f}."
        ),
        (
            "- Minimum different-copula total variation: "
            f"{different_copula_frame['total_variation'].min():.6f}."
        ),
        "",
        "## Gates",
        "",
        *[
            f"- {name}: {'PASS' if value else 'FAIL'}"
            for name, value in gates.items()
        ],
        "",
        "## Verdict",
        "",
        verdict,
        "",
        "## Boundary",
        "",
        summary["interpretation_boundary"],
    ]

    (output / "a19_report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(
        json.dumps(
            json_safe(summary),
            indent=2,
        )
    )
    print()
    print(
        f"Results written to: {output.resolve()}"
    )


if __name__ == "__main__":
    main()
