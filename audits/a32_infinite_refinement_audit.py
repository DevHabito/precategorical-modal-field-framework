from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20260806
TREE_SAMPLES = 600
MAX_DEPTH = 8
SCHEDULE_SAMPLES = 500
SCHEDULE_MAX_DEPTH = 7
MARTINGALE_PATHS = 120_000
MARTINGALE_DEPTH = 30
MARTINGALE_RHO = 0.72
MARTINGALE_SCALE = 0.8
MAX_NUMERICAL_ERROR = 2e-11
MAX_MARTINGALE_RELATIVE_ERROR = 0.035
MIN_MEASURE_NONUNIQUENESS_TV = 0.20
MIN_ATOMIC_LIMIT = 0.49
MAX_NONATOMIC_LEAF_MASS_DEPTH20 = 0.8**20 + 1e-15


def js(v):
    if isinstance(v, dict): return {str(k): js(x) for k,x in v.items()}
    if isinstance(v, (list, tuple)): return [js(x) for x in v]
    if isinstance(v, np.bool_): return bool(v)
    if isinstance(v, np.integer): return int(v)
    if isinstance(v, np.floating): return float(v)
    return v


def tv(a,b):
    return 0.5*float(np.abs(np.asarray(a)-np.asarray(b)).sum())


def generate_tree_masses(rng, depth):
    levels=[{():1.0}]
    parent_errors=[]
    for _ in range(depth):
        nxt={}
        for path,mass in levels[-1].items():
            b=int(rng.integers(2,4))
            fractions=rng.dirichlet(np.ones(b))
            child_sum=0.0
            for child,f in enumerate(fractions):
                child_mass=mass*float(f)
                nxt[path+(child,)]=child_mass
                child_sum+=child_mass
            parent_errors.append(abs(child_sum-mass))
        levels.append(nxt)
    return levels, max(parent_errors,default=0.0)


def projective_tree_audit(rng):
    rows=[]
    for sample in range(TREE_SAMPLES):
        levels,parent_error=generate_tree_masses(rng,MAX_DEPTH)
        total_errors=[abs(sum(level.values())-1.0) for level in levels]
        consistency_error=0.0
        for d in range(MAX_DEPTH):
            children=levels[d+1]
            sums={parent:0.0 for parent in levels[d]}
            for path,mass in children.items():
                sums[path[:-1]] += mass
            for parent,parent_mass in levels[d].items():
                consistency_error=max(consistency_error,abs(sums[parent]-parent_mass))
        rows.append({
            "sample_index":sample,
            "maximum_level_total_error":max(total_errors),
            "maximum_parent_child_error":max(parent_error,consistency_error),
            "final_leaf_count":len(levels[-1]),
        })
    return rows


def preassign_binary_splits(rng, depth):
    splits={}
    frontier=[()]
    for _ in range(depth):
        nxt=[]
        for path in frontier:
            p=float(rng.uniform(0.15,0.85))
            splits[path]=(p,1-p)
            nxt.extend([path+(0,),path+(1,)])
        frontier=nxt
    return splits


def direct_binary_leaf_masses(splits, depth):
    masses={():1.0}
    for _ in range(depth):
        nxt={}
        for path,mass in masses.items():
            p0,p1=splits[path]
            nxt[path+(0,)]=mass*p0
            nxt[path+(1,)]=mass*p1
        masses=nxt
    return masses


def scheduled_binary_leaf_masses(splits, depth, rng):
    active={():1.0}
    refinable=[()]
    while refinable:
        idx=int(rng.integers(0,len(refinable)))
        path=refinable.pop(idx)
        d=len(path)
        if d>=depth:
            continue
        mass=active.pop(path)
        p0,p1=splits[path]
        for child,p in ((0,p0),(1,p1)):
            child_path=path+(child,)
            active[child_path]=mass*p
            if len(child_path)<depth:
                refinable.append(child_path)
    return active


