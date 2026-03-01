# Plan: L01 Standalone Lectures -- Full Bundle

## 1. Context

### Original Request
Create two new lecture products for Lesson 01 (Blockchain Fundamentals):
1. A 10-slide mini-lecture (Pattern A) -- broad blockchain overview with TikZ comics and pgfplots
2. A full technical quantitative lecture bundle (Pattern B) -- INTRO preview, pre-class handout, 50-70 frame main lecture, and 4-part quiz (80 questions)

All materials added to the GH Pages `index.html`.

### Interview Summary
- Mini-lecture: ALL blockchain fundamentals topics (broad overview, 10 slides)
- Technical lecture: NEW STANDALONE (do not modify existing `01_blockchain_fundamentals.tex`)
- Format: LaTeX beamer `.tex` files
- Ecosystem: FULL BUNDLE (INTRO + pre-class + main lecture + 4-part quiz)

### Codebase Facts (from research)
- **Beamer template**: `template_beamer_final.tex` at repo root -- Madrid theme, 8pt, 169 aspect ratio
- **Color palette**: mlblue (#0066CC), mlpurple (#3333B2), mllavender family (4 levels), mlorange, mlgreen, mlred, mlgray, lightgray, midgray
- **Theme config**: palette primary/secondary/tertiary/quaternary, structure, frametitle, block title/body
- **Custom macro**: `\bottomnote{}` -- vfill + rule + footnotesize bold text
- **Listings style**: `python` style defined with course colors
- **Existing L01**: 36 frames (`\begin{frame}` blocks), 5 sections, 5 PNG/PDF images from subdirs. Already covers Python code demos, block header details, and Byzantine Generals content -- so the new technical lecture must differentiate with deeper quantitative treatment beyond this 36-frame baseline.
- **Quiz format**: HTML with KaTeX, 3-column grid, CSS variables matching course colors, nav bar with mlpurple-to-mlblue gradient, progress bar, stat badges, `loadNextQuestions()` pagination in groups of 3
- **GH Pages**: `index.html` (374 lines) with sidebar nav, hero stats, lesson/notebook/quiz/notes/resources sections
- **`lectures/` directory**: Does NOT exist yet -- must be created
- **Existing quizzes**: `quiz/quiz1.html` through `quiz/quiz4.html` (4 files, 20 questions each)

---

## 2. Work Objectives

### Core Objective
Produce a complete standalone lecture ecosystem for Blockchain Fundamentals that complements (but does not duplicate) the existing L01 slide deck, following the patterns from the Digital-Finance-Introduction reference repository.

### Deliverables

| ID | File | Type | Description |
|----|------|------|-------------|
| D1 | `lectures/blockchain_intro.tex` | Mini-lecture | 10-slide beamer with TikZ comics + pgfplots chart |
| D2 | `lectures/blockchain_fundamentals_intro.tex` | INTRO preview | 6-slide preview deck with TikZ + pgfplots |
| D3 | `lectures/blockchain_fundamentals_preclass.tex` | Pre-class handout | 2-page discovery activities PDF |
| D4 | `lectures/blockchain_fundamentals.tex` | Technical lecture | 50-70 frame lecture with 13+ TikZ diagrams |
| D5a | `quiz/quiz_bf_part1.html` | Quiz Part 1 | Block Anatomy & Hash Chains (20 questions) |
| D5b | `quiz/quiz_bf_part2.html` | Quiz Part 2 | Merkle Trees & Data Structures (20 questions) |
| D5c | `quiz/quiz_bf_part3.html` | Quiz Part 3 | Consensus Mechanisms (20 questions) |
| D5d | `quiz/quiz_bf_part4.html` | Quiz Part 4 | Decentralization & Security (20 questions) |
| D6 | `index.html` (modified) | GH Pages | New "Standalone Lectures" section with all cards |

### Definition of Done
1. All 9 files exist in the correct locations
2. All `.tex` files compile with `pdflatex` without errors (user verifies)
3. All `.tex` files use the exact same beamer preamble (Madrid, same colors, same `\bottomnote{}`)
4. Mini-lecture has exactly 10 frames with at least 1 TikZ comic strip and 1 pgfplots chart
5. INTRO preview has exactly 6 frames with 3 TikZ + 3 pgfplots
6. Pre-class handout is article class, 2 pages, landscape-ready activities
7. Technical lecture has 50-70 frames, 8 sections, 13+ TikZ diagrams
8. Each quiz has exactly 20 questions in the exact HTML/CSS/JS format as `quiz/quiz1.html`
9. `index.html` has a new "Standalone Lectures" section with BF badge and full bundle cards
10. No existing files modified (except `index.html`)
11. Content in D4 is deeper, more quantitative, and more TikZ-heavy than existing L01

---

## 3. Guardrails

### MUST HAVE
- Identical beamer preamble to existing L01 (colors, theme, `\bottomnote{}`)
- `\usepackage{tikz}` and `\usepackage{pgfplots}` added where needed
- TikZ libraries: `arrows.meta`, `positioning`, `shapes.geometric`, `calc`, `chains`, `decorations.pathmorphing`
- pgfplots `compat=1.18` or `newest`
- Quiz HTML/CSS/JS structure identical to `quiz/quiz1.html`
- Quiz nav links point to `../index.html` for Dashboard
- All content technically accurate and appropriate for BSc level
- Mathematical formulations in the technical lecture (hash functions, probability of mining, staking economics)
- Author: Prof. Dr. Joerg Osterrieder
- Institute: University Lecture Series

### MUST NOT HAVE
- Any modifications to existing `01_blockchain_fundamentals/01_blockchain_fundamentals.tex`
- Any modifications to existing `quiz/quiz1.html` through `quiz/quiz4.html`
- External image dependencies (all visuals via TikZ/pgfplots inline)
- Content that merely duplicates the existing L01 slides
- Hardcoded dates (use `\today`)
- Non-compiling LaTeX (no undefined commands, missing packages)

---

## 4. Task Flow

### Dependency Graph

```
T1 (create lectures/ dir)
  |
  +---> T2 (mini-lecture D1) --------+
  |                                   |
  +---> T3 (INTRO preview D2) -------+
  |                                   |
  +---> T4 (pre-class handout D3) ---+---> T8 (index.html update D6)
  |                                   |
  +---> T5 (technical lecture D4) ---+
                                      |
T6 (quiz part 1-2, D5a+D5b) --------+
T7 (quiz part 3-4, D5c+D5d) --------+
```

**Parallelizable groups:**
- Group A: T2 + T3 + T4 (independent LaTeX files)
- Group B: T6 + T7 (independent quiz HTML files)
- T5 runs alone (largest deliverable, 50-70 frames)
- T8 runs last (depends on all file paths being finalized)

---

## 5. Detailed Tasks

### T1: Create `lectures/` Directory
**Priority:** P0 (prerequisite)
**Effort:** Trivial
**Action:** `mkdir -p lectures/`
**Acceptance Criteria:**
- [ ] Directory `D:/Joerg/Research/slides/cryptocurrency/lectures/` exists

---

### T2: Mini-Lecture -- `lectures/blockchain_intro.tex` (D1)
**Priority:** P1
**Effort:** Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_intro.tex`

**Specification:**
Exactly 10 frames. Same beamer preamble as existing L01 plus TikZ/pgfplots packages.

**Frame-by-frame content:**

| Frame | Title | Content | Visual |
|-------|-------|---------|--------|
| 1 | Title slide | "Blockchain Fundamentals: A Visual Introduction" + "digital chain of trust" hook analogy | Plain title layout |
| 2 | The Trust Problem | TikZ comic strip panel 1: Alice wants to send money to Bob, but how to trust without a bank? | TikZ comic (stick figures, speech bubbles, thought clouds) |
| 3 | Chaining Blocks | TikZ comic strip panel 2: Blocks linking together, hash arrows, narrator explains immutability | TikZ comic (block boxes with hash arrows, narrator character) |
| 4 | Immutability | Core concept 1: Cryptographic hashing, avalanche effect, tamper-evident chain | TikZ diagram: block modification cascading invalidation |
| 5 | Consensus | Core concept 2: How the network agrees -- PoW lottery analogy, PoS staking analogy | TikZ split diagram: miners vs validators |
| 6 | Decentralization | Core concept 3: No single point of failure, network topology | TikZ network diagram: centralized vs decentralized vs distributed |
| 7 | Risks: The 51% Attack | Edge case 1: What happens when one entity controls majority | TikZ pie chart + attack scenario diagram |
| 8 | The Scalability Trilemma | Edge case 2: Security vs Decentralization vs Scalability trade-off | TikZ triangle diagram with labels |
| 9 | Blockchain by the Numbers | pgfplots chart: Bitcoin mining difficulty over time (log scale) OR TPS comparison across chains | pgfplots bar/line chart with real-world approximate data |
| 10 | Takeaways & Evaluation Framework | 5 evaluation questions for any blockchain project: Is it decentralized? Immutable? Transparent? Scalable? Secure? | Structured checklist layout |

**Preamble additions (beyond base template):**
```latex
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, decorations.pathmorphing}
```

**Acceptance Criteria:**
- [ ] Exactly 10 `\begin{frame}` ... `\end{frame}` blocks
- [ ] At least 2 frames with TikZ comic strip elements (stick figures, speech bubbles)
- [ ] At least 1 frame with a pgfplots chart (axis environment)
- [ ] Uses `\bottomnote{}` on content frames
- [ ] Title: "Blockchain Fundamentals: A Visual Introduction"
- [ ] Subtitle references "Standalone Mini-Lecture"
- [ ] Author: Prof. Dr. Joerg Osterrieder
- [ ] All TikZ diagrams use course colors (mlblue, mlpurple, mlorange, mlgreen, mlred)
- [ ] Compiles with pdflatex (no external images required)

---

### T3: INTRO Preview -- `lectures/blockchain_fundamentals_intro.tex` (D2)
**Priority:** P1
**Effort:** Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_fundamentals_intro.tex`

