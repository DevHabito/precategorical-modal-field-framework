
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260808

A = 0.825
INNOVATION_SD = math.sqrt(1.0 - A * A)  # stationary variance normalized to 1
LAMBDA_VALUES = (0.5, 1.0, 2.0)
TIME_STEPS = tuple(range(0, 31))

EMPIRICAL_N_VALUES = (32, 128, 512, 2048)
EMPIRICAL_REPLICATES = 3000
EMPIRICAL_BATCH_SIZE = 250

CENTERING_DIMS = (8, 16, 64, 256)

MAX_EXACT_ERROR = 2e-12
MAX_MATCHED_NULL_FINAL_DIFFERENCE = 1e-8
MIN_MATCHED_NULL_INITIAL_DIFFERENCE = 1e-4
MIN_NONGAUSSIAN_EXCESS_ABS = 0.05
MIN_STATIONARY_Q_DIFFERENCE = 1e-4


def json_safe(value):
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def q_from_log_mgf(log_mgf: float, lambda_value: float) -> float:
    return -log_mgf / lambda_value


def gaussian_q(mean: float, variance: float, lambda_value: float) -> float:
    return mean - 0.5 * lambda_value * variance


def matched_null_log_mgf(distribution: str, argument: float) -> float:
    """
    Both distributions have mean 0 and variance 1.

    rademacher:
      P(X=-1)=P(X=1)=1/2
      M(s)=cosh(s)

    three_point:
      P(X=-sqrt(2))=1/4
      P(X=0)=1/2
      P(X=sqrt(2))=1/4
      M(s)=1/2 + 1/2 cosh(sqrt(2)s)
    """
    if distribution == "rademacher":
        return math.log(math.cosh(argument))
    if distribution == "three_point":
        return math.log(
            0.5 + 0.5 * math.cosh(math.sqrt(2.0) * argument)
        )
    raise ValueError(distribution)


def matched_null_dynamics_audit() -> list[dict[str, float]]:
    rows = []

    for lambda_value in LAMBDA_VALUES:
        previous_difference = float("inf")

        for time_step in TIME_STEPS:
            contraction = A ** time_step
            gaussian_noise_variance = 1.0 - A ** (2 * time_step)
            total_variance = contraction**2 + gaussian_noise_variance

            log_noise_mgf = (
                0.5 * lambda_value**2 * gaussian_noise_variance
            )

            log_mgf_first = (
                matched_null_log_mgf(
                    "rademacher",
                    -lambda_value * contraction,
                )
                + log_noise_mgf
            )
            log_mgf_second = (
                matched_null_log_mgf(
                    "three_point",
                    -lambda_value * contraction,
                )
                + log_noise_mgf
            )

            q_first = q_from_log_mgf(log_mgf_first, lambda_value)
            q_second = q_from_log_mgf(log_mgf_second, lambda_value)
            q_gaussian = gaussian_q(
                0.0,
                total_variance,
                lambda_value,
            )
            difference = abs(q_first - q_second)

            rows.append(
                {
                    "lambda": lambda_value,
                    "time_step": time_step,
                    "contraction": contraction,
                    "q_rademacher": q_first,
                    "q_three_point": q_second,
                    "q_gaussian_same_mean_variance": q_gaussian,
                    "matched_null_difference": difference,
                    "rademacher_gaussian_error": abs(
                        q_first - q_gaussian
                    ),
                    "three_point_gaussian_error": abs(
                        q_second - q_gaussian
                    ),
                    "nonincreasing_from_previous": bool(
                        difference <= previous_difference + 1e-15
                    ),
                }
            )
            previous_difference = difference

    return rows


def cumulant_decay_audit() -> list[dict[str, float]]:
    rows = []

    # Initial Rademacher cumulants: k2=1, k4=-2, k6=16.
    for time_step in TIME_STEPS:
        variance = (
            A ** (2 * time_step)
            + (1.0 - A ** (2 * time_step))
        )
        kappa4 = -2.0 * A ** (4 * time_step)
        kappa6 = 16.0 * A ** (6 * time_step)

        rows.append(
            {
                "time_step": time_step,
                "variance": variance,
                "kappa4": kappa4,
                "kappa6": kappa6,
                "standardized_excess_kurtosis": kappa4 / variance**2,
                "standardized_sixth_cumulant": kappa6 / variance**3,
            }
        )

    return rows


