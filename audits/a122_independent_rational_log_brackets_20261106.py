#!/usr/bin/env python3
"""Independent A122 sign brackets using exact rational logarithm bounds.

This verifies the stated formula at two rational parameter points. It does
not prove that a discrete index subsequence realizes critical resonance.
"""
from fractions import Fraction as F

def log_bracket(x,n=70):
    z=(x-1)/(x+1);a=abs(z);total=F(0);term=a
    for j in range(n):
        total+=2*term/F(2*j+1);term*=a*a
    rem=2*term/(F(2*n+1)*(1-a*a))
    return (-total-rem,-total) if z<0 else (total,total+rem)

def interval_mul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def divide(a,b):
    assert b[0]*b[1]>0
    return interval_mul(a,(1/b[1],1/b[0]))
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def pt(x):return x,x

def omega(s,t):
    ls=log_bracket(s);lt=log_bracket(t)
    c=divide(lt,interval_mul(pt(F(2)),ls))
    G=(s-F(1,8))/t-4*F(1,1875)
    P=(t-s)/2
    Q=interval_mul(pt((1-t)*G),sub(pt(F(1)),c))
    ratio=divide(Q,pt(P));lr=(log_bracket(ratio[0])[0],log_bracket(ratio[1])[1])
    xi=divide(lr,ls)
    return interval_mul(pt(G),add(pt(F(1)),interval_mul(pt(1-t),xi))),xi

if __name__=="__main__":
    for t in (F(131,1000),F(132,1000)):
        O,X=omega(F(129,1000),t)
        print('tau',t,'omega',float(O[0]),float(O[1]),
              'xi',float(X[0]),float(X[1]),
              'certified sign',O[1]<0 or O[0]>0)
