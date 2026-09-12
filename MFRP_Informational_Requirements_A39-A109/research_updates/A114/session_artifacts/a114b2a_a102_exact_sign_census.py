#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2] if len(HERE.parents) >= 3 else HERE
CANDIDATES = [
    REPO_ROOT / 'results' / 'a102_complete_rational_witness_lift_atlas_catalogue.json',
    HERE / 'a102_complete_rational_witness_lift_atlas_catalogue.json',
]
CATALOGUE = next((p for p in CANDIDATES if p.exists()), CANDIDATES[0])
OUT = HERE / 'A114B2A_A102_EXACT_SIGN_CENSUS_20260912.json'


def Q(x): return sp.Rational(1, 2**x)
def eps(M): return sp.Rational(1, (1875 if M % 2 == 0 else 2500) * 2**(M//2))
def sg(x): return 1 if x > 0 else -1 if x < 0 else 0


def upper_gamma_boundary_value(M: int, s: sp.Rational, j: int) -> sp.Expr:
    h = M//2; e = eps(M); mean = sp.Rational(M,2)
    qs = [1,h,h+1]
    AQ = sp.Matrix([[1,1,1], qs, [Q(x) for x in qs]])
    slope = AQ.inv(method='DM') * sp.Matrix([1,mean,0])
    const = AQ.inv(method='DM') * sp.Matrix([0,0,1])
    def qc(base): return sp.cancel(sum(const[i]*base**qs[i] for i in range(3)))
    def qd(base): return sp.cancel(sum(slope[i]*base**qs[i] for i in range(3)))
    def br(base,k): return sp.cancel(base**k - sp.Rational(M-k,M) - sp.Rational(k,M)*base**M)
    def ar(base): return sp.cancel((1+base**M)/2)
    beta = sp.Rational(1,8); gamma = sp.Rational(1,16)
    Hb = sp.cancel(ar(beta)-qd(beta)+2*e)
    Hg = sp.cancel(ar(gamma)-qd(gamma)-2*e)
    Hs = sp.cancel(ar(s)-qd(s)-2*e)
    G = sp.Matrix([
        [br(beta,j), br(beta,j+1), Hb],
        [br(gamma,j), br(gamma,j+1), Hg],
        [br(s,j), br(s,j+1), Hs],
    ])
    rhs = sp.Matrix([qc(beta), qc(gamma), qc(s)])
    G1 = G.copy(); G1[:,1] = rhs
    return sp.factor(G1.det(method='domain-ge'))  # F_j^up


data = json.loads(CATALOGUE.read_text(encoding='utf-8'))
records = [r for r in data['records'] if r['key_fields']['compressed_phase'] == 'unique_b_plus_2']
by_class = Counter()
by_sign = Counter()
class_by_sign = defaultdict(Counter)
examples = {'positive': None, 'negative': None}
for r in records:
    kf = r['key_fields']; res = r['resolution']
    M = int(kf['maximum']); b = int(kf['base_contact']); s = sp.Rational(kf['witness'])
    phi = upper_gamma_boundary_value(M,s,b+2)
    sign = sg(phi)
    cls = res['detailed_class']
    by_class[cls] += 1
    by_sign[str(sign)] += 1
    class_by_sign[cls][str(sign)] += 1
    key = 'positive' if sign > 0 else 'negative' if sign < 0 else 'zero'
    if key in examples and examples[key] is None:
        examples[key] = {'M':M,'s':str(s),'b':b,'class':cls,'Phi_sign':sign}

expected_classes = {
    'legacy_three_band_gamma_plus': 404,
    'legacy_three_band_gamma_minus': 14,
    'legacy_two_band_compressed': 14,
    'endpoint_released_gamma_inactive': 5,
    'q0q1_gamma_active': 4,
    'q0q1_gamma_inactive': 3,
}

out = {
    'audit': 'A114B2A_A102_EXACT_SIGN_CENSUS',
    'role': 'finite historical consistency check only; not part of the all-M proof',
    'source_catalogue': 'results/a102_complete_rational_witness_lift_atlas_catalogue.json',
    'unique_b_plus_2_record_count': len(records),
    'Phi_definition': 'Phi=F_(b+2)^up evaluated exactly at each rational A102 witness',
    'Phi_sign_counts': dict(by_sign),
    'detailed_class_counts': dict(by_class),
    'detailed_class_by_Phi_sign': {k:dict(v) for k,v in sorted(class_by_sign.items())},
    'examples': examples,
}
out['gates'] = {
    'exact_record_count_444': len(records) == 444,
    'no_zero_Phi_witnesses': by_sign.get('0',0) == 0,
    'positive_Phi_count_404': by_sign.get('1',0) == 404,
    'negative_Phi_count_40': by_sign.get('-1',0) == 40,
    'class_counts_exact': dict(by_class) == expected_classes,
    'all_positive_Phi_are_gamma_plus': class_by_sign['legacy_three_band_gamma_plus'].get('1',0) == 404 and sum(v.get('1',0) for k,v in class_by_sign.items() if k != 'legacy_three_band_gamma_plus') == 0,
    'no_negative_Phi_is_gamma_plus': class_by_sign['legacy_three_band_gamma_plus'].get('-1',0) == 0,
}
out['verdict'] = 'PASS' if all(out['gates'].values()) else 'FAIL'
out['claim_limits'] = [
    'A102 is a finite rational witness atlas through M=520; this census does not establish an all-M theorem.',
    'The all-M Phi>0 theorem is analytic and does not depend on these 444 records.',
    'The negative-Phi side contains multiple architecture classes and remains open as a global tail classification problem.',
]
OUT.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps({'verdict':out['verdict'],'sign_counts':out['Phi_sign_counts'],'class_counts':out['detailed_class_counts'],'gates':out['gates']}, indent=2))
