# L10 Work Plan: Layer 2 Scaling Solutions Standalone Lecture Bundle

## Context

### Original Request
Create the complete L10 Layer 2 Scaling Solutions standalone lecture bundle following the exact patterns established in L04-L09 (most recently the DAOs & Governance bundle). The bundle includes a ~55-frame technical lecture, 10-frame mini-lecture, 6-frame INTRO preview, pre-class handout, 4 HTML quizzes, and GitHub Pages integration.

### Reference Files (Structural Templates)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\dao_governance.tex` -- Tech lecture template (55 frames, 5 sections, compact preamble, lines 1-52)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\dao_governance_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble, lines 1-85)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\dao_governance_intro_preview.tex` -- INTRO preview template (6 frames, compact preamble without colortbl/Solidity, lines 1-35)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\dao_governance_preclass.tex` -- Pre-class handout template (article-class, 4 activities, glossary, lines 1-60)
- `D:\Joerg\Research\slides\cryptocurrency\quiz\quiz_dg_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data, Dashboard + GitHub nav only)
- `D:\Joerg\Research\slides\cryptocurrency\index.html` -- GitHub Pages (d9 DG subsection pattern at lines 650-686, sidebar links at lines 177-180, hero stats at line 186, CSS classes at lines 97-98)

### Key Patterns Extracted from Reference Files

**Tech lecture preamble (compact, single-line usepackage, lines 1-52):**
```latex
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}
```

**Color palette (EXACT RGB values -- identical across ALL lectures):**
```latex
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255,127,14}
\definecolor{mlgreen}{RGB}{44,160,44}
\definecolor{mlred}{RGB}{214,39,40}
\definecolor{mlgray}{RGB}{127,127,127}
```

**Solidity language definition colors:**
```latex
\definecolor{solkeyword}{RGB}{0,102,153}
\definecolor{solstring}{RGB}{163,21,21}
\definecolor{solcomment}{RGB}{0,128,0}
\definecolor{solnumber}{RGB}{0,128,128}
```

**Beamer theme configuration:**
```latex
\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{palette quaternary}{bg=mlpurple,fg=white}
\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{title}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamercolor{block title}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{block body}{bg=mllavender4,fg=black}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamersize{text margin left=5mm,text margin right=5mm}
```

**Mini-lecture preamble (verbose, separate usepackage lines):**
Each `\usepackage` on its own line. Includes additional colors `lightgray` and `midgray`. Uses `\usetikzlibrary{arrows.meta, positioning, shapes.geometric, shapes.symbols, calc, decorations.pathmorphing, mindmap}`.

**INTRO preamble (compact, no colortbl, no Solidity):**
Single-line usepackage WITHOUT `colortbl`. No Solidity `\lstdefinelanguage`. Minimal TikZ: `arrows.meta,positioning,shapes.geometric,calc`.

**Pre-class preamble (article-class, HTML colors):**
`\documentclass[11pt,a4paper]{article}`. Colors use `\definecolor{...}{HTML}{...}` format. Includes `\activitybox` and `\fillcell` commands.

**Quiz HTML:**
KaTeX 0.16.9. CSS variables with `--quiz-accent: #8b5cf6`. 3-column grid. Nav has Dashboard + GitHub links ONLY (NO prev/next inter-quiz nav).

**index.html current state (AFTER L09 integration):**
- Hero stats: 36 Lectures, 40 Quizzes (line 186)
- CSS classes defined: d1-d9 (lines 41-98)
- Sidebar: DG entries at lines 177-180, followed by `</details>` at line 181
- DG subsection: lines 650-686, followed by `</section>` at line 687
- D10 CSS does NOT yet exist -- must be added after d9 (line 98)
- L2 sidebar links do NOT yet exist -- must be added after DG entries (line 180)
- L2 subsection does NOT yet exist -- must be added after DG quiz-grid closing `</div>` (line 686), before `</section>` (line 687)

---

## Work Objectives

### Core Objective
Produce a complete, self-contained L10 Layer 2 Scaling Solutions lecture bundle that compiles without errors and integrates into the existing GitHub Pages site.

### Deliverables

| # | Deliverable | File Path | Description |
|---|-------------|-----------|-------------|
| 1 | Mini-Lecture | `lectures/layer2_scaling_intro.tex` | 10-frame TikZ comic introduction, ZERO code |
| 2 | INTRO Preview | `lectures/layer2_scaling_intro_preview.tex` | 6-frame preview with charts & roadmap |
| 3 | Pre-Class Handout | `lectures/layer2_scaling_preclass.tex` | Article-class, 4 activities, glossary |
| 4 | Technical Lecture | `lectures/layer2_scaling.tex` | ~55-frame Beamer presentation, 5 sections, light code (3-4 fragile) |
| 5 | Quiz L2-1 | `quiz/quiz_l2_part1.html` | 20 questions: Scaling Problem & L2 Fundamentals |
| 6 | Quiz L2-2 | `quiz/quiz_l2_part2.html` | 20 questions: Optimistic Rollups |
| 7 | Quiz L2-3 | `quiz/quiz_l2_part3.html` | 20 questions: Zero-Knowledge Rollups |
| 8 | Quiz L2-4 | `quiz/quiz_l2_part4.html` | 20 questions: Sidechains, Alt Scaling, L2 Ecosystem & Future |
| 9 | index.html update | `index.html` | d10 pink CSS, L2 sidebar links, hero stats (40 Lectures, 44 Quizzes), L2 subsection |

### Definition of Done
- All 4 LaTeX files compile with `pdflatex` without errors
- All 4 HTML quiz files render correctly in browser
- index.html displays L2 subsection with correct links and sidebar IDs
- Hero stats updated to 40 Lectures, 44 Quizzes
- Frame counts match: 55 tech + 10 mini + 6 intro = 71 frames total
- Exactly 4 `[fragile]` frames with code lstlisting in tech lecture (Frames ~8, ~18, ~30, ~42)
- Color palette matches L04-L09 exactly

---

## Must Have / Must NOT Have

### MUST Have
1. Exact same color palette (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray)
2. Same Beamer theme configuration as dao_governance.tex
3. Same Solidity language definition and lstset in tech lecture preamble (code frames use Solidity snippets -- L2 contracts)
4. `\bottomnote` command on every frame
5. Section divider frames with `beamercolorbox[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}`
6. Section summary frames at end of each section
7. TikZ `remember picture` where appropriate
8. `align=center` on ALL TikZ nodes that contain `\\`
9. Roadmap TikZ on Frame 2 with 5 colored boxes and Stealth arrows
10. Table of Contents on Frame 3
11. Frame comments `% Frame N: Title` for every frame
12. Section comments `%% ============================================================`

### MUST NOT Have
1. NO `\foreach` with `/` multi-variable syntax
2. NO parameterized styles with `#1` in TikZ
3. NO style names conflicting with pgf built-ins (diamond, step, text, signal)
4. NO missing `align=center` on multi-line TikZ nodes
5. NO more than 4 `[fragile]` frames
6. NO code in the mini-lecture (zero lstlisting)
7. NO breaking changes to existing index.html content/links

---

## TikZ Safety Rules (MANDATORY for all executors)

1. `\\` in TikZ nodes REQUIRES `align=center` (or `align=left`/`align=right`) -- without it, compilation crashes
2. NO `\foreach` with `/` multi-variable syntax -- use separate loops or manual placement
3. NO `#1` params in TikZ styles -- expand inline, do not define parameterized styles
4. NO reserved style names: `diamond`, `step`, `text`, `signal` -- use unique prefixes like `l2box`, `l2node`, `l2step`
5. Code frames MUST use `[fragile]` option -- every frame containing `lstlisting` environment

---

## 5-Section Topic Breakdown

### Section 1: The Scaling Problem & Layer 2 Fundamentals (Frames 4-14, 11 frames)
Blockchain trilemma (scalability, security, decentralization), why L1 can't scale (Ethereum ~15 TPS, Bitcoin ~7 TPS), gas fee spikes during congestion, L2 taxonomy overview, state channels (Lightning Network, Raiden), Plasma chains, the general concept of off-chain computation with on-chain settlement, data availability basics.

### Section 2: Optimistic Rollups (Frames 15-25, 11 frames)
How optimistic rollups work (assume valid, prove fraud), sequencer role and centralization concerns, fraud proof mechanism, challenge period (7 days typical), data posting to L1, Arbitrum architecture, Optimism (OP Stack), Base (Coinbase L2), transaction lifecycle on an optimistic rollup, fee structure (L1 data cost + L2 execution cost), comparative analysis.

### Section 3: Zero-Knowledge Rollups (Frames 26-36, 11 frames)
Zero-knowledge proof fundamentals (completeness, soundness, zero-knowledge), ZK-SNARKs vs ZK-STARKs (trusted setup, proof size, verification time), validity proofs vs fraud proofs, zkSync Era architecture, StarkNet and Cairo language, Polygon zkEVM, prover costs and hardware requirements, recursive proofs, ZK rollup transaction lifecycle, proving time tradeoffs.

### Section 4: Sidechains & Alternative Scaling (Frames 37-47, 11 frames)
Sidechains vs rollups (trust model differences), Polygon PoS architecture, Avalanche subnets and custom VMs, modular blockchain thesis (execution/settlement/consensus/data availability separation), EIP-4844 (Proto-Danksharding) and blob transactions, Celestia and modular DA, Danksharding roadmap, Validiums (off-chain DA), Volitions (user-chosen DA).

### Section 5: L2 Ecosystem & Future (Frames 48-55, 8 frames)
Bridge security and bridge hacks (Ronin $625M, Wormhole $325M, Nomad $190M), cross-L2 communication protocols, L2 economics (sequencer revenue, MEV on L2, fee compression), L3s and app-specific chains, account abstraction on L2, L2 interoperability standards, the endgame vision (rollup-centric Ethereum roadmap).

---

## Task Flow and Dependencies

