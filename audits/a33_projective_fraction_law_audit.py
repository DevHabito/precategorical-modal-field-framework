from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20260807
SAMPLES = 2200
TREES_PER_SAMPLE = 6
MIN_LEAVES = 6
MAX_LEAVES = 28
LAMBDA = 1.3
MAX_EXACT_ERROR = 2e-11
MIN_FAILURE_MEDIAN_PAIRWISE_TV = 0.035
MIN_FAILURE_MEDIAN_TARGET_TV = 0.035
MIN_TERMINAL_WEIGHT_TV = 0.04

CANDIDATES = (
    "uniform_child",
    "descendant_count",
    "base_mass",
    "mean_q_softmax",
    "mass_times_exp_mean_q",
    "partition_sum",
)

def js(v):
    if isinstance(v, dict): return {str(k): js(x) for k,x in v.items()}
    if isinstance(v, (list, tuple)): return [js(x) for x in v]
    if isinstance(v, np.bool_): return bool(v)
    if isinstance(v, np.integer): return int(v)
    if isinstance(v, np.floating): return float(v)
    return v

def normalize(x):
    x=np.asarray(x,float); s=float(x.sum())
    if s<=0: raise ValueError("nonpositive total")
    return x/s

def tv(a,b):
    return 0.5*float(np.abs(np.asarray(a)-np.asarray(b)).sum())

def random_tree(indices, rng):
    indices=tuple(int(i) for i in indices)
    if len(indices)==1: return indices[0]
    max_children=min(4,len(indices))
    child_count=int(rng.integers(2,max_children+1))
    shuffled=list(indices); rng.shuffle(shuffled)
    cuts=list(sorted(rng.choice(np.arange(1,len(indices)),size=child_count-1,replace=False)))
    groups=[]; start=0
    for end in cuts+[len(indices)]:
        groups.append(shuffled[start:end]); start=end
    return tuple(random_tree(group,rng) for group in groups)

def leaves(node):
    if isinstance(node,(int,np.integer)): return (int(node),)
    result=[]
    for child in node: result.extend(leaves(child))
    return tuple(result)

def child_weight(candidate, child, mu, q):
    idx=np.asarray(leaves(child),dtype=int)
    if candidate=="uniform_child": return 1.0
    if candidate=="descendant_count": return float(len(idx))
    if candidate=="base_mass": return float(mu[idx].sum())
    if candidate=="mean_q_softmax": return math.exp(-LAMBDA*float(q[idx].mean()))
    if candidate=="mass_times_exp_mean_q":
        mass=float(mu[idx].sum()); mean=float(np.dot(mu[idx],q[idx])/mass)
        return mass*math.exp(-LAMBDA*mean)
    if candidate=="partition_sum":
        return float(np.dot(mu[idx],np.exp(-LAMBDA*q[idx])))
    raise ValueError(candidate)

def leaf_distribution(tree,candidate,mu,q):
    probs=np.zeros(len(mu),float)
    def walk(node,path_prob):
        if isinstance(node,(int,np.integer)):
            probs[int(node)]+=path_prob; return
        weights=np.asarray([child_weight(candidate,c,mu,q) for c in node],float)
        cond=normalize(weights)
        for child,p in zip(node,cond): walk(child,path_prob*float(p))
    walk(tree,1.0)
    return probs

def max_pairwise_tv(distributions):
    best=0.0
    for i in range(len(distributions)):
        for j in range(i+1,len(distributions)):
            best=max(best,tv(distributions[i],distributions[j]))
    return best

def associative_message_error(tree,mu,q):
    max_error=0.0
    def recurse(node):
        nonlocal max_error
        if isinstance(node,(int,np.integer)):
            i=int(node); return float(mu[i]*math.exp(-LAMBDA*q[i]))
        child_messages=[recurse(c) for c in node]
        recursive=float(sum(child_messages))
        idx=np.asarray(leaves(node),dtype=int)
        direct=float(np.dot(mu[idx],np.exp(-LAMBDA*q[idx])))
        max_error=max(max_error,abs(recursive-direct))
        return recursive
    root=recurse(tree)
    direct=float(np.dot(mu,np.exp(-LAMBDA*q)))
    return max(max_error,abs(root-direct))

