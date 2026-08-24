# A104 — Exact exceptional q0/q1 continuum segment atlas

## Question

A102 closed the pointwise rational-witness lift atlas, but seven witnesses required exceptional q0/q1 active sets rather than the legacy-natural or endpoint-released families. A104 asks whether those seven exact bases remain valid on their complete A95 rational source segments, only on proper witness-containing subcomponents, or fail internally.

The seven source records split into two architectures:

1. **q0/q1 with gamma inactive**
   \[
   P=\{j,M\},\qquad Q=\{0,1,h,h+1\},
   \]
   with \(\alpha+\) and \(\beta-\) active, for \(M=396,455,496\).

2. **q0/q1 with gamma-minus active**
   \[
   P=\{j-1,j,M\},\qquad Q=\{0,1,h,h+1\},
   \]
   with \(\alpha+\), \(\beta-\), and \(\gamma-\) active, for \(M=443,449,484,490\).

## Exact symbolic reduction

Only the active alpha row depends on the probe \(s\). Around the exact reference \(s=1/8\), an exact Sherman–Morrison row update expresses every basic variable, active multiplier, unused-atom reduced cost, inactive-band slack, and the common denominator as a sparse rational polynomial in \(s\).

Across the seven records this gives:

- **6,489 KKT conditions**;
- **6,496 numerator/denominator sign obligations**;
- no floating-point sign gate.

All source condition counts agree exactly with the pointwise certificates routed by A102.

## Result

All seven source segments contain a **proper two-sided strict KKT subcomponent** around the A102 witness. No exceptional basis covers its complete A95 source segment.

| \(M\) | Architecture | Certified strict component, approximately | Lower boundary | Upper boundary |
|---:|---|---|---|---|
| 396 | q0/q1, gamma inactive | \((0.12998746046060514,\ 0.13001712851537764)\) | inactive \(\gamma-\) slack | basic \(q_0\) mass |
| 443 | q0/q1, gamma active | \((0.12995038668064895,\ 0.13010385308290245)\) | active \(\gamma-\) multiplier | basic \(p_{77}\) mass |
| 449 | q0/q1, gamma active | \((0.12984485224446118,\ 0.13003812547052784)\) | active \(\gamma-\) multiplier | basic \(p_{78}\) mass |
| 455 | q0/q1, gamma inactive | \((0.12997406869424574,\ 0.13000195631728176)\) | inactive \(\gamma-\) slack | basic \(q_0\) mass |
| 484 | q0/q1, gamma active | \((0.12995988958653437,\ 0.13009785095622953)\) | active \(\gamma-\) multiplier | basic \(p_{84}\) mass |
| 490 | q0/q1, gamma active | \((0.12986717027689298,\ 0.13003754002200674)\) | active \(\gamma-\) multiplier | basic \(p_{85}\) mass |
| 496 | q0/q1, gamma inactive | \((0.12997863902983456,\ 0.13000525542593838)\) | inactive \(\gamma-\) slack | basic \(q_0\) mass |

The table reports decimal approximations only for readability. The committed catalogue stores exact rational isolating brackets and exact rational component hulls.

## Boundary proof and falsifiability

The audit isolated **25 sign-changing candidate roots**. Fourteen are the nearest boundaries of the seven witness-containing components. Every selected root has opposite exact endpoint signs and a derivative interval with fixed nonzero sign, so it is locally unique and simple.

The three gamma-inactive records have several competing roots on each side. A104 does not choose the nearest boundary by decimal midpoint alone. It proves **11 strict rational bracket-ordering inequalities**, showing that every competing left bracket ends before the selected lower bracket and every competing right bracket starts after the selected upper bracket.

All 6,496 core sign certificates pass. Every nonselected condition also remains positive on the complete hull spanning both selected isolating brackets. Finally, A104 gives **14 exact rational outside counterexamples**, one beyond each selected boundary, where the responsible condition is strictly negative.

## Structural interpretation

The two exceptional architectures have different two-sided exit mechanisms:

- with gamma inactive, decreasing \(s\) activates the gamma-minus constraint, while increasing \(s\) drives \(q_0\) to zero;
- with gamma-minus active, decreasing \(s\) drives its active dual multiplier to zero, while increasing \(s\) removes the lower adjacent \(P\) atom.

Thus the pointwise q0/q1 solutions are genuine open phases, not isolated rational coincidences, but their validity is narrower than the source segments supplied by the compressed atlas.

## Claim boundary

A104 proves exact continuum persistence only for the seven exceptional A102 source segments. It does not prove continuum lifting for the other 1,056 A102 witnesses, coverage of complete A92 algebraic cells, validity outside the declared contract, a universal support law, or any physical or ontological interpretation.