**Specification:**
Exactly 6 frames. Preview deck teasing the full technical lecture. Mix of TikZ and pgfplots.

| Frame | Title | Visual Type | Content |
|-------|-------|-------------|---------|
| 1 | Title | -- | "Blockchain Fundamentals: Course Preview" |
| 2 | Block Anatomy | TikZ | Detailed block diagram with header fields and body |
| 3 | Hash Linking & Merkle Trees | TikZ | Chain of 3 blocks + mini Merkle tree inside one block |
| 4 | PoW vs PoS Energy | pgfplots | Bar chart comparing energy consumption (TWh) |
| 5 | Decentralization Spectrum | pgfplots | Spectrum chart: fully centralized to fully decentralized with example projects plotted |
| 6 | Blockchain Adoption Trends | pgfplots | Line chart: number of blockchain wallets / active addresses over years (approximate data) |

**Acceptance Criteria:**
- [ ] Exactly 6 frames
- [ ] At least 2 TikZ diagrams (frames 2, 3)
- [ ] At least 3 pgfplots charts (frames 4, 5, 6)
- [ ] Uses identical beamer preamble + TikZ/pgfplots packages
- [ ] Subtitle: "INTRO Preview -- What You Will Learn"
- [ ] Compiles with pdflatex

---

### T4: Pre-Class Handout -- `lectures/blockchain_fundamentals_preclass.tex` (D3)
**Priority:** P1
**Effort:** Low-Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_fundamentals_preclass.tex`

**Specification:**
This is NOT a beamer document. It is an `article` class document, 2 pages, designed as a pre-class discovery handout.

**Document class:** `\documentclass[11pt,a4paper]{article}`
**Uses:** Same color definitions, geometry package for margins, enumitem for lists

**Article-class preamble template (T4 does NOT use the beamer preamble):**
```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=2cm]{geometry}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{hyperref}

