#Requires -Version 5.1
<#
.SYNOPSIS
    Creates the folder structure for a new problem in this repository.

.DESCRIPTION
    Builds problems/P<nnn>-<slug>/ with every directory the layout in
    skills/log/reference/layout.md expects, and seeds three files: meta.yaml,
    README.md and human/attempt.md.

    It deliberately does NOT create prompts/prompt0.md. The human attempt has to
    be written and committed before the first prompt is sent, and the
    human_attempt_first gate checks the git history for that ordering. Creating
    both at once would make the ordering impossible to demonstrate.

    Template versions written into meta.yaml are read from the template files
    themselves, so this script does not go stale when a template is bumped.

.PARAMETER Id
    Problem number, without the P. Padded to three digits: 2 becomes P002.

.PARAMETER Slug
    Short name for the folder. Lowercase letters, digits and single hyphens.

.PARAMETER Title
    Human-readable title. Defaults to the slug with hyphens turned into spaces.

.PARAMETER RepoRoot
    Repository root. Found automatically by walking up from this script.

.PARAMETER Bare
    Create only directories and .gitkeep files. No meta.yaml, README.md or
    attempt.md.

.PARAMETER Force
    Allow writing into a problem folder that already exists. Existing files are
    left alone; only what is missing gets created.

.EXAMPLE
    .\scripts\New-Problem.ps1 -Id 2 -Slug pendulum-with-moving-pivot

.EXAMPLE
    .\scripts\New-Problem.ps1 -Id 2 -Slug some-slug -WhatIf

    Shows what would be created without creating anything.
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [ValidateRange(1, 999)]
    [int]$Id,

    [Parameter(Mandatory)]
    [ValidatePattern('^[a-z0-9]+(-[a-z0-9]+)*$')]
    [string]$Slug,

    [string]$Title,

    [string]$RepoRoot,

    [switch]$Bare,

    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

function Find-RepoRoot {
    <# Walks up from a starting directory until it finds one containing .git #>
    param([Parameter(Mandatory)][string]$StartPath)

    $dir = Get-Item -LiteralPath $StartPath
    while ($null -ne $dir) {
        if (Test-Path -LiteralPath (Join-Path $dir.FullName '.git')) {
            return $dir.FullName
        }
        $dir = $dir.Parent
    }
    return $null
}

function Write-TextFile {
    <#
        Writes UTF-8 without a byte order mark and with LF line endings, which
        is what git and the rest of this repository expect. Set-Content on
        Windows PowerShell 5.1 would add a BOM and CRLF.
    #>
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][AllowEmptyString()][string]$Content
    )

    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    $normalized = $Content -replace "`r`n", "`n"
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $normalized, $utf8NoBom)
}

function Get-TemplateVersion {
    <# Reads a version like v1.2 out of the first line of a template file #>
    param([Parameter(Mandatory)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return 'unknown' }

    $firstLine = Get-Content -LiteralPath $Path -TotalCount 1
    if ($firstLine -match 'v(\d+\.\d+)') { return "v$($Matches[1])" }
    return 'unknown'
}

function Get-ChangelogVersion {
    <# Reads the newest "## vX.Y" heading out of CHANGELOG.md #>
    param([Parameter(Mandatory)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return 'unknown' }

    foreach ($line in Get-Content -LiteralPath $Path) {
        if ($line -match '^##\s+v(\d+\.\d+)') { return "v$($Matches[1])" }
    }
    return 'unknown'
}

# --------------------------------------------------------------------------
# Resolve where we are
# --------------------------------------------------------------------------

if (-not $RepoRoot) {
    $RepoRoot = Find-RepoRoot -StartPath $PSScriptRoot
    if (-not $RepoRoot) {
        throw "Could not find the repository root. Run this from inside the repo, or pass -RepoRoot."
    }
}

$RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path

if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot 'templates'))) {
    throw "No templates folder under '$RepoRoot'. That does not look like this repository."
}

$problemId  = 'P{0:d3}' -f $Id
$folderName = "$problemId-$Slug"
$problemDir = Join-Path (Join-Path $RepoRoot 'problems') $folderName

if ((Test-Path -LiteralPath $problemDir) -and -not $Force) {
    throw "'problems\$folderName' already exists. Pass -Force to fill in what is missing, or pick another id or slug."
}

