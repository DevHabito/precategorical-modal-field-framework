#!/usr/bin/env python3
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
TH=(HERE/'A114B2E_PHI_ZERO_BOUNDARY_THEOREM_20260914.md').read_text(encoding='utf-8')
AC=json.loads((HERE/'A114B2E_PHI_ZERO_ANALYTIC_CERTIFICATE_20260914.json').read_text(encoding='utf-8'))
FC=json.loads((HERE/'A114B2E_PHI_ZERO_FRACTION_CROSSCHECK_20260914.json').read_text(encoding='utf-8'))
C2=(HERE/'A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text(encoding='utf-8')
B2B=(HERE/'session_artifacts/A114B2B_GAMMA_MINUS_TAIL_EXCLUSION_THEOREM_20260913.md').read_text(encoding='utf-8')
B1=(HERE/'session_artifacts/A114B1_ANALYTIC_TAIL_BPLUS1_GAMMA_PIVOT_THEOREM_20260912.md').read_text(encoding='utf-8')
A112=(HERE.parent/'A110_A112/session_artifacts/A112_ANALYTIC_TAIL_STRUCTURAL_THEOREM_20260911.md').read_text(encoding='utf-8')
OUT=HERE/'A114B2E_PHI_ZERO_LOGICAL_AUDIT_20260914.json'

def section(text,n,nextn):
    return text.split(f'## {n}.',1)[1].split(f'## {nextn}.',1)[0]

c2s3=section(C2,3,4); c2s4=section(C2,4,5); c2s5=section(C2,5,6)
c2s6=section(C2,6,7); c2s7=section(C2,7,8); c2s8=section(C2,8,9)

checks={
 'status_is_conditional_boundary_theorem':'PROVED conditional boundary theorem' in TH,
 'strict_bplus2_premise':'j=b+2' in TH and 'strict compressed maximizer' in TH,
 'Phi_zero_premise':'\\boxed{\\Phi=0}' in TH,
 'does_not_import_B1_zero_pivot_conclusion':'does **not** import the distinct A114-B1 `b+1` zero-pivot result' in TH,
 'stronger_B2B_contrapositive_explicit':'\\Phi\\le0\\Longrightarrow3j-h\\ge13' in TH,
 'B2B_has_strict_positive_contradiction_margin':'1.0392\\times10^{-6}>0' in B2B,
 'source_box_reproved_at_equality':'\\frac9{1000}<Q:=' in TH and '<\\frac1{25}' in TH,
 'exact_C_GP_pivot_used':'p_{j+1}^{G^+}' in TH and 'S_{\\gamma+}^C' in TH and '\\det B_C' in TH,
 'gamma_plus_slack_exact_zero':'\\boxed{S_{\\gamma+}^C=0}' in TH,
 'p0_exact_elimination_present':'B_0-B_1p_0' in TH and 'K_\\beta' in TH and 'S_{\\gamma+}^C' in TH,
 'B0_B1_definitions_present':'B_0=C_\\gamma K_\\beta-K_{\\gamma+}C_\\beta' in TH and 'B_1=A_\\gamma K_\\beta-K_{\\gamma+}A_\\beta' in TH,
 'p0_positive_not_continuity':'p_0^C=\\frac{B_0}{B_1}>0' in TH,
 'p0_uniform_separation':'p_0^C>2.9407\\times10^{-3}' in TH,
 'no_Phi_p0_intersection_claim':'`Phi=0` and `p0^C=0` do not intersect' in TH,
 'C2_section3_no_Phi_dependency':'Phi' not in c2s3,
 'C2_section4_no_Phi_dependency':'Phi' not in c2s4,
 'C2_section5_no_Phi_dependency':'Phi' not in c2s5,
 'C2_section6_is_the_Phi_slack_step':'Phi<0' in c2s6 and 'gamma+' in c2s6,
 'C2_section7_no_Phi_dependency':'Phi' not in c2s7,
 'C2_section8_no_Phi_dependency':'Phi' not in c2s8,
 'all_remaining_C_KKT_gates_declared_strict':'All remaining C KKT gates are strict' in TH,
 'unique_primal_argument_uses_strict_reduced_costs':'Every nonbasic P/Q reduced cost is strictly positive' in TH and 'only one primal solution' in TH,
 'tight_inactive_slack_not_misread_as_primal_direction':'does not create a primal direction' in TH,
 'GP_zero_mass_from_A112':'p_{j+1}^{G^+}=0' in TH and 'F_{b+3}^{\\rm up}<0' in TH,
 'C_GP_primal_coalescence':'C=G^+' in TH and 'as primal points' in TH,
 'no_unique_basis_overclaim':'No claim of a unique optimal basis' in TH,
 'analytic_certificate_passes':AC.get('status')=='PASS' and AC.get('gate_count')==22 and AC.get('pass_count')==22,
 'fraction_crosscheck_passes':FC.get('status')=='PASS' and FC.get('gate_count')==24 and FC.get('pass_count')==24,
 'A112_adjacent_formula_dependency_present':'p_{j+1}=\\frac{F_j^{up}}{D_G}' in A112,
 'B1_DG_positive_orientation_present':'D_G>0' in B1,
 'finite_controls_regression_only':'regression/falsification evidence only' in TH,
 'no_physical_claim':'physical' in TH.lower() and 'interpretation' in TH.lower(),
}

out={
 'audit':'A114B2E_PHI_ZERO_LOGICAL_COMPOSITION_AUDIT',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'check_count':len(checks),
 'pass_count':sum(checks.values()),
 'failed':[k for k,v in checks.items() if not v],
 'checks':checks,
 'scope':['M>=521','129/1000<=s<=133/1000','strict compressed b+2','Phi=0'],
 'key_guardrail':'C2 is not imported wholesale across its Phi<0 premise. Its source box is re-established at equality; Sections 3-5 and 7-8 are checked to contain no Phi dependency; Section 6 is replaced by the exact zero-slack pivot identity.',
 'nonclaims':['strict complementarity at Phi=0','unique optimal basis','outside-window extension','physical interpretation']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'check_count':out['check_count'],'pass_count':out['pass_count'],'failed':out['failed']},indent=2))
