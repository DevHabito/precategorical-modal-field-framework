#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser(description="Run a sequential interval of MFRP audits.")
    p.add_argument('--from-audit',type=int,default=39)
    p.add_argument('--to-audit',type=int,default=106)
    p.add_argument('--continue-on-error',action='store_true')
    p.add_argument('--runtime',type=Path,default=ROOT/'build'/'runtime')
    args=p.parse_args()
    subprocess.run([sys.executable,str(ROOT/'tools'/'materialize_runtime.py'),'--output',str(args.runtime),'--clean'],check=True)
    logs=ROOT/'logs'/'replay'; logs.mkdir(parents=True,exist_ok=True)
    scripts=[]
    for path in args.runtime.glob('a[0-9][0-9]*_audit.py'):
        m=re.match(r'a(\d+)_',path.name)
        if m and args.from_audit<=int(m.group(1))<=args.to_audit:
            scripts.append((int(m.group(1)),path))
    scripts.sort()
    failures=[]
    for n,path in scripts:
        log=logs/f'a{n:02d}_{path.stem}.log'
        print(f"[A{n}] {path.name}",flush=True)
        completed=subprocess.run([sys.executable,str(path)],cwd=args.runtime,text=True,capture_output=True)
        log.write_text(completed.stdout+'\n--- STDERR ---\n'+completed.stderr,encoding='utf-8')
        if completed.returncode!=0:
            failures.append((n,path.name,completed.returncode))
            print(f"  FAIL (exit {completed.returncode}); log: {log}")
            if not args.continue_on_error: break
        else:
            print(f"  PASS; log: {log}")
    if failures:
        print('Failures:',failures); raise SystemExit(1)
    print(f"Completed {len(scripts)} audits successfully.")

if __name__=='__main__':
    main()
