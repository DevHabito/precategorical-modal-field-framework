# Historical ZIP integrity finding — 2026-10-19

**Status:** CONFIRMED STRUCTURAL FAILURE on repository bytes; three
historical reproducibility archives are not valid ZIP files.

This finding is about the **stored packages**, not evidence that a
mathematical proposition is false. It is a separate reproducibility
blocker, despite previously restored root SHA-256 inventories.

## 1. Full tracked ZIP corpus

The read-only Python 3 `zipfile` job
[GitHub Actions run 39342219023](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39342219023)
audited every tracked `.zip` file on the audit branch:

- 22 tracked ZIP archives inspected;
- 19 archives opened and passed structural-member and CRC checks;
- **3 archives failed** with `BadZipFile: File is not a zip file`.

The job **failed as intended**. No archive was extracted, executed,
regenerated, corrected or replaced by this audit.

| Corrupt path relative to the project | Stored bytes | Read result |
|---|---:|---|
| `MFRP_Informational_Requirements_A39-A109/research_updates/A110_A112/archives/A112_TAIL_CLOSURE_WORKING_SET_20260911.zip` | 14,861 | BadZipFile |
| `MFRP_Informational_Requirements_A39-A109/research_updates/A113/archives/A113_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip` | 7,529 | BadZipFile |
| `MFRP_Informational_Requirements_A39-A109/research_updates/A114/archives/A114A_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip` | 7,529 | BadZipFile |

The corresponding original GitHub history lists **one introducing commit**
for each archive path:

- A112: `9b07cf470bb305d6a8cfbf7f2bbddad3e504b936`
  (2026-09-12);
- A113 and A114-A: `4c069a4a706b5e932b417e62065f4c6d949adb1a`
  (2026-09-12).

No earlier revision of those *same paths* appeared in the available
GitHub commit-history queries. This does not establish that an external
local, detached-branch, or differently named copy never existed.

## 2. Why the SHA-256 integrity gate did not detect it

The root `MANIFEST.csv` and `SHA256SUMS.txt` record the bytes that
exist in Git. A valid hash proves consistency with a particular byte
sequence. It does **not** certify the semantic completeness, extractability,
or correctness of that sequence.

The historic local SHA-256 manifests also contain records for these three
archive paths:

- `A110_A112/MANIFEST_A112_TAIL_CLOSURE_20260911.sha256`;
- `A113/MANIFEST_A113_20260912.sha256`;
- `A114/MANIFEST_A114A_20260912.sha256`.

A follow-up run of `tools/audit_zip_packages.py` independently
recomputed SHA-256 for all three stored archive byte sequences and
compared them to their **dated local manifests**. All three comparisons
**FAILED** in
[archive audit run 39342441591](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39342441591):

| Package | Present SHA-256 | Historical manifest SHA-256 |
|---|---|---|
| A112 | `d4e38e7593df21dc183cdfa36a1d9caf00746bc67d019917d5922b03bbf2a271` | `4e1a6f8899fb1498ac95c1527c10fb0c3f2b863f04cd76dab09826b3337fee21` |
| A113 | `87f3596e733d67e95202e19c9c07e00c873c1d4900bde7f6b13803fe00dac210` | `7a16d3a97626afb4fd57eb41a3152c75cabe679ea36698cae2f01761df890f15` |
| A114-A | `631b7fa62fe2c2ab772394ade39371c2bb111bc036c07bebadf011186179df80` | `9328538264bacb2bcddcaa8876b66d3914e4a76ae650f138bd1f302e70ab8c04` |

Thus we have **two independently observable failures**: each archive is
structurally unreadable and the bytes stored in Git do not correspond to
the dated reproducibility checksum. Do **not** overwrite the historical
manifest with the currently observed digest, because that would erase
a useful recovery fingerprint.

The Git blob SHA of each archive is identical in its single introducing
GitHub commit and in the current repository. The mismatch therefore
**predates the 2026-10-19 audit**; the available history does not
determine whether the intended full archive was lost before upload,
during the original transfer, or in a separate untracked workflow.

## 3. Direct ZIP structure observation

