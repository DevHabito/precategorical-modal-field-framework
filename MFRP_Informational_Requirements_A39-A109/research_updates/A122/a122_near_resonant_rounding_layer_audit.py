#!/usr/bin/env python3
from fractions import Fraction as F
import json, math, sys
from pathlib import Path

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

BETA = F(1, 8)
DELTA = F(1, 1875)
OUT = Path(__file__).resolve().parent / "A122_EXACT_AUDIT_RESULTS_20260915.json"


def sg(x):
    return (x > 0) - (x < 0)


def B(M, k, r):
    return r**k - F(M-k, M) - F(k, M) * r**M


def dB(M, k, r):
    return r**(k+1) - r**k + F(1-r**M, M)


def den(M, tau):
    h = M // 2
    u = tau**h
    return tau - h*u + (h-1)*tau*u


def eps(M, tau):
    h = M // 2
    u = tau**h
    return DELTA * (u if M % 2 == 0 else F(1+tau, 2)*u)


def dt(M, r, tau):
    h = M // 2
    u = tau**h
    rh = r**h
    L = r - h*rh + (h-1)*rh*r
    if M % 2 == 0:
        return rh - u*L/den(M, tau)
    return F(rh + rh*r, 2) - F(1+tau, 2)*u*L/den(M, tau)


def E(M, k, s, tau):
    e = eps(M, tau)
    hb = F(1+BETA**M, 2) - dt(M, BETA, tau) + 2*e
    hs = F(1+s**M, 2) - dt(M, s, tau) - 2*e
    bb, bt = B(M, k, BETA), B(M, k, tau)
    xb, xt = dB(M, k, BETA), dB(M, k, tau)
    A = F(1+tau**M, 2)
    X = A*bb - hb*bt
    Y = -A*xb + hb*xt
    W = -bb*xt + bt*xb
    return X*dB(M, k, s) + Y*B(M, k, s) + W*hs


def b_exact(M, s, tau):
    lo, hi = 0, M
    target = tau**M
    while lo < hi:
        m = (lo + hi) // 2
        if s**(2*m) <= target:
            hi = m
        else:
            lo = m + 1
    return lo


