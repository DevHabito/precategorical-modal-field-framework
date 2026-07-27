# GitHub Release Checklist

- [x] Use the parent repository split license: Apache-2.0 for software and CC BY 4.0 for scientific content/data.
- [x] Publish under `DevHabito/precategorical-modal-field-framework` and update the URL in `CITATION.cff`.
- [ ] Run `python tools/verify_results.py`.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Regenerate figures and confirm a clean Git diff.
- [ ] Review claim boundaries in `REPRODUCIBILITY.md`.
- [ ] Create a signed or annotated version tag.
- [ ] Attach the release ZIP and SHA-256 manifest.
- [ ] Optionally archive the tagged release on Zenodo.
