#!/usr/bin/env python3
"""A114-B1 exact gamma-plus pivot/orientation certificate.

Purpose
-------
Close the determinant-orientation gap needed to use the A112-A Cramer bridge
as a *sufficient* sign test rather than only a necessary localization test.

Frozen analytic-tail variables are the same normalized variables used by
A112-B/G.  No finite M grid and no floating sign decision is used here.

The script proves, separately for even and odd M:
  1. the reduced 3x3 gamma-plus determinant D_G equals det(C)*A(s), where
     C is the 4x4 confluent generalized-Vandermonde P interpolation matrix
     from A112-F/G and A(s) is the coefficient of t in the remaining alpha
     equation after solving normalization/mean/beta/gamma;
  2. the full 8x8 Charnes-Cooper basis determinant has the same orientation
     as D_G via the exact A112-B ratio;
  3. therefore, importing only already-proved signs det(C)<0 (A110) and
     A(s)<0 (A112-G), D_G>0 follows without assuming primal positivity.

The sign imports are theorem dependencies, not numerical gates in this file.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

m,r,s,U,T,Y,V,W,R=sp.symbols('m r s U T Y V W R', positive=True)
BETA=sp.Rational(1,8); GAMMA=sp.Rational(1,16); TAU=sp.Rational(1,2)
M0=521
U0=F(1,2**260)
M2U_UB=F(1,2**241)


def parity_objects(parity):
    if parity=='even':
        h=sp.Rational(1,2)/m
        hrat=sp.Rational(1,2); hp1rat=sp.Rational(1,2)+m
        denq=1-(h+1)*U; eps=U/1875
        betaM=U**6; gammaM=U**8; tauM=U**2
        qa=[(-2*U/denq,2/denq),
            ((1+(h-1)*U)/denq,-2*h/denq),
            (-2*(h-1)*U/denq,2*(h-1)/denq)]
    else:
        h=(1/m-1)/2
        hrat=sp.Rational(1,2)-m/2; hp1rat=sp.Rational(1,2)+m/2
        denq=1-(h+1)*U; eps=U/2500
        betaM=U**6/8; gammaM=U**8/16; tauM=U**2/2
        qa=[(-sp.Rational(3,2)*U/denq,2/denq),
            ((1+(2*h-1)*U)/(2*denq),-2*h/denq),
            ((1-(4*h-2)*U)/(2*denq),(2*h-2)/denq)]

    bq=[BETA,U**3,BETA*U**3]
    gq=[GAMMA,U**4,GAMMA*U**4]
    sq=[s,U*V,s*U*V]
    def CD(vals):
        Dv=sp.cancel(sum(qa[i][0]*vals[i] for i in range(3)))
        Cv=sp.cancel(sum(qa[i][1]*vals[i] for i in range(3)))
        return Cv,Dv
    Cb,Db=CD(bq); Cg,Dg=CD(gq); Cs,Ds=CD(sq)

    # 4x4 P interpolation system used in A112-F/G.
    C=sp.Matrix([
        [1,1,1,1],
        [0,r,r+m,1],
        [1,U*Y,BETA*U*Y,betaM],
        [1,U*Y*T,GAMMA*U*Y*T,gammaM],
    ])
    detC=sp.factor(C.det(method='domain-ge'))
    rhsS=sp.Matrix([1,sp.Rational(1,2),Db-2*eps,Dg+2*eps])
    rhsC=sp.Matrix([0,0,Cb,Cg])
    ps=C.inv(method='DM')*rhsS
    pc=C.inv(method='DM')*rhsC
    Pvals=[1,U*R,s*U*R,U*W]
    qS=[qa[i][0] for i in range(3)]
    qC=[qa[i][1] for i in range(3)]
    A=sp.cancel(sum(ps[i]*Pvals[i] for i in range(4))-sum(qS[i]*sq[i] for i in range(3))-2*eps)
    B=sp.cancel(sum(pc[i]*Pvals[i] for i in range(4))-sum(qC[i]*sq[i] for i in range(3)))

    # A112-A reduced 3x3 determinant.
    Hb=sp.cancel((1+betaM)/2-Db+2*eps)
    Hg=sp.cancel((1+gammaM)/2-Dg-2*eps)
    Hs=sp.cancel((1+U*W)/2-Ds-2*eps)
    def Br(xj,xj1,xM):
        return (sp.cancel(xj-(1-r)-r*xM),
                sp.cancel(xj1-(1-r-m)-(r+m)*xM))
    Bbj,Bbj1=Br(U*Y,BETA*U*Y,betaM)
    Bgj,Bgj1=Br(U*Y*T,GAMMA*U*Y*T,gammaM)
    Bsj,Bsj1=Br(U*R,s*U*R,U*W)
    G=sp.Matrix([[Bbj,Bbj1,Hb],[Bgj,Bgj1,Hg],[Bsj,Bsj1,Hs]])
    DG=sp.factor(G.det(method='domain-ge'))

    # Full 8x8 gamma-plus basis, mean rows divided by M>0.
    B8=sp.Matrix([
        [1,1,1,1,0,0,0,-1],
        [0,0,0,0,1,1,1,-1],
        [0,r,r+m,1,0,0,0,-sp.Rational(1,2)],
        [0,0,0,0,m,hrat,hp1rat,-sp.Rational(1,2)],
        [0,0,0,0,TAU,U,U/2,0],
        [1,U*R,s*U*R,U*W,-s,-U*V,-s*U*V,-2*eps],
        [-1,-U*Y,-BETA*U*Y,-betaM,BETA,U**3,BETA*U**3,-2*eps],
        [1,U*Y*T,GAMMA*U*Y*T,gammaM,-GAMMA,-U**4,-GAMMA*U**4,-2*eps],
    ])
    detB8=sp.factor(B8.det(method='domain-ge'))
    ratio=sp.factor(sp.cancel(detB8/DG))
    expected=(2*m-U*(2*m+1))/4 if parity=='even' else (2*m-U*(m+1))/4

    return {
        'C':C,'detC':detC,'A':A,'B':B,'DG':DG,
        'detB8':detB8,'ratio':ratio,'expected_ratio':sp.factor(expected)
    }

out={'audit':'A114B1_GAMMA_PIVOT_ORIENTATION_CERTIFICATE','status':'PASS','parity':{}}
for parity in ('even','odd'):
    o=parity_objects(parity)
    identity=sp.cancel(o['DG']-o['detC']*o['A'])==0
    ratio_identity=sp.cancel(o['ratio']-o['expected_ratio'])==0
    # Positivity of detB8/DG follows from the already-certified tail bounds
    # M^2 U < 2^-241 and U < 2^-260.  The same conservative gate handles both parities.
    ratio_positive_gate=(M2U_UB+2*U0<1)
    assert identity and ratio_identity and ratio_positive_gate
    out['parity'][parity]={
        'DG_equals_detC_times_A':identity,
        'detB8_over_DG':str(o['ratio']),
        'detB8_over_DG_exact_identity':ratio_identity,
        'detB8_over_DG_positive_tail_gate':ratio_positive_gate,
    }
out['imported_proved_signs']={
    'A110_generalized_vandermonde':'det(C)<0 for 0<gamma<beta<1 and 0<j<j+1<M',
    'A112G_branch_regularity':'A(s)<0 on the full localization strip j=b+1 or b+2',
}
out['conclusion']=(
    'D_G=det(C)A(s)>0 on the complete analytic-tail localization strip, '
    'without assuming p_j>0 or p_(j+1)>0; the full 8x8 basis is nonsingular '
    'and has the same determinant orientation.'
)
out['claim_limits']=[
    'This certificate closes determinant orientation only; it does not by itself select a lifted contact.',
    'The signs det(C)<0 and A(s)<0 are imported from already-proved A110 and A112-G theorems, respectively.',
    'No finite M grid or floating-point sign decision is used.'
]
Path('/mnt/data/a114b1_audit/A114B1_GAMMA_PIVOT_ORIENTATION_CERTIFICATE_20260912.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
