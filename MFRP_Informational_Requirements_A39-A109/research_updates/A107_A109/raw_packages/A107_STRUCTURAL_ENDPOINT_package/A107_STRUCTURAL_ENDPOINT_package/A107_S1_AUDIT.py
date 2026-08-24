#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path
from typing import Any

REPO=Path('/mnt/data/a107_work/repo')
sys.path.insert(0,str(REPO/'audits'))
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as a107min
import a107_b1_gamma_plus_preregistered_batch_audit as a107b1

EXPECTED_PREREG_SHA256='e634534d18afb2008dd047411d6102687d34eae0836ef97d83fd78a1b240c7ef'
DEFAULT_PREREG=Path('/mnt/data/A107_S1_PREREGISTRATION.json')
DEFAULT_OUT=Path('/mnt/data/A107_S1_RESULT.json')

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--preregistration',default=str(DEFAULT_PREREG))
    ap.add_argument('--output',default=str(DEFAULT_OUT))
    args=ap.parse_args()
    prereg=Path(args.preregistration)
    ph=sha256(prereg)
    if ph!=EXPECTED_PREREG_SHA256:
        raise RuntimeError(f'prereg hash mismatch {ph}')
    pp=json.loads(prereg.read_text())
    pred_by_rank={int(x['canonical_rank']):x for x in pp['holdout_predictions']}
    source=a107b1.source_records()
    if len(source)!=922: raise RuntimeError(f'expected 922 got {len(source)}')
    batch=source[25:33]
    if len(batch)!=8: raise RuntimeError('batch != 8')
    outputs=[]
    original=a105.build_integer_polynomials
    try:
        a105.build_integer_polynomials=a107min.build_integer_polynomials
        for rank,record in enumerate(batch,start=26):
            analyzed=a105.analyze_record(record)
            analyzed['architecture_class']='legacy_three_band_gamma_plus'
            regression=a107b1.direct_checkpoint_regression(record,analyzed) if 'strict_component' in analyzed else {
                'checkpoint_count':0,'comparison_count':0,'mismatch_count':0,
                'positivity_failure_count':0,'outside_sign_failure_count':0,
                'mismatches':[],'positivity_failures':[],'outside_sign_failures':[],'checkpoints':[]}
            local_success,reasons=a107b1.per_record_success(record,analyzed,regression)
            pred=pred_by_rank[rank]
            observed=analyzed.get('status')
            predicted=pred['predicted_class']
            classifiable=predicted in {'proper_strict_subcomponent','full_segment_coverage'}
            class_match=(observed==predicted) if classifiable else None
            selected=a107b1.semantic_selected_boundaries(analyzed)
            expected_boundary=pred.get('if_partial_predicted_boundary')
            if predicted=='proper_strict_subcomponent':
                boundary_match=(len(selected)==1 and selected[0]['side']=='left' and selected[0]['condition']==expected_boundary)
            else:
                boundary_match=None
            outputs.append({
                'canonical_rank':rank,
                'source_key':record['key'],
                'maximum':int(record['key_fields']['maximum']),
                'contact_j':int(record['key_fields']['compressed_maximizer_contact']),
                'witness':str(record['key_fields']['witness']),
                'segment_open_bounds':record['segment_open_bounds'],
                'frozen_prediction':pred,
                'observed_class':observed,
                'classifiable':classifiable,
                'classification_match':class_match,
                'selected_boundaries':selected,
                'predicted_partial_boundary_match':boundary_match,
                'analysis':analyzed,
                'direct_checkpoint_regression':regression,
                'local_stability_success':local_success,
                'local_stability_failure_reasons':reasons,
            })
    finally:
        a105.build_integer_polynomials=original

    local_success_count=sum(bool(x['local_stability_success']) for x in outputs)
    classifiable=[x for x in outputs if x['classifiable']]
    class_mismatches=[x for x in classifiable if x['classification_match'] is False]
    predicted_partials=[x for x in classifiable if x['frozen_prediction']['predicted_class']=='proper_strict_subcomponent']
    boundary_mismatches=[x for x in predicted_partials if x['predicted_partial_boundary_match'] is False]
    unresolved=[x for x in outputs if x['observed_class']=='internal_failure_or_unresolved']
    witness_failures=[x for x in outputs if x['observed_class']=='witness_failure']

    if local_success_count==8:
        local_verdict='PASS_BATCH_LOCAL_STABILITY'
    elif witness_failures:
        local_verdict='FAIL_BATCH_LOCAL_STABILITY'
    else:
        local_verdict='INCONCLUSIVE_BATCH'

    if unresolved or local_verdict=='INCONCLUSIVE_BATCH':
        structural_verdict='INCONCLUSIVE_STRUCTURAL_HOLDOUT'
    elif not classifiable:
        structural_verdict='NOT_ADJUDICATED_NO_CLASSIFIABLE_RECORDS'
    elif class_mismatches or boundary_mismatches:
        structural_verdict='REFUTED_STRUCTURAL_ENDPOINT_SIGN_RULE'
    elif predicted_partials:
        structural_verdict='PROSPECTIVE_SUPPORT_STRUCTURAL_ENDPOINT_SIGN_RULE'
    else:
        structural_verdict='CLASSIFICATION_SUPPORT_BOUNDARY_NOT_TESTED'

    status_counts=Counter(x['observed_class'] for x in outputs)
    boundary_counts=Counter(b['condition'] for x in outputs for b in x['selected_boundaries'])
    side_counts=Counter(b['side'] for x in outputs for b in x['selected_boundaries'])
    total_conditions=sum(int(x['analysis'].get('condition_count',0)) for x in outputs)
    comparisons=sum(int(x['direct_checkpoint_regression'].get('comparison_count',0)) for x in outputs)
    mismatches=sum(int(x['direct_checkpoint_regression'].get('mismatch_count',0)) for x in outputs)

    result={
        'audit':'A107-S1_STRUCTURAL_ENDPOINT_SIGN_HOLDOUT',
        'preregistration':{'path':str(prereg),'sha256':ph,'expected_sha256':EXPECTED_PREREG_SHA256,'hash_match':ph==EXPECTED_PREREG_SHA256},
        'selection':{'canonical_ranks':list(range(26,34)),'batch_size':8,'source_gamma_plus_count':len(source)},
        'summary':{
            'status_counts':dict(status_counts),
            'local_stability_success_count':local_success_count,
            'local_stability_failure_count':8-local_success_count,
            'classifiable_count':len(classifiable),
            'classification_match_count':len(classifiable)-len(class_mismatches),
            'classification_mismatch_count':len(class_mismatches),
            'predicted_partial_count':len(predicted_partials),
            'predicted_partial_boundary_match_count':len(predicted_partials)-len(boundary_mismatches),
            'predicted_partial_boundary_mismatch_count':len(boundary_mismatches),
            'selected_boundary_condition_counts':dict(boundary_counts),
            'selected_boundary_side_counts':dict(side_counts),
            'total_KKT_condition_count':total_conditions,
            'total_direct_checkpoint_comparisons':comparisons,
            'total_direct_checkpoint_mismatches':mismatches,
            'witness_failure_count':len(witness_failures),
            'unresolved_count':len(unresolved),
        },
        'local_stability_verdict':local_verdict,
        'structural_endpoint_sign_verdict':structural_verdict,
        'classification_mismatches':[
            {'canonical_rank':x['canonical_rank'],'predicted':x['frozen_prediction']['predicted_class'],'observed':x['observed_class']}
            for x in class_mismatches],
        'boundary_mismatches':[
            {'canonical_rank':x['canonical_rank'],'expected':x['frozen_prediction'].get('if_partial_predicted_boundary'),'observed':x['selected_boundaries']}
            for x in boundary_mismatches],
        'records':outputs,
        'scope':{
            'claim':'prospective holdout test of the exact lower-endpoint sign predictor on canonical gamma-plus ranks 26..33',
            'nonclaims':pp['nonclaims'],
        }
    }
    out=Path(args.output); out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({
        'prereg_hash':ph,
        'local_verdict':local_verdict,
        'structural_verdict':structural_verdict,
        'status_counts':dict(status_counts),
        'classification_match_count':len(classifiable)-len(class_mismatches),
        'classification_mismatch_count':len(class_mismatches),
        'predicted_partial_count':len(predicted_partials),
        'boundary_match_count':len(predicted_partials)-len(boundary_mismatches),
        'boundary_mismatch_count':len(boundary_mismatches),
        'conditions':total_conditions,
        'comparisons':comparisons,
        'direct_mismatches':mismatches,
        'output':str(out),
    },indent=2))
if __name__=='__main__': main()
