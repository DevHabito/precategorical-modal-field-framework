# A89 — Explicit Uniform Local-Secant Positivity Threshold

**Programme:** Modal Field Research Programme  
**Audit:** A89  
**Author line:** Felipe Gianini Romero  
**Status:** analytic continuum theorem with exact rational majorants and a conservative explicit support threshold  
**Claim boundary:** no minimal-threshold claim, no universal all-\(k\) unimodality theorem, and no physical interpretation

## Technical abstract

A88 reduced the local secant

\[
S_{M,b}(s)=E_{M,b}(s)-E_{M,b+1}(s),
\qquad
b=\lceil M c(s)\rceil,
\]

with

\[
c(s)=\frac{\log 2}{-2\log s},
\]

to an exact nine-term confluent exponential polynomial. It proved positivity in 8,019 rational cells through \(M=900\) and obtained positive parity-leading limits, but it did not give an explicit finite threshold valid for the full continuum of probe values.

A89 supplies that missing step. Under the unchanged local contract

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\qquad
\beta=\frac18,
\qquad
t=\frac12,
\]

it proves

\[
\boxed{
M\ge521
\quad\Longrightarrow\quad
S_{M,\lceil M c(s)\rceil}(s)>0
}
\]

for every real \(s\) in the declared interval.

The proof uses only exact rational inequalities after two endpoint comparisons for \(c(s)\). It decomposes the normalized secant into a positive probe-target term, a negative beta-target term, a target-affine term, and three residual blocks. The final certified lower margin is

\[
\boxed{
S_{M,b}(s)\,[u_M t^b]^{-1}
>
0.00455475149775
}
\]

under deliberately rounded majorants, where

\[
u_M=2^{-\lfloor M/2\rfloor}.
\]

The threshold \(521\) is sufficient for this particular certificate. It is not asserted to be the smallest true threshold.

---

## 1. Question left by A88

A88 established:

1. an exact nine-term formula for \(S_{M,b}(s)\);
2. exact positivity through \(M=900\) on nine rational probes;
3. strict dominance of a four-channel core on those finite cells;
4. positive parity-leading limits.

The unresolved point was quantitative:

> Can the asymptotic positivity be converted into one explicit \(M_0\) that is valid for every real probe in the whole local interval?

A89 answers yes, with

\[
M_0=521.
\]

---

## 2. Exact slope bracketing without logarithmic gates

For \(p/q\ge0\),

\[
c(s)>\frac pq
\iff
2^q s^{2p}>1,
\]

and

\[
c(s)<\frac pq
\iff
2^q s^{2p}<1.
\]

These are integer comparisons when \(s\) is rational. A89 verifies independently that

\[
\frac{16923}{100000}
<
c\!\left(\frac{129}{1000}\right),
\]

and

\[
c\!\left(\frac{133}{1000}\right)
<
\frac{17180}{100000}.
\]

Since \(c(s)\) is strictly increasing on \((0,1)\), these inequalities bracket the slope on the entire interval.

Let

\[
b=\lceil Mc(s)\rceil.
\]

For every \(M\ge521\), they imply

\[
b\ge89,
\]

and

\[
\lambda_M:=\frac{b+1}{M}
<
\frac{17180}{100000}+rac{2}{521}
<
\frac{22}{125}.
\]

They also control the slowly decaying beta-target channel. Since

\[
\frac{\beta^b}{u_M}=2^{\lfloor M/2\rfloor-3b},
\]

and

\[
\left(\frac12-3\frac{16923}{100000}\right)521
=-4.00649,
\]

the integer exponent satisfies

\[
\lfloor M/2\rfloor-3b\le-5.
\]

Therefore

\[
\boxed{
\frac{\beta^b}{u_M}\le\frac1{32}
}
\]

for every \(M\ge521\).

This dyadic step is the main reason the conservative certificate closes at \(521\). At \(M=520\), the same argument gives only \(1/16\).

---

## 3. Uniform control of the \(D\)-block

Write

\[
h=\lfloor M/2\rfloor,
\qquad
u=2^{-h}.
\]

For even supports, the exact block can be written

\[
D_M(r)=-2ur+R_M^{\rm even}(r),
\]

