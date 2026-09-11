#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, hashlib, time, importlib.util, os

LO=F(129,1000); HI=F(133,1000)
BETA=F(1,8); GAMMA=F(1,16); TAU=F(1,2)

# ---------- exact linear algebra ----------
def solve(A,b):
    a=[[F(v) for v in row]+[F(bb)] for row,bb in zip(A,b)]
    n=len(a)
    for c in range(n):
        p=next(i for i in range(c,n) if a[i][c])
        a[c],a[p]=a[p],a[c]
        z=a[c][c]; a[c]=[v/z for v in a[c]]
        for i in range(n):
            if i==c: continue
            z=a[i][c]
            if z: a[i]=[a[i][k]-z*a[c][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]

def inv(A):
    n=len(A); cols=[]
    for j in range(n): cols.append(solve(A,[int(i==j) for i in range(n)]))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def mv(A,v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

# ---------- sparse polynomials in s ----------
def padd(*terms):
    out={}
    for p,a in terms:
        if not a: continue
        for e,c in p.items():
            out[e]=out.get(e,F(0))+a*c
            if not out[e]: del out[e]
    return out

def pscale(p,a): return {e:a*c for e,c in p.items() if a*c}
def pconst(a): return {} if not a else {0:F(a)}
def peval(p,x): return sum(c*x**e for e,c in p.items())
def pder(p): return {e-1:F(e)*c for e,c in p.items() if e and c}
def pmul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            out[e+f]=out.get(e+f,F(0))+a*b
    return {e:c for e,c in out.items() if c}

def pcanon(p): return tuple(sorted((int(e),str(c)) for e,c in p.items() if c))

@lru_cache(maxsize=1000000)
def fpow(x:F,e:int): return x**e

def enclosure(p,l,u):
    lo=F(0); hi=F(0)
    for e,c in p.items():
        a=fpow(l,e); b=fpow(u,e)
        if c>=0: lo+=c*a; hi+=c*b
        else: lo+=c*b; hi+=c*a
    return lo,hi

def cert_sign(p,l=LO,u=HI,sign=1,maxdepth=12):
    boxes=0; md=0; stack=[(l,u,0)]
    while stack:
        a,b,d=stack.pop(); boxes+=1; md=max(md,d)
        x,y=enclosure(p,a,b)
        if sign>0 and x>0: continue
        if sign<0 and y<0: continue
        if d>=maxdepth: return False,boxes,md,(a,b,x,y)
        m=(a+b)/2; stack.append((a,m,d+1)); stack.append((m,b,d+1))
    return True,boxes,md,None

def cert_implication(epos,eneg,target,l=LO,u=HI,maxdepth=14):
    # prove epos>0 and eneg<0 => target>0
    boxes=0; md=0; stack=[(l,u,0)]
    while stack:
        a,b,d=stack.pop(); boxes+=1; md=max(md,d)
        tl,tu=enclosure(target,a,b)
        if tl>0: continue  # conclusion true regardless
        pl,pu=enclosure(epos,a,b); nl,nu=enclosure(eneg,a,b)
        if pu<=0 or nl>=0: continue  # antecedent false throughout
        if d>=maxdepth: return False,boxes,md,(a,b,pl,pu,nl,nu,tl,tu)
        m=(a+b)/2; stack.append((a,m,d+1)); stack.append((m,b,d+1))
    return True,boxes,md,None

# ---------- architecture ----------
def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))

def q_aff(M):
    h=M//2; r=F(1,2**h); D=1-(h+1)*r
    if M%2==0:
        return [(-2*r/D,2/D),((1+(h-1)*r)/D,F(-2*h)/D),(-2*(h-1)*r/D,F(2*(h-1))/D)]
    return [(-F(3,2)*r/D,F(2)/D),((1+(2*h-1)*r)/(2*D),F(-2*h)/D),((1-(4*h-2)*r)/(2*D),F(2*h-2)/D)]

@lru_cache(None)
def p_inverse(M,j):
    P=[0,j,j+1,M]
    return inv([[1,x,BETA**x,GAMMA**x] for x in P])

@lru_cache(None)
def q_inverse(M):
    h=M//2; Q=[1,h,h+1]
    return inv([[1,x,TAU**x] for x in Q])