if (-not $Title) {
    $Title = ($Slug -replace '-', ' ')
    $Title = $Title.Substring(0, 1).ToUpper() + $Title.Substring(1)
}

$today = Get-Date -Format 'yyyy-MM-dd'

# --------------------------------------------------------------------------
# Directories
# --------------------------------------------------------------------------

# Every directory the layout expects. Each one gets a .gitkeep, because git
# tracks files and not folders, so an empty directory would not survive a clone.
$subdirs = @(
    'human'
    'prompts'
    'answers'
    'audits'
    'final'
    'sources'
    'explore'
    'assets'
    'assets/code'
    'assets/figures'
)

if ($PSCmdlet.ShouldProcess($problemDir, 'Create problem folder')) {
    New-Item -ItemType Directory -Path $problemDir -Force | Out-Null
    Write-Host "created  problems\$folderName\"
}

foreach ($sub in $subdirs) {
    $path = Join-Path $problemDir $sub
    if ($PSCmdlet.ShouldProcess($path, 'Create directory')) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null

        # assets is only a container for code and figures, so it needs no keeper
        if ($sub -ne 'assets') {
            $keep = Join-Path $path '.gitkeep'
            if (-not (Test-Path -LiteralPath $keep)) {
                Write-TextFile -Path $keep -Content ''
            }
        }
        $display = $sub.Replace('/', '\')
        Write-Host "created  problems\$folderName\$display\"
    }
}

if ($Bare) {
    Write-Host ''
    Write-Host "Done. Bare structure only, no files seeded."
    return
}

# --------------------------------------------------------------------------
# Seeded files
# --------------------------------------------------------------------------

$templatesDir = Join-Path $RepoRoot 'templates'

$versions = [ordered]@{
    conventions       = Get-TemplateVersion (Join-Path $templatesDir 'CONVENTIONS.md')
    prompt0           = Get-TemplateVersion (Join-Path $templatesDir 'prompt0.md')
    audit             = Get-TemplateVersion (Join-Path $templatesDir 'audit-prompt.md')
    blind_solve       = Get-TemplateVersion (Join-Path $templatesDir 'blind-solve-prompt.md')
    human_attempt     = Get-TemplateVersion (Join-Path $templatesDir 'human-attempt.md')
    compliance_probe  = Get-TemplateVersion (Join-Path $templatesDir 'compliance-probe.md')
    exploration       = Get-TemplateVersion (Join-Path $templatesDir 'exploration-prompt.md')
    log_skill         = Get-ChangelogVersion (Join-Path $RepoRoot 'CHANGELOG.md')
}

$versionBlock = ($versions.Keys | ForEach-Object { "  {0}: {1}" -f $_, $versions[$_] }) -join "`n"

$metaTemplate = @'
problem_id: __ID__
slug: __SLUG__
title: "__TITLE__"
course: "Introduction to Theoretical Physics"
opened: __DATE__
closed:
status: open                 # open | closed | escalated | abandoned
verdict:                     # ACCEPT | ACCEPT-WITH-FIXES | REVISE | REJECT | ESCALATED
rounds: 0

templates:
__VERSIONS__

# One entry per model call. Effort level cannot be observed from inside a
# session, so it is always user-reported, and `unknown` is a valid value.
# Never guess one: a guessed field silently poisons comparisons across runs.
runs: []
#  - artifact: answers/answer-1.md
#    role: solver              # solver | auditor | blind-solver | explorer
#    model_id:
#    model_label:
#    model_source: user-reported
#    effort:
#    effort_source: user-reported
#    tools: []
#    date:

# Filled by /log. See skills/log/SKILL.md for what each one checks.
gates: {}

human_attempt:
  committed_before_prompt0:
  time_spent_min:
  reached_an_answer:
  prediction:
  prediction_correct:

ground_truth:
  available:
  source:                    # professor | answer-key | measurement | numerical | none
  verdict:
  arrived:                   # before-loop | mid-loop | after-loop | none

compliance_probe:
  run: false
  probed_claim:
  probed_claim_known_right_by:
  outcome:                   # held | asked | caved
  fabricated_support:

independence:
  declaration_requested:
  retrieval_suspected:
  perturbation_test_run:

sources:
  used: 0
  consulted: 0
  verified_tool: 0
  verified_human: 0
  unverified: 0

result_one_line:
branches_queued: []
'@

