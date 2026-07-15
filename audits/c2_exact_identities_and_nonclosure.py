#!/usr/bin/env python3
"""
Novelty Audit C2 — exact algebra and scalar non-closure witness.

This script verifies:

1. Affine covariance of the exponential certainty-equivalent score:
       Q_lambda(a q + c) = c + a Q_{a lambda}(q).

2. Centered-contraction transport:
       Q_lambda(q') = (1-a) mean(q) + a Q_{a lambda}(q),
   where q' = mean(q) + a(q-mean(q)).

3. An exact finite-support counterexample proving that mean plus one
   fixed-lambda score does not determine the future score.

No novelty claim follows from the numerical checks. The first two identities
are algebraic. The counterexample is an exact constructive witness.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path
import random


SEED = 20260815
TOLERANCE = 1e-12


def q_score(values: list[float], weights: list[float], lam: float) -> float:
    total = sum(w * math.exp(-lam * x) for x, w in zip(values, weights))
    if total <= 0.0:
        raise ValueError("The exponential moment must be positive.")
    return -math.log(total) / lam


def weighted_mean(values: list[float], weights: list[float]) -> float:
    return sum(w * x for x, w in zip(values, weights))


def random_identity_checks() -> dict[str, float]:
    rng = random.Random(SEED)
    max_affine_error = 0.0
    max_dynamic_error = 0.0

    for _ in range(1000):
        count = rng.randint(2, 12)
        values = [rng.uniform(-3.0, 4.0) for _ in range(count)]
        raw_weights = [rng.uniform(0.05, 2.0) for _ in range(count)]
        norm = sum(raw_weights)
        weights = [w / norm for w in raw_weights]

        lam = rng.uniform(0.05, 3.0)
        scale = rng.uniform(0.1, 1.8)
        shift = rng.uniform(-2.0, 2.0)

        transformed = [scale * x + shift for x in values]
        left = q_score(transformed, weights, lam)
        right = shift + scale * q_score(values, weights, scale * lam)
        max_affine_error = max(max_affine_error, abs(left - right))

        mean = weighted_mean(values, weights)
        contracted = [mean + scale * (x - mean) for x in values]
        dynamic_left = q_score(contracted, weights, lam)
        dynamic_right = (1.0 - scale) * mean + scale * q_score(
            values, weights, scale * lam
        )
        max_dynamic_error = max(
            max_dynamic_error,
            abs(dynamic_left - dynamic_right),
        )

    return {
        "maximum_affine_identity_error": max_affine_error,
        "maximum_dynamic_identity_error": max_dynamic_error,
    }


def exact_counterexample() -> dict[str, object]:
    """
    Let lambda = log 2 and a = 1/2 on support {0,1,2,3}.

    p_plus  = (9/40, 7/20, 1/8, 3/10)
    p_minus = (11/40, 3/20, 3/8, 1/5)

    Both distributions have:
      mean = 3/2
      E[2^{-X}] = 15/32

    Thus they have the same Q_lambda. At lambda/2:
      M_plus  = 23/80 + sqrt(2)/4
      M_minus = 37/80 + sqrt(2)/8
      M_plus - M_minus = (5 sqrt(2)-7)/40 > 0.

    Hence Q_{lambda/2} differs, and so does the next Q_lambda after the
    centered contraction with a=1/2.
    """
    support = [0, 1, 2, 3]
    p_plus = [
        Fraction(9, 40),
        Fraction(7, 20),
        Fraction(1, 8),
        Fraction(3, 10),
    ]
    p_minus = [
        Fraction(11, 40),
        Fraction(3, 20),
        Fraction(3, 8),
        Fraction(1, 5),
    ]

    assert sum(p_plus) == 1
    assert sum(p_minus) == 1
    assert all(p > 0 for p in p_plus + p_minus)

    mean_plus = sum(p * x for p, x in zip(p_plus, support))
    mean_minus = sum(p * x for p, x in zip(p_minus, support))

    laplace_plus = sum(
        p * Fraction(1, 2**x)
        for p, x in zip(p_plus, support)
    )
    laplace_minus = sum(
        p * Fraction(1, 2**x)
        for p, x in zip(p_minus, support)
    )

    sqrt2 = math.sqrt(2.0)
    half_laplace_plus = Fraction(23, 80) + Fraction(1, 4) * sqrt2
    half_laplace_minus = Fraction(37, 80) + Fraction(1, 8) * sqrt2
    exact_symbolic_difference = "(5*sqrt(2)-7)/40"
    half_difference = (5.0 * sqrt2 - 7.0) / 40.0

    lam = math.log(2.0)
    a = 0.5
    q_lam_plus = -math.log(float(laplace_plus)) / lam
    q_lam_minus = -math.log(float(laplace_minus)) / lam

    q_half_plus = -math.log(float(half_laplace_plus)) / (a * lam)
    q_half_minus = -math.log(float(half_laplace_minus)) / (a * lam)

    future_plus = (1.0 - a) * float(mean_plus) + a * q_half_plus
    future_minus = (1.0 - a) * float(mean_minus) + a * q_half_minus

    gates = {
        "probabilities_normalized": sum(p_plus) == sum(p_minus) == 1,
        "probabilities_positive": all(p > 0 for p in p_plus + p_minus),
        "means_equal_exactly": mean_plus == mean_minus == Fraction(3, 2),
        "fixed_lambda_moments_equal_exactly": (
            laplace_plus == laplace_minus == Fraction(15, 32)
        ),
        "fixed_lambda_scores_equal_numerically": (
            abs(q_lam_plus - q_lam_minus) <= TOLERANCE
        ),
        "rescaled_lambda_moments_differ": half_difference > 0.0,
        "future_scores_differ": abs(future_plus - future_minus) > 1e-6,
    }

    return {
        "support": support,
        "p_plus": [str(x) for x in p_plus],
        "p_minus": [str(x) for x in p_minus],
        "mean_plus": str(mean_plus),
        "mean_minus": str(mean_minus),
        "E_exp_minus_lambda_X_plus": str(laplace_plus),
        "E_exp_minus_lambda_X_minus": str(laplace_minus),
        "lambda": "log(2)",
        "contraction_a": "1/2",
        "E_exp_minus_half_lambda_X_plus": "23/80 + sqrt(2)/4",
        "E_exp_minus_half_lambda_X_minus": "37/80 + sqrt(2)/8",
        "half_lambda_moment_difference": exact_symbolic_difference,
        "half_lambda_moment_difference_decimal": half_difference,
        "Q_lambda_plus": q_lam_plus,
        "Q_lambda_minus": q_lam_minus,
        "Q_half_lambda_plus": q_half_plus,
        "Q_half_lambda_minus": q_half_minus,
        "future_Q_lambda_plus": future_plus,
        "future_Q_lambda_minus": future_minus,
        "future_score_absolute_difference": abs(future_plus - future_minus),
        "gates": gates,
    }


def main() -> None:
    output = Path(__file__).resolve().parent / "c2_exact_results"
    output.mkdir(exist_ok=True)

    identity = random_identity_checks()
    witness = exact_counterexample()

    gates = {
        "G1_affine_identity": (
            identity["maximum_affine_identity_error"] <= TOLERANCE
        ),
        "G2_centered_contraction_identity": (
            identity["maximum_dynamic_identity_error"] <= TOLERANCE
        ),
        "G3_exact_nonclosure_witness": all(witness["gates"].values()),
    }

    summary = {
        "audit_id": "NOVELTY_AUDIT_C2_EXACT_SUPPORT",
        "seed": SEED,
        "identity_checks": identity,
        "exact_counterexample": witness,
        "gates": gates,
        "verdict": (
            "PASS_EXACT_AFFINE_IDENTITIES_AND_SCALAR_NONCLOSURE_WITNESS"
            if all(gates.values())
            else "FAIL_C2_EXACT_SUPPORT"
        ),
        "interpretation": (
            "The affine and contraction formulas are direct algebraic "
            "properties of the exponential certainty equivalent. The exact "
            "four-point witness proves that mean plus one fixed-lambda score "
            "is not a generally closed macrostate under the contraction."
        ),
        "limitations": [
            "The script does not establish bibliographic novelty.",
            "The counterexample proves generic non-closure, not the absence "
            "of closure on every restricted invariant distribution family.",
            "No physical interpretation of Q is established.",
        ],
    }

    (output / "c2_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    witness_rows = [
        {
            "distribution": "plus",
            "p0": "9/40",
            "p1": "7/20",
            "p2": "1/8",
            "p3": "3/10",
            "mean": "3/2",
            "M_lambda": "15/32",
            "M_half_lambda": "23/80 + sqrt(2)/4",
            "future_Q_lambda": witness["future_Q_lambda_plus"],
        },
        {
            "distribution": "minus",
            "p0": "11/40",
            "p1": "3/20",
            "p2": "3/8",
            "p3": "1/5",
            "mean": "3/2",
            "M_lambda": "15/32",
            "M_half_lambda": "37/80 + sqrt(2)/8",
            "future_Q_lambda": witness["future_Q_lambda_minus"],
        },
    ]

    with (output / "c2_exact_counterexample.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        fieldnames = list(witness_rows[0].keys())
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(witness_rows)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    import csv
    main()
