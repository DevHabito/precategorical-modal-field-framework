# Exact Global Continuous Phase Theorems

**Programme:** Modal Field Research Programme  
**Provisional audit:** A66  
**Author line:** Felipe Gianini Romero  
**Status:** exact global continuous theorem for two fixed completions; no all-contract theorem

## Technical abstract

A65 supplied exact positive right derivatives at the boundary for most
contracts and found no reversal in 30,960 continuous-grid evaluations.
That result was still local plus computational.

A66 removes the grid from the proof for two strategically chosen contracts:

1. the original canonical noisy contract;
2. one of the seven-variable degenerate contracts that A65 could not treat
   with its eight-variable local basis theorem.

For the canonical contract,

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52,
\]

with target exponent \(1\), tolerance

\[
\varepsilon=10^{-4},
\]

and fixed completion

\[
D_\alpha=\{\alpha,3,10\},
\qquad
2\le\alpha<3,
\]

the exact minimax ratio is a continuous union of seven rational branches in

\[
s=2^{-\alpha}.
\]

Six phase transitions are unique simple roots of explicit integer
polynomials. On every phase:

- all basic primal variables are nonnegative;
- all active inequality multipliers are nonnegative;
- all nonbasic reduced costs are nonnegative;
- all inactive error-band inequalities are satisfied;
- all denominators remain nonzero;
- the exact derivative factor
  \[
  \kappa(s)=-s\frac{d\rho}{ds}
  \]
  is strictly positive.

Adjacent rational value branches agree exactly at each transition.
Consequently,

\[
\boxed{
\frac{d\rho}{d\alpha}>0
\quad\text{for every }2\le\alpha<3.
}
\]

Therefore

\[
\boxed{
\alpha^\star=2
}
\]

is the unique global minimizer of the first anchor for the fixed completion
\(\{\alpha,3,10\}\).

The future-score risk increases from

\[
0.0097681452113756748881978026104657257056548058426406
\]

at the boundary to the coalescence limit

\[
0.089066653294909667174066303390545901413652444911754
\]

as \(\alpha\to3^-\). The limiting risk is approximately

\[
9.118072199744
\]

times the boundary risk.

The second theorem uses

\[
\mathbb E[X]=\frac54,
\qquad
\mu=3,
\qquad
\varepsilon=\frac1{19200},
\]

and

\[
D_\alpha=\{\alpha,5,7\},
\qquad
4\le\alpha<5.
\]

This contract was degenerate at the A65 boundary: it had seven positive
Charnes–Cooper variables and only two active observation inequalities.

A66 finds that one seven-variable rational branch remains primal–dual optimal
on the entire interval and satisfies

\[
\boxed{
\frac{d\rho}{d\alpha}>0
\quad\text{for every }4\le\alpha<5.
}
\]

Thus

\[
\boxed{
\alpha^\star=4
}
\]

is also the unique global first-anchor optimum for this fixed completion.

This resolves a genuine A65 degeneracy rather than deleting it by
perturbation.

---

## 1. Exact certification method

For a fixed active phase, write the Charnes–Cooper equations as

\[
B(s)z(s)=b.
\]

Because the first transform row is

\[
(1,s,s^2,\ldots,s^5),
\]

all entries of \(B(s)\) are polynomials or rational constants. Hence

\[
z(s)=B(s)^{-1}b
\]

and the minimax value

\[
\rho(s)=c^\top z(s)
\]

are rational functions of \(s\).

The dual vector is

\[
y(s)=B(s)^{-\top}c_B.
\]

For each phase, A66 checks the signs of:

\[
z_B(s),
\]

\[
y_{\mathrm{active}}(s),
\]

\[
A^\top y(s)-c,
\]

and every inactive observation slack.

Each sign condition is reduced to a rational function. Its numerator and
denominator roots are isolated exactly by rational intervals. The certificate
then verifies:

1. no numerator or denominator root lies inside the declared phase;
2. no denominator vanishes at a transition;
3. one exact rational sample inside the phase has the required sign.

Since a rational function cannot change sign without crossing a zero or a
pole, the sign holds throughout the entire phase.

The derivative is treated identically through

\[
\kappa(s)=-s\rho'(s).
\]

No finite-difference or grid argument is used in the phase proof.

---

## 2. Canonical phase atlas

The canonical domain is

\[
s\in\left(\frac18,\frac14\right],
\]

which corresponds to

\[
\alpha\in[2,3).
\]

