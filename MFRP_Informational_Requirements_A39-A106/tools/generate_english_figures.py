#!/usr/bin/env python3
"""Generate English-language figures from the stored audit result JSON files.

The figures are publication-facing summaries. Exact numerical and symbolic
claims remain in results/*.json and audits/*.py.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from fractions import Fraction

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIG = ROOT / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def load(name: str):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def save(name: str, title: str, xlabel: str = "", ylabel: str = "", *, legend=True, ylog=False, xlog=False, rotate=0):
    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if ylog:
        plt.yscale("log")
    if xlog:
        plt.xscale("log")
    if rotate:
        plt.xticks(rotation=rotate)
    plt.grid(True)
    if legend:
        handles, labels = plt.gca().get_legend_handles_labels()
        if handles:
            plt.legend()
    plt.tight_layout()
    plt.savefig(FIG / name, dpi=180)
    plt.close()


def risk(ratio):
    return 0.5 * np.log2(np.asarray(ratio, dtype=float))


def eval_expr(expr: str, variable: str, values):
    sym = sp.Symbol(variable)
    parsed = sp.sympify(expr)
    roots = list(parsed.atoms(sp.CRootOf))
    if roots:
        # Every stored CRootOf in A52-A57 refers to the same certified s-star.
        parsed = parsed.xreplace({root: sp.Float("0.15089310440819246869427271203663056829344524984640") for root in roots})
    fun = sp.lambdify(sym, parsed, "numpy")
    out = np.asarray(fun(values), dtype=float)
    if out.ndim == 0:
        out = np.full_like(np.asarray(values, dtype=float), float(out), dtype=float)
    return out


def piecewise_risk(data, phase_key, transition_coordinate, domain, transform):
    phases = list(data[phase_key].values())
    boundaries = [domain[0]] + [float(x[transition_coordinate]) for x in data["transition_table"]] + [domain[1]]
    xs_all, ys_all = [], []
    for i, phase in enumerate(phases):
        lo, hi = boundaries[i], boundaries[i + 1]
        if hi <= lo:
            continue
        xs = np.linspace(lo, hi, max(8, int(250 * (hi - lo) / (domain[1] - domain[0])) + 2), endpoint=(i == len(phases)-1))
        svals = transform(xs)
        try:
            ratios = eval_expr(phase["ratio"], "s", svals)
            ys = risk(ratios)
        except Exception:
            continue
        finite = np.isfinite(ys)
        xs_all.append(xs[finite]); ys_all.append(ys[finite])
    if xs_all:
        return np.concatenate(xs_all), np.concatenate(ys_all)
    return np.array([]), np.array([])


def figures_a47():
    d = load("a47_global_noise_separation_phase_diagram_results.json")
    gamma = np.linspace(3, 12, 500)
    r = 2.0 ** (-gamma)
    plt.figure(figsize=(10, 6))
    for key, expr in d["boundaries"].items():
        y = eval_expr(expr, "r", r)
        plt.plot(gamma, y, label=key)
    plt.axhline(1e-4, linestyle="--", label=r"Benchmark $\varepsilon=10^{-4}$")
    save("a47_global_phase_diagram.png", "A47 — Global noise-separation phase boundaries", r"Third exponent $\gamma$", r"Absolute error $\varepsilon$")


def figures_a51():
    d = load("a51_target_exclusion_distance_results.json")
    delta = np.linspace(0.001, 1.999, 800)
    s = 2.0 ** (-(1 + delta))
    exact_ratio = eval_expr(d["exact_result"]["ratio"], "s", s)
    xn, yn = piecewise_risk(d, "noisy_phases", "delta_decimal", (0.0, 2.0), lambda x: 2.0 ** (-(1+x)))
    plt.figure(figsize=(10, 6))
    plt.plot(delta, risk(exact_ratio), label="Exact observations")
    if len(xn): plt.plot(xn, yn, label=r"Noise $\varepsilon=10^{-4}$")
    save("a51_target_exclusion_distance_risk.png", "A51 — Target-exclusion distance law", r"Minimum exclusion distance $\delta$", "Future minimax risk")


def figures_a52():
    d = load("a52_continuous_second_anchor_results.json")
    beta = np.linspace(2.001, 3.999, 800)
    s = 2.0 ** (-beta)
    exact_ratio = eval_expr(d["exact_result"]["ratio"], "s", s)
    xn, yn = piecewise_risk(d, "noisy_phases", "beta_decimal", (2.0, 4.0), lambda x: 2.0 ** (-x))
    plt.figure(figsize=(10, 6))
    plt.plot(beta, risk(exact_ratio), label="Exact observations")
    if len(xn): plt.plot(xn, yn, label=r"Noise $\varepsilon=10^{-4}$")
    beta_star = float(d["stationary_result"]["beta_star_decimal"])
    risk_star = float(d["stationary_result"]["future_risk_star_decimal"])
    plt.scatter([beta_star], [risk_star], label=r"Certified $\beta^\star$")
    save("a52_continuous_second_anchor_risk.png", "A52 — Continuous relaxation of the second anchor", r"Second anchor $\beta$", "Future minimax risk")


def figures_a53():
    d = load("a53_coupled_second_third_anchor_results.json")
    caps = d["numerical_reconnaissance"]["finite_caps"]
    gamma = [30 if x["gamma_cap"] == "infinity" else float(x["gamma_cap"]) for x in caps]
    rs = [float(x["future_risk"]) for x in caps]
    betas = [float(x["beta_optimum"]) for x in caps]
    plt.figure(figsize=(10, 6))
    plt.plot(gamma, rs, marker="o", label="Optimized future risk")
    plt.xlabel(r"Third-anchor cap $\Gamma$ (30 denotes infinity)")
    plt.ylabel("Future minimax risk")
    ax = plt.gca().twinx()
    ax.plot(gamma, betas, marker="x", label=r"Optimized $\beta$")
    ax.set_ylabel(r"Optimized second anchor $\beta$")
    plt.title("A53 — Coupled second- and third-anchor optimization")
    plt.grid(True)
    plt.tight_layout(); plt.savefig(FIG / "a53_coupled_anchor_risk_curves.png", dpi=180); plt.close()


def figures_a54():
    d = load("a54_universal_continuum_witness_results.json")
    expr = sp.sympify(d["universal_certificate"]["difference_polynomial"])
    roots = list(expr.atoms(sp.CRootOf))
    sstar = sp.Float(d["universal_certificate"]["s_star_decimal"])
    expr = expr.xreplace({root: sstar for root in roots})
    r = sp.Symbol("r")
    fun = sp.lambdify(r, expr, "numpy")
    eta = np.linspace(2, 15, 700)
    y = np.asarray(fun(2.0 ** (-eta)), dtype=float)
    plt.figure(figsize=(10, 6))
    plt.plot(eta, y, label=r"$L_{p^\star}(\eta)-L_{q^\star}(\eta)$")
    plt.axhline(2e-4, label="Upper tolerance")
    plt.axhline(-2e-4, label="Lower tolerance")
    plt.axvline(float(d["universal_certificate"]["beta_star_decimal"]), linestyle="--", label=r"$\beta^\star$")
    save("a54_universal_continuum_witness_band.png", "A54 — Universal witness across the observation continuum", r"Observed exponent $\eta$", "Transform difference")


def figures_a55():
    d = load("a55_finite_cap_implementability_results.json")
    table = d["finite_cap_table"]
    gamma = [x["gamma"] for x in table]
    absolute = [float(x["absolute_excess_decimal"]) for x in table]
    relative = [float(x["relative_excess_percent"]) for x in table]
    plt.figure(figsize=(9, 6)); plt.plot(gamma, absolute, marker="o")
    save("a55_finite_cap_absolute_convergence.png", "A55 — Absolute convergence to the compactified optimum", r"Finite third-anchor cap $\Gamma$", "Absolute risk excess", ylog=True, legend=False)
    plt.figure(figsize=(9, 6)); plt.plot(gamma, relative, marker="o")
    save("a55_finite_cap_relative_convergence.png", "A55 — Relative loss from replacing infinity by a finite cap", r"Finite third-anchor cap $\Gamma$", "Relative risk excess (%)", ylog=True, legend=False)


def figures_a56():
    d = load("a56_cost_regularized_finite_cap_results.json")
    rt = d["risk_table"]
    gamma = [x["gamma"] for x in rt]
    risks = [float(x["risk_decimal"]) for x in rt]
    gains = [float(x.get("next_step_gain_decimal") or np.nan) for x in rt]
    plt.figure(figsize=(9, 6)); plt.plot(gamma, gains, marker="o")
    save("a56_break_even_costs.png", "A56 — Strictly decreasing marginal return", r"Upgrade from $\Gamma$ to $\Gamma+1$", "Break-even unit cost", ylog=True, legend=False)
    policy = d["example_policy"]
    costs = [float(x["cost_decimal"]) for x in policy]
    selected = [x["selected_gamma"] for x in policy]
    plt.figure(figsize=(9, 6)); plt.step(costs, selected, where="mid"); plt.scatter(costs, selected)
    save("a56_cost_selected_cap_policy.png", "A56 — Cost-selected finite-cap policy", "Abstract unit cost", r"Selected cap $\Gamma$", xlog=True, legend=False)
    plt.figure(figsize=(9, 6)); plt.plot(gamma, risks, marker="o")
    save("a56_risk_complexity_frontier.png", "A56 — Risk–complexity frontier", r"Finite cap $\Gamma$", "Future minimax risk", legend=False)


def figures_a57():
    d = load("a57_heteroscedastic_third_channel_results.json")
    table = d["break_even_policy"]["baseline_table"]
    gamma = [x["gamma"] for x in table]
    allowed = [float(x["allowed_percent"]) for x in table]
    plt.figure(figsize=(9, 6)); plt.plot(gamma, allowed, marker="o")
    save("a57_allowed_noise_increase.png", "A57 — Allowable next-channel noise increase", r"Current cap $\Gamma$", "Allowable deterioration (%)", ylog=True, legend=False)
    factors = np.linspace(1, 1.5, 80)
    plt.figure(figsize=(9, 6))
    for g in [6, 9, 12, 15]:
        threshold = next(float(x["maximum_next_factor_decimal"]) for x in table if x["gamma"] == g)
        plt.plot(factors, threshold * factors / factors[0], label=rf"$\Gamma={g}$")
    plt.plot(factors, factors, linestyle="--", label="No-upgrade boundary")
    save("a57_upgrade_threshold_map.png", "A57 — Exact upgrade decision map", "Current noise factor", "Maximum next-channel factor")


def figures_a58():
    d = load("a58_independent_three_channel_error_results.json")
    slopes = d["baseline"]["risk_slopes"]
    labels = [r"Channel $2$", r"Channel $\beta$", r"Channel $\infty$"]
    vals = [float(slopes[k]["decimal"]) for k in ["u2", "ub", "ui"]]
    plt.figure(figsize=(8, 6)); plt.bar(labels, vals)
    save("a58_channel_sensitivity_priority.png", "A58 — Calibration priority across three channels", ylabel="Risk sensitivity", legend=False)
    impacts = d["individual_ten_percent_impacts"]
    vals = [float(impacts[k]["relative_increase_percent"]) for k in ["u2", "ub", "ui"]]
    plt.figure(figsize=(8, 6)); plt.bar(labels, vals)
    save("a58_individual_error_impacts.png", "A58 — Effect of a 10% deterioration in each channel", ylabel="Relative risk increase (%)", legend=False)


def figures_a59():
    d = load("a59_correlated_ellipsoidal_calibration_results.json")
    cases = d["cases"]
    rho = [float(x["correlation"]) for x in cases]
    risks = [float(x["risk"]) for x in cases]
    exact = [float(x["exact_excess"]) for x in cases]
    linear = [float(x["linear_excess"]) for x in cases]
    vectors = np.array([[float(v) for v in x["worst_error_factors"]] for x in cases])
    plt.figure(figsize=(9, 6)); plt.plot(rho, exact, marker="o", label="Exact nonlinear excess"); plt.plot(rho, linear, marker="x", label="First-order prediction")
    save("a59_exact_vs_linear_correlation.png", "A59 — Exact solution versus local linear approximation", "Common correlation", "Risk excess over the center")
    plt.figure(figsize=(9, 6)); plt.plot(rho, risks, marker="o")
    save("a59_risk_vs_correlation.png", "A59 — Robust risk amplification under correlation", "Common correlation", "Future robust risk", legend=False)
    plt.figure(figsize=(9, 6))
    for i, label in enumerate([r"$u_2^\star$", r"$u_\beta^\star$", r"$u_\infty^\star$"]): plt.plot(rho, vectors[:, i], marker="o", label=label)
    save("a59_worst_direction_vs_correlation.png", "A59 — Adversarial calibration direction", "Common correlation", "Worst-case error factor")


def figures_a60():
    d = load("a60_general_covariance_matrix_results.json")
    cases = d["cases"]
    labels = [x["name"].replace("_", " ") for x in cases]
    risks = [float(x["robust_risk"]) for x in cases]
    vectors = np.array([[float(v) for v in x["worst_error_factors"]] for x in cases])
    plt.figure(figsize=(10, 6)); plt.bar(labels, risks); save("a60_general_covariance_risks.png", "A60 — Robust risk under general covariance matrices", ylabel="Future robust risk", rotate=25, legend=False)
    x = np.arange(len(labels)); w=.25
    plt.figure(figsize=(11, 6))
    for i, lab in enumerate([r"$u_2^\star$", r"$u_\beta^\star$", r"$u_\infty^\star$"]): plt.bar(x+(i-1)*w, vectors[:,i], w, label=lab)
    plt.xticks(x, labels, rotation=25); save("a60_general_covariance_worst_vectors.png", "A60 — Worst directions by covariance model", ylabel="Worst-case error factor")
    diag = cases[0]["local_covariance_diagnostic"]
    marg = [float(v) for v in diag["marginal_contributions"]]
    pair_names = list(diag["pairwise_contributions"].keys()); pair = [float(diag["pairwise_contributions"][k]) for k in pair_names]
    plt.figure(figsize=(10, 6)); plt.bar(["Channel 2", "Channel beta", "Channel infinity"]+pair_names, marg+pair)
    save("a60_covariance_contributions.png", "A60 — Local covariance contribution decomposition", ylabel="Contribution to local variance", rotate=25, legend=False)


def figures_a61():
    d = load("a61_spectral_covariance_uncertainty_results.json")
    table = d["risk_table"]
    tau = np.array([float(x["tau_decimal"]) for x in table])
    upper = np.array([float(x["upper_risk"]) for x in table])
    premium = np.array([float(x["upper_premium"]) for x in table])
    factors = np.array([[float(v) for v in x["upper_worst_error_factors"]] for x in table])
    lower = np.array([float(x["lower_risk"]) if x["lower_risk"] is not None else np.nan for x in table])
    plt.figure(figsize=(9, 6)); plt.plot(tau[1:], premium[1:], marker="o")
    save("a61_covariance_uncertainty_premium.png", "A61 — Premium from covariance uncertainty", r"Spectral radius $\tau$", "Additional robust risk", xlog=True, ylog=True, legend=False)
    plt.figure(figsize=(9, 6)); plt.plot(tau, upper, marker="o", label="Exact upper endpoint"); plt.plot(tau, lower, marker="o", label="Exact lower endpoint"); plt.axhline(float(d["point_estimate"]["robust_risk"]), label="Point estimate")
    save("a61_spectral_risk_interval.png", "A61 — Risk interval induced by covariance uncertainty", r"Spectral radius $\tau$", "Future robust risk")
    plt.figure(figsize=(9, 6))
    for i, lab in enumerate([r"$u_2^\star$", r"$u_\beta^\star$", r"$u_\infty^\star$"]): plt.plot(tau, factors[:,i], marker="o", label=lab)
    save("a61_worst_vector_vs_tau.png", "A61 — Worst direction under spectral inflation", r"Spectral radius $\tau$", "Worst-case error factor")


def figures_a62():
    d = load("a62_bootstrap_spectral_protocol_results.json")
    cells = d["validation_cells"]
    labels = [f"{x['model_family']}\n{x['scenario']}\nn={x['sample_size']}" for x in cells]
    raw = [100*x["raw_coverage"] for x in cells]; cal=[100*x["calibrated_coverage"] for x in cells]
    x=np.arange(len(labels)); w=.38
    plt.figure(figsize=(14, 6)); plt.bar(x-w/2, raw, w, label="Raw bootstrap"); plt.bar(x+w/2, cal, w, label="Calibrated"); plt.axhline(95, linestyle="--", label="95% target"); plt.xticks(x, labels, rotation=35)
    save("a62_bootstrap_coverage_validation.png", "A62 — Bootstrap coverage before and after calibration", ylabel="Coverage (%)")
    rawv=[100*x["raw_contract_valid_rate"] for x in cells]; calv=[100*x["calibrated_contract_valid_rate"] for x in cells]
    plt.figure(figsize=(14, 6)); plt.bar(x-w/2, rawv,w,label="Raw radius"); plt.bar(x+w/2,calv,w,label="Calibrated radius"); plt.xticks(x,labels,rotation=35)
    save("a62_contract_availability.png", "A62 — Certified-contract availability after calibration", ylabel="Contract-valid rate (%)")
    plt.figure(figsize=(9, 6))
    for family, trace in d["calibration_traces"].items():
        factors=[float(z["factor"]) for z in trace]; mins=[float(z["minimum_coverage"]) for z in trace]
        plt.plot(factors, mins, marker="o", label=family.replace("_", " "))
    plt.axhline(.95, linestyle="--", label="95% target")
    save("a62_required_inflation_factors.png", "A62 — Required bootstrap-radius inflation", "Calibration factor", "Minimum calibration coverage")


def figures_a63():
    d=load("a63_structural_generalization_results.json")
    rows=d["contracts"]
    noisy=[x for x in rows if x["epsilon"]=="1/10000"]
    labels=[f"mu{x['target_exponent']}-{x['mean_mode']}-M{x['maximum']}" for x in noisy]
    offsets=[x["winner"][2]-x["target_exponent"] for x in noisy]
    plt.figure(figsize=(13,6)); plt.bar(labels,offsets); plt.axhline(3,label="Exact-data third-anchor offset"); save("a63_noisy_anchor_atlas.png","A63 — Noisy third-anchor atlas",ylabel=r"Optimal offset $\lambda_3-\mu$",rotate=55)
    plt.figure(figsize=(10,7))
    for target in [1,2]:
        for mode in ["central","lower"]:
            sel=sorted([x for x in noisy if x["target_exponent"]==target and x["mean_mode"]==mode],key=lambda z:z["maximum"])
            plt.plot([x["maximum"] for x in sel],[x["winner"][2]-target for x in sel],marker="o",label=f"mu={target}, {mode} mean")
    save("a63_noisy_third_anchor_offsets.png","A63 — The noisy third anchor is contract dependent",r"Support maximum $M$",r"Third-anchor offset $\lambda_3-\mu$")
    plt.figure(figsize=(10,7))
    for target in [1,2]:
        for eps,label in [("0","exact"),("1/10000","noisy")]:
            sel=sorted([x for x in rows if x["target_exponent"]==target and x["mean_mode"]=="central" and x["epsilon"]==eps],key=lambda z:z["maximum"])
            plt.plot([x["maximum"] for x in sel],[float(x["winner_risk_decimal"]) for x in sel],marker="o",label=f"mu={target}, {label}")
    save("a63_risk_vs_support_size.png","A63 — Risk versus microscopic support size",r"Support maximum $M$","Future minimax risk")


def figures_a64():
    d=load("a64_scale_normalized_boundary_pair_results.json"); s=d["atlas_summary"]
    plt.figure(figsize=(9,6)); plt.bar(["First anchor at mu+1","Boundary-pair optimum exists","Every optimum has pair"],[s["all_first_boundary_count"],s["boundary_pair_exists_count"],s["all_optimizers_have_pair_count"]]); plt.axhline(240,label="All contracts")
    save("a64_boundary_pair_counts.png","A64 — Persistence of boundary anchors",ylabel="Number of contracts",rotate=10)
    align=s["translation_alignment_by_delta"]; keys=["0","1/7500","1/1875","1/750"]
    plt.figure(figsize=(9,6)); plt.bar(keys,[100*align[k]["fraction"] for k in keys]); save("a64_target_translation_alignment.png","A64 — Target-shift alignment",r"Relative error $\delta$","Aligned groups (%)",legend=False)
    rows=d["contracts"]; baseline=[x for x in rows if x["delta"]=="1/1875" and x["mean_fraction"]=="1/2"]
    plt.figure(figsize=(10,7))
    for target in [1,2,3]:
        sel=sorted([x for x in baseline if x["target_exponent"]==target],key=lambda z:z["maximum"])
        plt.plot([x["maximum"] for x in sel],[x["winner"][2]-target for x in sel],marker="o",label=f"mu={target}")
    save("a64_normalized_third_anchor_offsets.png",r"A64 — Third anchor at $\delta=1/1875$ and central mean",r"Support maximum $M$",r"Third-anchor offset $\lambda_3-\mu$")


def figures_a65():
    d=load("a65_continuous_first_anchor_results.json")
    cert=d["local_certificates"]
    plt.figure(figsize=(9,6)); plt.hist([float(x["kappa_alpha_decimal"]) for x in cert],bins=30); save("a65_boundary_sensitivity_distribution.png","A65 — Exact boundary-sensitivity distribution",r"Exact factor $\kappa_\alpha$","Number of contracts",legend=False)
    sc=d["scan_contracts"]
    order=["0","1/7500","1/1875","1/750"]; pos={k:i for i,k in enumerate(order)}
    plt.figure(figsize=(10,7))
    for M in sorted({x["maximum"] for x in sc}):
        sel=[x for x in sc if x["maximum"]==M]
        plt.scatter([pos[x["delta"]] for x in sel],[x["minimum_adjacent_increment"] for x in sel],label=f"M={M}",alpha=.7)
    plt.xticks(range(len(order)),order); plt.yscale("log"); save("a65_continuous_grid_margins.png","A65 — Positive margins in the continuous stress atlas",r"Relative error $\delta$","Smallest adjacent ratio increase")
    summ=d["local_certificate_summary"]
    plt.figure(figsize=(9,6)); plt.bar(["Strict local certificate","Positive derivative, degenerate basis","Unresolved degeneracy"],[summ["strict_local_basis_count"],summ["degenerate_derivative_certificate_count"],summ["unresolved_degenerate_count"]]); plt.axhline(240,label="All contracts")
    save("a65_local_certificate_coverage.png","A65 — Coverage of exact local certificates",ylabel="Contracts",rotate=10)
    curves=d["curve_rows"]
    cond=[(5,"1/4",1,"0"),(5,"1/4",3,"1/1875"),(6,"1/2",1,"1/750"),(7,"2/5",2,"1/7500"),(8,"1/3",3,"1/1875"),(9,"1/2",1,"1/1875")]
    plt.figure(figsize=(10,7))
    for M,mf,mu,de in cond:
        sel=sorted([x for x in curves if x["maximum"]==M and x["mean_fraction"]==mf and x["target_exponent"]==mu and x["delta"]==de],key=lambda z:z["alpha_offset"])
        plt.plot([x["alpha_offset"] for x in sel],[x["risk"] for x in sel],label=f"M={M}, m/M={mf}, mu={mu}, delta={de}")
    save("a65_representative_first_anchor_curves.png","A65 — Moving the first anchor away increases risk",r"Relative first anchor $\alpha-\mu$","Future minimax risk")


def phase_plot(result, contract_key, phases_key, transitions_key, out_curve, out_map, title_curve, title_map, alpha_lo, alpha_hi):
    phases=result[contract_key][phases_key] if contract_key else result[phases_key]
    transitions=result[contract_key][transitions_key] if contract_key else result[transitions_key]
    bounds=[alpha_lo]+[float(x["boundary"]["alpha_decimal"]) for x in transitions]+[alpha_hi]
    funcs=[sp.lambdify(sp.Symbol("s"),sp.sympify(x["ratio"]),"numpy") for x in phases]
    alpha=np.linspace(alpha_lo,alpha_hi-1e-5,1400); vals=[]
    for a in alpha:
        idx=min(np.searchsorted(bounds[1:],a,side="right"),len(funcs)-1); vals.append(.5*math.log2(float(funcs[idx](2**(-a)))))
    plt.figure(figsize=(10,7)); plt.plot(alpha,vals)
    for b in bounds[1:-1]: plt.axvline(b,linestyle="--")
    plt.scatter([alpha_lo],[vals[0]],label="Global optimum"); save(out_curve,title_curve,r"First anchor $\alpha$","Future minimax risk")
    plt.figure(figsize=(11,5))
    for i,(l,r) in enumerate(zip(bounds[:-1],bounds[1:]),1): plt.barh([0],[r-l],left=[l],height=.45); plt.text((l+r)/2,0,str(i),ha="center",va="center")
    plt.xlim(alpha_lo,alpha_hi); plt.yticks([]); save(out_map,title_map,r"First anchor $\alpha$",legend=False)


def figures_a66():
    d=load("a66_exact_global_phase_results.json")
    phase_plot(d,"canonical","phases","transitions","a66_canonical_global_monotonicity.png","a66_canonical_phase_map.png","A66 — Global continuous theorem for the canonical contract","A66 — Seven algebraic phases of the canonical contract",2,3)
    deg=d["degenerate"]; f=sp.lambdify(sp.Symbol("s"),sp.sympify(deg["ratio"]),"numpy"); a=np.linspace(4,5-1e-5,1000); y=[.5*math.log2(float(f(2**(-x)))) for x in a]
    plt.figure(figsize=(10,7)); plt.plot(a,y); plt.scatter([4],[y[0]],label="Global optimum"); save("a66_degenerate_global_monotonicity.png","A66 — Global theorem for the degenerate contract",r"First anchor $\alpha$","Future minimax risk")


def figures_a67():
    d=load("a67_central_mean_support_family_results.json"); supports=d["supports"]
    plt.figure(figsize=(10,7))
    for item in supports:
        bounds=[2]+[float(x["boundary"]["alpha_decimal"]) for x in item["transitions"]]+[3]
        funcs=[sp.lambdify(sp.Symbol("s"),sp.sympify(x["ratio"]),"numpy") for x in item["phases"]]
        a=np.linspace(2,3-1e-5,1000); y=[]
        for aa in a:
            idx=min(np.searchsorted(bounds[1:],aa,side="right"),len(funcs)-1); y.append(.5*math.log2(float(funcs[idx](2**(-aa)))))
        plt.plot(a,y,label=f"M={item['maximum']}")
    save("a67_support_family_risk_curves.png","A67 — Global theorem for five support sizes",r"First anchor $\alpha$","Future minimax risk")
    Ms=[x["maximum"] for x in supports]; phases=[x["phase_count"] for x in supports]; trans=[x["transition_count"] for x in supports]; x=np.arange(len(Ms)); w=.38
    plt.figure(figsize=(9,6)); plt.bar(x-w/2,phases,w,label="Phases"); plt.bar(x+w/2,trans,w,label="Transitions"); plt.xticks(x,Ms); save("a67_support_family_phase_counts.png","A67 — Algebraic complexity by support size",r"Support maximum $M$","Count")
    plt.figure(figsize=(10,7))
    for item in supports: plt.scatter([float(x["boundary"]["alpha_decimal"]) for x in item["transitions"]],[item["maximum"]]*item["transition_count"],label=f"M={item['maximum']}")
    save("a67_support_family_transition_map.png","A67 — Map of 28 algebraic transitions",r"Transition position in $\alpha$",r"Support maximum $M$")
    plt.figure(figsize=(9,6)); plt.plot(Ms,[float(x["boundary_risk_decimal"]) for x in supports],marker="o",label=r"$Q_M(2)$"); plt.plot(Ms,[float(x["coalescence_risk_limit_decimal"]) for x in supports],marker="o",label=r"$Q_M(3^-)$")
    save("a67_risk_vs_support_size.png","A67 — Risk at the boundary and at coalescence",r"Support maximum $M$","Future minimax risk")


def figures_a68():
    d=load("a68_dual_envelope_channel_value_results.json"); a=d["phase_activity_counts"]
    labs=[r"$\alpha+$",r"$\alpha$ inactive",r"$\beta-$",r"$\beta$ inactive",r"$\gamma+$",r"$\gamma-$",r"$\gamma$ inactive"]
    vals=[a["alpha_positive"],a["alpha_inactive"],a["beta_negative"],a["beta_inactive"],a["gamma_positive"],a["gamma_negative"],a["gamma_inactive"]]
    plt.figure(figsize=(10,6)); plt.bar(labs,vals); plt.axhline(33,label="All phases"); save("a68_dual_channel_activity.png","A68 — Dual activity of observation channels",ylabel="Number of phases")
    rem=d["channel_removal_theorem"]["results"]; M=[x["maximum"] for x in rem]
    plt.figure(figsize=(9,6)); plt.plot(M,[float(x["full_boundary_risk_decimal"]) for x in rem],marker="o",label="Three channels"); plt.plot(M,[float(x["removed_risk_decimal"]) for x in rem],marker="o",label=r"Without $\alpha$")
    save("a68_first_channel_removal_risk.png","A68 — Exact cost of removing the first channel",r"Support maximum $M$","Future minimax risk")
    plt.figure(figsize=(9,6)); plt.plot(M,[float(x["risk_multiplier"]) for x in rem],marker="o")
    save("a68_first_channel_value_multiplier.png","A68 — Risk multiplier after first-channel removal",r"Support maximum $M$","Risk multiplier",legend=False)


def figures_a69():
    d=load("a69_cramer_chebyshev_reduction_results.json"); p=d["phase_records"]
    labels=[f"M{x['maximum']}-P{x['phase']}" for x in p]; x=np.arange(len(labels)); w=.38
    plt.figure(figsize=(15,6)); plt.bar(x-w/2,[x["declared_numerator_sign"] for x in p],w,label=r"sign $\Delta_\alpha$"); plt.bar(x+w/2,[x["declared_determinant_sign"] for x in p],w,label=r"sign $\Delta$"); plt.xticks(x,labels,rotation=60); plt.yticks([-1,0,1]); save("a69_cramer_orientation_map.png","A69 — Cramer orientations across 33 phases",ylabel="Orientation")
    finite=[x for x in p if x["flip_margin_multiple"] is not None]; plt.figure(figsize=(11,6)); plt.bar([f"M{x['maximum']}-P{x['phase']}" for x in finite],[float(x["flip_margin_multiple"]) for x in finite]); plt.axhline(100,label="100x margin"); save("a69_numerator_flip_margins.png","A69 — Margin to a numerator-sign reversal",ylabel=r"$\varepsilon_{flip}/\varepsilon_{declared}$",ylog=True,rotate=55)
    sig=d["contact_signatures"]; plt.figure(figsize=(11,6)); plt.bar(range(1,len(sig)+1),[x["instance_count"] for x in sig]); save("a69_contact_signature_counts.png","A69 — Compression into 18 contact signatures","Contact-signature class","Number of phases",legend=False)
    c=d["order_only_counterexample"]; vals=[float(sp.Rational(c["uniform_numerator"])),float(sp.Rational(c["stretched_numerator"]))]; plt.figure(figsize=(8,6)); plt.bar(["Uniform\n0,1,2,3,4,5","Stretched\n0,1,2,3,4,9"],vals); plt.axhline(0)
    save("a69_order_only_counterexample.png","A69 — Exact counterexample to an order-only rule",ylabel=r"Cramer numerator $\Delta_\alpha$",legend=False)


def figures_a70():
    d=load("a70_signed_q_schur_dominance_results.json"); p=d["phases"]; labels=[f"M{x['maximum']}-P{x['phase']}" for x in p]
    plt.figure(figsize=(15,6)); plt.bar(labels,[float(x["dominance_ratio_decimal"]) for x in p]); plt.axhline(1,label="Sign threshold"); save("a70_phase_dominance_ratios.png","A70 — Exact dominance of aligned terms",ylabel="Dominance ratio",rotate=60)
    x=np.arange(len(labels)); w=.4; plt.figure(figsize=(15,6)); plt.bar(x-w/2,[z["positive_term_count"] for z in p],w,label="Positive terms"); plt.bar(x+w/2,[z["negative_term_count"] for z in p],w,label="Negative terms"); plt.xticks(x,labels,rotation=60); save("a70_signed_term_counts.png","A70 — Every decomposition contains cancellation",ylabel="Number of terms")
    c=d["family_summary"]["minor_class_counts"]; plt.figure(figsize=(9,6)); plt.bar(["Ordinary q-Schur","Confluent norm–mean","Derivative only"],[c["ordinary_q_schur"],c["confluent_norm_mean"],c["derivative_only"]]); save("a70_minor_class_counts.png","A70 — Minor classes in the expansion",ylabel="Occurrences",rotate=10,legend=False)
    weak=next(z for z in p if z["maximum"]==9 and z["phase"]==7); plt.figure(figsize=(8,6)); plt.bar(["Aligned","Opposing"],[float(sp.Rational(weak["aligned_magnitude"])),float(sp.Rational(weak["opposing_magnitude"]))]); save("a70_weakest_dominance_phase.png","A70 — Phase closest to cancellation",ylabel="Exact rational magnitude",legend=False)


def figures_a71():
    d=load("a71_orientation_bifurcation_results.json"); w=d["weak_signature"]; Ms=sorted(map(int,w["values_M8_to_M16"].keys())); vals=[float(sp.Rational(w["values_M8_to_M16"][str(M)])) for M in Ms]
    plt.figure(figsize=(9,6)); plt.plot(Ms,vals,marker="o"); plt.axhline(0); plt.axvline(9.5,linestyle="--",label="Bifurcation 9→10"); save("a71_weak_signature_bifurcation.png","A71 — Orientation reversal of the inherited signature",r"Support maximum $M$",r"Cramer numerator $\Delta_{weak}$")
    t=d["M10_global_theorem"]["exact_phase_result"]; phase_plot({"x":t},"x","phases","transitions","a71_M10_global_risk_curve.png","a71_M10_phase_map.png","A71 — Global continuous theorem at M=10","A71 — Six phases after active-set bifurcation",2,3)
    top=d["M10_contract"]["top_10_designs"]; plt.figure(figsize=(12,6)); plt.bar([str(tuple(x["design"])) for x in top],[float(sp.log(sp.Rational(x["ratio"]))/(2*sp.log(2))) for x in top]); save("a71_M10_exact_catalogue_top10.png","A71 — Ten best exact designs at M=10",ylabel="Future minimax risk",rotate=45,legend=False)


def main():
    for fn in [figures_a47, figures_a51, figures_a52, figures_a53, figures_a54, figures_a55, figures_a56, figures_a57, figures_a58, figures_a59, figures_a60, figures_a61, figures_a62, figures_a63, figures_a64, figures_a65, figures_a66, figures_a67, figures_a68, figures_a69, figures_a70, figures_a71]:
        fn()
    expected = {
        'a47_global_phase_diagram.png','a51_target_exclusion_distance_risk.png','a52_continuous_second_anchor_risk.png','a53_coupled_anchor_risk_curves.png','a54_universal_continuum_witness_band.png','a55_finite_cap_absolute_convergence.png','a55_finite_cap_relative_convergence.png','a56_break_even_costs.png','a56_cost_selected_cap_policy.png','a56_risk_complexity_frontier.png','a57_allowed_noise_increase.png','a57_upgrade_threshold_map.png','a58_channel_sensitivity_priority.png','a58_individual_error_impacts.png','a59_exact_vs_linear_correlation.png','a59_risk_vs_correlation.png','a59_worst_direction_vs_correlation.png','a60_covariance_contributions.png','a60_general_covariance_risks.png','a60_general_covariance_worst_vectors.png','a61_covariance_uncertainty_premium.png','a61_spectral_risk_interval.png','a61_worst_vector_vs_tau.png','a62_bootstrap_coverage_validation.png','a62_contract_availability.png','a62_required_inflation_factors.png','a63_noisy_anchor_atlas.png','a63_noisy_third_anchor_offsets.png','a63_risk_vs_support_size.png','a64_boundary_pair_counts.png','a64_normalized_third_anchor_offsets.png','a64_target_translation_alignment.png','a65_boundary_sensitivity_distribution.png','a65_continuous_grid_margins.png','a65_local_certificate_coverage.png','a65_representative_first_anchor_curves.png','a66_canonical_global_monotonicity.png','a66_canonical_phase_map.png','a66_degenerate_global_monotonicity.png','a67_risk_vs_support_size.png','a67_support_family_phase_counts.png','a67_support_family_risk_curves.png','a67_support_family_transition_map.png','a68_dual_channel_activity.png','a68_first_channel_removal_risk.png','a68_first_channel_value_multiplier.png','a69_contact_signature_counts.png','a69_cramer_orientation_map.png','a69_numerator_flip_margins.png','a69_order_only_counterexample.png','a70_minor_class_counts.png','a70_phase_dominance_ratios.png','a70_signed_term_counts.png','a70_weakest_dominance_phase.png','a71_M10_exact_catalogue_top10.png','a71_M10_global_risk_curve.png','a71_M10_phase_map.png','a71_weak_signature_bifurcation.png'
    }
    actual={p.name for p in FIG.glob('*.png')}
    missing=expected-actual
    print(json.dumps({'generated':len(actual),'expected':len(expected),'missing':sorted(missing)},indent=2))
    if missing: raise SystemExit(1)

if __name__ == '__main__':
    main()
