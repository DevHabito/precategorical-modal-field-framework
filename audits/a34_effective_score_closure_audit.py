#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260808
LAMBDA = 1.3
ETA = 0.35
CONTRACTION = 1.0 - ETA / 2.0
ASSOCIATIVITY_SAMPLES = 5000
GAUGE_SAMPLES = 4000
CUMULANT_SAMPLES = 3000
MAX_EXACT_ERROR = 2e-11
MIN_DYNAMIC_WITNESS_DIFFERENCE = 1e-4
MIN_MOMENT_PAIR_DIFFERENCE = 1e-3


def json_safe(value):
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(v) for v in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def normalize(weights: np.ndarray) -> np.ndarray:
    weights = np.asarray(weights, dtype=float)
    total = float(weights.sum())
    if total <= 0.0:
        raise ValueError("Nonpositive total weight.")
    return weights / total


def logsumexp(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    maximum = float(values.max())
    return maximum + math.log(float(np.exp(values - maximum).sum()))


def q_effective(
    q: np.ndarray,
    mu: np.ndarray,
    lambda_value: float = LAMBDA,
) -> float:
    q = np.asarray(q, dtype=float)
    mu = normalize(np.asarray(mu, dtype=float))
    if lambda_value == 0.0:
        return float(np.dot(mu, q))
    log_terms = np.log(mu) - lambda_value * q
    return -logsumexp(log_terms) / lambda_value


def weighted_moments(q: np.ndarray, mu: np.ndarray) -> dict[str, float]:
    q = np.asarray(q, dtype=float)
    mu = normalize(np.asarray(mu, dtype=float))
    mean = float(np.dot(mu, q))
    centered = q - mean
    variance = float(np.dot(mu, centered**2))
    kappa3 = float(np.dot(mu, centered**3))
    central4 = float(np.dot(mu, centered**4))
    kappa4 = central4 - 3.0 * variance**2
    return {
        "mean": mean,
        "variance": variance,
        "kappa3": kappa3,
        "kappa4": kappa4,
    }


def random_partition(n: int, rng: np.random.Generator) -> list[np.ndarray]:
    group_count = int(rng.integers(2, min(10, n) + 1))
    permutation = rng.permutation(n)
    cuts = sorted(
        rng.choice(np.arange(1, n), size=group_count - 1, replace=False)
    )
    groups = []
    start = 0
    for end in cuts + [n]:
        groups.append(np.asarray(permutation[start:end], dtype=int))
        start = end
    return groups


def associativity_audit(rng: np.random.Generator) -> list[dict[str, float]]:
    rows = []
    for sample_index in range(ASSOCIATIVITY_SAMPLES):
        n = int(rng.integers(5, 81))
        mu = normalize(np.exp(rng.normal(0.0, 0.8, size=n)))
        q = rng.normal(0.0, 1.2, size=n)
        groups = random_partition(n, rng)

        direct = q_effective(q, mu)
        group_masses = np.asarray([float(mu[g].sum()) for g in groups])
        group_scores = np.asarray([
            q_effective(q[g], mu[g]) for g in groups
        ])
        hierarchical = q_effective(group_scores, group_masses)

        # Equivalent additive partition weight.
        direct_weight = float(np.dot(mu, np.exp(-LAMBDA * q)))
        hierarchical_weight = float(
            np.dot(group_masses, np.exp(-LAMBDA * group_scores))
        )
        rows.append({
            "sample_index": sample_index,
            "n": n,
            "group_count": len(groups),
            "effective_score_error": abs(direct - hierarchical),
            "partition_weight_error": abs(direct_weight - hierarchical_weight),
        })
    return rows


def gauge_affine_audit(rng: np.random.Generator) -> list[dict[str, float]]:
    rows = []
    for sample_index in range(GAUGE_SAMPLES):
        n = int(rng.integers(3, 40))
        mu = normalize(np.exp(rng.normal(0.0, 0.6, size=n)))
        q = rng.normal(0.0, 1.0, size=n)
        shift = float(rng.uniform(-4.0, 4.0))
        scale = float(rng.uniform(0.2, 2.5))

        base = q_effective(q, mu, LAMBDA)
        shifted = q_effective(q + shift, mu, LAMBDA)
        affine = q_effective(scale * q + shift, mu, LAMBDA)
        predicted_affine = shift + scale * q_effective(
            q, mu, LAMBDA * scale
        )
        rows.append({
            "sample_index": sample_index,
            "shift_covariance_error": abs(shifted - (base + shift)),
            "affine_rescaling_identity_error": abs(affine - predicted_affine),
        })
    return rows


def moment_insufficiency_audit() -> list[dict[str, float]]:
    rows = []
    q_a = np.asarray([-1.0, 1.0])
    mu_a = np.asarray([0.5, 0.5])
    q_b = np.asarray([-math.sqrt(2.0), 0.0, math.sqrt(2.0)])
    mu_b = np.asarray([0.25, 0.5, 0.25])
    for lambda_value in (0.25, 0.5, 1.0, 1.3, 2.0, 4.0):
        moments_a = weighted_moments(q_a, mu_a)
        moments_b = weighted_moments(q_b, mu_b)
        score_a = q_effective(q_a, mu_a, lambda_value)
        score_b = q_effective(q_b, mu_b, lambda_value)
        rows.append({
            "lambda": lambda_value,
            "mean_error": abs(moments_a["mean"] - moments_b["mean"]),
            "variance_error": abs(moments_a["variance"] - moments_b["variance"]),
            "effective_score_a": score_a,
            "effective_score_b": score_b,
            "effective_score_difference": abs(score_a - score_b),
        })
    return rows


def matched_q_mean_dynamic_witness() -> list[dict[str, float]]:
    """Same mean and same Q_lambda, different future under centered contraction."""
    rows = []
    for b in (1.25, 1.5, 2.0, 2.5, 3.0):
        # Distribution A: +/-1 with equal mass, mean 0.
        q_a = np.asarray([-1.0, 1.0])
        mu_a = np.asarray([0.5, 0.5])
        z_target = math.cosh(LAMBDA)
        denominator = 2.0 * (math.cosh(LAMBDA * b) - 1.0)
        w = (z_target - 1.0) / denominator
        if not (0.0 < w < 0.5):
            continue
        # Distribution B: +/-b with mass w each and zero with remaining mass.
        q_b = np.asarray([-b, 0.0, b])
        mu_b = np.asarray([w, 1.0 - 2.0 * w, w])

        q0_a = q_effective(q_a, mu_a, LAMBDA)
        q0_b = q_effective(q_b, mu_b, LAMBDA)
        mean_a = weighted_moments(q_a, mu_a)["mean"]
        mean_b = weighted_moments(q_b, mu_b)["mean"]

        # Current deterministic centered RZS-like contraction:
        # q' = mean(q) + a [q - mean(q)].
        q_a_next = mean_a + CONTRACTION * (q_a - mean_a)
        q_b_next = mean_b + CONTRACTION * (q_b - mean_b)
        q1_a = q_effective(q_a_next, mu_a, LAMBDA)
        q1_b = q_effective(q_b_next, mu_b, LAMBDA)

        # Exact closure using mean and the whole Q(lambda) curve:
        predicted_a = (
            (1.0 - CONTRACTION) * mean_a
            + CONTRACTION * q_effective(q_a, mu_a, LAMBDA * CONTRACTION)
        )
        predicted_b = (
            (1.0 - CONTRACTION) * mean_b
            + CONTRACTION * q_effective(q_b, mu_b, LAMBDA * CONTRACTION)
        )
        rows.append({
            "b": b,
            "outer_mass_each": w,
            "initial_mean_error": abs(mean_a - mean_b),
            "initial_effective_score_error": abs(q0_a - q0_b),
            "future_effective_score_a": q1_a,
            "future_effective_score_b": q1_b,
            "future_effective_score_difference": abs(q1_a - q1_b),
            "curve_closure_error_a": abs(q1_a - predicted_a),
            "curve_closure_error_b": abs(q1_b - predicted_b),
        })
    return rows


def cumulant_audit(rng: np.random.Generator) -> list[dict[str, float]]:
    rows = []
    for sample_index in range(CUMULANT_SAMPLES):
        n = int(rng.integers(4, 30))
        mu = normalize(np.exp(rng.normal(0.0, 0.5, size=n)))
        q = rng.normal(0.0, 0.7, size=n)
        moments = weighted_moments(q, mu)
        for lambda_value in (0.025, 0.05, 0.1, 0.2):
            exact = q_effective(q, mu, lambda_value)
            second = moments["mean"] - 0.5 * lambda_value * moments["variance"]
            third = second + (lambda_value**2 / 6.0) * moments["kappa3"]
            fourth = third - (lambda_value**3 / 24.0) * moments["kappa4"]
            rows.append({
                "sample_index": sample_index,
                "lambda": lambda_value,
                "second_order_error": abs(exact - second),
                "third_order_error": abs(exact - third),
                "fourth_order_error": abs(exact - fourth),
            })
    return rows


def scalar_loss_witness() -> list[dict[str, float]]:
    rows = []
    for amplitude in np.linspace(0.2, 2.5, 60):
        q_pair = np.asarray([-amplitude, amplitude])
        mu_pair = np.asarray([0.5, 0.5])
        scalar = q_effective(q_pair, mu_pair, LAMBDA)
        q_constant = np.asarray([scalar, scalar])
        mu_constant = np.asarray([0.5, 0.5])
        initial_error = abs(
            q_effective(q_pair, mu_pair, LAMBDA)
            - q_effective(q_constant, mu_constant, LAMBDA)
        )
        pair_next = CONTRACTION * q_pair
        constant_next = q_constant.copy()
        future_difference = abs(
            q_effective(pair_next, mu_pair, LAMBDA)
            - q_effective(constant_next, mu_constant, LAMBDA)
        )
        rows.append({
            "amplitude": amplitude,
            "matched_effective_score": scalar,
            "initial_effective_score_error": initial_error,
            "future_effective_score_difference": future_difference,
        })
    return rows


def main() -> None:
    output = Path("a34_exact_results")
    output.mkdir(exist_ok=True)

    theorem = r"""# A34 — Effective Score and Dynamic Closure

## Definition
For positive masses \(\mu_i\) with \(\sum_i\mu_i=1\),
\[
Q_\lambda(q,\mu)=-\frac1\lambda\log\sum_i\mu_i e^{-\lambda q_i}.
\]

## Associative aggregation
For a partition into groups \(G\), let \(\mu_G=\sum_{i\in G}\mu_i\) and
\(Q_G=Q_\lambda(q_G,\mu_G^{-1}\mu|_G)\). Then
\[
Q_\lambda(q,\mu)
=-\frac1\lambda\log\sum_G\mu_G e^{-\lambda Q_G}.
\]
Thus exact aggregation requires carrying both group mass and group effective
score.

## Gauge and affine covariance
\[
Q_\lambda(q+c)=Q_\lambda(q)+c,
\]
and for \(a>0\),
\[
Q_\lambda(aq+c)=c+aQ_{a\lambda}(q).
\]

## Cumulant expansion
Writing weighted cumulants \(\kappa_n\),
\[
Q_\lambda=\kappa_1-\frac\lambda2\kappa_2
+\frac{\lambda^2}{6}\kappa_3
-\frac{\lambda^3}{24}\kappa_4+\cdots.
\]
Mean and variance are insufficient at finite lambda because higher cumulants
contribute.

## Dynamic closure obstruction
For centered affine contraction
\[
q_i'=\bar q+a(q_i-\bar q),
\]
\[
Q_\lambda'= (1-a)\bar q+aQ_{a\lambda}.
\]
Therefore a scalar \(Q_\lambda\) at one fixed lambda is not generally closed.
Two microdistributions can have the same mean and the same \(Q_\lambda\), but
different \(Q_{a\lambda}\), and hence different next macro scores.

Exact deterministic closure is available if one carries the mean and the
whole log-partition curve in lambda. This is an infinite-dimensional macro
state unless an independently justified finite-dimensional distribution
family is invariant under the dynamics.

## Boundary
Static associativity does not establish autonomous macrodynamics. No physical
interpretation of Q, thermodynamic free energy, or exact RZS closure is claimed.
"""
    (output / "a34_theorem.md").write_text(theorem, encoding="utf-8")

    rng = np.random.default_rng(SEED)
    frames = {
        "associativity": pd.DataFrame(associativity_audit(rng)),
        "gauge": pd.DataFrame(gauge_affine_audit(rng)),
        "moments": pd.DataFrame(moment_insufficiency_audit()),
        "matched": pd.DataFrame(matched_q_mean_dynamic_witness()),
        "cumulants": pd.DataFrame(cumulant_audit(rng)),
        "scalar_loss": pd.DataFrame(scalar_loss_witness()),
    }
    file_names = {
        "associativity": "a34_associative_aggregation.csv",
        "gauge": "a34_gauge_affine_covariance.csv",
        "moments": "a34_mean_variance_insufficiency.csv",
        "matched": "a34_matched_q_mean_dynamic_witness.csv",
        "cumulants": "a34_cumulant_expansion.csv",
        "scalar_loss": "a34_scalar_information_loss.csv",
    }
    for key, frame in frames.items():
        frame.to_csv(output / file_names[key], index=False)

    cumulant_summary = []
    for lambda_value, group in frames["cumulants"].groupby("lambda"):
        cumulant_summary.append({
            "lambda": float(lambda_value),
            "median_second_order_error": float(group["second_order_error"].median()),
            "median_third_order_error": float(group["third_order_error"].median()),
            "median_fourth_order_error": float(group["fourth_order_error"].median()),
        })

    gates = {
        "G1_associative_mass_score_aggregation_exact": bool(
            frames["associativity"][["effective_score_error", "partition_weight_error"]].max().max()
            <= MAX_EXACT_ERROR
        ),
        "G2_global_q_shift_covariance_exact": bool(
            frames["gauge"]["shift_covariance_error"].max() <= MAX_EXACT_ERROR
        ),
        "G3_affine_rescaling_identity_exact": bool(
            frames["gauge"]["affine_rescaling_identity_error"].max() <= MAX_EXACT_ERROR
        ),
        "G4_mean_and_variance_do_not_determine_effective_score": bool(
            frames["moments"]["mean_error"].max() <= MAX_EXACT_ERROR
            and frames["moments"]["variance_error"].max() <= MAX_EXACT_ERROR
            and frames["moments"]["effective_score_difference"].max() >= MIN_MOMENT_PAIR_DIFFERENCE
        ),
        "G5_same_mean_and_qeff_can_have_different_future": bool(
            frames["matched"]["initial_mean_error"].max() <= MAX_EXACT_ERROR
            and frames["matched"]["initial_effective_score_error"].max() <= MAX_EXACT_ERROR
            and frames["matched"]["future_effective_score_difference"].min() >= MIN_DYNAMIC_WITNESS_DIFFERENCE
        ),
        "G6_whole_partition_curve_closes_centered_contraction": bool(
            frames["matched"][["curve_closure_error_a", "curve_closure_error_b"]].max().max()
            <= MAX_EXACT_ERROR
        ),
        "G7_scalar_qeff_alone_not_dynamically_closed": bool(
            frames["scalar_loss"]["initial_effective_score_error"].max() <= MAX_EXACT_ERROR
            and frames["scalar_loss"]["future_effective_score_difference"].median()
            >= MIN_DYNAMIC_WITNESS_DIFFERENCE
        ),
        "G8_cumulant_expansion_improves_with_added_terms_at_small_lambda": bool(
            all(
                item["median_fourth_order_error"] < item["median_third_order_error"]
                < item["median_second_order_error"]
                for item in cumulant_summary
            )
        ),
        "G9_static_projectivity_not_promoted_to_dynamic_closure": True,
        "G10_no_physical_free_energy_or_thermodynamic_claim": True,
    }
    verdict = (
        "PASS_STATIC_EFFECTIVE_SCORE_WITH_DYNAMIC_CLOSURE_OBSTRUCTION"
        if all(gates.values())
        else "FAIL_EFFECTIVE_SCORE_CLOSURE_AUDIT"
    )

    classification = [
        {
            "object": "(mu_A, Q_lambda(A)) under static regrouping",
            "status": "EXACTLY_ASSOCIATIVE",
        },
        {
            "object": "Q_lambda alone",
            "status": "STATICALLY_AGGREGATABLE_ONLY_WITH_MASS",
        },
        {
            "object": "mean and variance",
            "status": "INSUFFICIENT_AT_FINITE_LAMBDA",
        },
        {
            "object": "single fixed-lambda Q under centered contraction",
            "status": "NOT_AUTONOMOUSLY_CLOSED",
        },
        {
            "object": "mean plus full Q(lambda) curve",
            "status": "EXACTLY_CLOSED_FOR_DETERMINISTIC_CENTERED_CONTRACTION",
        },
        {
            "object": "finite cumulant truncation",
            "status": "ASYMPTOTIC_APPROXIMATION_NOT_EXACT_GENERAL_CLOSURE",
        },
        {
            "object": "physical RZS macro observable",
            "status": "NOT_ESTABLISHED",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a34_effective_score_classification.csv", index=False
    )

    aggregate = {
        "maximum_associativity_error": float(
            frames["associativity"][["effective_score_error", "partition_weight_error"]].max().max()
        ),
        "maximum_shift_covariance_error": float(frames["gauge"]["shift_covariance_error"].max()),
        "maximum_affine_identity_error": float(frames["gauge"]["affine_rescaling_identity_error"].max()),
        "maximum_same_moment_qeff_difference": float(frames["moments"]["effective_score_difference"].max()),
        "minimum_matched_mean_qeff_future_difference": float(frames["matched"]["future_effective_score_difference"].min()),
        "maximum_curve_closure_error": float(frames["matched"][["curve_closure_error_a", "curve_closure_error_b"]].max().max()),
        "median_scalar_loss_future_difference": float(frames["scalar_loss"]["future_effective_score_difference"].median()),
        "cumulant_summary": cumulant_summary,
    }
    summary = {
        "seed": SEED,
        "lambda": LAMBDA,
        "eta": ETA,
        "contraction": CONTRACTION,
        "aggregate_results": aggregate,
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "The effective log-partition score is an exact static coarse-graining variable when paired with additive mass. "
            "It is gauge-covariant and composes associatively. However, it loses microscopic information: equal means and variances can yield different scores, and equal means plus equal fixed-lambda scores can evolve differently under the deterministic centered contraction. "
            "The exact contraction law requires the score evaluated at a rescaled lambda, so a single scalar is not dynamically closed. Exact closure uses the mean and the whole log-partition curve, or an independently justified invariant finite-dimensional family."
        ),
        "interpretation_boundary": (
            "A34 establishes a static sufficient message and a dynamic no-go. It does not identify Q_eff as physical free energy, prove thermodynamics, or establish a closed RZS macrodynamics."
        ),
    }
    (output / "a34_summary.json").write_text(
        json.dumps(json_safe(summary), indent=2), encoding="utf-8"
    )

    report = [
        "# A34 — Effective Score and Dynamic Closure",
        "",
        "## Main result",
        "",
        "The log-partition effective score is exactly associative when carried with mass, but a single fixed-lambda scalar is not dynamically closed under the centered contraction.",
        "",
        "## Aggregate results",
        "",
    ]
    for key, value in aggregate.items():
        if key != "cumulant_summary":
            report.append(f"- {key}: {value}")
    report.extend(["", "## Gates", ""])
    report.extend([f"- {name}: {'PASS' if value else 'FAIL'}" for name, value in gates.items()])
    report.extend(["", "## Verdict", "", verdict, "", "## Boundary", "", summary["interpretation_boundary"]])
    (output / "a34_report.md").write_text("\n".join(report), encoding="utf-8")

    print(json.dumps(json_safe(summary), indent=2))
    print(f"\nResults written to: {output.resolve()}")


if __name__ == "__main__":
    main()
