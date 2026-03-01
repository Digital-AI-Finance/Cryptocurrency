# Plan: Fix Broken GitHub Pages Links

## Problem Summary

The GitHub Pages site has broken links because files exist locally but are not tracked in git (404 on GH Pages). One PDF (`lectures/blockchain_fundamentals.pdf`) doesn't exist at all.

### Link Inventory from index.html (~98 local links)

| Category | Count | Tracked |
|----------|-------|---------|
| Lesson 1-4 topic PDFs (`01_*/...` through `04_*/...`) | 24 | All 24 |
| Standalone lecture PDFs (`lectures/*.pdf`) | 32 | 12 of 32 (BF+CS+ES groups) |
| Quiz HTMLs (all groups + quiz1-4) | 36 | 16 of 36 (bf+cs+es+quiz1-4) |
| Notes PDFs (`notes/*.pdf`) | 4 | All 4 |
| `glossary.md` + `assessments/final_report_template.md` | 2 | Both |

**~40 files need git tracking:** 20 lecture PDFs + 20 quiz HTMLs + matching TEX files.
**1 file needs compilation:** `lectures/blockchain_fundamentals.pdf` (tex exists, pdflatex failed).

## Implementation Steps

### Step 1: Write Python Link Checker Script
Create `check_links.py` (stdlib only) that:
- Parses `index.html`, extracts all `href` from `<a>` tags
- Classifies: anchor (`#`), external (`http`/`https`), or local file
- For local files: checks `os.path.exists()` relative to repo root
- Also checks `git ls-files` to identify exist-but-untracked files
- Outputs: BROKEN (missing), UNTRACKED (exists but not in git), OK
- Exit code 1 if any BROKEN links

### Step 2: Run Link Checker as Diagnostic
Execute `python check_links.py`. Output is the source of truth for subsequent steps.

### Step 3: Fix Missing Files (conditional on Step 2 output)
For any BROKEN links where `.tex` exists: compile with pdflatex from `lectures/` dir, two passes for beamer:
```bash
cd lectures && pdflatex -interaction=nonstopmode <file>.tex && pdflatex -interaction=nonstopmode <file>.tex
```
Known: `blockchain_fundamentals.pdf` needs this. If compilation fails, note for user.

### Step 4: Git Add All UNTRACKED Referenced Files
Add every file the checker identified as UNTRACKED:
```bash
git add lectures/*.pdf lectures/*.tex \
  quiz/quiz_tc_*.html quiz/quiz_df_*.html quiz/quiz_nf_*.html \
  quiz/quiz_sc_*.html quiz/quiz_ct_*.html \
  index.html
```
This covers the 20 untracked lecture PDFs, 20 matching TEX files, 20 quiz HTMLs, and modified index.html. Already-tracked files (lesson topics, notes, glossary, bf/cs/es quizzes, quiz1-4) are unaffected by git add.

### Step 5: Re-run Link Checker
Confirm 0 BROKEN links. All UNTRACKED should now show as OK.

### Step 6: Commit and Push
Commit and push to `main` to trigger GH Pages rebuild.

## Acceptance Criteria
- [ ] `check_links.py` runs and reports 0 BROKEN local links
- [ ] All files referenced in `index.html` exist on disk
- [ ] All referenced files are tracked in git
- [ ] `git push` completed successfully

## Risks
- **LaTeX compilation failure:** MiKTeX may need packages. Fall back to user manual compilation.
- **Large commit:** Binary PDFs unavoidable for GH Pages.

PLAN_READY: .omc/plans/fix-broken-links.md
