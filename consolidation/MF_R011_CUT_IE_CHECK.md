# MF-R011 — independent cut inclusion-exclusion check

**Run date:** 2026-10-01  
**Implementation:** `tools/mf_r011_cut_inclusion_exclusion.py`  
**Arithmetic:** exact integers and `Fraction`; no floating-point arithmetic.  
**Relationship to frozen target:** this checker was written after `MF_R011_FROZEN_N6_CHECKPOINT.md` froze the n=6 target, and it does not use the rooted-reachable recurrence or any frozen target value as input.

## 1. Independent event decomposition

Fix distinct vertices `s,t` in a loopless labeled digraph on `n` vertices.
For every subset `S` with

\[
s\in S,\qquad t\notin S,
\]

let `A_S` be the event that **no directed edge leaves `S`**.

Then

\[
s\not\leadsto t
\quad\Longleftrightarrow\quad
\bigcup_{S:\,s\in S,\ t\notin S} A_S.
\]

The two directions are elementary and important:

- if `s` does not reach `t`, take `S` to be the exact set of vertices reachable from `s`; no edge can leave `S`, otherwise its endpoint would also be reachable;
- if some `S` contains `s`, excludes `t`, and has no outgoing edge, every directed path starting at `s` stays inside `S`, so it cannot reach `t`.

This decomposition is different from the reachable-set-size recurrence used in
`MF_R011_FROZEN_N6_CHECKPOINT.md`. Here we do not classify by one exact reachable
set and do not use the classical counts `a_j`.

## 2. Inclusion-exclusion count

There are

\[
2^{n-2}
\]

candidate subsets `S` containing `s` and excluding `t`.

For any nonempty family `F` of such subsets, the intersection

\[
\bigcap_{S\in F} A_S
\]

forces absent exactly every directed edge belonging to

\[
\bigcup_{S\in F}\delta^+(S),
\]

where `delta^+(S)` is the directed cut from `S` to its complement.
All other directed non-loop edges remain free. Hence that intersection contains
exactly

\[
2^{n(n-1)-\left|\bigcup_{S\in F}\delta^+(S)\right|}
\]

graphs.

Inclusion-exclusion therefore gives the exact count

\[
B_n
=
\sum_{\varnothing\neq F}
(-1)^{|F|+1}
2^{n(n-1)-\left|\bigcup_{S\in F}\delta^+(S)\right|}.
\]

The checker represents every directed cut as an integer bit mask and computes
the union cardinality with exact bit operations. For `n=6` there are only

\[
2^{6-2}=16
\]

cut events and therefore

\[
2^{16}-1=65535
\]

nonempty families in the inclusion-exclusion sum.

## 3. Exact output

The checker produced:

```text
n=2 nonreach=2/4=1/2 P=1 sensitive=8/8
n=3 nonreach=24/64=3/8 P=3/4 sensitive=288/384
n=4 nonreach=1024/4096=1/4 P=1/2 sensitive=24576/49152
n=5 nonreach=153600/1048576=75/512 P=75/256 sensitive=6144000/20971520
n=6 nonreach=82051072/1073741824=313/4096 P=313/2048 sensitive=4923064320/32212254720
```

Thus the independent cut calculation reproduces all historical small-n MF-R011
values through `n=5` and, more importantly, reproduces the pre-registered n=6
target exactly:

\[
\boxed{B_6=82051072},
\]

\[
\boxed{\Pr(s\not\leadsto t)=313/4096},
\]

\[
\boxed{P_6=313/2048},
\]

and

\[
\boxed{4923064320\text{ sensitive pairs out of }32212254720}.
\]

No target value is imported by the checker.

## 4. What this cross-check buys us

The n=6 agreement is stronger than simply rerunning the same recurrence in a
second language:

- the frozen derivation partitions graphs by the exact reachable set of `s`
  and uses rooted-reachable counts `a_j`;
- the new checker treats non-reachability as a union of directed-cut events and
  applies inclusion-exclusion over all such cuts;
- the two routes share the graph ensemble and the mathematical definition of
  reachability, but they do not share the same counting decomposition.

This reduces the risk of a common arithmetic or recurrence error.

It does **not** make the result novel, physical, or asymptotic.

## 5. Literature boundary

The root-reachable counts used in the first derivation are classical initially
connected digraph counts. Published tables include Jonah Ostroff,
*Counting Connected Digraphs with Gradings* (PhD dissertation, Brandeis
University, 2013), Table 1.

Fixed-pair random-digraph reachability itself is also prior art; Uno and Ibaraki
(1998) explicitly study its exact computation. The role of the present checker
is therefore verification, not novelty manufacture.

## 6. Current evidential status

For the exact finite sensitivity values we now have distinct layers:

1. historical exhaustive graph-edge enumeration for `n<=5`;
2. independent Lean graph-mask enumeration for `n<=5`, subject to the active
   end-to-end CI/kernel gate;
3. exact reachable-set counting derivation;
4. independent directed-cut inclusion-exclusion computation through `n=6`.

Agreement across these routes supports the finite arithmetic claim. Formal
promotion still depends on the Lean semantic bridge and kernel replay passing;
this Python checker does not replace that gate.
