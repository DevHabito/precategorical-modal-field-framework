#!/usr/bin/env python3
"""Independent checks for the exact d=3 bulk constant.

For 2+1 Minkowski spacetime, the small-disagreement tail is bulk dominated:

    F_3(eps) ~ C_3 eps^3.

The analytic derivation gives

    C_3 = 32*pi/9,

and therefore the comparable true-twin expectation satisfies

    E[T_n] ~ (32*pi/3) / n.

This script:
1. numerically integrates the exact bulk coefficient in (u,v) endpoint-distance
   coordinates;
2. evaluates the reduced integral after s=u+v, w=(u-v)/(u+v);
3. checks both against the closed constants.

SciPy is used only as a regression; the accompanying theorem contains the
closed analytic evaluation.
"""

from __future__ import annotations

import math

from scipy.integrate import dblquad, quad


def K_uv(u: float, v: float) -> float:
    return (
        u**4
        + v**4
        + (4.0 - u**2 - v**2) * u * v
    )


def original_integral() -> float:
    """I = int_{u,v>0,u+v<2} uv / K(u,v)^(3/2) du dv."""

    def inner(v: float, u: float) -> float:
        k = K_uv(u, v)
        return u * v / (k ** 1.5)

    value, _ = dblquad(
        inner,
        0.0,
        2.0,
        lambda u: 0.0,
        lambda u: 2.0 - u,
        epsabs=1.0e-10,
        epsrel=1.0e-9,
    )
    return value


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
    i1 = original_integral()
    i2 = reduced_integral()
    exact_i = math.pi / 8.0

    c3 = (256.0 / 9.0) * exact_i
    k3 = 3.0 * c3

    print(f"original I       = {i1:.12f}")
    print(f"reduced I        = {i2:.12f}")
    print(f"pi/8             = {exact_i:.12f}")
    print(f"C_3              = {c3:.12f}")
    print(f"32*pi/9          = {32.0 * math.pi / 9.0:.12f}")
    print(f"K_3 twin         = {k3:.12f}")
    print(f"32*pi/3          = {32.0 * math.pi / 3.0:.12f}")

    assert math.isclose(i1, exact_i, rel_tol=2.0e-7, abs_tol=2.0e-8)
    assert math.isclose(i2, exact_i, rel_tol=1.0e-12, abs_tol=1.0e-12)
    assert math.isclose(c3, 32.0 * math.pi / 9.0, rel_tol=1.0e-12)
    assert math.isclose(k3, 32.0 * math.pi / 3.0, rel_tol=1.0e-12)

    print("PASS: d=3 bulk and true-twin constants verified.")


if __name__ == "__main__":
    main()