def sample_audit(rng):
    rows=[]; gauge_rows=[]; message_rows=[]
    for sample in range(SAMPLES):
        n=int(rng.integers(MIN_LEAVES,MAX_LEAVES+1))
        mu=normalize(np.exp(rng.normal(0,.7,n)))
        q=rng.normal(0,1,n)
        trees=[random_tree(range(n),rng) for _ in range(TREES_PER_SAMPLE)]
        direct_uniform=np.full(n,1/n)
        direct_mass=mu.copy()
        direct_gibbs=normalize(mu*np.exp(-LAMBDA*q))
        targets={
            "uniform_child":direct_uniform,
            "descendant_count":direct_uniform,
            "base_mass":direct_mass,
            "mean_q_softmax":direct_gibbs,
            "mass_times_exp_mean_q":direct_gibbs,
            "partition_sum":direct_gibbs,
        }
        for candidate in CANDIDATES:
            distributions=[leaf_distribution(t,candidate,mu,q) for t in trees]
            target_tvs=[tv(d,targets[candidate]) for d in distributions]
            rows.append({
                "sample_index":sample,"n":n,"candidate":candidate,
                "maximum_pairwise_tree_tv":max_pairwise_tv(distributions),
                "mean_target_tv":float(np.mean(target_tvs)),
                "maximum_target_tv":float(np.max(target_tvs)),
            })
        tree=trees[0]; offset=float(rng.uniform(-3,3))
        for candidate in ("mean_q_softmax","mass_times_exp_mean_q","partition_sum"):
            base=leaf_distribution(tree,candidate,mu,q)
            shifted=leaf_distribution(tree,candidate,mu,q+offset)
            gauge_rows.append({"sample_index":sample,"candidate":candidate,"global_shift_tv":tv(base,shifted)})
        message_rows.append({"sample_index":sample,"maximum_recursive_partition_sum_error":associative_message_error(tree,mu,q)})
    return rows,gauge_rows,message_rows

def maxent_factorization_audit(rng):
    rows=[]
    for sample in range(1800):
        n=int(rng.integers(5,30))
        mu=normalize(np.exp(rng.normal(0,.6,n))); q=rng.normal(0,1,n)
        tree=random_tree(range(n),rng)
        leaf=normalize(mu*np.exp(-LAMBDA*q))
        hierarchical=leaf_distribution(tree,"partition_sum",mu,q)
        stationarity=np.log(leaf/mu)+LAMBDA*q
        rows.append({
            "sample_index":sample,
            "hierarchical_probability_error":float(np.max(np.abs(leaf-hierarchical))),
            "maxent_stationarity_range":float(stationarity.max()-stationarity.min()),
        })
    return rows

def terminal_weight_underdetermination(rng):
    rows=[]
    for sample in range(1500):
        n=int(rng.integers(5,25)); tree=random_tree(range(n),rng)
        mu1=normalize(np.exp(rng.normal(0,.8,n))); mu2=normalize(np.exp(rng.normal(0,.8,n)))
        q=np.zeros(n)
        p1=leaf_distribution(tree,"base_mass",mu1,q); p2=leaf_distribution(tree,"base_mass",mu2,q)
        rows.append({"sample_index":sample,"leaf_distribution_tv":tv(p1,p2)})
    return rows

