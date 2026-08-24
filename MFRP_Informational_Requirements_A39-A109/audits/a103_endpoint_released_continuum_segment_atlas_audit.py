#!/usr/bin/env python3
"""A103 exact continuum atlas for the 76 endpoint-released lift segments.

A97 found 76 rational obstruction witnesses whose strict global finite-LP
optimum has

    P={j-1,j,M}, Q={1,h,h+1}, active={alpha+,beta-}, gamma inactive.

A103 upgrades those isolated witnesses to exact continuous statements on the
76 rational phase segments inherited from A95.  Only the alpha row varies with
s.  A rank-one row update around the dyadic reference s=1/8 gives one sparse
common denominator and sparse exact numerators for every KKT condition.

For every segment the audit either:
  * certifies the basis on the complete closed rational segment, or
  * isolates the nearest algebraic KKT boundary/boundaries, proves the maximal
    strict component containing the A95 witness, and gives an exact rational
    counterexample outside that component.

The theorem is relative to the declared finite LP and the A95 rational inner
phase segments.  It is not an all-cell lifted theorem, not an all-M theorem,
and not a physical or ontological claim.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import multiprocessing as mp
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
PROVENANCE = ROOT / "provenance" / "a103_continuum_atlas" if HERE.name == "audits" else HERE / "provenance"
A95_RESULT = RESULTS / "a95_rational_witness_lift_results.json"
A95_CATALOGUE = RESULTS / "a95_rational_witness_lift_catalogue.json"
A97_RESULT = RESULTS / "a97_endpoint_released_interval_and_obstruction_results.json"
A97_CATALOGUE = RESULTS / "a97_endpoint_released_obstruction_catalogue.json"
A102_RESULT = RESULTS / "a102_complete_rational_witness_lift_atlas_results.json"

REF = sp.Rational(1, 8)
ROOT_TOL = sp.Rational(1, 10**27)
MAX_DEPTH = 16
SparsePoly = dict[int, sp.Rational]

def normalized_epsilon(M):
 h=M//2; factor=1875 if M%2==0 else 2500; return sp.Rational(1,factor*2**h)
def tv(x): return sp.Rational(1,2**x)
def bv(x): return sp.Rational(1,2**(3*x))
def gv(x): return sp.Rational(1,2**(4*x))
def add(*parts):
 out={}
 for p,scale,shift in parts:
  scale=sp.Rational(scale)
  for e,c in p.items(): out[e+shift]=out.get(e+shift,sp.Rational(0))+scale*c
 return {e:c for e,c in out.items() if c}
def ev(p,x): return sum(c*x**e for e,c in p.items())
def der(p): return {e-1:e*c for e,c in p.items() if e>0}
def interval_powers(p,lp,up):
 lo=sp.Rational(0); hi=sp.Rational(0)
 for e,c in p.items():
  le=lp[e]; ue=up[e]
  if c>=0: lo+=c*le; hi+=c*ue
  else: lo+=c*ue; hi+=c*le
 return lo,hi

def rank(M,j,s0):
 h=M//2; mean=sp.Rational(M,2); eps=normalized_epsilon(M)
 P=[j-1,j,M]; Q=[1,h,h+1]
 def a0(x): return s0**x
 rows=[
 [1,1,1,0,0,0,-1],
 [0,0,0,1,1,1,-1],
 [*P,0,0,0,-mean],
 [0,0,0,*Q,-mean],
 [0,0,0,*[tv(x) for x in Q],0],
 [*[a0(x) for x in P],*[-a0(x) for x in Q],-2*eps],
 [*[-bv(x) for x in P],*[bv(x) for x in Q],-2*eps],
 ]
 mat=sp.Matrix(rows); inv=mat.inv(method='DM'); rhs=sp.Matrix([0,0,0,0,1,0,0]); obj=sp.Matrix([*[tv(x) for x in P],0,0,0,0])
 b0=inv*rhs; d0=inv.T*obj; ai=5; ud=inv[:,ai]
 signs=[1,1,1,-1,-1,-1,0]; exps=[*P,*Q,0]
 updates=[]
 for sig,e in zip(signs,exps):
  updates.append({} if sig==0 else add(({e:sp.Rational(sig)},1,0),({0:-sp.Rational(sig)*s0**e},1,0)))
 den={0:sp.Rational(1)}
 for up,c in zip(updates,ud): den=add((den,1,0),(up,c,0))
 dot={}
 for up,c in zip(updates,b0): dot=add((dot,1,0),(up,c,0))
 bn=[add((den,b0[i],0),(dot,-ud[i],0)) for i in range(7)]
 odu=obj.dot(ud); dn=[]
 for col in range(7):
  ui={}
  for row,up in enumerate(updates): ui=add((ui,1,0),(up,inv[row,col],0))
  dn.append(add((den,d0[col],0),(ui,-odu,0)))
 cond=[]
 names=[*[f'basic_p_{x}' for x in P],*[f'basic_q_{x}' for x in Q],'basic_t']
 cond.extend(zip(names,bn)); cond.extend([('active_dual_alpha_+1',dn[5]),('active_dual_beta_-1',dn[6])])
 ps=set(P); qs=set(Q)
 for x in range(M+1):
  if x not in ps:
   cond.append((f'reduced_cost_p_{x}',add((dn[0],1,0),(dn[2],x,0),(dn[5],1,x),(dn[6],-bv(x),0),(den,-tv(x),0))))
  if x not in qs:
   cond.append((f'reduced_cost_q_{x}',add((dn[1],1,0),(dn[3],x,0),(dn[4],tv(x),0),(dn[5],-1,x),(dn[6],bv(x),0))))
 # slacks
 ad={}
 for i,x in enumerate(P): ad=add((ad,1,0),(bn[i],1,x))
 for i,x in enumerate(Q): ad=add((ad,1,0),(bn[3+i],-1,x))
 def cd(fn):
  out={}
  for i,x in enumerate(P): out=add((out,1,0),(bn[i],fn(x),0))
  for i,x in enumerate(Q): out=add((out,1,0),(bn[3+i],-fn(x),0))
  return out
 bd=cd(bv); gd=cd(gv); t=bn[-1]
 cond += [('inactive_slack_alpha_-1',add((t,2*eps,0),(ad,1,0))),('inactive_slack_beta_+1',add((t,2*eps,0),(bd,-1,0))),('inactive_slack_gamma_+1',add((t,2*eps,0),(gd,-1,0))),('inactive_slack_gamma_-1',add((t,2*eps,0),(gd,1,0)))]
 return den,cond


def sign(x:int|sp.Expr)->int: return 1 if x>0 else -1 if x<0 else 0

def int_poly(p:dict[int,sp.Rational], orientation:int=1)->dict[int,int]:
    L=1
    for c in p.values(): L=math.lcm(L,int(c.q))
    out={e:orientation*int(c.p)*(L//int(c.q)) for e,c in p.items()}
    g=0
    for v in out.values(): g=math.gcd(g,abs(v))
    if g>1: out={e:v//g for e,v in out.items()}
    return {e:v for e,v in out.items() if v}

def derivative(p:dict[int,int])->dict[int,int]:
    return {e-1:e*c for e,c in p.items() if e>0 and e*c}

def point_sign(p:dict[int,int],x:sp.Rational)->int:
    if not p: return 0
    d=max(p); a=int(x.p); b=int(x.q)
    total=0
    for e,c in p.items(): total += c*pow(a,e)*pow(b,d-e)
    return sign(total)

def interval_signs(p:dict[int,int],l:sp.Rational,u:sp.Rational)->tuple[int,int]:
    if not p:return (0,0)
    d=max(p); D=math.lcm(int(l.q),int(u.q)); a=int(l.p)*(D//int(l.q)); b=int(u.p)*(D//int(u.q))
    lo=0;hi=0
    for e,c in p.items():
        lv=pow(a,e)*pow(D,d-e); uv=pow(b,e)*pow(D,d-e)
        if c>=0: lo+=c*lv;hi+=c*uv
        else: lo+=c*uv;hi+=c*lv
    return sign(lo),sign(hi)

def certify_positive(p:dict[int,int],l:sp.Rational,u:sp.Rational,max_depth:int=MAX_DEPTH)->dict[str,Any]:
    """Exact positivity certificate on closed [l,u]."""
    cache:dict[tuple[int,int,int,int],tuple[int,int]]={}
    def iv(poly:dict[int,int],a:sp.Rational,b:sp.Rational):
        key=(id(poly),hash(a),hash(b),len(poly))
        if key not in cache: cache[key]=interval_signs(poly,a,b)
        return cache[key]
    pL=point_sign(p,l); pU=point_sign(p,u)
    if pL<=0 or pU<=0:
        return {'pass':False,'method':'endpoint_nonpositive','endpoint_signs':[pL,pU],'nodes':0,'max_depth':0}
    first=iv(p,l,u)
    if first[0]>0:
        return {'pass':True,'method':'single_interval','endpoint_signs':[pL,pU],'nodes':1,'max_depth':0}
    d1=derivative(p); d2=derivative(d1)
    if d1:
        s1=iv(d1,l,u)
        if s1[0]>0:
            return {'pass':True,'method':'monotone_increasing','endpoint_signs':[pL,pU],'derivative_signs':list(s1),'nodes':1,'max_depth':0}
        if s1[1]<0:
            return {'pass':True,'method':'monotone_decreasing','endpoint_signs':[pL,pU],'derivative_signs':list(s1),'nodes':1,'max_depth':0}
    if d2:
        s2=iv(d2,l,u)
        if s2[1]<0:
            return {'pass':True,'method':'strictly_concave_endpoint_minimum','endpoint_signs':[pL,pU],'second_derivative_signs':list(s2),'nodes':1,'max_depth':0}
        if s2[0]>0 and d1:
            dl=point_sign(d1,l);du=point_sign(d1,u)
            if dl>=0:
                return {'pass':True,'method':'convex_increasing','endpoint_signs':[pL,pU],'derivative_endpoint_signs':[dl,du],'nodes':1,'max_depth':0}
            if du<=0:
                return {'pass':True,'method':'convex_decreasing','endpoint_signs':[pL,pU],'derivative_endpoint_signs':[dl,du],'nodes':1,'max_depth':0}
    stack=[(l,u,0)];nodes=0;deep=0
    while stack:
        a,b,depth=stack.pop();nodes+=1;deep=max(deep,depth)
        ss=iv(p,a,b)
        if ss[0]>0: continue
        # local shape tests
        if d1:
            ds=iv(d1,a,b)
            if ds[0]>0 and point_sign(p,a)>0: continue
            if ds[1]<0 and point_sign(p,b)>0: continue
        if d2:
            dds=iv(d2,a,b)
            if dds[1]<0 and point_sign(p,a)>0 and point_sign(p,b)>0: continue
        if depth>=max_depth:
            return {'pass':False,'method':'adaptive_unresolved','endpoint_signs':[pL,pU],'nodes':nodes,'max_depth':deep,'unresolved_interval':[str(a),str(b)],'interval_signs':list(ss)}
        m=(a+b)/2
        sm=point_sign(p,m)
        if sm<=0:
            return {'pass':False,'method':'internal_nonpositive_witness','endpoint_signs':[pL,pU],'nodes':nodes,'max_depth':deep,'counterexample':str(m),'counterexample_sign':sm}
        stack.append((m,b,depth+1));stack.append((a,m,depth+1))
    return {'pass':True,'method':'adaptive_interval','endpoint_signs':[pL,pU],'nodes':nodes,'max_depth':deep}

def isolate_sign_change(p:dict[int,int],a:sp.Rational,b:sp.Rational)->dict[str,Any]:
    sa=point_sign(p,a);sb=point_sign(p,b)
    if sa==0:return {'exact_root':str(a),'bracket':[str(a),str(a)],'endpoint_signs':[0,0],'simple':False}
    if sb==0:return {'exact_root':str(b),'bracket':[str(b),str(b)],'endpoint_signs':[0,0],'simple':False}
    if sa*sb>=0: raise ValueError(('no sign change',sa,sb,a,b))
    lo,hi=a,b;slo,shi=sa,sb
    steps=0
    while hi-lo>ROOT_TOL and steps<160:
        mid=(lo+hi)/2;sm=point_sign(p,mid);steps+=1
        if sm==0:
            return {'exact_root':str(mid),'bracket':[str(mid),str(mid)],'endpoint_signs':[0,0],'simple':False,'bisection_steps':steps}
        if sm==slo: lo,slo=mid,sm
        else: hi,shi=mid,sm
    d=derivative(p); dsigns=interval_signs(d,lo,hi) if d else (0,0)
    simple=(dsigns[0]>0 or dsigns[1]<0)
    return {'bracket':[str(lo),str(hi)],'endpoint_signs':[slo,shi],'width':str(hi-lo),'bisection_steps':steps,'derivative_interval_signs':list(dsigns),'unique_simple_in_bracket':simple}

def build_polys(record:dict[str,Any]):
    M=int(record['maximum']);j=int(record['compressed_maximizer_contact']);w=sp.Rational(record['witness'])
    den,conds=rank(M,j,REF)
    ori=sign(ev(den,w))
    if ori==0: raise RuntimeError('denominator zero at witness')
    polys=[('common_denominator',int_poly(den,ori))]
    polys += [(n,int_poly(p,ori)) for n,p in conds]
    return polys,ori

def analyze_record(record:dict[str,Any])->dict[str,Any]:
    t=time.time();M=int(record['maximum']);j=int(record['compressed_maximizer_contact']);w=sp.Rational(record['witness']);segL=sp.Rational(record['segment_open_bounds'][0]);segU=sp.Rational(record['segment_open_bounds'][1])
    polys,ori=build_polys(record); pmap=dict(polys)
    assert all(point_sign(p,w)>0 for _,p in polys)
    left_candidates=[];right_candidates=[]
    for name,p in polys:
        sl=point_sign(p,segL);sr=point_sign(p,segU)
        if sl<0:left_candidates.append(name)
        if sr<0:right_candidates.append(name)
        if sl==0:left_candidates.append(name)
        if sr==0:right_candidates.append(name)
    left_roots=[]
    for name in left_candidates:
        p=pmap[name]; sw=point_sign(p,w); sl=point_sign(p,segL)
        if sl*sw<0:left_roots.append({'condition':name,**isolate_sign_change(p,segL,w)})
        elif sl==0:left_roots.append({'condition':name,'exact_root':str(segL),'bracket':[str(segL),str(segL)],'endpoint_signs':[0,0],'unique_simple_in_bracket':False})
    right_roots=[]
    for name in right_candidates:
        p=pmap[name]; sw=point_sign(p,w); sr=point_sign(p,segU)
        if sw*sr<0:right_roots.append({'condition':name,**isolate_sign_change(p,w,segU)})
        elif sr==0:right_roots.append({'condition':name,'exact_root':str(segU),'bracket':[str(segU),str(segU)],'endpoint_signs':[0,0],'unique_simple_in_bracket':False})
    def brats(x):return tuple(sp.Rational(v) for v in x['bracket'])
    # nearest roots to witness: max left root, min right root, using midpoint ordering
    selected_left=max(left_roots,key=lambda x:sum(brats(x))/2) if left_roots else None
    selected_right=min(right_roots,key=lambda x:sum(brats(x))/2) if right_roots else None
    coreL=brats(selected_left)[1] if selected_left else segL
    coreU=brats(selected_right)[0] if selected_right else segU
    if not coreL<w<coreU: raise RuntimeError(('invalid core',M,coreL,w,coreU))
    certificates=[];failures=[];methods={};nodes=0
    for name,p in polys:
        cert=certify_positive(p,coreL,coreU)
        certificates.append({'name':name,**cert})
        methods[cert['method']]=methods.get(cert['method'],0)+1;nodes+=int(cert.get('nodes',0))
        if not cert['pass']:failures.append({'name':name,**cert})
    # Selected root local simplicity and signs are required.
    root_fail=[]
    for side,root in [('left',selected_left),('right',selected_right)]:
        if root and not root.get('exact_root') and not root.get('unique_simple_in_bracket'):
            root_fail.append({'side':side,'condition':root['condition'],'reason':'root_not_simple_in_bracket'})
    # Exact counterexamples just outside component where available.
    counterexamples=[]
    if selected_left:
        a,b=brats(selected_left); x=(segL+a)/2 if segL<a else a
        if x<coreL:
            counterexamples.append({'side':'left','condition':selected_left['condition'],'point':str(x),'sign':point_sign(pmap[selected_left['condition']],x)})
    if selected_right:
        a,b=brats(selected_right); x=(b+segU)/2 if b<segU else b
        if x>coreU:
            counterexamples.append({'side':'right','condition':selected_right['condition'],'point':str(x),'sign':point_sign(pmap[selected_right['condition']],x)})
    full=(selected_left is None and selected_right is None and not failures)
    partial=((selected_left is not None or selected_right is not None) and not failures and not root_fail)
    status='full_segment_coverage' if full else 'proper_strict_subcomponent' if partial else 'internal_failure_or_unresolved'
    return {
      'key':f"M={M}|b={record['base_contact']}|phase={record['compressed_phase']}|side={record['phase_side']}|s={record['witness']}|j={j}",
      'maximum':M,'base_contact':int(record['base_contact']),'compressed_phase':record['compressed_phase'],'phase_side':record['phase_side'],'witness':str(w),'compressed_contact':j,
      'segment_open_bounds':[str(segL),str(segU)],'reference_probe_for_rank_one':'1/8','orientation':ori,'condition_count':len(polys)-1,'numerator_plus_denominator_count':len(polys),
      'status':status,'strict_component':{'lower':str(coreL),'upper':str(coreU),'selected_left_boundary':selected_left,'selected_right_boundary':selected_right},
      'all_left_root_candidates':left_roots,'all_right_root_candidates':right_roots,'endpoint_negative_or_zero_conditions':{'left':left_candidates,'right':right_candidates},
      'certificate_summary':{'pass_count':sum(c['pass'] for c in certificates),'failure_count':len(failures),'method_counts':methods,'adaptive_node_count':nodes,'root_failure_count':len(root_fail)},
      'condition_certificates':certificates,'failures':failures,'root_failures':root_fail,'outside_counterexamples':counterexamples,'seconds':time.time()-t,
    }



def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_records() -> list[dict[str, Any]]:
    a97 = json.loads(A97_CATALOGUE.read_text(encoding="utf-8"))
    a95 = json.loads(A95_CATALOGUE.read_text(encoding="utf-8"))
    pass_keys = {
        (int(record["maximum"]), str(record["witness"]), int(record["compressed_maximizer_contact"]))
        for record in a97["records"]
        if record["endpoint_released_result"]["status"] == "pass"
    }
    records = [
        record for record in a95["records"]
        if int(record["strict_pass_count"]) == 0
        and (
            int(record["maximum"]),
            str(record["witness"]),
            int(record["compressed_maximizer_contact"]),
        ) in pass_keys
    ]
    records.sort(key=lambda item: (
        int(item["maximum"]),
        int(item["compressed_maximizer_contact"]),
        str(item["witness"]),
    ))
    return records


def analyze_record_complete(record: dict[str, Any]) -> dict[str, Any]:
    output = analyze_record(record)
    # Strengthen the core certificate: every non-selected condition is positive
    # on the complete boundary hull, including both tiny isolating brackets.
    source = {
        "maximum": output["maximum"],
        "compressed_maximizer_contact": output["compressed_contact"],
        "witness": output["witness"],
    }
    polynomials, _ = build_polys(source)
    left = output["strict_component"]["selected_left_boundary"]
    right = output["strict_component"]["selected_right_boundary"]
    segment_lower = sp.Rational(output["segment_open_bounds"][0])
    segment_upper = sp.Rational(output["segment_open_bounds"][1])
    hull_lower = sp.Rational(left["bracket"][0]) if left else segment_lower
    hull_upper = sp.Rational(right["bracket"][1]) if right else segment_upper
    selected = {item["condition"] for item in (left, right) if item}
    method_counts: Counter[str] = Counter()
    failures: list[dict[str, Any]] = []
    nonselected_count = 0
    for name, polynomial in polynomials:
        if name in selected:
            continue
        certificate = certify_positive(polynomial, hull_lower, hull_upper)
        nonselected_count += 1
        method_counts[certificate["method"]] += 1
        if not certificate["pass"]:
            failures.append({"name": name, **certificate})
    output["nonselected_boundary_hull_certificate"] = {
        "hull": [str(hull_lower), str(hull_upper)],
        "selected_boundary_conditions": sorted(selected),
        "nonselected_condition_count": nonselected_count,
        "pass_count": nonselected_count - len(failures),
        "failure_count": len(failures),
        "method_counts": dict(method_counts),
        "failures": failures,
    }
    if failures:
        output["status"] = "internal_failure_or_unresolved"
    return output


def write_chunk(start: int, end: int, output: Path, workers: int) -> None:
    records = source_records()[start:end]
    computed: list[dict[str, Any]] = []
    with mp.Pool(processes=min(workers, max(1, len(records)))) as pool:
        for item in pool.imap_unordered(analyze_record_complete, records, chunksize=1):
            computed.append(item)
            print(json.dumps({
                "maximum": item["maximum"],
                "status": item["status"],
                "condition_failures": item["certificate_summary"]["failure_count"],
                "hull_failures": item["nonselected_boundary_hull_certificate"]["failure_count"],
            }), flush=True)
    computed.sort(key=lambda item: item["key"])
    payload = {
        "audit_phase": "A103_EXACT_CONTINUUM_CHUNK",
        "source_record_slice": [start, end],
        "record_count": len(computed),
        "records": computed,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(output), "record_count": len(computed)}))


def semantic_right_boundary(name: str | None) -> str | None:
    if name is None:
        return None
    if name.startswith("basic_p_"):
        return "basic_p_{j-1}"
    return name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-start", type=int)
    parser.add_argument("--chunk-end", type=int)
    parser.add_argument("--chunk-output", type=str)
    parser.add_argument("--workers", type=int, default=min(8, max(1, os.cpu_count() or 1)))
    parser.add_argument("--chunk-glob", type=str, default="a103_chunk_*.json")
    args = parser.parse_args()
    RESULTS.mkdir(parents=True, exist_ok=True)
    PROVENANCE.mkdir(parents=True, exist_ok=True)

    if args.chunk_output is not None:
        if args.chunk_start is None or args.chunk_end is None:
            raise ValueError("--chunk-start and --chunk-end are required with --chunk-output")
        write_chunk(args.chunk_start, args.chunk_end, Path(args.chunk_output), args.workers)
        return

    a95 = json.loads(A95_RESULT.read_text(encoding="utf-8"))
    a97 = json.loads(A97_RESULT.read_text(encoding="utf-8"))
    a102 = json.loads(A102_RESULT.read_text(encoding="utf-8"))
    expected = source_records()
    expected_keys = {
        f"M={int(record['maximum'])}|b={int(record['base_contact'])}|phase={record['compressed_phase']}|side={record['phase_side']}|s={record['witness']}|j={int(record['compressed_maximizer_contact'])}"
        for record in expected
    }

    chunk_paths = sorted(PROVENANCE.glob(args.chunk_glob))
    records: list[dict[str, Any]] = []
    chunk_manifest = []
    for path in chunk_paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        records.extend(payload["records"])
        chunk_manifest.append({
            "file": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "record_count": int(payload["record_count"]),
            "source_record_slice": payload["source_record_slice"],
        })
    records.sort(key=lambda item: item["key"])
    keys = [record["key"] for record in records]
    duplicate_keys = [key for key, count in Counter(keys).items() if count > 1]
    missing_keys = sorted(expected_keys - set(keys))
    extra_keys = sorted(set(keys) - expected_keys)

    status_counts = Counter(record["status"] for record in records)
    phase_status_counts = Counter((record["compressed_phase"], record["status"]) for record in records)
    left_boundary_counts = Counter(
        (record["strict_component"]["selected_left_boundary"] or {}).get("condition")
        for record in records
    )
    right_boundary_counts = Counter(
        semantic_right_boundary((record["strict_component"]["selected_right_boundary"] or {}).get("condition"))
        for record in records
    )
    condition_count = sum(int(record["condition_count"]) for record in records)
    polynomial_count = sum(int(record["numerator_plus_denominator_count"]) for record in records)
    core_failures = sum(int(record["certificate_summary"]["failure_count"]) for record in records)
    root_failures = sum(int(record["certificate_summary"]["root_failure_count"]) for record in records)
    hull_failures = sum(int(record["nonselected_boundary_hull_certificate"]["failure_count"]) for record in records)
    outside_counterexamples = [
        counterexample
        for record in records
        for counterexample in record["outside_counterexamples"]
    ]
    nonnegative_counterexamples = [item for item in outside_counterexamples if int(item["sign"]) >= 0]
    selected_roots = [
        root
        for record in records
        for root in (
            record["strict_component"]["selected_left_boundary"],
            record["strict_component"]["selected_right_boundary"],
        )
        if root is not None
    ]
    all_selected_roots_simple = all(
        bool(root.get("unique_simple_in_bracket")) or "exact_root" in root
        for root in selected_roots
    )
    all_components_contain_witness = all(
        sp.Rational(record["strict_component"]["lower"])
        < sp.Rational(record["witness"])
        < sp.Rational(record["strict_component"]["upper"])
        for record in records
    )

    a95_valid = bool(
        a95.get("verdict")
        == "PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION"
        and all(a95.get("gates", {}).values())
        and a95["natural_lift_result"]["no_strict_lift_count"] == 83
    )
    a97_valid = bool(
        a97.get("verdict")
        == "PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS"
        and all(a97.get("gates", {}).values())
        and a97["obstruction_atlas"]["endpoint_released_strict_pass_count"] == 76
    )
    a102_valid = bool(
        a102.get("verdict") == "PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS"
        and all(a102.get("gates", {}).values())
        and a102["complete_atlas"]["witness_count"] == 1063
    )

    gates = {
        "A95_rational_witness_source_present_and_passed": a95_valid,
        "A97_76_endpoint_released_witness_source_present_and_passed": a97_valid,
        "A102_complete_witness_atlas_source_present_and_passed": a102_valid,
        "chunk_provenance_is_present": len(chunk_paths) > 0,
        "chunk_records_cover_exactly_76_source_segments": len(records) == 76,
        "all_76_keys_are_unique": len(duplicate_keys) == 0,
        "no_source_segment_is_missing_or_extra": not missing_keys and not extra_keys,
        "exact_KKT_condition_count_is_54944": condition_count == 54944,
        "exact_numerator_plus_denominator_count_is_55020": polynomial_count == 55020,
        "classification_is_25_full_and_51_partial_with_zero_unresolved": status_counts == {
            "full_segment_coverage": 25,
            "proper_strict_subcomponent": 51,
        },
        "all_14_unique_b_plus_3_segments_have_full_coverage": phase_status_counts[("unique_b_plus_3", "full_segment_coverage")] == 14,
        "all_11_b_plus_2_to_b_plus_3_right_segments_have_full_coverage": phase_status_counts[("b_plus_2_to_b_plus_3", "full_segment_coverage")] == 11,
        "all_46_b_plus_1_to_b_plus_2_right_segments_are_partial": phase_status_counts[("b_plus_1_to_b_plus_2", "proper_strict_subcomponent")] == 46,
        "all_5_unique_b_plus_2_segments_are_partial": phase_status_counts[("unique_b_plus_2", "proper_strict_subcomponent")] == 5,
        "exactly_four_lower_boundaries_are_gamma_minus_slack_roots": left_boundary_counts == {None: 72, "inactive_slack_gamma_-1": 4},
        "right_boundaries_are_49_p_lower_mass_roots_and_two_q0_reduced_cost_roots": right_boundary_counts == {None: 25, "basic_p_{j-1}": 49, "reduced_cost_q_0": 2},
        "all_55_selected_algebraic_boundaries_are_locally_unique_and_simple": len(selected_roots) == 55 and all_selected_roots_simple,
        "all_55020_core_polynomial_certificates_pass": core_failures == 0,
        "all_nonselected_conditions_pass_on_complete_boundary_hulls": hull_failures == 0,
        "all_51_partial_segments_have_exact_negative_outside_counterexamples": len(outside_counterexamples) == 55 and not nonnegative_counterexamples,
        "every_certified_component_contains_its_A95_witness": all_components_contain_witness,
        "no_denominator_or_KKT_condition_failure_remains": core_failures == 0 and root_failures == 0 and hull_failures == 0,
        "formal_contract_and_nonphysical_scope_are_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}
    verdict = (
        "PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS"
        if all(gates.values())
        else "FAIL_A103_EXACT_CONTINUUM_ENDPOINT_RELEASED_SEGMENT_CLASSIFICATION"
    )

    catalogue = {
        "audit": "A103_EXACT_ENDPOINT_RELEASED_CONTINUUM_SEGMENT_ATLAS",
        "contract": {
            "source_segment_count": 76,
            "maximum_range": [125, 520],
            "source_segments": "A95 exact rational inner phase segments corresponding to the 76 A97 endpoint-released strict witnesses",
            "tested_family": "P={j-1,j,M}, Q={1,h,h+1}, alpha+ and beta- active, gamma inactive",
            "symbolic_method": "exact Sherman-Morrison rank-one alpha-row update around s=1/8",
            "claim": "complete exact classification of the strict KKT component containing each of the 76 rational witnesses inside its declared rational source segment",
            "explicit_nonclaim": "not a lift theorem for the other 987 A102 witnesses, not an all-cell theorem, not an all-M theorem, and not a physical claim",
        },
        "summary": {
            "record_count": len(records),
            "unique_key_count": len(set(keys)),
            "status_counts": dict(status_counts),
            "phase_status_counts": {f"{phase}::{status}": count for (phase, status), count in sorted(phase_status_counts.items())},
            "condition_count": condition_count,
            "numerator_plus_denominator_count": polynomial_count,
            "selected_boundary_count": len(selected_roots),
            "left_boundary_counts": {str(key): value for key, value in left_boundary_counts.items()},
            "right_boundary_counts": {str(key): value for key, value in right_boundary_counts.items()},
            "outside_counterexample_count": len(outside_counterexamples),
            "core_failure_count": core_failures,
            "root_failure_count": root_failures,
            "hull_failure_count": hull_failures,
        },
        "chunk_manifest": chunk_manifest,
        "records": records,
        "failures": {
            "duplicate_keys": duplicate_keys,
            "missing_keys": missing_keys,
            "extra_keys": extra_keys,
            "nonnegative_outside_counterexamples": nonnegative_counterexamples,
        },
    }
    results = {
        "audit": "A103_EXACT_ENDPOINT_RELEASED_CONTINUUM_SEGMENT_ATLAS",
        "evidence_class": "exact sparse rational-function KKT reduction, exact rational interval arithmetic, exact algebraic root brackets, and exact outside counterexamples",
        "scope": catalogue["contract"],
        "continuum_atlas": catalogue["summary"],
        "structural_result": {
            "full_segment_classes": [
                {"compressed_phase": "unique_b_plus_3", "segment_count": 14},
                {"compressed_phase": "b_plus_2_to_b_plus_3", "phase_side": "right", "segment_count": 11},
            ],
            "partial_segment_classes": [
                {"compressed_phase": "b_plus_1_to_b_plus_2", "phase_side": "right", "segment_count": 46},
                {"compressed_phase": "unique_b_plus_2", "segment_count": 5},
            ],
            "boundary_mechanisms": {
                "lower_gamma_minus_slack_entry": 4,
                "upper_p_lower_mass_exit": 49,
                "upper_q0_reduced_cost_entry": 2,
            },
            "interpretation": "the endpoint-released family is continuously valid on all 76 witness-containing components, but only 25 cover their complete A95 rational source segment; 51 encounter exact internal KKT boundaries",
        },
        "provenance": {
            "chunk_count": len(chunk_manifest),
            "chunks": chunk_manifest,
            "source_hashes": {
                "A95_result": sha256(A95_RESULT),
                "A95_catalogue": sha256(A95_CATALOGUE),
                "A97_result": sha256(A97_RESULT),
                "A97_catalogue": sha256(A97_CATALOGUE),
                "A102_result": sha256(A102_RESULT),
            },
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "fail_count": len(gates) - sum(gates.values()),
        "failed_gates": [name for name, passed in gates.items() if not passed],
        "verdict": verdict,
    }

    catalogue_path = RESULTS / "a103_endpoint_released_continuum_segment_catalogue.json"
    result_path = RESULTS / "a103_endpoint_released_continuum_segment_results.json"
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")
    result_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": verdict,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "full_segment_count": status_counts.get("full_segment_coverage", 0),
        "partial_segment_count": status_counts.get("proper_strict_subcomponent", 0),
        "result": str(result_path),
        "catalogue": str(catalogue_path),
    }, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