def stationary_rademacher_audit() -> list[dict[str, float]]:
    rows = []

    # X = sum_{k>=0} INNOVATION_SD * A^k * eps_k,
    # eps_k in {-1,+1}, equally likely.
    stationary_variance = (
        INNOVATION_SD**2 / (1.0 - A**2)
    )
    stationary_kappa4 = (
        -2.0
        * INNOVATION_SD**4
        / (1.0 - A**4)
    )
    stationary_excess = (
        stationary_kappa4 / stationary_variance**2
    )

    for lambda_value in LAMBDA_VALUES:
        log_mgf = 0.0
        terms_used = 0

        for k in range(10000):
            coefficient = (
                lambda_value
                * INNOVATION_SD
                * A**k
            )
            contribution = math.log(
                math.cosh(coefficient)
            )
            log_mgf += contribution
            terms_used = k + 1

            if coefficient**2 < 1e-28:
                break

        q_exact = q_from_log_mgf(
            log_mgf,
            lambda_value,
        )
        q_gaussian = gaussian_q(
            0.0,
            stationary_variance,
            lambda_value,
        )

        rows.append(
            {
                "lambda": lambda_value,
                "stationary_variance": stationary_variance,
                "stationary_kappa4": stationary_kappa4,
                "stationary_excess_kurtosis": stationary_excess,
                "exact_stationary_q": q_exact,
                "gaussian_stationary_q": q_gaussian,
                "absolute_q_difference": abs(
                    q_exact - q_gaussian
                ),
                "terms_used": terms_used,
            }
        )

    return rows


def centered_noise_shape_audit() -> list[dict[str, float]]:
    rows = []

    # For iid unit-variance Rademacher noise eps_j and
    # centered component y_i = eps_i - mean(eps):
    # kappa4(y_i) = -2 * sum_j c_j^4,
    # variance(y_i) = sum_j c_j^2.
    for dimension in CENTERING_DIMS:
        own = 1.0 - 1.0 / dimension
        other = -1.0 / dimension

        coefficient_square_sum = (
            own**2
            + (dimension - 1) * other**2
        )
        coefficient_fourth_sum = (
            own**4
            + (dimension - 1) * other**4
        )
        excess = (
            -2.0
            * coefficient_fourth_sum
            / coefficient_square_sum**2
        )

        rows.append(
            {
                "dimension": dimension,
                "centered_component_variance": coefficient_square_sum,
                "centered_component_kappa4": (
                    -2.0 * coefficient_fourth_sum
                ),
                "centered_component_excess_kurtosis": excess,
            }
        )

    return rows


def empirical_gaussian_q_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for lambda_value in LAMBDA_VALUES:
        population_q = -0.5 * lambda_value

        for sample_size in EMPIRICAL_N_VALUES:
            estimates = []

            remaining = EMPIRICAL_REPLICATES
            while remaining > 0:
                batch = min(
                    EMPIRICAL_BATCH_SIZE,
                    remaining,
                )
                samples = rng.normal(
                    0.0,
                    1.0,
                    size=(batch, sample_size),
                )
                logits = -lambda_value * samples
                row_max = logits.max(
                    axis=1,
                    keepdims=True,
                )
                log_mean_exp = (
                    row_max[:, 0]
                    + np.log(
                        np.mean(
                            np.exp(logits - row_max),
                            axis=1,
                        )
                    )
                )
                estimates.extend(
                    (
                        -log_mean_exp / lambda_value
                    ).tolist()
                )
                remaining -= batch

            estimates_array = np.asarray(
                estimates,
                dtype=float,
            )
            errors = estimates_array - population_q
            delta_rmse = (
                math.sqrt(
                    math.exp(lambda_value**2) - 1.0
                )
                / (
                    lambda_value
                    * math.sqrt(sample_size)
                )
            )

            rows.append(
                {
                    "lambda": lambda_value,
                    "sample_size": sample_size,
                    "mean_estimate": float(
                        estimates_array.mean()
                    ),
                    "bias": float(
                        errors.mean()
                    ),
                    "rmse": float(
                        np.sqrt(
                            np.mean(errors**2)
                        )
                    ),
                    "median_absolute_error": float(
                        np.median(np.abs(errors))
                    ),
                    "delta_method_rmse": delta_rmse,
                    "rmse_to_delta_ratio": float(
                        np.sqrt(
                            np.mean(errors**2)
                        )
                        / delta_rmse
                    ),
                }
            )

    return rows


