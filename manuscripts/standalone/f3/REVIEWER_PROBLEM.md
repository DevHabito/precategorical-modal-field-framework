# Blind rederivation challenge: one-score nonclosure

**Instructions to an independent reviewer:** Work from the definitions below **without reading** \`ARTICLE.md\`, the existing Lean files, the repository's earlier MF-R049 examples, or the test code. Record the method and any failed attempt before seeing those materials. The challenge is not itself evidence of a completed blind review.

Let \(p=(p_0,p_1,p_2,p_3)\) have strictly positive entries summing to one, supported at positions \(0,1,2,3\). Put \(m(p)=\sum jp_j\) and \(P_p(t)=\sum p_jt^j\). Define

\[
S_\lambda(p)=-\frac{\log P_p(e^{-\lambda})}{\lambda},
\]

for \(\lambda>0\). For \(a=1/2\), update positions by \(x_j'=(1-a)m(p)+aj\), preserving the probabilities. Fix \(\lambda=2\log2\).

**Question:** Does there exist a function \(G\) such that \(S_\lambda(T_ap)=G(m(p),S_\lambda(p))\) for **every** strictly positive \(p\) on this fixed support? Prove the answer. A counterexample must exhibit positive normalized weights with an exact verification of all equalities and the strict output inequality.

Please also examine:

- Whether a counterexample remains when the two laws have identical support and mean.
- Whether a claim about all finite-dimensional closure systems follows from this question.
- Whether an argument at \(\lambda=0\), \(a=1\), or at a transform parameter unchanged by the update is relevant.
- Which classical moment/transform uniqueness results might apply, and whether they actually imply the statement.

**Before opening the proof:** submit your derivation, failed approaches, prior-art matches, confidence level and conflict/independence disclosure. Only then compare with \`ARTICLE.md\` and the formal code.

Review status on creation: **NO EXTERNAL RESPONSE RECEIVED**.
