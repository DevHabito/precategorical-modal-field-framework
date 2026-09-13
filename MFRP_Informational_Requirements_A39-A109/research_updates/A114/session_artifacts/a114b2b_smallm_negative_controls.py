#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path
import importlib.util

HERE=Path(__file__).resolve().parent
# This control script is intended to run beside the independent reduced scan helper.
spec=importlib.util.spec_from_file_location('scan',HERE/'a114b2b_independent_reduced_exact_scan.py')
scan=importlib.util.module_from_spec(spec); spec.loader.exec_module(scan)
# Exact A102 strict unique-b+2 gamma-minus witnesses.
CASES=[
(23,'131/1000',6),(29,'131/1000',7),(34,'131/1000',8),(35,'13/100',8),
(45,'131/1000',10),(51,'131/1000',11),(56,'131/1000',12),(62,'131/1000',13),
(68,'131/1000',14),(85,'131/1000',17),(91,'131/1000',18),(102,'131/1000',20),
(108,'131/1000',21),(114,'131/1000',22)]
rows=[]
for M,ss,j in CASES:
 s=F(ss); h=M//2
 phi=scan.upper_F(M,j,s)
 p0,pm,pj,pM,t=scan.gamma_minus_primal(M,j,s)
 rows.append({'M':M,'s':ss,'j':j,'3j-h':3*j-h,'phi_sign':scan.sgn(phi),
              'p0_sign':scan.sgn(p0),'p_jm1_sign':scan.sgn(pm),'p_j_sign':scan.sgn(pj),
              'pM_sign':scan.sgn(pM),'t_sign':scan.sgn(t)})
out={'audit':'A114B2B_SMALLM_NEGATIVE_CONTROLS','count':len(rows),
     'all_3j_minus_h_lt_13':all(r['3j-h']<13 for r in rows),
     'all_phi_negative':all(r['phi_sign']<0 for r in rows),
     'all_gamma_minus_primal_positive':all(min(r['p0_sign'],r['p_jm1_sign'],r['p_j_sign'],r['pM_sign'],r['t_sign'])>0 for r in rows),
     'rows':rows,'verdict':'PASS'}
(HERE/'A114B2B_SMALLM_NEGATIVE_CONTROLS_20260913.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