@lru_cache(None)
def primal_aff(M,j):
    h=M//2; P=[0,j,j+1,M]; Q=[1,h,h+1]; e=eps(M)
    qa=q_aff(M)
    qb_s=sum(qa[i][0]*BETA**Q[i] for i in range(3)); qb_0=sum(qa[i][1]*BETA**Q[i] for i in range(3))
    qg_s=sum(qa[i][0]*GAMMA**Q[i] for i in range(3)); qg_0=sum(qa[i][1]*GAMMA**Q[i] for i in range(3))
    C=[[1,1,1,1],P,[BETA**x for x in P],[GAMMA**x for x in P]]
    ps=solve(C,[1,F(M,2),qb_s-2*e,qg_s+2*e]); pc=solve(C,[0,0,qb_0,qg_0])
    # signed delta coefficients F(z)=sum(P-Q) z^x = Aslope(z)t+Bconst(z)
    A={}; B={}
    for x,a,b in zip(P,ps,pc): A[x]=A.get(x,F(0))+a; B[x]=B.get(x,F(0))+b
    for x,(a,b) in zip(Q,qa): A[x]=A.get(x,F(0))-a; B[x]=B.get(x,F(0))-b
    A={x:v for x,v in A.items() if v}; B={x:v for x,v in B.items() if v}
    Aalpha=padd((A,1),(pconst(1),-2*e)); Balpha=B
    return {'P':P,'Q':Q,'ps':ps,'pc':pc,'qa':qa,'A':Aalpha,'B':Balpha}

@lru_cache(None)
def dual_struct(M,j):
    h=M//2; P=[0,j,j+1,M]; Q=[1,h,h+1]; e=eps(M)
    IP=p_inverse(M,j)
    At,Lt,Bt,Ct=mv(IP,[TAU**x for x in P])
    As=[{P[i]:IP[r][i] for i in range(4) if IP[r][i]} for r in range(4)]
    Asp,Lsp,Bsp,Csp=As
    IQ=q_inverse(M)
    gs=[]; g0=[]
    for q in Q:
        gs.append(padd(({q:F(1)},1),(Bsp,-BETA**q),(Csp,-GAMMA**q)))
        g0.append(Bt*BETA**q+Ct*GAMMA**q)
    qsl=[]
    for r in range(3):
        z={}
        for i in range(3): z=padd((z,1),(gs[i],IQ[r][i]))
        qsl.append(z)
    y1s,y3s,y4s=qsl; y1c,y3c,y4c=mv(IQ,g0)
    mu=F(M,2)
    Ld=padd((Asp,-1),(y1s,1),(Lsp,-mu),(y3s,mu),(pconst(1),2*e),(Bsp,2*e),(Csp,-2*e))
    C0=At+y1c+mu*(Lt+y3c)+2*e*(-Bt+Ct)
    return locals()

def raff(M,j,x,kind):
    d=dual_struct(M,j)
    if kind=='p':
        a=padd((d['Asp'],-1),(d['Lsp'],-F(x)),({x:F(1)},1),(d['Bsp'],-BETA**x),(d['Csp'],-GAMMA**x))
        c=d['At']+F(x)*d['Lt']+d['Bt']*BETA**x+d['Ct']*GAMMA**x-TAU**x
    else:
        a=padd((d['y1s'],1),(d['y3s'],F(x)),(d['y4s'],TAU**x),({x:F(1)},-1),(d['Bsp'],BETA**x),(d['Csp'],GAMMA**x))
        c=d['y1c']+F(x)*d['y3c']+TAU**x*d['y4c']-d['Bt']*BETA**x-d['Ct']*GAMMA**x
    return a,F(c)

# A81/A83 compressed adjacent factor, independently transcribed from formulas.
def reduced_blocks(M,j):
    h=M//2; e=eps(M); u=F(1,2**h); d=1-(h+1)*u
    B={0:-F(M-j,M),j:F(1),M:-F(j,M)}
    C={1:F(2)/d,h:F(-2*h)/d,h+1:F(2*(h-1))/d}
    if M%2==0:
        D={1:-2*u/d,h:1+2*h*u/d,h+1:-2*(h-1)*u/d}
    else:
        D={1:-F(3,2)*u/d,h:F(1,2)+F(3*h,2)*u/d,h+1:F(1,2)-F(3*(h-1),2)*u/d}
    H={0:F(1,2)-2*e,M:F(1,2)}
    for x,a in D.items(): H[x]=-a
    Bb=peval(B,BETA); Cb=peval(C,BETA); Ab=(1+BETA**M)/2; Db=peval(D,BETA); Hb=Ab-Db+2*e
    return B,C,D,H,Bb,Cb,Hb