```
Task 1 (Mini-Lecture)  --------\
Task 2 (INTRO Preview) --------\
Task 3 (Pre-Class)     --------+---> Task 9 (index.html) ---> Task 10 (Verification)
Task 4 (Tech Lecture)  --------/
Tasks 5-8 (Quizzes)   --------/
```

Tasks 1-8 are independent and can be executed in parallel.
Task 9 depends on all file paths being finalized.
Task 10 depends on all files existing.

---

## Detailed TODOs

### TASK 1: Mini-Lecture (`lectures/layer2_scaling_intro.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM | **Estimated frames:** 10

#### Preamble
- Copy the ENTIRE preamble from `dao_governance_intro.tex` (verbose style), changing only:
  - Title: `Layer 2 Scaling Solutions: A Visual Introduction`
  - Subtitle: `Standalone Mini-Lecture`
  - Quote text (Frame 1)
- This includes ALL verbose `\usepackage` lines (separate, not single-line)
- This includes `lightgray` and `midgray` additional colors
- This includes mini-lecture-specific beamer settings NOT in the tech lecture template:
  - `\setbeamercolor{section in toc}{fg=mlpurple}`
  - `\setbeamercolor{subsection in toc}{fg=mlblue}`
  - `\setbeamertemplate{enumerate items}[default]`
- TikZ libraries: `arrows.meta, positioning, shapes.geometric, shapes.symbols, calc, decorations.pathmorphing, mindmap`

#### Frame Specifications

**Frame 1: Title (plain)**
- `\begin{frame}[plain]` with centered title, subtitle, rule, quote, author, date
- Quote: `"Rollups are the only trustless scaling solution for Ethereum" -- Vitalik Buterin`
- Purple title, blue subtitle

**Frame 2: The Scaling Problem (TikZ Comic)**
- 3-panel comic layout (same panel dimensions as dao_governance_intro.tex):
  - Panel 1: Alice wants to swap tokens on Ethereum. Gas fee: $150! "I just wanted to trade $20 of tokens!" Shocked face, wallet showing high fees.
  - Panel 2: Bob explains: "Ethereum can only handle 15 transactions per second. When everyone wants to use it, fees go crazy!" TikZ diagram showing bottleneck -- many transactions trying to squeeze through a narrow pipe.
  - Panel 3: "What if we did most of the work somewhere else and just reported the results back?" Light bulb moment. Arrows showing transactions going to a Layer 2, then a summary going back to Ethereum L1.
- Stick figures, speech bubbles, same drawing style as DG intro

**Frame 3: The Blockchain Trilemma**
- TikZ triangle diagram:
  - Three vertices: Scalability (top), Security (bottom-left), Decentralization (bottom-right)
  - Inside triangle: "Pick any 2" label
  - Around triangle: examples of chains optimizing for different pairs
    - Security + Decentralization = Ethereum L1 (slow)
    - Scalability + Security = Centralized L2 (trusted sequencer)
    - Scalability + Decentralization = Sharded chains (complex)
- Color-coded vertices with icons

**Frame 4: What is Layer 2? (TikZ Comic)**
- 3-panel layout:
  - Panel 1: Ethereum L1 is like a busy highway. Cars (transactions) are stuck in traffic. "There's only one lane!" Toll booth (gas fees) charging high prices.
  - Panel 2: Layer 2 builds express lanes on top. Cars go fast on L2, only check in with L1 at exits. "Same destination, less traffic!" Multiple L2 lanes drawn above the highway.
  - Panel 3: Results posted back to L1 as a compressed summary. "1000 transactions, 1 proof!" L1 verifies and everyone is happy. Cost comparison: $150 on L1 vs $0.10 on L2.

**Frame 5: Types of Layer 2 Solutions**
- TikZ taxonomy tree:
  - Root: Layer 2 Solutions
  - Branch 1 (mlblue): Rollups -> Optimistic Rollups (Arbitrum, Optimism, Base) / ZK Rollups (zkSync, StarkNet, Polygon zkEVM)
  - Branch 2 (mlgreen): State Channels -> Lightning Network (Bitcoin) / Raiden (Ethereum)
  - Branch 3 (mlorange): Sidechains -> Polygon PoS / Avalanche Subnets
  - Branch 4 (mlpurple): Validiums -> StarkEx / Immutable X
- Color-coded with brief descriptions

**Frame 6: Optimistic vs ZK Rollups (TikZ Comic)**
- 3-panel comic:
  - Panel 1: Optimistic Rollup: "I'll assume everything is correct unless someone proves otherwise." Judge character sitting back relaxed. 7-day waiting period clock. "Trust but verify!"
  - Panel 2: ZK Rollup: "I'll prove everything is correct with math BEFORE submitting." Scientist character with equations. Instant finality. "Don't trust, verify with proofs!"
  - Panel 3: Side-by-side comparison box: Optimistic = cheaper to post, slower finality (7 days) / ZK = expensive to prove, instant finality. "Different tradeoffs, same goal: scale Ethereum!"

**Frame 7: How Rollups Work**
- TikZ step-by-step diagram:
  - Step 1: Users send transactions to L2 sequencer
  - Step 2: Sequencer orders and executes transactions
  - Step 3: Sequencer batches transactions together
  - Step 4: Compressed batch posted to L1 (calldata or blobs)
  - Step 5: L1 verifies (fraud proof OR validity proof)
  - Step 6: State finalized on L1
- Arrows connecting each step, color-coded for L1 vs L2 operations

**Frame 8: Bridge Security Risks**
- TikZ warning diagram with 3 panels:
  - Panel 1: Bridge concept -- lock tokens on Chain A, mint wrapped tokens on Chain B. Lock/mint arrows between two chains.
  - Panel 2: Bridge hack scenarios -- validator compromise, smart contract bug, oracle manipulation. Red warning icons.
  - Panel 3: Major hacks listed: Ronin Bridge ($625M), Wormhole ($325M), Nomad ($190M). Dollar amounts in red. Total: $1B+ lost to bridge hacks.
- Shield icon cracked down the middle

**Frame 9: The L2 Ecosystem Today**
- TikZ showcase grid (4 panels):
  - Arbitrum: $10B+ TVL, largest L2, Arbitrum One + Nova
  - Optimism: OP Stack, Superchain vision, Base built on it
  - zkSync Era: ZK rollup, native account abstraction
  - StarkNet: STARKs-based, Cairo language, provable programs
- Each with key stat, technology type, and unique feature

**Frame 10: Key Takeaways**
- TikZ numbered boxes (5 takeaways):
  1. Ethereum L1 can't scale alone -- the blockchain trilemma forces tradeoffs
  2. Layer 2 solutions execute transactions off-chain and settle on L1 for security
  3. Optimistic rollups assume validity (fraud proofs); ZK rollups prove validity (validity proofs)
  4. Bridges connect L1 and L2 but are major security risks ($1B+ hacked)
  5. The future is rollup-centric: Ethereum as settlement layer, L2s as execution layers
- Pink teaser bar at bottom

**Acceptance Criteria (Task 1):**
- [ ] Exactly 10 frames
- [ ] Zero `[fragile]` frames, zero lstlisting
- [ ] All TikZ comics use same panel style as dao_governance_intro.tex (draw, rounded corners, stick figures)
- [ ] All multi-line TikZ nodes have `align=center`
- [ ] Verbose preamble matching dao_governance_intro.tex structure
- [ ] Compiles with pdflatex without errors

---

### TASK 2: INTRO Preview (`lectures/layer2_scaling_intro_preview.tex`)
**Priority:** HIGH | **Complexity:** LOW | **Estimated frames:** 6

#### Preamble
- Compact preamble matching `dao_governance_intro_preview.tex` exactly
- Same compact style as tech lecture BUT without colortbl, without Solidity definition
- Minimal TikZ libraries: `arrows.meta,positioning,shapes.geometric,calc`
- Title: `Layer 2 Scaling Solutions: Course Preview`
- Subtitle: `INTRO Preview`

#### Frame Specifications

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Why Layer 2 Scaling Matters**
- Two-column: pgfplots bar chart (left) + Key Metrics block (right)
- Chart: Ethereum L1 TPS vs L2 TPS, gas costs L1 vs L2, TVL growth on L2s (normalized bars)
- Key metrics: $30B+ TVL across L2s, 50x cheaper transactions, 100x+ throughput improvement, 10+ major L2s live

**Frame 3: L2 Ecosystem at a Glance**
- TikZ hub diagram (same style as DG "Ecosystem at a Glance"):
  - Center: L2 Ecosystem
  - Spokes: Optimistic Rollups (Arbitrum, Optimism, Base), ZK Rollups (zkSync, StarkNet, Polygon zkEVM), Sidechains (Polygon PoS), Infrastructure (Bridges, Sequencers), Data Availability (EIP-4844, Celestia), Tools (L2Beat, Block Explorers)
- Color-coded by category

**Frame 4: L2 TVL Growth Trajectory**
- Two-column: pgfplots line chart (left) + Growth Drivers block (right)
- Chart: Total L2 TVL and number of active L2s from 2020-2025
- Growth drivers: DeFi migration to L2, EIP-4844 fee reduction, institutional adoption, gaming and NFTs on L2

**Frame 5: Course Coverage**
- TikZ 5-step process flow (same style as DG "Course Coverage"):
  - (1) Scaling Problem & Fundamentals
  - (2) Optimistic Rollups
  - (3) ZK Rollups
  - (4) Sidechains & Alt Scaling
  - (5) L2 Ecosystem & Future
- Sub-labels for each step
- Prerequisites + Outcomes blocks

**Frame 6: What You Will Learn**
- Two-column: Learning Outcomes block (left) + TikZ skill diagram (right)
- Outcomes: L2 architecture, rollup mechanics, proof systems, bridge security, L2 economics
- TikZ: central "L2 Scaling Mastery" node with 5 skill spokes

**Acceptance Criteria (Task 2):**
- [ ] Exactly 6 frames
- [ ] Compact preamble matching dao_governance_intro_preview.tex
- [ ] pgfplots charts with correct axis styling
- [ ] Compiles with pdflatex without errors

