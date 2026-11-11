# Exact Stieltjes-Wigert identification of the constant-rate generator

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact classical identification  
**Novelty consequence:** the constant-rate spectral/finite-polynomial closure structure is classical, not a project novelty

## 1. Purpose

The multi-electron bridge initially exposed a finite hierarchy of exponential transforms. A deeper literature audit shows that, after a natural change of variables, the constant-rate generator is the classical Stieltjes-Wigert q-difference operator shifted by the identity.

This identification materially changes the novelty boundary.

The result is not a new solvable birth-death spectrum. It is a physical realization of classical q-orthogonal-polynomial structure.

## 2. Constant-rate birth-death generator

Write

$$
q=e^{-c}\in(0,1),
\qquad
c=2\beta E_{\rm C},
$$

and consider the constant-rate version

$$
(\mathcal L f)(N)
=
B[f(N+1)-f(N)]
+
Dq^{-N}[f(N-1)-f(N)],
$$

where

$$
B>0,\qquad D>0.
$$

For the electronic model,

$$
B=\Gamma^+,
\qquad
D=\Gamma_0e^{-c/2}.
$$

## 3. Natural q-lattice coordinate

Define

$$
y_N=\frac{B}{D}q^N.
$$

Then

$$
N\to N+1
\quad\Longrightarrow\quad
y\to qy,
$$

and

$$
N\to N-1
\quad\Longrightarrow\quad
y\to y/q.
$$

Also,

$$
Dq^{-N}
=
\frac{B}{y}.
$$

Therefore a function \(g(y_N)=f(N)\) satisfies

$$
\boxed{
\frac{\mathcal L}{B}g(y)
=
g(qy)-g(y)
+
\frac1y[g(y/q)-g(y)].
}
$$

Equivalently,

$$
\frac{\mathcal L}{B}
=
T_q-I-y^{-1}(I-T_{q^{-1}}).
$$

## 4. Exact match with the Stieltjes-Wigert operator

A standard Stieltjes-Wigert q-difference equation is

$$
-x(1-q^n)S_n(x;q)
=
xS_n(qx;q)
-(1+x)S_n(x;q)
+
S_n(x/q;q).
$$

Dividing by \(x\),

$$
(q^n-1)S_n(x;q)
=
S_n(qx;q)-S_n(x;q)
+
\frac1x[S_n(x/q;q)-S_n(x;q)].
$$

This is exactly the transformed electronic generator.

Hence

$$
\boxed{
\mathcal L S_n(y_N;q)
=
B(q^n-1)S_n(y_N;q).
}
$$

The degree-\(n\) Stieltjes-Wigert polynomial is an exact backward-generator eigenfunction.

The eigenvalue is

$$
\boxed{
\lambda_n^{\rm gen}
=
-B(1-q^n).
}
$$

## 5. Meaning of the earlier transform ladder

The monomials

$$
1,y,y^2,\ldots,y^m
$$

span the same polynomial space as

$$
S_0(y;q),S_1(y;q),\ldots,S_m(y;q).
$$

Because

$$
y^j
=
\left(\frac{B}{D}\right)^j q^{jN},
$$

the earlier hierarchy

$$
G_c,G_{2c},\ldots,G_{mc}
$$

is the moment/monomial representation of the same finite polynomial flag.

The triangular closure previously derived is therefore the monomial-basis form of the classical Stieltjes-Wigert spectral structure.

This is a major novelty downgrade.

## 6. Scalar mode

For \(n=1\), the Stieltjes-Wigert polynomial is affine in \(y\).

Thus the centered observable previously written as

$$
e^{-cN}-G_c^{\rm ss}
$$

is, up to affine scaling, the degree-one Stieltjes-Wigert eigenmode.

Its decay rate

$$
B(1-q)
$$

is exactly the \(n=1\) classical eigenvalue magnitude.

This mode is useful physically, but its existence is not a new spectral discovery.

## 7. Stationary measure and the Stieltjes-Wigert moment problem

The constant-rate detailed-balance equation gives

$$
\frac{\pi_{N+1}}{\pi_N}
=
\frac{B}{D}q^{N+1}.
$$

Therefore

$$
\pi_N
\propto
\left(\frac{B}{D}\right)^N
q^{N(N+1)/2}.
$$

Under

$$
y_N=\frac{B}{D}q^N,
$$

the support is a geometric q-lattice.

Discrete orthogonality measures on geometric q-lattices are part of the classical Stieltjes-Wigert moment problem. Christiansen and Koelink studied self-adjoint q-difference operators and discrete classical solutions of that moment problem.

Thus the stationary law, its geometric support after transformation, and the orthogonal-polynomial operator belong to an established mathematical structure.

## 8. What remains exact but not novel

The following earlier bridge results remain correct:

- the transform-shift identity;
- finite closure at \(\lambda=mc\);
- the scalar equation at \(\lambda=c\);
- the stationary transform identities inside the constant-rate model;
- the mean-versus-transform closure comparison.

However, in the constant-rate setting these facts should now be viewed as consequences or elementary coordinate forms of classical q-orthogonal-polynomial structure.

## 9. What remains scientifically interesting

Two features are not removed by the constant-rate identification.

### Time-dependent drive

For a specified time-dependent birth rate \(B(t)\),

$$
\mathcal L_t
$$

still preserves every finite polynomial flag in \(q^N\), but there is no single time-independent Stieltjes-Wigert eigenbasis unless additional structure is proved.

The finite hierarchy becomes a nonautonomous triangular system.

### Hidden-phase marginalization

In the experiment, phase is randomized between repetitions.

Even though the phase-conditioned hierarchy is finite and exact, marginalizing over phase generates mixed correlations such as

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
$$

This destroys generic scalar closure of the phase-averaged transform.

That obstruction is not removed by recognizing the constant-rate Stieltjes-Wigert operator.

## 10. Revised novelty boundary

The project must not claim novelty for:

- the constant-rate eigenvalues;
- the polynomial flag;
- the degree-one transform eigenmode;
- Stieltjes-Wigert orthogonality;
- the discrete-normal stationary law;
- q-adapted coordinates in exactly solvable birth-death processes.

The remaining project-specific questions are narrower:

1. the exact nonautonomous transform hierarchy induced by the experimentally specified drive;
2. its Floquet structure under a periodic drive;
3. the exact information lost when random phase is marginalized;
4. whether the phase-conditioned reduced hierarchy is experimentally useful.

Absolute priority for these narrower statements remains unassessed.

## 11. Literature anchors

- Jacob S. Christiansen and Erik Koelink, “Self-adjoint difference operators and classical solutions to the Stieltjes-Wigert moment problem,” Journal of Approximation Theory 140 (2006), 1-26.
- Jacob Stordal Christiansen, “The moment problem associated with the Stieltjes-Wigert polynomials,” Journal of Mathematical Analysis and Applications 277 (2003), 218-245.
- NIST DLMF, section 18.27(vi), Stieltjes-Wigert polynomials.
- Ryu Sasaki, “Exactly solvable birth and death processes,” Journal of Mathematical Physics 50, 103509 (2009).

The role of these sources is adversarial: they explain why the constant-rate closure should be treated as classical structure rather than a project discovery.