def Epoly(M,j):
    B,C,D,H,Bb,Cb,Hb=reduced_blocks(M,j)
    delta={j+1:F(1),j:F(-1),0:F(1,M),M:F(-1,M)}
    Bt=peval(B,TAU); db=peval(delta,BETA); dt=peval(delta,TAU); At=(1+TAU**M)/2
    X=At*Bb-Hb*Bt; Y=-At*db+Hb*dt; W=-Bb*dt+Bt*db
    return padd((delta,X),(B,Y),(H,W))

def proportional(p,q):
    ks=set(p)|set(q); r=None
    for k in ks:
        a=p.get(k,F(0)); b=q.get(k,F(0))
        if not a and not b: continue
        if not b: return None
        z=a/b
        if r is None: r=z
        elif z!=r: return None
    return r

def ceil_mc(M,s):
    for k in range(1,M+1):
        if 2**M*s.numerator**(2*k) <= s.denominator**(2*k): return k
    raise RuntimeError

def envelope_pairs():
    out=set()
    for M in range(14,521):
        h=M//2; blo=ceil_mc(M,LO); bhi=ceil_mc(M,HI)
        for b0 in range(blo,bhi+1):
            for off in (1,2,3):
                j=b0+off
                if 2<=j<=h-2: out.add((M,j))
    return sorted(out)

# ---------- independent historical controls ----------
def historical_regression():
    path=Path('/mnt/data/h19_exact/h19_standalone_frozen.py')
    if not path.exists(): return {'available':False}
    spec=importlib.util.spec_from_file_location('h19_independent_control',path); h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    fails=[]; comps=0
    # Use all 16 already-inspected H19 records.
    for pred in h.PREDICTIONS:
        M=int(pred['maximum']); j=int(pred['contact_j']); s0=h.sp.Rational(pred['witness']); sf=F(int(s0.p),int(s0.q)); hh=M//2
        direct=dict(h.direct_gamma_plus_conditions(M,j,s0)); d=dual_struct(M,j); ya=-d['C0']/peval(d['Ld'],sf)
        def sfraction(v): return F(int(h.sp.numer(v)),int(h.sp.denom(v)))
        tests=[('active_dual_alpha_+1',ya)]
        for x in [1]:
            a,c=raff(M,j,x,'p'); tests.append((f'reduced_cost_p_{x}',peval(a,sf)*ya+c))
        for x in [0,2,hh-1,hh+2,M]:
            a,c=raff(M,j,x,'q'); tests.append((f'reduced_cost_q_{x}',peval(a,sf)*ya+c))
        # primal all eight
        pr=primal_aff(M,j); A=peval(pr['A'],sf); B=peval(pr['B'],sf); t=-B/A
        for x,a,b in zip(pr['P'],pr['ps'],pr['pc']): tests.append((f'basic_p_{x}',a*t+b))
        for x,(a,b) in zip(pr['Q'],pr['qa']): tests.append((f'basic_q_{x}',a*t+b))
        tests.append(('basic_t',t))
        for name,val in tests:
            comps+=1
            if val!=sfraction(direct[name]): fails.append({'rank':int(pred['canonical_rank']),'name':name})
    return {'available':True,'comparisons':comps,'failures':fails}