---

### TASK 3: Pre-Class Handout (`lectures/layer2_scaling_preclass.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM

#### Preamble
- Article-class matching `dao_governance_preclass.tex` exactly
- `\documentclass[11pt,a4paper]{article}`
- Same packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- Color definitions using HTML format (not RGB)
- Header: `Layer 2 Scaling Solutions | Lesson 10 | Pre-Class Discovery Handout`
- `\activitybox` and `\fillcell` commands

#### Activity 1: Explore L2 Solutions (10 min)
- Visit L2Beat.com (the canonical L2 data aggregator), answer:
  1. What is the total TVL across all Layer 2 solutions? How does it compare to Ethereum L1 DeFi TVL?
  2. List the top 3 L2s by TVL. For each, note: name, TVL, technology type (Optimistic/ZK/Other), and TPS.
  3. Pick one L2 and look at its "Risk Analysis" on L2Beat. What are the trust assumptions? Is the sequencer centralized?
  4. Compare the average transaction fee on Ethereum L1 vs your chosen L2. What is the cost ratio?
- Bonus: Find an L2 that has a "Stage 2" designation on L2Beat. What does Stage 2 mean for security?
- Fill-in table: L2 Name | TVL ($) | Type | Avg Fee ($) | Stage

#### Activity 2: Rollup Comparison (10 min)
- Compare Optimistic Rollups and ZK Rollups across key dimensions:
  1. How does an Optimistic Rollup handle an invalid transaction? How long does the challenge period last?
  2. How does a ZK Rollup handle an invalid transaction? What is the role of the prover?
  3. Which type has faster finality? Why?
  4. Which type is cheaper to operate? Why?
- Fill-in table: Dimension | Optimistic Rollup | ZK Rollup
  - Rows: Proof Type, Finality Time, Computation Cost, EVM Compatibility, Major Examples, Trust Assumption

#### Activity 3: Bridge Security Analysis (5 min)
- Research major bridge hacks and analyze the security implications:
  1. Find the Ronin Bridge hack (March 2022). How much was stolen? What was the root cause?
  2. Find the Wormhole hack (February 2022). What vulnerability was exploited?
  3. Calculate the total value lost across the top 5 bridge hacks. What percentage of total L2 TVL does this represent?
  4. What is the difference between a "trusted bridge" and a "trustless bridge"? Which is more secure and why?
- Fill-in: Total Bridge Losses: $___ | Largest Single Hack: $___ | Root Cause Pattern: ___

#### Activity 4: L2 Fee Analysis (5 min)
- Compare transaction costs across L1 and L2:
  1. Go to l2fees.info. Compare the cost of a simple ETH transfer on: Ethereum L1, Arbitrum, Optimism, zkSync Era, and Base.
  2. How did EIP-4844 (March 2024) change L2 fees? What are "blobs" and why do they matter?
  3. If a user makes 10 transactions per day, calculate the monthly cost savings of using an L2 vs L1.
  4. Where does the L2 sequencer earn revenue? How does the fee get split between L1 data cost and L2 execution cost?
- Fill-in table: Chain | ETH Transfer ($) | Token Swap ($) | Monthly Cost (10 tx/day)

#### Glossary (14 terms)

| Term | Definition |
|------|-----------|
| **Layer 2 (L2)** | A scaling solution built on top of a Layer 1 blockchain (like Ethereum) that processes transactions off-chain while inheriting the security of the underlying L1 through proofs or fraud challenges. |
| **Rollup** | A Layer 2 scaling technique that executes transactions off-chain, then posts compressed transaction data to L1, allowing anyone to verify correctness. The two main types are optimistic and zero-knowledge rollups. |
| **Optimistic Rollup** | A rollup that assumes all transactions are valid by default and only checks them if someone submits a fraud proof during the challenge period (typically 7 days). Examples: Arbitrum, Optimism, Base. |
| **Zero-Knowledge Rollup (ZK Rollup)** | A rollup that generates a cryptographic validity proof (ZK-SNARK or ZK-STARK) for every batch of transactions, providing instant mathematical certainty of correctness without a challenge period. |
| **Fraud Proof** | A mechanism used in optimistic rollups where a verifier can challenge an invalid state transition by submitting proof of fraud to the L1 contract, triggering re-execution and correction. |
| **Validity Proof** | A cryptographic proof (ZK-SNARK or ZK-STARK) submitted by a ZK rollup prover that mathematically guarantees a batch of transactions was executed correctly, without revealing the underlying data. |
| **Sequencer** | The entity (often a single operator in current L2 designs) responsible for ordering transactions, executing them, and submitting batches to L1. Sequencer centralization is a key trust assumption in most current L2s. |
| **State Channel** | A Layer 2 technique where participants open a channel on-chain, conduct many off-chain transactions between themselves, and settle the final state on-chain. Best for repeated interactions between fixed parties (e.g., Lightning Network). |
| **Sidechain** | An independent blockchain with its own consensus mechanism that connects to a main chain via a bridge. Unlike rollups, sidechains do NOT inherit L1 security -- they have their own validator set. Example: Polygon PoS. |
| **Bridge** | A protocol that enables asset transfers between different blockchains or between L1 and L2. Bridges lock assets on the source chain and mint equivalent tokens on the destination chain. They are a major attack vector ($1B+ stolen). |
| **Data Availability (DA)** | The guarantee that transaction data is published and accessible so that anyone can independently verify the L2 state. Without DA, users cannot reconstruct the L2 state or challenge invalid transitions. |
| **Blob (EIP-4844)** | A new transaction type introduced in Ethereum's Dencun upgrade (March 2024) that provides cheap temporary data storage for rollups. Blobs are pruned after ~18 days, reducing L2 costs by 10-100x compared to calldata. |
| **ZK-SNARK** | Zero-Knowledge Succinct Non-Interactive Argument of Knowledge. A proof system producing small, fast-to-verify proofs but requiring a trusted setup ceremony. Used by zkSync and Polygon zkEVM. |
| **ZK-STARK** | Zero-Knowledge Scalable Transparent Argument of Knowledge. A proof system with no trusted setup, larger proofs but quantum-resistant and transparent. Used by StarkNet and StarkEx. |

**Acceptance Criteria (Task 3):**
- [ ] Article-class preamble matches dao_governance_preclass.tex
- [ ] 4 activities with `\activitybox` command
- [ ] Glossary with 14 terms in tabular format
- [ ] Header says "Lesson 10"
- [ ] Fill-in tables with `\fillcell`
- [ ] Compiles with pdflatex without errors

---

### TASK 4: Technical Lecture (`lectures/layer2_scaling.tex`)
**Priority:** HIGH | **Complexity:** HIGH | **Estimated frames:** 55

#### Preamble (copy from dao_governance.tex exactly)
- Compact single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- All color definitions (mlblue through mlgray + solkeyword/string/comment/number)
- Beamer theme colors, navigation symbols, itemize, margins
- `\bottomnote` command
- Solidity language definition and `\lstset`
- TikZ/pgfplots with `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `Layer 2 Scaling Solutions: Scaling Ethereum and Beyond`
- Subtitle: `Standalone Technical Lecture`

#### OPENING (Frames 1-3)

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ roadmap with 5 boxes (same style as DG roadmap):
  - Box 1 (mlblue): `1. Scaling Problem\\\& L2 Fundamentals`
  - Box 2 (mlgreen): `2. Optimistic\\Rollups`
  - Box 3 (mlorange): `3. Zero-Knowledge\\Rollups`
  - Box 4 (mlred): `4. Sidechains \&\\Alt Scaling`
  - Box 5 (mlpurple): `5. L2 Ecosystem\\\& Future`
- ALL boxes MUST have `align=center` since they contain `\\`
- Stealth arrows connecting boxes
- Two-column: Learning Objectives + Prerequisites
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--5}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections covering the scaling problem to the L2 ecosystem and future}`

#### SECTION 1: The Scaling Problem & Layer 2 Fundamentals (Frames 4-14)

**Frame 4: Section 1 Divider**
- `beamercolorbox` with palette quaternary
- Title: `Section 1: The Scaling Problem \& Layer 2 Fundamentals`
- Subtitle: `Why blockchains can't scale natively and how Layer 2 solves it`
- Two-column: What You Will Learn + Frames in This Section
- Learning items:
  - The blockchain trilemma and its implications for scalability
  - Why Ethereum L1 is limited to ~15 TPS
  - Layer 2 taxonomy: rollups, state channels, sidechains, validiums
  - State channels, Plasma, and early L2 approaches

**Frame 5: The Blockchain Trilemma**
- TikZ equilateral triangle diagram:
  - Three vertices with colored circles: Scalability (mlblue, top), Security (mlred, bottom-left), Decentralization (mlgreen, bottom-right)
  - Each edge labeled with the tradeoff when you pick the two endpoints
  - Center: "Pick any two" label
  - Examples positioned near edges: Bitcoin/Ethereum (secure + decentralized, not scalable), Solana (scalable + secure, less decentralized), some L2s (scalable + decentralized, dependent on L1 security)
- `\bottomnote{Vitalik Buterin formalized the trilemma -- Layer 2 solutions aim to break it by separating execution from consensus}`

**Frame 6: Ethereum's Scaling Bottleneck**
- Two-column:
  - Left: Block explaining the bottleneck
    - Ethereum processes ~15 TPS (transactions per second)
    - Block gas limit: 30M gas, target 15M
    - Simple transfer: 21,000 gas, swap: ~150,000 gas
    - At peak demand: gas prices spike to 100+ gwei ($50-$500 per transaction)
  - Right: pgfplots chart showing Ethereum gas prices over time (2020-2025), with spikes during NFT mints, DeFi summer, token launches
- `\bottomnote{At 15 TPS, Ethereum can serve roughly 1.3 million transactions per day -- Visa processes 150 million}`