| Phase | \(\alpha\)-interval | Active \(P\)-support | Active \(Q\)-support | Active bands |
|---:|---:|---:|---:|---|
| 1 | [2.000000000000, 2.274386321248] | [0, 1, 3, 5] | [1, 2, 4] | alpha+, beta-, gamma+ |
| 2 | [2.274386321248, 2.648586886262] | [0, 2, 3, 5] | [1, 2, 4] | alpha+, beta-, gamma+ |
| 3 | [2.648586886262, 2.876330478845] | [0, 2, 5] | [1, 2, 3, 4] | alpha+, beta-, gamma+ |
| 4 | [2.876330478845, 2.908567843187] | [0, 1, 2, 5] | [1, 2, 3] | alpha+, beta-, gamma+ |
| 5 | [2.908567843187, 2.911461258358] | [0, 1, 2, 5] | [1, 3] | alpha+, beta- |
| 6 | [2.911461258358, 2.912942078443] | [1, 2, 5] | [0, 1, 3] | alpha+, beta- |
| 7 | [2.912942078443, 3.000000000000] | [1, 2, 5] | [0, 1, 3] | alpha+, gamma- |

The first four phases have three active observation bands.
In phases 5 and 6, the \(\gamma=10\) band becomes inactive.
In phase 7, the \(\beta=3\) band is inactive and the negative
\(\gamma=10\) band becomes active.

The phase changes are genuine changes of the primal or dual active structure,
not arbitrary subdivisions.

---

## 3. Exact transition points

| Transition | \(\alpha\) | \(s\) | Trigger |
|---:|---:|---:|---|
| 1→2 | 2.274386321247813 | 0.206700484963703 | `reduced_cost_2` / `reduced_cost_1` |
| 2→3 | 2.648586886262090 | 0.159476208214847 | `basic_3` / `basic_9` |
| 3→4 | 2.876330478844989 | 0.136187813845444 | `basic_10` / `basic_1` |
| 4→5 | 2.908567843186568 | 0.133178412813844 | `basic_8` / `inactive_slack_gamma_+1` |
| 5→6 | 2.911461258357643 | 0.132911582835783 | `basic_0` / `basic_6` |
| 6→7 | 2.912942078443073 | 0.132775228886563 | `inactive_slack_gamma_-1` / `inactive_slack_beta_-1` |

The transition values are algebraic in \(s\). Their displayed \(\alpha\)
coordinates are numerical values of

\[
-\log_2s.
\]

At every transition:

- the relevant transition polynomial has one simple root in its exact
  rational isolating interval;
- the adjacent value difference has that transition polynomial as a factor;
- the two rational branches therefore agree at the transition;
- neither branch denominator vanishes there.

Thus the seven pieces join continuously.

---

## 4. Transition polynomials

### $T_1$

\[
929784437276336 s^{4} - 2495955329401486 s^{3} + 2290811108027383 s^{2} - 814144850536196 s + 90754286658276=0.
\]

The relevant root is uniquely isolated in

\[
\left[2625591/12702394,\;3502024/16942505\right].
\]

### $T_2$

\[
1135150378646781824 s^{4} - 1755571467890751488 s^{3} - 1714425261612062 s^{2} + 730905407330461244 s - 110132228840229597=0.
\]

The relevant root is uniquely isolated in

\[
\left[2447508/15347167,\;3437299/21553679\right].
\]

### $T_3$

\[
66742936414437376 s^{4} + 65178648842224 s^{3} - 219584937996775582 s^{2} + 172082763261113708 s - 19386030909542541=0.
\]

The relevant root is uniquely isolated in

\[
\left[2754144/20223131,\;3219347/23639024\right].
\]

### $T_4$

\[
99536337724743680 s^{4} + 97203454809320 s^{3} - 326877094348350445 s^{2} + 255404565182019874 s - 28248264471173857=0.
\]

The relevant root is uniquely isolated in

\[
\left[319391/2398219,\;21202393/159202926\right].
\]

### $T_5$

\[
1066112 s^{5} - 3491250 s^{3} + 2718052 s^{2} - 292914 s - 931=0.
\]

The relevant root is uniquely isolated in

\[
\left[2721131/20473242,\;2858071/21503551\right].
\]

### $T_6$

\[
644914736407773184 s^{5} - 2108767625497805536 s^{3} + 1637481634193964764 s^{2} - 173234073933378840 s - 956956581196913=0.
\]

The relevant root is uniquely isolated in

\[
\left[4433149/33388374,\;420059/3163685\right].
\]

---

## 5. Canonical global theorem

### Theorem 5.1

For the six-state contract with mean \(5/2\), target exponent \(1\),
absolute tolerance \(10^{-4}\), and fixed anchors \(3\) and \(10\), define

\[
\rho(\alpha)
=
\mathcal R_{\mathrm{ratio}}
\bigl(\{\alpha,3,10\}\bigr).
\]

Then \(\rho(\alpha)\) is continuous on \([2,3)\) and strictly increasing.

Therefore

\[
\boxed{
\arg\min_{2\le\alpha<3}\rho(\alpha)=\{2\}.
}
\]

Because the logarithm is strictly increasing, the same statement holds for

\[
Q(\alpha)=\frac12\log_2\rho(\alpha).
\]

### Boundary value

At \(\alpha=2\), the exact ratio is

\[
\boxed{
\rho(2)
=
2263558795360587104/2233113362221566575.
}
\]

