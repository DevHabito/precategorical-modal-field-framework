
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260810

A = 0.825
INNOVATION_SD = math.sqrt(1.0 - A * A)
LAMBDA_VALUES = (0.5, 1.0, 2.0)
BLOCK_SIZES = (1, 4, 16, 64, 256)

KERNEL_ROWS = 2500
KERNEL_DIMENSION = 64
KERNEL_BURN_IN = 140
KERNEL_LAMBDA = 1.0

MAX_EXACT_ERROR = 3e-12
MIN_STATIONARY_EXCESS_SPREAD = 0.8
MIN_STATIONARY_Q_SPREAD_LAMBDA_2 = 0.3
MAX_BLOCK_Q_ERROR_AT_256 = 0.001
MIN_KERNEL_MAX_PROBABILITY_SPREAD = 0.015
MIN_COMMON_SHOCK_LIMIT_EXCESS_ABS = 1.9


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


def normalize(values: np.ndarray, axis: int = -1) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    return values / values.sum(axis=axis, keepdims=True)


def innovation_excess(distribution: str) -> float:
    if distribution == "gaussian":
        return 0.0
    if distribution == "rademacher":
        return -2.0
    if distribution == "uniform":
        return -6.0 / 5.0
    if distribution == "laplace":
        return 3.0
    if distribution == "student8":
        return 6.0 / (8.0 - 4.0)
    raise ValueError(distribution)


def stationary_excess(distribution: str) -> float:
    factor = (1.0 - A * A) / (1.0 + A * A)
    return innovation_excess(distribution) * factor


def log_mgf_innovation(distribution: str, argument: float) -> float:
    """
    Innovations are centered and scaled to variance 1-A^2.
    """
    sigma = INNOVATION_SD

    if distribution == "gaussian":
        return 0.5 * sigma**2 * argument**2

    if distribution == "rademacher":
        return math.log(math.cosh(sigma * argument))

    if distribution == "uniform":
        x = math.sqrt(3.0) * sigma * argument
        if abs(x) < 1e-7:
            return (
                x**2 / 6.0
                - x**4 / 180.0
                + x**6 / 2835.0
            )
        return math.log(math.sinh(x) / x)

    if distribution == "laplace":
        scale = sigma / math.sqrt(2.0)
        product = scale * argument
        if abs(product) >= 1.0:
            return float("inf")
        return -math.log(1.0 - product**2)

    if distribution == "student8":
        # Every nonzero exponential moment diverges for a Student-t law.
        if argument == 0.0:
            return 0.0
        return float("inf")

    raise ValueError(distribution)


def stationary_log_mgf(distribution: str, argument: float) -> float:
    if distribution == "student8" and argument != 0.0:
        return float("inf")

    total = 0.0

    for power in range(10000):
        scaled_argument = argument * A**power
        contribution = log_mgf_innovation(
            distribution,
            scaled_argument,
        )

        if not math.isfinite(contribution):
            return contribution

        total += contribution

        if abs(contribution) < 1e-17:
            break
    else:
        raise RuntimeError("Stationary log-MGF series did not converge.")

    return total


def stationary_cumulant_audit() -> list[dict[str, object]]:
    rows = []

    for distribution in (
        "gaussian",
        "rademacher",
        "uniform",
        "laplace",
        "student8",
    ):
        excess = stationary_excess(distribution)

        rows.append(
            {
                "distribution": distribution,
                "stationary_mean": 0.0,
                "stationary_variance": 1.0,
                "innovation_excess_kurtosis": innovation_excess(
                    distribution
                ),
                "stationary_excess_kurtosis": excess,
                "stationary_fourth_cumulant": excess,
                "exponential_moments_exist_near_zero": (
                    distribution != "student8"
                ),
            }
        )

    return rows


