# Quick capture script for Windows PowerShell
# Usage: .\scripts\capture.ps1 -Title "Note title" -Content "Content"

param(
    [string]$Title = "Untitled",
    [string]$Content = ""
)

$VaultPath = Join-Path $PSScriptRoot "..\vault"
$InboxPath = Join-Path $VaultPath "00-inbox"
$Date = Get-Date -Format "yyyy-MM-dd"
$Time = Get-Date -Format "HH:mm"

# Sanitize filename
$Filename = $Title -replace '[^\w\s]', '' -replace '\s+', '-'

$NotePath = Join-Path $InboxPath "$Filename.md"

$NoteContent = @"
# $Title

**Captured:** $Date $Time
**Tags:** #inbox

$Content

## Notes


## Related
-
"@

Set-Content -Path $NotePath -Value $NoteContent -Encoding UTF8

Write-Host "Created: $NotePath"
