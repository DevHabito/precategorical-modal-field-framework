#!/usr/bin/env python3
"""Exact interval certificate for A76.

This script certifies the actual M=21,22,23 active branches on
s in [13/100,33/250], the exclusion of the opposite gamma sign,
the actual Cramer orientations, and the primal infeasibility of the old
A75 candidate at M=22,23.
"""
from __future__ import annotations
import importlib.util, json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
CORE=HERE/'a76_active_reentry_core.py'
A67=HERE/'a67_central_mean_support_family_audit.py'
A75=HERE/'a75_parity_orientation_results.json'
DISC=HERE/'a76_M21_M23_phase_discovery.json'

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    core=load_module(CORE,'a76_core_interval')
    a67=load_module(A67,'a67_for_a76_interval')
    a75=json.loads(A75.read_text())
    discovery=json.loads(DISC.read_text())
    discovery_map={x['maximum']:x for x in discovery['supports']}
    alpha_probe=float(sp.N(-sp.log(core.S0,2),30))

    selected={}; opposite={}; cramer={}; old={}; discovery_checks={}
    condition_count=0; condition_ok=[]; opposite_ok=[]; cramer_ok=[]

    for M in [21,22,23]:
        active=core.actual_active_observations(M)
        branch=core.build_branch(a67,M,core.actual_positive_indices(M),active)
        conds=[]
        for name,expr in branch['conditions']:
            cert=core.rational_sign(expr,a67.S)
            conds.append({'name':name,'certificate':cert})
            condition_ok.append(cert['sign']==1)
        condition_count += len(conds)
        selected[str(M)]={
            'signature':core.actual_signature(M),
            'condition_count':len(conds),
            'all_conditions_positive':all(c['certificate']['sign']==1 for c in conds),
            'conditions':conds,
            'ratio_at_probe':str(sp.factor(branch['ratio'].subs(a67.S,core.S0))),
            'risk_at_probe_decimal':str(sp.N(sp.log(branch['ratio'].subs(a67.S,core.S0))/(2*sp.log(2)),50)),
        }

        opp=-active[-1][1]
        opp_branch=core.build_branch(a67,M,core.actual_positive_indices(M),(('alpha',1),('beta',-1),('gamma',opp)))
        cname='active_dual_gamma_'+('+1' if opp>0 else '-1')
        expr=core.condition_expression(opp_branch,cname)
        cert=core.rational_sign(expr,a67.S)
        opposite_ok.append(cert['sign']==-1)
        opposite[str(M)]={
            'opposite_gamma_sign':opp,
            'multiplier_name':cname,
            'multiplier':str(expr),
            'certificate':cert,
            'value_at_probe':str(sp.factor(expr.subs(a67.S,core.S0))),
        }

        dets=core.actual_gamma_determinants(M)
        ncert=core.polynomial_sign(dets['numerator'],dets['variable'])
        dcert=core.polynomial_sign(dets['denominator'],dets['variable'])
        msign=ncert['sign']*dcert['sign']
        expected=1 if M in {21,22} else -1
        cramer_ok.append(msign==expected)
        cramer[str(M)]={
            'gamma_plus_numerator':str(dets['numerator']),
            'gamma_plus_denominator':str(dets['denominator']),
            'numerator_certificate':ncert,
            'denominator_certificate':dcert,
            'gamma_plus_multiplier_sign':msign,
        }

        observed=core.discovery_signature_at_probe(discovery_map[M],alpha_probe)
        expected_sig=core.actual_signature(M)
        discovery_checks[str(M)]={'observed':observed,'expected':expected_sig,'matches':observed==expected_sig}

    finite={r['maximum']:r for r in a75['finite_Bernstein_certificates']}
    for M in [22,23]:
        branch=core.build_branch(a67,M,core.old_candidate_indices(M),(('alpha',1),('beta',-1),('gamma',1)))
        expr=core.condition_expression(branch,'basic_4')
        cert=core.rational_sign(expr,a67.S)
        old[str(M)]={
            'A75_gamma_plus_multiplier_sign':finite[M]['multiplier_sign'],
            'basic_4':str(expr),
            'basic_4_certificate':cert,
            'basic_4_value_at_probe':str(sp.factor(expr.subs(a67.S,core.S0))),
        }

    gates={
        'A75_previous_audit_passed':all(a75['gates'].values()),
        'numerical_discovery_has_seven_phases_each':all(discovery_map[M]['phase_count']==7 for M in [21,22,23]),
        'discovery_signature_at_probe_matches_exact_branch':all(x['matches'] for x in discovery_checks.values()),
        'all_159_selected_branch_KKT_conditions_positive_on_interval':condition_count==159 and all(condition_ok),
        'opposite_gamma_sign_multiplier_negative_for_all_three_supports':len(opposite_ok)==3 and all(opposite_ok),
        'actual_gamma_plus_Cramer_orientation_is_plus_plus_minus':len(cramer_ok)==3 and all(cramer_ok),
        'actual_M21_M22_gamma_plus_and_M23_gamma_minus_selected':all(selected[str(M)]['all_conditions_positive'] for M in [21,22,23]),
        'A75_old_candidate_positive_at_M22_M23_but_primal_infeasible':all(old[str(M)]['A75_gamma_plus_multiplier_sign']==1 and old[str(M)]['basic_4_certificate']['sign']==-1 for M in [22,23]),
    }
    result={
        'audit':'A76_INTERVAL_ACTIVE_SET_CERTIFICATE',
        'interval':{
            's_lower':str(core.INTERVAL_LOWER),'s_upper':str(core.INTERVAL_UPPER),
            'alpha_lower_decimal':str(sp.N(-sp.log(core.INTERVAL_UPPER,2),50)),
            'alpha_upper_decimal':str(sp.N(-sp.log(core.INTERVAL_LOWER,2),50)),
            'probe_s':str(core.S0),'probe_alpha_decimal':str(sp.N(-sp.log(core.S0,2),50)),
        },
        'selected_interval_certificates':selected,
        'opposite_sign_certificates':opposite,
        'actual_Cramer_certificates':cramer,
        'old_candidate_primal_infeasibility':old,
        'discovery_checks':discovery_checks,
        'gates':gates,
        'verdict':'PASS' if all(gates.values()) else 'FAIL',
    }
    out=HERE/'a76_interval_certificate_results.json'; out.write_text(json.dumps(result,indent=2))
    print(json.dumps({'gate_count':len(gates),'pass_count':sum(gates.values()),'condition_count':condition_count,'verdict':result['verdict'],'output':out.name},indent=2))
    if not all(gates.values()): raise SystemExit(1)
if __name__=='__main__': main()
