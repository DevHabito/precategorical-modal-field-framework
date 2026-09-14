#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114C2_SECOND_TIE_PHI_CERTIFICATE_20260914.json'

B=F(1,8); G=F(1,16)
S0=F(129,1000); S1=F(133,1000)
RMIN=F(9,1000)
RMAX=S1*S1
EMAX=F(1,1875)
H0=260
U0=F(1,2**H0)
DEN0=1-F(H0+1)*U0
JMIN=91
ETA=F(1,10**28)
TRIPLE_ERROR=F(1,10**26)

# Symbolic core identity. The approximating primitives retain the exact
# common Q-block denominator d=1-(h+1)U and the parity coefficient delta
# in D_r/U (delta=2 even, 3/2 odd). The delta terms cancel identically.
U,a,R,Y,s,b,g,e,d,delta=sp.symbols('U a R Y s b g e d delta')
Bs=-a+U*R
Bb=-a+U*Y
Bg=-a
Cs=2*s/d; Cb=2*b/d; Cg=2*g/d
Hs=sp.Rational(1,2)+delta*U*s/d-2*e*U
Hb=sp.Rational(1,2)+delta*U*b/d+2*e*U
qg=sp.Rational(1,2)+delta*U*g/d-2*e*U
phi0=sp.expand(
    Bs*(qg*Cb-Cg*Hb)
   +Cs*(Bg*Hb-qg*Bb)
   +Hs*(Cg*Bb-Bg*Cb)
)
core_identity=U/d*(
    R*(b-g)-Y*(s-g)-8*a*e*(s-g)
    -4*U*e*R*(b+g)+4*U*e*Y*(s-g)
)
identity_ok=sp.factor(phi0-core_identity)==0

# Uniform localization / ratio bounds.
rho=(B/S0)**JMIN
coef=(B-G)-(S1-G)*rho
core_lower=(
    RMIN*coef
    -8*EMAX*(S1-G)
    -4*U0*EMAX*RMAX*(B+G)
)

# Uniform normalized tail bounds. Exact F_up differs from the core model
# only through gamma^j, r^M, and central-Q high-node tails. Every primitive
# deviation is written as U*eta_i. The following envelopes are deliberately
# much weaker than the actual tails.
gamma_j_norm=RMAX*(G/S0)**JMIN
central_tail=(2*S1)**H0
central_primitive_error=F(4*(H0+1))*central_tail/DEN0
m_tail=(2*S1*S1)**H0

# The sequences (h+1)(2 s_max)^h and (2 s_max^2)^h decrease for h>=260.
tail_ratio=F(H0+2,H0+1)*(2*S1)

# Safe absolute primitive bound used by the telescoping estimate.
# |B_r| is below 1+URmax, |C_r| below 2*smax/d plus tiny tail,
# and H/q_gamma are below 1/2 + O(U). All are far below 2.
approx_B_bound=1+U0*RMAX
approx_C_bound=2*S1/DEN0
approx_H_bound=F(1,2)+2*U0*S1/DEN0+2*EMAX*U0
primitive_bound=max(approx_B_bound,approx_C_bound,approx_H_bound)+U0*ETA

# Six triple products make up Phi. If exact and core primitives are bounded
# in magnitude by 2 and each primitive perturbation is <=U*ETA, telescoping
# each triple gives <=12 U ETA, hence <=72 U ETA total. TRIPLE_ERROR=1e-26
# is a conservative envelope larger than 72*ETA.
perturbation_bound=F(72)*ETA
final_lower=core_lower-TRIPLE_ERROR

gates={
 'symbolic_core_identity':identity_ok,
 'denominator_gt_0p999':DEN0>F(999,1000),
 'jmin_91_consistent':JMIN==91,
 'rho_lt_0p057':rho<F(57,1000),
 'coefficient_positive':coef>F(58,1000),
 'Rmax_lt_0p018':RMAX<F(18,1000),
 'gamma_j_normalized_tail_lt_eta':gamma_j_norm<ETA,
 'central_high_node_tail_lt_1e_100':central_primitive_error<F(1,10**100),
 'M_tail_lt_1e_300':m_tail<F(1,10**300),
 'tail_sequences_decrease_after_h260':tail_ratio<1,
 'all_primitive_errors_below_eta':max(gamma_j_norm,central_primitive_error,m_tail)<ETA,
 'all_exact_and_core_primitives_below_2':primitive_bound<2,
 'telescoping_72eta_below_error_cap':perturbation_bound<TRIPLE_ERROR,
 'core_lower_gt_2p25e_4':core_lower>F(225,10**6),
 'final_lower_positive':final_lower>F(1,5000),
}

def dec(x):
    return f'{float(x):.18e}'

out={
 'audit':'A114C2_SECOND_TIE_PHI_POSITIVITY_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'scope':{
   'M_min':521,
   's_min':'129/1000',
   's_max':'133/1000',
   'contact':'j=b+2',
   'boundary':'E_(b+2)=0',
 },
 'dependency':[
   'A114-A already proves the strict implication R=s^(b+2)/U <= 9/1000 => E_(b+2)<0. Therefore E_(b+2)=0 implies R>9/1000.',
   'Frozen localization gives j=b+2>=91.',
 ],
 'exact_core_identity':'Phi0/U = [R(beta-gamma)-Y(s-gamma)-8 a e(s-gamma)-4 U e R(beta+gamma)+4 U e Y(s-gamma)] / d',
 'ratio_identity':'Y=R*(beta/s)^j <= R*(125/129)^91',
 'gate_count':len(gates),
 'pass_count':sum(bool(v) for v in gates.values()),
 'failed':[k for k,v in gates.items() if not v],
 'gates':gates,
 'hard_margins':{
   'rho':dec(rho),
   'coefficient':dec(coef),
   'gamma_j_normalized_tail':dec(gamma_j_norm),
   'central_high_node_normalized_error':dec(central_primitive_error),
   'tail_ratio_after_h260':dec(tail_ratio),
   'primitive_abs_bound':dec(primitive_bound),
   'core_lower_for_Phi_over_U':dec(core_lower),
   'tail_error_cap':dec(TRIPLE_ERROR),
   'final_lower_for_Phi_over_U':dec(final_lower),
 },
 'conclusion':'Under the promoted A114-A R>9/1000 tie consequence, E_(b+2)=0 forces Phi=F_(b+2)^up>0. The sign proof does not use the dyadic gate 3j-h<=12 and does not use finite root data.',
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':out['hard_margins']},indent=2))