def stationary_q_audit() -> list[dict[str, object]]:
    rows = []

    for lambda_value in LAMBDA_VALUES:
        for distribution in (
            "gaussian",
            "rademacher",
            "uniform",
            "laplace",
            "student8",
        ):
            log_mgf = stationary_log_mgf(
                distribution,
                -lambda_value,
            )

            if math.isfinite(log_mgf):
                q_value = -log_mgf / lambda_value
                defined = True
            else:
                q_value = float("-inf")
                defined = False

            rows.append(
                {
                    "distribution": distribution,
                    "lambda": lambda_value,
                    "stationary_q": q_value,
                    "q_defined": defined,
                    "gaussian_reference_q": -0.5 * lambda_value,
                    "absolute_gaussian_difference": (
                        abs(q_value + 0.5 * lambda_value)
                        if defined
                        else float("inf")
                    ),
                }
            )

    return rows


def block_q_universality_audit() -> list[dict[str, object]]:
    rows = []

    for distribution in (
        "gaussian",
        "rademacher",
        "uniform",
        "laplace",
        "student8",
    ):
        for lambda_value in LAMBDA_VALUES:
            previous_error = float("inf")

            for block_size in BLOCK_SIZES:
                argument = (
                    -lambda_value
                    / math.sqrt(block_size)
                )
                one_log_mgf = stationary_log_mgf(
                    distribution,
                    argument,
                )

                if math.isfinite(one_log_mgf):
                    block_q = (
                        -block_size
                        * one_log_mgf
                        / lambda_value
                    )
                    gaussian_q = -0.5 * lambda_value
                    error = abs(block_q - gaussian_q)
                    defined = True
                    nonincreasing = (
                        error <= previous_error + 1e-15
                    )
                    previous_error = error
                else:
                    block_q = float("-inf")
                    gaussian_q = -0.5 * lambda_value
                    error = float("inf")
                    defined = False
                    nonincreasing = False

                rows.append(
                    {
                        "distribution": distribution,
                        "lambda": lambda_value,
                        "block_size": block_size,
                        "block_q": block_q,
                        "gaussian_reference_q": gaussian_q,
                        "absolute_gaussian_error": error,
                        "q_defined": defined,
                        "nonincreasing_from_previous": nonincreasing,
                    }
                )

    return rows


def draw_innovation(
    distribution: str,
    shape: tuple[int, int],
    rng: np.random.Generator,
) -> np.ndarray:
    sigma = INNOVATION_SD

    if distribution == "gaussian":
        return rng.normal(0.0, sigma, size=shape)

    if distribution == "rademacher":
        return rng.choice(
            np.asarray([-sigma, sigma]),
            size=shape,
        )

    if distribution == "uniform":
        bound = math.sqrt(3.0) * sigma
        return rng.uniform(-bound, bound, size=shape)

    if distribution == "laplace":
        return rng.laplace(
            0.0,
            sigma / math.sqrt(2.0),
            size=shape,
        )

    if distribution == "student8":
        degrees = 8.0
        scale = sigma / math.sqrt(
            degrees / (degrees - 2.0)
        )
        return (
            rng.standard_t(degrees, size=shape)
            * scale
        )

    raise ValueError(distribution)


def operational_kernel_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for distribution in (
        "gaussian",
        "rademacher",
        "uniform",
        "laplace",
        "student8",
    ):
        state = np.zeros(
            (KERNEL_ROWS, KERNEL_DIMENSION),
            dtype=float,
        )

        for _ in range(KERNEL_BURN_IN):
            state = (
                A * state
                + draw_innovation(
                    distribution,
                    state.shape,
                    rng,
                )
            )

        row_mean = state.mean(
            axis=1,
            keepdims=True,
        )
        row_sd = state.std(
            axis=1,
            keepdims=True,
        )
        z = (state - row_mean) / row_sd

        logits = -KERNEL_LAMBDA * z
        logits -= logits.max(
            axis=1,
            keepdims=True,
        )
        probabilities = normalize(
            np.exp(logits),
            axis=1,
        )

        entropy = -np.sum(
            probabilities
            * np.log(probabilities),
            axis=1,
        )
        effective_count = 1.0 / np.sum(
            probabilities**2,
            axis=1,
        )
        maximum_probability = probabilities.max(
            axis=1,
        )

        rows.append(
            {
                "distribution": distribution,
                "rows": KERNEL_ROWS,
                "dimension": KERNEL_DIMENSION,
                "median_maximum_probability": float(
                    np.median(maximum_probability)
                ),
                "mean_maximum_probability": float(
                    maximum_probability.mean()
                ),
                "median_entropy": float(
                    np.median(entropy)
                ),
                "median_effective_count": float(
                    np.median(effective_count)
                ),
            }
        )

    return rows


