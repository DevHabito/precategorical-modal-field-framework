#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114C2_PHI_CORE_EXACT_CROSSCHECK_20260914.json'
B=F(1,8); G=F(1,16)

MS=list(range(521,701,17))+[760,821,886,951,1000,1282,1500,2049]
SS=[F(n,10000) for n in (1290,1295,1300,1305,1310,1315,1320,1325,1330)]
ERRCAP=F(1,10**26)

def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))

def exact_b(M,s):
    # Smallest integer b with s^(2b)<=2^(-M), using only exact integer/rational comparisons.
    target=F(1,2**M)
    lo,hi=0,M
    while lo<hi:
        mid=(lo+hi)//2
        if s**(2*mid)<=target: hi=mid
        else: lo=mid+1
    return lo

def full_phi(M,s,j):
    h=M//2; U=F(1,2**h); d=1-(h+1)*U; ep=eps(M)
    a=F(M-j,M)
    def Br(r): return r**j-a-F(j,M)*r**M
    def Cr(r): return 2*r/d-F(2*h,1)*r**h/d+F(2*(h-1),1)*r**(h+1)/d
    def Dr(r):
        if M%2==0:
            return -2*U*r/d+(1+2*h*U/d)*r**h-2*(h-1)*U*r**(h+1)/d
        return -F(3,2)*U*r/d+(F(1,2)+F(3,2)*h*U/d)*r**h+(F(1,2)-F(3,2)*(h-1)*U/d)*r**(h+1)
    def Ar(r): return F(1+r**M,2)
    Hb=Ar(B)-Dr(B)+2*ep
    qg=Ar(G)-Dr(G)-2*ep
    Bs,Bb,Bg=Br(s),Br(B),Br(G)
    Cs,Cb,Cg=Cr(s),Cr(B),Cr(G)
    Hs=Ar(s)-Dr(s)-2*ep
    return Bs*(qg*Cb-Cg*Hb)+Cs*(Bg*Hb-qg*Bb)+Hs*(Cg*Bb-Bg*Cb)

def core_phi(M,s,j):
    h=M//2; U=F(1,2**h); d=1-(h+1)*U
    R=s**j/U; Y=B**j/U; a=F(M-j,M); e=eps(M)/U
    return U/d*(R*(B-G)-Y*(s-G)-8*a*e*(s-G)-4*U*e*R*(B+G)+4*U*e*Y*(s-G))

rows=[]; failures=[]; worst=None
for M in MS:
    for s in SS:
        b=exact_b(M,s); j=b+2; U=F(1,2**(M//2))
        exact=full_phi(M,s,j); core=core_phi(M,s,j)
        err=abs(exact-core)/U
        rec={'M':M,'s':str(s),'b':b,'j':j,'normalized_error':f'{float(err):.18e}','below_1e_26':err<ERRCAP}
        rows.append(rec)
        if worst is None or err>worst[0]: worst=(err,rec)
        if err>=ERRCAP: failures.append(rec)

out={
 'audit':'A114C2_PHI_CORE_EXACT_CROSSCHECK',
 'status':'PASS' if not failures else 'FAIL',
 'method':'Independent exact-Fraction reconstruction of the complete A81 upper boundary and the C2 core. b is found by exact rational binary search; no logarithm or floating sign decision is used.',
 'case_count':len(rows),
 'pass_count':len(rows)-len(failures),
 'error_cap':'1e-26',
 'worst_case':worst[1],
 'failure_count':len(failures),
 'failures':failures,
 'scope_note':'Finite transcription/falsification crosscheck only. Uniform Phi positivity is established by the analytic 15-gate certificate, not by this grid.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','case_count','pass_count','worst_case','failure_count')},indent=2))
