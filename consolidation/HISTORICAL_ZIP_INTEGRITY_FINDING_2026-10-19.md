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

A follow-up run of `tools/audit_zip_packages.py` now compares these
historical records to the **current exact archive bytes**. This
secondary match must be interpreted separately from ZIP structural
validity; a match cannot transform an invalid package into a valid one.

## 3. Direct ZIP structure observation

The GitHub byte stream has ordinary ZIP local-header prefixes, but the
A112/A113 response does not contain a valid end-of-central-directory
record. The A113 local header for the second entry declares a compressed
payload larger than the bytes remaining in the stored file.

The standard-library ZIP parser's direct failure on the actual
GitHub Actions checkout is the dispositive reproducibility gate.
The header observations are supplementary diagnosis only.

The archives may be partially salvageable, but salvaging intact
members is **not equivalent** to recovering the complete published
certificate bundle, nor to rerunning the original verification.

## 4. Mathematical assurance impact

The mathematical claims of the historical A112, A113 and A114-A
documents are **not refuted** by this finding. Their recorded proof maps
and human-readable theorem claims remain accessible.

However, the exact full certificate scripts and reported generated
artifacts bundled **only** in these invalid ZIPs cannot currently be
treated as independently re-executed from their advertised canonical
package. In particular:

- the all-tail A112-G `A(s)<0` bound is an **open independent audit gate**;
- the A112-B interlacing and A112-C quantitative checkpoint implications
  are likewise not closed by archive metadata;
- A113's full continuous-source tail majorants have not been independently
  re-executed from the archived script;
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