**Frame 7: L2 Taxonomy Overview**
- TikZ taxonomy diagram (tree layout):
  - Root: Off-Chain Scaling Solutions
  - Branch 1: Rollups (inherit L1 security)
    - Optimistic Rollups (fraud proofs)
    - ZK Rollups (validity proofs)
  - Branch 2: State Channels (fixed participant set)
    - Payment Channels (Lightning)
    - State Channels (Raiden)
  - Branch 3: Sidechains (own consensus)
    - Polygon PoS
    - Avalanche Subnets
  - Branch 4: Validiums (off-chain DA)
    - StarkEx
    - Immutable X
  - Branch 5: Plasma (merkle tree commitments, mostly deprecated)
- Color-coded branches, trust model annotation on each

**Frame 8: State Channel Contract [FRAGILE] -- CODE FRAME 1**
- `\begin{frame}[fragile]{State Channel Contract}`
- Left column: Solidity snippet for a simplified payment channel
```solidity
// Simple Payment Channel
contract PaymentChannel {
    address public sender;
    address public recipient;
    uint256 public expiration;

    constructor(address _to,
                uint256 duration)
        payable {
        sender = msg.sender;
        recipient = _to;
        expiration = block.timestamp
            + duration;
    }

    function close(uint256 amount,
                   bytes memory sig)
        external {
        require(msg.sender == recipient);
        require(verify(amount, sig));
        payable(recipient).transfer(
            amount);
        selfdestruct(
            payable(sender));
    }
}
```
- Right column: explanation of state channels -- open channel with deposit, exchange signed messages off-chain, close channel with final state, dispute resolution via timeout
- `\bottomnote{State channels are ideal for repeated payments between two parties -- e.g., micropayments, gaming moves}`

**Frame 9: State Channels Deep Dive**
- TikZ step-by-step flow:
  - Step 1: Alice deposits 1 ETH into channel contract
  - Step 2: Alice signs message: "Bob gets 0.1 ETH" (off-chain)
  - Step 3: Alice signs message: "Bob gets 0.3 ETH" (off-chain, replaces previous)
  - Step 4: After 100 messages, Bob submits final state to close channel
  - Step 5: Contract verifies signature and distributes funds
- Annotations: only 2 on-chain transactions (open + close), unlimited off-chain transactions
- Lightning Network stats: 5,000+ BTC capacity, ~16,000 nodes

**Frame 10: Plasma Chains**
- Two-column:
  - Left: Plasma architecture explanation
    - Child chains submit merkle roots to L1
    - Users can exit with merkle proof
    - Mass exit problem: if operator is malicious, all users must exit simultaneously
    - Data availability problem: operator can withhold data
  - Right: TikZ diagram showing Plasma chain structure:
    - L1 root chain at top
    - Plasma child chain below with blocks
    - Merkle root commitments flowing up
    - Exit arrows with challenge period
- Why Plasma was mostly abandoned in favor of rollups
- `\bottomnote{Plasma was Ethereum's first L2 scaling proposal (2017) but was superseded by rollups which solve the data availability problem}`

**Frame 11: Rollups vs Other L2 Approaches**
- TikZ comparison matrix (styled as a table with colored headers):
  - Rows: Rollups, State Channels, Sidechains, Validiums, Plasma
  - Columns: Security Model, Data Availability, Generality, Finality, Current Status
  - Color-coded cells: green = strong, yellow = moderate, red = weak
- Key insight: rollups offer the best combination of security and generality
- `\bottomnote{Rollups are the dominant L2 paradigm because they inherit L1 security while supporting general-purpose computation}`

**Frame 12: How Rollups Work (General)**
- TikZ detailed flow diagram:
  - Users submit transactions to L2 sequencer
  - Sequencer executes and orders transactions
  - Sequencer compresses transaction batch
  - Batch data posted to L1 (calldata or blobs)
  - Proof posted to L1 (fraud proof OR validity proof)
  - L1 contract verifies and updates state root
- Two verification paths shown:
  - Optimistic: "Assume valid, challenge if fraud" (7-day window)
  - ZK: "Prove valid with math" (instant verification)
- L1 and L2 clearly delineated with dashed boundary

**Frame 13: Data Compression in Rollups**
- Two-column:
  - Left: How rollups compress data
    - Full L1 transaction: ~110 bytes (signature, nonce, gas, etc.)
    - Rollup compressed: ~12 bytes (address deltas, amount, etc.)
    - Compression ratio: ~10x
    - Signature aggregation: BLS signatures or validity proofs eliminate per-tx signatures
  - Right: TikZ visualization: 1000 L1 transactions stacked tall vs compressed rollup batch as small rectangle
- Cost savings calculation: 1000 txs on L1 = $50,000 vs rollup batch = $500
- `\bottomnote{Data compression is the key economic advantage of rollups -- less data on L1 means lower costs per transaction}`

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 key takeaways, numbered, colored backgrounds)
  1. The blockchain trilemma forces tradeoffs between scalability, security, and decentralization
  2. Ethereum L1 is limited to ~15 TPS; peak demand creates $50-$500 gas fees
  3. Layer 2 solutions process transactions off-chain and settle on L1 for security
  4. Rollups are the dominant L2 paradigm, offering L1 security with 10-100x cost reduction
  5. State channels work for fixed parties; Plasma was abandoned due to data availability issues

#### SECTION 2: Optimistic Rollups (Frames 15-25)

**Frame 15: Section 2 Divider**
- Title: `Section 2: Optimistic Rollups`
- Subtitle: `Fraud proofs, challenge periods, and the optimistic approach to scaling`
- Learning items:
  - How optimistic rollups assume validity and verify via fraud proofs
  - Sequencer role, centralization risks, and decentralization roadmaps
  - Challenge period mechanics and dispute resolution
  - Arbitrum, Optimism, and Base architecture comparisons

**Frame 16: Optimistic Rollup Architecture**
- TikZ layered architecture diagram:
  - Layer 1 (bottom): Ethereum L1 -- rollup contract, state roots, data availability
  - Layer 2 (middle): Execution -- sequencer, transaction ordering, state computation
  - Layer 3 (top): User-facing -- wallets, dApps, bridges
  - Between L1 and L2: batch submission (compressed data), state root updates, fraud proof submission
  - Verifier nodes watching for fraud
- Color-coded layers with arrows showing data flow
- `\bottomnote{Optimistic rollups "optimistically" assume all batches are valid -- anyone can challenge within the dispute window}`

**Frame 17: Fraud Proof Mechanism**
- TikZ step-by-step flow:
  - Step 1: Sequencer posts batch + state root to L1
  - Step 2: Challenge window opens (7 days)
  - Step 3a (normal): No challenge -- state finalized
  - Step 3b (dispute): Verifier detects invalid state transition
  - Step 4: Interactive fraud proof -- bisection protocol narrows down to single instruction
  - Step 5: L1 re-executes single instruction, determines fault
  - Step 6: Invalid batch reverted, malicious sequencer slashed
- Decision diamond: "Challenge submitted?" with Yes/No paths
- Bisection detail: 1 billion instructions -> ~30 rounds of bisection -> 1 instruction verified on L1

**Frame 18: Optimistic Rollup Fraud Proof [FRAGILE] -- CODE FRAME 2**
- `\begin{frame}[fragile]{Fraud Proof Challenge}`
- Left column: Solidity snippet for simplified challenge/response
```solidity
// Simplified Fraud Proof
contract OptimisticRollup {
    uint256 public challengePeriod
        = 7 days;
    mapping(bytes32 => uint256)
        public stateRoots;

    function submitBatch(
        bytes32 stateRoot,
        bytes calldata txData
    ) external onlySequencer {
        stateRoots[stateRoot] =
            block.timestamp;
        emit BatchSubmitted(
            stateRoot, txData);
    }

    function challengeBatch(
        bytes32 stateRoot,
        bytes calldata proof
    ) external {
        require(block.timestamp <
            stateRoots[stateRoot]
            + challengePeriod,
            "Challenge period over");
        require(verifyFraud(proof),
            "Invalid proof");
        delete stateRoots[stateRoot];
        // Slash sequencer bond
    }
}
```
- Right column: explanation of challenge period, sequencer bond/slash, interactive vs non-interactive fraud proofs, Arbitrum's multi-round vs Optimism's single-round approach

**Frame 19: The Sequencer Role**
- TikZ hub diagram:
  - Center: Sequencer (currently centralized in most L2s)
  - Incoming: User transactions, MEV bundles
  - Outgoing: Ordered batches to L1, receipts to users
  - Side panel: Sequencer responsibilities
    - Transaction ordering (and MEV extraction)
    - Batch compression and submission
    - State computation
    - Soft confirmations (pre-L1-finality)
- Centralization concern: single point of failure, censorship risk
- Decentralization roadmap: shared sequencing, based rollups, decentralized sequencer sets

**Frame 20: Arbitrum Deep Dive**
- Two-column:
  - Left: Arbitrum architecture
    - Arbitrum One: main chain, general purpose, ~$10B TVL
    - Arbitrum Nova: AnyTrust chain, data committee, for gaming/social
    - Arbitrum Orbit: L3 framework for app-specific chains
    - Nitro stack: WASM-based fraud proofs
    - Bold protocol: permissionless validation
  - Right: TikZ Arbitrum architecture layers:
    - User -> Sequencer -> Batch Poster -> Ethereum L1
    - Validators watching for fraud
    - Inbox/outbox message passing
- Key metrics: ~4,000 TPS capacity, $0.01-$0.10 fees

**Frame 21: Optimism & the OP Stack**
- Two-column:
  - Left: Optimism ecosystem
    - OP Mainnet: flagship chain
    - OP Stack: modular, open-source rollup framework
    - Superchain vision: network of interoperable OP chains
    - Base (Coinbase): built on OP Stack, ~$5B TVL
    - Fault proofs: recently activated on mainnet
  - Right: TikZ Superchain diagram:
    - Shared sequencer at top
    - Multiple OP chains (OP Mainnet, Base, Zora, Mode) branching below
    - Shared bridge to Ethereum L1 at bottom
    - Cross-chain messaging arrows between OP chains
