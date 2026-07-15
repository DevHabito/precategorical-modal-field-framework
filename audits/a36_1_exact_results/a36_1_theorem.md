# A36.1 — Corrective CLT Criterion

The original A36 used a fixed Kolmogorov–Smirnov threshold at block size 128.
For lattice-valued Rademacher sums, CDF jumps make that finite-size gate too
strong even though the central limit theorem is valid. The threshold is not
lowered.

For iid centered variance-one variables with characteristic function
\(\phi\), the normalized sum has characteristic function
\[
\phi_n(t)=\phi(t/\sqrt n)^n.
\]
Under the finite-variance CLT assumptions, \(\phi_n(t)\to e^{-t^2/2}\)
pointwise. The corrective audit measures convergence uniformly on the frozen
compact interval \([-4,4]\) for Rademacher, Laplace, and uniform inputs.

This does not remove the CLT assumptions and does not derive independence for
RZS noise.