def normalized_factor(M, k, s, tau):
    return E(M, k, s, tau) / (tau**(M//2) * tau**k)


def polynomial_core(M, k, s, tau):
    h = M // 2
    u = tau**h
    a = F(1) if M % 2 == 0 else F(1+tau, 2)
    G = (s-BETA)/tau - 4*DELTA
    return (
        F(tau-s, 2) * s**k/u
        + a*G * (-(1-tau) + F(1 + (1-tau)*k, M))
    )


# Exact rational interval logarithm via log x = 2 atanh((x-1)/(x+1)).
def log_interval(x, terms=25):
    assert x > 0
    z = (x-1)/(x+1)
    z2 = z*z
    term = z
    partial = F(0)
    for n in range(terms+1):
        partial += term/F(2*n+1)
        term *= z2
    remainder = abs(term) * F(2, 2*terms+3) / (1-z2)
    center = 2*partial
    if z >= 0:
        return center, center + remainder
    return center - remainder, center


def iadd(A, B):
    return A[0]+B[0], A[1]+B[1]


def isub(A, B):
    return A[0]-B[1], A[1]-B[0]


def imul(A, B):
    v = (A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1])
    return min(v), max(v)


def idiv(A, B):
    assert B[1] < 0 or B[0] > 0
    v = (A[0]/B[0], A[0]/B[1], A[1]/B[0], A[1]/B[1])
    return min(v), max(v)


def pt(x):
    return x, x


def omega_even_interval(s, tau, terms=25):
    ls = log_interval(s, terms)
    lt = log_interval(tau, terms)
    c = idiv(lt, imul(pt(F(2)), ls))
    G = (s-BETA)/tau - 4*DELTA
    P = F(tau-s, 2)
    Q = imul(pt((1-tau)*G), isub(pt(F(1)), c))
    ratio = idiv(Q, pt(P))
    lr = (log_interval(ratio[0], terms)[0], log_interval(ratio[1], terms)[1])
    xi = idiv(lr, ls)
    bracket = iadd(pt(F(1)), imul(pt(1-tau), xi))
    omega = imul(pt(G), bracket)
    return xi, omega


def diagnostic_eta(M, s_float, tau_float, odd):
    c = math.log(tau_float)/(2*math.log(s_float))
    sigma = 0.5 if odd else 0.0
    a = (1+tau_float)/2 if odd else 1.0
    G = (s_float-0.125)/tau_float - 4/1875
    P = (tau_float-s_float)/2 * tau_float**sigma
    Q = a*(1-tau_float)*G*(1-c)
    xi = math.log(Q/P)/math.log(s_float)
    omega = a*G*(1+(1-tau_float)*xi)
    eta_star = -omega/(Q*math.log(s_float))
    y = M*c
    rho = math.ceil(y) - y
    eta = M*(rho-xi)
    theta = omega + Q*math.log(s_float)*eta
    return {
        "rho_float": rho,
        "xi_float": xi,
        "eta_float": eta,
        "eta_star_float": eta_star,
        "Theta_float": theta,
    }


def main():
    exact_controls = []
    s = F(131, 1000)
    tau = F(1, 5)

    for M in (4568, 5596, 6624, 7652):
        k = b_exact(M, s, tau)
        N = normalized_factor(M, k, s, tau)
        C = polynomial_core(M, k, s, tau)
        R = N-C
        assert sg(N) == sg(C)
        assert abs(R) < F(1, M**5)
        d = diagnostic_eta(M, 0.131, 0.2, False)
        exact_controls.append({
            "M": M,
            "parity": "even",
            "b": k,
            "sign_exact_normalized_factor": sg(N),
            "sign_exact_polynomial_core": sg(C),
            "exact_remainder_lt_M_minus_5": True,
            **d,
        })

    for M in (959, 1449):
        k = b_exact(M, s, tau)
        N = normalized_factor(M, k, s, tau)
        C = polynomial_core(M, k, s, tau)
        R = N-C
        assert sg(N) == sg(C)
        assert abs(R) < F(1, M**3)
        d = diagnostic_eta(M, 0.131, 0.2, True)
        exact_controls.append({
            "M": M,
            "parity": "odd",
            "b": k,
            "sign_exact_normalized_factor": sg(N),
            "sign_exact_polynomial_core": sg(C),
            "exact_remainder_lt_M_minus_3": True,
            **d,
        })

    s0 = F(129, 1000)
    tau_left = F(131, 1000)
    tau_right = F(132, 1000)
    _, omega_left = omega_even_interval(s0, tau_left, 25)
    _, omega_right = omega_even_interval(s0, tau_right, 25)
    assert omega_left[1] < 0
    assert omega_right[0] > 0

    out = {
        "audit": "A122_NEAR_RESONANT_ROUNDING_LAYER_AUDIT",
        "date": "2026-09-15",
        "status": "PASS_WITH_INTRINSIC_DOUBLE_CRITICAL_EXISTENCE",
        "exact_polynomial_core_controls": exact_controls,
        "double_critical_even_certificate": {
            "s": "129/1000",
            "tau_left": "131/1000",
            "tau_right": "132/1000",
            "log_series_terms": 26,
            "omega_left_interval_float": [float(omega_left[0]), float(omega_left[1])],
            "omega_right_interval_float": [float(omega_right[0]), float(omega_right[1])],
            "exact_assertions": [
                "upper(omega_left) < 0",
                "lower(omega_right) > 0",
                "continuity therefore gives at least one tau_* in (131/1000,132/1000) with Omega_even(xi_even)=0",
            ],
        },
        "analytic_formulas_checked": {
            "core": "N_M = Phi_p(x_M) + Omega_p(x_M)/M + R_M",
            "Omega": "a_p*G*(1+(1-tau)*x)",
            "near_resonant_limit": "M*N_M -> Q_p*log(s)*eta + Omega_p(xi_p) when M*(x_M-xi_p)->eta",
            "next_scaled_layer": "if x_M=xi+eta/M+zeta/M^2+o(M^-2), coefficient at M^-2 is Q log(s) zeta + 0.5 Q log(s)^2 eta^2 + aG(1-tau)eta",
        },
        "nonclaims": [
            "finite exact controls do not prove the asymptotic theorem; the proof is analytic",
            "existence of an intrinsic double-critical tau_* does not prove an actual arithmetic subsequence realizes exact phase resonance",
            "no uniform finite M0 over the full target region",
            "no collision-scaling theorem here",
            "no target-deformed A114 theorem",
            "no novelty/priority claim",
            "no physical or ontological interpretation",
        ],
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
