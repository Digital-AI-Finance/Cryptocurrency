# Plan: L02 Technical Lecture + GH Pages Update

## 1. Context

### Scope (from interview)
- **Keep** existing mini-lecture (`cryptography_intro.tex`) -- no changes
- **Create** technical quantitative lecture (`cryptography_security.tex`) -- ~55 frames, 8 sections
- **Update** `index.html` -- add CS subsection combined under existing Standalone Lectures section
- Follow the full L02 plan as-is for topic emphasis (detailed frame-by-frame specs in `.omc/plans/l02-lectures.md` Section 5, T5, lines 282-403)

### What Already Exists (no modifications)
- `lectures/cryptography_intro.tex` (10 frames, mini-lecture)
- `lectures/cryptography_security_intro.tex` (6 frames, INTRO preview)
- `lectures/cryptography_security_preclass.tex` (pre-class handout)
- `quiz/quiz_cs_part1.html` through `quiz_cs_part4.html` (80 questions)

### What Must Be Created
1. `lectures/cryptography_security.tex` -- 50-70 frame technical lecture
2. `index.html` modifications -- CS subsection + hero stats + sidebar

---

## 2. Deliverables

| ID | File | Action | Description |
|----|------|--------|-------------|
| D1 | `lectures/cryptography_security.tex` | CREATE | ~55 frame beamer lecture, 8 sections, 15+ TikZ, 5+ pgfplots |
| D2 | `index.html` | MODIFY | Add CS subsection within Standalone Lectures, update stats/sidebar |

---

## 3. Task Plan

### T1: Create Technical Lecture (`cryptography_security.tex`)

