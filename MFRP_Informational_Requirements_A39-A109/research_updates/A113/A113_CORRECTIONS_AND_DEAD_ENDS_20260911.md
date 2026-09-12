# A113 field notes — failed stronger claims and corrections

This file deliberately records the mistakes and tempting shortcuts encountered while extending A94 into the analytic tail.

## 1. False shortcut: `b+3` disappears in the tail

Early high-precision exploration suggested that `E_(b+2)` might always be negative for `M>=521`, which would restrict the global compressed maximizer to `{b+1,b+2}`.

That is false.

Exact rational counterexample:

- `M=561`;
- `s=129/1000`;
- `b=95`;
- `E_(b+2)>0`.

Therefore `b+3` remains a real compressed-maximizer phase in the tail.

## 2. A numerical false alarm at M=661

An insufficient-precision exploratory evaluation initially appeared to give `E_(b+3)>0` at `M=661`, `s=129/1000`, apparently refuting the remote-sign law itself.

Exact `Fraction` arithmetic showed the value is negative.

The event is preserved because it demonstrates severe cancellation in the deep tail and why floating-point/multiprecision scans cannot be theorem gates here.

## 3. False shortcut: the second secant is always positive

A natural route to one-variation would be

`E_(b+1)-E_(b+2)>0`.

This is false.

Exact counterexample:

- `M=2049`;
- `s=133/1000`;
- `E_(b+1)<0`;
- `E_(b+2)<0`;
- `E_(b+1)-E_(b+2)<0`.

The sign sequence still has one variation; it simply need not be locally decreasing after the transition.

## 4. Successful replacement: central nesting

The correct sufficient relation is

`J = E_(b+1) - 2 E_(b+2) > 0`.

The factor 2 comes from the exact target node `tau=1/2`. In this combination, the large nonconfluent target-affine term cancels exactly.

`J>0` rules out the only dangerous pattern

`E_(b+1)<0<E_(b+2)`

without demanding the false second-secant monotonicity.

## 5. Prototype constants were hardened

The first A113 certificate used a few deliberately coarse work constants (`0.36`, etc.) whose correctness had been checked during derivation but not linked to explicit gates in the script.

The hardened certificate derives and checks those caps internally. This did not change any theorem margin or sign; it removed an auditability weakness.

## 6. Current discipline

- exploratory high-precision scans are allowed to suggest targets;
- every suspicious deep-tail sign must be rechecked exactly;
- false stronger claims remain recorded;
- the final theorem uses only exact rational inequalities and symbolic identities;
- compressed-objective claims and lifted-LP claims remain separate.
