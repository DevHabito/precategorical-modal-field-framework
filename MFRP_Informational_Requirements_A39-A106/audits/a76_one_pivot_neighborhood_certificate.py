#!/usr/bin/env python3
"""Exact one-pivot neighborhood certificate for A76.

At s0=131/1000, classify every signature in the declared one-pivot
neighborhood of the actual M=21,22,23 optimal signatures.
"""
from __future__ import annotations
import importlib.util,json
from collections import Counter,defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
CORE=HERE/'a76_active_reentry_core.py'
A73=HERE/'a73_complete_one_pivot_neighborhood_audit.py'

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    core=load_module(CORE,'a76_core_neighbors')
    a73=load_module(A73,'a73_for_a76_neighbors')
    a73.S0=core.S0
    records=[]; summaries={}; combined=Counter(); pivot=defaultdict(Counter)
    for M in [21,22,23]:
        candidates=core.generate_neighbors(M)
        counts=Counter(); counts_all=Counter(); strict=[]
        for index,candidate in enumerate(candidates,1):
            ev=a73.exact_basis_evaluation(M,candidate)
            cls=ev['classification'];counts_all[cls]+=1
            if not candidate['is_reference']:
                counts[cls]+=1;combined[cls]+=1;pivot[candidate['kind']][cls]+=1
            if ev['strict_local_optimum']:
                strict.append({'candidate_index':index,'kind':candidate['kind'],'detail':candidate['detail'],'p_support':candidate['p_support'],'q_support':candidate['q_support'],'active_observations':candidate['active_observations']})
            first={
                'negative_basic':ev.get('negative_basic',[])[:1],
                'negative_active_dual':ev.get('negative_active_dual',[])[:1],
                'negative_reduced_cost':ev.get('negative_reduced_cost',[])[:1],
                'negative_inactive_slack':ev.get('negative_inactive_slack',[])[:1],
            }
            records.append({'maximum':M,'candidate_index':index,**candidate,'classification':cls,'strict_local_optimum':ev['strict_local_optimum'],'negative_counts':ev.get('negative_counts',{}),'first_failure':first})
        summaries[str(M)]={
            'candidate_count_including_reference':len(candidates),
            'single_pivot_neighbor_count':len(candidates)-1,
            'classification_counts_including_reference':dict(counts_all),
            'classification_counts_neighbors':dict(counts),
            'strict_local_optima':strict,
        }
    gates={
        'all_456_declared_one_pivot_neighbors_enumerated':sum(x['single_pivot_neighbor_count'] for x in summaries.values())==456,
        'all_459_reference_and_neighbor_bases_nonsingular_and_classified':len(records)==459 and not any(r['classification'] in {'rank_mismatch','singular'} for r in records),
        'each_actual_reference_is_unique_strict_local_optimum':all(len(summaries[str(M)]['strict_local_optima'])==1 and summaries[str(M)]['strict_local_optima'][0]['kind']=='reference' for M in [21,22,23]),
        'no_declared_neighbor_is_locally_optimal':combined.get('locally_optimal',0)==0,
        'combined_neighbor_failure_counts_match':dict(combined)=={'primal_infeasible':329,'active_dual_multiplier_infeasible':55,'reduced_cost_infeasible':68,'inactive_observation_slack_infeasible':4},
    }
    result={
        'audit':'A76_ONE_PIVOT_NEIGHBORHOOD_CERTIFICATE',
        'probe_s':str(core.S0),
        'moves':['exchange one P contact','exchange one Q contact','flip beta or gamma active-band sign','deactivate beta or gamma while one active P or Q contact leaves the reduced basis'],
        'excluded_moves':['scale-variable exchange','alpha sign flip or deactivation','two-contact exchange','combined contact and sign exchange','complete LP-basis enumeration'],
        'neighbor_counts':{'21':145,'22':152,'23':159,'total':456},
        'support_summaries':summaries,
        'combined_neighbor_classification_counts':dict(combined),
        'pivot_type_classification_counts':{k:dict(v) for k,v in pivot.items()},
        'candidate_records':records,
        'gates':gates,
        'verdict':'PASS' if all(gates.values()) else 'FAIL',
    }
    out=HERE/'a76_one_pivot_neighborhood_results.json';out.write_text(json.dumps(result,indent=2))
    print(json.dumps({'gate_count':len(gates),'pass_count':sum(gates.values()),'neighbor_counts':result['neighbor_counts'],'failure_counts':dict(combined),'verdict':result['verdict'],'output':out.name},indent=2))
    if not all(gates.values()):raise SystemExit(1)
if __name__=='__main__':main()
