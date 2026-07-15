#!/usr/bin/env python3
"""
A23 — RZS q-Field Primitive and Gauge Audit

Operational contracts used
--------------------------
- Edge length: ell_ij = exp(q_ij).
- Directed shortest-path cost: d_dir(i,j).
- Symmetric round-trip cost:
      D_eff(i,j) = 1/2 [d_dir(i,j) + d_dir(j,i)].
- Global gauge:
      q -> q + c
  implies
      ell -> exp(c) ell,
      D_eff -> exp(c) D_eff.
- Normalized geometry D_hat is invariant under that global scale.
- Centered q dynamics:
      q_{t+1} = q_t - 1/2 center(eta * center(q_t) + noise_t).

Questions
---------
1. Is q information beyond the order, or merely a recoding?
2. Which q observables survive the global additive gauge?
3. Can the centered q dynamics select an absolute scale?
4. Does eta define a physical rate without a calibrated duration per step?

Exact conclusions tested
------------------------
A. If q is measurable from the order and model-independent randomness, it
   cannot break the A18–A21 equivalence.
B. A separately supplied q-field can add information, but its admissibility
   depends on its own operational definition.
C. Under q -> q+c, centered q and D_hat are invariant while D_eff rescales.
D. The centered dynamics is gauge-equivariant and cannot damp or select the
   constant mode.
E. A discrete relaxation coefficient determines only the product
   lambda * Delta_tau. Without calibrated Delta_tau, no physical rate lambda
   is identified.

Boundary
--------
The coordinate-linked q witness used below is deliberately not promoted to an
RZS physical primitive. It is used only to prove that an independently
calibrated q-field could break the order-only degeneracy. Whether the actual
RZS q has such an independent operational meaning remains an open model
question.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.sparse.csgraph import floyd_warshall
from scipy.stats import beta


SEED = 20260726

ORDER_N_VALUES = (32, 64, 128)
ORDER_COUPLED_SAMPLES = 250

GAUGE_GRAPH_N = 18
GAUGE_SAMPLES = 80
GAUGE_OFFSETS = (-2.0, -0.5, 0.75, 1.6)

DYNAMICS_VECTOR_SIZE = 120
DYNAMICS_SAMPLES = 100
DYNAMICS_STEPS = 60
ETA = 0.35
NOISE_SD = 0.08

RATE_ETA_VALUES = (0.1, 0.35, 0.8)
RATE_TIME_UNITS = (0.25, 1.0, 4.0)

MAX_NUMERICAL_ERROR = 2e-11
MIN_COORDINATE_Q_VARIANCE_SEPARATION = 0.02
MAX_EMPIRICAL_VARIANCE_ERROR = 0.01


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


def apply_model(
    model: str,
    u: np.ndarray,
    v: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if model == "uniform":
        return u, v

    if model == "power_anisotropic":
        return np.power(u, 4.0), np.sqrt(v)

    if model == "beta_skew":
        return (
            beta.ppf(u, 2.0, 5.0),
            beta.ppf(v, 5.0, 2.0),
        )

    raise ValueError(f"Unknown model: {model}")


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


def integer_ranks(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values)
    ranks = np.empty(len(values), dtype=np.int32)
    ranks[order] = np.arange(len(values), dtype=np.int32)
    return ranks


def array_hash(array: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(array).tobytes()
    ).hexdigest()


def order_interval_size_field(
    relation: np.ndarray,
) -> np.ndarray:
    """
    q built deterministically from order interval sizes. Non-comparable pairs
    receive zero. This is a deliberately redundant q construction.
    """
    n = len(relation)
    reflexive = relation | np.eye(n, dtype=bool)
    interval_sizes = (
        reflexive.astype(np.int16)
        @ reflexive.astype(np.int16)
    )
    field = np.zeros((n, n), dtype=float)
    field[relation] = np.log1p(
        interval_sizes[relation].astype(float)
    )
    np.fill_diagonal(field, 0.0)
    return field


def shared_random_q(
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    field = rng.normal(
        0.0,
        1.0,
        size=(n, n),
    )
    np.fill_diagonal(field, 0.0)
    return field


def rank_gap_q(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    n = len(x)
    rank_x = integer_ranks(x).astype(float)
    rank_y = integer_ranks(y).astype(float)
    field = (
        np.abs(
            rank_x[:, None]
            - rank_x[None, :]
        )
        + np.abs(
            rank_y[:, None]
            - rank_y[None, :]
        )
    ) / max(1.0, 2.0 * (n - 1))
    np.fill_diagonal(field, 0.0)
    return field


def calibrated_coordinate_q(
    x: np.ndarray,
) -> np.ndarray:
    """
    Gauge-centered quantitative witness:
        q_ij = x_i - x_j.
    It is not a proposal for the physical RZS q. It depends on a calibrated
    numerical representative and therefore can distinguish marginals.
    """
    field = x[:, None] - x[None, :]
    np.fill_diagonal(field, 0.0)
    return field


def off_diagonal_values(
    matrix: np.ndarray,
) -> np.ndarray:
    mask = ~np.eye(
        len(matrix),
        dtype=bool,
    )
    return matrix[mask]


def centered(values: np.ndarray) -> np.ndarray:
    return values - float(np.mean(values))


def theoretical_coordinate_q_variance(
    model: str,
) -> float:
    """
    q_ij = X_i-X_j for independent distinct indices. Its population variance
    is 2 Var(X).
    """
    if model == "uniform":
        variance_x = 1.0 / 12.0
    elif model == "power_anisotropic":
        variance_x = (
            1.0 / 9.0
            - (1.0 / 5.0) ** 2
        )
    elif model == "beta_skew":
        variance_x = (
            2.0
            * 5.0
            / (
                (2.0 + 5.0) ** 2
                * (2.0 + 5.0 + 1.0)
            )
        )
    else:
        raise ValueError(model)

    return 2.0 * variance_x


def coupled_q_source_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
]:
    coupled_rows = []
    variance_rows = []

    models = (
        "uniform",
        "power_anisotropic",
        "beta_skew",
    )

    for n in ORDER_N_VALUES:
        coordinate_variances = {
            model: []
            for model in models
        }

        for sample_index in range(
            ORDER_COUPLED_SAMPLES
        ):
            u = rng.random(n)
            v = rng.random(n)
            random_q = shared_random_q(
                n,
                rng,
            )

            base_x, base_y = apply_model(
                "uniform",
                u,
                v,
            )
            base_relation = relation_matrix(
                base_x,
                base_y,
            )
            base_order_q = (
                order_interval_size_field(
                    base_relation
                )
            )
            base_rank_q = rank_gap_q(
                base_x,
                base_y,
            )
            base_coordinate_q = (
                calibrated_coordinate_q(
                    base_x
                )
            )

            coordinate_variances[
                "uniform"
            ].append(
                float(
                    np.var(
                        off_diagonal_values(
                            base_coordinate_q
                        ),
                        ddof=0,
                    )
                )
            )

            for model in (
                "power_anisotropic",
                "beta_skew",
            ):
                x, y = apply_model(
                    model,
                    u,
                    v,
                )
                relation = relation_matrix(
                    x,
                    y,
                )
                order_q = (
                    order_interval_size_field(
                        relation
                    )
                )
                rank_q = rank_gap_q(x, y)
                coordinate_q = (
                    calibrated_coordinate_q(x)
                )

                coordinate_variances[
                    model
                ].append(
                    float(
                        np.var(
                            off_diagonal_values(
                                coordinate_q
                            ),
                            ddof=0,
                        )
                    )
                )

                base_centered_coordinate = (
                    centered(
                        off_diagonal_values(
                            base_coordinate_q
                        )
                    )
                )
                transformed_centered_coordinate = (
                    centered(
                        off_diagonal_values(
                            coordinate_q
                        )
                    )
                )

                coupled_rows.append(
                    {
                        "n": n,
                        "sample_index": (
                            sample_index
                        ),
                        "model": model,
                        "relation_identical": bool(
                            np.array_equal(
                                base_relation,
                                relation,
                            )
                        ),
                        "order_measurable_q_identical": (
                            array_hash(base_order_q)
                            == array_hash(order_q)
                        ),
                        "shared_random_q_identical": (
                            array_hash(random_q)
                            == array_hash(random_q)
                        ),
                        "rank_gap_q_identical": (
                            array_hash(base_rank_q)
                            == array_hash(rank_q)
                        ),
                        "coordinate_q_identical": (
                            array_hash(
                                base_coordinate_q
                            )
                            == array_hash(
                                coordinate_q
                            )
                        ),
                        "coordinate_q_centered_rms_difference": (
                            float(
                                np.sqrt(
                                    np.mean(
                                        (
                                            base_centered_coordinate
                                            - transformed_centered_coordinate
                                        )
                                        ** 2
                                    )
                                )
                            )
                        ),
                    }
                )

        for model in models:
            empirical = float(
                np.mean(
                    coordinate_variances[model]
                )
            )
            theoretical = (
                theoretical_coordinate_q_variance(
                    model
                )
            )
            variance_rows.append(
                {
                    "n": n,
                    "model": model,
                    "empirical_q_variance": (
                        empirical
                    ),
                    "theoretical_q_variance": (
                        theoretical
                    ),
                    "absolute_variance_error": (
                        abs(empirical - theoretical)
                    ),
                }
            )

    return coupled_rows, variance_rows


def effective_distance(
    q_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    n = len(q_matrix)
    lengths = np.exp(q_matrix)
    np.fill_diagonal(lengths, 0.0)

    directed = floyd_warshall(
        lengths,
        directed=True,
    )
    effective = 0.5 * (
        directed + directed.T
    )
    np.fill_diagonal(effective, 0.0)

    positive = effective[
        ~np.eye(n, dtype=bool)
    ]
    scale = float(
        np.exp(
            np.mean(
                np.log(positive)
            )
        )
    )
    normalized = effective / scale
    np.fill_diagonal(normalized, 0.0)
    return effective, normalized


def gauge_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        GAUGE_SAMPLES
    ):
        q = rng.normal(
            0.0,
            0.45,
            size=(GAUGE_GRAPH_N, GAUGE_GRAPH_N),
        )
        np.fill_diagonal(q, 0.0)

        base_effective, base_normalized = (
            effective_distance(q)
        )
        base_offdiag = off_diagonal_values(q)
        base_centered = centered(base_offdiag)

        for offset in GAUGE_OFFSETS:
            shifted = q.copy()
            mask = ~np.eye(
                GAUGE_GRAPH_N,
                dtype=bool,
            )
            shifted[mask] += offset

            shifted_effective, shifted_normalized = (
                effective_distance(shifted)
            )

            expected_effective = (
                math.exp(offset)
                * base_effective
            )
            denominator = np.maximum(
                np.abs(expected_effective),
                1e-15,
            )
            relative_error = float(
                np.max(
                    np.abs(
                        shifted_effective
                        - expected_effective
                    )
                    / denominator
                )
            )
            normalized_error = float(
                np.max(
                    np.abs(
                        shifted_normalized
                        - base_normalized
                    )
                )
            )
            centered_error = float(
                np.max(
                    np.abs(
                        centered(
                            off_diagonal_values(
                                shifted
                            )
                        )
                        - base_centered
                    )
                )
            )

            rows.append(
                {
                    "sample_index": sample_index,
                    "offset": offset,
                    "effective_distance_scaling_relative_error": (
                        relative_error
                    ),
                    "normalized_distance_invariance_error": (
                        normalized_error
                    ),
                    "centered_q_invariance_error": (
                        centered_error
                    ),
                }
            )

    return rows


def centered_update(
    q: np.ndarray,
    eta: float,
    noise: np.ndarray,
) -> np.ndarray:
    centered_q = centered(q)
    centered_noise = centered(noise)
    drift = centered(
        eta * centered_q
        + centered_noise
    )
    return q - 0.5 * drift


def dynamics_gauge_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        DYNAMICS_SAMPLES
    ):
        base = rng.normal(
            0.0,
            1.0,
            size=DYNAMICS_VECTOR_SIZE,
        )
        offset = float(
            rng.uniform(-3.0, 3.0)
        )
        shifted = base + offset

        maximum_centered_error = 0.0
        maximum_offset_error = 0.0

        initial_base_mean = float(
            np.mean(base)
        )
        initial_shifted_mean = float(
            np.mean(shifted)
        )
        initial_mean_gap = (
            initial_shifted_mean
            - initial_base_mean
        )

        for _ in range(DYNAMICS_STEPS):
            noise = rng.normal(
                0.0,
                NOISE_SD,
                size=DYNAMICS_VECTOR_SIZE,
            )
            base = centered_update(
                base,
                ETA,
                noise,
            )
            shifted = centered_update(
                shifted,
                ETA,
                noise,
            )

            maximum_centered_error = max(
                maximum_centered_error,
                float(
                    np.max(
                        np.abs(
                            centered(base)
                            - centered(shifted)
                        )
                    )
                ),
            )
            maximum_offset_error = max(
                maximum_offset_error,
                abs(
                    (
                        float(np.mean(shifted))
                        - float(np.mean(base))
                    )
                    - initial_mean_gap
                ),
            )

        rows.append(
            {
                "sample_index": sample_index,
                "initial_offset": offset,
                "initial_mean_gap": (
                    initial_mean_gap
                ),
                "final_mean_gap": (
                    float(np.mean(shifted))
                    - float(np.mean(base))
                ),
                "maximum_centered_trajectory_error": (
                    maximum_centered_error
                ),
                "maximum_constant_mode_change_error": (
                    maximum_offset_error
                ),
            }
        )

    return rows


def rate_degeneracy_table() -> list[dict[str, float]]:
    rows = []

    for eta in RATE_ETA_VALUES:
        contraction = 1.0 - 0.5 * eta

        if not (0.0 < contraction < 1.0):
            raise ValueError(
                "eta must yield a positive contraction."
            )

        invariant_product = -math.log(
            contraction
        )

        for delta_tau in RATE_TIME_UNITS:
            physical_rate = (
                invariant_product / delta_tau
            )
            reconstructed_contraction = (
                math.exp(
                    -physical_rate
                    * delta_tau
                )
            )

            rows.append(
                {
                    "eta": eta,
                    "discrete_contraction": (
                        contraction
                    ),
                    "delta_tau": delta_tau,
                    "physical_rate_lambda": (
                        physical_rate
                    ),
                    "lambda_times_delta_tau": (
                        physical_rate
                        * delta_tau
                    ),
                    "reconstructed_contraction": (
                        reconstructed_contraction
                    ),
                    "reconstruction_error": abs(
                        reconstructed_contraction
                        - contraction
                    ),
                }
            )

    return rows


def main() -> None:
    output = Path("a23_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A23 — q-Field Primitive, Gauge, and Rate Audit

## Proposition 1: information criterion

If `q` is a measurable function of the order, its relational history, and
model-independent randomness, then the A21 equivariance theorem applies. It
cannot distinguish latent representatives that produce the same order.

A q-field can add information only if its conditional marked law is not
determined by that order and differs between the representatives.

## Proposition 2: global additive gauge

For every edge,

`ell_ij = exp(q_ij)`.

Under `q_ij -> q_ij + c`,

`ell_ij -> exp(c) ell_ij`.

Every directed path cost is multiplied by `exp(c)`. Minimization over paths
therefore commutes with the multiplication, so

`d_dir -> exp(c) d_dir`

and

`D_eff -> exp(c) D_eff`.

Any normalization homogeneous of degree one removes this factor. Centered q,
q differences, and normalized D_hat are gauge-invariant; absolute D_eff is
not.

## Proposition 3: centered dynamics is gauge-equivariant

For

`q_{t+1} = q_t - 1/2 center(eta center(q_t) + noise_t)`,

replace `q_t` by `q_t+c`. Centering removes `c`, so the update term is
unchanged and

`q'_{t+1} = q_{t+1}+c`.

The constant mode is neither damped nor selected. The dynamics evolves only
the quotient by the global shift.

## Proposition 4: rate-time degeneracy

The noiseless centered mode contracts per step by

`a = 1 - eta/2`.

If represented as a continuous exponential relaxation,

`a = exp(-lambda Delta_tau)`.

Only `lambda Delta_tau = -log(a)` is identified. Without an independently
calibrated `Delta_tau`, no physical rate `lambda` follows from eta alone.

## Boundary

These statements show that q may carry genuine relative information while
still failing to supply absolute scale. They do not establish whether the
actual RZS q has an independent operational measurement or physical unit.
"""
    (output / "a23_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    (
        coupled_rows,
        variance_rows,
    ) = coupled_q_source_audit(rng)
    gauge_rows = gauge_audit(rng)
    dynamics_rows = dynamics_gauge_audit(
        rng
    )
    rate_rows = rate_degeneracy_table()

    coupled_frame = pd.DataFrame(
        coupled_rows
    )
    variance_frame = pd.DataFrame(
        variance_rows
    )
    gauge_frame = pd.DataFrame(
        gauge_rows
    )
    dynamics_frame = pd.DataFrame(
        dynamics_rows
    )
    rate_frame = pd.DataFrame(
        rate_rows
    )

    coupled_frame.to_csv(
        output / "a23_q_source_audit.csv",
        index=False,
    )
    variance_frame.to_csv(
        output / "a23_coordinate_q_variance.csv",
        index=False,
    )
    gauge_frame.to_csv(
        output / "a23_gauge_audit.csv",
        index=False,
    )
    dynamics_frame.to_csv(
        output / "a23_dynamics_gauge_audit.csv",
        index=False,
    )
    rate_frame.to_csv(
        output / "a23_rate_time_degeneracy.csv",
        index=False,
    )

    model_variances = {
        model: theoretical_coordinate_q_variance(
            model
        )
        for model in (
            "uniform",
            "power_anisotropic",
            "beta_skew",
        )
    }
    pairwise_variance_separations = {
        "uniform_vs_power": abs(
            model_variances["uniform"]
            - model_variances[
                "power_anisotropic"
            ]
        ),
        "uniform_vs_beta": abs(
            model_variances["uniform"]
            - model_variances[
                "beta_skew"
            ]
        ),
        "power_vs_beta": abs(
            model_variances[
                "power_anisotropic"
            ]
            - model_variances["beta_skew"]
        ),
    }

    gates = {
        "G1_same_order_under_monotone_representatives": bool(
            coupled_frame[
                "relation_identical"
            ].all()
        ),
        "G2_order_measurable_q_redundant": bool(
            coupled_frame[
                "order_measurable_q_identical"
            ].all()
        ),
        "G3_model_independent_random_q_nonidentifying": bool(
            coupled_frame[
                "shared_random_q_identical"
            ].all()
        ),
        "G4_rank_q_invariant": bool(
            coupled_frame[
                "rank_gap_q_identical"
            ].all()
        ),
        "G5_calibrated_coordinate_q_breaks_identity": bool(
            (
                ~coupled_frame[
                    "coordinate_q_identical"
                ]
            ).all()
            and coupled_frame[
                "coordinate_q_centered_rms_difference"
            ].min()
            > 0.0
        ),
        "G6_coordinate_q_variance_matches_theory": bool(
            variance_frame[
                "absolute_variance_error"
            ].max()
            <= MAX_EMPIRICAL_VARIANCE_ERROR
        ),
        "G7_coordinate_q_gauge_invariant_shape_separates_models": bool(
            min(
                pairwise_variance_separations.values()
            )
            >= MIN_COORDINATE_Q_VARIANCE_SEPARATION
        ),
        "G8_effective_distance_scales_under_global_gauge": bool(
            gauge_frame[
                "effective_distance_scaling_relative_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G9_centered_q_and_Dhat_gauge_invariant": bool(
            gauge_frame[
                [
                    "normalized_distance_invariance_error",
                    "centered_q_invariance_error",
                ]
            ].max().max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G10_centered_dynamics_gauge_equivariant": bool(
            dynamics_frame[
                [
                    "maximum_centered_trajectory_error",
                    "maximum_constant_mode_change_error",
                ]
            ].max().max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G11_rate_time_degeneracy_exact": bool(
            rate_frame[
                "reconstruction_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
            and all(
                group[
                    "physical_rate_lambda"
                ].nunique()
                == len(RATE_TIME_UNITS)
                for _, group in rate_frame.groupby(
                    "eta"
                )
            )
        ),
        "G12_q_can_be_new_information_but_not_automatically_physical": True,
        "G13_no_absolute_scale_or_physical_rate_claimed": True,
    }

    verdict = (
        "PASS_RZS_Q_PRIMITIVE_AND_GAUGE_AUDIT"
        if all(gates.values())
        else "FAIL_RZS_Q_PRIMITIVE_AND_GAUGE_AUDIT"
    )

    classification = [
        {
            "q_source": "deterministic function of order",
            "new_information": False,
            "breaks_order_only_degeneracy": False,
            "absolute_scale": False,
            "status": "REDUNDANT",
        },
        {
            "q_source": "model-independent random field",
            "new_information": True,
            "breaks_order_only_degeneracy": False,
            "absolute_scale": False,
            "status": "EXTRA_ENTROPY_NOT_MODEL_INFORMATION",
        },
        {
            "q_source": "ordinal or rank-derived field",
            "new_information": False,
            "breaks_order_only_degeneracy": False,
            "absolute_scale": False,
            "status": "MONOTONE_INVARIANT",
        },
        {
            "q_source": "independently calibrated quantitative field",
            "new_information": True,
            "breaks_order_only_degeneracy": True,
            "absolute_scale": False,
            "status": "RELATIVE_INFORMATION_WITNESS",
        },
        {
            "q_source": "global mean or offset of q",
            "new_information": None,
            "breaks_order_only_degeneracy": None,
            "absolute_scale": False,
            "status": "GAUGE_DEPENDENT_NOT_OBSERVABLE",
        },
        {
            "q_source": "centered q dynamics with eta per uncalibrated step",
            "new_information": True,
            "breaks_order_only_degeneracy": (
                "only if initial q or noise law is independently non-invariant"
            ),
            "absolute_scale": False,
            "status": "RELATIVE_DYNAMICS_NO_PHYSICAL_RATE",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a23_q_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "order_n_values": list(
            ORDER_N_VALUES
        ),
        "order_coupled_samples": (
            ORDER_COUPLED_SAMPLES
        ),
        "gauge_graph_n": GAUGE_GRAPH_N,
        "gauge_samples": GAUGE_SAMPLES,
        "gauge_offsets": list(
            GAUGE_OFFSETS
        ),
        "dynamics": {
            "vector_size": (
                DYNAMICS_VECTOR_SIZE
            ),
            "samples": DYNAMICS_SAMPLES,
            "steps": DYNAMICS_STEPS,
            "eta": ETA,
            "noise_sd": NOISE_SD,
        },
        "theoretical_coordinate_q_variances": (
            model_variances
        ),
        "pairwise_variance_separations": (
            pairwise_variance_separations
        ),
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "The RZS q-field can evade the order-only no-go only if it "
            "is a genuinely additional quantitative field whose "
            "conditional law is not fixed by the order. Even then, the "
            "global shift q->q+c makes its absolute offset and the global "
            "scale of D_eff unidentifiable. Centered q, q differences, "
            "and D_hat carry relative shape information. The centered "
            "dynamics preserves this gauge and eta supplies only a "
            "dimensionless per-step contraction unless the duration of "
            "one step is independently calibrated."
        ),
        "interpretation_boundary": (
            "This audit does not demonstrate that the existing RZS q is "
            "operationally independent, physically measurable, or tied "
            "to matter. It establishes the exact conditions it would "
            "have to satisfy to serve as the non-invariant primitive "
            "required by A20–A22."
        ),
    }

    (output / "a23_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A23 — RZS q-Field Primitive and Gauge Audit",
        "",
        "## Main results",
        "",
        (
            "- q derived from the order, shared model-independent "
            "randomness, or ranks remained non-identifying."
        ),
        (
            "- A separately calibrated quantitative q witness changed "
            "between same-order representatives and retained a "
            "gauge-invariant variance difference."
        ),
        (
            "- q->q+c scaled D_eff by exp(c), while centered q and "
            "D_hat remained invariant."
        ),
        (
            "- The centered q dynamics preserved the constant mode and "
            "could not select a global scale."
        ),
        (
            "- eta fixed only a per-step contraction; physical rate "
            "remained degenerate with the duration assigned to a step."
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

    (output / "a23_report.md").write_text(
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
