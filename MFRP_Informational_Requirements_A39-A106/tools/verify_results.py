#!/usr/bin/env python3
from __future__ import annotations
import compileall, hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def stats(d):
    g=d.get('gates')
    if isinstance(g,dict): return sum(v is True for v in g.values()),len(g),all(v is True for v in g.values())
    p=int(d.get('pass_count',0)); t=int(d.get('gate_count',0)); return p,t,p==t and t>0

def main():
    failures=[]; registry=json.loads((ROOT/'audit_registry.json').read_text()); gates=0
    for e in registry:
        p=ROOT/'results'/e['result']
        try: d=json.loads(p.read_text(encoding='utf-8'))
        except Exception as exc: failures.append(f'{p}: {exc}'); continue
        if not str(d.get('verdict','')).startswith('PASS'): failures.append(f'{p}: non-PASS verdict')
        passed,total,ok=stats(d); gates+=total
        if not ok: failures.append(f'{p}: gates {passed}/{total}')
    for p in (ROOT/'results').glob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as exc: failures.append(f'{p}: invalid JSON {exc}')
    if not compileall.compile_dir(ROOT/'audits',quiet=1,force=True): failures.append('Audit compilation failed')
    if not compileall.compile_dir(ROOT/'tools',quiet=1,force=True): failures.append('Tool compilation failed')
    manifest=ROOT/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            digest,rel=line.split('  ',1); path=ROOT/rel
            if not path.exists(): failures.append(f'Missing: {rel}'); continue
            if hashlib.sha256(path.read_bytes()).hexdigest()!=digest: failures.append(f'Hash mismatch: {rel}')
    out={'audit_results':len(registry),'gate_count':gates,'figures':len(list((ROOT/'figures').glob('*.png'))),'failures':failures,'status':'PASS' if not failures else 'FAIL'}
    print(json.dumps(out,indent=2))
    if failures: raise SystemExit(1)
if __name__=='__main__': main()