% Course color palette (copied from beamer preamble)
\definecolor{mlblue}{HTML}{0066CC}
\definecolor{mlpurple}{HTML}{3333B2}
\definecolor{mllavender}{HTML}{ADADE0}
\definecolor{mllavender2}{HTML}{C1C1E8}
\definecolor{mllavender3}{HTML}{CCCCEB}
\definecolor{mllavender4}{HTML}{D6D6EF}
\definecolor{mlorange}{HTML}{FF7F0E}
\definecolor{mlgreen}{HTML}{2CA02C}
\definecolor{mlred}{HTML}{D62728}
\definecolor{mlgray}{HTML}{7F7F7F}
\definecolor{lightgray}{HTML}{F0F0F0}
\definecolor{midgray}{HTML}{B4B4B4}
```
**Important:** The `\bottomnote{}` macro is NOT available in article class. Do not use it in T4. Use standard `\footnote{}` or manual footer text instead.

**Page 1: "What Makes a Digital Ledger Trustworthy?"**
- Activity 1: "The Broken Telephone" -- Students pass a message and observe how it changes. Analogy to data integrity.
- Activity 2: "Hash It Yourself" -- Given 3 short strings, students compute a simple checksum (sum of ASCII values mod 256). Discover the avalanche effect when one character changes.
- Activity 3: "Link the Chain" -- Paper exercise: create 3 "blocks" on index cards with hash of previous block. Try tampering with block 2 -- what happens?

**Page 2: "How Do Strangers Agree?"**
- Activity 4: "The Byzantine Generals" -- Role-play scenario: 5 students are generals, 1 is a traitor. How do they agree on attack/retreat? Connect to consensus.
- Activity 5: "Staking vs Mining" -- Compare two reward mechanisms: lottery (PoW) vs weighted vote (PoS). Which is fairer? Which is cheaper?
- Reflection Questions: 3 open-ended questions for students to bring to class.

**Acceptance Criteria:**
- [ ] Uses `article` class, NOT beamer
- [ ] Exactly 2 pages when compiled
- [ ] Uses same course colors (mlblue, mlpurple, etc.)
- [ ] Contains 5 discovery activities
- [ ] Contains 3 reflection questions
- [ ] Header with course title, lesson number, "Pre-Class Discovery Handout"
- [ ] Compiles with pdflatex

---

### T5: Technical Quantitative Lecture -- `lectures/blockchain_fundamentals.tex` (D4)
**Priority:** P0 (largest deliverable)
**Effort:** High
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_fundamentals.tex`

