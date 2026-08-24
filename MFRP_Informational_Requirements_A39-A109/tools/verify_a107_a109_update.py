#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=[]; failures=[]
def check(name, ok, detail=""):
    checks.append({"name":name,"pass":bool(ok),"detail":detail})
    if not ok: failures.append(name)
manifest=ROOT/'MANIFEST_A107_A109.sha256'
manifest_errors=[]
for line in manifest.read_text().splitlines():
    if not line.strip(): continue
    digest, rel = line.split('  ',1)
    path=ROOT/rel
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        manifest_errors.append(rel)
check('update_manifest_hashes',not manifest_errors,','.join(manifest_errors[:10]))
status=json.loads((ROOT/'results'/'a107_a109'/'A109_PROSPECTIVE_STATUS_R106_R414.json').read_text())['status']
check('resolved_309',status['mathematically_resolved']==309)
check('strict_clean_308',status['strict_clean_prospective']==308)
check('no_non_adjacent',status['non_adjacent']==0)
check('no_direct_mismatches',status['direct_mismatches']==0)
pr=ROOT/'preregistrations'/'a107_a109'/'A109_H19_PREREGISTRATION.json'
sha=hashlib.sha256(pr.read_bytes()).hexdigest()
check('h19_prereg_sha',sha=='abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d',sha)
cp=subprocess.run([sys.executable,'-m','unittest','tests.test_a109_update'],cwd=ROOT,text=True,capture_output=True)
check('a109_unit_tests',cp.returncode==0,cp.stdout+cp.stderr)
out={'audit':'A107_A109_UPDATE_VERIFICATION','check_count':len(checks),'pass_count':sum(x['pass'] for x in checks),'failure_count':len(failures),'checks':checks,'failures':failures,'verdict':'PASS_A107_A109_UPDATE_VERIFICATION' if not failures else 'FAIL_A107_A109_UPDATE_VERIFICATION'}
print(json.dumps(out,indent=2))
if failures: raise SystemExit(1)
