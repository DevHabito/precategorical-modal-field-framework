#!/usr/bin/env python3
from __future__ import annotations
import sys,json,hashlib,time,argparse
from pathlib import Path
from collections import Counter
import sympy as sp
REPO=Path('/mnt/data/a107_work/repo');sys.path.insert(0,str(REPO/'audits'))
import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1
PR=Path('/mnt/data/A109_H6D_PREREGISTRATION.json'); EXPECTED='ac533ef4fc567a7da804a38ed27ec9e67266edce359bbc227934799fb3b7ff79'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def bisect(poly,a,b,sa,sb,steps=30):
    if not (sa*sb<0): raise RuntimeError('no strict sign change')
    lo,hi=a,b;slo,shi=sa,sb
    for k in range(steps):
        m=(lo+hi)/2; sm=a103.sign(a103.ev(poly,m))
        if sm==0:
            return {'lower':str(m),'upper':str(m),'exact_rational_root':True,'steps':k+1,'signs':[0,0]}
        if sm==slo: lo,slo=m,sm
        else: hi,shi=m,sm
    return {'lower':str(lo),'upper':str(hi),'exact_rational_root':False,'steps':steps,'signs':[int(slo),int(shi)],'width':str(hi-lo)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    if sha(PR)!=EXPECTED: raise RuntimeError('prereg mismatch')
    pr=json.loads(PR.read_text()); allowed=set(pr['ranks'])
    if args.rank not in allowed: raise RuntimeError('rank not preregistered')
    pred=next(x for x in pr['frozen_predictions'] if x['canonical_rank']==args.rank)
    record=b1.source_records()[args.rank-1]
    if record['key']!=pred['source_key']: raise RuntimeError('source mismatch')
    M=int(record['key_fields']['maximum']); j=int(record['key_fields']['compressed_maximizer_contact'])
    w=sp.Rational(str(record['key_fields']['witness'])); L=sp.Rational(str(record['segment_open_bounds'][0])); R=sp.Rational(str(record['segment_open_bounds'][1]))
    t=time.time(); D,conds=amin.rank_one_gamma_plus_conditions(M,j); cm=dict(conds)
    # Basic applicability and denominator.
    Dpoly=a103.int_poly(D,1); Dcert=a103.certify_positive(Dpoly,L,R,max_depth=28)
    witness_nonpos=[name for name,p in conds if a103.sign(a103.ev(p,w))<=0]
    failures=[]; unresolved=[]; methods=Counter(); certs=[]; root=None; target=None; target_deriv_cert=None; target_signs=None
    expected=pred['predicted_class']; boundaries=pred['predicted_boundaries']
    if expected=='full_segment_coverage':
        cert_names={name for name,_ in conds}
    elif expected=='proper_strict_subcomponent' and len(boundaries)==1:
        target=boundaries[0]['condition']; side=boundaries[0]['side']; cert_names={name for name,_ in conds if name!=target}
        N=cm[target]; der=a103.derivative(a103.int_poly(N,1))
        if side=='left':
            target_deriv_cert=a103.certify_positive(der,L,R,max_depth=28)
            target_signs={'L':int(a103.sign(a103.ev(N,L))),'witness':int(a103.sign(a103.ev(N,w))),'R':int(a103.sign(a103.ev(N,R)))}
            if target_deriv_cert['pass'] and target_signs['L']<0 and target_signs['witness']>0:
                root=bisect(a103.int_poly(N,1),L,w,target_signs['L'],target_signs['witness'])
            else: failures.append({'kind':'target_left_pattern_failure','derivative_certificate':target_deriv_cert,'signs':target_signs})
        elif side=='right':
            negder={k:-v for k,v in der.items()}
            target_deriv_cert=a103.certify_positive(negder,L,R,max_depth=28)
            target_signs={'L':int(a103.sign(a103.ev(N,L))),'witness':int(a103.sign(a103.ev(N,w))),'R':int(a103.sign(a103.ev(N,R)))}
            if target_deriv_cert['pass'] and target_signs['witness']>0 and target_signs['R']<0:
                root=bisect(a103.int_poly(N,1),w,R,target_signs['witness'],target_signs['R'])
            else: failures.append({'kind':'target_right_pattern_failure','derivative_certificate':target_deriv_cert,'signs':target_signs})
        else: raise RuntimeError('unsupported side')
    else:
        raise RuntimeError('diagnostic only supports frozen full or single-boundary predictions')
    # Exact positivity of every required non-target (or all, for full) KKT numerator on complete source segment.
    for name,p in conds:
        if name not in cert_names: continue
        cert=a103.certify_positive(a103.int_poly(p,1),L,R,max_depth=28); methods[cert['method']]+=1
        certs.append({'condition':name,**cert})
        if not cert['pass']:
            row={'condition':name,**cert}
            if cert.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'}: failures.append(row)
            else: unresolved.append(row)
    # Direct symbolic-vs-matrix checks.
    probes=[]
    if expected=='full_segment_coverage':
        probes=[('left_endpoint',L,True),('left_mid',(L+w)/2,True),('witness',w,True),('right_mid',(w+R)/2,True),('right_endpoint',R,True)]
    else:
        assert root is not None
        a=sp.Rational(root['lower']); b=sp.Rational(root['upper']); side=boundaries[0]['side']
        if side=='left':
            outside=(L+a)/2 if L<a else L
            inside=(b+w)/2 if b<w else w
            probes=[('outside_left',outside,False),('inside',inside,True),('witness',w,True),('right_mid',(w+R)/2,True)]
        else:
            inside=(w+a)/2 if w<a else w
            outside=(b+R)/2 if b<R else R
            probes=[('left_mid',(L+w)/2,True),('witness',w,True),('inside',inside,True),('outside_right',outside,False)]
    direct=[]; dmismatch=0; positivity_fail=[]; outside_fail=[]
    for label,s,strict_expected in probes:
        den=a103.ev(D,s); dconds=amin.direct_gamma_plus_conditions(M,j,s); mm=[]; nonpos=[]
        for name,val in dconds:
            if a103.ev(cm[name],s)!=den*val: mm.append(name)
            if val<=0: nonpos.append(name)
        dmismatch+=len(mm)
        if strict_expected and nonpos: positivity_fail.append({'label':label,'nonpositive':nonpos})
        if (not strict_expected) and target not in nonpos: outside_fail.append({'label':label,'nonpositive':nonpos,'expected_target':target})
        direct.append({'label':label,'probe':str(s),'comparison_count':len(dconds),'mismatches':mm,'nonpositive_conditions':nonpos})
    exact=[]
    if not Dcert['pass']: exact.append('D_certificate_failed')
    if witness_nonpos: exact.append('witness_not_strict')
    if failures: exact.append('exact_condition_failure')
    if dmismatch: exact.append('direct_symbolic_mismatch')
    if positivity_fail: exact.append('direct_inside_positivity_failure')
    if outside_fail: exact.append('direct_outside_target_failure')
    if exact: verdict='REFUTED_OR_FAILED_A109_H6D_CERTIFICATE'
    elif unresolved: verdict='INCONCLUSIVE_A109_H6D_CERTIFICATE'
    else: verdict='RESOLVED_SUPPORT_A109_H6D_CERTIFICATE'
    out={'audit':pr['audit'],'preregistration_sha256':sha(PR),'rank':args.rank,'source_key':record['key'],'M':M,'j':j,'segment':[str(L),str(R)],'witness':str(w),
         'frozen_prediction':pred,'verdict':verdict,'denominator_certificate':Dcert,'witness_nonpositive_conditions':witness_nonpos,
         'target':target,'target_derivative_certificate':target_deriv_cert,'target_signs':target_signs,'unique_root_certificate':root,
         'certified_condition_count':len(certs),'certificate_methods':dict(methods),'exact_failure_count':len(failures),'unresolved_count':len(unresolved),
         'exact_failures_detail':failures,'unresolved_detail':unresolved,'direct_checks':direct,'direct_comparison_count':sum(x['comparison_count'] for x in direct),'direct_mismatch_count':dmismatch,
         'direct_positivity_failures':positivity_fail,'direct_outside_failures':outside_fail,'exact_verdict_failures':exact,'seconds':time.time()-t,'scope':pr['scope']}
    Path(args.out).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'rank':args.rank,'verdict':verdict,'certified_conditions':len(certs),'exact_failures':len(failures),'unresolved':len(unresolved),'direct_comparisons':out['direct_comparison_count'],'direct_mismatches':dmismatch,'seconds':out['seconds'],'output':args.out},indent=2))
if __name__=='__main__': main()
