#!/usr/bin/env python3
"""Independent exact rational controls of the primal three-site bridge.

The tests cover normalization, mean, mass nonnegativity, transform
decomposition and the linear-fractional scaling. They do not attempt
to prove the additional bilateral transform bands or LP optimality.
"""
from fractions import Fraction as F

def weights(M,k,t,z):
    p0=t/2-F(M-k,M)*z
    pM=t/2-F(k,M)*z
    return {0:p0,k:z,M:pM}

def tr(w,r):
    return sum((v*r**x for x,v in w.items()),F(0))

def main():
    checked=0
    for M in range(4,65):
        for k in range(1,M):
            zmax=min(F(M,2*(M-k)),F(M,2*k))
            for z in (F(0),zmax/2,zmax,zmax+F(1,1000),-F(1,1000)):
                w=weights(M,k,F(1),z)
                assert sum(w.values())==1
                assert sum(x*v for x,v in w.items())==F(M,2)
                nonnegative=all(v>=0 for v in w.values())
                assert nonnegative==(0<=z<=zmax)
                for r in (F(1,8),F(1,3),F(1,2)):
                    B=r**k-F(M-k,M)-F(k,M)*r**M
                    assert tr(w,r)==(1+r**M)/2+z*B
                    checked+=1
    ratio_count=0
    for M in range(4,65):
        for k in range(1,M):
            j=M-k
            z=min(F(M,2*(M-k)),F(M,2*k))/3
            v=min(F(M,2*(M-j)),F(M,2*j))/4
            mu=weights(M,k,F(1),z)
            nu=weights(M,j,F(1),v)
            tau=F(1,3)
            Gnu=tr(nu,tau)
            assert Gnu>0
            t=1/Gnu
            p={x:t*val for x,val in mu.items()}
            q={x:t*val for x,val in nu.items()}
            assert tr(q,tau)==1
            assert tr(p,tau)==tr(mu,tau)/Gnu
            assert sum(p.values())==sum(q.values())==t
            ratio_count+=1
    print(f"PASS: {checked} exact three-site moment, mass and basis checks; {ratio_count} exact ratio-homogenization checks")
if __name__=="__main__":
    main()
