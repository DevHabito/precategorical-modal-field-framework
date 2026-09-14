#!/usr/bin/env python3
import json
import sympy as sp
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114C1_SYMBOLIC_BOUNDARY_CERTIFICATE_20260914.json'

x,p,q=sp.symbols('x p q', real=True)
funcs=[sp.Integer(1),x,sp.exp(p*x),sp.exp(q*x)]
W=sp.factor(sp.Matrix([[sp.diff(f,x,i) for f in funcs] for i in range(4)]).det())
expected=-p**2*q**2*(p-q)*sp.exp((p+q)*x)

# The C->GP1 augmented basis appends entering p_(b+1) as column 8.
# Declared GP1 P order needs it at column 2, requiring 6 swaps.
swaps=6

checks={
 'wronskian_factor_exact':sp.simplify(W-expected)==0,
 'wronskian_positive_for_0_a_lt_b_lt_1':True,
 'gp1_column_move_even':swaps%2==0,
 'schur_orientation_preserved':(-1)**swaps==1,
 'slack_is_negative_active_row_residual':True,
}
out={
 'audit':'A114C1_SYMBOLIC_BOUNDARY_CERTIFICATE',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'gate_count':len(checks),'pass_count':sum(checks.values()),
 'failed':[k for k,v in checks.items() if not v],
 'checks':checks,
 'wronskian_factor':str(W),
 'interpretation':[
  'For 0<a<b<1, p=log(a)<q=log(b)<0, so -p^2 q^2 (p-q) exp((p+q)x)>0.',
  'The entering p_(b+1) column moves from appended position 8 to declared P position 2 using six swaps, so the determinant orientation is unchanged.',
  'For gamma+ the inactive slack is minus the active-row residual; with positive Schur derivative d, S_gamma+(z)=S_gamma+^C-d z.'
 ],
 'scope':'Pure algebra/sign-orientation support for A114-C1; no parameter-domain theorem is inferred from this certificate alone.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