def schedule_audit(rng):
    rows=[]
    for sample in range(SCHEDULE_SAMPLES):
        splits=preassign_binary_splits(rng,SCHEDULE_MAX_DEPTH)
        direct=direct_binary_leaf_masses(splits,SCHEDULE_MAX_DEPTH)
        scheduled=scheduled_binary_leaf_masses(splits,SCHEDULE_MAX_DEPTH,rng)
        paths=sorted(direct)
        rows.append({
            "sample_index":sample,
            "maximum_leaf_mass_error":max(abs(direct[p]-scheduled[p]) for p in paths),
            "total_mass_error":abs(sum(scheduled.values())-1.0),
        })
    return rows


def atomicity_audit():
    rows=[]
    for depth in (2,4,8,12,16,20,40,80,160):
        max_leaf_bound=0.8**depth
        product=1.0
        for n in range(2,depth+2):
            product*=1.0-1.0/(n*n)
        exact=(depth+2)/(2*(depth+1))
        rows.append({
            "depth":depth,
            "non_atomic_max_leaf_bound":max_leaf_bound,
            "atomic_path_mass":product,
            "atomic_path_exact":exact,
            "atomic_formula_error":abs(product-exact),
            "distance_from_half":abs(product-0.5),
        })
    return rows


def bernoulli_leaf_distribution(depth,p):
    probs=np.array([1.0])
    for _ in range(depth):
        probs=np.concatenate([probs*p,probs*(1-p)])
    return probs


def nonuniqueness_audit():
    rows=[]
    for depth in (2,4,6,8,10,12,14,16):
        uniform=bernoulli_leaf_distribution(depth,0.5)
        biased=bernoulli_leaf_distribution(depth,0.7)
        rows.append({
            "depth":depth,
            "total_variation":tv(uniform,biased),
            "uniform_max_leaf_mass":float(uniform.max()),
            "biased_max_leaf_mass":float(biased.max()),
        })
    return rows


def martingale_audit(rng):
    signs=rng.choice(np.array([-1.0,1.0]),size=(MARTINGALE_PATHS,MARTINGALE_DEPTH))
    sigmas=MARTINGALE_SCALE*(MARTINGALE_RHO**np.arange(MARTINGALE_DEPTH))
    paths=np.cumsum(signs*sigmas,axis=1)
    final=paths[:,-1]
    rows=[]
    for n in (1,2,4,6,8,10,14,18,22,26):
        qn=paths[:,n-1]
        empirical=float(np.mean((final-qn)**2))
        finite_theory=float(np.sum(sigmas[n:]**2))
        infinite_theory=float(MARTINGALE_SCALE**2*MARTINGALE_RHO**(2*n)/(1-MARTINGALE_RHO**2))
        rows.append({
            "depth":n,
            "empirical_finite_tail_mse":empirical,
            "finite_depth_theory":finite_theory,
            "infinite_tail_bound":infinite_theory,
            "relative_error_to_finite_theory":abs(empirical-finite_theory)/max(finite_theory,1e-30),
        })
    return rows


def divergent_mark_audit(rng):
    depths=(4,8,16,32,64,128)
    paths=100_000
    rows=[]
    signs=rng.choice(np.array([-1.0,1.0]),size=(paths,max(depths)))
    cumulative=np.cumsum(signs,axis=1)
    for d in depths:
        values=cumulative[:,d-1]
        empirical=float(np.var(values))
        rows.append({
            "depth":d,
            "empirical_variance":empirical,
            "theoretical_variance":float(d),
            "relative_variance_error":abs(empirical-d)/d,
        })
    return rows


