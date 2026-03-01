# Fix All Gaps Plan

## Status: REVISION 2 (Addressing Critic Feedback)

## Context

After a comprehensive inventory analysis (`course_inventory.json`), several gaps were identified across the 13-lesson cryptocurrency course. Upon verification, some reported gaps were stale (files exist on disk but weren't captured in the inventory). This plan addresses the **confirmed** gaps.

## Confirmed Gaps (Verified Against Filesystem)

### Tier 1: Actual Defects (Must Fix)

| # | Gap | Details | Effort |
|---|-----|---------|--------|
| 1 | `quiz/quiz3.html` has 17 questions | Should have 20 like all other quizzes. Need 3 more Ethereum/Smart Contract questions. | Small |
| 2 | L12 `tokenomics_mechanism.tex` has 49 frames | All other technical lectures have 55 frames. Need 6 more frames. | Medium |
| 3 | `course_inventory.json` is stale | L12/L13 preview slides and preclass marked as `null` but files exist (`*_intro_preview.tex`, `*_preclass.tex`). Multiple summary counts wrong. | Small |

### Tier 2: Structural Gaps (New Content, Not Fixes)

| # | Gap | Details | Effort |
|---|-----|---------|--------|
| 4 | No numbered-directory lesson lectures for L05-L13 | Only L01-L04 have `0N_topic/0N_topic.tex` format (~36-frame lesson lectures with live coding). These are a different format from the standalone technical lectures. | **Massive** (9 lectures x ~36 frames) |
| 5 | No student notes for any lesson | Zero note files found in the entire repo. No template exists. | **Massive** (13 note documents) |

### False Gaps (Already Fixed)

| Gap | Reality |
|-----|---------|
| Missing preclass L12 | `lectures/tokenomics_mechanism_preclass.tex` exists (13KB) |
| Missing preclass L13 | `lectures/privacy_zk_proofs_preclass.tex` exists (13KB) |
| Missing preview L12 | `lectures/tokenomics_mechanism_intro_preview.tex` exists with PDF |
| Missing preview L13 | `lectures/privacy_zk_proofs_intro_preview.tex` exists with PDF |

## Implementation Plan

### Task 1: Add 3 Questions to quiz3.html
- **File:** `quiz/quiz3.html`
- **Action:**
  1. Read existing 17 questions to understand topics covered (Ethereum & Smart Contracts).
  2. Add 3 new questions (IDs 18, 19, 20) covering gaps in the topic. Match existing quiz format (multiple choice, 4 options, explanation field).
  3. Update the hardcoded progress badge in the HTML (line ~310: `0/17` must become `0/20`) so the initial render before JS hydration shows the correct total.
- **Acceptance Criteria:**
  - quiz3.html has exactly 20 question objects in the `quizData.questions` array.
  - All questions have valid IDs (18, 19, 20), `correct` field, 4 `options`, and `explanation`.
  - Hardcoded progress counter in HTML matches 20.

### Task 2: Add 6 Frames to L12 Tokenomics Technical Lecture
- **File:** `lectures/tokenomics_mechanism.tex`
- **Action:** Read existing 49 frames across 5 sections. Section 4 (Token Design Framework) has ~8 frames and is the thinnest. Add 6 frames distributed to bring thin sections up, targeting 55 total. Follow existing Beamer conventions: `\bottomnote{}` on every frame, mlblue/mlpurple colors, TikZ diagrams, no parameterized TikZ styles in beamer frames.
- **Sections (current frame counts to verify):**
  1. Token Fundamentals & Supply Economics
  2. Bonding Curves & Pricing Mechanisms
  3. Incentive Design & Game Theory
  4. Token Design Framework (thinnest — ~8 frames)
  5. Case Studies & Pitfalls
- **Acceptance Criteria:**
  - 55 `\begin{frame}` occurrences total.
  - Compiles with pdflatex (2 passes) without errors.
  - All new frames have `\bottomnote{}`.
  - No `style=solidity` (use `\lstset` defaults).
  - TikZ styles non-parameterized (no `fill=#1` or `fill=##1`).

### Task 3: Update course_inventory.json
- **File:** `course_inventory.json`
- **Action:** Update all stale entries:
  - **L12 entry:** Set `preview_slides` to `{"file": "lectures/tokenomics_mechanism_intro_preview.tex", "pdf": "lectures/tokenomics_mechanism_intro_preview.pdf", "frames": 6}`, set `preclass_handout` to `{"file": "lectures/tokenomics_mechanism_preclass.tex"}`, update technical lecture frames from 49 to 55.
  - **L13 entry:** Set `preview_slides` to `{"file": "lectures/privacy_zk_proofs_intro_preview.tex", "pdf": "lectures/privacy_zk_proofs_intro_preview.pdf", "frames": 6}`, set `preclass_handout` to `{"file": "lectures/privacy_zk_proofs_preclass.tex"}`.
  - **Summary counts — ALL of these must be updated:**
    - `total_standalone_preview_slides`: 11 → 13
    - `total_preclass_handouts`: 11 → 13
    - `total_frames_preview_slides`: 66 → 78 (adding 2 x 6 frames)
    - `total_frames_technical_lectures`: 706 → 712 (adding 6 frames to L12)
    - `total_frames_all`: 1075 → 1093 (adding 6 tech + 12 preview)
    - `total_quiz_questions`: 1117 → 1120 (adding 3 questions)
  - **`gaps_and_observations` — specific keys to handle:**
    - REMOVE: `missing_preclass_L12`, `missing_preclass_L13`, `missing_preview_L12`, `missing_preview_L13`
    - REMOVE: `quiz3_has_17_questions` (fixed by Task 1)
    - REMOVE: `L12_has_49_frames` (fixed by Task 2)
    - KEEP: `missing_notes_L05_to_L13`, `missing_lesson_lectures_L05_to_L13`, `missing_topic_pdfs_L05_to_L13` (still true, deferred)
    - KEEP: `L04_has_59_frames` (not a defect, just an observation)
- **Acceptance Criteria:**
  - JSON is valid (parseable by `jq` or `python -m json.tool`).
  - `total_standalone_preview_slides` = 13
  - `total_preclass_handouts` = 13
  - `total_frames_preview_slides` = 78
  - `total_frames_technical_lectures` = 712
  - `total_frames_all` = 1093
  - `total_quiz_questions` = 1120
  - `gaps_and_observations` has exactly 4 remaining keys (the deferred items + L04 observation).

### Task 4: Recompile L12 PDF
- **Action:** Run `pdflatex` twice on `lectures/tokenomics_mechanism.tex` to generate updated PDF with 55 frames.
- **Acceptance Criteria:** PDF compiles without errors. Output has 55 pages.

### Deferred (Not In Scope)
- **Lesson lectures for L05-L13:** These are a different format (~36 frames with live coding demos) from the standalone technical lectures (~55 frames, theory-focused). Creating 9 of these is a separate project, not a "fix."
- **Student notes:** No note template exists anywhere in the repo. This is a new deliverable requiring format design before content creation.

## Execution Order

1. Task 1 (quiz3.html) — independent
2. Task 2 (L12 frames) — independent
3. Task 4 (recompile L12 PDF) — depends on Task 2
4. Task 3 (update inventory) — depends on Tasks 1, 2

## Risks

| Risk | Mitigation |
|------|------------|
| TikZ compilation errors in new L12 frames | Use non-parameterized styles; test compile after adding frames |
| quiz3 question quality | Match difficulty and format of existing questions |
| L12 section imbalance after adding frames | Distribute frames across thinnest sections (Section 4 priority) |
| Hardcoded HTML counters in quiz3 | Explicitly update the progress badge `0/17` → `0/20` |

## Verification

- [ ] quiz3.html has 20 questions (grep count of `"id":` in questions array)
- [ ] quiz3.html progress badge shows `0/20` (not `0/17`)
- [ ] tokenomics_mechanism.tex has 55 `\begin{frame}` occurrences
- [ ] tokenomics_mechanism.pdf compiles without errors (55 pages)
- [ ] course_inventory.json is valid JSON
- [ ] course_inventory.json summary: preview=13, preclass=13, preview_frames=78, tech_frames=712, all_frames=1093, quiz_questions=1120
- [ ] gaps_and_observations has exactly 4 remaining keys
