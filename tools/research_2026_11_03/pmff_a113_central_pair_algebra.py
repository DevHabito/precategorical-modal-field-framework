#!/usr/bin/env python3
"""Exact symbolic A113 central-pair algebra, not a central sign theorem.

The seven k-channel values are represented by independent formal variables.
Every (k+1) power is represented as (base)*[k-power], so polynomial
normalization can be checked without numerical logs, fitting or sampling.
"""
import sympy as sp

k = sp.symbols("k", integer=True, nonnegative=True)
beta, source, target, mass, h_beta, h_source = sp.symbols(
    "beta source target mass h_beta h_source")
coeff_beta, coeff_source, coeff_target = sp.symbols(
    "coeff_beta coeff_source coeff_target")
lin_beta, lin_source, lin_target, const = sp.symbols(
    "lin_beta lin_source lin_target const")
p_bs, p_bt, p_st, p_b, p_s, p_t = sp.symbols(
    "p_bs p_bt p_st p_b p_s p_t")

p = [
    (mass * (source-beta), beta*source, p_bs),
    (h_source * (beta-target), beta*target, p_bt),
    (h_beta * (target-source), source*target, p_st),
]
channels = [
    (coeff_beta, lin_beta, beta, p_b),
    (coeff_source, lin_source, source, p_s),
    (coeff_target, lin_target, target, p_t),
]
at_k = sum((weight * power) for weight, _, power in p) + sum(
    (c + k*d)*power for c,d,_,power in channels) + const
at_next = sum(weight * base * power for weight,base,power in p) + sum(
    (c + (k+1)*d)*base*power for c,d,base,power in channels) + const
transformed = sum(weight*(1-2*base)*power for weight,base,power in p) + sum(
    ((1-2*base)*(c+k*d)-2*base*d)*power
    for c,d,base,power in channels) - const
assert sp.expand(at_k-2*at_next-transformed)==0

half = sp.Rational(1,2)
assert sp.expand(
    (coeff_target+k*lin_target)*p_t -
    2*(coeff_target+(k+1)*lin_target)*half*p_t +
    lin_target*p_t)==0

# Negative control: the target linear term is NOT +d*(1/2)^k.
wrong=sp.expand(
    (coeff_target+k*lin_target)*p_t -
    2*(coeff_target+(k+1)*lin_target)*half*p_t -
    lin_target*p_t)
assert wrong != 0 and sp.simplify(wrong+2*lin_target*p_t)==0

print("A113 central pair seven-channel identity: PASS (symbolic)")
print("A113 half-target affine cancellation: PASS (symbolic)")
print("A113 target-linear sign mutation negative control: PASS")
print("SCOPE: exact algebra only; no continuous sign or global A113 proof")