**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/cryptography_security.tex`
**Effort:** High (largest deliverable)

**Preamble:** Copy verbatim from `lectures/blockchain_fundamentals.tex` lines 1-31 (compact beamer preamble with 10 colors, listings, TikZ/pgfplots with `chains` + `automata` libraries). Then set:
```latex
\title{Cryptography \& Security: A Quantitative Deep Dive}
\subtitle{Standalone Technical Lecture}
\author{Prof.~Dr.~Joerg Osterrieder}
\institute{University Lecture Series}
\date{\today}
```

**8 Sections (~55 frames):**

| Section | Frames | Topic | Key Visuals |
|---------|--------|-------|-------------|
| 1. Introduction & Motivation | 5 | Timeline, Kerckhoffs, threat model, roadmap | TikZ timeline, taxonomy tree |
| 2. Hash Functions Deep Dive | 7 | Formal properties, Merkle-Damgard, SHA-256, sponge, birthday bound | TikZ pipeline, pgfplots collision curve + throughput chart |
| 3. Symmetric Cryptography | 5 | AES, block cipher modes, Diffie-Hellman, hybrid | TikZ round diagram + modes, pgfplots throughput comparison |
| 4. Asymmetric Cryptography | 7 | RSA, elliptic curves, ECDSA keys, ECDLP, Ed25519 | TikZ EC point addition, pgfplots attack complexity |
| 5. Digital Signatures | 7 | ECDSA, Schnorr, MuSig, multi-sig, nonce reuse, batch verify | TikZ signing flows, pgfplots batch verification + comparison |
| 6. Key Management & Wallets | 6 | BIP-39/32/44, HD wallets, hardware wallets, Shamir | TikZ derivation tree, security model, Shamir diagram |
| 7. Cryptographic Protocols | 6 | ZK proofs, SNARKs/STARKs, commitments, secret sharing, ring sigs | TikZ cave diagram, commitment flow, ring signature circle |
| 8. Attacks & Post-Quantum | 9 | Birthday attack, length extension, side-channel, Shor, Grover, PQC, migration | pgfplots hash comparison + qubit timeline + PQC key sizes |

**Total:** 52 frames + summary/questions = ~55 frames

**Constraints:**
- All visuals via TikZ/pgfplots -- NO `\includegraphics`
- All TikZ uses course colors (mlblue, mlpurple, mlorange, mlgreen, mlred)
- Uses `\bottomnote{}` on content frames
- Content deeper than existing L02 (covers symmetric crypto, sponge, Schnorr, ZK proofs, post-quantum -- topics absent from existing L02)
- Mathematical formulations: hash properties, ECDSA, birthday bound, DH, Shamir polynomial

**Acceptance Criteria:**
- [ ] 50-70 `\begin{frame}` blocks
- [ ] 8 `\section{}` commands
- [ ] >= 15 `\begin{tikzpicture}` environments
- [ ] >= 5 `\begin{axis}` environments
- [ ] No `\includegraphics` calls
- [ ] Preamble matches `blockchain_fundamentals.tex` lines 1-31

### T2: Update GH Pages (`index.html`)

**File:** `D:/Joerg/Research/slides/cryptocurrency/index.html`
**Effort:** Low-Medium

**Changes:**

1. **Hero stats** (line 145): Change `<b>4</b><small>Lectures</small>` to `<b>8</b>` and `<b>8</b><small>Quizzes</small>` to `<b>12</b>`

2. **Sidebar** (after line 139): Add CS entries inside existing `<details class="d5">`:
   ```html
   <a href="#sl-cs-mini">Mini-Lecture: Crypto</a>
   <a href="#sl-cs-intro">CS INTRO Preview</a>
   <a href="#sl-cs-pre">CS Pre-Class Handout</a>
   <a href="#sl-cs-main">CS Technical Lecture</a>
   ```

3. **CS subsection** (insert before `</section>` at line 322): Add within existing `<section class="section d5">`:
   - New section-head div with "CS" badge and "Standalone Lectures: Cryptography & Security" title
   - Mini-lecture card linking to `lectures/cryptography_intro.pdf`
   - Technical bundle grid (INTRO, PRE, 90min cards)
   - Quiz grid (CS-1 through CS-4 cards)

**Combined approach:** Both BF and CS content lives within the single `<section class="section d5" id="standalone-lectures">` element. Each has its own visual `section-head` div.

**Acceptance Criteria:**
- [ ] CS subsection renders within Standalone Lectures section
- [ ] All 4 lecture cards link to correct PDF paths
- [ ] All 4 quiz cards link to correct HTML paths
- [ ] Hero stats show: 8 Lectures, 12 Quizzes
- [ ] Sidebar has 8 links (4 BF + 4 CS)
- [ ] Existing BF subsection unchanged
- [ ] Valid HTML, no broken structure

---

## 4. Execution Strategy

### Parallelization
T1 and T2 are **independent** -- execute in parallel:
- T1: Delegate to `executor-high` (opus) -- largest task, needs deep crypto expertise
- T2: Delegate to `executor` (sonnet) -- HTML editing, moderate complexity

### Implementation Notes for T1

Due to the size (~55 frames), split T1 into two sub-tasks:
- **T1a:** Sections 1-4 (preamble + 24 frames: Intro, Hash, Symmetric, Asymmetric)
- **T1b:** Sections 5-8 (28 frames: Signatures, Wallets, Protocols, Attacks + Summary/Questions)

Both write to the same file sequentially (T1b appends after T1a).

### Template References
- Preamble: `lectures/blockchain_fundamentals.tex` lines 1-31 (preamble) + new title block
- TikZ patterns: `lectures/blockchain_fundamentals.tex` (technical diagrams, flow charts)
- pgfplots patterns: `lectures/cryptography_intro.tex` frame 9 (grouped bar chart)
- Elliptic curve TikZ: Use smooth curves over reals, not finite field points

---

## 5. Verification Steps

| Check | Command/Method | Pass Criteria |
|-------|---------------|---------------|
| V1 | `grep -c 'begin{frame}' lectures/cryptography_security.tex` | 50-70 |
| V2 | `grep -c '\\section{' lectures/cryptography_security.tex` | 8 |
| V3 | `grep -c 'begin{tikzpicture}' lectures/cryptography_security.tex` | >= 15 |
| V4 | `grep -c 'begin{axis}' lectures/cryptography_security.tex` | >= 5 |
| V5 | `grep -c 'includegraphics' lectures/cryptography_security.tex` | 0 |
| V6 | Visual check of index.html CS subsection | Cards render, links valid |
| V7 | Hero stats in index.html | Lectures=8, Quizzes=12 |
| V8 | Sidebar link count | 8 entries in d5 details |

---

## 6. Risk Mitigation

| Risk | Mitigation |
|------|------------|
| TikZ compilation errors in complex crypto diagrams | Use patterns from existing mini-lecture. Keep diagrams modular. Test with simple coordinates for EC curves. |
| File too large for single agent | Split into T1a (sections 1-4) and T1b (sections 5-8) |
| Content overlap with existing L02 | New lecture covers symmetric crypto, sponge, Schnorr, ZK proofs, post-quantum -- all absent from existing L02 |
| index.html breaking BF section | Insert CS after BF content, never modify BF HTML |

---

## 7. Definition of Done

1. `lectures/cryptography_security.tex` exists with 50-70 frames, 8 sections, 15+ TikZ, 5+ pgfplots
2. `index.html` has CS subsection with all cards + updated stats + sidebar
3. No existing files modified (except `index.html`)
4. Architect verification passed
