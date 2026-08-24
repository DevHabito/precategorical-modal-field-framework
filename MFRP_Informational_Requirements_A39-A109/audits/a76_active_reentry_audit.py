#!/usr/bin/env python3
"""Aggregate the independently generated A76 exact certificates."""
from __future__ import annotations
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
INTERVAL=HERE/'a76_interval_certificate_results.json'
NEIGHBORS=HERE/'a76_one_pivot_neighborhood_results.json'
DISCOVERY=HERE/'a76_M21_M23_phase_discovery.json'

def load(path):
    if not path.exists(): raise FileNotFoundError(path)
    return json.loads(path.read_text())

def main():
    interval=load(INTERVAL);neighbors=load(NEIGHBORS);discovery=load(DISCOVERY)
    gates={
        'interval_certificate_passed':interval['verdict']=='PASS' and all(interval['gates'].values()),
        'one_pivot_certificate_passed':neighbors['verdict']=='PASS' and all(neighbors['gates'].values()),
        'discovery_has_seven_phases_each':all(x['phase_count']==7 for x in discovery['supports']),
        'actual_selected_sequence_is_gamma_plus_plus_minus':{
            M:interval['selected_interval_certificates'][M]['signature']['active_observations'][-1][1]
            for M in ['21','22','23']
        }=={'21':1,'22':1,'23':-1},
        'old_candidate_positive_orientation_does_not_restore_primal_feasibility':all(
            interval['old_candidate_primal_infeasibility'][M]['A75_gamma_plus_multiplier_sign']==1
            and interval['old_candidate_primal_infeasibility'][M]['basic_4_certificate']['sign']==-1
            for M in ['22','23']
        ),
        'all_456_neighbors_rejected':sum(neighbors['combined_neighbor_classification_counts'].values())==456,
    }
    verdict='PASS_NO_ACTIVE_REENTRY_AT_M22_AND_ACTUAL_SIGN_FLIP_AT_M23' if all(gates.values()) else 'FAIL_A76_ACTIVE_REENTRY_AUDIT'
    result={
        'audit':'A76_CANDIDATE_ORIENTATION_VERSUS_ACTUAL_ACTIVE_SET',
        'interval':interval['interval'],
        'candidate_versus_actual':{
            'A75_old_candidate':'P={0,3,4,M}, Q={1,floor(M/2),floor(M/2)+1}',
            'actual_family':'P={0,5,6,M}, Q={1,floor(M/2),floor(M/2)+1}',
            'A75_candidate_gamma_plus_signs':{
                '21':-1,'22':1,'23':1,
            },
            'actual_selected_gamma_signs':{
                '21':1,'22':1,'23':-1,
            },
            'formal_statement':(
                'The A75 candidate orientation re-entry at M=22 is not an active-set re-entry. '
                'The actual optimizer already uses gamma-plus at M=21 and M=22, then flips to gamma-minus at M=23.'
            ),
        },
        'interval_certificate':interval,
        'one_pivot_certificate':neighbors,
        'numerical_phase_discovery':discovery,
        'formal_results':[
            'the old candidate orientation re-entry at M=22 does not correspond to active-set re-entry',
            'the actual optimal contact family differs from the A75 candidate family',
            'all 159 exact KKT conditions of the selected M=21,22,23 branches are positive on the complete interval',
            'the opposite gamma sign is excluded by a negative active multiplier in each support',
            'the actual gamma-plus Cramer numerator changes sign between M=22 and M=23 while the determinant stays positive',
            'the old M=22 and M=23 candidate remains primal-infeasible despite positive gamma-plus orientation',
            'all 456 declared one-pivot neighbors are rejected and each actual reference is the unique strict local optimum at the probe',
        ],
        'gates':gates,
        'verdict':verdict,
        'boundary':(
            'A76 is exact on the declared interval and exact at the one-pivot probe. '
            'The seven-phase full-alpha atlases are numerical discovery artifacts, not complete algebraic global phase theorems for M=21,22,23.'
        ),
    }
    out=HERE/'a76_active_reentry_results.json';out.write_text(json.dumps(result,indent=2))
    summary={
        'audit':result['audit'],'gate_count':len(gates),'pass_count':sum(gates.values()),
        'candidate_gamma_plus_signs':result['candidate_versus_actual']['A75_candidate_gamma_plus_signs'],
        'actual_selected_gamma_signs':result['candidate_versus_actual']['actual_selected_gamma_signs'],
        'selected_condition_counts':{M:interval['selected_interval_certificates'][M]['condition_count'] for M in ['21','22','23']},
        'neighbor_counts':neighbors['neighbor_counts'],
        'neighbor_failure_counts':neighbors['combined_neighbor_classification_counts'],
        'failed_gates':[k for k,v in gates.items() if not v],'verdict':verdict,
    }
    sout=HERE/'a76_active_reentry_summary.json';sout.write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
    if not all(gates.values()): raise SystemExit(1)
if __name__=='__main__':main()
