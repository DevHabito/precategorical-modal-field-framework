# A114-C2 — corrections and dead ends

## 1. False dyadic shortcut rejected

A tempting route to the second compressed tie was

\[
3(b+2)-h\ge13\stackrel{?}{\Longrightarrow}E_{b+2}<0,
\]

which would have implied that `E_(b+2)=0` can only occur when `3(b+2)-h<=12`, allowing direct reuse of the B2-B dyadic `Phi>0` gate.

This implication is **false**.

Exact rational counterexamples at `s=129/1000` include:

- `M=821`, `b=139`, `j=b+2=141`, `3j-h=13`, but `E_j>0`;
- `M=886`, `b=150`, `j=152`, `3j-h=13`, but `E_j>0`;
- `M=951`, `b=161`, `j=163`, `3j-h=14`, but `E_j>0`.

Therefore A114-C2 does **not** use a dyadic cutoff to prove `Phi>0` on the tie.

## 2. Correct replacement

The correct variable is

\[
R=\frac{s^j}{U},\qquad j=b+2,
\]

not `3j-h` alone.

The promoted A114-A proof already establishes the stronger implication

\[
R\le 9/1000\Longrightarrow E_{b+2}<0.
\]

Hence on the tie `E_(b+2)=0`,

\[
R>9/1000.
\]

Writing

\[
Y=\frac{\beta^j}{U}=R\left(\frac\beta s\right)^j
\]

and using `j>=91` gives a uniform suppression of the negative beta channel. The standalone A114-C2 certificate then proves `Phi>0` with a normalized lower margin above `2.25e-4`, while all omitted normalized tail terms are bounded below `1e-26` in aggregate.

## 3. Scientific discipline

The rejected dyadic shortcut is preserved because it was plausible from early finite roots: the first exploratory ties happened to have small `3j-h`. Later adversarial cells showed ties with larger offsets. The final theorem therefore uses the exact transform ratio forced by the tie rather than a fitted arithmetic threshold.

No physical or ontological conclusion is attached to this correction.