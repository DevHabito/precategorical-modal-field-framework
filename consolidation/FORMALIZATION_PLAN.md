# Consolidation 1.0 — Lean 4 formalization roadmap

The goal of formalization is not to make the project look more rigorous. The goal is to expose missing definitions, hidden assumptions, type mismatches, and invalid inference chains to an independent proof kernel.

Lean verification certifies only that a formal conclusion follows from formal hypotheses. It does not certify novelty, empirical relevance, or that nature satisfies the hypotheses.

## Toolchain

Preferred stack:

- Lean 4;
- mathlib;
- `lake` project with pinned dependency versions;
- CI that runs `lake build` on every change to formal files;
- no `sorry` in files marked verified;
- bundled `leanchecker` replay for each project module, sharded across CI runners so the independent replay is not hidden by build/runtime limits;
- generated finite certificates allowed only when their generator and checker are both documented.

## Formalization order

### F0 — definition sanity pilot — COMPLETE

Formalize MF-R009, the non-injectivity of the minimum-representative quotient-poset code, using one explicit finite witness.

Purpose: validate the graph/SCC/quotient/code definitions before attempting a counting theorem.

Completion status: the explicit two-graph witness is connected to `Relation.ReflTransGen` reachability, SCC minima, quotient orders, and the direct representative-code computation with no `sorry`.

### F1 — first substantive target: MF-R008 — COMPLETE

Formalized the shifted-binomial count

\[
N_{\mathrm{rep}}(n)=\sum_{k=1}^{n}\binom{n-1}{k-1}p(k).
\]

The completed proof does not trust the historical Python enumerator. It contains the following independent layers:

- a finite labeled ground carrier and the family of representative sets containing the distinguished label `0`;
- a proof that the `k`-representative fiber has cardinality `binom(n-1,k-1)`;
- an executable three-state encoding of antisymmetric relations on unordered pairs;
- exact Lean `native_decide` enumeration of the small labeled-poset counts `1,3,19,219,4231`;
- a semantic proof that the executable transitivity checker is equivalent to mathematical transitivity;
- an exact bijection between accepted three-state encodings and Boolean partial-order matrices;
- an explicit canonical MF-R008 code type whose cardinality is the fiber sum;
- a carrier-transport equivalence showing that the canonical `Fin k` presentation is exactly equivalent to the literal code `(S,P)` with `P` a partial order on the actual representative set `S`;
- an explicit generic realization theorem: every literal `(S,P)` code is realized by a loopless directed graph whose SCC equivalence is exactly equality of the representative map, whose chosen representatives are minimum labels in those SCCs, and whose quotient reachability order is exactly `P`;
- the verified five-vertex conclusion `Nat.card (LiteralRepresentativeCode 4) = 5234`.

Verification status: the complete Lean library builds with the pinned Lean/mathlib environment, rejects `sorry`/`admit`, and every project module passes a bundled `leanchecker` kernel replay in the module-sharded CI.

Scope boundary: F1 proves the declared MF-R008 code/count theorem and closes the realizability of the counted literal codes. It does not establish novelty, retain or count discarded SCC memberships as part of the code, or imply injectivity of the representative code.

### F2 — independent finite computation: MF-R011 — COMPLETE AT DECLARED `n=5` SCOPE

Formalized the declared five-vertex loopless labeled-digraph ensemble, directed-edge coordinate system, edge-toggle operation, compact reachability computation, semantic reference closure, and the exact event counted by the edge-toggle indicator.

The formal chain independently certifies

\[
P_5=\frac{6144000}{20971520}=\frac{75}{256}.
\]

It includes:

- an independent bit-mask graph ensemble;
- exact `native_decide` counts through `n=5`;
- a symbolic five-step Floyd–Warshall reference relation proved equivalent to `Relation.ReflTransGen` reachability;
- an exhaustive semantic audit over all `2^20` five-vertex graph masks connecting the optimized reachability code to that reference;
- a bijection between the 20 mask coordinates and the 20 directed non-loop edges;
- proofs that `toggleMask` flips exactly the selected edge and preserves every other edge;
- an indicator bridge proving each summand is exactly the event that the full labeled reachability preorder changes;
- a generic edge-addition theorem stating that insertion preserves reflexive-transitive closure exactly when the target was already reachable from the source.

Verification status: at commit `83b45fed020e24f7f9ceba7ecd86220e9c2b8b08`, workflow `Lean formal verification` run `301` completed successfully. The pinned `lake build`, proof-placeholder rejection, and every declared module-sharded bundled `leanchecker` replay passed.

Independent non-Lean checks also include an exact reachable-set derivation for `n=5` and a pre-registered directed-cut inclusion-exclusion cross-check through `n=6`, giving

\[
P_6=\frac{313}{2048}.
\]

Scope boundary: F2 formalizes the exact `n=5` statistic and its semantic bridge. The human-readable general identity

\[
P_n=2\Pr(s\not\leadsto t)=2\bigl(1-\gamma_{n,1/2}\bigr)
\]

is not being represented as a general probabilistic Lean theorem for arbitrary `n`, and the `n=6` checkpoint is not part of the end-to-end Lean promotion claim.

### F3 — exact dynamic non-closure: MF-R049 — NEXT

Formalize an explicit finite witness proving that mean plus one fixed-lambda entropic score does not determine the next score under the declared centered contraction.

The first formalization task is **not** to translate the historical floating-point audit. It is to extract a minimal exact theorem.

Preferred proof architecture:

1. define a finite-support exponential moment using exact rational weights;
2. prove two positive four-point distributions have the same normalization, the same mean, and the same moment at the initial scale;
3. prove their required rescaled moments differ exactly;
4. isolate one small analytic lemma connecting positive exponential moments to the entropic score `Q_lambda`, using injectivity of `log` only where needed;
5. derive different next fixed-`lambda` scores through the exact centered-contraction transport identity;
6. keep the unrestricted-distribution scope and the nonclaims explicit.

A rationalized witness is preferable if it preserves the exact MF-R049 existence claim while eliminating unnecessary square-root algebra. Any replacement of the historical witness must be derived and documented exactly, not selected by numerical fitting.

Do not claim that no finite-dimensional closure can exist, that the whole `lambda ↦ Q_lambda` curve is always minimal, or that the mathematical counterexample is a physical evolution law.

### F4 — only after compression: optimization theorems

Do not formalize A112–A122 in chronological form. First rewrite them as C3/C4/C5 self-contained theorem packages. Then select small reusable lemmas:

- determinant/non-singularity lemmas;
- exact sign implications;
- one-variation consequences from adjacent nesting inequalities;
- rounding-phase sign-front lemma;
- interval/cell decomposition statements.

The final asymptotic theorems may require more mathlib infrastructure and are not the first formalization target.

## Independence policy

The Lean development should not import generated facts from the existing Python audits as axioms. Python may generate candidate witnesses or finite data, but Lean must check the mathematical statement from definitions.

For finite exhaustive claims, two implementations are preferred:

1. existing Python exact enumeration;
2. Lean decidable computation from independently written definitions.

Agreement is useful precisely because the implementations do not share the same code path.

## Directory target

The implementation lives under

`formal/lean/`

with modules named by mathematical content rather than audit numbers. Current modules include the representative-code witness, representative counting, poset enumeration/semantics/bijection, count bridge, literal-code carrier equivalence, generic representative-code graph realization, generic edge-addition reachability, edge-toggle finite enumeration, and the `n=5` semantic/ensemble/indicator bridges. A-number provenance may appear in comments, not in theorem names.
