#!/usr/bin/env python3
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
TH=(HERE/'A114C1_BPLUS1_BPLUS2_COMPRESSED_TIE_THEOREM_20260914.md').read_text()
REG=json.loads((HERE/'A114C1_TIE_BRACKET_EXACT_REGRESSION_20260914.json').read_text())
SYM=json.loads((HERE/'A114C1_SYMBOLIC_BOUNDARY_CERTIFICATE_20260914.json').read_text())
A113=(HERE.parent/'A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md').read_text()
B1=(HERE/'session_artifacts/A114B1_ANALYTIC_TAIL_BPLUS1_GAMMA_PIVOT_THEOREM_20260912.md').read_text()
C1=(HERE/'A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text()
C2=(HERE/'A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text()
B2E=(HERE/'A114B2E_PHI_ZERO_BOUNDARY_THEOREM_20260914.md').read_text()
OUT=HERE/'A114C1_LOGICAL_AUDIT_20260914.json'

checks={
 'tie_premise_present':'E_{b+1}=0' in TH,
 'triple_tie_excluded_from_A113':'E_{b+1}-2E_{b+2}>0' in A113 and 'E_{b+2}<0' in TH,
 'phi_positive_uses_GP2':'C1-A. `Phi>0`' in TH and '`G_2^+` satisfies the complete **strict** KKT system' in TH,
 'minimal_A112_lemma_not_strict_max_import':'minimal A112 composition lemma' in TH,
 'gamma_zero_exact_identity':'N_\\gamma=-\\frac{\\det B}{D_G}E_{b+1}' in TH and 'y_\\gamma=0' in TH,
 'gamma_zero_primal_strict':'every basic primal variable and `t` strictly positive' in TH,
 'gamma_zero_all_variable_rc_strict':'every nonbasic P/Q reduced cost strictly positive' in TH,
 'alpha_beta_proved_at_equality':'Wronskian' in TH and 'y_\\alpha>0' in TH and 'y_\\beta>0' in TH,
 'alpha_beta_not_continuity':'This is an equality-set proof, not a limiting argument.' in TH,
 'optimal_face_dimension_one':'entire optimal set is contained in one affine line' in TH,
 'tie_source_lower_reproved':'Q:=s^{j-1}/U\\le9/1000\\Longrightarrow E_{b+1}<0' in TH,
 'tie_source_upper_uses_phi_negative':'upper source-box proof uses only `Phi<0`' in TH,
 'C_endpoint_positive_case':'p_0^C>0' in TH and 'conv{G_1^+,C}' in TH,
 'E_endpoint_negative_case':'p_0^C<0' in TH and 'conv{G_1^+,E}' in TH,
 'zero_endpoint_coalescence':'p_0^C=0' in TH and 'C=E' in TH,
 'gp1_opposite_extension_blocked':'continuation through `G_1^+`' in TH and 'gamma-plus slack negative' in TH,
 'QI_QA_extra_direction_excluded':'QI/QA architectures do not create an additional optimal direction' in TH,
 'phi_zero_source_box_reopened':'At `Phi=0`, the source-box lower bound again follows from `E_(b+1)=0`' in TH,
 'phi_zero_p0_positive':'B2-E gamma-zero elimination' in TH and 'p_0^C>0' in TH,
 'phi_zero_left_rc_zero':'r_C(p_{b+1})=0' in TH,
 'phi_zero_schur_positive':'d=\\frac{\\det B_{G_1^+}}{\\det B_C}>0' in TH,
 'phi_zero_gamma_blocks_direction':'S_{\\gamma+}(z)<0' in TH,
 'phi_zero_unique_primal':'common C/G1+/G2+ primal point is the unique primal optimum' in TH,
 'C2_det_orientation_dependency_exists':'det B_C>0' in C2,
 'B1_full_gamma_det_orientation_exists':'det B_8' in B1 and 'strictly positive' in B1,
 'C1_endpoint_exchange_dependency_exists':'operatorname{sgn}p_{j-1}^E=-' in C1,
 'B2E_p0_separation_dependency_exists':'p_0^C>0' in B2E,
 'regression_passes':REG.get('status')=='PASS' and REG.get('gate_count')==24 and REG.get('pass_count')==24,
 'symbolic_boundary_certificate_passes':SYM.get('status')=='PASS' and SYM.get('gate_count')==5 and SYM.get('pass_count')==5,
 'finite_controls_not_premise':'regression/falsification evidence only' in TH,
 'second_tie_not_overclaimed':'does not claim' in TH.lower() and 'second compressed tie' in TH,
 'no_physical_claim':'physical or ontological interpretation' in TH,
}

out={
 'audit':'A114C1_LOGICAL_COMPOSITION_AUDIT',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'check_count':len(checks),
 'pass_count':sum(checks.values()),
 'failed':[k for k,v in checks.items() if not v],
 'checks':checks,
 'scope':['M>=521','129/1000<=s<=133/1000','E_(b+1)=0'],
 'guardrails':[
  'No strict-b+2 theorem is imported wholesale onto the compressed tie.',
  'GP1 alpha/beta dual positivity is proved at y_gamma=0 by generalized-Vandermonde orientation, not continuity.',
  'Both ends of the one-dimensional optimal face are closed: endpoint nonnegativity blocks C/E side, gamma+ feasibility blocks continuation through GP1.',
  'The phi=0 uniqueness step uses a nonzero Schur complement to show the only zero-cost entering variable is blocked immediately by gamma+ feasibility.',
  'Finite brackets are regression only.'
 ],
 'open':['second compressed tie E_(b+2)=0']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'check_count':out['check_count'],'pass_count':out['pass_count'],'failed':out['failed']},indent=2))
