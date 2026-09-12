# A114-B2-A — positive-pivot gamma-plus theorem in the strict compressed `b+2` tail phase

## Status

**PROVED under the frozen analytic-tail contract for the subphase with strict compressed maximizer `b+2` and positive upper-gamma pivot**

\[
\Phi(M,s):=F_{b+2}^{\rm up}(s)>0.
\]

This theorem does **not** classify the complementary region \(\Phi\le0\). In particular, A114-B2 as a complete lifted-architecture classification remains open.

## Contract

Let

\[
M\ge521,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

with the frozen conventions inherited from A112/A113:

\[
\beta=\frac18,
\qquad
\gamma=\frac1{16},
\qquad
\tau=\frac12,
\qquad
h=\lfloor M/2\rfloor,
\]

and the parity-dependent normalized tolerance used throughout the analytic-tail package.

Define

\[
c(s)=\frac{\log2}{-2\log s},
\qquad
b=\lceil Mc(s)\rceil.
\]

Assume the compressed objective has strict maximizer

\[
\boxed{j=b+2}.
\]

By A113 one-variation this is equivalently the central sign pattern

\[
E_{b+1}>0>E_{b+2}.
\]

Finally assume

\[
\boxed{\Phi(M,s)=F_{b+2}^{\rm up}(s)>0}.
\]

## The lifted candidate

Take the gamma-plus adjacent basis at the same contact

\[
P=\{0,b+2,b+3,M\},
\qquad
Q=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,
\qquad
\beta-,
\qquad
\gamma+.
\]

## Theorem

Under the contract and assumptions above, this basis satisfies every strict KKT condition of the full declared finite lifted LP. Consequently it is the unique strict global basic optimum.

In compact form,

\[
\boxed{
\text{strict compressed }b+2\text{ maximum and }F_{b+2}^{\rm up}>0
\Longrightarrow
\text{unique strict gamma-plus lift at contact }b+2.
}
\]

## Proof

### 1. Determinant orientation is already independent of primal positivity

A114-B1 repaired the only circularity that would otherwise prevent a sufficient Cramer sign test. On the complete A112 localization strip \(j=b+1\) or \(j=b+2\), the reduced gamma-plus determinant obeys

\[
D_G=\det(C)A(s).
\]

A110 gives the generalized-Vandermonde orientation

\[
\det(C)<0,
\]

and A112-G gives, before any adjacent-primal positivity is assumed,

\[
A(s)<0.
\]

Therefore

\[
\boxed{D_G>0}
\]

uniformly on the whole tail localization strip.

This step is crucial: no implication proved under \(p_j,p_{j+1}>0\) is reversed here.

### 2. Exact Cramer bridge at contact `j=b+2`

A112-A proves the exact identities

\[
p_{j+1}=\frac{F_j^{\rm up}}{D_G},
\qquad
p_j=-\frac{F_{j+1}^{\rm up}}{D_G}.
\]

Set \(j=b+2\). Then

\[
p_{b+3}=\frac{F_{b+2}^{\rm up}}{D_G}
=\frac{\Phi}{D_G}>0.
\]

The A112-A uniform upper-boundary barrier gives

\[
F_k^{\rm up}<0\qquad(k\ge b+3),
\]

so in particular

\[
p_{b+2}=-\frac{F_{b+3}^{\rm up}}{D_G}>0.
\]

Hence the two adjacent P masses required by the A112 gamma-plus composition are strictly positive.

### 3. The compressed sign required by the active gamma dual is exactly available

Because `b+2` is the strict compressed maximizer, A113 gives

\[
E_{b+2}<0.
\]

The A112 logical composition audit identifies A112-D as the only KKT-closure step that uses a compressed-factor sign. Its exact identity is

\[
N_\gamma=-\frac{\det B}{D_G}E_j.
\]

At \(j=b+2\), adjacent positivity plus the A112-B determinant-orientation transfer yields \(\det B/D_G>0\), while \(E_{b+2}<0\). Thus

\[
y_\gamma>0.
\]

The existing active-dual ordering then gives

\[
y_\alpha>0,
\qquad
y_\beta>0,
\qquad
y_\gamma>0.
\]

No sign of \(E_{b+1}\) is used to prove this candidate; the fact that \(E_{b+1}>0\) merely explains why the neighboring contact-`b+1` gamma-plus basis can fail its gamma dual in the difficult B2 regime.

### 4. Full strict KKT closure is inherited from A112

With

\[
p_{b+2}>0,
\qquad
p_{b+3}>0,
\qquad
E_{b+2}<0,
\]

all hypotheses of the proved A112 gamma-plus composition at fixed contact \(j=b+2\) hold.

Therefore:

- the remaining basic masses are strictly positive;
- \(t>0\);
- every active multiplier is strictly positive;
- every nonbasic P reduced cost is strictly positive;
- every nonbasic Q reduced cost is strictly positive;
- every opposite inactive band slack is strictly positive.

Thus the complete strict KKT system holds.

### 5. Globality and uniqueness

The KKT system scanned by A112 is the full declared finite LP, not a restricted comparison among gamma-plus candidates. Strict feasibility of all basic variables, strict active multipliers, strict inactive slacks and strict reduced costs therefore certifies a unique strict global basic optimum.

No enumeration of two-band, q0/q1, gamma-minus or endpoint-released alternatives is required on the \(\Phi>0\) subphase: a distinct competing optimum would contradict the strict full-LP KKT certificate.

## Equality and negative-pivot boundary

This theorem deliberately assumes

\[
\Phi>0.
\]

At

\[
\Phi=0,
\]

the contact-`b+2` gamma-plus basis has

\[
p_{b+3}=0,
\]

so strictness is lost. A114-B2-A makes no claim about which degenerate or alternative architecture represents the global optimum on that pivot set.

For

\[
\Phi<0,
\]

the same gamma-plus contact has \(p_{b+3}<0\) and is primal-infeasible. A114-B2-W1 already proves that the complementary regime can require a genuinely different architecture: at \(M=521,s=129/1000\), the strict optimum is q0/q1 with gamma-minus active.

Neither fact proves a universal classifier for the \(\Phi\le0\) region.

## Independent exact controls

The standalone A114-B2-A cross-check recomputes the full gamma-plus KKT system directly, without importing the analytic theorem certificate.

Positive-pivot controls include both parities:

- \(M=522,s=129/1000\): strict compressed `b+2`, \(\Phi>0\), contact `b+2` passes \(1053/1053\) strict KKT conditions;
- \(M=523,s=132/1000\): strict compressed `b+2`, \(\Phi>0\), contact `b+2` passes \(1055/1055\) strict KKT conditions;
- \(M=521,s=131/1000\): strict compressed `b+2`, \(\Phi>0\), contact `b+2` passes \(1051/1051\).

A premise-negative control is retained:

- \(M=521,s=129/1000\): strict compressed `b+2` but \(\Phi<0\); the contact-`b+2` gamma-plus basis is rejected exactly through a negative adjacent basic mass.

These finite controls are replication checks only. They are not the all-\(M\) proof.

## A102 historical consistency check

An exact rational census of all 444 A102 `unique_b_plus_2` witnesses gives:

- \(404\) with \(\Phi>0\), all \(404\) classified as legacy gamma-plus;
- \(40\) with \(\Phi<0\), none classified as legacy gamma-plus;
- no zero-\(\Phi\) rational witness in the frozen A102 witness set.

The 40 negative-pivot witnesses split across several architecture classes, so the census explicitly argues **against** promoting a one-family rule on \(\Phi<0\).

A102 is finite and ends at \(M=520\). This consistency check is not used to prove the analytic-tail theorem.

## Claim boundary

### PROVED

\[
\boxed{
M\ge521,
\ s\in[129/1000,133/1000],
\ j_{\max}=b+2\text{ strict},
\ F_{b+2}^{\rm up}>0
\Rightarrow
\text{unique strict gamma-plus lift at }b+2.
}
\]

### NOT PROVED HERE

- the architecture on \(F_{b+2}^{\rm up}=0\);
- a complete classification of \(F_{b+2}^{\rm up}<0\);
- `Phi<0 => q0/q1 gamma-minus` for all tail points;
- that \(F_{b+2}^{\rm up}\) alone classifies every architecture in A114-B2;
- any statement outside the frozen source window;
- any physical interpretation.

## Scientific status after A114-B2-A

A114-B2 is now partitioned into:

1. **positive pivot \(\Phi>0\): CLOSED by A114-B2-A**;
2. **zero pivot \(\Phi=0\): OPEN**;
3. **negative pivot \(\Phi<0\): OPEN globally**, with A114-B2-W1 providing one exact q0/q1 gamma-minus tail witness.

The next genuine research target is therefore the nonpositive-pivot region, especially the architecture transitions inside \(\Phi<0\).