and for odd supports,

\[
D_M(r)=-\frac32ur+R_M^{\rm odd}(r).
\]

For \(h\ge260\) and

\[
\beta\le r\le\frac{133}{1000},
\]

the remainders are bounded by evaluating monotone geometric majorants at \(h=260\). The audit stores the exact rational values of

\[
\frac{|R_M^{\rm even}(r)|}{u},
\qquad
\frac{|R_M^{\rm odd}(r)|}{u}.
\]

The bounds use only the facts that

\[
(2s_{\max})^h,
\quad
h2^{-h},
\quad
(h+1)2^{-h}
\]

are decreasing in the declared tail.

---

## 4. Consequences for the active envelope coefficients

Let

\[
H_\beta
=
\frac{1+\beta^M}{2}-D_M(\beta)+2\varepsilon_M,
\]

\[
H_s
=
\frac{1+s^M}{2}-D_M(s)-2\varepsilon_M.
\]

The exact remainder bounds imply

\[
\boxed{
\frac{49}{100}<H_\beta,H_s<\frac{51}{100}
}
\]

for every \(M\ge521\) and every probe in the interval.

They also give

\[
\boxed{
\frac{|H_\beta-H_s|}{u}<\frac{19}{1000}
}
\]

and, with

\[
A=\frac{1+t^M}{2},
\]

\[
\boxed{
\frac{|A-H_r|}{u}<\frac{27}{100}
\qquad
(r=\beta,s).
}
\]

These constants are intentionally rounded upward. The exact stored bounds are smaller.

---

## 5. Exact normalized secant decomposition

Normalize by

\[
ut^b.
\]

The complete secant separates into six channels:

\[
\frac{S_{M,b}(s)}{ut^b}
=
P_{\beta s}
+P_{\beta t}
+P_{st}
+P_\beta
+P_s
+P_t.
\]

### 5.1 Positive probe-target term

The positive term is

\[
P_{st}
=(1-st)(t-s)H_\beta\frac{s^b}{u}.
\]

Write

\[
\delta=b-Mc(s)\in[0,1).
\]

Then

\[
\frac{s^b}{u}
=
\begin{cases}
s^\delta,&M\text{ even},\\[3pt]
\dfrac{s^\delta}{\sqrt2},&M\text{ odd}.
\end{cases}
\]

Using

\[
s^\delta\ge s\ge\frac{129}{1000},
\qquad
\frac1{\sqrt2}>\frac7{10},
\]

A89 obtains

\[
\boxed{
P_{st}
>
\frac{30317557683}{2000000000000}
=
0.0151587788415.
}
\]

### 5.2 Negative beta-target term

The beta-target contribution is

\[
P_{\beta t}
=(1-\beta t)(\beta-t)H_s\frac{\beta^b}{u}.
\]

Using \(H_s<51/100\) and \(\beta^b/u\le1/32\),

\[
\boxed{
|P_{\beta t}|
<
\frac{459}{81920}
=
0.00560302734375.
}
\]

### 5.3 Target-affine term

Define

\[
a_r=\frac{1-r^M}{M}.
\]

The target-affine contribution reduces exactly to

\[
P_t
=
\frac{
H_\beta-H_s
+(b+1)(H_s a_\beta-H_\beta a_s)
}{4u}.
\]

The inner expression has the useful identity

\[
H_s a_\beta-H_\beta a_s
=
-\frac{H_\beta-H_s}{M}
+
\frac{H_\beta s^M-H_s\beta^M}{M}.
\]

Therefore

\[
|P_t|
\le
\frac14
\left[
\frac{|H_\beta-H_s|}{u}
+
\lambda_M\frac{H_\beta s^M+H_s\beta^M}{u}
\right].
\]

The exact majorant is below

\[
0.00475,
\]

and the rounded certificate uses

\[
\boxed{|P_t|<\frac1{200}=0.005.}
\]

---

## 6. The five-term residual becomes three bounded blocks

After grouping affine pairs, the five nonleading terms reduce to three exact expressions.

### 6.1 Pure \(\beta s\) channel

