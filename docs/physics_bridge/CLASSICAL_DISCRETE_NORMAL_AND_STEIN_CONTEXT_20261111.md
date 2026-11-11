# Classical identification of the stationary law and generator context

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Purpose:** prevent the physical bridge from claiming novelty for classical discrete-normal or Stein-generator structure

## 1. Stationary law in discrete-normal form

Under the paper's time-averaged-rate approximation, the stationary family is

$$
\pi_N
\propto
\exp[-a(N-\nu)^2],
\qquad
N\in\mathbb Z,
$$

with

$$
a=\beta E_{\rm C}>0,
\qquad
c=2a.
$$

Expand the exponent:

$$
-a(N-\nu)^2
=
-aN^2+2a\nu N-a\nu^2.
$$

Ignoring the \(N\)-independent normalization factor, define

$$
q=e^{-2a}=e^{-c},
$$

and

$$
\theta=e^{2a\nu-a}=e^{c(\nu-1/2)}.
$$

Then

$$
\boxed{
\pi_N
\propto
\theta^N q^{N(N-1)/2}.
}
$$

This is the standard two-parameter discrete-normal form used in the probability literature on integer support.

Therefore the stationary distribution itself is not a project novelty.

## 2. Detailed-balance ratio

The discrete-normal ratio is

$$
\frac{\pi_{N+1}}{\pi_N}
=
\theta q^N.
$$

For the published birth-death model,

$$
b_N=\Gamma^+,
$$

and

$$
d_{N+1}
=
\Gamma_0e^{-\beta E_{\rm C}}e^{c(N+1)}.
$$

Hence

$$
\frac{b_N}{d_{N+1}}
=
\frac{\Gamma^+}{\Gamma_0}
e^{-c(N+1/2)}.
$$

Using

$$
\nu=\frac{\log(\Gamma^+/\Gamma_0)}{c},
$$

this becomes

$$
\frac{b_N}{d_{N+1}}
=
e^{c(\nu-1/2)}e^{-cN}
=
\theta q^N.
$$

Thus the stationary law of the averaged-rate coarse-grained model follows directly from ordinary birth-death detailed balance.

## 3. Stein-generator context

For a target discrete distribution \(\pi\), any birth-death rates satisfying

$$
\pi_N b_N
=
\pi_{N+1}d_{N+1}
$$

define a reversible Markov generator with invariant law \(\pi\).

The generator approach to Stein's method uses precisely this kind of Markov operator to characterize a target distribution through identities of the form

$$
\mathbb E_\pi[\mathcal L f]=0.
$$

Therefore the fact that the Salhani-model generator is adapted to its discrete-normal stationary law belongs to established probability theory.

The physical bridge should not claim novelty for:

- the existence of a reversible birth-death generator for a discrete-normal law;
- the stationary detailed-balance recurrence;
- the use of the generator as a distribution-characterizing operator;
- exponential tilting properties of the discrete normal.

## 4. Nearby q-birth-death literature

Exactly solvable q-birth-death models provide a second strong prior.

A particularly relevant neighboring example is the alternative q-Charlier process, whose standard exactly solvable parametrization includes:

$$
B(x)=a,
$$

and

$$
D(x)=q^{-x}-1,
$$

with a natural sinusoidal coordinate

$$
\eta(x)=1-q^x.
$$

The Salhani-model rate is not the same:

$$
D_{\rm Salhani}(N)\propto q^{-N},
$$

without the subtractive constant.

So the processes are not being identified.

However, the comparison shows that:

- constant birth with exponentially growing death is not a new structural motif;
- q-adapted observables such as \(q^N\) already play a central role in exactly solvable birth-death theory;
- an affine function of \(q^N\) appearing as a useful eigen-observable has a close classical analogue.

This substantially narrows any defensible novelty claim for the physical bridge.

## 5. What remains project-specific

After this classical identification, the strongest project-specific mathematical statement currently retained is:

> For the exact exponential-death generator used in the 2026 multi-electron model, finite invariant subspaces built from finitely many pure exponentials \(N\mapsto e^{-\alpha N}\) are classified by the commensurability condition \(\lambda/c\in\mathbb N\), with minimal ladder \(0,c,\ldots,\lambda\).

A second project-specific comparison is:

> In that same generator, the ordinary mean is non-autonomous over unrestricted distributions, while the physically matched transform at \(\lambda=c\) is exactly scalar-autonomous.

Both statements are elementary once the generator is written. Their absolute priority is not established.

## 6. Novelty wording after this audit

Allowed wording:

**Exact model-specific closure classification and observable comparison, positioned inside classical discrete-normal, Stein-generator, q-birth-death, and generating-function theory. Priority not certified.**

Forbidden wording:

- new discrete Gaussian;
- new Stein operator;
- first exact birth-death closure;
- new stochastic-thermodynamic law;
- experimentally discovered fundamental observable.

## 7. Literature anchors

The literature map should include, at minimum:

- Adrienne W. Kemp (1997), discrete-normal characterizations;
- survey literature on discrete analogues of the Gaussian;
- Stein's method for discrete distributions and birth-death generators;
- Karlin-McGregor/general birth-death spectral theory;
- exactly solvable q-birth-death processes, including the alternative q-Charlier example.

The purpose of these references is adversarial: they define what the project is **not** entitled to claim.
