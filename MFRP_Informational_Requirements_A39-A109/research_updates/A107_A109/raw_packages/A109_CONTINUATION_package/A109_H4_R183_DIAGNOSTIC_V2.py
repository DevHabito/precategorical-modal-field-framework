#!/usr/bin/env python3
import sys,json,hashlib,time
from pathlib import Path
from collections import Counter
import sympy as sp
REPO=Path('/mnt/data/a107_work/repo');sys.path.insert(0,str(REPO/'audits'))
import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1
PR=Path('/mnt/data/A109_H4_R183_DIAGNOSTIC_PREREGISTRATION.json'); EXPECTED='fe222cf6aac119e2bc745a5f1e57cc16fe7c27ed7e8511d9dbce39d879a6e25c'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bisect_exact(poly,a,b,steps=24):
 sa=a103.sign(a103.ev(poly,a)); sb=a103.sign(a103.ev(poly,b))
 if not (sa<0 and sb>0): raise RuntimeError('expected -/+ bracket')
 for _ in range(steps):
  m=(a+b)/2; sm=a103.sign(a103.ev(poly,m))
  if sm==0: return {'lower':str(m),'upper':str(m),'exact_rational_root':True,'steps':_+1,'signs':[0,0]}
  if sm<0: a=m
  else: b=m
 return {'lower':str(a),'upper':str(b),'exact_rational_root':False,'steps':steps,'signs':[int(a103.sign(a103.ev(poly,a))),int(a103.sign(a103.ev(poly,b)))],'width':str(b-a)}
def main():
 if sha(PR)!=EXPECTED: raise RuntimeError('prereg mismatch')
 pr=json.loads(PR.read_text()); r=b1.source_records()[182]; M=int(r['key_fields']['maximum']);j=int(r['key_fields']['compressed_maximizer_contact']);w=sp.Rational(str(r['key_fields']['witness']));L=sp.Rational(str(r['segment_open_bounds'][0]));R=sp.Rational(str(r['segment_open_bounds'][1]))
 if r['key']!=pr['source_key']: raise RuntimeError('source mismatch')
 t=time.time(); D,conds=amin.rank_one_gamma_plus_conditions(M,j);cm=dict(conds);target=f'basic_p_{j+1}';N=cm[target]
 Dcert=a103.certify_positive(a103.int_poly(D,1),L,R,max_depth=28); dcert=a103.certify_positive(a103.derivative(a103.int_poly(N,1)),L,R,max_depth=28)
 signs={'target_L':int(a103.sign(a103.ev(N,L))),'target_witness':int(a103.sign(a103.ev(N,w))),'target_R':int(a103.sign(a103.ev(N,R)))}
 failures=[]; unresolved=[]; methods=Counter(); non_count=0
 for name,p in conds:
  if name==target: continue
  non_count+=1;cert=a103.certify_positive(a103.int_poly(p,1),L,R,max_depth=28);methods[cert['method']]+=1
  if not cert['pass']:
   row={'condition':name,**cert}
   if cert.get('method') in {'internal_nonpositive_witness','endpoint_nonpositive'}: failures.append(row)
   else: unresolved.append(row)
 bracket=None
 if Dcert['pass'] and dcert['pass'] and signs['target_L']<0 and signs['target_witness']>0: bracket=bisect_exact(a103.int_poly(N,1),L,w,24)
 # Monotonicity + sign-changing exact bracket proves unique root; choose rational probes safely on each side.
 direct=[]; dmismatch=0; inside_fail=[]; outside_fail=[]
 if bracket:
  a=sp.Rational(bracket['lower']); b=sp.Rational(bracket['upper']); inside=(b+w)/2 if a!=b else (a+w)/2; outside=(L+a)/2 if a!=b else (L+a)/2
  for label,s,inside_expected in [('inside',inside,True),('witness',w,True),('outside_left',outside,False)]:
   den=a103.ev(D,s); dconds=amin.direct_gamma_plus_conditions(M,j,s); nonpos=[]; mm=[]
   for name,val in dconds:
    if a103.ev(cm[name],s)!=den*val: mm.append(name)
    if val<=0: nonpos.append(name)
   dmismatch+=len(mm)
   if inside_expected and nonpos: inside_fail.append({'label':label,'nonpositive':nonpos})
   if (not inside_expected) and target not in nonpos: outside_fail.append({'label':label,'nonpositive':nonpos})
   direct.append({'label':label,'probe':str(s),'comparison_count':len(dconds),'mismatches':mm,'nonpositive_conditions':nonpos})
 exact=[]
 if not Dcert['pass']: exact.append('D_certificate_failed')
 if not dcert['pass']: exact.append('target_monotonicity_failed')
 if signs['target_L']>=0 or signs['target_witness']<=0: exact.append('target_sign_pattern_failed')
 if failures: exact.append('non_target_nonpositive')
 if dmismatch: exact.append('direct_symbolic_mismatch')
 if inside_fail: exact.append('direct_inside_positivity_failure')
 if outside_fail: exact.append('direct_outside_target_failure')
 if exact: verdict='REFUTED_OR_FAILED_R183_SUFFICIENT_CERTIFICATE'
 elif unresolved: verdict='INCONCLUSIVE_R183_SUFFICIENT_CERTIFICATE'
 elif bracket is None: verdict='INCONCLUSIVE_R183_SUFFICIENT_CERTIFICATE'
 else: verdict='RESOLVED_SUPPORT_R183_LEFT_BOUNDARY'
 out={'audit':pr['audit'],'implementation':'V2 exact monotone bisection; same frozen diagnostic requirements','preregistration_sha256':sha(PR),'verdict':verdict,'rank':183,'source_key':r['key'],'M':M,'j':j,'segment':[str(L),str(R)],'witness':str(w),'target':target,'denominator_certificate':Dcert,'target_derivative_certificate':dcert,'target_signs':signs,'non_target_condition_count':non_count,'non_target_certificate_methods':dict(methods),'non_target_failure_count':len(failures),'non_target_unresolved_count':len(unresolved),'non_target_failures':failures,'non_target_unresolved':unresolved,'unique_root_certificate':{'monotonicity':'strictly increasing','exact_sign_bracket':bracket},'direct_checks':direct,'direct_comparison_count':sum(x['comparison_count'] for x in direct),'direct_mismatch_count':dmismatch,'inside_failures':inside_fail,'outside_failures':outside_fail,'exact_failures':exact,'seconds':time.time()-t,'scope':pr['scope']}
 p=Path('/mnt/data/A109_H4_R183_DIAGNOSTIC_RESULT.json');p.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({'verdict':verdict,'non_target_count':non_count,'non_target_failures':len(failures),'non_target_unresolved':len(unresolved),'root_bracket':bracket,'direct_comparisons':out['direct_comparison_count'],'direct_mismatches':dmismatch,'seconds':out['seconds'],'output':str(p)},indent=2))
if __name__=='__main__':main()