**Specification:**
50-70 frames, 8 sections, 13+ TikZ diagrams, mathematical formulations, quantitative focus. Content must be DIFFERENT and DEEPER than existing L01.

**Section Plan:**

#### Section 1: Introduction & Motivation (5-6 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 1 | Title slide | "Blockchain Fundamentals: A Quantitative Deep Dive" | -- |
| 2 | Historical Context | Timeline from DigiCash (1989) to Bitcoin (2008) to Ethereum (2015) to present | TikZ timeline diagram |
| 3 | The Problem Statement | Formal definition of the double-spending problem. Mathematical notation. | TikZ: two conflicting transaction paths |
| 4 | Trust Models | Centralized vs distributed trust. Formal trust assumptions. | TikZ: trust model comparison |
| 5 | Course Roadmap | What this lecture covers -- 8 sections overview | -- |

#### Section 2: Block Anatomy (6-8 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 6 | Block Data Structure | Formal specification: `Block = (index, timestamp, data, prevHash, nonce, hash)` | TikZ: detailed block diagram with field sizes |
| 7 | Block Header Fields | Each field explained with byte sizes (Bitcoin: 80-byte header) | TikZ: byte-level layout diagram |
| 8 | Block Body: UTXO Model | Unspent Transaction Output model. Inputs reference previous outputs. | TikZ: UTXO flow diagram |
| 9 | Block Body: Account Model | Ethereum's account-based model vs UTXO. State transitions. | TikZ: state transition diagram |
| 10 | Transaction Structure | Bitcoin transaction format: version, inputs[], outputs[], locktime | TikZ: transaction anatomy |
| 11 | Coinbase Transaction | Special first transaction in each block. Mining reward mechanism. | -- |

#### Section 3: Hash Functions & Cryptographic Linking (7-9 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 12 | Hash Function Properties | Formal: preimage resistance, second preimage resistance, collision resistance | -- |
| 13 | SHA-256 Overview | Merkle-Damgard construction, compression function, 64 rounds | TikZ: SHA-256 pipeline diagram |
| 14 | The Avalanche Effect | Mathematical: Hamming distance analysis. One-bit input change -> ~50% output bits flip. | pgfplots: bit-flip distribution histogram |
| 15 | Hash Pointers & Linked Lists | Formal: `H(B_i) = SHA256(B_i.header)`, `B_i.prevHash = H(B_{i-1})` | TikZ: chain of blocks with hash arrows |
| 16 | Birthday Paradox & Collision Probability | $P(\text{collision}) \approx 1 - e^{-n^2/(2 \cdot 2^{256})}$ | pgfplots: collision probability curve |
| 17 | Tamper Detection Proof | Formal proof: changing any block invalidates all subsequent hashes | TikZ: cascade invalidation diagram |

#### Section 4: Merkle Trees (5-6 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 18 | Binary Hash Tree | Definition: leaf nodes = H(tx), internal nodes = H(child1 || child2) | TikZ: full Merkle tree diagram |
| 19 | Merkle Proof (SPV) | Verification path: $O(\log n)$ hashes needed. Formal proof path. | TikZ: highlighted proof path in tree |
| 20 | Proof Verification Algorithm | Step-by-step: given tx, siblings, root -- verify inclusion | -- (pseudocode) |
| 21 | Merkle Tree Efficiency | Comparison: naive verification $O(n)$ vs Merkle $O(\log n)$ | pgfplots: comparison chart (n vs log n) |
| 22 | Patricia Merkle Tries | Ethereum's modified Merkle Patricia Trie for state storage | TikZ: trie structure diagram |

#### Section 5: Proof of Work (7-9 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 23 | PoW Formal Definition | Find nonce s.t. $H(\text{header} \| \text{nonce}) < T$ where $T$ is target | -- |
| 24 | Mining as Bernoulli Trials | Each hash attempt: $P(\text{success}) = T / 2^{256}$. Expected attempts: $2^{256}/T$ | -- |
| 25 | Difficulty Adjustment | Bitcoin: recalculate every 2016 blocks. $D_{new} = D_{old} \times (T_{actual} / T_{target})$ | pgfplots: difficulty over time (log scale) |
| 26 | Mining Economics | Revenue: block reward + fees. Cost: electricity + hardware. Break-even analysis. | pgfplots: cost vs revenue chart |
| 27 | Hash Rate Distribution | Current mining pool distribution. Concentration risks. | pgfplots: pie/bar chart of pool shares |
| 28 | Selfish Mining Strategy | Formal: publish blocks strategically to gain unfair advantage. Threshold: 1/3 hashrate. | TikZ: block withholding timeline diagram |
| 29 | Energy Consumption Analysis | Bitcoin network: ~150 TWh/year. Comparison to countries. | pgfplots: energy comparison bar chart |

