#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A115A_UNIFORM_H_GAP_CERTIFICATE_20260914.json'

H0=260
TAU_LO=F(49,100); TAU_HI=F(51,100)
S_LO=F(129,1000); S_HI=F(133,1000)
BETA_LO=F(31,250); BETA_HI=F(63,500)
EBAR_EVEN=F(1,1875); EBAR_ODD=F(1,2500)

U0=TAU_HI**H0
hU_decay_ratio=TAU_HI*F(H0+1,H0)
relative_den_correction=U0*(F(H0)*(1/TAU_LO-1)+1)
r=S_HI/TAU_LO
tail=3*r**H0
gap=S_LO-BETA_HI

even_lower=gap/TAU_HI-4*EBAR_EVEN-tail
odd_lower=gap*(1+TAU_HI)/(2*TAU_HI)-4*EBAR_ODD-tail

gates={
 'parameter_ordering':0<BETA_LO<=BETA_HI<S_LO<=S_HI<TAU_LO<=TAU_HI<1,
 'source_beta_gap_at_least_0p003':gap>=F(3,1000),
 'hU_sequence_decreases_after_h260':hU_decay_ratio<1,
 'relative_denominator_correction_lt_half':relative_den_correction<F(1,2),
 'source_target_ratio_lt_0p272':r<F(272,1000),
 'normalized_high_node_tail_lt_1e_100':tail<F(1,10**100),
 'even_normalized_gap_gt_0p0037':even_lower>F(37,10000),
 'odd_normalized_gap_gt_0p0028':odd_lower>F(28,10000),
}

def dec(x): return f'{float(x):.18e}'

out={
 'audit':'A115A_UNIFORM_H_GAP_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'scope':{
  'M_min':521,
  'beta':['31/250','63/500'],
  's':['129/1000','133/1000'],
  'tau':['49/100','51/100'],
  'epsilon':'tau^h/(1875 even; 2500 odd)'
 },
 'gate_count':len(gates),
 'pass_count':sum(bool(v) for v in gates.values()),
 'failed':[k for k,v in gates.items() if not v],
 'gates':gates,
 'hard_margins':{
  'minimum_s_minus_beta':dec(gap),
  'hU_decay_ratio_at_h260':dec(hU_decay_ratio),
  'relative_denominator_correction':dec(relative_den_correction),
  'normalized_high_node_tail_bound':dec(tail),
  'even_lower_bound':dec(even_lower),
  'odd_lower_bound':dec(odd_lower),
 },
 'conclusion':'Uniformly on the local A115 box, (H_s-H_beta)/tau^h > 0.0028. This is a supporting analytic lemma only, not a generalized A113 theorem.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':out['hard_margins']},indent=2))
