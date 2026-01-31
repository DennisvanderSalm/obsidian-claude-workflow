# Create daily note from template (Windows PowerShell)
# Usage: .\scripts\daily.ps1

$VaultPath = Join-Path $PSScriptRoot "..\vault"
$Date = Get-Date -Format "yyyy-MM-dd"

$NotePath = Join-Path $VaultPath "00-inbox\$Date.md"

$NoteContent = @"
# $Date

**Tags:** #daily

## Focus for Today
-

## Tasks
- [ ]

## Notes


## Wins


## Learned


## Tomorrow
-
"@

Set-Content -Path $NotePath -Value $NoteContent -Encoding UTF8

Write-Host "Created daily note: $NotePath"