#### Section 6: Proof of Stake (7-9 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 30 | PoS Formal Definition | Validator selection: $P(\text{selected}) = \text{stake}_i / \sum \text{stake}$ | -- |
| 31 | Validator Lifecycle | Deposit -> active -> proposing -> attesting -> exit/slashing | TikZ: state machine diagram |
| 32 | Slashing Conditions | Double voting, surround voting. Penalty: up to full stake. | TikZ: slashing scenario diagram |
| 33 | Nothing-at-Stake Problem | Without slashing: validators can vote on all forks costlessly | TikZ: fork diagram with multi-voting |
| 34 | Finality: Casper FFG | Ethereum's finality gadget. Checkpoints, justified, finalized. 2/3 supermajority. | TikZ: checkpoint chain diagram |
| 35 | Staking Economics | APY calculation: $r = \frac{R}{S}$ where R=total rewards, S=total staked | pgfplots: staking yield curve |
| 36 | PoW vs PoS Quantitative | Side-by-side: energy, finality time, attack cost, minimum stake | -- (comparison table) |

#### Section 7: Network & Decentralization (6-8 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 37 | P2P Network Topology | Unstructured overlay network. Gossip protocol. | TikZ: network graph with gossip propagation |
| 38 | Block Propagation | Compact block relay, fiber network. Propagation time distribution. | pgfplots: propagation time histogram |
| 39 | Fork Resolution | Longest chain rule (PoW), heaviest chain (PoS). Orphan blocks. | TikZ: forking and resolution diagram |
| 40 | Nakamoto Coefficient | Minimum number of entities to control >50%. Measures decentralization. | pgfplots: Nakamoto coefficient across chains |
| 41 | Decentralization Metrics | Gini coefficient of stake/hashrate. Shannon entropy of validator set. | -- (formulas + interpretation) |
| 42 | Full Nodes vs Light Clients | Resource requirements, security trade-offs, SPV fraud proofs | TikZ: node hierarchy diagram |

#### Section 8: Security Analysis & Future (7-9 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 43 | 51% Attack Analysis | Formal: probability of k-deep reorganization with fraction q of hashrate | -- |
| 44 | Attack Cost Estimation | Cost to attack Bitcoin: hardware + electricity for 1 hour of majority | pgfplots: attack cost over time |
| 45 | Byzantine Generals Theorem | Formal: tolerates up to $f < n/3$ Byzantine nodes (PBFT). Bitcoin tolerates $f < n/2$. | TikZ: generals diagram |
| 46 | Sybil Attack & Countermeasures | Identity-free systems. PoW/PoS as Sybil resistance mechanisms. | TikZ: Sybil attack diagram |
| 47 | Quantum Computing Threat | Grover's algorithm: square root speedup for mining. Shor's algorithm: breaks ECDSA. | -- |
| 48 | Layer 2 Solutions | Lightning Network, rollups, state channels. Scalability without sacrificing security. | TikZ: L1/L2 architecture diagram |
| 49 | Cross-Chain Interoperability | Bridges, atomic swaps, relay chains. Trust assumptions. | TikZ: bridge architecture |
| 50+ | Summary & Key Formulas | Formula reference sheet. All key equations from the lecture. | -- |
| 51+ | Questions & Discussion | Open-ended prompts for class discussion | -- |

**Preamble (same as T2, plus listings for pseudocode):**
```latex
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{listings}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, chains, decorations.pathmorphing, automata}
```

**Acceptance Criteria:**
- [ ] 50-70 `\begin{frame}` blocks (count frames, not slides)
- [ ] Exactly 8 `\section{}` commands
- [ ] At least 13 distinct TikZ pictures (`\begin{tikzpicture}`)
- [ ] At least 5 pgfplots charts (`\begin{axis}`)
- [ ] Mathematical formulations: hash function properties, mining probability, difficulty adjustment formula, staking probability, attack cost, collision probability
- [ ] Uses `\bottomnote{}` on content frames
- [ ] Title: "Blockchain Fundamentals: A Quantitative Deep Dive"
- [ ] Subtitle: "Standalone Technical Lecture"
- [ ] Content does NOT duplicate existing L01 (deeper, more formal, more quantitative)
- [ ] All TikZ/pgfplots use course colors
- [ ] Compiles with pdflatex

---

### T6: Quiz Parts 1-2 -- `quiz/quiz_bf_part1.html` and `quiz/quiz_bf_part2.html` (D5a, D5b)
**Priority:** P1
**Effort:** Medium
**Depends on:** None (independent)
**Files:**
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_bf_part1.html`
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_bf_part2.html`