The GitHub byte stream has ordinary ZIP local-header prefixes, but the
A112/A113 response does not contain a valid end-of-central-directory
record. The A113 local header for the second entry declares a compressed
payload larger than the bytes remaining in the stored file.

The standard-library ZIP parser's direct failure on the actual
GitHub Actions checkout is the dispositive reproducibility gate.
The header observations are supplementary diagnosis only.

The archives were **partially salvaged** by a read-only,
local-header, DEFLATE and CRC validator in
[recovery run 39343471074](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39343471074):

- A112: four local-header members passed CRC (two are empty directory
  entries; two are JSON certificates for A112-D and the logical audit);
  the A112-G branch-regularity JSON member failed decompression/CRC.
- A113: its first member, the complete **9,145-byte original Python
  certificate script**, passed raw DEFLATE and CRC. Its second JSON
  member is truncated.
- A114-A: the first certificate Python member is truncated; **no
  complete original member was recovered**.

The intact A113 Python source has SHA-256
`46e1fec5197c7253e29156e592e2320905cd993caa66f3f5b9cd109471b11587`.
It is preserved separately, byte-for-byte, at
`consolidation/recovered_provenance/a113_tail_global_compressed_one_variation_certificate.py`.

In [run 39343954194](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39343954194)
the unchanged recovered A113 Python script was executed with pinned
SymPy in an isolated CI environment: its **23/23 declared exact
symbolic/rational gates passed**. Another independent exact proof of
the A113 parity contact envelopes is recorded in
[A113_RECOVERED_CERTIFICATE_AND_CONTACT_ENVELOPES_2026-10-19.md](A113_RECOVERED_CERTIFICATE_AND_CONTACT_ENVELOPES_2026-10-19.md).

**This is recovery of one intact A113 source member, not recovery of
the complete historical ZIP or the missing original result JSON**.
The historical archive SHA-256 mismatches and failing ZIP integrity
gate remain unchanged. The 23 passing original gates alone do not
certify the validity of every analytic majorant used in the all-tail
proof claim.

## 4. Mathematical assurance impact

The mathematical claims of the historical A112, A113 and A114-A
documents are **not refuted** by this finding. Their recorded proof maps
and human-readable theorem claims remain accessible.

However, the **complete** historical reproducibility packages
remain unusable. Partial source recovery can establish executable
claims of an intact individual member, but it cannot validate
missing files, hidden script dependencies, or unproven analytic
majorant-to-factor implications. In particular:

- the all-tail A112-G `A(s)<0` bound is an **open independent audit gate**;
- the A112-B interlacing and A112-C quantitative checkpoint implications
  are likewise not closed by archive metadata;
- the recovered original A113 script's 23 exact gates have been
  re-executed successfully, but the full continuous-source tail
  **majorant derivations** have not yet been independently rebuilt;
- A114-A's isolated full reproducibility package is not currently usable.

Separate exact checks already completed **remain valid at their own
explicit scopes**: finite LP/KKT controls, the direct analytic P/Q
determinant argument, the conditional Q Chebyshev lemma, and the
fully replayed C2 Lean proof. Do not erase those scoped results
or promote them into all-tail results.

## 5. Recovery criteria

Do **not** silently rewrite the original ZIPs, guess their missing
compressed bytes, reconstruct a favorable certificate from reported
PASS values, or claim that a recovered subset is the full original
package.

An acceptable replacement requires:

1. locate an intact independently traceable original copy (for example,
   a dated local or remote backup);
2. preserve the invalid archive and its original Git blob SHA;
3. validate the candidate replacement structurally and by CRC;
4. compare recovered member names and SHA-256 values to dated manifests,
   where individual member hashes exist;
5. run the original scripts in a pinned, isolated environment and audit
   both analytic inequalities and dependencies;
6. store a separate recovery record and only then update theorem assurance
   labels, with no retroactive alteration of the original evidence.

## 6. Merge gate

`tools/audit_zip_packages.py` and
`.github/workflows/archive-integrity-audit.yml` add an explicit failing
integrity gate. The audit PR must remain **DRAFT / NOT MERGEABLE** while
any required historical reproducibility package is invalid or the
recovery plan is not explicitly reconciled.

A GitHub Actions red result here is an **honest finding**, not a
reason to disable or conditionally bypass the check.
