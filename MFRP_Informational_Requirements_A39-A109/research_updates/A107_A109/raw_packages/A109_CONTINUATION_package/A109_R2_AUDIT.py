#!/usr/bin/env python3
from __future__ import annotations
import json,hashlib,sys,time
from pathlib import Path
REPO=Path('/mnt/data/a107_work/repo');sys.path.insert(0,str(REPO/'audits'))
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1
PR=Path('/mnt/data/A109_R2_PREREGISTRATION.json'); EXPECTED='75e400b94e7a27cc15b5813085928b5da7c2f7bed62780eeb60ac8c97f3327f6'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 if sha(PR)!=EXPECTED: raise RuntimeError('prereg hash mismatch')
 pr=json.loads(PR.read_text()); rank=int(pr['selected_rank']); src=b1.source_records(); record=src[rank-1]
 if record['key']!=pr['selected_source_key']: raise RuntimeError('source key mismatch')
 t=time.time(); orig=a105.build_integer_polynomials
 try:
  a105.build_integer_polynomials=amin.build_integer_polynomials; atlas=a105.analyze_record(record)
 finally: a105.build_integer_polynomials=orig
 atlas['architecture_class']='legacy_three_band_gamma_plus'
 selected=b1.semantic_selected_boundaries(atlas); reg=b1.direct_checkpoint_regression(record,atlas) if 'strict_component' in atlas else None
 core=atlas.get('core_certificate',{}); hull=atlas.get('nonselected_boundary_hull_certificate',{})
 failures=[]; fp=pr['frozen_prediction']
 if atlas.get('status')!=fp['class']: failures.append('class_mismatch')
 if selected!=fp['boundaries']: failures.append('boundary_mismatch')
 if atlas.get('root_failures'): failures.append('root_failure')
 if core.get('failure_count',0): failures.append('core_certificate_failure')
 if hull.get('failure_count',0): failures.append('hull_certificate_failure')
 if reg and (reg['mismatch_count'] or reg['positivity_failure_count'] or reg['outside_sign_failure_count']): failures.append('direct_regression_failure')
 verdict='PASS_A109_R2_RIGHT_BRANCH' if not failures else 'REFUTED_A109_R2_RIGHT_BRANCH'
 res={'audit':pr['audit'],'preregistration_sha256':sha(PR),'verdict':verdict,'rank':rank,'source_key':record['key'],'M':int(record['key_fields']['maximum']),'j':int(record['key_fields']['compressed_maximizer_contact']),'frozen_prediction':fp,'atlas_class':atlas.get('status'),'selected_boundaries':selected,'endpoint_nonpositive_conditions':atlas.get('endpoint_nonpositive_conditions'),'strict_component':atlas.get('strict_component'),'outside_counterexamples':atlas.get('outside_counterexamples'),'core_certificate_summary':{k:core.get(k) for k in ['condition_count','pass_count','failure_count','method_counts']},'hull_certificate_summary':{k:hull.get(k) for k in ['condition_count','pass_count','failure_count','method_counts']},'root_failures':atlas.get('root_failures'),'direct_regression_summary':None if reg is None else {k:reg[k] for k in ['checkpoint_count','comparison_count','mismatch_count','positivity_failure_count','outside_sign_failure_count']},'failures':failures,'seconds':time.time()-t,'scope':{'nonclaims':pr['nonclaims']}}
 p=Path('/mnt/data/A109_R2_RESULT.json');p.write_text(json.dumps(res,indent=2),encoding='utf-8')
 print(json.dumps({'verdict':verdict,'rank':rank,'atlas_class':res['atlas_class'],'selected_boundaries':selected,'direct_regression_summary':res['direct_regression_summary'],'core_failures':core.get('failure_count',0),'hull_failures':hull.get('failure_count',0),'seconds':res['seconds'],'output':str(p)},indent=2))
if __name__=='__main__':main()
