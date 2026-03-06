# Course Improvement Plan: Ultra Hostile Review

## Status: REVISION 2 (Addressing Critic Feedback)

## Verdict: This course is a HALF-BUILT HOUSE sold as move-in ready.

The first 4 lessons are polished. The remaining 9 are bare studs and drywall. Anyone looking at the inventory will immediately see that L01-L04 are "premium" and L05-L13 are "economy class." This two-tier structure is the single most damaging problem. And the GH Pages landing page -- the first thing anyone sees -- claims this is a "4 Lessons" course when it has 13.

---

## SEVERITY CLASSIFICATION

| Severity | Meaning | Count |
|----------|---------|-------|
| **S1 - BROKEN** | Actively incorrect or misleading | 5 |
| **S2 - EMBARRASSING** | Visible quality gaps a reviewer/student will notice immediately | 8 |
| **S3 - UNPROFESSIONAL** | Inconsistencies that undermine credibility | 6 |
| **S4 - MISSED OPPORTUNITY** | Pedagogical improvements that would elevate the course | 5 |

---

## S1: BROKEN (Fix Immediately)

### S1-0: GH Pages hero claims "4 Lessons" -- the course has 13

**File:** `index.html`, lines 209-210
**Impact:** The FIRST thing any visitor sees. The hero banner says "BSc Level Course -- 4 Lessons" and the stats block shows `<b>4</b><small>Lessons</small>`. The course has **13 lessons**. This is a factual error visible within 2 seconds of loading the page. The stats also show "20 Topics" (stale from the original 4-lesson x 5-topics structure) and "7 Notebooks" (accurate for L01-L04 only).

**Evidence:**
```html
<p>BSc Level Course &mdash; 4 Lessons</p>
<div class="hero-stats">
  <span><b>4</b><small>Lessons</small></span>
  <span><b>20</b><small>Topics</small></span>
  <span><b>52</b><small>Lectures</small></span>
  <span><b>7</b><small>Notebooks</small></span>
  <span><b>56</b><small>Quizzes</small></span>
</div>
```

**Fix:** Update hero text to "13 Lessons", update stats to: Lessons=13, Topics=65 (13x5 sections), Lectures=52 (or accurate count), Notebooks=11, Quizzes=56. This is Sprint 1, item 0 -- the absolute first fix.

### S1-1: DAO Governance has 2 `\section{}` commands but 5 logical sections

**File:** `lectures/dao_governance.tex`
**Impact:** Beamer navigation bar shows 2 sections. Students see 2 dots in the progress indicator while 5 sections of content scroll by. Every other technical lecture (except L01/L02 which have 8) has exactly 5 `\section{}` commands.

**Evidence:**
```
dao_governance.tex: 2 sections    <-- BROKEN
blockchain_fundamentals.tex: 8 sections
cryptography_security.tex: 8 sections
All others (L03-L08, L10-L13): 5 sections
```

The inventory *claims* 5 sections: "DAO Fundamentals & Architecture", "Voting Mechanisms & Token Governance", "Treasury Management & Economics", "Governance Security", "Case Studies & Future". But only the first 2 have `\section{}` tags. Sections 3, 4, and 5 are missing their tags.

**Fix:** Add 3 missing `\section{}` commands before the frames for sections 3, 4, and 5. Recompile PDF.

### S1-2: L12/L13 quizzes use invalid JSON syntax

**Files:** `quiz/quiz_tm_part{1-4}.html`, `quiz/quiz_zk_part{1-4}.html` (8 files total)
**Impact:** Any automated tool, CI pipeline, or analytics system that parses quiz data as JSON will break on these files. They use JavaScript object literal syntax (unquoted keys) instead of valid JSON (quoted keys).

**Evidence:**
```
L01-L11 (48 files): "question": "Which field..."    <-- valid JSON
L12-L13 (8 files):   question: "Which field..."     <-- NOT valid JSON
```

14% of quiz files use a different format than the other 86%. The quizzes still *work* in a browser (JavaScript is lenient about key quoting), but this is a ticking time bomb for any tooling and a clear sign of inconsistent generation.

