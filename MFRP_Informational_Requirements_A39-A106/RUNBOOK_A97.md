# A97 Runbook

A97 is split into two memory-isolated exact phases and one lightweight assembly step.

```bash
mkdir -p provenance/a97_phase

python audits/a97_endpoint_released_interval_and_obstruction_audit.py \
  --interval-only-output provenance/a97_phase/a97_interval_phase.json

python audits/a97_endpoint_released_interval_and_obstruction_audit.py \
  --workers 16 \
  --atlas-only-output provenance/a97_phase/a97_atlas_phase.json

python audits/a97_endpoint_released_interval_and_obstruction_audit.py
python tools/generate_a97_figure.py
```

Expected verdict:

```text
PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS
```

The phase split is computational only. The interval phase and witness-atlas phase use disjoint exact certificates and are combined by the final audit invocation.