**HTML Template Pattern (from `quiz/quiz1.html`):**
- Exact same CSS (copy verbatim from quiz1.html, lines 10-295)
- Exact same JS logic (copy verbatim from quiz1.html, lines 337-770)
- Same nav structure: title in `.nav-title`, links to `../index.html` (Dashboard) and GitHub
- Same quiz container, header, stats, progress bar, questions-row, next button, results card
- KaTeX loaded for math rendering
- 20 questions per quiz, 4 options (A/B/C/D), correct answer + explanation

**Quiz Part 1: Block Anatomy & Hash Chains (20 questions)**
Topic coverage:
- Block structure fields (index, timestamp, transactions, prevHash, nonce, hash) -- 4 questions
- Block header vs body -- 2 questions
- Hash function properties (deterministic, one-way, collision-resistant, avalanche) -- 4 questions
- SHA-256 specifics -- 2 questions
- Hash pointers and chain linking -- 3 questions
- Genesis block -- 1 question
- Tamper detection and chain invalidation -- 2 questions
- Block size and capacity -- 2 questions

**Quiz Part 2: Merkle Trees & Data Structures (20 questions)**
Topic coverage:
- Merkle tree construction (leaf hashing, pairing, root) -- 4 questions
- SPV verification and proof paths -- 3 questions
- Verification complexity O(log n) -- 2 questions
- UTXO model -- 3 questions
- Account model (Ethereum) -- 2 questions
- Transaction structure -- 3 questions
- Patricia Merkle Trie basics -- 2 questions
- Coinbase transaction -- 1 question

**Nav title format:** "Quiz BF-1: Block Anatomy & Hash Chains" / "Quiz BF-2: Merkle Trees & Data Structures"

**Acceptance Criteria:**
- [ ] Each file has exactly 20 questions
- [ ] Each question has 4 options (A, B, C, D) with exactly 1 correct
- [ ] Each question has an `explanation` field
- [ ] HTML/CSS/JS structure matches `quiz/quiz1.html` exactly
- [ ] Nav links: Dashboard -> `../index.html`, GitHub -> repo URL
- [ ] KaTeX loaded for math rendering
- [ ] Questions use KaTeX math notation where appropriate (e.g., `$O(\log n)$`)
- [ ] No duplicate questions between Part 1 and Part 2
- [ ] No duplicate questions with existing `quiz/quiz1.html`

---

### T7: Quiz Parts 3-4 -- `quiz/quiz_bf_part3.html` and `quiz/quiz_bf_part4.html` (D5c, D5d)
**Priority:** P1
**Effort:** Medium
**Depends on:** None (independent)
**Files:**
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_bf_part3.html`
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_bf_part4.html`

**Quiz Part 3: Consensus Mechanisms (20 questions)**
Topic coverage:
- Double-spending problem -- 2 questions
- PoW mechanics (nonce, target, difficulty) -- 4 questions
- Mining economics (reward, fees, halving) -- 3 questions
- PoS mechanics (stake, validator selection) -- 4 questions
- Slashing and penalties -- 2 questions
- Nothing-at-stake problem -- 1 question
- Finality (probabilistic vs deterministic) -- 2 questions
- Difficulty adjustment algorithm -- 2 questions

**Quiz Part 4: Decentralization & Security (20 questions)**
Topic coverage:
- 51% attack mechanics and cost -- 3 questions
- Byzantine Generals Problem / BFT -- 3 questions
- Sybil attacks -- 2 questions
- Network topology (P2P, gossip protocol) -- 2 questions
- Fork types (soft fork, hard fork) -- 2 questions
- Nakamoto coefficient / decentralization metrics -- 2 questions
- Scalability trilemma -- 2 questions
- Layer 2 solutions -- 2 questions
- Quantum computing threats -- 2 questions

**Acceptance Criteria:**
- [ ] Same as T6 criteria
- [ ] No duplicate questions across all 4 quiz parts
- [ ] No duplicate questions with existing `quiz/quiz1.html`
- [ ] Nav titles: "Quiz BF-3: Consensus Mechanisms" / "Quiz BF-4: Decentralization & Security"

---

### T8: GH Pages Update -- `index.html` (D6)
**Priority:** P1
**Effort:** Low-Medium
**Depends on:** T2, T3, T4, T5, T6, T7 (needs final file paths)
**File:** `D:/Joerg/Research/slides/cryptocurrency/index.html` (MODIFY existing)

**Changes Required:**

1. **Update hero stats**: Change counts to reflect new materials
   - Quizzes: 4 -> 8 (4 existing + 4 new)
   - Add a "Lectures" stat if not present

2. **Add sidebar nav entry** under L1:
   ```html
   <a href="#standalone-lectures">Standalone Lectures</a>
   ```

3. **Add nav link** in `.nav-links`:
   ```html
   <a href="#standalone-lectures">Lectures</a>
   ```