This reproduces the A49 finite-catalogue winner \(\{2,3,10\}\).

### Coalescence limit

As \(\alpha\to3^-\), the branch limit is

\[
\boxed{
\rho(3^-)
=
441938162655374364239/390605214984835914470.
}
\]

This is a one-sided limit. At \(\alpha=3\), the first two observations
coalesce and the constraint rank changes, so the duplicate-anchor problem is
a different optimization contract.

---

## 6. Degenerate global theorem

Consider

\[
\operatorname{supp}P\subseteq\{0,\ldots,5\},
\qquad
\mathbb E[X]=\frac54,
\]

target exponent \(3\), normalized error

\[
\delta=\frac1{1875},
\]

and absolute tolerance

\[
\varepsilon=\frac1{19200}.
\]

For

\[
D_\alpha=\{\alpha,5,7\},
\qquad
4\le\alpha<5,
\]

the active supports are fixed throughout:

\[
\operatorname{supp}P=\{1,2,5\},
\]

\[
\operatorname{supp}Q=\{0,1,3\}.
\]

Only the positive \(\alpha\) band and the negative \(\gamma=7\) band are
active. The \(\beta=5\) band remains inactive.

The exact ratio is

\[
\rho(s)
=
256*(127339100160000*s**5 + 49269657872557*s**3 - 611237629135200*s**2 + 437970783852729*s - 3299462238213)/(36356633651052544*s**5 + 367219704268800*s**3 - 147019732592001376*s**2 + 111154637815933632*s - 858094746758687).
\]

Its exact derivative factor is

\[
\kappa(s)
=
5498989859010964736*s*(s - 1)*(162428549595136*s**6 - 326553595019264*s**5 + 2827493048320*s**4 + 327109272750432*s**3 - 167826786540576*s**2 + 3247495011357*s - 422240110947)/(36356633651052544*s**5 + 367219704268800*s**3 - 147019732592001376*s**2 + 111154637815933632*s - 858094746758687)**2.
\]

All primal, dual, reduced-cost, slack, denominator, and derivative signs hold
on

\[
s\in\left(\frac1{32},\frac1{16}\right].
\]

Therefore

\[
\boxed{
\frac{d\rho}{d\alpha}>0
\quad\text{for }4\le\alpha<5.
}
\]

The exact boundary ratio is

\[
\boxed{
\rho(4)
=
1813793639768317/1800783220223842.
}
\]

This is the same rational ratio that A64 found in the exact tie between
\(\{4,5,7\}\) and \(\{4,7,12\}\).

The tie at the boundary does not persist when the first anchor moves:
the fixed completion \(\{\alpha,5,7\}\) worsens strictly for every
\(\alpha>4\).

---

## 7. What A66 changes

Before A66, the evidence hierarchy was:

\[
\text{integer atlas}
\rightarrow
\text{local derivatives}
\rightarrow
\text{dense continuous grid}.
\]

A66 adds:

\[
\boxed{
\text{exact global continuous phase theorem}.
}
\]

For the canonical contract, this means the first-boundary law is no longer a
catalogue artifact or a numerical-grid observation.

The result also shows why a single derivative calculation was insufficient:
the canonical value function changes active structure six times before
coalescence. Global proof requires controlling every phase and every junction.

---

## 8. Logical status

### Established exactly

1. Seven complete canonical primal–dual phases.
2. Six simple algebraic transition roots.
3. Exact sign control of all primal variables, dual multipliers, reduced
   costs, inactive slacks, and denominators.
4. Strictly positive derivative on every canonical phase.
5. Exact continuity at all six transitions.
6. Unique global first-anchor optimum \(\alpha=2\) for
   \(\{\alpha,3,10\}\).
7. A single global seven-variable phase for the degenerate contract.
8. Unique global first-anchor optimum \(\alpha=4\) for
   \(\{\alpha,5,7\}\).

### Not established

1. A global theorem for all 240 A65 contracts.
2. Monotonicity for every possible fixed pair \((\beta,\gamma)\).
3. A theorem when \(\beta\) and \(\gamma\) are reoptimized as \(\alpha\)
   changes.
4. Arbitrary support sizes and means.
5. Continuous microscopic supports.
6. A universal physical interpretation of the anchor coordinates.

---

## 9. Next rigorous target

The phase machinery now works.

The next step should test whether it can be made uniform across a family
rather than repeated contract by contract.

A controlled target is the central-mean family

\[
M\in\{5,6,7,8,9\},
\qquad
m=\frac M2,
\qquad
\mu=1,
\qquad
\delta=\frac1{1875},
\]

using each A64 optimal completion.

For each \(M\), the task is:

1. enumerate all exact active phases;
2. isolate every transition polynomial;
3. certify derivative positivity;
4. search for a common sign structure or a parameterized determinant
   identity.

That would show whether the canonical theorem is one isolated success or the
first member of a support-size theorem.