\[
P_{\beta s}
=(1-\beta s)A(s-\beta)
\frac{(\beta s)^b}{ut^b}.
\]

### 6.2 Beta-affine block

Let

\[
X_\beta=Aa_s-H_s a_t.
\]

Then

\[
P_\beta
=(1-\beta)^2
\left[(b+1)X_\beta-(A-H_s)\right]
\frac{\beta^b}{ut^b}.
\]

### 6.3 Probe-affine block

Let

\[
X_s=Aa_\beta-H_\beta a_t.
\]

Then

\[
P_s
=(1-s)^2
\left[(A-H_\beta)-(b+1)X_s\right]
\frac{s^b}{ut^b}.
\]

Using

\[
b\ge89,
\quad
\frac{b+1}{M}<\frac{22}{125},
\quad
\frac{|A-H_r|}{u}<\frac{27}{100},
\]

together with the geometric factors

\[
(2s)^b,
\qquad
4^{-b},
\]

the sum of these three blocks is bounded by

\[
1.3424096897\ldots\times10^{-52}.
\]

The rounded theorem uses the much weaker but simpler bound

\[
\boxed{
|P_{\beta s}|+|P_\beta|+|P_s|
<10^{-6}.
}
\]

---

## 7. Uniform positive margin

Combining the rounded bounds gives

\[
\frac{S_{M,b}(s)}{ut^b}
>
0.0151587788415
-0.00560302734375
-0.005
-0.000001.
\]

Hence

\[
\boxed{
\frac{S_{M,b}(s)}{ut^b}
>
0.00455475149775
>0.
}
\]

Since \(ut^b>0\),

\[
\boxed{
S_{M,\lceil Mc(s)\rceil}(s)>0
}
\]

for every integer \(M\ge521\) and every real

\[
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

The tighter, unrounded rational budget stored by the audit gives

\[
0.00480575149775\ldots
\]

after normalization.

---

## 8. Why \(521\) is not called optimal

For \(M=520\), the slope lower bound yields only

\[
\frac{\beta^b}{u}\le\frac1{16}.
\]

Under the same deliberately coarse component bounds, the resulting lower margin is negative. At \(M=521\), the integer exponent drops by one and the cap becomes \(1/32\), closing the proof.

This establishes:

> \(521\) is the first support at which this selected dyadic majorant certificate closes.

It does **not** establish:

> the secant is nonpositive at \(M=520\), or \(521\) is the smallest possible threshold under a sharper proof.

The distinction is essential.

---

## 9. Regression checks

The analytic theorem is independent of a finite scan. Nevertheless, the implementation evaluates 45 exact rational regression cells:

\[
M\in\{521,522,625,900,1000\}
\]

at the nine A88 probes. All 45 normalized secants are strictly positive.

These cells test the algebraic decomposition. They are not used as evidence for the continuum theorem.

---

## 10. What A89 proves

A89 proves, under the declared reduced contract:

1. exact endpoint slope brackets by integer arithmetic;
2. a uniform contact lower bound \(b\ge89\);
3. a uniform ratio bound \((b+1)/M<22/125\);
4. uniform control of the parity-dependent \(D\)-block remainder;
5. uniform bounds on \(H_\beta\), \(H_s\), \(H_\beta-H_s\), and \(A-H_r\);
6. an explicit positive normalized secant margin;
7. the continuum theorem
   \[
   M\ge521\Rightarrow S_{M,\lceil Mc(s)\rceil}(s)>0
   \]
   for all declared probes.

---

## 11. What A89 does not prove

A89 does not prove:

1. that \(521\) is the smallest true threshold;
2. positivity outside \([129/1000,133/1000]\);
3. global monotonicity of \(E_{M,k}\) in \(k\), which A87 already falsified;
4. universal one-sign-variation for every \(M\) and every contact;
5. the A86 three-contact strip for all \(M\);
6. a physical meaning for contacts, bands, \(s\), \(q\), or \(\lambda\);
7. any derivation of spacetime, matter, energy, or pre-temporal ontology.

The new result is a precise mathematical closure of one asymptotic gap: the local secant required by the offset classifier is now uniformly positive beyond an explicit finite support threshold on the full local probe interval.