4. **Add new section** AFTER the Lesson 4 section and BEFORE the Notebooks section. Use a new color (e.g., `#e11d48` rose or `#0ea5e9` sky blue) for the standalone lectures section.

   **Section structure:**
   ```
   Standalone Lectures (section header with badge count)

   Mini-Lecture subsection:
   - Card: BF badge, "Blockchain Fundamentals", "10-slide visual introduction", links to lectures/blockchain_intro.pdf

   Technical Lecture Bundle subsection:
   - Card: INTRO badge, "BF Course Preview", "6-slide preview deck", links to lectures/blockchain_fundamentals_intro.pdf
   - Card: PRE badge, "Pre-Class Handout", "2-page discovery activities", links to lectures/blockchain_fundamentals_preclass.pdf
   - Card: 90min badge, "Blockchain Fundamentals", "50+ frame quantitative deep dive", links to lectures/blockchain_fundamentals.pdf

   Associated Quizzes subsection:
   - Card: Q-BF1, "Block Anatomy & Hash Chains", "20 questions", links to quiz/quiz_bf_part1.html
   - Card: Q-BF2, "Merkle Trees & Data Structures", "20 questions", links to quiz/quiz_bf_part2.html
   - Card: Q-BF3, "Consensus Mechanisms", "20 questions", links to quiz/quiz_bf_part3.html
   - Card: Q-BF4, "Decentralization & Security", "20 questions", links to quiz/quiz_bf_part4.html
   ```

5. **CSS additions**: New color class for standalone lectures section (`.d5` or `.standalone`), badge styles for BF/INTRO/PRE/90min

**Acceptance Criteria:**
- [ ] New "Standalone Lectures" section visible on the page
- [ ] Mini-lecture card with "BF" badge linking to `lectures/blockchain_intro.pdf`
- [ ] INTRO card linking to `lectures/blockchain_fundamentals_intro.pdf`
- [ ] PRE card linking to `lectures/blockchain_fundamentals_preclass.pdf`
- [ ] 90min card linking to `lectures/blockchain_fundamentals.pdf`
- [ ] 4 quiz cards (Q-BF1 through Q-BF4) linking to correct quiz HTML files
- [ ] All links are relative paths (no absolute URLs for local files)
- [ ] PDF links (`lectures/*.pdf`) will be broken until user compiles `.tex` files with pdflatex (see Post-Implementation section)
- [ ] Hero stats updated
- [ ] Sidebar navigation updated
- [ ] Existing sections and content unchanged
- [ ] Page renders correctly (valid HTML)

---

## 6. Commit Strategy

| Commit | Tasks | Message |
|--------|-------|---------|
| C1 | T1 | "chore: create lectures/ directory" |
| C2 | T2, T3, T4 | "feat: add blockchain mini-lecture, INTRO preview, and pre-class handout" |
| C3 | T5 | "feat: add 60-frame quantitative blockchain fundamentals lecture" |
| C4 | T6, T7 | "feat: add 4-part blockchain fundamentals quiz (80 questions)" |
| C5 | T8 | "feat: add standalone lectures section to GH Pages index" |

---

## 7. Risk Identification

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TikZ compilation errors | Medium | High | Use well-tested TikZ patterns. Avoid exotic libraries. Keep diagrams modular. |
| pgfplots data accuracy | Medium | Medium | Use approximate but defensible data points. Add footnotes citing sources. |
| Quiz question overlap with existing quiz1 | Low | Medium | Cross-reference all 20 questions in quiz1.html. Ensure no duplicates. |
| LaTeX preamble mismatch | Low | High | Copy preamble verbatim from existing L01. Add packages at the end of preamble, never modify existing commands. |
| index.html breaking existing layout | Low | High | Modify only by INSERTING new section. Never change existing sections. Test card grid responsiveness. |
| Content overlap with existing L01 | Medium | Medium | Existing L01 has 36 frames covering Python demos, block headers, and Byzantine Generals at an introductory level. New lecture must be quantitative/formal with deeper mathematics and deliberately different examples. |
| File too large for single agent | Medium | Medium | T5 is the largest task. Can be split into sub-tasks if needed: T5a (sections 1-4, ~25 frames), T5b (sections 5-8, ~25-35 frames). |

---

## 8. Verification Steps

