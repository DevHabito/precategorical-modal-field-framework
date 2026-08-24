#!/usr/bin/env python3
from __future__ import annotations
import sys,json,hashlib,time,argparse
from pathlib import Path
from collections import Counter
import sympy as sp
REPO=Path('/mnt/data/a107_work/repo'); sys.path.insert(0,str(REPO/'audits'))
import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1
PR=Path('/mnt/data/A109_H13D_PREREGISTRATION.json')
PRSHA='fb15ea204528f2c676ae616c601426a046f1e5978ccf5eaa9a76efdd9ba561e7'
MAN=Path('/mnt/data/A109_H13D_SHARDED_EXECUTION_MANIFEST.json')
MANSHA='1a69e16bd3a9554f0cc1419a2c74cd7944c41a571e6aaf57c743cce4914c197d'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bisect(poly,a,b,sa,sb,steps=30):
    if not sa*sb<0: raise RuntimeError('no strict sign change')
    lo,hi=a,b;slo,shi=sa,sb
    for k in range(steps):
        m=(lo+hi)/2;sm=a103.sign(a103.ev(poly,m))
        if sm==0:return {'lower':str(m),'upper':str(m),'exact_rational_root':True,'steps':k+1,'signs':[0,0]}
        if sm==slo: lo,slo=m,sm
        else: hi,shi=m,sm
    return {'lower':str(lo),'upper':str(hi),'exact_rational_root':False,'steps':steps,'signs':[int(slo),int(shi)],'width':str(hi-lo)}
def setup():
    if sha(PR)!=PRSHA or sha(MAN)!=MANSHA: raise RuntimeError('frozen hash mismatch')
    pr=json.loads(PR.read_text()); man=json.loads(MAN.read_text()); rank=319
    pred=pr['frozen_predictions'][0]; record=b1.source_records()[rank-1]
    if record['key']!=pred['source_key']: raise RuntimeError('source mismatch')
    M=int(record['key_fields']['maximum']);j=int(record['key_fields']['compressed_maximizer_contact'])
    w=sp.Rational(str(record['key_fields']['witness']));L=sp.Rational(str(record['segment_open_bounds'][0]));R=sp.Rational(str(record['segment_open_bounds'][1]))
    D,conds=amin.rank_one_gamma_plus_conditions(M,j); cm=dict(conds)
    if len(conds)!=man['condition_count_from_frozen_architecture']: raise RuntimeError('condition count mismatch')
    return pr,man,pred,record,M,j,w,L,R,D,conds,cm
def target_data(pred,L,R,w,cm):
    target=pred['predicted_boundaries'][0]['condition']; side=pred['predicted_boundaries'][0]['side']; N=cm[target]
    der=a103.derivative(a103.int_poly(N,1)); signs={'L':int(a103.sign(a103.ev(N,L))),'witness':int(a103.sign(a103.ev(N,w))),'R':int(a103.sign(a103.ev(N,R)))}
    if side=='left':
        dc=a103.certify_positive(der,L,R,max_depth=28); root=bisect(a103.int_poly(N,1),L,w,signs['L'],signs['witness']) if dc['pass'] and signs['L']<0 and signs['witness']>0 else None
    elif side=='right':
        dc=a103.certify_positive({k:-v for k,v in der.items()},L,R,max_depth=28); root=bisect(a103.int_poly(N,1),w,R,signs['witness'],signs['R']) if dc['pass'] and signs['witness']>0 and signs['R']<0 else None
    else: raise RuntimeError('unsupported side')
    return target,side,signs,dc,root
def base(outpath):
    pr,man,pred,record,M,j,w,L,R,D,conds,cm=setup();t=time.time(); target,side,signs,dc,root=target_data(pred,L,R,w,cm)
    Dcert=a103.certify_positive(a103.int_poly(D,1),L,R,max_depth=28); witness_nonpos=[n for n,p in conds if a103.sign(a103.ev(p,w))<=0]
    fails=[]
    if not Dcert['pass']: fails.append('D_certificate_failed')
    if witness_nonpos: fails.append('witness_not_strict')
    if not dc.get('pass') or root is None: fails.append('target_pattern_failed')
    verdict='BASE_SUPPORT' if not fails else 'BASE_REFUTED_OR_FAILED'
    out={'audit':'A109-H13D_SHARDED_BASE','rank':319,'preregistration_sha256':sha(PR),'manifest_sha256':sha(MAN),'verdict':verdict,'M':M,'j':j,'segment':[str(L),str(R)],'witness':str(w),'frozen_prediction':pred,'denominator_certificate':Dcert,'witness_nonpositive_conditions':witness_nonpos,'target':target,'target_side':side,'target_signs':signs,'target_derivative_certificate':dc,'unique_root_certificate':root,'failures':fails,'seconds':time.time()-t}
    Path(outpath).write_text(json.dumps(out,indent=2)); print(json.dumps({'verdict':verdict,'failures':fails,'seconds':out['seconds'],'output':outpath},indent=2))
