# A99 Reproducibility Contract

- Python with SymPy and Matplotlib.
- No random seeds are used.
- `audits/a99_q0q1_interval_and_residual_atlas_audit.py` performs all promoted calculations.
- The symbolic interval stage uses exact rational sparse-polynomial arithmetic.
- Both root brackets are rational intervals of width `1/10^24`.
- Root uniqueness and simplicity are certified by exact endpoint signs and exact derivative interval signs.
- All 799 nonboundary KKT numerators and the common determinant are enclosed by exact rational interval evaluation.
- The remaining-residual atlas uses exact rational matrix inversion and checks every unused P/Q atom reduced cost.
- The claim is restricted to the declared finite LP contracts and the local search interval.
