# A104 reproducibility statement

A104 is deterministic and uses exact SymPy rational arithmetic for matrix inverses, rank-one updates, sparse polynomial coefficients, endpoint signs, root brackets, derivative signs, interval enclosures, and outside counterexamples.

The seven records are committed separately under `provenance/a104_exceptional_continuum_atlas/`. The final audit assembly loads exactly those seven files, verifies their source routing and counts, and writes the consolidated result and catalogue.

The root-ordering layer is stronger than choosing boundaries by decimal approximation: all competing isolating brackets are compared by exact rational inequalities. Every nonselected KKT condition is certified positive on the complete hull containing both selected root brackets.

The theorem remains restricted to the seven A95 rational source segments routed to exceptional q0/q1 architectures by A102. It is not a continuum theorem for the complete 1,063-witness atlas or for complete A92 cells.