def dependence_obstruction_audit() -> list[dict[str, float]]:
    rows = []
    rho = 0.25

    # Xi = sqrt(rho) C + sqrt(1-rho) Gi,
    # where C is unit Rademacher and Gi are iid standard Gaussian.
    # The variance-normalized block sum has Rademacher coefficient alpha_M.
    # Its excess kurtosis equals -2 alpha_M^4.
    for block_size in (
        1,
        4,
        16,
        64,
        256,
        1024,
    ):
        denominator_variance = (
            block_size
            + rho
            * block_size
            * (block_size - 1)
        )
        common_coefficient = (
            math.sqrt(rho)
            * block_size
            / math.sqrt(denominator_variance)
        )
        gaussian_coefficient_variance = (
            (1.0 - rho)
            * block_size
            / denominator_variance
        )
        excess = -2.0 * common_coefficient**4

        rows.append(
            {
                "block_size": block_size,
                "rho": rho,
                "common_shock_coefficient": common_coefficient,
                "idiosyncratic_gaussian_variance": (
                    gaussian_coefficient_variance
                ),
                "standardized_block_excess_kurtosis": excess,
            }
        )

    return rows


def main() -> None:
    output = Path("a37_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = r"""# A37 — Noise-Law Universality Audit

## Stationary affine law

For

\[
X_{t+1}=aX_t+\xi_t,\qquad |a|<1,
\]

with iid innovations independent of the past, the stationary characteristic
function is

\[
\phi_X(t)=\prod_{k=0}^{\infty}\phi_\xi(a^k t).
\]

When the cumulants exist,

\[
\kappa_r(X)=\frac{\kappa_r(\xi)}{1-a^r}.
\]

Matching innovation means and variances therefore fixes the stationary mean
and variance, but not higher cumulants.

## Exponential-score obstruction

The stationary effective score is

\[
Q_\lambda
=
-\lambda^{-1}\log E[e^{-\lambda X}].
\]

It depends on all cumulants for which the expansion is valid. Heavy-tailed
laws such as Student-t have no nonzero moment-generating function, so
\(Q_\lambda\) is not finite even though their variance may exist.

## Conditional coarse-graining universality

For \(M\) independent stationary copies,

\[
Y_M=M^{-1/2}\sum_{i=1}^{M}X_i,
\]

the log-MGF is

\[
\log E[e^{sY_M}]
=
M\log M_X(s/\sqrt M).
\]

If exponential moments are controlled near zero, the effective score tends
to the Gaussian value as \(M\to\infty\). Weak CLT convergence alone does not
guarantee convergence of exponential moments.

## Dependence obstruction

A shared non-Gaussian common factor can survive variance-normalized
coarse-graining. Independence or an adequate mixing condition is therefore
required for Gaussian universality.

## Boundary

The audit establishes conditional universality classes. It does not identify
the physical RZS innovation law or demonstrate independence across relational
components.
"""
    (
        output / "a37_theorem.md"
    ).write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    frames = {
        "cumulants": pd.DataFrame(
            stationary_cumulant_audit()
        ),
        "stationary_q": pd.DataFrame(
            stationary_q_audit()
        ),
        "block_q": pd.DataFrame(
            block_q_universality_audit()
        ),
        "kernel": pd.DataFrame(
            operational_kernel_audit(rng)
        ),
        "dependence": pd.DataFrame(
            dependence_obstruction_audit()
        ),
    }

    file_map = {
        "cumulants": (
            "a37_stationary_cumulants.csv"
        ),
        "stationary_q": (
            "a37_stationary_effective_score.csv"
        ),
        "block_q": (
            "a37_independent_block_universality.csv"
        ),
        "kernel": (
            "a37_operational_kernel_sensitivity.csv"
        ),
        "dependence": (
            "a37_dependence_obstruction.csv"
        ),
    }

    for key, frame in frames.items():
        frame.to_csv(
            output / file_map[key],
            index=False,
        )

    stationary_excess_values = (
        frames["cumulants"][
            "stationary_excess_kurtosis"
        ].to_numpy()
    )
    stationary_excess_spread = float(
        stationary_excess_values.max()
        - stationary_excess_values.min()
    )

    lambda_2_defined = frames["stationary_q"][
        (frames["stationary_q"]["lambda"] == 2.0)
        & (frames["stationary_q"]["q_defined"])
    ]
    stationary_q_spread_lambda_2 = float(
        lambda_2_defined[
            "stationary_q"
        ].max()
        - lambda_2_defined[
            "stationary_q"
        ].min()
    )

    light_tailed_block = (
        frames["block_q"]
        .query(
            "distribution in "
            "['gaussian', 'rademacher', 'uniform', 'laplace']"
        )
    )
    final_block = light_tailed_block[
        light_tailed_block["block_size"] == 256
    ]

    monotonic_light_tailed = True
    for _, group in (
        light_tailed_block
        .sort_values("block_size")
        .groupby(["distribution", "lambda"])
    ):
        errors = (
            group[
                "absolute_gaussian_error"
            ].to_numpy()
        )
        monotonic_light_tailed = (
            monotonic_light_tailed
            and all(
                errors[index + 1]
                <= errors[index] + 1e-15
                for index in range(
                    len(errors) - 1
                )
            )
        )

    kernel_max_probability_spread = float(
        frames["kernel"][
            "median_maximum_probability"
        ].max()
        - frames["kernel"][
            "median_maximum_probability"
        ].min()
    )

    student_q_rows = frames["stationary_q"][
        frames["stationary_q"]["distribution"] == "student8"
    ]
    student_block_rows = frames["block_q"][
        frames["block_q"]["distribution"] == "student8"
    ]

    gates = {
        "G1_stationary_characteristic_function_and_cumulant_formula_stated": True,
        "G2_equal_stationary_mean_variance_do_not_fix_higher_cumulants": bool(
            stationary_excess_spread
            >= MIN_STATIONARY_EXCESS_SPREAD
        ),
        "G3_light_tailed_stationary_effective_scores_depend_on_noise_law": bool(
            stationary_q_spread_lambda_2
            >= MIN_STATIONARY_Q_SPREAD_LAMBDA_2
        ),
        "G4_student_t_finite_variance_does_not_make_q_lambda_finite": bool(
            (~student_q_rows["q_defined"]).all()
        ),
        "G5_independent_light_tailed_block_scores_converge_to_gaussian": bool(
            monotonic_light_tailed
            and final_block[
                "absolute_gaussian_error"
            ].max()
            <= MAX_BLOCK_Q_ERROR_AT_256
        ),
        "G6_student_t_block_q_remains_undefined_under_finite_block_averaging": bool(
            (~student_block_rows["q_defined"]).all()
        ),
        "G7_common_nongaussian_factor_blocks_gaussian_universality": bool(
            abs(
                frames["dependence"][
                    "standardized_block_excess_kurtosis"
                ].iloc[-1]
            )
            >= MIN_COMMON_SHOCK_LIMIT_EXCESS_ABS
        ),
        "G8_standardized_operational_kernel_retains_noise_law_sensitivity": bool(
            kernel_max_probability_spread
            >= MIN_KERNEL_MAX_PROBABILITY_SPREAD
        ),
        "G9_variance_matching_and_centering_are_not_exact_universality_principles": True,
        "G10_universality_requires_independence_or_mixing_and_exponential_moment_control": True,
        "G11_no_physical_rzs_noise_law_claimed": True,
    }

    verdict = (
        "PASS_PARTIAL_NOISE_UNIVERSALITY_WITH_MOMENT_AND_DEPENDENCE_LIMITS"
        if all(gates.values())
        else "FAIL_NOISE_UNIVERSALITY_AUDIT"
    )

    classification = [
        {
            "regime": "single stationary component, matched variance",
            "universal": False,
            "required_information": "innovation higher cumulants or full law",
            "status": "NO_EXACT_UNIVERSALITY",
        },
        {
            "regime": "independent block sums with local exponential moments",
            "universal": "asymptotically Gaussian for audited score",
            "required_information": "independence and MGF control",
            "status": "CONDITIONAL_COARSE_GRAIN_UNIVERSALITY",
        },
        {
            "regime": "finite-variance Student-t innovations",
            "universal": False,
            "required_information": "tail class",
            "status": "Q_LAMBDA_UNDEFINED",
        },
        {
            "regime": "shared non-Gaussian common shock",
            "universal": False,
            "required_information": "dependence structure",
            "status": "DEPENDENCE_OBSTRUCTION",
        },
        {
            "regime": "row-standardized exponential transition kernel",
            "universal": False,
            "required_information": "stationary shape after standardization",
            "status": "OPERATIONAL_LAW_SENSITIVITY",
        },
        {
            "regime": "actual RZS innovations",
            "universal": None,
            "required_information": "noise law, dependence, and tail control",
            "status": "NOT_ESTABLISHED",
        },
    ]

    pd.DataFrame(classification).to_csv(
        output / "a37_universality_classification.csv",
        index=False,
    )

    stationary_q_summary = []
    for lambda_value, group in (
        frames["stationary_q"]
        .groupby("lambda")
    ):
        defined_group = group[
            group["q_defined"]
        ]
        stationary_q_summary.append(
            {
                "lambda": float(lambda_value),
                "minimum_defined_q": float(
                    defined_group[
                        "stationary_q"
                    ].min()
                ),
                "maximum_defined_q": float(
                    defined_group[
                        "stationary_q"
                    ].max()
                ),
                "defined_q_spread": float(
                    defined_group[
                        "stationary_q"
                    ].max()
                    - defined_group[
                        "stationary_q"
                    ].min()
                ),
            }
        )

    aggregate_results = {
        "stationary_excess_kurtosis_spread": (
            stationary_excess_spread
        ),
        "stationary_q_results": (
            stationary_q_summary
        ),
        "maximum_light_tailed_block_q_error_at_256": float(
            final_block[
                "absolute_gaussian_error"
            ].max()
        ),
        "kernel_median_max_probability_spread": (
            kernel_max_probability_spread
        ),
        "common_shock_excess_at_block_1024": float(
            frames["dependence"][
                "standardized_block_excess_kurtosis"
            ].iloc[-1]
        ),
    }

    summary = {
        "seed": SEED,
        "contraction": A,
        "innovation_sd": INNOVATION_SD,
        "aggregate_results": aggregate_results,
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "Matching innovation mean and variance fixes the stationary mean "
            "and variance of the affine q process but not its higher "
            "cumulants, effective score, or standardized transition-kernel "
            "statistics. Independent coarse-graining produces strong "
            "Gaussian universality for light-tailed laws with controlled "
            "exponential moments. That universality fails as a statement "
            "about Q_lambda for Student-t tails, whose moment-generating "
            "function is infinite, and it can be blocked by shared "
            "non-Gaussian dependence. The RZS noise law is therefore "
            "macroscopically dispensable only under additional tail and "
            "dependence conditions that are not yet derived."
        ),
        "interpretation_boundary": (
            "A37 identifies universality classes in an affine stationary "
            "model. It does not prove that RZS relational components are "
            "independent copies, that their innovations have exponential "
            "moments, or that the audited block sum is the physical "
            "coarse-graining operation."
        ),
    }

    (
        output / "a37_summary.json"
    ).write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A37 — Noise-Law Universality",
        "",
        "## Main result",
        "",
        (
            "Noise-law details survive at the stationary component and "
            "operational-kernel levels. Conditional universality appears "
            "under independent coarse-graining with exponential-moment "
            "control."
        ),
        "",
        "## Stationary effective-score spread",
        "",
    ]

    for item in stationary_q_summary:
        report_lines.extend(
            [
                f"### lambda={item['lambda']}",
                (
                    "- Minimum defined Q: "
                    f"{item['minimum_defined_q']:.12g}"
                ),
                (
                    "- Maximum defined Q: "
                    f"{item['maximum_defined_q']:.12g}"
                ),
                (
                    "- Spread: "
                    f"{item['defined_q_spread']:.12g}"
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
        output / "a37_report.md"
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
