#!/usr/bin/env python3
"""Exact algebraic audit for Bridge 1A.

The script checks only identities promoted in the bridge note. It does not
reproduce the 2012 experimental dataset.
"""

from fractions import Fraction


def U(n: int, ng: Fraction) -> Fraction:
    """Dimensionless electrostatic energy U/Ec."""
    return Fraction(n*n) - 2*Fraction(n)*ng


def event_heat(delta_n: int, ng: Fraction) -> Fraction:
    """Dimensionless event heat Q/Ec for delta_n = +/-1."""
    assert delta_n in (-1, 1)
    return 2*Fraction(delta_n)*(ng-Fraction(1,2))


probes = [
    Fraction(0),
    Fraction(1,10),
    Fraction(1,4),
    Fraction(1,2),
    Fraction(3,4),
    Fraction(9,10),
    Fraction(1),
]

for ng in probes:
    # 0 -> 1
    du_forward = U(1,ng)-U(0,ng)
    q_forward = event_heat(+1,ng)
    assert q_forward == -du_forward

    # 1 -> 0
    du_reverse = U(0,ng)-U(1,ng)
    q_reverse = event_heat(-1,ng)
    assert q_reverse == -du_reverse

    # Energy-gap identity.
    assert U(1,ng)-U(0,ng) == 1-2*ng

# Two-state identifiability: on {0,1}, E[n]=P(n=1).
for p in probes:
    mean = (1-p)*0+p*1
    assert mean == p

print("BRIDGE_1A_EXACT_AUDIT: PASS")
print(f"gate_charge_probes={len(probes)}")
print("checked: Q_event = -Delta U in both directions")
print("checked: on support {0,1}, mean occupancy determines the distribution")
