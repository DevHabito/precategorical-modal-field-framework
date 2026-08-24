#!/usr/bin/env python3
import argparse,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'audits'))
import a105_legacy_two_band_continuum_segment_atlas_audit as a
p=argparse.ArgumentParser();p.add_argument('index',type=int);p.add_argument('--outdir',default=str(ROOT/'provenance'/'a105_legacy_two_band_continuum_atlas'/'records'));args=p.parse_args()
r=a.source_records()[args.index]
t=time.time();x=a.analyze_record(r)
out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
path=out/f'a105_record_{args.index:03d}.json'
path.write_text(json.dumps(x,indent=2),encoding='utf-8')
print(json.dumps({'index':args.index,'maximum':x['maximum'],'status':x['status'],'seconds':time.time()-t,'path':str(path)}),flush=True)
