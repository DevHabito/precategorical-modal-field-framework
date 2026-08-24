#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
B=Path('/mnt/data')
prp=B/'A109_H10_PREREGISTRATION.json'; pr=json.loads(prp.read_text()); prsha=hashlib.sha256(prp.read_bytes()).hexdigest()
pred={int(x['canonical_rank']):x for x in pr['holdout_predictions']}
full_files=['A109_H10_S1_RESULT.json','A109_H10_S3_RESULT.json','A109_H10_S5_RESULT.json','A109_H10_S6_RESULT.json','A109_H10_S8_RESULT.json']
checks=[]; direct=0; mism=0; ranks=[]
for fn in full_files:
 d=json.loads((B/fn).read_text())
 checks.append((d['preregistration_sha256']==prsha,f'{fn}: prereg hash'))
 for r in d['records']:
  rank=int(r['canonical_rank']); ranks.append(rank)
  checks.append((r['frozen_prediction']['predicted_class']==pred[rank]['predicted_class'],f'r{rank}: prediction class unchanged'))
  checks.append((r['frozen_prediction']['predicted_boundaries']==pred[rank]['predicted_boundaries'],f'r{rank}: prediction boundaries unchanged'))
  checks.append((r['atlas_class']==pred[rank]['predicted_class'],f'r{rank}: atlas class'))
  checks.append((r['selected_boundaries']==pred[rank]['predicted_boundaries'],f'r{rank}: atlas boundaries'))
  checks.append((not r['failures'],f'r{rank}: no reported failures'))
  x=r['direct_regression_summary'] or {}; direct+=x.get('comparison_count',0); mism+=x.get('mismatch_count',0)
for rank in [273,274,277,278,283,284]:
 core=json.loads((B/f'A109_H10D_R{rank}_CORE.json').read_text()); ranks.append(rank)
 checks.append((core['frozen_prediction']['predicted_class']==pred[rank]['predicted_class'],f'r{rank}: diagnostic prediction class unchanged'))
 checks.append((core['frozen_prediction']['predicted_boundaries']==pred[rank]['predicted_boundaries'],f'r{rank}: diagnostic prediction boundaries unchanged'))
 checks.append((core['verdict']=='CORE_SUPPORT',f'r{rank}: core support'))
 checks.append((not core['exact_failures'],f'r{rank}: no exact core failure'))
 checks.append((not core['unresolved'],f'r{rank}: no unresolved core condition'))
 n=5 if pred[rank]['predicted_class']=='full_segment_coverage' else 4
 for i in range(n):
  dd=json.loads((B/f'A109_H10D_R{rank}_D{i}.json').read_text())
  checks.append((dd['verdict']=='DIRECT_SUPPORT',f'r{rank}/d{i}: direct support'))
  checks.append((not dd['mismatches'],f'r{rank}/d{i}: zero mismatches'))
  direct+=dd['comparison_count']; mism+=len(dd['mismatches'])
checks.append((sorted(ranks)==list(range(271,287)),'all ranks exactly 271..286 once'))
checks.append((direct==27703,'combined direct comparison count = 27703'))
checks.append((mism==0,'combined direct mismatches = 0'))
failed=[label for ok,label in checks if not ok]
out={'audit':'A109_H10_INDEPENDENT_ARTIFACT_CONSISTENCY_CHECK','preregistration_sha256':prsha,'check_count':len(checks),'failure_count':len(failed),'failures':failed,'rank_count':len(ranks),'rank_range':[min(ranks),max(ranks)],'direct_comparisons':direct,'direct_mismatches':mism,'status':'PASS' if not failed else 'FAIL'}
(B/'A109_H10_INDEPENDENT_CONSISTENCY_CHECK.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