- `\bottomnote{The Superchain vision aims to make all OP Stack chains interoperable -- shared bridge, shared security, shared sequencer}`

**Frame 22: Base & Coinbase L2**
- Two-column:
  - Left: Base details
    - Built on OP Stack (Optimism partnership)
    - Backed by Coinbase (400M+ users funneled in)
    - No native token -- uses ETH for gas
    - Focus: onboarding the next billion users
    - Key apps: Friend.tech, Aerodrome, on-chain social
  - Right: TikZ onboarding funnel:
    - Coinbase exchange users (top, wide)
    - Coinbase Wallet (smart wallet, gasless)
    - Base L2 (dApps, DeFi, social)
    - Ethereum L1 (settlement)
- Growth metrics: fastest L2 to reach $5B TVL

**Frame 23: Optimistic Rollup Fee Structure**
- TikZ fee breakdown diagram:
  - Total L2 fee = L1 data cost + L2 execution cost
  - L1 data cost (dominant): posting compressed batch data to Ethereum
    - Pre-EIP-4844: calldata (~16 gas/byte)
    - Post-EIP-4844: blobs (~1 gas/byte equivalent, 10-100x cheaper)
  - L2 execution cost (minor): sequencer computation fee
  - pgfplots stacked bar chart: L1 component vs L2 component, pre-4844 vs post-4844
- Revenue model: sequencer earns spread between user fees and L1 costs
- `\bottomnote{EIP-4844 (March 2024) reduced L2 data costs by 10-100x by introducing blob transactions with separate fee market}`

**Frame 24: Optimistic Rollup Comparison Table**
- Full-width comparison table (booktabs):
  - Columns: Feature, Arbitrum One, Optimism, Base
  - Rows: Technology, Fraud Proof Type, Challenge Period, TVL, TPS, Avg Fee, Native Token, Sequencer, Key Feature
  - Arbitrum: Nitro/WASM, Interactive bisection, 7 days, $10B+, ~4000, $0.02, ARB, Centralized, Orbit L3s
  - Optimism: Bedrock, Cannon fault proof, 7 days, $7B+, ~2000, $0.02, OP, Centralized, Superchain
  - Base: OP Stack, Inherits Cannon, 7 days, $5B+, ~2000, $0.01, None (ETH), Coinbase, Mass adoption
- `\bottomnote{All three share the 7-day challenge period -- this is the fundamental tradeoff of optimistic rollups: security at the cost of withdrawal delay}`

**Frame 25: Section 2 Summary**
- 5-point summary boxes
  1. Optimistic rollups assume transactions are valid and rely on fraud proofs for security
  2. The 7-day challenge period enables anyone to dispute invalid state transitions via interactive bisection
  3. Sequencers are currently centralized single operators -- decentralization is an active research area
  4. Arbitrum (largest TVL), Optimism (Superchain/OP Stack), and Base (Coinbase) lead the optimistic rollup ecosystem
  5. EIP-4844 reduced L2 fees by 10-100x by introducing blob transactions for cheaper data availability

#### SECTION 3: Zero-Knowledge Rollups (Frames 26-36)

**Frame 26: Section 3 Divider**
- Title: `Section 3: Zero-Knowledge Rollups`
- Subtitle: `Validity proofs, SNARKs vs STARKs, and the mathematical approach to scaling`
- Learning items:
  - Zero-knowledge proof fundamentals: completeness, soundness, zero-knowledge
  - ZK-SNARKs vs ZK-STARKs: tradeoffs and trust assumptions
  - zkSync Era, StarkNet, and Polygon zkEVM architectures
  - Prover costs, hardware requirements, and proving time optimization

**Frame 27: Zero-Knowledge Proof Fundamentals**
- Two-column:
  - Left: Three properties of ZK proofs
    - Completeness: if the statement is true, the verifier will be convinced
    - Soundness: if the statement is false, no prover can convince the verifier
    - Zero-Knowledge: the verifier learns nothing beyond the truth of the statement
  - Right: TikZ illustration of "Ali Baba's Cave" analogy
    - Circular cave with two paths (A and B)
    - Prover enters one path, verifier calls out which path to exit
    - If prover knows the secret door, can always exit the correct side
    - Repeated rounds make cheating probability negligible
- `\bottomnote{ZK proofs were invented by Goldwasser, Micali, and Rackoff in 1985 -- applied to blockchains starting around 2018}`

**Frame 28: ZK-SNARKs vs ZK-STARKs**
- TikZ side-by-side comparison panels:
  - ZK-SNARK panel (mlblue):
    - Succinct: small proof size (~200 bytes)
    - Non-Interactive: single message from prover to verifier
    - Requires trusted setup ceremony (toxic waste)
    - Fast verification: O(1) -- constant time
    - NOT quantum-resistant
    - Used by: zkSync, Polygon zkEVM, Zcash
  - ZK-STARK panel (mlgreen):
    - Scalable: proof size grows quasi-linearly with computation
    - Transparent: no trusted setup needed
    - Larger proofs (~100 KB)
    - Verification: O(log^2 n) -- polylogarithmic
    - Quantum-resistant (hash-based)
    - Used by: StarkNet, StarkEx
- Mathematical notation: SNARK proof size $O(1)$ vs STARK proof size $O(\log^2 n)$
- `\bottomnote{SNARKs are smaller and faster to verify; STARKs are transparent and quantum-resistant -- each has its niche}`

**Frame 29: ZK Rollup Architecture**
- TikZ layered architecture diagram:
  - Top: Users submit transactions to ZK L2
  - Middle-top: Sequencer orders and executes transactions
  - Middle: Prover generates validity proof for batch
  - Middle-bottom: Batch data + validity proof posted to L1
  - Bottom: L1 verifier contract checks proof in O(1) time
  - State root updated immediately upon proof verification
- Key difference from optimistic: NO challenge period, state is final once proof verified
- Prover hardware requirements callout: GPU/FPGA clusters, significant compute cost

**Frame 30: ZK Proof Verification Contract [FRAGILE] -- CODE FRAME 3**
- `\begin{frame}[fragile]{ZK Proof Verification}`
- Left column: Solidity verifier contract
```solidity
// Simplified ZK Verifier
contract ZKRollupVerifier {
    bytes32 public stateRoot;
    uint256 public batchNumber;

    function verifyAndUpdate(
        bytes32 newStateRoot,
        uint256[2] memory proofA,
        uint256[2][2] memory proofB,
        uint256[2] memory proofC,
        uint256[] memory publicInputs
    ) external {
        require(
            verifyProof(
                proofA, proofB, proofC,
                publicInputs
            ),
            "Invalid ZK proof"
        );
        stateRoot = newStateRoot;
        batchNumber++;
        emit StateUpdated(
            batchNumber, newStateRoot);
    }
}
```
- Right column: explanation of pairing-based verification (bn128 curve), public inputs (previous state root, new state root, batch hash), Groth16 vs PLONK proof systems, gas cost of on-chain verification (~300K gas)

**Frame 31: zkSync Era**
- Two-column:
  - Left: zkSync architecture
    - zkSync Era: general-purpose ZK rollup (live since March 2023)
    - zkEVM: EVM-compatible at bytecode level
    - Native account abstraction (every account is a smart contract)
    - LLVM compiler: Solidity/Vyper -> zkSync bytecode
    - Boojum prover: GPU-based, parallelizable
    - ZK Stack: open-source framework for custom ZK chains (Hyperchains)
  - Right: TikZ zkSync stack:
    - dApps at top
    - zkEVM execution layer
    - Boojum prover (GPU cluster)
    - Ethereum L1 at bottom with proof + data
- Key metric: sub-cent fees, 100+ TPS

**Frame 32: StarkNet & Cairo**
- Two-column:
  - Left: StarkNet details
    - STARK-based (no trusted setup, quantum-resistant)
    - Cairo: native programming language (not EVM-compatible)
    - Provable computation: any Cairo program can generate a STARK proof
    - Recursive proofs: proof of proofs for scalability
    - SHARP (Shared Prover): multiple apps share proving costs
    - Madara: Starknet sequencer framework
  - Right: TikZ StarkNet architecture:
    - Cairo programs at top
    - SHARP prover in middle
    - Recursive proof compression
    - Single proof to Ethereum L1
- Tradeoff: not EVM-compatible but more expressive provable computation

**Frame 33: Polygon zkEVM**
- Two-column:
  - Left: Polygon zkEVM approach
    - Type 2 zkEVM: EVM-equivalent at opcode level
    - Full Solidity/Vyper compatibility without code changes
    - Proof generation: ~10 minutes per batch
    - Part of Polygon 2.0 vision: unified liquidity via AggLayer
    - CDK (Chain Development Kit): framework for custom ZK L2s
  - Right: TikZ Polygon 2.0 diagram:
    - Multiple chains connected via AggLayer
    - Polygon PoS, zkEVM, Miden (STARK), and CDK chains
    - Shared bridge and liquidity layer
    - Ethereum L1 as settlement
- zkEVM types explained: Type 1 (full equivalence) -> Type 4 (high-level language compatible)

**Frame 34: Prover Economics**
- TikZ cost breakdown diagram:
  - Prover hardware costs: GPU/FPGA clusters ($10K-$100K+ investment)
  - Per-batch proving cost: electricity, hardware amortization
  - Proving time vs batch size tradeoff:
    - Small batch: fast proof, high per-tx cost
    - Large batch: slow proof, low per-tx cost
  - pgfplots chart: cost per transaction vs batch size (hyperbolic curve)
- Prover decentralization challenge: specialized hardware creates centralization
- `\bottomnote{ZK provers are computationally expensive -- this is why ZK rollups have higher operational costs but faster finality than optimistic rollups}`

