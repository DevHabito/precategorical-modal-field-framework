#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description="Create a flat audit runtime workspace.")
    parser.add_argument('--output',type=Path,default=ROOT/'build'/'runtime')
    parser.add_argument('--clean',action='store_true')
    args=parser.parse_args()
    out=args.output.resolve()
    if args.clean and out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True,exist_ok=True)
    copied=0
    for folder, patterns in [('audits',['*.py']),('results',['*.json']),('templates',['*.json'])]:
        for src in (ROOT/folder).glob('*'):
            if src.is_file() and any(src.match(p) for p in patterns):
                shutil.copy2(src,out/src.name); copied+=1
    print(f"Materialized {copied} files in {out}")
if __name__=='__main__': main()