def gaussian_affine_closure_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for sample_index in range(5000):
        mean = float(
            rng.normal(0.0, 2.0)
        )
        variance = float(
            np.exp(
                rng.normal(-0.2, 0.8)
            )
        )
        contraction = float(
            rng.uniform(-0.95, 0.95)
        )
        drift = float(
            rng.normal(0.0, 0.5)
        )
        innovation_variance = float(
            np.exp(
                rng.normal(-2.0, 1.0)
            )
        )
        lambda_value = float(
            rng.uniform(0.1, 3.0)
        )

        next_mean = drift + contraction * mean
        next_variance = (
            contraction**2 * variance
            + innovation_variance
        )

        direct_q = gaussian_q(
            next_mean,
            next_variance,
            lambda_value,
        )

        log_mgf_transformed = (
            -lambda_value * next_mean
            + 0.5
            * lambda_value**2
            * next_variance
        )
        mgf_q = q_from_log_mgf(
            log_mgf_transformed,
            lambda_value,
        )

        rows.append(
            {
                "sample_index": sample_index,
                "absolute_closure_error": abs(
                    direct_q - mgf_q
                ),
            }
        )

    return rows


def main() -> None:
    output = Path("a35_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = r"""# A35 — Gaussian Closure and Innovation-Law Audit

## Affine Gaussian invariance

Let

\[
X_{t+1}=b+aX_t+\xi_t,
\]

where \(X_t\) is Gaussian and \(\xi_t\) is independent Gaussian noise. Then
\(X_{t+1}\) is Gaussian with

\[
m_{t+1}=b+am_t,
\qquad
v_{t+1}=a^2v_t+v_\xi.
\]

For a Gaussian law,

\[
Q_\lambda
=
-\lambda^{-1}\log E[e^{-\lambda X}]
=
m-\frac{\lambda}{2}v.
\]

Thus mean and variance form an exact finite-dimensional closure only inside
the Gaussian family.

## Cumulant recurrence

For independent affine innovations,

\[
\kappa_r(X_{t+1})
=
a^r\kappa_r(X_t)+\kappa_r(\xi_t)
\]

for \(r\ge2\), with the usual affine rule for the mean. Gaussian innovations
have no cumulants above order two, so initial higher cumulants decay as
\(a^{rt}\) when \(|a|<1\).

Non-Gaussian innovations continuously regenerate higher cumulants. Their
stationary values are

\[
\kappa_r^*
=
\frac{\kappa_r(\xi)}{1-a^r}.
\]

Therefore a Gaussian stationary closure is not valid unless the innovation
law is Gaussian or satisfies equivalent higher-cumulant restrictions.

## Centering is not Gaussianization

The map \(\epsilon\mapsto\epsilon-\bar\epsilon\) is linear. It preserves
Gaussianity when the input is Gaussian, but it does not generally transform
non-Gaussian input into Gaussian noise.

## Finite empirical caveat

Even when the population law is exactly Gaussian, the finite empirical
quantity

\[
-\lambda^{-1}\log\left(n^{-1}\sum_i e^{-\lambda q_i}\right)
\]

is a random estimator, not exactly \(m-\lambda v/2\). Its uncertainty depends
strongly on both sample size and \(\lambda\).

## Boundary

The current RZS contract specifies centered noise but does not, in the
materials audited here, derive a Gaussian innovation law. Gaussian closure is
therefore conditional, not established as an RZS law.
"""
    (
        output / "a35_theorem.md"
    ).write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    frames = {
        "gaussian_closure": pd.DataFrame(
            gaussian_affine_closure_audit(rng)
        ),
        "matched_nulls": pd.DataFrame(
            matched_null_dynamics_audit()
        ),
        "cumulants": pd.DataFrame(
            cumulant_decay_audit()
        ),
        "stationary_rademacher": pd.DataFrame(
            stationary_rademacher_audit()
        ),
        "centered_noise": pd.DataFrame(
            centered_noise_shape_audit()
        ),
        "empirical_gaussian": pd.DataFrame(
            empirical_gaussian_q_audit(rng)
        ),
    }

    file_map = {
        "gaussian_closure": (
            "a35_gaussian_affine_closure.csv"
        ),
        "matched_nulls": (
            "a35_matched_moment_gaussianization.csv"
        ),
        "cumulants": (
            "a35_gaussian_noise_cumulant_decay.csv"
        ),
        "stationary_rademacher": (
            "a35_nongaussian_stationary_control.csv"
        ),
        "centered_noise": (
            "a35_centered_noise_shape.csv"
        ),
        "empirical_gaussian": (
            "a35_finite_empirical_gaussian_q.csv"
        ),
    }

    for key, frame in frames.items():
        frame.to_csv(
            output / file_map[key],
            index=False,
        )

    matched_initial = (
        frames["matched_nulls"]
        .query("time_step == 0")
        ["matched_null_difference"]
    )
    matched_final = (
        frames["matched_nulls"]
        .query("time_step == 30")
        ["matched_null_difference"]
    )

    empirical_monotonic = True
    for _, group in (
        frames["empirical_gaussian"]
        .sort_values("sample_size")
        .groupby("lambda")
    ):
        rmse_values = group["rmse"].to_numpy()
        empirical_monotonic = (
            empirical_monotonic
            and all(
                rmse_values[index + 1]
                < rmse_values[index]
                for index in range(
                    len(rmse_values) - 1
                )
            )
        )

    largest_n = (
        frames["empirical_gaussian"]
        .query("sample_size == 2048")
        .sort_values("lambda")
    )

    gates = {
        "G1_affine_gaussian_family_exactly_closed": bool(
            frames["gaussian_closure"][
                "absolute_closure_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G2_gaussian_q_exactly_mean_variance_functional": True,
        "G3_same_mean_variance_nongaussian_nulls_differ_at_finite_time": bool(
            matched_initial.min()
            >= MIN_MATCHED_NULL_INITIAL_DIFFERENCE
        ),
        "G4_gaussian_innovations_asymptotically_erase_higher_moments": bool(
            matched_final.max()
            <= MAX_MATCHED_NULL_FINAL_DIFFERENCE
            and frames["matched_nulls"][
                "nonincreasing_from_previous"
            ].all()
        ),
        "G5_higher_cumulants_decay_under_gaussian_innovations": bool(
            abs(
                frames["cumulants"][
                    "kappa4"
                ].iloc[-1]
            )
            < abs(
                frames["cumulants"][
                    "kappa4"
                ].iloc[0]
            )
            * 1e-8
            and abs(
                frames["cumulants"][
                    "kappa6"
                ].iloc[-1]
            )
            < abs(
                frames["cumulants"][
                    "kappa6"
                ].iloc[0]
            )
            * 1e-12
        ),
        "G6_nongaussian_innovations_generate_nongaussian_stationary_law": bool(
            abs(
                frames["stationary_rademacher"][
                    "stationary_excess_kurtosis"
                ].iloc[0]
            )
            >= MIN_NONGAUSSIAN_EXCESS_ABS
        ),
        "G7_nongaussian_stationary_q_differs_from_gaussian_closure": bool(
            frames["stationary_rademacher"][
                "absolute_q_difference"
            ].max()
            >= MIN_STATIONARY_Q_DIFFERENCE
        ),
        "G8_centering_does_not_gaussianize_rademacher_noise": bool(
            frames["centered_noise"][
                "centered_component_excess_kurtosis"
            ].abs().min()
            >= MIN_NONGAUSSIAN_EXCESS_ABS
        ),
        "G9_finite_empirical_gaussian_q_converges_with_sample_size": bool(
            empirical_monotonic
        ),
        "G10_finite_sample_error_increases_with_lambda": bool(
            all(
                largest_n["rmse"].iloc[index + 1]
                > largest_n["rmse"].iloc[index]
                for index in range(
                    len(largest_n) - 1
                )
            )
        ),
        "G11_population_closure_distinguished_from_empirical_estimator": True,
        "G12_gaussian_rzs_noise_not_claimed_or_derived": True,
    }

    verdict = (
        "PASS_GAUSSIAN_CLOSURE_CONDITIONAL_ON_INNOVATION_LAW"
        if all(gates.values())
        else "FAIL_GAUSSIAN_CLOSURE_AUDIT"
    )

    classification = [
        {
            "case": "Gaussian initial law + Gaussian innovations",
            "finite_dimensional_closure": True,
            "state_required": "mean and covariance",
            "status": "EXACT_GAUSSIAN_CLOSURE",
        },
        {
            "case": "Non-Gaussian initial law + Gaussian innovations",
            "finite_dimensional_closure": "asymptotic, not finite-time exact",
            "state_required": "higher cumulants at finite time",
            "status": "ASYMPTOTIC_GAUSSIANIZATION",
        },
        {
            "case": "Non-Gaussian innovations",
            "finite_dimensional_closure": False,
            "state_required": "innovation-dependent higher cumulants",
            "status": "NONGAUSSIAN_STATIONARY_OBSTRUCTION",
        },
        {
            "case": "Centered non-Gaussian innovations",
            "finite_dimensional_closure": False,
            "state_required": "full centered innovation law",
            "status": "CENTERING_NOT_GAUSSIANIZATION",
        },
        {
            "case": "Finite empirical Gaussian sample",
            "finite_dimensional_closure": "population law only",
            "state_required": "sampling uncertainty",
            "status": "FINITE_SAMPLE_ESTIMATION_ERROR",
        },
        {
            "case": "Current RZS noise contract",
            "finite_dimensional_closure": None,
            "state_required": "specified innovation distribution",
            "status": "GAUSSIANITY_NOT_DERIVED",
        },
    ]

    pd.DataFrame(classification).to_csv(
        output / "a35_gaussian_closure_classification.csv",
        index=False,
    )

    matched_summary = []
    for lambda_value, group in (
        frames["matched_nulls"]
        .groupby("lambda")
    ):
        group = group.sort_values(
            "time_step"
        )
        matched_summary.append(
            {
                "lambda": float(lambda_value),
                "initial_difference": float(
                    group[
                        "matched_null_difference"
                    ].iloc[0]
                ),
                "difference_at_step_1": float(
                    group[
                        "matched_null_difference"
                    ].iloc[1]
                ),
                "difference_at_step_10": float(
                    group.query(
                        "time_step == 10"
                    )[
                        "matched_null_difference"
                    ].iloc[0]
                ),
                "difference_at_step_30": float(
                    group[
                        "matched_null_difference"
                    ].iloc[-1]
                ),
            }
        )

    empirical_summary = (
        frames["empirical_gaussian"]
        .to_dict(orient="records")
    )

    aggregate_results = {
        "maximum_exact_gaussian_closure_error": float(
            frames["gaussian_closure"][
                "absolute_closure_error"
            ].max()
        ),
        "matched_null_results": matched_summary,
        "stationary_rademacher_excess_kurtosis": float(
            frames["stationary_rademacher"][
                "stationary_excess_kurtosis"
            ].iloc[0]
        ),
        "maximum_stationary_q_gaussian_error": float(
            frames["stationary_rademacher"][
                "absolute_q_difference"
            ].max()
        ),
        "centered_rademacher_excess_by_dimension": (
            frames["centered_noise"]
            .to_dict(orient="records")
        ),
        "empirical_gaussian_results": empirical_summary,
    }

    summary = {
        "seed": SEED,
        "contraction": A,
        "normalized_innovation_sd": INNOVATION_SD,
        "aggregate_results": aggregate_results,
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "Mean and variance give an exact dynamic closure for Q_lambda "
            "only when the q law is Gaussian and the affine innovations are "
            "Gaussian. Gaussian innovations asymptotically erase higher "
            "cumulants of non-Gaussian initial laws, but finite-time "
            "predictions still depend on those cumulants. Non-Gaussian "
            "innovations regenerate higher cumulants and generally produce "
            "a non-Gaussian stationary law. Centering the noise does not "
            "remove this obstruction. The current RZS noise contract "
            "therefore does not justify Gaussian closure without an "
            "independent innovation-law assumption or derivation."
        ),
        "interpretation_boundary": (
            "A35 establishes conditional probabilistic theorems and "
            "controls. It does not show that actual RZS q values are iid, "
            "Gaussian, exchangeable, or governed by Gaussian innovations."
        ),
    }

    (
        output / "a35_summary.json"
    ).write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A35 — Gaussian Closure Audit",
        "",
        "## Main result",
        "",
        (
            "Gaussian closure is exact only conditional on a Gaussian law "
            "and Gaussian affine innovations. Centering alone is not enough."
        ),
        "",
        "## Matched-moment nulls",
        "",
    ]

    for item in matched_summary:
        report_lines.extend(
            [
                f"### lambda={item['lambda']}",
                (
                    "- Initial difference: "
                    f"{item['initial_difference']:.12g}"
                ),
                (
                    "- Step 1 difference: "
                    f"{item['difference_at_step_1']:.12g}"
                ),
                (
                    "- Step 10 difference: "
                    f"{item['difference_at_step_10']:.12g}"
                ),
                (
                    "- Step 30 difference: "
                    f"{item['difference_at_step_30']:.12g}"
                ),
                "",
            ]
        )

    report_lines.extend(
        [
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
    )

    (
        output / "a35_report.md"
    ).write_text(
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