| Step | Command/Check | Pass Criteria |
|------|---------------|---------------|
| V1 | `ls lectures/` | 4 `.tex` files present |
| V2 | `ls quiz/quiz_bf_*` | 4 `.html` files present |
| V3 | Frame count in D1 | `grep -c '\\begin{frame}' lectures/blockchain_intro.tex` = 10 |
| V4 | Frame count in D2 | `grep -c '\\begin{frame}' lectures/blockchain_fundamentals_intro.tex` = 6 |
| V5 | Frame count in D4 | `grep -c '\\begin{frame}' lectures/blockchain_fundamentals.tex` in range [50, 70] |
| V6 | Section count in D4 | `grep -c '\\section{' lectures/blockchain_fundamentals.tex` = 8 |
| V7 | TikZ count in D4 | `grep -c 'begin{tikzpicture}' lectures/blockchain_fundamentals.tex` >= 13 |
| V8 | Question count per quiz | `grep -c '"id":' quiz/quiz_bf_partN.html` = 20 for each N |
| V9 | Index.html validity | Open in browser, verify new section renders, all links work |
| V10 | No existing file changes | `git diff --name-only` shows only `index.html` as modified existing file |
| V11 | Preamble consistency | Compare first 60 lines of each new `.tex` with L01 preamble -- colors, theme, macro must match |
| V12 | Quiz HTML consistency | Compare CSS/JS structure of new quiz files with `quiz/quiz1.html` -- must be identical except question data and title |

---

## 9. Execution Notes for Implementers

### LaTeX Preamble Template (copy for beamer files)
The canonical beamer preamble lives in `D:/Joerg/Research/slides/cryptocurrency/01_blockchain_fundamentals/01_blockchain_fundamentals.tex`.

**For T2 and T3 (no code listings needed):**
Copy lines 1-59 verbatim, then append:
```latex
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, decorations.pathmorphing}
```

**For T5 (includes listings style definition for pseudocode):**
Copy lines 1-82 verbatim (this includes the `\lstdefinestyle{python}{...}` block on lines 62-82), then append:
```latex
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, chains, decorations.pathmorphing, automata}
```

**For T4 (article class -- needs its own preamble, see T4 specification):**
T4 does NOT use the beamer preamble. See the dedicated article-class preamble template in the T4 task section.

### Quiz HTML Template
`D:/Joerg/Research/slides/cryptocurrency/quiz/quiz1.html` is the canonical template. Copy the entire file, then replace:
1. `<title>` tag content
2. `.nav-title` text
3. `.quiz-title` text
4. The `quizData.questions` array (replace all 20 questions)

### TikZ Comic Strip Pattern
For stick figures and speech bubbles:
```latex
\begin{tikzpicture}
  % Stick figure
  \draw[thick] (0,0) circle (0.3); % head
  \draw[thick] (0,-0.3) -- (0,-1.2); % body
  \draw[thick] (0,-0.6) -- (-0.5,-1); % left arm
  \draw[thick] (0,-0.6) -- (0.5,-1); % right arm
  \draw[thick] (0,-1.2) -- (-0.3,-1.8); % left leg
  \draw[thick] (0,-1.2) -- (0.3,-1.8); % right leg
  % Speech bubble
  \node[draw, rounded corners, fill=mllavender4, text width=3cm, align=center] at (2, 0.5) {Speech text};
  \draw[->, thick] (1.2, 0.3) -- (0.4, 0.1);
\end{tikzpicture}
```

### pgfplots Chart Pattern
```latex
\begin{tikzpicture}
\begin{axis}[
  width=0.9\textwidth, height=5cm,
  xlabel={X Label}, ylabel={Y Label},
  grid=major, grid style={gray!30},
  title style={font=\bfseries},
  every axis label/.style={font=\small},
  tick label style={font=\tiny},
  legend style={font=\tiny, at={(0.97,0.97)}, anchor=north east}
]
\addplot[mlblue, thick, mark=*] coordinates { ... };
\end{axis}
\end{tikzpicture}
```

---

## 10. Post-Implementation: PDF Compilation

The `index.html` links point to `.pdf` files (e.g., `lectures/blockchain_intro.pdf`) but no task in this plan produces those PDFs. They must be compiled manually by the user after all `.tex` files are created.

**Compilation commands (run from the repository root):**

```bash
# Mini-lecture
cd lectures && pdflatex blockchain_intro.tex && pdflatex blockchain_intro.tex && cd ..

# INTRO preview
cd lectures && pdflatex blockchain_fundamentals_intro.tex && pdflatex blockchain_fundamentals_intro.tex && cd ..

# Pre-class handout
cd lectures && pdflatex blockchain_fundamentals_preclass.tex && pdflatex blockchain_fundamentals_preclass.tex && cd ..

# Technical lecture (run twice for cross-references)
cd lectures && pdflatex blockchain_fundamentals.tex && pdflatex blockchain_fundamentals.tex && cd ..
```

**Notes:**
- Each file is compiled twice to resolve cross-references (TOC, page numbers).
- Requires a working TeX distribution (e.g., TeX Live, MiKTeX) with `pdflatex` on PATH.
- Required packages: `tikz`, `pgfplots`, `listings`, `beamer`, `geometry`, `enumitem`, `xcolor`, `hyperref`.
- Until these commands are run, the PDF links on `index.html` will return 404.
