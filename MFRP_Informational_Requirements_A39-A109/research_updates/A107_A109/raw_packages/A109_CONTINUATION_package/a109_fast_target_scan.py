import sys,json,time,hashlib
from pathlib import Path
from collections import Counter
import sympy as sp
REPO=Path('/mnt/data/a107_work/repo'); sys.path.insert(0,str(REPO/'audits'))
import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1
REF=sp.Rational(1,8)

def target_polys(maximum:int, contact:int):
    h=maximum//2; mean=sp.Rational(maximum,2); eps=a103.normalized_epsilon(maximum)
    ps=[0,contact,contact+1,maximum]; qs=[1,h,h+1]
    def alpha0(x): return REF**x
    rows=[
      [1,1,1,1,0,0,0,-1],
      [0,0,0,0,1,1,1,-1],
      [*ps,0,0,0,-mean],
      [0,0,0,0,*qs,-mean],
      [0,0,0,0,*[a103.tv(x) for x in qs],0],
      [*[alpha0(x) for x in ps],*[-alpha0(x) for x in qs],-2*eps],
      [*[-a103.bv(x) for x in ps],*[a103.bv(x) for x in qs],-2*eps],
      [*[a103.gv(x) for x in ps],*[-a103.gv(x) for x in qs],-2*eps],
    ]
    inv=sp.Matrix(rows).inv(method='DM')
    rhs=sp.Matrix([0,0,0,0,1,0,0,0]); basic0=inv*rhs; u=inv[:,5]
    signs=[1,1,1,1,-1,-1,-1,0]; exps=[*ps,*qs,0]
    updates=[]
    for sg,e in zip(signs,exps):
        if sg==0: updates.append({})
        else: updates.append(a103.add(({e:sp.Rational(sg)},1,0),({0:-sp.Rational(sg)*REF**e},1,0)))
    D={0:sp.Rational(1)}
    for upd,c in zip(updates,u): D=a103.add((D,1,0),(upd,c,0))
    dot={}
    for upd,c in zip(updates,basic0): dot=a103.add((dot,1,0),(upd,c,0))
    nums=[a103.add((D,basic0[i],0),(dot,-u[i],0)) for i in range(4)]
    # order in p support = 0,j,j+1,M => target lower=p_j index1, upper=p_{j+1} index2
    return D, nums[2], nums[1]

def validate_against_full(src, ranks):
    for rank in ranks:
        r=src[rank-1];M=int(r['key_fields']['maximum']);j=int(r['key_fields']['compressed_maximizer_contact'])
        D,U,L=target_polys(M,j); D2,conds=amin.rank_one_gamma_plus_conditions(M,j); cm=dict(conds)
        assert D==D2 and U==cm[f'basic_p_{j+1}'] and L==cm[f'basic_p_{j}'], (rank,M,j)

def main():
    src=b1.source_records(); validate_against_full(src,[174,175,176,177,178,179,180,181])
    cache={}; rows=[]; first_two=None; t=time.time()
    for rank in range(174,len(src)+1):
        r=src[rank-1];M=int(r['key_fields']['maximum']);j=int(r['key_fields']['compressed_maximizer_contact'])
        Lb=sp.Rational(str(r['segment_open_bounds'][0]));Rb=sp.Rational(str(r['segment_open_bounds'][1]));w=sp.Rational(str(r['key_fields']['witness']))
        key=(M,j)
        if key not in cache: cache[key]=target_polys(M,j)
        D,Nu,Nl=cache[key]
        # exact target-only applicability, same A109 rule
        Dcert=a103.certify_positive(a103.int_poly(D,1),Lb,Rb,max_depth=28)
        ucert=a103.certify_positive(a103.derivative(a103.int_poly(Nu,1)),Lb,Rb,max_depth=28)
        mdl={k:-v for k,v in a103.derivative(a103.int_poly(Nl,1)).items()}
        lcert=a103.certify_positive(mdl,Lb,Rb,max_depth=28)
        sUL=a103.sign(a103.ev(Nu,Lb));sUw=a103.sign(a103.ev(Nu,w));sLR=a103.sign(a103.ev(Nl,Rb));sLw=a103.sign(a103.ev(Nl,w))
        app=bool(Dcert['pass'] and ucert['pass'] and lcert['pass'] and sUw>0 and sLw>0 and sUL!=0 and sLR!=0)
        if not app: pred='NO_CLASSIFICATION';bounds=[]
        elif sUL<0 and sLR<0: pred='proper_strict_subcomponent';bounds=[{'side':'left','condition':f'basic_p_{j+1}'},{'side':'right','condition':f'basic_p_{j}'}]
        elif sUL<0: pred='proper_strict_subcomponent';bounds=[{'side':'left','condition':f'basic_p_{j+1}'}]
        elif sLR<0: pred='proper_strict_subcomponent';bounds=[{'side':'right','condition':f'basic_p_{j}'}]
        else: pred='full_segment_coverage';bounds=[]
        row={'canonical_rank':rank,'source_key':r['key'],'M':M,'j':j,'witness':str(w),'segment':[str(Lb),str(Rb)],'applicable':app,'signs':{'upper_at_L':int(sUL),'upper_at_witness':int(sUw),'lower_at_R':int(sLR),'lower_at_witness':int(sLw)},'prediction':pred,'boundaries':bounds}
        rows.append(row)
        if len(bounds)==2 and first_two is None: first_two=row
    out={'audit':'A109_FAST_TARGET_ONLY_SCAN_R174_R922','method':'Exact target-only implementation algebraically regression-checked against full rank_one_gamma_plus_conditions on ranks 174..181; no non-adjacent KKT/full-atlas outcomes consulted.','record_count':len(rows),'first_two_sided_prediction':first_two,'prediction_counts':dict(Counter(r['prediction'] for r in rows)),'records':rows,'seconds':time.time()-t}
    p=Path('/mnt/data/A109_FAST_TARGET_ONLY_SCAN_R174_R922.json');p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'first_two_sided_prediction':first_two,'prediction_counts':out['prediction_counts'],'records':len(rows),'unique_Mj':len(cache),'seconds':out['seconds'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
if __name__=='__main__':main()
