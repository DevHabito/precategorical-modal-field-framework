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
PR=Path('/mnt/data/A109_H8D_PREREGISTRATION.json'); PRSHA='65f281a7fec2ab904af0afe3028a301b1ccf37a456b0374251569d5bfa9feb9d'
MAN=Path('/mnt/data/A109_H8D_EXECUTION_MANIFEST.json'); MANSHA='bd2919930e93e273264734ed549cfcf3b8c10f3d87944f2460a13ed5225b9793'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bisect(poly,a,b,sa,sb,steps=30):
    if not sa*sb<0: raise RuntimeError('no strict sign change')
    lo,hi=a,b;slo,shi=sa,sb
    for k in range(steps):
        m=(lo+hi)/2;sm=a103.sign(a103.ev(poly,m))
        if sm==0:return {'lower':str(m),'upper':str(m),'exact_rational_root':True,'steps':k+1,'signs':[0,0]}
        if sm==slo:lo,slo=m,sm
        else:hi,shi=m,sm
    return {'lower':str(lo),'upper':str(hi),'exact_rational_root':False,'steps':steps,'signs':[int(slo),int(shi)],'width':str(hi-lo)}
def setup(rank):
    if sha(PR)!=PRSHA or sha(MAN)!=MANSHA: raise RuntimeError('frozen file hash mismatch')
    pr=json.loads(PR.read_text()); pred=next(x for x in pr['frozen_predictions'] if x['canonical_rank']==rank)
    record=b1.source_records()[rank-1]
    if record['key']!=pred['source_key']: raise RuntimeError('source mismatch')
    M=int(record['key_fields']['maximum']);j=int(record['key_fields']['compressed_maximizer_contact'])
    w=sp.Rational(str(record['key_fields']['witness']));L=sp.Rational(str(record['segment_open_bounds'][0]));R=sp.Rational(str(record['segment_open_bounds'][1]))
    D,conds=amin.rank_one_gamma_plus_conditions(M,j);cm=dict(conds)
    return pr,pred,record,M,j,w,L,R,D,conds,cm
def get_root_and_target(pred,L,R,w,cm):
    target=None; root=None; signs=None; deriv_cert=None
    if pred['predicted_class']=='proper_strict_subcomponent':
        if len(pred['predicted_boundaries'])!=1:raise RuntimeError('unsupported boundaries')
        target=pred['predicted_boundaries'][0]['condition'];side=pred['predicted_boundaries'][0]['side'];N=cm[target]
        der=a103.derivative(a103.int_poly(N,1))
        signs={'L':int(a103.sign(a103.ev(N,L))),'witness':int(a103.sign(a103.ev(N,w))),'R':int(a103.sign(a103.ev(N,R)))}
        if side=='left':
            deriv_cert=a103.certify_positive(der,L,R,max_depth=28)
            if deriv_cert['pass'] and signs['L']<0 and signs['witness']>0:root=bisect(a103.int_poly(N,1),L,w,signs['L'],signs['witness'])
        elif side=='right':
            deriv_cert=a103.certify_positive({k:-v for k,v in der.items()},L,R,max_depth=28)
            if deriv_cert['pass'] and signs['witness']>0 and signs['R']<0:root=bisect(a103.int_poly(N,1),w,R,signs['witness'],signs['R'])
        else: raise RuntimeError('bad side')
    return target,root,signs,deriv_cert
