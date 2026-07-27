# Bootstrap Spectral Covariance Protocol: Calibration, Validation, and Failure Boundary

**Programme:** Modal Field Research Programme  
**Provisional audit:** A62  
**Author line:** Felipe Gianini Romero  
**Status:** reproducible model-conditional statistical protocol; raw bootstrap rejected; no universal finite-sample coverage theorem

## Technical abstract

A61 showed how to propagate a certified spectral covariance radius

\[
\|\Sigma-\widehat\Sigma\|_2\le\tau
\]

into an exact robust-risk upper bound. A62 estimates the covariance and a usable spectral radius from repeated three-channel calibration data.

For each sample, the protocol:

1. estimates the unbiased sample covariance;
2. resamples complete calibration rows;
3. recomputes bootstrap covariance matrices;
4. evaluates the spectral deviations;
5. takes the upper empirical 95% quantile;
6. multiplies the raw radius by a model-conditional safety factor.

The raw bootstrap was audited rather than presumed valid. The simulation design used 399 bootstrap replications, 500 calibration simulations per cell, 1000 independent validation simulations per cell, and sample sizes 30, 60, and 120.

The raw minimum coverage was:

\[
\boxed{\text{Gaussian family: }89.2\%}
\]

\[
\boxed{\text{Student-}t_5\text{ family: }80.7\%}
\]

Therefore, the uninflated nonparametric bootstrap radius is rejected as a finite-sample 95% procedure in the audited regime.

Using separate calibration and validation seeds, the selected safety factors were:

\[
\boxed{c_{\rm Gaussian}=1.5}
\]

\[
\boxed{c_{t_5}=1.9}
\]

The independent validation minima became 97.0% for the Gaussian family and 95.0% for the Student-t5 family.

A second finding is equally important: statistical coverage and downstream mathematical availability are different. The minimum calibrated contract-valid rates were 89.4% for the Gaussian family and 63.7% for the heavy-tail family.

For Student-t5 data with n=30, the calibrated radius covered at 95.0%, but only 63.7% of samples remained inside the A58/A60 certified box. The rate that was both covered and contract-valid was 58.7%.

\[
\boxed{\text{Coverage and contract availability must be reported separately.}}
\]

## 1. Statistical input

Let \(X_1,\ldots,X_n\in\mathbb R^3\) be repeated calibration residuals ordered as \((u_2,u_\beta,u_\infty)\). The unbiased covariance estimator is

\[
\widehat\Sigma=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar X)(X_i-\bar X)^\top.
\]

Complete rows are resampled, preserving the observed dependence between channels.

## 2. Raw bootstrap radius

For bootstrap replicate \(b\), define

\[
T_b^\star=\|\widehat\Sigma_b^\star-\widehat\Sigma\|_2.
\]

The raw radius is the upper empirical quantile at index

\[
\left\lceil(B+1)(1-\alpha)\right\rceil.
\]

Here \(B=399\) and \(\alpha=0.05\). Despite the conservative finite-bootstrap ordering rule, raw finite-sample coverage was insufficient.

## 3. Calibration and validation separation

For each declared model family, the smallest factor on the grid 1.00, 1.05, ..., 3.00 reaching at least 96% coverage in every calibration cell was selected. Validation then used new random seeds and 1000 simulations per cell.

This avoids reporting in-sample calibration performance as independent validation. It does not make the factors universal constants.

## 4. Gaussian validation

The calibrated Gaussian factor was \(c_G=1.5\).

| Covariance scenario | n | Raw coverage | Calibrated coverage | Contract valid | Covered and valid |
|---|---:|---:|---:|---:|---:|
| diagonal | 30 | 91.1% | 99.1% | 95.4% | 94.5% |
| diagonal | 60 | 94.3% | 99.5% | 99.9% | 99.4% |
| diagonal | 120 | 94.8% | 99.6% | 100.0% | 99.6% |
| positive correlation | 30 | 89.2% | 97.0% | 89.4% | 86.4% |
| positive correlation | 60 | 91.4% | 97.8% | 99.6% | 97.4% |
| positive correlation | 120 | 93.1% | 99.0% | 100.0% | 99.0% |
| mixed correlation | 30 | 89.5% | 98.0% | 93.7% | 91.7% |
| mixed correlation | 60 | 92.3% | 99.0% | 99.8% | 98.8% |
| mixed correlation | 120 | 93.0% | 98.7% | 100.0% | 98.7% |

