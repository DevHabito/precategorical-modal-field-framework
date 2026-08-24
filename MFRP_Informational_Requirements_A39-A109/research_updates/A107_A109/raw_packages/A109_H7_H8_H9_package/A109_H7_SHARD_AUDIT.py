#!/usr/bin/env python3
from __future__ import annotations
import json,hashlib,sys,time,argparse
from pathlib import Path
from collections import Counter
REPO=Path('/mnt/data/a107_work/repo'); sys.path.insert(0,str(REPO/'audits'))
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1

PR=Path('/mnt/data/A109_H7_PREREGISTRATION.json'); EXPECTED='7271e73abc02f7e0c37d2a8f4ff5c3d71f8a0fa86dbf5cba8c3515efc9fa440a'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--start',type=int,required=True); ap.add_argument('--end',type=int,required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
 if sha(PR)!=EXPECTED: raise RuntimeError('prereg hash mismatch')
 pr=json.loads(PR.read_text()); allowed=[tuple(x) for x in pr['holdout_selection']['shards']]
 if (args.start,args.end) not in allowed: raise RuntimeError('unfrozen shard')
 preds={int(x['canonical_rank']):x for x in pr['holdout_predictions']}; src=b1.source_records(); batch=src[args.start-1:args.end]
 out=[]; orig=a105.build_integer_polynomials
 for rank,record in enumerate(batch,start=args.start):
  t=time.time(); pred=preds[rank]
  try:
   a105.build_integer_polynomials=amin.build_integer_polynomials
   atlas=a105.analyze_record(record)
  finally: a105.build_integer_polynomials=orig
  atlas['architecture_class']='legacy_three_band_gamma_plus'
  selected=b1.semantic_selected_boundaries(atlas)
  reg=b1.direct_checkpoint_regression(record,atlas) if 'strict_component' in atlas else None
  core=atlas.get('core_certificate',{}); hull=atlas.get('nonselected_boundary_hull_certificate',{})
  failures=[]
  if pred['predicted_class']!='NO_CLASSIFICATION':
   if atlas.get('status')!=pred['predicted_class']: failures.append('class_mismatch')
   if selected!=pred['predicted_boundaries']: failures.append('boundary_mismatch')
  if atlas.get('root_failures'): failures.append('root_failure')
  if core.get('failure_count',0): failures.append('core_certificate_failure')
  if hull.get('failure_count',0): failures.append('hull_certificate_failure')
  if reg and (reg['mismatch_count'] or reg['positivity_failure_count'] or reg['outside_sign_failure_count']): failures.append('direct_regression_failure')
  out.append({'canonical_rank':rank,'source_key':record['key'],'maximum':int(record['key_fields']['maximum']),'contact_j':int(record['key_fields']['compressed_maximizer_contact']),
              'frozen_prediction':pred,'atlas_class':atlas.get('status'),'selected_boundaries':selected,
              'endpoint_nonpositive_conditions':atlas.get('endpoint_nonpositive_conditions'),
              'core_certificate_summary':{k:core.get(k) for k in ['condition_count','pass_count','failure_count','method_counts']},
              'hull_certificate_summary':{k:hull.get(k) for k in ['condition_count','pass_count','failure_count','method_counts']},
              'root_failure_count':len(atlas.get('root_failures',[])),
              'direct_regression_summary':None if reg is None else {k:reg[k] for k in ['checkpoint_count','comparison_count','mismatch_count','positivity_failure_count','outside_sign_failure_count']},
              'failures':failures,'strict_component':atlas.get('strict_component'),'outside_counterexamples':atlas.get('outside_counterexamples'),'seconds':time.time()-t})
 failures=[{'rank':x['canonical_rank'],'failures':x['failures']} for x in out if x['failures']]
 if failures: verdict='REFUTED_A109_H7_TWO_SIDED_RULE'
 else: verdict='PASS_A109_H7_TWO_SIDED_HOLDOUT'
 res={'audit':'A109_H7_UNCHANGED_TWO_SIDED_ADJACENT_BOUNDARY_HOLDOUT_SHARD','preregistration_sha256':sha(PR),'rank_range':[args.start,args.end],'verdict':verdict,
      'summary':{'record_count':len(out),'predicted_class_counts':dict(Counter(x['frozen_prediction']['predicted_class'] for x in out)),'atlas_class_counts':dict(Counter(x['atlas_class'] for x in out)),
                 'match_count':sum(not x['failures'] for x in out),'partial_count':sum(x['atlas_class']=='proper_strict_subcomponent' for x in out),
                 'direct_comparisons':sum((x['direct_regression_summary'] or {}).get('comparison_count',0) for x in out),'direct_mismatches':sum((x['direct_regression_summary'] or {}).get('mismatch_count',0) for x in out),
                 'core_failures':sum((x['core_certificate_summary'].get('failure_count') or 0) for x in out),'hull_failures':sum((x['hull_certificate_summary'].get('failure_count') or 0) for x in out)},
      'failures':failures,'records':out,'scope':{'nonclaims':pr['nonclaims']}}
 Path(args.out).write_text(json.dumps(res,indent=2),encoding='utf-8')
 print(json.dumps({'verdict':verdict,**res['summary'],'seconds':sum(x['seconds'] for x in out),'output':args.out},indent=2))
if __name__=='__main__': main()