def cert(block,outpath):
    pr,man,pred,record,M,j,w,L,R,D,conds,cm=setup();t=time.time(); target=man['frozen_target_condition']; blocks=[tuple(x) for x in man['condition_blocks_inclusive']]
    if block<0 or block>=len(blocks): raise RuntimeError('bad block')
    lo,hi=blocks[block]; methods=Counter(); failures=[]; unresolved=[]; checked=0; skipped=[]
    for idx in range(lo,hi+1):
        name,p=conds[idx]
        if name==target:
            skipped.append({'index':idx,'condition':name,'reason':'frozen_target'}); continue
        checked+=1; c=a103.certify_positive(a103.int_poly(p,1),L,R,max_depth=28); methods[c['method']]+=1
        if not c['pass']:
            row={'index':idx,'condition':name,**c}
            if c.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'}: failures.append(row)
            else: unresolved.append(row)
    verdict='CERT_SUPPORT' if not failures and not unresolved else ('CERT_REFUTED_OR_FAILED' if failures else 'CERT_INCONCLUSIVE')
    out={'audit':'A109-H13D_SHARDED_CERT_BLOCK','rank':319,'block_index':block,'condition_index_range':[lo,hi],'preregistration_sha256':sha(PR),'manifest_sha256':sha(MAN),'verdict':verdict,'checked_condition_count':checked,'skipped':skipped,'certificate_methods':dict(methods),'exact_failure_count':len(failures),'unresolved_count':len(unresolved),'failures':failures,'unresolved':unresolved,'seconds':time.time()-t}
    Path(outpath).write_text(json.dumps(out,indent=2)); print(json.dumps({'block':block,'range':[lo,hi],'verdict':verdict,'checked':checked,'failures':len(failures),'unresolved':len(unresolved),'seconds':out['seconds'],'output':outpath},indent=2))
def direct(probe,outpath):
    pr,man,pred,record,M,j,w,L,R,D,conds,cm=setup(); target,side,signs,dc,root=target_data(pred,L,R,w,cm)
    if root is None: raise RuntimeError('no target root')
    a=sp.Rational(root['lower']); b=sp.Rational(root['upper'])
    if side=='left':
        probes=[('outside_left',(L+a)/2 if L<a else L,False),('inside',(b+w)/2 if b<w else w,True),('witness',w,True),('right_mid',(w+R)/2,True)]
    else:
        probes=[('left_mid',(L+w)/2,True),('witness',w,True),('inside',(w+a)/2 if w<a else w,True),('outside_right',(b+R)/2 if b<R else R,False)]
    if probe not in man['direct_probe_indices']: raise RuntimeError('unfrozen probe')
    label,s,strict_expected=probes[probe]; t=time.time()
    # Exact sparse-polynomial evaluation with one shared rational power table. This is algebraically identical
    # to a103.ev but avoids repeated exponentiation at large rational checkpoint denominators.
    maxdeg=max([max(D.keys(),default=0)]+[max(poly.keys(),default=0) for poly in cm.values()])
    powers=[sp.Integer(1)]
    for _ in range(maxdeg): powers.append(powers[-1]*s)
    def fast_ev(poly): return sum(coeff*powers[degree] for degree,coeff in poly.items())
    den=fast_ev(D); dconds=amin.direct_gamma_plus_conditions(M,j,s); mm=[]; nonpos=[]
    for name,val in dconds:
        if fast_ev(cm[name])!=den*val: mm.append(name)
        if val<=0: nonpos.append(name)
    pf=bool(strict_expected and nonpos); of=bool((not strict_expected) and target not in nonpos); verdict='DIRECT_SUPPORT' if not mm and not pf and not of else 'DIRECT_REFUTED_OR_FAILED'
    out={'audit':'A109-H13D_SHARDED_DIRECT','rank':319,'probe_index':probe,'probe_label':label,'probe':str(s),'strict_expected':strict_expected,'target':target,'preregistration_sha256':sha(PR),'manifest_sha256':sha(MAN),'verdict':verdict,'comparison_count':len(dconds),'mismatches':mm,'nonpositive_conditions':nonpos,'positivity_failure':pf,'outside_failure':of,'seconds':time.time()-t}
    Path(outpath).write_text(json.dumps(out,indent=2)); print(json.dumps({'probe':probe,'label':label,'verdict':verdict,'comparisons':len(dconds),'mismatches':len(mm),'nonpositive':nonpos,'seconds':out['seconds'],'output':outpath},indent=2))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['base','cert','direct'],required=True); ap.add_argument('--block',type=int,default=-1); ap.add_argument('--probe',type=int,default=-1); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.mode=='base': base(a.out)
    elif a.mode=='cert': cert(a.block,a.out)
    else: direct(a.probe,a.out)
if __name__=='__main__': main()
