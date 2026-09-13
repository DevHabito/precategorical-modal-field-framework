# A114-B2-B corrections and scope — 2026-09-13

## Preserved correction from exploration

During the new tail architecture tests, three exploratory representatives were initially replayed with a contact index one below the true `j=b+2`. The full exact KKT checker rejected them. The mistake was caught before publication.

After recomputing `b`, strict compressed winner and `Phi` exactly, the corrected contacts are:

- `M=522, s=263/2000`: `j=92`, endpoint-released strict KKT pass;
- `M=538, s=53/400`: `j=95`, compressed two-band strict KKT pass;
- `M=555, s=13/100`: `j=97`, q0/q1 gamma-inactive strict KKT pass.

These exploratory examples are **not proof dependencies** of A114-B2-B.

## Unrestricted discovery context

Correct-parity 260-digit unrestricted revised-simplex runs independently rediscovered:

- endpoint-released at `M=522, s=263/2000`;
- compressed two-band at `M=538, s=53/400`;
- q0/q1 gamma-inactive at `M=555, s=13/100`.

B2-W1 already provides the q0/q1 gamma-minus tail architecture at `M=521, s=129/1000`.

These runs demonstrate residual architectural diversity but remain discovery/falsification evidence only.

## Scope retained

A114-B2-B proves only that the pure central-Q gamma-minus branch is impossible when `j=b+2` and `Phi<0` in the analytic tail. It does not yet partition the four remaining observed families and does not classify `Phi=0`.
