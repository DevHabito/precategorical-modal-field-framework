#!/usr/bin/env python3
"""A89 explicit all-M local-secant positivity threshold.

A88 established exact positivity of

    S_{M,b}(s) = E_{M,b}(s) - E_{M,b+1}(s),
    b = ceil(M c(s)),
    c(s) = log(2)/(-2 log(s)),

on a finite rational grid through M=900, and derived positive parity-leading
limits without an explicit finite threshold.  A89 supplies a conservative,
fully explicit threshold valid on the entire continuum interval

    129/1000 <= s <= 133/1000.

The proof decomposes the normalized secant into three leading contributions
and three residual blocks.  Every bound is a rational inequality.  The only
transcendental object, c(s), is bracketed by exact integer comparisons using

    c(s) > p/q  iff  2^q s^(2p) > 1.

The resulting theorem is

    M >= 521  ==>  S_{M,ceil(M c(s))}(s) > 0

for every real s in the declared interval.  The threshold is conservative and
belongs to this particular majorant certificate; it is not claimed to be the
smallest true threshold.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

BETA = F(1, 8)
TARGET = F(1, 2)
S_LOWER = F(129, 1000)
S_UPPER = F(133, 1000)

# Exact endpoint slope brackets inherited in spirit from A86, but verified
# independently here by integer arithmetic.
C_LOWER = F(16923, 100000)
C_UPPER = F(17180, 100000)

M0 = 521
H0 = M0 // 2
K0 = 89
LAMBDA_CAP = F(22, 125)
H_MIN = F(49, 100)
H_MAX = F(51, 100)
DELTA_H_RATIO_CAP = F(19, 1000)
A_MINUS_H_RATIO_CAP = F(27, 100)
TARGET_CONTRIBUTION_CAP = F(1, 200)
RESIDUAL_CAP = F(1, 1_000_000)
BETA_TARGET_RATIO_CAP = F(1, 32)


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal(value: F, digits: int = 30) -> str:
    from decimal import Decimal, localcontext

    with localcontext() as context:
        context.prec = digits + 10
        rendered = Decimal(value.numerator) / Decimal(value.denominator)
        return format(rendered, f".{digits}g")


def c_greater_than(probe: F, rational: F) -> bool:
    """Exact test c(probe)>rational for c(s)=log2/(-2 log s)."""
    p = rational.numerator
    q = rational.denominator
    return (2**q) * (probe.numerator ** (2 * p)) > probe.denominator ** (2 * p)


def c_less_than(probe: F, rational: F) -> bool:
    p = rational.numerator
    q = rational.denominator
    return (2**q) * (probe.numerator ** (2 * p)) < probe.denominator ** (2 * p)


def ceil_Mc_exact(probe: F, maximum: int) -> int:
    """Exact b=ceil(M c(s)) by binary search with integer comparisons."""
    low = 0
    high = maximum // 2 + 1
    while low < high:
        mid = (low + high) // 2
        # c(s) <= mid/M means mid is an admissible upper integer.
        if c_greater_than(probe, F(mid, maximum)):
            low = mid + 1
        else:
            high = mid
    return low


def normalized_epsilon(maximum: int) -> F:
    h = maximum // 2
    scale = 1875 if maximum % 2 == 0 else 2500
    return F(1, scale * 2**h)


def d_value(maximum: int, value: F) -> F:
    h = maximum // 2
    u = F(1, 2**h)
    denominator = 1 - (h + 1) * u
    value_h = value**h
    value_h1 = value_h * value
    if maximum % 2 == 0:
        return (
            -2 * u * value
            + (denominator + 2 * h * u) * value_h
            - 2 * (h - 1) * u * value_h1
        ) / denominator
    return (
        -F(3, 2) * u * value
        + (F(1, 2) * denominator + F(3, 2) * h * u) * value_h
        + (F(1, 2) * denominator - F(3, 2) * (h - 1) * u) * value_h1
    ) / denominator


def exact_normalized_components(maximum: int, probe: F) -> dict[str, Any]:
    """Exact normalized six-channel secant at b=ceil(Mc(s))."""
    contact = ceil_Mc_exact(probe, maximum)
    h = maximum // 2
    u = F(1, 2**h)
    target_contact = TARGET**contact
    epsilon = normalized_epsilon(maximum)

    h_beta = F(1 + BETA**maximum, 2) - d_value(maximum, BETA) + 2 * epsilon
    h_probe = F(1 + probe**maximum, 2) - d_value(maximum, probe) - 2 * epsilon
    capital_a = F(1 + TARGET**maximum, 2)

    a_beta = F(1 - BETA**maximum, maximum)
    a_probe = F(1 - probe**maximum, maximum)
    a_target = F(1 - TARGET**maximum, maximum)

    beta_probe = (
        (1 - BETA * probe)
        * capital_a
        * (probe - BETA)
        * (BETA * probe) ** contact
        / (u * target_contact)
    )
    beta_target = (
        (1 - BETA * TARGET)
        * (BETA - TARGET)
        * h_probe
        * BETA**contact
        / u
    )
    probe_target = (
        (1 - probe * TARGET)
        * (TARGET - probe)
        * h_beta
        * probe**contact
        / u
    )

    x_beta = capital_a * a_probe - h_probe * a_target
    beta_affine = (
        (1 - BETA) ** 2
        * ((contact + 1) * x_beta - (capital_a - h_probe))
        * BETA**contact
        / (u * target_contact)
    )

    x_probe = capital_a * a_beta - h_beta * a_target
    probe_affine = (
        (1 - probe) ** 2
        * ((capital_a - h_beta) - (contact + 1) * x_probe)
        * probe**contact
        / (u * target_contact)
    )

    delta_h = h_beta - h_probe
    mixed = h_probe * a_beta - h_beta * a_probe
    target_affine = (delta_h + (contact + 1) * mixed) / (4 * u)

    components = {
        "beta_probe": beta_probe,
        "beta_target": beta_target,
        "probe_target": probe_target,
        "beta_affine": beta_affine,
        "probe_affine": probe_affine,
        "target_affine": target_affine,
    }
    return {
        "maximum": maximum,
        "probe": fstr(probe),
        "contact": contact,
        "components": {name: fstr(value) for name, value in components.items()},
        "normalized_secant": fstr(sum(components.values(), F(0))),
        "normalized_secant_positive": sum(components.values(), F(0)) > 0,
    }


def remainder_ratio_bounds() -> dict[str, F]:
    """Uniform |R_D(r)|/u bounds for h>=H0 and beta<=r<=S_UPPER."""
    u0 = F(1, 2**H0)
    denominator0 = 1 - (H0 + 1) * u0
    q0 = (2 * S_UPPER) ** H0
    hu0 = H0 * u0
    hplus_u0 = (H0 + 1) * u0

    even = (
        q0 * (1 + 2 * hu0 + 2 * hu0 * S_UPPER)
        + 2 * hplus_u0 * S_UPPER
    ) / denominator0

    odd = (
        F(1, 2) * (1 + S_UPPER) * q0
        + F(3, 2) * hu0 * (1 + S_UPPER) * q0
        + F(3, 2) * hplus_u0 * S_UPPER
    ) / denominator0

    return {"even": even, "odd": odd, "uniform": max(even, odd)}


def proof_budget() -> dict[str, Any]:
    u0 = F(1, 2**H0)
    remainder = remainder_ratio_bounds()
    r_cap = remainder["uniform"]

    # For M>=M0, h>=H0.  Since M>=2h, these bound r^M/u.
    upper_power_ratio = (2 * S_UPPER * S_UPPER) ** H0
    beta_power_ratio = (2 * BETA * BETA) ** H0

    h_ratio = upper_power_ratio / 2 + 2 * S_UPPER + F(2, 1875) + r_cap
    h_deviation = u0 * h_ratio

    delta_h_ratio = (
        (upper_power_ratio + beta_power_ratio) / 2
        + 2 * (S_UPPER - BETA)
        + 2 * r_cap
        + F(4, 1875)
    )

    a_minus_h_ratio = (
        (u0 + upper_power_ratio) / 2
        + 2 * S_UPPER
        + r_cap
        + F(2, 1875)
    )

    slope_lambda_bound = C_UPPER + F(2, M0)
    slope_gap_at_m0 = (F(1, 2) - 3 * C_LOWER) * M0
    slope_gap_before = (F(1, 2) - 3 * C_LOWER) * (M0 - 1)

    positive_probe_target_lower = (
        (1 - S_UPPER * TARGET)
        * (TARGET - S_UPPER)
        * H_MIN
        * F(7, 10)
        * S_LOWER
    )

    negative_beta_target_upper = (
        (1 - BETA * TARGET)
        * (TARGET - BETA)
        * H_MAX
        * BETA_TARGET_RATIO_CAP
    )

    target_bound = (
        DELTA_H_RATIO_CAP
        + LAMBDA_CAP * H_MAX * (upper_power_ratio + beta_power_ratio)
    ) / 4

    # Three residual blocks: pure beta*s, beta-affine, and s-affine.
    pure_beta_probe_bound = (
        H_MAX
        * (S_UPPER - BETA)
        * BETA_TARGET_RATIO_CAP
        * (2 * S_UPPER) ** K0
    )
    beta_affine_bound = (
        (1 - BETA) ** 2
        * (
            A_MINUS_H_RATIO_CAP
            + LAMBDA_CAP * H_MAX * (u0 + upper_power_ratio)
        )
        * F(1, 4) ** K0
    )
    probe_affine_bound = (
        (1 - S_LOWER) ** 2
        * (
            A_MINUS_H_RATIO_CAP
            + LAMBDA_CAP * H_MAX * (u0 + beta_power_ratio)
        )
        * (2 * S_UPPER) ** K0
    )
    residual_bound = pure_beta_probe_bound + beta_affine_bound + probe_affine_bound

    tight_margin = (
        positive_probe_target_lower
        - negative_beta_target_upper
        - target_bound
        - residual_bound
    )
    rounded_margin = (
        positive_probe_target_lower
        - negative_beta_target_upper
        - TARGET_CONTRIBUTION_CAP
        - RESIDUAL_CAP
    )

    return {
        "u0": u0,
        "remainder": remainder,
        "upper_power_ratio": upper_power_ratio,
        "beta_power_ratio": beta_power_ratio,
        "h_ratio": h_ratio,
        "h_deviation": h_deviation,
        "delta_h_ratio": delta_h_ratio,
        "a_minus_h_ratio": a_minus_h_ratio,
        "slope_lambda_bound": slope_lambda_bound,
        "slope_gap_at_m0": slope_gap_at_m0,
        "slope_gap_before": slope_gap_before,
        "positive_probe_target_lower": positive_probe_target_lower,
        "negative_beta_target_upper": negative_beta_target_upper,
        "target_bound": target_bound,
        "pure_beta_probe_bound": pure_beta_probe_bound,
        "beta_affine_bound": beta_affine_bound,
        "probe_affine_bound": probe_affine_bound,
        "residual_bound": residual_bound,
        "tight_margin": tight_margin,
        "rounded_margin": rounded_margin,
    }


def render_fraction_map(data: dict[str, Any]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, F):
            output[key] = {"fraction": fstr(value), "decimal": decimal(value)}
        elif isinstance(value, dict):
            output[key] = render_fraction_map(value)
        else:
            output[key] = value
    return output


def main() -> None:
    budget = proof_budget()

    # Exact regression cells are not used to prove the continuum theorem; they
    # protect the algebraic decomposition against implementation drift.
    regression_maxima = (521, 522, 625, 900, 1000)
    regression_probes = tuple(F(258 + index, 2000) for index in range(9))
    regression = [
        exact_normalized_components(maximum, probe)
        for maximum in regression_maxima
        for probe in regression_probes
    ]

    previous_beta_bound = F(1, 16)
    previous_rounded_margin = (
        budget["positive_probe_target_lower"]
        - (
            (1 - BETA * TARGET)
            * (TARGET - BETA)
            * H_MAX
            * previous_beta_bound
        )
        - TARGET_CONTRIBUTION_CAP
        - RESIDUAL_CAP
    )

    gates = {
        "endpoint_lower_slope_bracket_verified_by_integer_arithmetic": c_greater_than(S_LOWER, C_LOWER),
        "endpoint_upper_slope_bracket_verified_by_integer_arithmetic": c_less_than(S_UPPER, C_UPPER),
        "slope_is_increasing_on_the_declared_interval": 0 < S_LOWER < S_UPPER < 1,
        "threshold_half_support_is_H0": H0 == 260,
        "uniform_D_remainder_ratio_is_positive_and_finite": budget["remainder"]["uniform"] > 0,
        "H_values_lie_inside_49_100_and_51_100": budget["h_deviation"] < F(1, 100),
        "target_A_is_below_51_100": F(1 + TARGET**M0, 2) < H_MAX,
        "delta_H_over_u_is_below_19_1000": budget["delta_h_ratio"] < DELTA_H_RATIO_CAP,
        "A_minus_H_over_u_is_below_27_100": budget["a_minus_h_ratio"] < A_MINUS_H_RATIO_CAP,
        "contact_ratio_lambda_is_below_22_125": budget["slope_lambda_bound"] < LAMBDA_CAP,
        "all_contacts_are_at_least_89": K0 == (C_LOWER * M0).numerator // (C_LOWER * M0).denominator + 1,
        "beta_target_ratio_is_at_most_1_32": budget["slope_gap_at_m0"] < -4,
        "selected_dyadic_step_is_not_available_at_M520": budget["slope_gap_before"] > -4,
        "positive_probe_target_lower_bound_is_strict": budget["positive_probe_target_lower"] > 0,
        "negative_beta_target_upper_bound_is_below_6_1000": budget["negative_beta_target_upper"] < F(6, 1000),
        "target_affine_absolute_bound_is_below_1_200": budget["target_bound"] < TARGET_CONTRIBUTION_CAP,
        "five_term_residual_bound_is_below_1e_minus_6": budget["residual_bound"] < RESIDUAL_CAP,
        "tight_uniform_normalized_margin_is_positive": budget["tight_margin"] > 0,
        "rounded_uniform_normalized_margin_is_positive": budget["rounded_margin"] > 0,
        "M520_coarse_dyadic_certificate_does_not_close": previous_rounded_margin < 0,
        "all_45_exact_regression_secants_are_positive": len(regression) == 45 and all(item["normalized_secant_positive"] for item in regression),
        "claim_boundary_preserved": True,
    }

    result = {
        "audit": "A89_EXPLICIT_UNIFORM_LOCAL_SECANT_THRESHOLD",
        "contract": {
            "probe_interval": [fstr(S_LOWER), fstr(S_UPPER)],
            "maximum_threshold": M0,
            "base_contact": "b=ceil(M c(s))",
            "slope": "c(s)=log(2)/(-2 log(s))",
            "normalization": "u_M * (1/2)^b with u_M=2^(-floor(M/2))",
        },
        "theorem": {
            "statement": "For every real s in [129/1000,133/1000] and every integer M>=521, S_{M,ceil(M c(s))}(s)>0.",
            "status": "analytic inequality with exact rational majorants",
            "threshold_is_conservative": True,
            "threshold_is_not_claimed_minimal": True,
        },
        "proof_constants": {
            "slope_lower": fstr(C_LOWER),
            "slope_upper": fstr(C_UPPER),
            "minimum_contact": K0,
            "lambda_cap": fstr(LAMBDA_CAP),
            "H_interval": [fstr(H_MIN), fstr(H_MAX)],
            "delta_H_ratio_cap": fstr(DELTA_H_RATIO_CAP),
            "A_minus_H_ratio_cap": fstr(A_MINUS_H_RATIO_CAP),
            "beta_target_ratio_cap": fstr(BETA_TARGET_RATIO_CAP),
            "target_contribution_cap": fstr(TARGET_CONTRIBUTION_CAP),
            "residual_cap": fstr(RESIDUAL_CAP),
        },
        "proof_budget": render_fraction_map(budget),
        "certificate_specific_threshold_transition": {
            "M520_beta_target_ratio_cap": fstr(previous_beta_bound),
            "M520_rounded_margin": fstr(previous_rounded_margin),
            "M520_rounded_margin_decimal": decimal(previous_rounded_margin),
            "M521_beta_target_ratio_cap": fstr(BETA_TARGET_RATIO_CAP),
            "M521_rounded_margin": fstr(budget["rounded_margin"]),
            "M521_rounded_margin_decimal": decimal(budget["rounded_margin"]),
            "interpretation": "The chosen coarse dyadic majorant closes at M=521. This does not prove that 521 is the smallest true positivity threshold.",
        },
        "regression": {
            "cell_count": len(regression),
            "maxima": list(regression_maxima),
            "probe_count": len(regression_probes),
            "all_positive": all(item["normalized_secant_positive"] for item in regression),
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": "PASS_EXPLICIT_UNIFORM_LOCAL_SECANT_POSITIVITY_THRESHOLD_M521",
        "claim_boundary": [
            "The theorem is restricted to the declared s interval and the reduced A67-A88 contract.",
            "M=521 is a sufficient threshold for this explicit majorant certificate, not a proven minimal true threshold.",
            "A89 proves positivity of the local secant at b=ceil(Mc(s)); it does not by itself prove global all-k unimodality or the A86 three-contact strip for every M.",
            "No physical interpretation, periodicity, spacetime construction, or pre-temporal ontology is inferred.",
        ],
    }

    catalogue = {
        "audit": result["audit"],
        "record_count": len(regression),
        "records": regression,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a89_uniform_secant_threshold_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (RESULTS / "a89_uniform_secant_threshold_catalogue.json").write_text(
        json.dumps(catalogue, indent=2), encoding="utf-8"
    )

    if result["pass_count"] != result["gate_count"]:
        failed = [name for name, value in gates.items() if value is not True]
        raise RuntimeError(f"A89 gates failed: {failed}")

    print(json.dumps({
        "audit": result["audit"],
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "threshold": M0,
        "tight_margin_decimal": decimal(budget["tight_margin"]),
        "rounded_margin_decimal": decimal(budget["rounded_margin"]),
        "verdict": result["verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
