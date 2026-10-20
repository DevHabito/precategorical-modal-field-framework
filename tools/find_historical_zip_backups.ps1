<#
.SYNOPSIS
    Read-only search for exact historical A112/A113/A114-A ZIP backups.

.DESCRIPTION
    Compares SHA-256 against immutable hashes preserved in dated research
    manifests. Does not extract, execute, rename, copy, or change any file.
    Paths and findings are printed locally; no data is transmitted.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string[]] $Roots
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$targets = @(
    [pscustomobject]@{
        Name = "A112_TAIL_CLOSURE_WORKING_SET_20260911.zip"
        Sha256 = "4e1a6f8899fb1498ac95c1527c10fb0c3f2b863f04cd76dab09826b3337fee21"
    },
    [pscustomobject]@{
        Name = "A113_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip"
        Sha256 = "7a16d3a97626afb4fd57eb41a3152c75cabe679ea36698cae2f01761df890f15"
    },
    [pscustomobject]@{
        Name = "A114A_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip"
        Sha256 = "9328538264bacb2bcddcaa8876b66d3914e4a76ae650f138bd1f302e70ab8c04"
    }
)

$byHash = @{}
$byName = @{}
foreach ($target in $targets) {
    $byHash[$target.Sha256.ToUpperInvariant()] = $target.Name
    $byName[$target.Name.ToUpperInvariant()] = $target.Sha256
}

$results = New-Object System.Collections.Generic.List[object]
$scannedPaths = New-Object 'System.Collections.Generic.HashSet[string]'

foreach ($root in $Roots) {
    if (-not (Test-Path -LiteralPath $root -PathType Container)) {
        Write-Warning ("Directory not found: " + $root)
        continue
    }

    $candidateFiles = Get-ChildItem -LiteralPath $root -Filter "*.zip" -File -Recurse -Force -ErrorAction SilentlyContinue
    foreach ($candidate in $candidateFiles) {
        if (-not $scannedPaths.Add($candidate.FullName.ToUpperInvariant())) {
            continue
        }

        try {
            $sha = (Get-FileHash -LiteralPath $candidate.FullName -Algorithm SHA256 -ErrorAction Stop).Hash.ToUpperInvariant()
        }
        catch {
            Write-Warning ("Could not hash file: " + $candidate.FullName)
            continue
        }

        $nameKey = $candidate.Name.ToUpperInvariant()
        if ($byHash.ContainsKey($sha)) {
            $results.Add([pscustomobject]@{
                Status = "EXACT_HISTORICAL_SHA256_MATCH"
                ExpectedFile = $byHash[$sha]
                LocalPath = $candidate.FullName
                Sha256 = $sha
                Bytes = $candidate.Length
            })
        }
        elseif ($byName.ContainsKey($nameKey)) {
            $results.Add([pscustomobject]@{
                Status = "FILENAME_MATCH_SHA256_MISMATCH"
                ExpectedFile = $candidate.Name
                LocalPath = $candidate.FullName
                Sha256 = $sha
                Bytes = $candidate.Length
            })
        }
    }
}

Write-Output ("Unique ZIP files scanned: " + $scannedPaths.Count)
if ($results.Count -eq 0) {
    Write-Output "No exact historical hash or expected filename match found."
}
else {
    $results | Format-Table -AutoSize
}
Write-Output "Read-only scan completed. Matching SHA-256 does not replace ZIP CRC and reproducibility checks."