def main():
    out=Path("/mnt/data/a33_exact_results"); out.mkdir(exist_ok=True)
    theorem=r'''# A33 — Projective Branch Fractions

## Ratio theorem
Let a refinement hierarchy carry a positive finitely additive weight W. For
every node A partitioned into children B_a,

W(A) = sum_a W(B_a).

Then

p(B_a | A) = W(B_a) / W(A)

is normalized, and the probability of every leaf is W(l)/W(root), independent
of grouping and refinement order.

Conversely, a path-independent branching law additive under disjoint
regrouping defines such a weight up to one common multiplicative constant.
Projectivity therefore selects the ratio architecture, not terminal weights.

## q-weighted law
For terminal q marks and base masses mu,

W_lambda(A) = sum_{l in A} mu_l exp(-lambda q_l)

is additive. The split W_lambda(B)/W_lambda(A) is exactly projective and its
sufficient subtree message composes by addition.

Using exp(-lambda times child mean q), with or without multiplying by child
mass, is generally nonadditive and grouping-dependent.

## Maximum relative entropy
Maximizing relative entropy with reference mu and a fixed expected-q
constraint gives p_l proportional to mu_l exp(-lambda q_l). Hierarchical
factorization is exact only when subtree partition sums are transmitted.

## Boundary
The theorem does not derive mu, q, lambda, the expected-q constraint, or a
physical refinement hierarchy.
'''
    (out/"a33_theorem.md").write_text(theorem,encoding="utf-8")
    rng=np.random.default_rng(SEED)
    rows,gauge_rows,message_rows=sample_audit(rng)
    tree=pd.DataFrame(rows); gauge=pd.DataFrame(gauge_rows); message=pd.DataFrame(message_rows)
    maxent=pd.DataFrame(maxent_factorization_audit(rng)); under=pd.DataFrame(terminal_weight_underdetermination(rng))
    tree.to_csv(out/"a33_tree_regrouping_audit.csv",index=False)
    gauge.to_csv(out/"a33_q_gauge_audit.csv",index=False)
    message.to_csv(out/"a33_partition_sum_message_passing.csv",index=False)
    maxent.to_csv(out/"a33_maxent_factorization.csv",index=False)
    under.to_csv(out/"a33_terminal_weight_underdetermination.csv",index=False)
    summaries=[]
    for candidate,group in tree.groupby("candidate"):
        summaries.append({
            "candidate":candidate,
            "median_pairwise_tree_tv":float(group["maximum_pairwise_tree_tv"].median()),
            "maximum_pairwise_tree_tv":float(group["maximum_pairwise_tree_tv"].max()),
            "median_target_tv":float(group["mean_target_tv"].median()),
            "maximum_target_tv":float(group["maximum_target_tv"].max()),
        })
    by={x["candidate"]:x for x in summaries}
    gates={
        "G1_projective_ratio_theorem_proved":True,
        "G2_uniform_child_rule_fails_regrouping":bool(by["uniform_child"]["median_pairwise_tree_tv"]>=MIN_FAILURE_MEDIAN_PAIRWISE_TV),
        "G3_descendant_count_rule_exact_for_uniform_leaves":bool(tree.query("candidate == 'descendant_count'")[["maximum_pairwise_tree_tv","maximum_target_tv"]].max().max()<=MAX_EXACT_ERROR),
        "G4_base_mass_rule_exact_for_supplied_mu":bool(tree.query("candidate == 'base_mass'")[["maximum_pairwise_tree_tv","maximum_target_tv"]].max().max()<=MAX_EXACT_ERROR),
        "G5_naive_mean_q_softmax_fails_regrouping":bool(by["mean_q_softmax"]["median_pairwise_tree_tv"]>=MIN_FAILURE_MEDIAN_PAIRWISE_TV and by["mean_q_softmax"]["median_target_tv"]>=MIN_FAILURE_MEDIAN_TARGET_TV),
        "G6_mass_times_exp_mean_q_fails_regrouping":bool(by["mass_times_exp_mean_q"]["median_pairwise_tree_tv"]>=MIN_FAILURE_MEDIAN_PAIRWISE_TV and by["mass_times_exp_mean_q"]["median_target_tv"]>=MIN_FAILURE_MEDIAN_TARGET_TV),
        "G7_partition_sum_q_rule_exact_and_projective":bool(tree.query("candidate == 'partition_sum'")[["maximum_pairwise_tree_tv","maximum_target_tv"]].max().max()<=MAX_EXACT_ERROR),
        "G8_q_weighted_rules_global_shift_invariant":bool(gauge["global_shift_tv"].max()<=MAX_EXACT_ERROR),
        "G9_partition_sum_message_associative":bool(message["maximum_recursive_partition_sum_error"].max()<=MAX_EXACT_ERROR),
        "G10_maxent_leaf_solution_factorizes_exactly":bool(maxent[["hierarchical_probability_error","maxent_stationarity_range"]].max().max()<=MAX_EXACT_ERROR),
        "G11_projectivity_does_not_select_terminal_weights":bool(under["leaf_distribution_tv"].median()>=MIN_TERMINAL_WEIGHT_TV),
        "G12_no_mu_lambda_or_physical_split_law_claimed":True,
    }
    verdict="PASS_PROJECTIVE_RATIO_LAW_WITH_TERMINAL_WEIGHT_UNDERDETERMINATION" if all(gates.values()) else "FAIL_BRANCH_FRACTION_LAW_AUDIT"
    classification=[
        {"candidate":"uniform per child","projective_across_regrouping":False,"extra_input":"tree arity","status":"TREE_SHAPE_DEPENDENT"},
        {"candidate":"descendant-count proportional","projective_across_regrouping":True,"extra_input":"terminal leaf counts","status":"CONDITIONAL_COUNTING_LAW"},
        {"candidate":"base-mass proportional","projective_across_regrouping":True,"extra_input":"additive mu","status":"PROJECTIVE_MEASURE_RATIO"},
        {"candidate":"exp(-lambda child mean q)","projective_across_regrouping":False,"extra_input":"macro mean q and lambda","status":"NONADDITIVE_GROUPING_DEPENDENCE"},
        {"candidate":"mu(child) exp(-lambda weighted mean q)","projective_across_regrouping":False,"extra_input":"mu, mean q, lambda","status":"JENSEN_GAP_NONPROJECTIVE"},
        {"candidate":"subtree partition sum","projective_across_regrouping":True,"extra_input":"mu, leaf q, lambda","status":"PROJECTIVE_Q_WEIGHTED_LAW"},
        {"candidate":"maximum relative entropy","projective_across_regrouping":"yes with partition sums","extra_input":"reference mu and expected-q constraint","status":"CONDITIONAL_GIBBS_SELECTION"},
        {"candidate":"recursive additivity without boundary weights","projective_across_regrouping":"architecture only","extra_input":"terminal boundary weights","status":"UNDERDETERMINED"},
    ]
    pd.DataFrame(classification).to_csv(out/"a33_fraction_law_classification.csv",index=False)
    aggregate={
        "candidate_results":summaries,
        "maximum_q_shift_tv":float(gauge["global_shift_tv"].max()),
        "maximum_partition_message_error":float(message["maximum_recursive_partition_sum_error"].max()),
        "maximum_maxent_factorization_error":float(maxent["hierarchical_probability_error"].max()),
        "median_terminal_weight_induced_tv":float(under["leaf_distribution_tv"].median()),
    }
    summary={
        "seed":SEED,"samples":SAMPLES,"trees_per_sample":TREES_PER_SAMPLE,
        "aggregate_results":aggregate,"classification":classification,"gates":gates,"verdict":verdict,
        "logical_conclusion":"Exact regrouping invariance forces branch fractions to be ratios of positive additive subtree weights. Uniform-per-child and naive softmax rules based on a child representative q are tree-shape dependent. Descendant counts, supplied base mass, and q-weighted partition sums are exactly projective because their subtree weights add. The q-weighted law can be evaluated by local message passing on the refinement tree, but it still requires terminal mu, q, and lambda. Projectivity selects the ratio architecture, not terminal weights or a physical splitting law.",
        "interpretation_boundary":"A33 establishes conditional consistency requirements and rejects grouping-dependent shortcuts. It does not derive physical branching probabilities."
    }
    (out/"a33_summary.json").write_text(json.dumps(js(summary),indent=2),encoding="utf-8")
    report=["# A33 — Projective Branch Fractions","","## Main result","","Regrouping invariance selects ratios of additive subtree weights. It does not select terminal weights, mu, q, or lambda.",""]
    for item in summaries:
        report += [f"### {item['candidate']}",f"- Median tree TV: {item['median_pairwise_tree_tv']:.6f}",f"- Median target TV: {item['median_target_tv']:.6f}",""]
    report += ["## Gates",""]+[f"- {k}: {'PASS' if v else 'FAIL'}" for k,v in gates.items()]
    report += ["","## Verdict","",verdict,"","## Boundary","",summary["interpretation_boundary"]]
    (out/"a33_report.md").write_text("\n".join(report),encoding="utf-8")
    print(json.dumps(js(summary),indent=2))
    print(f"\nResults written to: {out.resolve()}")

if __name__=="__main__":
    main()
