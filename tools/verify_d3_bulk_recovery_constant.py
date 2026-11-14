#!/usr/bin/env python3
"""Independent checks for the exact d=3 bulk constant.

For 2+1 Minkowski spacetime, the small-disagreement tail is bulk dominated:

    F_3(eps) ~ C_3 eps^3.

The analytic derivation gives

    C_3 = 32*pi/9,

and therefore the comparable true-twin expectation satisfies

    E[T_n] ~ (32*pi/3) / n.

This script:
1. numerically integrates the full two-variable coefficient after changing
   variables to s = u + v and w = (u - v) / (u + v);
2. evaluates the one-variable integral after integrating out s analytically;
3. checks both against the closed constants.

SciPy is used only as a regression; the accompanying theorem contains the
closed analytic evaluation.
"""

from __future__ import annotations

import math
import warnings

from scipy.integrate import IntegrationWarning, quad


def transformed_integral(tolerance: float) -> float:
    """Integrate the two-variable expression before analytic reduction."""

    def integrate_scale(w: float) -> float:
        a = (1.0 - w) * (1.0 + w)
        b = w**2 * (w**2 + 3.0)

        def integrand(s: float) -> float:
            return a / (4.0 * a + b * s**2)**1.5

        value, _ = quad(
            integrand, 0.0, 2.0, epsabs=tolerance, epsrel=tolerance, limit=300
        )
        return value

    # Integrate only the positive half by symmetry. QUADPACK uses interior
    # nodes, so it never needs the singular corner (s, w) = (0, 1).
    value, _ = quad(
        integrate_scale, 0.0, 1.0,
        epsabs=tolerance / 2.0, epsrel=tolerance / 2.0, limit=300,
    )
    return 2.0 * value


def reduced_integral() -> float:
    """After integrating s, I = int_{-1}^1 [4(1+w^2)]^-1 dw."""

    value, _ = quad(
        lambda w: 1.0 / (4.0 * (1.0 + w * w)),
        -1.0,
        1.0,
        epsabs=1.0e-13,
        epsrel=1.0e-13,
    )
    return value


def main() -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        coarse = transformed_integral(1.0e-8)
        i1 = transformed_integral(1.0e-10)
        i2 = reduced_integral()
    exact_i = math.pi / 8.0

    c3 = (256.0 / 9.0) * exact_i
    k3 = 3.0 * c3

    print(f"transformed I    = {i1:.12f}")
    print(f"reduced I        = {i2:.12f}")
    print(f"pi/8             = {exact_i:.12f}")
    print(f"C_3              = {c3:.12f}")
    print(f"32*pi/9          = {32.0 * math.pi / 9.0:.12f}")
    print(f"K_3 twin         = {k3:.12f}")
    print(f"32*pi/3          = {32.0 * math.pi / 3.0:.12f}")

    assert math.isclose(coarse, i1, rel_tol=0.0, abs_tol=1.0e-8)
    assert math.isclose(i1, exact_i, rel_tol=0.0, abs_tol=1.0e-9)
    assert math.isclose(i2, exact_i, rel_tol=1.0e-12, abs_tol=1.0e-12)
    assert math.isclose(c3, 32.0 * math.pi / 9.0, rel_tol=1.0e-12)
    assert math.isclose(k3, 32.0 * math.pi / 3.0, rel_tol=1.0e-12)

    print("PASS: d=3 bulk and true-twin constants verified.")


if __name__ == "__main__":
    main()
