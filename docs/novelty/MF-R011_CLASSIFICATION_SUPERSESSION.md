# MF-R011 classification supersession notice

**Effective date:** 2026-10-01  
**Scope:** MF-R011 only  
**Reason:** Consolidation 1.0 recovered closer prior literature and completed a stronger semantic/formal audit.

## Current classification

The current publication-safe classification of MF-R011 is:

`EXACT FINITE REACHABILITY-SENSITIVITY RESULT; PRIORITY OF THE SPECIFIC VALUE NOT CERTIFIED`

The canonical mathematical statement uses the **full labeled reflexive-transitive reachability preorder** on the original vertices. For `n=5`, under the declared uniform loopless labeled-digraph / directed-edge-toggle ensemble,

\[
P_5=\frac{6144000}{20971520}=\frac{75}{256}.
\]

The exact `n=5` executable statistic and its semantic bridge have an end-to-end Lean/kernel pass. At commit

`83b45fed020e24f7f9ceba7ecd86220e9c2b8b08`

GitHub Actions workflow `Lean formal verification`, run `301`, completed successfully, including the pinned-toolchain build and all declared module-sharded `leanchecker` replays.

This formal promotion applies to the declared exact `n=5` claim. The human-readable structural identity

\[
P_n=2\Pr(s\not\leadsto t)=2\bigl(1-\gamma_{n,1/2}\bigr)
\]

is not being represented as a general probabilistic theorem already formalized in Lean for arbitrary `n`.

## Literature correction

The former wording

`APPARENTLY UNREPORTED EXACT FINITE SENSITIVITY STATISTIC; NOVELTY NOT CERTIFIED`

is superseded as a **current** classification.

Uno and Ibaraki (1998), *Reachability Problems of Random Digraphs*, treat fixed-pair reachability probability in independent-edge random digraphs and exact computation of that probability. Qin, Sheng, Parkinson, and Falkner (DASFAA 2017), *Edge Influence Computation in Dynamic Graphs*, study edge influence through changes in reachability after edge deletion.

Therefore the project must not claim novelty for random-digraph reachability probability, its general exact computation, or reachability-based edge influence as concepts. The inspected literature does not certify priority either way for the particular reduced value `75/256`; absence of an explicit match is not proof of novelty.

## Historical files

Several July-era classification/freeze artifacts contain the superseded wording. Those files are preserved as provenance rather than silently rewritten as if the earlier audit had never existed. In particular, historical or generated snapshots may include:

- `docs/novelty/RESULT_CLASSIFICATION_PATCH.csv`;
- older generated/exported classification CSV/JSON snapshots;
- manuscript freeze snapshots created before the 2026-10-01 consolidation correction.

When such a historical artifact conflicts with the current classification, this notice, `docs/novelty/MF-R011_edge_flip_probability.md`, `docs/novelty/NOVELTY_AUDIT_C1_SUMMARY.md`, `consolidation/C1_3_EDGE_TOGGLE_SENSITIVITY.md`, and `consolidation/CLAIM_LEDGER.md` control the current MF-R011 wording.

Historical snapshots may continue to contain the old phrase only as dated provenance. They must not be quoted as the project's present novelty assessment.

## Terminology correction

The preferred current wording is

> single-edge toggle changes the full labeled reachability preorder

rather than the looser phrase

> single-edge flip changes the condensation preorder.

The full labeled reachability relation is a preorder on the original vertices. Its mutual-reachability equivalence classes yield SCCs, and quotienting those classes yields the condensation poset. These are related objects but should not be used as interchangeable representation names in the formal statement.

## Nonclaims

This supersession does not change any archived integer, fraction, ensemble definition, or theorem. It does not establish that `75/256` is globally novel or previously published, does not provide an asymptotic theorem, and does not assign physical significance to the statistic.
