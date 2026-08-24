#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, sys, time
from pathlib import Path
from collections import Counter
import sympy as sp

REPO=Path('/mnt/data/a107_work/repo')
sys.path.insert(0,str(REPO/'audits'))
import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1

PREREG=Path('/mnt/data/A108_P4_PREREGISTRATION.json')
EXPECTED='4dde3688f9127aef475a7f81f4a5c0a18ceb9f0375aff7172ec38a8af3719a98'
OUT=Path('/mnt/data/A108_P4C_RESULT.json')

def sha(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def peval(poly,x): return a103.ev(poly,x)

def target_certificate(record):
    M=int(record['key_fields']['maximum']); j=int(record['key_fields']['compressed_maximizer_contact'])
    L=sp.Rational(str(record['segment_open_bounds'][0])); R=sp.Rational(str(record['segment_open_bounds'][1])); w=sp.Rational(str(record['key_fields']['witness']))
    D,conds=amin.rank_one_gamma_plus_conditions(M,j)
    cmap=dict(conds); target=f'basic_p_{j+1}'; N=cmap[target]
    Dcert=a103.certify_positive(a103.int_poly(D,1),L,R,max_depth=28)
    dN=a103.derivative(a103.int_poly(N,1)); dcert=a103.certify_positive(dN,L,R,max_depth=28)
    signs={'N_lower':a103.sign(peval(N,L)),'N_witness':a103.sign(peval(N,w)),'N_upper':a103.sign(peval(N,R)),
           'D_lower':a103.sign(peval(D,L)),'D_witness':a103.sign(peval(D,w)),'D_upper':a103.sign(peval(D,R))}
    non=[]; failures=[]; unresolved=[]; methods=Counter()
    for name,p in conds:
        if name==target: continue
        cert=a103.certify_positive(a103.int_poly(p,1),L,R,max_depth=28)
        methods[cert['method']]+=1
        row={'condition':name,**cert}
        non.append(row)
        if not cert['pass']:
            if cert.get('method')=='internal_nonpositive_witness' or cert.get('method')=='endpoint_nonpositive': failures.append(row)
            else: unresolved.append(row)
    if not Dcert['pass']:
        (failures if Dcert.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'} else unresolved).append({'condition':'common_denominator',**Dcert})
    if not dcert['pass']:
        (failures if dcert.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'} else unresolved).append({'condition':'derivative_'+target,**dcert})
    classif='NO_CLASSIFICATION'
    root=None
    if not failures and not unresolved and Dcert['pass'] and dcert['pass'] and signs['N_witness']>0:
        if signs['N_lower']<0:
            classif='proper_strict_subcomponent'
            root=a103.isolate_sign_change(a103.int_poly(N,1),L,w)
        elif signs['N_lower']>0:
            classif='full_segment_coverage'
    return {'target_condition':target,'exact_signs':signs,'D_certificate':Dcert,'target_derivative_certificate':dcert,
            'non_target_condition_count':len(non),'non_target_certificate_methods':dict(methods),
            'non_target_failures':failures,'non_target_unresolved':unresolved,'certificate_class':classif,'target_root_if_partial':root}

def main():
    if sha(PREREG)!=EXPECTED: raise RuntimeError('prereg hash mismatch')
    pp=json.loads(PREREG.read_text())
    parent=json.loads(Path(pp['parent_preregistration']['path']).read_text())
    parent_preds={int(x['canonical_rank']):x for x in parent['holdout_predictions']}
    src=b1.source_records(); assert len(src)==922
    batch=src[81:89]
    out=[]
    orig=a105.build_integer_polynomials
    for rank,record in enumerate(batch,start=82):
        t=time.time()
        cert=target_certificate(record)
        frozen=parent_preds[rank]
        try:
            a105.build_integer_polynomials=amin.build_integer_polynomials
            atlas=a105.analyze_record(record)
        finally:
            a105.build_integer_polynomials=orig
        atlas['architecture_class']='legacy_three_band_gamma_plus'
        reg=b1.direct_checkpoint_regression(record,atlas) if 'strict_component' in atlas else None
        selected=b1.semantic_selected_boundaries(atlas)
        expected_boundary=f'basic_p_{int(record["key_fields"]["compressed_maximizer_contact"])+1}'
        if cert['certificate_class']=='proper_strict_subcomponent':
            boundary_match=(len(selected)==1 and selected[0]=={'side':'left','condition':expected_boundary})
        elif cert['certificate_class']=='full_segment_coverage': boundary_match=(len(selected)==0)
        else: boundary_match=None
        out.append({'canonical_rank':rank,'source_key':record['key'],'maximum':int(record['key_fields']['maximum']),
                    'contact_j':int(record['key_fields']['compressed_maximizer_contact']),'witness':str(record['key_fields']['witness']),
                    'segment_open_bounds':record['segment_open_bounds'],'frozen_parent_prediction':frozen['predicted_class'],
                    'sufficient_certificate':cert,'atlas_class':atlas.get('status'),'selected_boundaries':selected,
                    'certificate_matches_parent':cert['certificate_class']==frozen['predicted_class'],
                    'certificate_matches_atlas':cert['certificate_class']==atlas.get('status'),
                    'boundary_match':boundary_match,
                    'direct_regression_summary':None if reg is None else {k:reg[k] for k in ['checkpoint_count','comparison_count','mismatch_count','positivity_failure_count','outside_sign_failure_count']},
                    'seconds':time.time()-t})
    exact_failures=[]; inconclusive=[]
    for x in out:
        c=x['sufficient_certificate']
        if c['non_target_failures']: exact_failures.append({'rank':x['canonical_rank'],'type':'non_target_nonpositive','details':c['non_target_failures']})
        if c['non_target_unresolved']: inconclusive.append({'rank':x['canonical_rank'],'type':'non_target_unresolved','details':c['non_target_unresolved']})
        if not c['D_certificate']['pass'] or not c['target_derivative_certificate']['pass']: inconclusive.append({'rank':x['canonical_rank'],'type':'target_or_den_certificate'})
        if not x['certificate_matches_parent']: exact_failures.append({'rank':x['canonical_rank'],'type':'parent_prediction_mismatch'})
        if not x['certificate_matches_atlas']: exact_failures.append({'rank':x['canonical_rank'],'type':'atlas_mismatch'})
        if x['boundary_match'] is False: exact_failures.append({'rank':x['canonical_rank'],'type':'boundary_mismatch','observed':x['selected_boundaries']})
        rr=x['direct_regression_summary']
        if rr and (rr['mismatch_count'] or rr['positivity_failure_count'] or rr['outside_sign_failure_count']): exact_failures.append({'rank':x['canonical_rank'],'type':'direct_regression_failure','details':rr})
    if exact_failures: verdict='REFUTED_A108_P4C'
    elif inconclusive: verdict='INCONCLUSIVE_A108_P4C'
    else: verdict='PASS_SUFFICIENT_CERTIFICATE_HOLDOUT'
    result={'audit':'A108-P4C_EXECUTION_SHARD','preregistration_sha256':sha(PREREG),'verdict':verdict,
            'summary':{'record_count':len(out),'certificate_class_counts':dict(Counter(x['sufficient_certificate']['certificate_class'] for x in out)),
                       'atlas_class_counts':dict(Counter(x['atlas_class'] for x in out)),
                       'certificate_parent_match_count':sum(x['certificate_matches_parent'] for x in out),
                       'certificate_atlas_match_count':sum(x['certificate_matches_atlas'] for x in out),
                       'boundary_match_count':sum(x['boundary_match'] is True for x in out),
                       'partial_count':sum(x['atlas_class']=='proper_strict_subcomponent' for x in out),
                       'direct_comparisons':sum((x['direct_regression_summary'] or {}).get('comparison_count',0) for x in out),
                       'direct_mismatches':sum((x['direct_regression_summary'] or {}).get('mismatch_count',0) for x in out),
                       'non_target_failure_count':sum(len(x['sufficient_certificate']['non_target_failures']) for x in out),
                       'non_target_unresolved_count':sum(len(x['sufficient_certificate']['non_target_unresolved']) for x in out)},
            'exact_failures':exact_failures,'inconclusive_items':inconclusive,'records':out,
            'scope':{'claim':'deterministic execution shard of frozen P4 ranks 82..89','nonclaims':pp['nonclaims']}}
    OUT.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'verdict':verdict,**result['summary'],'output':str(OUT)},indent=2))
if __name__=='__main__': main()
