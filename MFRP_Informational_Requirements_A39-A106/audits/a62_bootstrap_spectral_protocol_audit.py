#!/usr/bin/env python3
"""A62 audit: bootstrap spectral-radius calibration and coverage study.

Purpose
-------
Estimate a covariance matrix Sigma_hat from repeated 3-channel calibration
residuals and construct a spectral confidence ball

    ||Sigma - Sigma_hat||_2 <= tau_hat.

The raw nonparametric bootstrap radius is audited rather than presumed valid.
A simulation-only safety multiplier is selected on calibration seeds and
tested on independent validation seeds.

Two model families are kept separate:
- Gaussian calibration residuals;
- multivariate t_5 residuals as a heavy-tail stress family.

The resulting factors are model-conditional empirical calibrations, not
universal finite-sample confidence theorems.

When the covariance ball contains the true covariance and the inflated upper
matrix remains inside the A58 box, A61 guarantees that the propagated upper
risk covers the true A60 robust risk.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A58_SCRIPT = HERE / "a58_independent_three_channel_error_audit.py"
A60_SCRIPT = HERE / "a60_general_covariance_matrix_audit.py"
A61_RESULTS = HERE / "a61_spectral_covariance_uncertainty_results.json"

ALPHA = 0.05
BOOTSTRAP_REPLICATES = 399
CALIBRATION_REPLICATES = 500
VALIDATION_REPLICATES = 1000
CALIBRATION_TARGET = 0.96
SAMPLE_SIZES = [30, 60, 120]
FACTOR_GRID = np.round(np.arange(1.0, 3.01, 0.05), 10)
BOX_VARIANCE_LIMIT = 1.0 / 400.0
BASE_SEED = 20260720


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def sample_covariance(data: np.ndarray) -> np.ndarray:
    centred = data - data.mean(axis=0, keepdims=True)
    return centred.T @ centred / (data.shape[0] - 1)


def symmetric_spectral_norm(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvalsh(matrix))))


def bootstrap_spectral_radius(
    data: np.ndarray,
    rng: np.random.Generator,
) -> tuple[float, np.ndarray]:
    n = data.shape[0]
    indices = rng.integers(
        0,
        n,
        size=(BOOTSTRAP_REPLICATES, n),
    )
    samples = data[indices]
    centred = samples - samples.mean(axis=1, keepdims=True)
    covariances = np.einsum(
        "bni,bnj->bij",
        centred,
        centred,
    ) / (n - 1)

    estimate = sample_covariance(data)
    deviations = covariances - estimate
    eigenvalues = np.linalg.eigvalsh(deviations)
    norms = np.max(np.abs(eigenvalues), axis=1)

    # Conservative empirical quantile on the finite bootstrap sample.
    order_index = (
        math.ceil(
            (BOOTSTRAP_REPLICATES + 1)
            * (1.0 - ALPHA)
        )
        - 1
    )
    order_index = min(
        max(order_index, 0),
        BOOTSTRAP_REPLICATES - 1,
    )
    radius = float(
        np.partition(norms, order_index)[order_index]
    )
    return radius, estimate


def generate_residuals(
    rng: np.random.Generator,
    covariance: np.ndarray,
    sample_size: int,
    distribution: str,
) -> np.ndarray:
    gaussian = rng.multivariate_normal(
        np.zeros(3),
        covariance,
        size=sample_size,
    )

    if distribution == "gaussian":
        return gaussian

    if distribution == "student_t_5":
        chi_square = rng.chisquare(
            5,
            size=sample_size,
        )
        # E[3/chi2_5] = 1, so the covariance remains covariance.
        return gaussian * np.sqrt(3.0 / chi_square)[:, None]

    raise ValueError(f"Unknown distribution: {distribution}")


def wilson_interval(
    successes: int,
    trials: int,
    z: float = 1.959963984540054,
) -> tuple[float, float]:
    proportion = successes / trials
    denominator = 1.0 + z * z / trials
    centre = (
        proportion
        + z * z / (2.0 * trials)
    ) / denominator
    radius = (
        z
        * math.sqrt(
            proportion * (1.0 - proportion) / trials
            + z * z / (4.0 * trials * trials)
        )
        / denominator
    )
    return centre - radius, centre + radius


def build_risk_coefficients() -> dict[str, Any]:
    a52 = load_module(A52_SCRIPT, "a52_for_a62")
    a58 = load_module(A58_SCRIPT, "a58_for_a62")
    a60 = load_module(A60_SCRIPT, "a60_for_a62")

    certificate = a58.build_certificate(a52)
    coefficients = a60.extract_linear_fractional(
        certificate["ratio"],
        [
            certificate["u2"],
            certificate["ub"],
            certificate["ui"],
        ],
    )

    s = certificate["s"]
    s_star = a52.s_star

    n0 = float(sp.N(coefficients["n0"].subs(s, s_star), 60))
    d0 = float(sp.N(coefficients["d0"].subs(s, s_star), 60))
    n = np.array(
        [
            float(sp.N(value.subs(s, s_star), 60))
            for value in coefficients["n"]
        ],
        dtype=float,
    )
    d = np.array(
        [
            float(sp.N(value.subs(s, s_star), 60))
            for value in coefficients["d"]
        ],
        dtype=float,
    )

    centre = np.array([1.05, 1.05, 1.05], dtype=float)
    a = n0 + float(n @ centre)
    b = d0 + float(d @ centre)

    return {
        "n0": n0,
        "d0": d0,
        "n": n,
        "d": d,
        "a": a,
        "b": b,
        "centre": centre,
    }


def robust_ratio(
    covariance: np.ndarray,
    coefficients: dict[str, Any],
) -> float:
    n = coefficients["n"]
    d = coefficients["d"]
    a = coefficients["a"]
    b = coefficients["b"]

    coefficient_a = b * b - float(d @ covariance @ d)
    coefficient_b = (
        -2.0 * a * b
        + 2.0 * float(n @ covariance @ d)
    )
    coefficient_c = (
        a * a
        - float(n @ covariance @ n)
    )

    discriminant = (
        coefficient_b * coefficient_b
        - 4.0 * coefficient_a * coefficient_c
    )
    if discriminant < -1e-7:
        raise RuntimeError(
            f"Negative quadratic discriminant: {discriminant}"
        )
    discriminant = max(discriminant, 0.0)

    roots = [
        (
            -coefficient_b
            + math.sqrt(discriminant)
        )
        / (2.0 * coefficient_a),
        (
            -coefficient_b
            - math.sqrt(discriminant)
        )
        / (2.0 * coefficient_a),
    ]

    admissible = []
    for candidate in roots:
        vector = n - candidate * d
        support_squared = float(
            vector @ covariance @ vector
        )
        support_squared = max(support_squared, 0.0)
        residual = (
            a
            - candidate * b
            + math.sqrt(support_squared)
        )
        branch = a - candidate * b
        if abs(residual) < 2e-5 and branch <= 1e-8:
            admissible.append(candidate)

    if len(admissible) != 1:
        raise RuntimeError(
            f"Expected one admissible root, got {admissible}"
        )
    return admissible[0]


def robust_risk(
    covariance: np.ndarray,
    coefficients: dict[str, Any],
) -> float:
    return 0.5 * math.log2(
        robust_ratio(covariance, coefficients)
    )


def covariance_scenarios() -> dict[str, np.ndarray]:
    diagonal = np.diag(
        [0.0009, 0.000625, 0.000225]
    )

    standard_deviations = np.sqrt(np.diag(diagonal))

    positive_correlation = np.array(
        [
            [1.0, 0.6, 0.3],
            [0.6, 1.0, 0.25],
            [0.3, 0.25, 1.0],
        ],
        dtype=float,
    )

    mixed_correlation = np.array(
        [
            [1.0, -0.4, -0.2],
            [-0.4, 1.0, 0.2],
            [-0.2, 0.2, 1.0],
        ],
        dtype=float,
    )

    scale = np.diag(standard_deviations)

    return {
        "diagonal": diagonal,
        "positive_correlation": (
            scale
            @ positive_correlation
            @ scale
        ),
        "mixed_correlation": (
            scale
            @ mixed_correlation
            @ scale
        ),
    }


def run_ratio_cell(
    covariance: np.ndarray,
    sample_size: int,
    distribution: str,
    replicates: int,
    seed: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    ratios = np.empty(replicates, dtype=float)

    for replicate in range(replicates):
        data = generate_residuals(
            rng,
            covariance,
            sample_size,
            distribution,
        )
        radius, estimate = bootstrap_spectral_radius(
            data,
            rng,
        )
        error = symmetric_spectral_norm(
            estimate - covariance
        )
        ratios[replicate] = error / radius

    return ratios


def choose_factor(
    calibration_cells: dict[str, np.ndarray],
) -> tuple[float, list[dict[str, Any]]]:
    diagnostics = []

    for factor in FACTOR_GRID:
        coverages = {
            name: float(np.mean(ratios <= factor))
            for name, ratios in calibration_cells.items()
        }
        minimum = min(coverages.values())
        diagnostics.append(
            {
                "factor": float(factor),
                "minimum_coverage": minimum,
                "coverages": coverages,
            }
        )

        if minimum >= CALIBRATION_TARGET:
            return float(factor), diagnostics

    raise RuntimeError(
        "No factor in the declared grid met the calibration target"
    )


def validate_cell(
    covariance: np.ndarray,
    sample_size: int,
    distribution: str,
    factor: float,
    replicates: int,
    seed: int,
    risk_coefficients: dict[str, Any],
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)

    raw_successes = 0
    calibrated_successes = 0
    raw_contract_valid = 0
    calibrated_contract_valid = 0
    raw_certified_joint = 0
    calibrated_certified_joint = 0
    raw_actual_risk_success = 0
    calibrated_actual_risk_success = 0
    implication_violations_raw = 0
    implication_violations_calibrated = 0

    ratios = np.empty(replicates, dtype=float)
    radii = np.empty(replicates, dtype=float)
    errors = np.empty(replicates, dtype=float)

    true_risk = robust_risk(
        covariance,
        risk_coefficients,
    )

    identity = np.eye(3)

    for replicate in range(replicates):
        data = generate_residuals(
            rng,
            covariance,
            sample_size,
            distribution,
        )
        radius, estimate = bootstrap_spectral_radius(
            data,
            rng,
        )
        error = symmetric_spectral_norm(
            estimate - covariance
        )

        raw_cover = error <= radius
        calibrated_radius = factor * radius
        calibrated_cover = error <= calibrated_radius

        raw_upper = estimate + radius * identity
        calibrated_upper = (
            estimate
            + calibrated_radius * identity
        )

        raw_valid = bool(
            np.min(np.linalg.eigvalsh(raw_upper)) > 0.0
            and np.max(np.diag(raw_upper))
            <= BOX_VARIANCE_LIMIT + 1e-15
        )
        calibrated_valid = bool(
            np.min(np.linalg.eigvalsh(calibrated_upper)) > 0.0
            and np.max(np.diag(calibrated_upper))
            <= BOX_VARIANCE_LIMIT + 1e-15
        )

        raw_successes += int(raw_cover)
        calibrated_successes += int(calibrated_cover)
        raw_contract_valid += int(raw_valid)
        calibrated_contract_valid += int(calibrated_valid)

        raw_certified_joint += int(raw_cover and raw_valid)
        calibrated_certified_joint += int(
            calibrated_cover
            and calibrated_valid
        )

        if raw_valid:
            raw_upper_risk = robust_risk(
                raw_upper,
                risk_coefficients,
            )
            raw_risk_cover = (
                raw_upper_risk
                + 2e-12
                >= true_risk
            )
            raw_actual_risk_success += int(
                raw_risk_cover
            )
            if raw_cover and not raw_risk_cover:
                implication_violations_raw += 1

        if calibrated_valid:
            calibrated_upper_risk = robust_risk(
                calibrated_upper,
                risk_coefficients,
            )
            calibrated_risk_cover = (
                calibrated_upper_risk
                + 2e-12
                >= true_risk
            )
            calibrated_actual_risk_success += int(
                calibrated_risk_cover
            )
            if (
                calibrated_cover
                and not calibrated_risk_cover
            ):
                implication_violations_calibrated += 1

        ratios[replicate] = error / radius
        radii[replicate] = radius
        errors[replicate] = error

    raw_interval = wilson_interval(
        raw_successes,
        replicates,
    )
    calibrated_interval = wilson_interval(
        calibrated_successes,
        replicates,
    )

    return {
        "sample_size": sample_size,
        "distribution": distribution,
        "factor": factor,
        "replicates": replicates,
        "raw_coverage": raw_successes / replicates,
        "raw_wilson_95": list(raw_interval),
        "calibrated_coverage": (
            calibrated_successes
            / replicates
        ),
        "calibrated_wilson_95": list(
            calibrated_interval
        ),
        "raw_contract_valid_rate": (
            raw_contract_valid
            / replicates
        ),
        "calibrated_contract_valid_rate": (
            calibrated_contract_valid
            / replicates
        ),
        "raw_certified_joint_rate": (
            raw_certified_joint
            / replicates
        ),
        "calibrated_certified_joint_rate": (
            calibrated_certified_joint
            / replicates
        ),
        "raw_actual_risk_coverage_among_valid": (
            raw_actual_risk_success
            / raw_contract_valid
            if raw_contract_valid
            else None
        ),
        "calibrated_actual_risk_coverage_among_valid": (
            calibrated_actual_risk_success
            / calibrated_contract_valid
            if calibrated_contract_valid
            else None
        ),
        "implication_violations_raw": (
            implication_violations_raw
        ),
        "implication_violations_calibrated": (
            implication_violations_calibrated
        ),
        "mean_bootstrap_radius": float(
            np.mean(radii)
        ),
        "mean_true_spectral_error": float(
            np.mean(errors)
        ),
        "ratio_quantiles": {
            "0.50": float(np.quantile(ratios, 0.50)),
            "0.90": float(np.quantile(ratios, 0.90)),
            "0.95": float(
                np.quantile(
                    ratios,
                    0.95,
                    method="higher",
                )
            ),
            "0.99": float(
                np.quantile(
                    ratios,
                    0.99,
                    method="higher",
                )
            ),
        },
        "true_robust_risk": true_risk,
    }


def main() -> None:
    for path in [
        A52_SCRIPT,
        A58_SCRIPT,
        A60_SCRIPT,
        A61_RESULTS,
    ]:
        if not path.exists():
            raise FileNotFoundError(path)

    a61_results = json.loads(
        A61_RESULTS.read_text(encoding="utf-8")
    )
    risk_coefficients = build_risk_coefficients()
    scenarios = covariance_scenarios()

    calibration_cells_gaussian: dict[str, np.ndarray] = {}
    calibration_cells_t5: dict[str, np.ndarray] = {}

    seed_counter = 0

    for scenario_name, covariance in scenarios.items():
        for sample_size in SAMPLE_SIZES:
            seed_counter += 1
            key = f"{scenario_name}_n{sample_size}"
            calibration_cells_gaussian[key] = run_ratio_cell(
                covariance,
                sample_size,
                "gaussian",
                CALIBRATION_REPLICATES,
                BASE_SEED + seed_counter,
            )

    positive_covariance = scenarios[
        "positive_correlation"
    ]

    for sample_size in SAMPLE_SIZES:
        seed_counter += 1
        key = f"student_t_5_positive_n{sample_size}"
        calibration_cells_t5[key] = run_ratio_cell(
            positive_covariance,
            sample_size,
            "student_t_5",
            CALIBRATION_REPLICATES,
            BASE_SEED + seed_counter,
        )

    gaussian_factor, gaussian_factor_trace = choose_factor(
        calibration_cells_gaussian
    )
    t5_factor, t5_factor_trace = choose_factor(
        calibration_cells_t5
    )

    validation_cells = []
    validation_seed_base = BASE_SEED + 100000

    for scenario_index, (
        scenario_name,
        covariance,
    ) in enumerate(scenarios.items()):
        for size_index, sample_size in enumerate(
            SAMPLE_SIZES
        ):
            seed = (
                validation_seed_base
                + 1000 * scenario_index
                + size_index
            )
            cell = validate_cell(
                covariance,
                sample_size,
                "gaussian",
                gaussian_factor,
                VALIDATION_REPLICATES,
                seed,
                risk_coefficients,
            )
            cell["scenario"] = scenario_name
            cell["model_family"] = "gaussian"
            validation_cells.append(cell)

    for size_index, sample_size in enumerate(
        SAMPLE_SIZES
    ):
        seed = (
            validation_seed_base
            + 10000
            + size_index
        )
        cell = validate_cell(
            positive_covariance,
            sample_size,
            "student_t_5",
            t5_factor,
            VALIDATION_REPLICATES,
            seed,
            risk_coefficients,
        )
        cell["scenario"] = (
            "positive_correlation"
        )
        cell["model_family"] = (
            "student_t_5"
        )
        validation_cells.append(cell)

    gaussian_validation = [
        cell
        for cell in validation_cells
        if cell["model_family"] == "gaussian"
    ]
    t5_validation = [
        cell
        for cell in validation_cells
        if cell["model_family"] == "student_t_5"
    ]

    raw_gaussian_minimum = min(
        cell["raw_coverage"]
        for cell in gaussian_validation
    )
    calibrated_gaussian_minimum = min(
        cell["calibrated_coverage"]
        for cell in gaussian_validation
    )
    raw_t5_minimum = min(
        cell["raw_coverage"]
        for cell in t5_validation
    )
    calibrated_t5_minimum = min(
        cell["calibrated_coverage"]
        for cell in t5_validation
    )

    gaussian_wilson_compatible = all(
        lower <= 0.95 <= upper
        or cell["calibrated_coverage"] >= 0.95
        for cell in gaussian_validation
        for lower, upper in [
            cell["calibrated_wilson_95"]
        ]
    )
    t5_wilson_compatible = all(
        lower <= 0.95 <= upper
        or cell["calibrated_coverage"] >= 0.95
        for cell in t5_validation
        for lower, upper in [
            cell["calibrated_wilson_95"]
        ]
    )

    implication_violations = sum(
        cell[
            "implication_violations_calibrated"
        ]
        for cell in validation_cells
    )

    gates = {
        "A61_complete_audit_passed": bool(
            all(a61_results["gates"].values())
        ),
        "calibration_and_validation_seeds_disjoint": True,
        "raw_bootstrap_undercoverage_detected": bool(
            raw_gaussian_minimum < 0.95
            and raw_t5_minimum < 0.95
        ),
        "gaussian_factor_found_in_declared_grid": bool(
            1.0 <= gaussian_factor <= 3.0
        ),
        "heavy_tail_factor_found_in_declared_grid": bool(
            1.0 <= t5_factor <= 3.0
        ),
        "heavy_tail_factor_exceeds_gaussian_factor": bool(
            t5_factor > gaussian_factor
        ),
        "gaussian_validation_compatible_with_95_percent": bool(
            gaussian_wilson_compatible
        ),
        "heavy_tail_validation_compatible_with_95_percent": bool(
            t5_wilson_compatible
        ),
        "A61_risk_implication_has_no_violations": bool(
            implication_violations == 0
        ),
        "all_covariance_scenarios_positive_definite": bool(
            all(
                np.min(np.linalg.eigvalsh(covariance))
                > 0
                for covariance in scenarios.values()
            )
        ),
    }

    verdict = (
        "PASS_MODEL_CONDITIONAL_BOOTSTRAP_SPECTRAL_PROTOCOL_RAW_BOOTSTRAP_REJECTED"
        if all(gates.values())
        else "FAIL_A62_BOOTSTRAP_COVERAGE_AUDIT"
    )

    result = {
        "audit": (
            "A62_BOOTSTRAP_SPECTRAL_COVARIANCE_PROTOCOL"
        ),
        "configuration": {
            "alpha": ALPHA,
            "bootstrap_replicates": BOOTSTRAP_REPLICATES,
            "calibration_replicates_per_cell": (
                CALIBRATION_REPLICATES
            ),
            "validation_replicates_per_cell": (
                VALIDATION_REPLICATES
            ),
            "calibration_target": (
                CALIBRATION_TARGET
            ),
            "sample_sizes": SAMPLE_SIZES,
            "factor_grid": [
                float(FACTOR_GRID[0]),
                float(FACTOR_GRID[-1]),
                0.05,
            ],
            "base_seed": BASE_SEED,
            "covariance_quantile_rule": (
                "higher empirical quantile at "
                "ceil((B+1)*(1-alpha))"
            ),
        },
        "protocol": {
            "estimate": (
                "unbiased sample covariance after "
                "sample-mean removal"
            ),
            "bootstrap": (
                "nonparametric row bootstrap"
            ),
            "raw_radius": (
                "95th percentile of "
                "||Sigma_hat_star-Sigma_hat||_2"
            ),
            "calibrated_radius": (
                "c_model * raw_radius"
            ),
            "upper_covariance": (
                "Sigma_hat + calibrated_radius * I"
            ),
            "risk_propagation": (
                "A60/A61 exact robust quadratic root"
            ),
            "out_of_contract_rule": (
                "do not issue an A60 certificate when "
                "max diagonal of upper covariance exceeds 1/400"
            ),
        },
        "model_conditional_factors": {
            "gaussian": gaussian_factor,
            "student_t_5": t5_factor,
            "interpretation": (
                "Factors were selected on calibration seeds "
                "to reach at least 96 percent empirical "
                "coverage in every declared cell, then "
                "evaluated on independent validation seeds."
            ),
        },
        "calibration_traces": {
            "gaussian": gaussian_factor_trace,
            "student_t_5": t5_factor_trace,
        },
        "validation_cells": validation_cells,
        "validation_summary": {
            "raw_gaussian_minimum_coverage": (
                raw_gaussian_minimum
            ),
            "calibrated_gaussian_minimum_coverage": (
                calibrated_gaussian_minimum
            ),
            "raw_student_t_5_minimum_coverage": (
                raw_t5_minimum
            ),
            "calibrated_student_t_5_minimum_coverage": (
                calibrated_t5_minimum
            ),
            "minimum_calibrated_contract_valid_rate_gaussian": min(
                cell["calibrated_contract_valid_rate"]
                for cell in gaussian_validation
            ),
            "minimum_calibrated_contract_valid_rate_student_t_5": min(
                cell["calibrated_contract_valid_rate"]
                for cell in t5_validation
            ),
            "A61_implication_violations": (
                implication_violations
            ),
        },
        "formal_results": [
            (
                "the raw nonparametric bootstrap spectral "
                "radius undercovers in audited finite samples"
            ),
            (
                "a model-conditional safety factor can be "
                "selected on calibration simulations and "
                "tested on independent validation simulations"
            ),
            (
                "the heavy-tailed family requires a larger "
                "factor than the Gaussian family"
            ),
            (
                "when the covariance ball covers and remains "
                "inside the A58 box, the A61 risk upper bound "
                "covers with no observed implication violation"
            ),
            (
                "contract availability must be reported "
                "separately from statistical coverage"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The calibrated multipliers are empirical and "
            "model-conditional. They are not universal "
            "finite-sample confidence constants. Gaussian "
            "and Student-t_5 families are audited separately; "
            "other distributions require new calibration or "
            "a theorem with explicit tail assumptions."
        ),
    }

    output_path = HERE / (
        "a62_bootstrap_spectral_protocol_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    template = {
        "input": {
            "calibration_residuals_csv": (
                "rows are repeated calibrations; "
                "columns are u2, u_beta, u_infinity"
            ),
            "confidence_level": 0.95,
            "bootstrap_replicates": 399,
            "model_family": (
                "gaussian or student_t_5 after "
                "separate validation"
            ),
            "safety_factor": {
                "gaussian": gaussian_factor,
                "student_t_5": t5_factor,
            },
        },
        "outputs": {
            "covariance_estimate": "3x3 matrix",
            "raw_spectral_radius": "scalar",
            "calibrated_spectral_radius": "scalar",
            "upper_covariance": (
                "Sigma_hat + tau_calibrated*I"
            ),
            "contract_status": (
                "valid only if max diagonal <= 0.0025"
            ),
            "robust_risk_upper": (
                "A60 quadratic root when contract valid"
            ),
        },
    }

    template_path = HERE / (
        "a62_bootstrap_protocol_template.json"
    )
    template_path.write_text(
        json.dumps(template, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gaussian_factor": gaussian_factor,
        "student_t_5_factor": t5_factor,
        "raw_gaussian_minimum_coverage": (
            raw_gaussian_minimum
        ),
        "calibrated_gaussian_minimum_coverage": (
            calibrated_gaussian_minimum
        ),
        "raw_student_t_5_minimum_coverage": (
            raw_t5_minimum
        ),
        "calibrated_student_t_5_minimum_coverage": (
            calibrated_t5_minimum
        ),
        "failed_gates": [
            name
            for name, value in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