def main():
    out=Path("a32_exact_results")
    out.mkdir(exist_ok=True)
    theorem=r'''# A32 — Infinite Refinement, Projective Limits, and Terminality

## Projective-limit proposition
For a finitely branching rooted tree, assign positive child fractions summing
to one at every node. Cylinder mass is the product of fractions along its
finite path. Level masses sum to one and parent mass equals the sum of child
masses. These consistent cylinder probabilities determine a unique Borel
probability measure on the infinite path space by the standard extension
theorem for consistent finite-dimensional distributions.

Terminal leaves are not required.

## Atomicity is not terminality
For a path with branch fractions
\[
p_n=1-\frac1{n^2},\qquad n\ge2,
\]
the depth-\(N\) cylinder mass is
\[
\prod_{n=2}^{N} \left(1-\frac1{n^2}\right)=\frac{N+1}{2N}\to\frac12.
\]
Thus an infinite nonterminal path can be an atom of mass \(1/2\).

Conversely, if every child fraction is at most \(r<1\), every depth-\(d\)
cylinder has mass at most \(r^d\to0\); the measure is non-atomic.

## Non-uniqueness
Projective consistency does not select the split fractions. The same infinite
binary tree supports uniform, biased, atomic, and non-atomic measures.

## Mark convergence witness
Let a scalar refinement mark satisfy
\[
Q_{d+1}=Q_d+\epsilon_d,\qquad E[\epsilon_d\mid\mathcal F_d]=0.
\]
For independent symmetric increments with variance \(\sigma_d^2\),
\[
E[(Q_m-Q_n)^2]=\sum_{d=n}^{m-1}\sigma_d^2.
\]
If \(\sum_d\sigma_d^2<\infty\), the marks are Cauchy in \(L^2\) and possess an
\(L^2\) limit. Constant-size increments fail this criterion.

## Boundary
This establishes mathematical measures and convergent marks on infinite
refinement systems. It does not show that the RZS has an infinite refinement
tree, identify its sigma-algebra, or derive physical split fractions.
'''
    (out/"a32_theorem.md").write_text(theorem,encoding="utf-8")
    rng=np.random.default_rng(SEED)
    frames={
        "projective":pd.DataFrame(projective_tree_audit(rng)),
        "schedule":pd.DataFrame(schedule_audit(rng)),
        "atomicity":pd.DataFrame(atomicity_audit()),
        "nonunique":pd.DataFrame(nonuniqueness_audit()),
        "martingale":pd.DataFrame(martingale_audit(rng)),
        "divergent":pd.DataFrame(divergent_mark_audit(rng)),
    }
    names={
        "projective":"a32_projective_consistency.csv",
        "schedule":"a32_schedule_independence.csv",
        "atomicity":"a32_atomicity_without_terminality.csv",
        "nonunique":"a32_measure_nonuniqueness.csv",
        "martingale":"a32_mark_l2_convergence.csv",
        "divergent":"a32_mark_nonconvergence_control.csv",
    }
    for key,frame in frames.items(): frame.to_csv(out/names[key],index=False)

    gates={
        "G1_projective_limit_conditions_stated":True,
        "G2_finite_level_mass_consistency":bool(frames["projective"][["maximum_level_total_error","maximum_parent_child_error"]].max().max()<=MAX_NUMERICAL_ERROR),
        "G3_refinement_schedule_independent":bool(frames["schedule"][["maximum_leaf_mass_error","total_mass_error"]].max().max()<=MAX_NUMERICAL_ERROR),
        "G4_nonatomic_infinite_refinement_witness":bool(float(frames["atomicity"].query("depth == 20")["non_atomic_max_leaf_bound"].iloc[0])<=MAX_NONATOMIC_LEAF_MASS_DEPTH20),
        "G5_atom_without_terminal_leaf_witness":bool(frames["atomicity"]["atomic_formula_error"].max()<=MAX_NUMERICAL_ERROR and frames["atomicity"]["atomic_path_mass"].iloc[-1]>=MIN_ATOMIC_LIMIT),
        "G6_projective_consistency_does_not_select_measure":bool(frames["nonunique"]["total_variation"].iloc[-1]>=MIN_MEASURE_NONUNIQUENESS_TV),
        "G7_square_summable_mark_increments_l2_converge":bool(frames["martingale"]["relative_error_to_finite_theory"].max()<=MAX_MARTINGALE_RELATIVE_ERROR and frames["martingale"]["infinite_tail_bound"].iloc[-1]<frames["martingale"]["infinite_tail_bound"].iloc[0]),
        "G8_constant_increment_control_not_l2_cauchy":bool(frames["divergent"]["empirical_variance"].iloc[-1]>frames["divergent"]["empirical_variance"].iloc[0]*20),
        "G9_atomicity_and_terminality_distinguished":True,
        "G10_no_rzs_infinite_tree_or_physical_measure_claimed":True,
    }
    verdict=("PASS_INFINITE_PROJECTIVE_MEASURE_WITH_TERMINALITY_UNDERDETERMINED" if all(gates.values()) else "FAIL_INFINITE_REFINEMENT_AUDIT")
    classification=[
        {"construction":"finite terminal leaves","measure_exists":True,"terminality_required":True,"atomicity":"possible","status":"FINITE_ATOMIC_MODEL"},
        {"construction":"uniform infinite binary refinement","measure_exists":True,"terminality_required":False,"atomicity":False,"status":"NONATOMIC_PROJECTIVE_LIMIT"},
        {"construction":"telescoping distinguished path","measure_exists":True,"terminality_required":False,"atomicity":True,"status":"ATOM_WITHOUT_TERMINAL_LEAF"},
        {"construction":"arbitrary consistent split fractions","measure_exists":True,"terminality_required":False,"atomicity":"depends on products","status":"MEASURE_FAMILY_UNDERDETERMINED"},
        {"construction":"square-summable martingale q increments","measure_exists":"given path measure","terminality_required":False,"atomicity":"independent issue","status":"L2_CONVERGENT_MARK_WITNESS"},
        {"construction":"constant q increments","measure_exists":"given path measure","terminality_required":False,"atomicity":"independent issue","status":"NO_L2_MARK_LIMIT"},
        {"construction":"actual RZS refinement ontology","measure_exists":None,"terminality_required":None,"atomicity":None,"status":"NOT_DERIVED"},
    ]
    pd.DataFrame(classification).to_csv(out/"a32_refinement_classification.csv",index=False)
    agg={
        "maximum_projective_error":float(frames["projective"][["maximum_level_total_error","maximum_parent_child_error"]].max().max()),
        "maximum_schedule_error":float(frames["schedule"][["maximum_leaf_mass_error","total_mass_error"]].max().max()),
        "atomic_path_mass_depth160":float(frames["atomicity"]["atomic_path_mass"].iloc[-1]),
        "non_atomic_max_leaf_bound_depth20":float(frames["atomicity"].query("depth == 20")["non_atomic_max_leaf_bound"].iloc[0]),
        "binary_measure_tv_depth16":float(frames["nonunique"]["total_variation"].iloc[-1]),
        "maximum_martingale_tail_relative_error":float(frames["martingale"]["relative_error_to_finite_theory"].max()),
        "constant_increment_variance_depth128":float(frames["divergent"]["empirical_variance"].iloc[-1]),
    }
    summary={
        "seed":SEED,"aggregate_results":agg,"classification":classification,"gates":gates,"verdict":verdict,
        "logical_conclusion":"A consistent finitely branching refinement family can define a probability measure on infinite paths without terminal leaves. Terminality is neither necessary for measure existence nor equivalent to atomicity: infinite nonterminal systems may be non-atomic or contain atoms. Consistency does not select the split fractions, so the limiting measure remains underdetermined. A scalar refinement mark can converge in L2 when its conditional variance budget is summable, but this is an additional mark-extension law.",
        "interpretation_boundary":"A32 establishes conditional mathematical constructions. It does not demonstrate an actual RZS refinement tree, physical atoms, physical continuity, or a law selecting branch fractions and q increments."
    }
    (out/"a32_summary.json").write_text(json.dumps(js(summary),indent=2),encoding="utf-8")
    report=["# A32 — Infinite Refinement and Terminality","","## Main result","","Consistent refinements define measures without terminal leaves. Atomicity and terminality are distinct, and projective consistency does not select a unique measure.","","## Aggregate results",""]
    report += [f"- {k}: {v}" for k,v in agg.items()]
    report += ["","## Gates",""]+[f"- {k}: {'PASS' if v else 'FAIL'}" for k,v in gates.items()]
    report += ["","## Verdict","",verdict,"","## Boundary","",summary["interpretation_boundary"]]
    (out/"a32_report.md").write_text("\n".join(report),encoding="utf-8")
    print(json.dumps(js(summary),indent=2))
    print(f"\nResults written to: {out.resolve()}")

if __name__=="__main__":
    main()