**Fix:** Convert all 8 L12/L13 quiz files to use quoted JSON keys matching L01-L11 format. Simple find-and-replace: wrap unquoted keys in double quotes.

### S1-3: L01 and L02 technical lectures are short of the 55-frame standard

**Files:** `lectures/blockchain_fundamentals.tex` (50 frames), `lectures/cryptography_security.tex` (52 frames)
**Impact:** The course standard is 55 frames per technical lecture. L03-L13 all have exactly 55. L01 is 10% short. L02 is 5% short. These are the FIRST two lectures students encounter -- they set the depth expectation.

| Lecture | Frames | Delta from 55 |
|---------|--------|---------------|
| L01 Blockchain | 50 | **-5** |
| L02 Cryptography | 52 | **-3** |
| L03 Ethereum | 55 | 0 |
| L04 ERC-20 | **59** | **+4** |
| L05-L13 | 55 each | 0 |

**Fix:** Add 5 frames to L01 and 3 frames to L02. Consider trimming 4 frames from L04 that overlap with L12 Tokenomics (e.g., "Token Valuation Frameworks", "Tokenomics in Code").

### S1-4: GH Pages has two-tier HTML structure -- L01-L04 get rich layout, L05-L13 get flat list

**File:** `index.html`
**Impact:** The GH Pages landing page treats L01-L04 and L05-L13 with completely different HTML/CSS structures:
- **L01-L04** (lines 213-520): Each lesson gets its own `<section>` with a numbered header, class-specific colors, a 5-card grid of topic diagrams (`.lgrid` with `.lcard` cards), AND a separate standalone lectures section.
- **L05-L13** (lines 520-858): All lumped into flat standalone lecture sections with a different card design (`.lec-card` vs `.lcard`). No topic grids, no per-lesson sections.

The sidebar navigation (lines 124-205) also reflects this: L01-L04 each have expandable dropdowns with 5 sub-links (one per topic). L05-L13 share a single "Standalone Lectures" dropdown with 52 flat links. A student looking for L09 DAOs material must scroll through 52 items.