**Frame 35: ZK Rollup Comparison Table**
- Full-width comparison table (booktabs):
  - Columns: Feature, zkSync Era, StarkNet, Polygon zkEVM
  - Rows: Proof System, EVM Compatibility, Language, Trusted Setup, Finality, TVL, Avg Fee, Key Innovation
  - zkSync: SNARKs (PLONK), Bytecode-level, Solidity, Yes (universal), Minutes, $1B+, $0.05, Native AA
  - StarkNet: STARKs, Not EVM (Cairo), Cairo, No, Minutes, $200M+, $0.02, Provable programs
  - Polygon: SNARKs, Opcode-level, Solidity, Yes, ~10 min, $100M+, $0.03, Full EVM equivalence

**Frame 36: Section 3 Summary**
- 5-point summary boxes
  1. ZK rollups use validity proofs to mathematically guarantee correctness -- no challenge period needed
  2. SNARKs produce small, fast-to-verify proofs but require trusted setup; STARKs are transparent and quantum-resistant
  3. zkSync Era offers native account abstraction; StarkNet uses Cairo for provable computation; Polygon zkEVM provides full EVM compatibility
  4. Prover economics create a tradeoff: expensive computation for instant finality vs cheap optimistic assumption with 7-day delay
  5. zkEVM types range from full Ethereum equivalence (Type 1) to high-level language compatibility (Type 4)

#### SECTION 4: Sidechains & Alternative Scaling (Frames 37-47)

**Frame 37: Section 4 Divider**
- Title: `Section 4: Sidechains \& Alternative Scaling`
- Subtitle: `Beyond rollups: sidechains, modular blockchains, and data availability innovations`
- Learning items:
  - Sidechains vs rollups: trust model differences
  - Polygon PoS and Avalanche subnets
  - Modular blockchain thesis and data availability separation
  - EIP-4844 (Proto-Danksharding) and blob transactions

**Frame 38: Sidechains vs Rollups**
- TikZ comparison diagram:
  - Left panel (mlred): Sidechain
    - Own consensus mechanism (own validator set)
    - Bridge to L1 (trust the bridge + validators)
    - Does NOT inherit L1 security
    - If sidechain validators collude, funds at risk
    - Examples: Polygon PoS, Gnosis Chain
  - Right panel (mlgreen): Rollup
    - No own consensus (inherits L1 security)
    - Posts data + proofs to L1
    - L1 can reconstruct full state
    - If rollup operator is malicious, users can always exit to L1
    - Examples: Arbitrum, zkSync
  - Center: Trust model arrow from "Trust L2 validators" (sidechain) to "Trust L1 + math" (rollup)
- `\bottomnote{The key distinction: rollups derive security FROM L1; sidechains have their OWN security -- a fundamental trust model difference}`

**Frame 39: Polygon PoS**
- Two-column:
  - Left: Polygon PoS architecture
    - Proof-of-Stake sidechain with ~100 validators
    - Heimdall layer: validator management, checkpointing to Ethereum
    - Bor layer: block production (EVM-compatible)
    - Checkpoints: periodic state snapshots to Ethereum L1
    - Bridge: PoS bridge for ETH/ERC-20 transfers
    - Transitioning to zkEVM (Polygon 2.0)
  - Right: TikZ Polygon PoS stack:
    - dApps at top
    - Bor (block production)
    - Heimdall (validator coordination)
    - Checkpoint to Ethereum every ~30 min
    - Ethereum L1 at bottom
- Key metrics: ~$1B TVL, 2-second block times, $0.01 fees, but trust assumptions differ from rollups

**Frame 40: Avalanche Subnets**
- Two-column:
  - Left: Avalanche architecture
    - Primary network: X-chain (assets), P-chain (platform), C-chain (contracts, EVM)
    - Subnets: custom blockchains with custom VMs and validator sets
    - Elastic subnets: dynamic validator participation
    - Warp messaging: cross-subnet communication
    - Examples: DFK Chain (gaming), Dexalot (trading), Beam (gaming)
  - Right: TikZ subnet architecture:
    - P-chain at center (validator management)
    - Multiple subnets radiating outward
    - Each subnet with custom VM (EVM, custom, WASM)
    - Warp messaging arrows between subnets
- Tradeoff: flexibility and customization vs fragmented liquidity and security
- `\bottomnote{Avalanche Subnets allow app-specific chains with custom rules -- similar to Cosmos zones or Polkadot parachains}`

**Frame 41: The Modular Blockchain Thesis**
- TikZ four-layer modular stack:
  - Layer 1: Execution (process transactions) -- L2s, app chains
  - Layer 2: Settlement (finality, dispute resolution) -- Ethereum
  - Layer 3: Consensus (ordering, agreement) -- Ethereum, shared sequencers
  - Layer 4: Data Availability (store transaction data) -- Ethereum blobs, Celestia, EigenDA
  - Monolithic chain (left): all 4 layers in one chain (Ethereum L1, Solana)
  - Modular chain (right): each layer optimized independently
- Key insight: separation of concerns allows each layer to specialize and scale independently
- `\bottomnote{The modular thesis: no single chain should do everything -- specialize each layer for maximum efficiency}`

**Frame 42: Bridge Contract [FRAGILE] -- CODE FRAME 4**
- `\begin{frame}[fragile]{Bridge Contract: Lock and Mint}`
- Left column: Solidity bridge pattern
```solidity
// L1 Bridge: Lock tokens
contract L1Bridge {
    mapping(bytes32 => bool)
        public processedDeposits;

    function deposit(
        address token,
        uint256 amount,
        address l2Recipient
    ) external {
        IERC20(token).transferFrom(
            msg.sender,
            address(this),
            amount
        );
        bytes32 depositHash =
            keccak256(abi.encode(
                token, amount,
                l2Recipient,
                block.number
            ));
        emit DepositInitiated(
            depositHash,
            token, amount,
            l2Recipient);
    }
}
```
- Right column: explanation of lock-and-mint bridge pattern, L1 locks native tokens, L2 mints wrapped representation, withdrawal requires proof (fraud proof or validity proof), bridge risks (validator compromise, smart contract bugs)

**Frame 43: EIP-4844 & Blob Transactions**
- Two-column:
  - Left: EIP-4844 (Proto-Danksharding) explained
    - New transaction type: "blob-carrying transaction"
    - Blobs: ~128 KB data chunks, separate fee market
    - Blobs are NOT accessible to EVM -- only commitment is stored
    - Blobs pruned after ~18 days (not permanent storage)
    - Separate blob fee market: blob base fee independent of execution gas
    - Impact: L2 data costs reduced 10-100x
  - Right: pgfplots before/after chart:
    - Pre-4844: L2 tx cost $0.50-$5.00 (calldata)
    - Post-4844: L2 tx cost $0.001-$0.05 (blobs)
- Timeline: Dencun upgrade, March 2024
- `\bottomnote{EIP-4844 was the single most impactful upgrade for L2 economics -- it made rollup fees nearly free by introducing blob space}`

**Frame 44: Celestia & Modular DA**
- Two-column:
  - Left: Celestia architecture
    - Purpose-built data availability layer
    - Data availability sampling (DAS): light nodes verify DA without downloading all data
    - Namespaced merkle trees: each rollup has its own namespace
    - No execution: Celestia does not execute transactions
    - Rollups can use Celestia for DA instead of Ethereum
    - Cost: significantly cheaper DA than Ethereum blobs
  - Right: TikZ modular stack with Celestia:
    - Execution: any rollup (Arbitrum, zkSync)
    - Settlement: Ethereum
    - DA: Celestia (or Ethereum blobs, or EigenDA)
    - Arrows showing data posted to Celestia, proofs to Ethereum
- Tradeoff: cheaper DA but weaker security guarantees than Ethereum DA

**Frame 45: Danksharding Roadmap**
- TikZ timeline/roadmap:
  - Phase 1 (Complete): EIP-4844 Proto-Danksharding -- 3 blob target per block (~375 KB/block)
  - Phase 2 (Planned): PeerDAS -- data availability sampling for validators
  - Phase 3 (Future): Full Danksharding -- 64+ blobs per block (~8 MB/block), DAS for all nodes
  - Each phase with estimated date, blob capacity increase, and impact on L2 costs
- Data throughput progression: 375 KB/block -> 1 MB/block -> 8 MB/block
- `\bottomnote{Full Danksharding will increase Ethereum's data throughput by 20x, further reducing L2 costs and enabling ~100,000 L2 TPS aggregate}`

**Frame 46: Validiums & Volitions**
- TikZ decision tree:
  - Root: Where to store transaction data?
  - Branch 1: On-chain (Ethereum L1/blobs) -> Rollup (highest security, moderate cost)
  - Branch 2: Off-chain (DAC or external DA) -> Validium (lower security, lowest cost)
  - Branch 3: User chooses per-tx -> Volition (flexible, user decides security/cost tradeoff)
  - Examples:
    - Validium: StarkEx (Immutable X, dYdX v3), zkPorter
    - Volition: zkSync (planned), StarkNet (planned)
- Security spectrum: Rollup (L1 DA) > Validium (committee DA) > Centralized
- `\bottomnote{Validiums trade data availability security for cost -- suitable for gaming and NFTs where individual tx values are lower}`

**Frame 47: Section 4 Summary**
- 5-point summary boxes
  1. Sidechains have their own security model; rollups inherit L1 security -- a fundamental trust difference
  2. Polygon PoS is a sidechain transitioning to ZK; Avalanche Subnets offer customizable app-specific chains
  3. The modular blockchain thesis separates execution, settlement, consensus, and data availability for specialization
  4. EIP-4844 reduced L2 costs by 10-100x via blob transactions -- the most impactful L2 upgrade to date
  5. Celestia provides dedicated DA; Validiums use off-chain DA for lower costs; Volitions let users choose per-transaction

#### SECTION 5: L2 Ecosystem & Future (Frames 48-55)

**Frame 48: Section 5 Divider**
- Title: `Section 5: L2 Ecosystem \& Future`
- Subtitle: `Bridge security, L2 economics, L3s, and the rollup-centric roadmap`
- Learning items:
  - Bridge security and major bridge hacks
  - Cross-L2 communication and interoperability
  - L2 economics: sequencer revenue, MEV, fee compression
  - L3s, account abstraction, and the Ethereum endgame