The weakest Gaussian validation cell was the positively correlated covariance at n=30: coverage improved from 89.2% to 97.0%. Its 95% Wilson interval was approximately [95.75%, 97.89%].

## 5. Heavy-tail stress validation

The Student-\(t_5\) factor was \(c_{t_5}=1.9\).

| n | Raw coverage | Calibrated coverage | Contract valid | Covered and valid | Actual risk coverage among valid |
|---:|---:|---:|---:|---:|---:|
| 30 | 80.7% | 95.0% | 63.7% | 58.7% | 93.1% |
| 60 | 85.0% | 98.2% | 74.7% | 72.9% | 98.0% |
| 120 | 89.7% | 98.6% | 87.8% | 86.4% | 98.6% |

At n=30, calibrated coverage was exactly 95.0%, with Wilson interval approximately [93.47%, 96.19%]. However, the larger radius frequently pushed the inflated covariance outside the current A58 variance box.

The correct software response is `OUT_OF_CONTRACT`, not silent clipping. Clipping would invalidate the spectral coverage statement.

## 6. Deterministic risk propagation

For each validation sample remaining inside the box, A60 evaluated the exact quadratic robust-risk root. The audited implication was

\[
\|\widehat\Sigma-\Sigma\|_2\le\widehat\tau
\quad\Longrightarrow\quad
Q^\star(\Sigma)\le Q^\star(\widehat\Sigma+\widehat\tau I).
\]

\[
\boxed{\text{Observed implication violations: }0}
\]

This does not prove bootstrap coverage. It confirms the deterministic A61 step whenever the statistical coverage event occurs.

## 7. Interpretation of the multipliers

The factors \(c_G=1.5\) and \(c_{t_5}=1.9\) are simulation-calibrated for the declared generators, covariance scales, sample sizes, bootstrap size, and quantile rule.

They are not distribution-free. A new residual model or instrument requires new calibration and independent validation, or a theorem with explicit tail assumptions.

## 8. Practical protocol

1. collect repeated three-channel calibration residuals;
2. estimate \(\widehat\Sigma\);
3. bootstrap complete rows;
4. compute spectral deviations;
5. take the declared upper empirical quantile;
6. multiply by a factor validated for the residual model;
7. form \(\widehat\Sigma^+=\widehat\Sigma+\widehat\tau I\);
8. require \(\max_i\widehat\Sigma^+_{ii}\le1/400\);
9. propagate through A60 only when the contract is valid;
10. report statistical coverage calibration and contract availability separately.

## 9. Logical status

### Established by the computational audit

1. Raw bootstrap undercoverage occurs in the audited finite samples.
2. Independent calibration and validation produce model-conditional safety factors.
3. The heavy-tail family requires a larger factor.
4. Calibrated validation is compatible with 95% coverage in every declared cell.
5. Heavy tails substantially reduce downstream certificate availability.
6. No A61 implication violation was observed.
7. The run is reproducible under the declared seeds and configuration.

### Not established

1. No universal finite-sample bootstrap theorem is proved.
2. The factors are not distribution-free.
3. Coverage outside the declared covariance and sample-size families is unknown.
4. Serial dependence is not included.
5. Student distributions with fewer than five degrees of freedom are not covered.
6. The A58 box is too narrow for many small-n heavy-tail outcomes.

## 10. Next rigorous target

The main remaining statistical failure is now identified:

\[
\boxed{\text{Heavy-tail covariance estimation produces radii too large for the current contract.}}
\]

The next step should compare the ordinary sample covariance with a robust estimator such as a block median-of-means covariance or a clipped outer-product estimator.

The target is the joint criterion

\[
\boxed{\text{coverage}+\text{contract availability}+\text{risk-bound validity}.}
\]

A robust estimator is useful only if it improves the full three-part outcome.