# ---------- full replication ----------
def run():
    allpairs=envelope_pairs(); assert len(allpairs)==1870
    start=int(os.environ.get('START','1')); end=int(os.environ.get('END',str(len(allpairs))))
    pairs=allpairs[start-1:end]
    stats={'global_start':start,'global_end':end,'global_pair_count':len(allpairs),
      'pairs':len(pairs),'slope_sign_certificates':0,'threshold_order_certificates':0,
      'slope_boxes':0,'threshold_boxes':0,'dual_denominator_certificates':0,'dual_denominator_boxes':0,
      'gamma_proportionality':0,'gamma_negative_prefactor':0,'conditional_rq2_certificates':0,'conditional_boxes':0,
      'primal_slope_pairs':0,'A_negative':0,'B_positive':0,'tder_positive':0,'primal_boxes':0,
      'max_depth':0,'failures':[]
    }
    t0=time.time()
    for idx,(M,j) in enumerate(pairs,1):
        h=M//2; d=dual_struct(M,j)
        # residual slopes: p1 + q five checkpoints
        residuals=[('p',1)]+[('q',x) for x in (0,2,h-1,h+2,M)]
        aff={key:raff(M,j,key[1],key[0]) for key in residuals}
        for key,(a,c) in aff.items():
            ok,bx,md,why=cert_sign(a,sign=-1,maxdepth=12); stats['slope_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
            if ok: stats['slope_sign_certificates']+=1
            else: stats['failures'].append({'pair':[M,j],'test':'slope','key':key,'detail':str(why)})
        a2,c2=aff[('q',2)]
        for key in [('p',1),('q',0),('q',h-1),('q',h+2),('q',M)]:
            ax,cx=aff[key]
            diff=padd((ax,c2),(a2,-cx))  # c2*ax - cx*a2 > 0 => T2<Tx
            ok,bx,md,why=cert_sign(diff,sign=1,maxdepth=12); stats['threshold_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
            if ok: stats['threshold_order_certificates']+=1
            else: stats['failures'].append({'pair':[M,j],'test':'threshold','key':key,'detail':str(why)})
        # dual denominator positive
        ok,bx,md,why=cert_sign(d['Ld'],sign=1,maxdepth=12); stats['dual_denominator_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
        if ok: stats['dual_denominator_certificates']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'dual_denominator','detail':str(why)})
        # y_gamma numerator proportional to E_j with negative rational ratio
        Ng=padd((d['Ld'],d['Ct']),(d['Csp'],d['C0'])); Ej=Epoly(M,j); rat=proportional(Ng,Ej)
        if rat is not None: stats['gamma_proportionality']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'gamma_proportionality'})
        if rat is not None and rat<0: stats['gamma_negative_prefactor']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'gamma_prefactor','ratio':str(rat)})
        # local maximum E_(j-1)>0, E_j<0 => actual RQ2 numerator >0
        N2=padd((d['Ld'],c2),(a2,-d['C0']))
        Em=Epoly(M,j-1)
        ok,bx,md,why=cert_implication(Em,Ej,N2,maxdepth=16); stats['conditional_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
        if ok: stats['conditional_rq2_certificates']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'conditional_rq2','detail':str(why)})
        # primal slopes and t monotonicity
        pr=primal_aff(M,j); sj=pr['ps'][1]; sj1=pr['ps'][2]
        if sj<0 and sj1>0: stats['primal_slope_pairs']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'primal_affine_slopes','sj':str(sj),'sj1':str(sj1)})
        for name,p,sgn in [('A',pr['A'],-1),('B',pr['B'],1)]:
            ok,bx,md,why=cert_sign(p,sign=sgn,maxdepth=12); stats['primal_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
            if ok: stats['A_negative' if name=='A' else 'B_positive']+=1
            else: stats['failures'].append({'pair':[M,j],'test':name,'detail':str(why)})
        Ntd=padd((pmul(pr['B'],pder(pr['A'])),1),(pmul(pder(pr['B']),pr['A']),-1))
        ok,bx,md,why=cert_sign(Ntd,sign=1,maxdepth=14); stats['primal_boxes']+=bx; stats['max_depth']=max(stats['max_depth'],md)
        if ok: stats['tder_positive']+=1
        else: stats['failures'].append({'pair':[M,j],'test':'tder','detail':str(why)})
        if idx%100==0:
            print(json.dumps({'progress':idx,'failures':len(stats['failures']),'elapsed':round(time.time()-t0,2)}),flush=True)
        if stats['failures']:
            # continue to collect, but fail-fast after 10 for usability
            if len(stats['failures'])>=10: break
    stats['elapsed_seconds']=time.time()-t0
    stats['historical_regression']=({'skipped':True} if os.environ.get('SKIP_HIST')=='1' else historical_regression())
    stats['verdict']='PASS' if not stats['failures'] and not stats['historical_regression'].get('failures',[]) else 'FAIL'
    return stats

if __name__=='__main__':
    out=run()
    p=Path(f"/mnt/data/A110_INDEPENDENT_EXHAUSTIVE_REPLICATION_{out['global_start']}_{out['global_end']}.json")
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    s=Path('/mnt/data/a110_independent_replication.py')
    manifest={s.name:hashlib.sha256(s.read_bytes()).hexdigest(),p.name:hashlib.sha256(p.read_bytes()).hexdigest()}
    Path('/mnt/data/A110_INDEPENDENT_EXHAUSTIVE_REPLICATION_SHA256.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps({'verdict':out['verdict'],'failures':len(out['failures']),'elapsed':out['elapsed_seconds'],'summary':{k:v for k,v in out.items() if k not in ('failures','historical_regression')}},default=str),flush=True)