**Frame 49: Bridge Security & Major Hacks**
- TikZ timeline with major bridge hacks:
  - Ronin Bridge (March 2022): $625M -- 5-of-9 validator keys compromised (social engineering)
  - Wormhole (February 2022): $325M -- signature verification bug
  - Nomad (August 2022): $190M -- initialization bug allowed anyone to drain
  - Harmony Horizon (June 2022): $100M -- 2-of-5 multi-sig compromised
  - Total: $1.5B+ lost to bridge hacks
- TikZ defense diagram: what makes a bridge secure?
  - Trustless bridges (L1-verified proofs) vs trusted bridges (validator committees)
  - Canonical bridges (official L2 bridge) vs third-party bridges
- `\bottomnote{Bridges are the weakest link in the L2 ecosystem -- Vitalik Buterin has warned that cross-chain bridges have fundamental security limitations}`

**Frame 50: Cross-L2 Communication**
- TikZ communication flow:
  - Problem: user has funds on Arbitrum, wants to use dApp on zkSync
  - Option 1: Withdraw to L1 (7+ days for optimistic), then deposit to target L2 -- slow and expensive
  - Option 2: Third-party bridge (fast but trust assumptions) -- Across, Stargate, Hop
  - Option 3: Native interop protocols -- Superchain messaging (OP Stack), AggLayer (Polygon), Hyperlane
  - Option 4: Intent-based protocols -- user states intent, solver fulfills across chains
- Shared sequencing: multiple L2s sharing the same sequencer for atomic cross-L2 transactions
- `\bottomnote{L2 interoperability is the next frontier -- without it, the multi-L2 world fragments liquidity and user experience}`

**Frame 51: L2 Economics**
- TikZ economic flow diagram:
  - Revenue sources for L2 operators:
    - User fees (L2 execution fee + L2 margin)
    - MEV extraction (sequencer ordering priority)
    - Blob fee arbitrage (buy blob space cheap, sell to users)
  - Cost structure:
    - L1 data posting (blob fees)
    - L1 proof verification (gas for proof tx)
    - Infrastructure (sequencer, prover hardware)
    - Staff and development
  - Profit = Revenue - Costs
  - pgfplots: L2 revenue vs costs over time, showing margin compression as competition increases
- Key insight: L2 sequencer revenue has become a significant business ($100M+/year for top L2s)

**Frame 52: MEV on Layer 2**
- Two-column:
  - Left: MEV in L2 context
    - Sequencer has monopoly on tx ordering (in current centralized designs)
    - Types of L2 MEV: arbitrage, liquidations, sandwich attacks
    - L1 MEV: proposer extracts via MEV-Boost/Flashbots
    - L2 MEV: sequencer directly extracts (no PBS separation yet)
    - Fair ordering: time-based ordering (FCFS), encrypted mempools, threshold decryption
  - Right: TikZ comparison:
    - L1 MEV flow: searcher -> builder -> proposer
    - L2 MEV flow: searcher -> sequencer (directly, no builder separation)
- Decentralized sequencing: shared sequencers (Espresso, Astria) aim to separate ordering from execution

**Frame 53: L3s & App-Specific Chains**
- TikZ three-layer hierarchy:
  - L1: Ethereum (settlement + security)
  - L2: General-purpose rollups (Arbitrum, Optimism, zkSync)
  - L3: App-specific chains built on L2 (further compression, custom execution)
  - Examples:
    - Arbitrum Orbit: L3 chains settling on Arbitrum L2
    - OP Stack L3: chains built on Base or OP Mainnet
    - StarkNet Appchains: custom Cairo execution environments
  - Use cases: gaming (dedicated throughput), DeFi (custom precompiles), privacy (shielded execution)
- Cost cascade: L1 > L2 > L3 (each layer further amortizes data costs)
- `\bottomnote{L3s take the rollup concept one level further -- an L3 settles on an L2 the way an L2 settles on L1}`

**Frame 54: Account Abstraction on L2**
- Two-column:
  - Left: Account abstraction on L2
    - ERC-4337: standardized account abstraction (works on L1 and L2)
    - Native AA: zkSync Era has native AA (every account is a smart account)
    - Benefits: gasless transactions (paymasters), social recovery, session keys, batch transactions
    - L2 advantage: lower gas costs make AA features practical (on L1, AA adds ~50% gas overhead)
    - Smart wallets: Coinbase Smart Wallet, Safe{Wallet}, Biconomy
  - Right: TikZ user experience comparison:
    - Traditional: User signs tx -> pay gas in ETH -> wait for confirmation
    - With AA: User clicks button -> paymaster pays gas -> sponsor or token payment -> instant UX
- Why L2 is the ideal home for AA: low fees make the overhead negligible
- `\bottomnote{Account abstraction on L2 enables Web2-like UX -- no seed phrases, no gas management, social recovery -- the key to mass adoption}`

**Frame 55: Key Takeaways and Course Summary**
- TikZ 5-box summary (matching DG Frame 55 style):
  - Box 1 (mlblue): Scaling Fundamentals -- the blockchain trilemma forces tradeoffs; L2 solutions process off-chain and settle on L1
  - Box 2 (mlpurple): Optimistic Rollups -- assume validity, challenge with fraud proofs; 7-day finality; Arbitrum, Optimism, Base lead the ecosystem
  - Box 3 (mlgreen): ZK Rollups -- prove validity with math; instant finality; SNARKs (small proofs, trusted setup) vs STARKs (transparent, quantum-safe)
  - Box 4 (mlorange): Alternative Scaling -- sidechains have own security; modular DA (EIP-4844, Celestia); Validiums trade DA for cost
  - Box 5 (mlred): L2 Ecosystem -- bridges are the weakest link ($1.5B+ hacked); sequencer economics drive L2 business models; L3s and AA are the next frontier
- Pink teaser bar: `Next: Advanced topics in cross-chain interoperability, shared sequencing, and based rollups`

**Acceptance Criteria (Task 4):**
- [ ] Exactly 55 frames with correct numbering
- [ ] 5 sections with divider and summary frames
- [ ] Exactly 4 `[fragile]` frames with lstlisting (Frames ~8, ~18, ~30, ~42)
- [ ] Preamble matches dao_governance.tex exactly (lines 1-52)
- [ ] All TikZ multi-line nodes have `align=center`
- [ ] No `\foreach` with `/` multi-variable syntax
- [ ] No parameterized styles with `#1`
- [ ] No reserved style names (diamond, step, text, signal)
- [ ] `\bottomnote` on every frame
- [ ] Compiles with pdflatex without errors

---

### TASK 5: Quiz L2-1 (`quiz/quiz_l2_part1.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz L2-1: Scaling Problem & L2 Fundamentals`
- 20 questions covering Section 1 topics:
  - Blockchain trilemma and scalability limits (Q1-Q4)
  - Ethereum TPS, gas fees, and congestion (Q5-Q7)
  - L2 taxonomy: rollups, state channels, sidechains, validiums (Q8-Q11)
  - State channels and payment channels (Q12-Q14)
  - Plasma chains and why they were abandoned (Q15-Q16)
  - Rollup fundamentals and data compression (Q17-Q20)
- Format: A/B/C/D multiple choice with explanations
- **Nav:** Dashboard + GitHub links ONLY (NO prev/next inter-quiz navigation). Copy quiz_dg_part1.html nav pattern.
- Copy CSS/JS structure from quiz_dg_part1.html exactly
- CSS variable: `--quiz-accent: #8b5cf6` (violet, same as existing template)

**Acceptance Criteria:**
- [ ] KaTeX v0.16.9 linked
- [ ] CSS variables match template
- [ ] 3-column grid layout
- [ ] 20 questions with JSON data
- [ ] All questions have correct answer and explanation
- [ ] Renders correctly in browser

---