def core(rank,outpath):
    pr,pred,record,M,j,w,L,R,D,conds,cm=setup(rank);t=time.time()
    Dcert=a103.certify_positive(a103.int_poly(D,1),L,R,max_depth=28)
    witness_nonpos=[name for name,p in conds if a103.sign(a103.ev(p,w))<=0]
    target,root,signs,deriv_cert=get_root_and_target(pred,L,R,w,cm)
    cert_names={name for name,_ in conds} if pred['predicted_class']=='full_segment_coverage' else {name for name,_ in conds if name!=target}
    certs=[];fail=[];unresolved=[];methods=Counter()
    for name,p in conds:
        if name not in cert_names:continue
        c=a103.certify_positive(a103.int_poly(p,1),L,R,max_depth=28);methods[c['method']]+=1;certs.append({'condition':name,**c})
        if not c['pass']:
            if c.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'}:fail.append({'condition':name,**c})
            else:unresolved.append({'condition':name,**c})
    pattern_fail=[]
    if pred['predicted_class']=='proper_strict_subcomponent' and (root is None or not deriv_cert or not deriv_cert.get('pass')):pattern_fail.append('target_pattern_failure')
    exact=[]
    if not Dcert['pass']:exact.append('D_certificate_failed')
    if witness_nonpos:exact.append('witness_not_strict')
    if fail:exact.append('exact_condition_failure')
    if pattern_fail:exact.append('target_pattern_failure')
    verdict='CORE_SUPPORT' if not exact and not unresolved else ('CORE_REFUTED_OR_FAILED' if exact else 'CORE_INCONCLUSIVE')
    out={'audit':'A109-H8D_SHARDED_CORE','rank':rank,'preregistration_sha256':sha(PR),'manifest_sha256':sha(MAN),'frozen_prediction':pred,'M':M,'j':j,'segment':[str(L),str(R)],'witness':str(w),'verdict':verdict,'denominator_certificate':Dcert,'witness_nonpositive_conditions':witness_nonpos,'target':target,'target_signs':signs,'target_derivative_certificate':deriv_cert,'unique_root_certificate':root,'certified_condition_count':len(certs),'certificate_methods':dict(methods),'exact_failures':fail,'unresolved':unresolved,'exact_verdict_failures':exact,'seconds':time.time()-t}
    Path(outpath).write_text(json.dumps(out,indent=2));print(json.dumps({'rank':rank,'verdict':verdict,'certified':len(certs),'fail':len(fail),'unresolved':len(unresolved),'seconds':out['seconds'],'output':outpath},indent=2))
def direct(rank,probe_index,outpath):
    pr,pred,record,M,j,w,L,R,D,conds,cm=setup(rank);target,root,signs,deriv=get_root_and_target(pred,L,R,w,cm)
    if pred['predicted_class']=='full_segment_coverage':
        probes=[('left_endpoint',L,True),('left_mid',(L+w)/2,True),('witness',w,True),('right_mid',(w+R)/2,True),('right_endpoint',R,True)]
    else:
        if root is None:raise RuntimeError('no root')
        a=sp.Rational(root['lower']);b=sp.Rational(root['upper']);side=pred['predicted_boundaries'][0]['side']
        if side=='left':
            outside=(L+a)/2 if L<a else L;inside=(b+w)/2 if b<w else w
            probes=[('outside_left',outside,False),('inside',inside,True),('witness',w,True),('right_mid',(w+R)/2,True)]
        else:
            inside=(w+a)/2 if w<a else w;outside=(b+R)/2 if b<R else R
            probes=[('left_mid',(L+w)/2,True),('witness',w,True),('inside',inside,True),('outside_right',outside,False)]
    if probe_index<0 or probe_index>=len(probes):raise RuntimeError('bad probe')
    label,s,strict_expected=probes[probe_index];t=time.time();den=a103.ev(D,s);dconds=amin.direct_gamma_plus_conditions(M,j,s);mm=[];nonpos=[]
    for name,val in dconds:
        if a103.ev(cm[name],s)!=den*val:mm.append(name)
        if val<=0:nonpos.append(name)
    positivity_failure=bool(strict_expected and nonpos);outside_failure=bool((not strict_expected) and target not in nonpos)
    verdict='DIRECT_SUPPORT' if not mm and not positivity_failure and not outside_failure else 'DIRECT_REFUTED_OR_FAILED'
    out={'audit':'A109-H8D_SHARDED_DIRECT','rank':rank,'probe_index':probe_index,'probe_label':label,'probe':str(s),'strict_expected':strict_expected,'target':target,'verdict':verdict,'comparison_count':len(dconds),'mismatches':mm,'nonpositive_conditions':nonpos,'positivity_failure':positivity_failure,'outside_failure':outside_failure,'seconds':time.time()-t,'preregistration_sha256':sha(PR),'manifest_sha256':sha(MAN)}
    Path(outpath).write_text(json.dumps(out,indent=2));print(json.dumps({'rank':rank,'probe':label,'verdict':verdict,'comparisons':len(dconds),'mismatches':len(mm),'nonpositive_count':len(nonpos),'seconds':out['seconds'],'output':outpath},indent=2))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rank',type=int,required=True,choices=[239,240]);ap.add_argument('--mode',choices=['core','direct'],required=True);ap.add_argument('--probe-index',type=int,default=-1);ap.add_argument('--out',required=True);a=ap.parse_args()
    if a.mode=='core':core(a.rank,a.out)
    else:direct(a.rank,a.probe_index,a.out)
if __name__=='__main__':main()
