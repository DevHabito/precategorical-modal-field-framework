# Exact full-F3 optimum and uniqueness in the odd case M=5

**7 November 2026.** A second, independent parity gate for the full three-band finite LP. The result is **only for this fixed instance**, not a universal odd-M theorem.

## Fixed contract

    M=5, mean=5/2,
    s=129/1000, tau=1/2,
    beta=1/8, gamma=1/16,
    delta=1/1875,
    epsilon=(1+tau)/2 * tau^2 * delta = 1/10000.

Both P and Q have arbitrary nonnegative masses on {0,...,5}, equal scaled totals and first moments, Q target transform exactly 1, and two-sided transform difference bands at all three observation nodes. Maximize the P target transform.

## The exact optimum

The objective is

    123288732982051199633 / 110644995632951812500
    = approximately 1.114273015935064.

The positive primal masses are:

    P0 = 247336980646395457 / 16733348104983453125
    P1 = 329511879709544395322 / 451800398834553234375
    P2 = 544570731187472897431 / 193628742357665671875
    P5 = 88035500964608000 / 86745676576234221

    Q1 = 8/7
    Q3 = 24/7
    t  = 32/7.

The remaining atom masses are zero. The only binding band rows are s upper (+) and gamma lower (-); all four remaining band slacks are strictly positive.

The equality constraints (two masses, two centered means and Q target) and these two binding bands form a nonsingular 7×7 rational system on the seven positive variables. Its determinant is exactly

    -86745676576234221 / 1310720000000000000.

## Dual, stationarity and uniqueness

The five unrestricted equality multipliers and two nonnegative active band multipliers are:

    aP = 1692141550835981 / 9317473316459100
    aQ = -6734478624380908261 / 36881665210983937500
    bP = -21460151083 / 356581451070
    bQ = 400025675314819507 / 4097962801220437500
    v  = 123288732982051199633 / 110644995632951812500

    u_s     = 551269531250000 / 196702214458581 > 0
    w_gamma = 124530930176 / 58338526725 > 0.

Every unused band multiplier is zero. The exact certificate verifies all P and Q atom reduced costs and the common-mass t row. All active reduced costs vanish, and every missing-atom reduced cost is strictly positive. The smallest missing-atom reduced cost is

    3923232564458594623 / 442579982531807250000 > 0.

The smallest inactive band slack is

    1938424698316759 / 3556899974423250000 > 0.

The primal objective exactly equals the dual objective v, which supplies a full upper bound. Strict complementarity and nonzero active determinant force any other optimum onto the same active equations and support, then force identical primal masses. Therefore the optimizer is **unique** for this finite contract.

A numerical LP solve suggested the candidate support only. The final checker does not use a numerical solver: it reconstructs the primal and dual by exact Fraction Gaussian elimination and independently tests every equality, inequality and reduced cost using the canonical F3 validator. Neither floating-point decimal above is used to determine any sign.

## Reproduction and limits

- [Odd M=5 exact KKT certificate script](../../audits/a115_odd_m5_full_lp_exact_kkt_certificate_20261107.py)
- [Even M=4 exact certificate and derivation](A115_FIXED_F3_M4_EXACT_PRIMAL_DUAL_CERTIFICATE_20261107.md)
- [Canonical F2/F3 mathematical contract](../research/A115_A122_CANONICAL_LP_CONTRACT_AND_GATES_20261107.md)

[GitHub Actions run 42386517555](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42386517555) completed **SUCCESS**, including the exact odd-parity primal/dual, complementary-slackness and uniqueness checks. The checked code is source commit 73cd0fbfdc600ec555882b6d31804bd7007508bc.

**The distinction from A115 remains important:** this F3 optimum has P support {0,1,2,5} and Q support {1,3}, with s+ and gamma- active. It is not the restricted A115 C2(k) active architecture. The existence of two exact finite examples, even and odd, does **not** prove eventual support stability, an all-parameter phase classification, or a new physical law.

The correct next mathematics is to vary M and the source/target nodes while recomputing complete primal-dual certificates. When doing so, a new basis must be permitted; we should not force the even or odd support pattern to persist.