### TASK 6: Quiz L2-2 (`quiz/quiz_l2_part2.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz L2-2: Optimistic Rollups`
- 20 questions covering Section 2 topics:
  - Optimistic rollup architecture and assumptions (Q1-Q3)
  - Fraud proof mechanism and bisection protocol (Q4-Q7)
  - Sequencer role and centralization (Q8-Q10)
  - Arbitrum architecture and Nitro (Q11-Q13)
  - Optimism, OP Stack, and Superchain (Q14-Q16)
  - Base and mass adoption strategy (Q17-Q18)
  - Fee structure and EIP-4844 impact (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 7: Quiz L2-3 (`quiz/quiz_l2_part3.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz L2-3: Zero-Knowledge Rollups`
- 20 questions covering Section 3 topics:
  - ZK proof fundamentals: completeness, soundness, zero-knowledge (Q1-Q3)
  - ZK-SNARKs vs ZK-STARKs comparison (Q4-Q7)
  - ZK rollup architecture and validity proofs (Q8-Q10)
  - zkSync Era and native account abstraction (Q11-Q13)
  - StarkNet, Cairo, and SHARP (Q14-Q16)
  - Polygon zkEVM and zkEVM types (Q17-Q18)
  - Prover economics and hardware requirements (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 8: Quiz L2-4 (`quiz/quiz_l2_part4.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz L2-4: Sidechains, Alternative Scaling & L2 Future`
- 20 questions covering Sections 4-5 topics:
  - Sidechains vs rollups trust model (Q1-Q2)
  - Polygon PoS and Avalanche Subnets (Q3-Q5)
  - Modular blockchain thesis (Q6-Q7)
  - EIP-4844, blobs, and data availability (Q8-Q10)
  - Celestia and modular DA (Q11-Q12)
  - Validiums and Volitions (Q13-Q14)
  - Bridge security and major hacks (Q15-Q16)
  - L2 economics, MEV, and sequencer revenue (Q17-Q18)
  - L3s, account abstraction, and future (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 9: GitHub Pages Update (`index.html`)
**Priority:** HIGH | **Complexity:** LOW

#### Changes Required

**1. Add d10 CSS class (after d9 styles, line 98):**
Insert AFTER line 98 (`.d9 summary{border-left:3px solid #8b5cf6}`), BEFORE the `.lec-grid` rule (line 99):
```css
.section-head.d10 span{background:#ec4899}
.d10 summary{border-left:3px solid #ec4899}
```

**2. Add L2 sidebar links (after DG entries, before `</details>` at line 181):**
Insert AFTER line 180 (`<a href="#sl-dg-main">DG Technical Lecture</a>`), BEFORE `</details>`:
```html
<a href="#sl-l2-mini">Mini-Lecture: Layer 2 Scaling</a>
<a href="#sl-l2-intro">L2 INTRO Preview</a>
<a href="#sl-l2-pre">L2 Pre-Class Handout</a>
<a href="#sl-l2-main">L2 Technical Lecture</a>
```

**3. Update hero stats (line 186):**
- Lectures: 36 -> 40
- Quizzes: 40 -> 44

**4. Add L2 subsection (after DG quiz-grid closing `</div>` at line 686, before `</section>` at line 687):**

```html
<div class="section-head d10" style="margin-top:16px"><span>L2</span><h2>Standalone Lectures: Layer 2 Scaling Solutions</h2></div>
<div class="lec-grid">
<a href="lectures/layer2_scaling_intro.pdf" class="lec-card" id="sl-l2-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>Layer 2 Scaling: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p></a>
<a href="lectures/layer2_scaling_intro_preview.pdf" class="lec-card" id="sl-l2-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>Layer 2 Scaling: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/layer2_scaling_preclass.pdf" class="lec-card" id="sl-l2-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>Layer 2 Scaling: Pre-Class Handout</h3>
<p>4 activities &bull; L2Beat exploration, rollup comparison, bridge security</p></a>
<a href="lectures/layer2_scaling.pdf" class="lec-card" id="sl-l2-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>Layer 2 Scaling: Scaling Ethereum and Beyond</h3>
<p>~55 frames &bull; Rollups, ZK proofs, bridges, L3s</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_l2_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz L2-1</div>
<h3>Scaling Problem &amp; L2 Fundamentals</h3>
<p>20 questions &bull; Trilemma, state channels, rollup basics</p></a>
<a href="quiz/quiz_l2_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz L2-2</div>
<h3>Optimistic Rollups</h3>
<p>20 questions &bull; Fraud proofs, sequencers, Arbitrum/Optimism</p></a>
<a href="quiz/quiz_l2_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz L2-3</div>
<h3>Zero-Knowledge Rollups</h3>
<p>20 questions &bull; SNARKs, STARKs, zkSync, StarkNet</p></a>
<a href="quiz/quiz_l2_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz L2-4</div>
<h3>Sidechains, Alt Scaling &amp; L2 Future</h3>
<p>20 questions &bull; Modular DA, bridges, L3s, AA</p></a>
</div>
```

**Acceptance Criteria (Task 9):**
- [ ] d10 CSS class exists with pink #ec4899 and renders correctly
- [ ] L2 sidebar links present with correct IDs (sl-l2-mini, sl-l2-intro, sl-l2-pre, sl-l2-main)
- [ ] Hero stats show 40 Lectures, 44 Quizzes
- [ ] L2 subsection appears after DG subsection
- [ ] All href paths are correct (PDF for lectures, HTML for quizzes)
- [ ] No existing content broken

---

### TASK 10: Verification
**Priority:** CRITICAL | **Depends on:** Tasks 1-9

1. **LaTeX compilation check:**
   - `pdflatex layer2_scaling.tex` -- must compile without errors
   - `pdflatex layer2_scaling_intro.tex` -- must compile without errors
   - `pdflatex layer2_scaling_intro_preview.tex` -- must compile without errors
   - `pdflatex layer2_scaling_preclass.tex` -- must compile without errors

2. **Frame count verification:**
   - Tech lecture: grep for `\begin{frame}` -- must be 55
   - Mini-lecture: must be 10
   - INTRO preview: must be 6

3. **Code frame verification:**
   - grep for `[fragile]` in tech lecture -- must be exactly 4

4. **TikZ safety verification:**
   - grep for `\\\\` inside TikZ nodes without `align=center` -- must be zero violations
   - grep for `\foreach` with `/` syntax -- must be zero
   - grep for parameterized `#1` in styles -- must be zero
   - grep for reserved style names (diamond, step, text, signal) used as custom styles -- must be zero

5. **Quiz verification:**
   - Each quiz file has exactly 20 questions in JSON
   - All `correct` values are A, B, C, or D
   - All `explanation` fields are non-empty

6. **index.html verification:**
   - Hero stats show correct numbers (40 Lectures, 44 Quizzes)
   - L2 sidebar IDs exist and scroll correctly
   - All L2 lecture/quiz href paths are valid
   - d10 CSS class renders pink #ec4899

---

## Commit Strategy

### Commit 1: Core lecture files
```
Add L10 Layer 2 Scaling Solutions lecture bundle (4 LaTeX files)

- layer2_scaling.tex: 55-frame technical lecture (5 sections)
- layer2_scaling_intro.tex: 10-frame mini-lecture with TikZ comics
- layer2_scaling_intro_preview.tex: 6-frame INTRO preview
- layer2_scaling_preclass.tex: Pre-class handout (4 activities, glossary)
```

### Commit 2: Quiz files
```
Add L2-1 through L2-4 interactive quizzes for Layer 2 Scaling Solutions

- quiz_l2_part1.html: Scaling Problem & L2 Fundamentals (20 questions)
- quiz_l2_part2.html: Optimistic Rollups (20 questions)
- quiz_l2_part3.html: Zero-Knowledge Rollups (20 questions)
- quiz_l2_part4.html: Sidechains, Alt Scaling & L2 Future (20 questions)
```

### Commit 3: GitHub Pages integration
```
Add Layer 2 Scaling Solutions section to GitHub Pages landing page

- Add L2 subsection with d10 pink color class (#ec4899)
- Add sidebar navigation links
- Update hero stats: 40 Lectures, 44 Quizzes
```

---

## Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| TikZ compilation errors from `\\` in nodes | MANDATE `align=center` on every node containing `\\`. Verify with grep before compile. |
| `\foreach` multi-variable syntax crash | BAN `/` syntax entirely. Use separate `\foreach` loops or manual placement. |
| Parameterized style `#1` conflict | BAN `#1` in all custom TikZ styles. Use fixed styles only. |
| Style name conflict with pgf built-ins | Use unique prefixes (e.g., `l2box`, `l2node`, `l2step`) for all custom style names. Avoid: diamond, step, text, signal. |
| lstlisting in non-fragile frame | Every frame with lstlisting MUST have `[fragile]` option. Verify with grep. |
| Color mismatch with L04-L09 | Copy color definitions verbatim from dao_governance.tex, character by character. |
| Code frames use Solidity | The 4 code frames use Solidity snippets (PaymentChannel, FraudProof, ZKVerifier, Bridge). The Solidity lstdef in preamble is actively used. Ensure `language=Solidity` is set. |
| index.html regression | Only add content after DG section. Do not modify any existing HTML elements. |
| pdflatex not available | Use `pdflatex` with `-interaction=nonstopmode` for error detection. Fall back to error-log review. |
| Overly long TikZ lines causing Beamer overflow | Test with 8pt font size. Use `\scriptsize` and `\tiny` aggressively in TikZ nodes. |
| Solidity code too long for fragile frames | Keep code snippets to 15-20 lines max. Use comments to indicate omitted parts. Pseudocode simplifications acceptable. |
| Quiz accent color mismatch | The existing quiz template already uses `--quiz-accent: #8b5cf6` (violet). L2 quizzes match by default. |
| Rapidly evolving L2 landscape | Use data accurate as of late 2024/early 2025. Note approximate TVL/fee figures. Avoid overly specific stats that will date quickly. |
| ZK math complexity overwhelming students | Keep ZK explanations at intuitive/analogy level. Use Ali Baba's Cave. Reserve formal math for optional bottomnotes. |

---

## Success Criteria

| Criterion | Verification Method |
|-----------|-------------------|
| All 4 LaTeX files compile cleanly | `pdflatex -interaction=nonstopmode` returns exit 0 |
| Tech lecture has exactly 55 frames | `grep -c "\\begin{frame}" layer2_scaling.tex` = 55 |
| Mini-lecture has exactly 10 frames | `grep -c "\\begin{frame}" layer2_scaling_intro.tex` = 10 |
| INTRO has exactly 6 frames | `grep -c "\\begin{frame}" layer2_scaling_intro_preview.tex` = 6 |
| Exactly 4 fragile frames in tech lecture | `grep -c "\[fragile\]" layer2_scaling.tex` = 4 |
| 80 quiz questions total (4 x 20) | JSON question count per file = 20 |
| All quiz explanations non-empty | No `"explanation": ""` in any quiz |
| index.html hero shows 40/44 | Visual inspection of rendered page |
| L2 sidebar IDs work | Click each sidebar link, verify scroll |
| No TikZ safety violations | Automated grep checks pass |
| Color palette exact match | Diff color definitions against dao_governance.tex |
| d10 pink CSS applied correctly | Visual inspection: #ec4899 pink for L2 section |

---

## File Path Summary (All Deliverables)

```
D:\Joerg\Research\slides\cryptocurrency\
  lectures\
    layer2_scaling_intro.tex             (Task 1 - Mini-lecture, 10 frames)
    layer2_scaling_intro_preview.tex     (Task 2 - INTRO preview, 6 frames)
    layer2_scaling_preclass.tex          (Task 3 - Pre-class handout)
    layer2_scaling.tex                   (Task 4 - Tech lecture, 55 frames)
  quiz\
    quiz_l2_part1.html                   (Task 5 - Quiz L2-1, 20 questions)
    quiz_l2_part2.html                   (Task 6 - Quiz L2-2, 20 questions)
    quiz_l2_part3.html                   (Task 7 - Quiz L2-3, 20 questions)
    quiz_l2_part4.html                   (Task 8 - Quiz L2-4, 20 questions)
  index.html                             (Task 9 - GitHub Pages update)
```
