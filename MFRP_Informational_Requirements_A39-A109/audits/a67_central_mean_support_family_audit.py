#!/usr/bin/env python3
"""A67 exact audit: central-mean support-size family M=5,...,9.

Contract family
---------------
For each M in {5,6,7,8,9}:

    support = {0,...,M}, mean = M/2, target exponent mu=1,
    delta = 1/1875, epsilon = delta * ell_1(M,M/2),

and the fixed A64 optimal completion

    D_alpha = {alpha, 3, gamma_M}, alpha in [2,3),

with gamma_5=10, gamma_6=5, gamma_7=gamma_8=gamma_9=4.

The script constructs every exact active phase, isolates all algebraic
transitions, certifies primal-dual optimality and positive derivative on each
phase, and verifies exact continuity at every transition.

This is an exact theorem for the five declared support sizes. It is not yet a
symbolic theorem for arbitrary M.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any
from functools import lru_cache
import argparse

import sympy as sp

HERE = Path(__file__).resolve().parent
S = sp.Symbol("s")

DOMAIN_LOWER = sp.Rational(1, 8)
DOMAIN_UPPER = sp.Rational(1, 4)

FAMILY = {
    5: {
        "mean": sp.Rational(5, 2),
        "epsilon": sp.Rational(1, 10000),
        "gamma": 10,
        "phase_specs": [
            ((0, 1, 3, 5, 7, 8, 10, 12), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 5, 7, 8, 10, 12), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 5, 7, 8, 9, 10, 12), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 1, 2, 5, 7, 8, 9, 12), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 1, 2, 5, 7, 9, 12), (("alpha", 1), ("beta", -1))),
            ((1, 2, 5, 6, 7, 9, 12), (("alpha", 1), ("beta", -1))),
            ((1, 2, 5, 6, 7, 9, 12), (("alpha", 1), ("gamma", -1))),
        ],
        "approx_alpha": [
            2.274386321248,
            2.648586886262,
            2.876330478845,
            2.908567843187,
            2.911461258358,
            2.912942078443,
        ],
    },
    6: {
        "mean": sp.Rational(3),
        "epsilon": sp.Rational(1, 15000),
        "gamma": 5,
        "phase_specs": [
            ((0, 1, 2, 3, 6, 9, 11, 14), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 6, 8, 9, 11, 14), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 6, 8, 9, 10, 11, 14), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 6, 8, 10, 11, 14), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 6, 8, 10, 11, 14), (("alpha", 1), ("beta", -1))),
            ((0, 2, 6, 8, 10, 11, 14), (("alpha", 1), ("gamma", -1))),
        ],
        "approx_alpha": [2.3365, 2.8935, 2.9155, 2.9405, 2.9435],
    },
    7: {
        "mean": sp.Rational(7, 2),
        "epsilon": sp.Rational(1, 20000),
        "gamma": 4,
        "phase_specs": [
            ((1, 2, 3, 7, 8, 10, 12, 16), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 1, 2, 3, 7, 10, 12, 16), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 7, 9, 10, 12, 16), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 7, 9, 11, 12, 16), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 7, 9, 11, 12, 16), (("alpha", 1), ("beta", -1))),
            ((0, 2, 7, 9, 11, 12, 16), (("alpha", 1), ("gamma", -1))),
        ],
        "approx_alpha": [2.4005, 2.5855, 2.8575, 2.9405, 2.9445],
    },
    8: {
        "mean": sp.Rational(4),
        "epsilon": sp.Rational(1, 30000),
        "gamma": 4,
        "phase_specs": [
            ((1, 3, 8, 9, 11, 13, 14, 18), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 1, 3, 8, 11, 13, 14, 18), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 3, 8, 10, 11, 13, 14, 18), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 8, 10, 13, 14, 18), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 2, 3, 8, 10, 13, 14, 18), (("alpha", 1), ("beta", -1), ("gamma", -1))),
            ((0, 2, 8, 10, 13, 14, 18), (("alpha", 1), ("gamma", -1))),
        ],
        "approx_alpha": [2.6675, 2.7705, 2.8775, 2.9505, 2.9625],
    },
    9: {
        "mean": sp.Rational(9, 2),
        "epsilon": sp.Rational(1, 40000),
        "gamma": 4,
        "phase_specs": [
            ((1, 3, 9, 10, 12, 15, 16, 20), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((1, 3, 4, 9, 10, 12, 15, 20), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((1, 3, 9, 10, 12, 14, 15, 20), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 1, 3, 9, 12, 14, 15, 20), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 3, 9, 11, 12, 14, 15, 20), (("alpha", 1), ("beta", -1), ("gamma", 1))),
            ((0, 3, 9, 11, 14, 15, 20), (("alpha", 1), ("beta", -1))),
            ((0, 2, 3, 9, 11, 14, 15, 20), (("alpha", 1), ("beta", -1), ("gamma", -1))),
            ((0, 2, 9, 11, 14, 15, 20), (("alpha", 1), ("gamma", -1))),
        ],
        "approx_alpha": [2.4935, 2.7525, 2.7805, 2.8415, 2.9115, 2.9205, 2.9715],
    },
}


def cancel_factor(expression: sp.Expr) -> sp.Expr:
    return sp.cancel(expression)


def build_branch(
    maximum: int,
    mean: sp.Rational,
    epsilon: sp.Rational,
    gamma: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[tuple[str, int], ...],
) -> dict[str, Any]:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1
    target_values = [sp.Rational(1, 2**x) for x in support]

    rows: list[list[sp.Expr]] = []
    rhs: list[sp.Rational] = []

    def add(row: list[sp.Expr], value: sp.Rational) -> None:
        rows.append(row)
        rhs.append(value)

    row = [sp.Integer(0)] * dimension
    for i in range(count): row[i] = 1
    row[-1] = -1
    add(row, sp.Rational(0))

    row = [sp.Integer(0)] * dimension
    for i in range(count): row[count+i] = 1
    row[-1] = -1
    add(row, sp.Rational(0))

    row = [sp.Integer(0)] * dimension
    for i,x in enumerate(support): row[i] = x
    row[-1] = -mean
    add(row, sp.Rational(0))

    row = [sp.Integer(0)] * dimension
    for i,x in enumerate(support): row[count+i] = x
    row[-1] = -mean
    add(row, sp.Rational(0))

    row = [sp.Integer(0)] * dimension
    for i in range(count): row[count+i] = target_values[i]
    add(row, sp.Rational(1))

    exponent_map = {"alpha": None, "beta": 3, "gamma": gamma}
    for name, sign in active_observations:
        exponent = exponent_map[name]
        values = [S**x if exponent is None else sp.Rational(1,2**(exponent*x)) for x in support]
        row = [sp.Integer(0)] * dimension
        for i in range(count):
            row[i] = sign * values[i]
            row[count+i] = -sign * values[i]
        row[-1] = -2 * epsilon
        add(row, sp.Rational(0))

    if len(rows) != len(positive_indices):
        raise RuntimeError("active row/basic variable count mismatch")

    basis = sp.Matrix([[rows[r][c] for c in positive_indices] for r in range(len(rows))])
    if basis.det() == 0:
        raise RuntimeError("singular symbolic basis")
    z_basic = [cancel_factor(v) for v in basis.inv() * sp.Matrix(rhs)]
    z = [sp.Integer(0)] * dimension
    for c,v in zip(positive_indices,z_basic): z[c]=v

    objective = [sp.Integer(0)] * dimension
    for i in range(count): objective[i]=target_values[i]
    ratio = cancel_factor(sum(objective[i]*z[i] for i in range(dimension)))

    dual = [cancel_factor(v) for v in basis.T.inv() * sp.Matrix([objective[c] for c in positive_indices])]
    reduced = [cancel_factor(sum(rows[r][c]*dual[r] for r in range(len(rows))) - objective[c]) for c in range(dimension)]

    conditions: list[tuple[str,sp.Expr]] = []
    for c,v in zip(positive_indices,z_basic): conditions.append((f"basic_{c}",v))
    for r,(name,sign) in enumerate(active_observations,start=5): conditions.append((f"active_dual_{name}_{sign:+d}",dual[r]))
    for c in range(dimension):
        if c not in positive_indices: conditions.append((f"reduced_cost_{c}",reduced[c]))

    active_set=set(active_observations)
    for name in ["alpha","beta","gamma"]:
        exponent=exponent_map[name]
        values=[S**x if exponent is None else sp.Rational(1,2**(exponent*x)) for x in support]
        diff=cancel_factor(sum(values[i]*(z[i]-z[count+i]) for i in range(count)))
        for sign in [1,-1]:
            if (name,sign) not in active_set:
                conditions.append((f"inactive_slack_{name}_{sign:+d}",cancel_factor(2*epsilon*z[-1]-sign*diff)))

    n,d=sp.fraction(ratio)
    kappa=cancel_factor(-S*(sp.diff(n,S)*d-n*sp.diff(d,S))/d**2)
    return {"positive_indices":positive_indices,"active_observations":active_observations,"ratio":ratio,"conditions":conditions,"kappa":kappa}


def primitive_poly(expr: sp.Expr) -> sp.Poly:
    p=sp.Poly(expr,S,domain=sp.QQ)
    _,prim=sp.primitive(p.as_expr(),S)
    return sp.Poly(prim,S,domain=sp.QQ)


def isolate_near(poly: sp.Poly, approx_alpha: float, neighboring_alphas: list[float]) -> dict[str,Any]:
    approx_s=2.0**(-approx_alpha)
    all_s=[DOMAIN_UPPER]+[sp.Float(2.0**(-a),30) for a in neighboring_alphas]+[DOMAIN_LOWER]
    # find matching position in decreasing s list using alpha order
    index=neighboring_alphas.index(approx_alpha)+1
    upper_mid=(float(all_s[index-1])+float(all_s[index]))/2
    lower_mid=(float(all_s[index])+float(all_s[index+1]))/2
    lo=sp.Rational(str(min(lower_mid,upper_mid)))
    hi=sp.Rational(str(max(lower_mid,upper_mid)))
    intervals=sp.intervals(poly,eps=sp.Rational(1,10**14))
    candidates=[]
    for (l,r),mult in intervals:
        if r < lo or l > hi: continue
        candidates.append((l,r,mult))
    if len(candidates)!=1:
        raise RuntimeError(f"expected one root near alpha={approx_alpha}, got {candidates}")
    l,r,m=candidates[0]
    return {"kind":"algebraic_root","left":l,"right":r,"multiplicity":m,"polynomial":poly,"s_decimal":float(sp.N((l+r)/2,30)),"alpha_decimal":float(sp.N(-sp.log((l+r)/2,2),30))}


def rational_boundary(value: sp.Rational) -> dict[str,Any]:
    return {"kind":"rational","left":value,"right":value,"multiplicity":1,"s_decimal":float(value),"alpha_decimal":float(-sp.log(value,2))}


@lru_cache(maxsize=None)
def roots_of_poly(poly_text: str) -> tuple[tuple[sp.Rational,sp.Rational,int], ...]:
    p=sp.Poly(sp.sympify(poly_text),S,domain=sp.QQ)
    out=[]
    for (l,r),m in sp.intervals(p,eps=sp.Rational(1,10**12)):
        if r < DOMAIN_LOWER or l > DOMAIN_UPPER: continue
        out.append((l,r,m))
    return tuple(out)

def roots_in_domain(expr: sp.Expr) -> list[tuple[sp.Rational,sp.Rational,int]]:
    if expr == 0: return []
    p=primitive_poly(expr)
    if p.degree()<=0: return []
    return list(roots_of_poly(str(p.as_expr())))


def certify_positive(expr: sp.Expr, lower: dict[str,Any], upper: dict[str,Any]) -> dict[str,Any]:
    expr=sp.cancel(expr)
    if expr==0:
        return {"ok":True,"identically_zero":True,"sample_sign":0}
    num,den=sp.fraction(expr)
    result={"identically_zero":False}
    for label,part in [("numerator",num),("denominator",den)]:
        interior=[]; lower_hits=[]; upper_hits=[]
        for l,r,m in roots_in_domain(part):
            if l>lower["right"] and r<upper["left"]: interior.append((l,r,m))
            elif not (r<lower["left"] or l>lower["right"]): lower_hits.append((l,r,m))
            elif not (r<upper["left"] or l>upper["right"]): upper_hits.append((l,r,m))
        result[f"interior_{label}_roots"]=len(interior)
        if interior:
            return {**result,"ok":False,"failure":f"interior_{label}_root"}
        if label=="denominator" and ((lower["kind"]=="algebraic_root" and lower_hits) or (upper["kind"]=="algebraic_root" and upper_hits)):
            return {**result,"ok":False,"failure":"denominator_zero_at_transition"}
    sample=(lower["right"]+upper["left"])/2
    value=sp.factor(expr.subs(S,sample))
    result.update({"sample":str(sample),"sample_sign":int(sp.sign(value)),"ok":bool(value>0)})
    if not result["ok"]: result["failure"]="nonpositive_sample"
    return result


def serialize_boundary(b: dict[str,Any]) -> dict[str,Any]:
    out={"kind":b["kind"],"left":str(b["left"]),"right":str(b["right"]),"s_decimal":str(sp.N((b["left"]+b["right"])/2,40)),"alpha_decimal":str(sp.N(-sp.log((b["left"]+b["right"])/2,2),40))}
    if b["kind"]=="algebraic_root": out.update({"polynomial":str(b["polynomial"].as_expr()),"multiplicity":b["multiplicity"]})
    return out


def audit_M(M: int, spec: dict[str,Any]) -> dict[str,Any]:
    branches=[build_branch(M,spec["mean"],spec["epsilon"],spec["gamma"],p,a) for p,a in spec["phase_specs"]]
    transitions=[]
    for i,(left,right,approx) in enumerate(zip(branches[:-1],branches[1:],spec["approx_alpha"]),start=1):
        diff=sp.cancel(left["ratio"]-right["ratio"])
        num=sp.fraction(diff)[0]
        poly=primitive_poly(num)
        boundary=isolate_near(poly,approx,spec["approx_alpha"])
        dl=sp.Poly(sp.fraction(left["ratio"])[1],S,domain=sp.QQ)
        dr=sp.Poly(sp.fraction(right["ratio"])[1],S,domain=sp.QQ)
        transitions.append({"from_phase":i,"to_phase":i+1,"boundary":boundary,"left_denominator_nonzero":sp.gcd(dl,poly).degree()==0,"right_denominator_nonzero":sp.gcd(dr,poly).degree()==0})

    boundaries=[rational_boundary(DOMAIN_UPPER)]+[t["boundary"] for t in transitions]+[rational_boundary(DOMAIN_LOWER)]
    phases=[]
    for i,branch in enumerate(branches):
        upper=boundaries[i]; lower=boundaries[i+1]
        certs=[]
        for name,expr in [*branch["conditions"],("kappa",branch["kappa"])]:
            certs.append({"name":name,**certify_positive(expr,lower,upper)})
        phases.append({"phase":i+1,"positive_indices":list(branch["positive_indices"]),"active_observations":[list(x) for x in branch["active_observations"]],"s_lower":serialize_boundary(lower),"s_upper":serialize_boundary(upper),"ratio":str(branch["ratio"]),"kappa":str(branch["kappa"]),"condition_count":len(certs),"all_conditions_certified":all(c["ok"] for c in certs),"conditions":certs})

    boundary_ratio=sp.factor(branches[0]["ratio"].subs(S,DOMAIN_UPPER))
    limit_ratio=sp.limit(branches[-1]["ratio"],S,DOMAIN_LOWER,dir="+")
    gates={
        "all_phase_conditions_certified":all(p["all_conditions_certified"] for p in phases),
        "all_phase_derivatives_positive":all(next(c for c in p["conditions"] if c["name"]=="kappa")["ok"] for p in phases),
        "all_transitions_simple":all(t["boundary"]["multiplicity"]==1 for t in transitions),
        "all_transition_denominators_finite":all(t["left_denominator_nonzero"] and t["right_denominator_nonzero"] for t in transitions),
        "coalescence_limit_above_boundary":bool(limit_ratio>boundary_ratio),
    }
    return {"maximum":M,"mean":str(spec["mean"]),"epsilon":str(spec["epsilon"]),"gamma":spec["gamma"],"design":f"{{alpha,3,{spec['gamma']}}}","alpha_domain":"[2,3)","phase_count":len(phases),"transition_count":len(transitions),"boundary_ratio":str(boundary_ratio),"boundary_risk_decimal":str(sp.N(sp.log(boundary_ratio)/(2*sp.log(2)),50)),"coalescence_ratio_limit":str(limit_ratio),"coalescence_risk_limit_decimal":str(sp.N(sp.log(limit_ratio)/(2*sp.log(2)),50)),"transitions":[{"from_phase":t["from_phase"],"to_phase":t["to_phase"],"boundary":serialize_boundary(t["boundary"]),"left_denominator_nonzero":t["left_denominator_nonzero"],"right_denominator_nonzero":t["right_denominator_nonzero"]} for t in transitions],"phases":phases,"gates":gates,"verdict":"PASS" if all(gates.values()) else "FAIL"}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--M",type=int,default=None)
    args=parser.parse_args()
    selected=[args.M] if args.M is not None else sorted(FAMILY)
    family_results=[]
    for M in selected:
        print(f"Auditing M={M}...",flush=True)
        result_M=audit_M(M,FAMILY[M])
        family_results.append(result_M)
        (HERE/f"a67_support_M{M}_result.json").write_text(json.dumps(result_M,indent=2),encoding="utf-8")
        print(json.dumps({"M":M,"phase_count":result_M["phase_count"],"transition_count":result_M["transition_count"],"verdict":result_M["verdict"],"root_cache_size":roots_of_poly.cache_info().currsize},indent=2),flush=True)
    if args.M is not None:
        if not all(all(r["gates"].values()) for r in family_results): raise SystemExit(1)
        return
    total_phases=sum(r["phase_count"] for r in family_results)
    total_transitions=sum(r["transition_count"] for r in family_results)
    gates={
        "all_five_support_contracts_pass":all(all(r["gates"].values()) for r in family_results),
        "all_exact_phase_derivatives_positive":all(r["gates"]["all_phase_derivatives_positive"] for r in family_results),
        "all_exact_phase_conditions_certified":all(r["gates"]["all_phase_conditions_certified"] for r in family_results),
        "all_phase_transitions_simple_and_finite":all(r["gates"]["all_transitions_simple"] and r["gates"]["all_transition_denominators_finite"] for r in family_results),
        "boundary_unique_global_minimum_all_supports":all(r["gates"]["coalescence_limit_above_boundary"] for r in family_results),
    }
    result={"audit":"A67_CENTRAL_MEAN_SUPPORT_SIZE_FAMILY","contract_family":{"support_maxima":[5,6,7,8,9],"mean":"M/2","target_exponent":1,"delta":"1/1875","first_anchor_domain":"[2,3)","fixed_second_anchor":3,"third_anchors":{"5":10,"6":5,"7":4,"8":4,"9":4}},"family_summary":{"support_count":5,"total_phase_count":total_phases,"total_transition_count":total_transitions,"phase_counts":{str(r["maximum"]):r["phase_count"] for r in family_results},"transition_counts":{str(r["maximum"]):r["transition_count"] for r in family_results},"theorem":"For each declared M and its A64 optimal completion, the exact minimax ratio is continuous and strictly increasing on alpha in [2,3); therefore alpha*=2 is the unique global first-anchor optimum."},"supports":family_results,"gates":gates,"verdict":"PASS_EXACT_CENTRAL_MEAN_SUPPORT_SIZE_FAMILY_THEOREM" if all(gates.values()) else "FAIL_A67_FAMILY_AUDIT","boundary":"This is an exact five-member support-size family theorem for M=5,...,9, not a symbolic theorem for arbitrary integer M and not a joint reoptimization theorem."}
    out=HERE/"a67_central_mean_support_family_results.json"
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    summary={"audit":result["audit"],"gate_count":len(gates),"pass_count":sum(gates.values()),"phase_counts":result["family_summary"]["phase_counts"],"transition_counts":result["family_summary"]["transition_counts"],"total_phase_count":total_phases,"total_transition_count":total_transitions,"failed_gates":[k for k,v in gates.items() if not v],"verdict":result["verdict"]}
    print(json.dumps(summary,indent=2))
    if not all(gates.values()): raise SystemExit(1)

if __name__=="__main__":
    main()