**Fix:** Either:
- **A.** Give each of L05-L13 its own `<section>` in the main content area with a consistent card layout (matching L01-L04 structure minus the topic PDFs that don't exist yet).
- **B.** Restructure the entire page with a uniform layout that works for lessons with and without supplementary materials.

---

## S2: EMBARRASSING (Fix Before Any External Review)

### S2-1: Two-tier course structure -- L01-L04 are "premium", L05-L13 are "economy"

**Impact:** The most damaging structural issue. Any reviewer will instantly see:

| Resource | L01-L04 | L05-L13 |
|----------|---------|---------|
| Technical lecture (55 frames) | Yes | Yes |
| Mini lecture (10 frames) | Yes | Yes |
| Preview slides (6 frames) | Yes | Yes |
| Pre-class handout | Yes | Yes |
| 4 quizzes (80 questions) | Yes | Yes |
| **Lesson lecture (~36 frames, live coding)** | **Yes** | **NO** |
| **Student notes PDF** | **Yes** | **NO** |
| **Interactive Colab notebooks** | **Yes (1-2 each)** | **NO** |
| **Topic diagram PDFs (5 per lesson)** | **Yes** | **NO** |

L01-L04 students get ~105 frames + hands-on notebooks + notes + visual aids. L05-L13 students get ~70 frames + quizzes. That is a **50% resource gap**.

**Fix options (choose one):**
- **A. Full parity (massive):** Create lesson lectures, notebooks, notes, and topic PDFs for L05-L13. Estimated: 9 x (36-frame lecture + 2 notebooks + notes + 5 topic PDFs) = months of work.
- **B. Honest labeling:** Mark L01-L04 as "Extended Modules" and L05-L13 as "Core Modules" in the GH Pages and syllabus. Document the difference.
- **C. Hybrid (recommended):** Create notebooks for L05-L13 (highest pedagogical impact per effort) and defer lesson lectures/notes/topic PDFs. Update GH Pages to reflect what's available.

### S2-2: Massive content duplication across lectures

**Impact:** The same topics appear in multiple lectures without cross-references. Students hear the same material 2-4 times.

| Topic | Lectures That Cover It | Canonical Owner |
|-------|----------------------|-----------------|
| Terra/LUNA collapse | L05 DeFi, L07 Stablecoins, L11 RWA (mini too) | L07 Stablecoins |
| Impermanent Loss | L05 DeFi (+ intro, preclass), L08 Trading, L12 Tokenomics preclass | L05 DeFi |
| Howey Test | L11 RWA (+ intro, preclass), L12 Tokenomics | L11 RWA |
| ZK-SNARKs/STARKs | L02 Crypto, L10 Layer 2 (+ intro, preview, preclass), L13 Privacy (+ preview, preclass) | L13 Privacy |

**Worst offender:** L11 RWA Tokenization Section 2 is "Stablecoins Deep Dive" -- a 10-frame section that's essentially a recap of L07. That's 18% of the lecture repeating another lesson's material.

**Fix:** In duplicate locations, replace full treatments with 1-frame cross-references: "As covered in L07, see Stablecoins & CBDCs lecture." Keep full treatment only in the canonical owner. L11 Section 2 should become "Stablecoins as RWA" (2-3 frames referencing L07, not 10 frames re-teaching).

### S2-3: No learning objectives on any lecture

**Impact:** Basic instructional design (Bloom's taxonomy, backward design) requires explicit learning objectives. Not one of the 13 technical lectures has a "By the end of this lecture, you will be able to..." frame. Each has a "Lecture Roadmap" -- but that's a table of contents, not objectives.

**Fix:** Add a "Learning Objectives" frame (frame 2 or 3) to each of the 13 technical lectures. Each should list 4-5 measurable outcomes using Bloom's taxonomy verbs (explain, analyze, calculate, implement, evaluate). Example for L01:
```
By the end of this lecture, you will be able to:
1. Explain the double-spending problem and how blockchain solves it
2. Describe the structure of a block (header, body, hash pointers)
3. Compare Proof of Work and Proof of Stake consensus mechanisms
4. Analyze the security guarantees of hash-chain immutability
5. Calculate the probability of a successful 51% attack
```

### S2-4: GH Pages shows empty notebooks section for L05-L13

**Impact:** The landing page has an "Interactive Notebooks" section listing 7 notebooks, all for L01-L04. A student in L09 (DAOs) looking for hands-on exercises finds nothing. No message. Just silence.

**Fix:** Add a "Notebooks for L05-L13 coming soon" notice in the notebooks section, or add lesson-specific notes indicating which lessons currently have notebooks.

### S2-5: No formative assessment within lectures

**Impact:** All 13 technical lectures are 55-frame monologues. No embedded "Check Your Understanding" frames, no polling questions, no think-pair-share prompts. All assessment is externalized to the separate quiz HTML files. Students sit through ~55 slides before getting any feedback on comprehension.

**Fix:** Add 2-3 "Checkpoint" frames per technical lecture (one after each major section) with 1-2 multiple choice or short-answer questions. This is standard in evidence-based instructional design.

### S2-6: Original quizzes (quiz1-4.html) vs standalone quizzes (52 files) -- undefined relationship

**Files:** `quiz/quiz1.html` through `quiz/quiz4.html` (4 files), plus 52 standalone quiz files
**Impact:** The course has TWO overlapping quiz systems with no guidance on how they relate:
- **4 original quizzes** (quiz1-4.html): 20 questions each, one per L01-L04. Presented in a separate "Interactive Quizzes" section on GH Pages (lines 898-913).
- **52 standalone quizzes** (quiz_XX_partN.html): 20 questions each, 4 per lesson across all 13 lessons. Embedded within each lesson's standalone lecture section on GH Pages.

Students encounter both systems. No documentation explains: Are the originals summative and the standalone formative? Are they duplicates? Should students do both? Only L01-L04 have originals -- L05-L13 have only standalone. This is a confusing dual-assessment structure.

**Fix:** Either:
- **A. Remove originals:** Delete quiz1-4.html and remove their GH Pages section. The 52 standalone quizzes fully cover L01-L04 (80 questions each vs 20 in the originals).
- **B. Label them clearly:** Add header text to GH Pages explaining "Comprehensive Quizzes" (standalone, 4 parts x 20 questions) vs "Quick Review" (original, 20 questions).
- **C. Create originals for L05-L13:** Add quiz5-13.html to provide parity. But this adds 9 more quiz files to an already complex system.

### S2-7: assessments/README.md promises "5 exercise PDFs" that do not exist

**File:** `assessments/README.md`
**Impact:** The README explicitly states: "The instructor provides: 5 exercise PDFs (one per topic + comprehensive)". The actual directory contains only `README.md` and `final_report_template.md`. Zero exercise PDFs. This is a broken promise in the repository itself -- anyone browsing the assessments directory sees a claim for content that does not exist.

**Fix:** Either:
- **A.** Create the 5 exercise PDFs as promised.
- **B.** Update README.md to remove the false claim and accurately describe what exists.

### S2-8: Preclass handout inconsistency -- L01/L02 are richer

**Evidence:**
```
blockchain_fundamentals_preclass.tex: 5 activities, 233 lines
cryptography_security_preclass.tex:   5 activities, 231 lines
ethereum_smart_contracts_preclass.tex: 4 activities, 180 lines
All L04-L13:                          4 activities, 174-201 lines
```

L01/L02 preclass handouts have 5 activities each and are ~30% longer. L03-L13 have 4 activities. This again reinforces the "early lessons are premium" perception.

**Fix:** Either add a 5th activity to L03-L13 preclass handouts (consistent with L01/L02), or document the rationale for the difference.

---

## S3: UNPROFESSIONAL (Fix When Convenient)

### S3-1: LaTeX preamble inconsistency between L01-L02 and L03-L13

**Evidence:**
```
L01-L02: Missing amssymb, colortbl packages. Uses python lstset style.
L03-L13: Has amssymb, colortbl. Uses Solidity lstdefinelanguage + lstset.
```

L01/L02 were authored at a different time with a different template version. Package lists and listing configurations diverge.

**Fix:** Standardize all 13 preambles. Better yet: extract common preamble into `lectures/preamble.tex` and use `\input{preamble.tex}`.

### S3-2: Section count inconsistency -- L01/L02 have 8, L03-L13 have 5

**Evidence:**
```
L01: 8 sections (Intro, Block Anatomy, Hash Functions, Merkle Trees, PoW, PoS, Network, Security)
L02: 8 sections (Intro, Hash Functions, Symmetric, Asymmetric, Signatures, Key Mgmt, Protocols, Attacks)
L03-L13: 5 sections each (except L09 which is broken -- see S1-1)
```

Beamer navigation shows 8 dots for L01/L02 and 5 for all others. Students notice this visual inconsistency.

**Fix:** Consolidate L01 and L02 into 5 sections each (combine related topics). For example, L01: "Introduction", "Block Structure & Hashing", "Merkle Trees", "Consensus Mechanisms", "Network & Security".

### S3-3: Two naming conventions for mini lectures and preview slides

**Evidence:**
```
L01-L08 mini lectures:  {short}_intro.tex       (blockchain_intro.tex)
L01-L08 preview slides: {full}_intro.tex         (blockchain_fundamentals_intro.tex)
L09-L13 mini lectures:  {full}_intro.tex         (dao_governance_intro.tex)
L09-L13 preview slides: {full}_intro_preview.tex (dao_governance_intro_preview.tex)
```

The `_intro.tex` suffix means different things depending on the lesson number. This is confusing for maintainers.

**Fix:** Rename to a consistent scheme across all 13 lessons:
- Mini lectures: `{topic}_mini.tex`
- Preview slides: `{topic}_preview.tex`
This requires renaming 26 TEX files + 26 PDFs and updating all references (GH Pages, inventory JSON).

### S3-4: SYSTEMATIC color code mismatch between inventory metadata and GH Pages

**Evidence:** This is NOT a single typo -- the entire color palette diverges:

| Lesson | Inventory Color | index.html Color | Match? |
|--------|----------------|------------------|--------|
| L01 | `#2563eb` (blue) | `#3b82f6` (lighter blue) | NO |
| L02 | `#7c3aed` (purple) | `#14b8a6` (teal!) | **NO -- completely different hue** |
| L03 | `#0891b2` (cyan) | `#6366f1` (indigo!) | **NO -- completely different hue** |
| L04+ | Similar mismatches throughout | | |

The inventory and GH Pages were clearly authored independently. The inventory colors are decorative metadata that nobody uses. The GH Pages colors are what students actually see.

**Fix:** Delete the `color` field from `course_inventory.json` entirely (it serves no purpose and is wrong), OR update it to match the actual GH Pages CSS classes. Effort is small but requires auditing all 13 pairs.

### S3-5: L04 has 59 frames -- 4 over the 55 standard

**File:** `lectures/erc20_token_creation.tex`
**Impact:** Token economics content in L04 (Token Valuation Frameworks, Tokenomics in Code) overlaps with L12 Tokenomics. L04 is doing L12's job.

**Fix:** Remove or condense 4 frames that overlap with L12 to reach 55.

### S3-6: No shared LaTeX preamble file (despite template_beamer_final.tex existing)

**Impact:** All 52+ TEX files copy-paste ~45 lines of identical color definitions, beamer settings, and TikZ library imports. Any change must be replicated in every file.

**Note:** A `template_beamer_final.tex` (28 frames, 5 sections) already exists at project root. It contains color definitions, beamer settings, and sample frame layouts. The plan must decide: is this template the canonical preamble source, or is it a dead file? If it IS the reference template, the shared preamble should be extracted FROM it rather than created from scratch.

**Fix:** Audit `template_beamer_final.tex` to determine if its preamble matches current lectures. If yes, extract its preamble into `lectures/preamble.tex` and use `\input{preamble.tex}` in all lecture files. If no, update the template to match and THEN extract.

---

## S4: MISSED OPPORTUNITIES (Enhance When Resources Allow)

### S4-1: No inter-lesson prerequisite graph

The course teaches 13 topics but never shows how they connect. No visual showing that L05 DeFi requires L03 Smart Contracts and L04 ERC-20. Add to GH Pages.

### S4-2: No capstone project integration

A `final_report_template.md` exists in `assessments/` but there is no lecture, rubric, or example projects. Students get a template with zero context.

### S4-3: No instructor notes or teaching guide

If another instructor teaches this course, they have no pacing guide, emphasis points, or common-misconception notes.

### S4-4: Glossary not integrated into lectures

A `glossary.md` exists and is linked from GH Pages, but lectures don't reference it. Students must discover it independently.

### S4-5: No accessibility considerations

Beamer PDFs are not screen-reader friendly. TikZ diagrams have no alt-text. Quiz HTML has not been tested for WCAG compliance.

---

## PRIORITY MATRIX

| Issue | Severity | Effort | Priority |
|-------|----------|--------|----------|
| S1-0 GH Pages hero "4 Lessons" | S1 | Trivial (edit 2 lines of HTML) | **P0 -- FIX FIRST** |
| S1-1 DAO sections | S1 | Small (add 3 lines + recompile) | **P1** |
| S1-2 Quiz JSON format | S1 | Small (find-replace in 8 files) | **P1** |
| S1-3 L01/L02 frame counts | S1 | Medium (add 8 frames total) | **P2** |
| S1-4 GH Pages two-tier HTML | S1 | Medium-Large (restructure HTML) | **P2** |
| S2-1 Two-tier content structure | S2 | **Massive** | **P2 (plan now, execute later)** |
| S2-2 Content duplication | S2 | Medium (edit 5-7 lectures) | **P2** |
| S2-3 Learning objectives | S2 | Medium (add 13 frames) | **P2** |
| S2-4 GH Pages notebooks notice | S2 | Small (add notice) | **P1** |
| S2-5 No formative assessment | S2 | Large (26-39 new frames) | **P3** |
| S2-6 Original vs standalone quizzes | S2 | Small-Medium (decide + implement) | **P2** |
| S2-7 Missing exercise PDFs | S2 | Small (fix README or create PDFs) | **P1** |
| S2-8 Preclass inconsistency | S3 | Small-Medium | **P3** |
| S3-1 Preamble inconsistency | S3 | Small | **P3** |
| S3-2 Section count L01/L02 | S3 | Medium | **P3** |
| S3-3 Naming conventions | S3 | Medium (52 renames) | **P4** |
| S3-4 Color mismatch (systematic) | S3 | Small (audit 13 pairs) | **P3** |
| S3-5 L04 59 frames | S3 | Small | **P3** |
| S3-6 Shared preamble + template audit | S3 | Medium (refactor 52 files) | **P4** |
| S4-1 Prerequisite graph | S4 | Small | **P3** |
| S4-2 Capstone lecture | S4 | Medium | **P3** |
| S4-3 Teaching guide | S4 | Large | **P4** |
| S4-4 Glossary integration | S4 | Small | **P4** |
| S4-5 Accessibility | S4 | Large | **P4** |

---

## RECOMMENDED EXECUTION ORDER

### Sprint 0: Emergency GH Pages Fix (15 minutes)
0. Fix hero text: "4 Lessons" -> "13 Lessons", update all stats (Lessons=13, Notebooks=11)
1. Fix `assessments/README.md`: remove false claim about "5 exercise PDFs" or accurately describe what exists

### Sprint 1: Fix the Broken (1-2 hours)
2. Add 3 `\section{}` commands to `dao_governance.tex`, recompile PDF
3. Convert 8 L12/L13 quiz files to quoted JSON format
4. Add "coming soon" notice to GH Pages notebooks section for L05-L13
5. Decide on original quizzes (quiz1-4.html): label them as "Quick Review" or remove them

### Sprint 2: Standardize Frame Counts (4-6 hours)
6. Add 5 frames to L01 `blockchain_fundamentals.tex` to reach 55
7. Add 3 frames to L02 `cryptography_security.tex` to reach 55
8. Recompile both PDFs

### Sprint 3: Content Quality (1-2 days)
9. Add learning objectives frame to all 13 technical lectures
10. Reduce/replace duplicate content (Terra/LUNA in L11 RWA, stablecoins in L11 RWA Section 2, ZK in L02/L10)
11. Fix inventory color codes (delete or sync with GH Pages)
12. Audit `template_beamer_final.tex` vs lecture preambles

### Sprint 4: GH Pages Structural Parity (2-3 days)
13. Restructure `index.html` so L05-L13 get per-lesson sections matching L01-L04 layout
14. Fix sidebar navigation: give each lesson its own expandable section
15. Create interactive notebooks for L05-L08 (DeFi, NFT, Stablecoins, Trading)

### Sprint 5: Lecture Standardization (1 week)
16. Consolidate L01/L02 to 5 sections each
17. Standardize LaTeX preambles (extract shared preamble.tex from template)
18. Trim L04 from 59 to 55 frames

### Sprint 6+: Full Parity (ongoing)
19. Create notebooks for L09-L13
20. Rename files to consistent naming convention
21. Add formative assessment checkpoints to all lectures
22. Create lesson lectures for L05-L13 (if desired)

---

## ACCEPTANCE CRITERIA FOR THIS PLAN

- [x] Every S1 issue has a concrete fix with specific file paths
- [x] Every S2 issue has a clear remediation path with options where appropriate
- [x] Priority matrix maps effort to value
- [x] Execution order respects dependencies (Sprint 0 before Sprint 1)
- [x] No vague "improve" or "enhance" -- every item is actionable with evidence
- [x] Content duplication identified with specific cross-lecture references
- [x] Frame counts verified against actual grep data
- [x] Section counts verified against actual grep data
- [x] Quiz format difference demonstrated with actual file content
- [x] GH Pages hero text factual error identified (Critic issue #1)
- [x] Original vs standalone quiz relationship addressed (Critic issue #2)
- [x] Missing assessments exercise PDFs flagged (Critic issue #3)
- [x] template_beamer_final.tex analyzed in context of shared preamble (Critic issue #4)
- [x] Color mismatch documented as systematic, not single typo (Critic issue #5)