$readmeTemplate = @'
# __ID__ — __TITLE__

**Date:** __DATE__
**Verdict:**
**Rounds:**
**Status:** open

## 1. The problem

<!-- Statement, verbatim. Image in assets/figures/ if there is one. -->

## 2. My first attempt

<!-- One paragraph. The full record is in human/attempt.md, written and
     committed before the first prompt was sent. -->

## 3. First interaction with the AI

<!-- The prompt is in prompts/prompt0.md. Which model, which effort level,
     how long it took. The hypotheses it put on the table. -->

## 4. Audit

<!-- What the auditor found. Which findings were accepted, which were rebutted
     and upheld. -->

## 5. Compliance probe

<!-- The claim probed, why it was known to be right, and the outcome:
     held, asked, or caved. -->

## 6. Reflection

<!-- What actually happened, in your own words. This section is the point of
     the logbook. -->

## 7. What this problem changed in the method

<!-- Only if something did. Delete this section otherwise. -->
'@

$attemptTemplate = @'
# Human attempt — __ID__

Time spent:
Date: __DATE__
Consulted:

## How I read the problem

<!-- What is being asked, in your own words. Where the statement is ambiguous. -->

## Hypotheses I am using

<!-- Numbered. These get compared against the model's. State them even when they
     feel obvious: "rolls without slipping" is a hypothesis. -->

1.

## Work

<!-- Your derivation, or a link to a scan in ../assets/figures/. Incomplete is
     fine and expected. -->

## Where I got stuck

<!-- The specific obstruction. Not "I ran out of time" but what you could not
     get past and what you would have needed. -->

## My prediction

<!-- Your answer, your best guess, or the form you expect the answer to take.
     Commit to something. A prediction you got wrong is worth more later than
     no prediction. -->

## Confidence

<!-- 0 to 1, in the prediction. -->

---

Do not edit this file after prompt0 is sent. It is a record of a prior, and a
prior edited after seeing the data is not a prior.
'@

function Expand-Stub {
    param([Parameter(Mandatory)][string]$Text)
    $Text.Replace('__ID__', $problemId).
          Replace('__SLUG__', $Slug).
          Replace('__TITLE__', $Title).
          Replace('__DATE__', $today).
          Replace('__VERSIONS__', $versionBlock)
}

$seedFiles = [ordered]@{
    'meta.yaml'         = Expand-Stub $metaTemplate
    'README.md'         = Expand-Stub $readmeTemplate
    'human/attempt.md'  = Expand-Stub $attemptTemplate
}

foreach ($relative in $seedFiles.Keys) {
    $path = Join-Path $problemDir $relative

    $display = $relative.Replace('/', '\')

    if (Test-Path -LiteralPath $path) {
        Write-Host "skipped  problems\$folderName\$display (already exists)"
        continue
    }

    if ($PSCmdlet.ShouldProcess($path, 'Write file')) {
        Write-TextFile -Path $path -Content $seedFiles[$relative]
        Write-Host "created  problems\$folderName\$display"
    }
}

# human/attempt.md is a real file now, so the .gitkeep beside it is redundant
$humanKeep = Join-Path $problemDir 'human/.gitkeep'
if ((Test-Path -LiteralPath $humanKeep) -and $PSCmdlet.ShouldProcess($humanKeep, 'Remove redundant .gitkeep')) {
    Remove-Item -LiteralPath $humanKeep -Force
}

# --------------------------------------------------------------------------
# What to do next
# --------------------------------------------------------------------------

Write-Host ''
Write-Host "$problemId is set up at problems\$folderName" -ForegroundColor Green
Write-Host ''
Write-Host 'Next, in order:'
Write-Host ''
Write-Host '  1. Write human\attempt.md yourself. Time it. Do not read anything else first.'
Write-Host '  2. Commit it on its own, before any prompt is sent:'
Write-Host ''
Write-Host "       git add problems/$folderName"
Write-Host "       git commit -m ""$problemId`: human attempt"""
Write-Host ''
Write-Host '  3. Only then write prompts\prompt0.md from templates\prompt0.md,'
Write-Host '     filling sections 0 to 5 and pasting 6 to 8 verbatim.'
Write-Host ''
Write-Host 'Step 2 is what the human_attempt_first gate checks. It reads the git'
Write-Host 'history, not the file dates, so committing both together fails it.'
