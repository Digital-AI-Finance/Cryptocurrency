# Plan: L14 — Introduction to Smart Contracts (Standalone Lecture)

**Revision:** 4 (fixing Lectures stat + pre-existing files)
**Status:** PENDING CRITIC REVIEW
**Created:** 2026-03-04

---

## 1. Requirements Summary

Create a **beginner-friendly introductory lecture on Smart Contracts** (zero prerequisites) as **L14**, expanding the course from 13 to 14 lessons. Distinct from L03 (Ethereum & Smart Contracts) which is technical/Solidity-heavy. L14 is conceptual with minimal code.

**Interview answers:**
- Topic: Introductory, without preknowledge
- Slot: L14 (additional, not a replacement)
- Deliverables: Full standalone set (tech + mini + preview + preclass + 4 quizzes)
- Code: Minimal — **maximum 0 code frames** (pseudocode in diagrams only, never Solidity lstlisting)
- Content: User's 3 themes split into 5 `\section{}` to match course standard (see Section 3)
- Naming: L09-L13 pattern (`smart_contracts` base)

---

## 2. Deliverables & File Names

Following L09 `dao_governance` naming exactly:

**Pre-existing files:** All 4 `.tex` files exist from a previous execution (different section structure). **OVERWRITE all 4** to match this plan's 5-section layout.

| File | Type | Size | Action |
|------|------|------|--------|
| `lectures/smart_contracts.tex` | Technical lecture | 56 frames, 5 sections | OVERWRITE |
| `lectures/smart_contracts_intro.tex` | Mini intro lecture | 10 frames | OVERWRITE |
| `lectures/smart_contracts_intro_preview.tex` | Preview slides | 6 frames | OVERWRITE |
| `lectures/smart_contracts_preclass.tex` | Preclass handout | ~200 lines | OVERWRITE |
| `quiz/quiz_sm_part1.html` | Quiz Part 1 | 20 questions |
| `quiz/quiz_sm_part2.html` | Quiz Part 2 | 20 questions |
| `quiz/quiz_sm_part3.html` | Quiz Part 3 | 20 questions |
| `quiz/quiz_sm_part4.html` | Quiz Part 4 | 20 questions |
| `index.html` | UPDATE | Add L14 section |
| `course_inventory.json` | UPDATE | Add L14 entry |

**Quiz prefix `sm`** (sc taken by stablecoins). Verified unique against: bf, cs, es, ct, df, tc, dg, sc, nf, tm, zk, l2, rw.

**Reference files to match format:**
- Technical: `lectures/dao_governance.tex` (Beamer Madrid, 8pt, 16:9, `\bottomnote{}`)
- Mini: `lectures/dao_governance_intro.tex`
- Preview: `lectures/dao_governance_intro_preview.tex`
- Preclass: `lectures/dao_governance_preclass.tex`
- Quiz: `quiz/quiz_dg_part1.html` (quoted JSON keys)

---

## 3. Technical Lecture Structure (56 frames)

The user requested 3 content themes. These map to 5 `\section{}` commands (course standard) by splitting Theme 1 and Theme 3 each into 2 sections:

- Theme 1 "Broad conceptual intro" → **Section 1** (foundations) + **Section 2** (platforms/regulation)
- Theme 2 "Business/finance" → **Section 3** (unchanged)
- Theme 3 "Technical-lite" → **Section 4** (mechanics) + **Section 5** (applications/security/summary)

### Opening (3 frames, before Section 1)
| # | Title |
|---|-------|
| 1 | Title Page (`\titlepage`) — "Introduction to Smart Contracts" |
| 2 | Lecture Roadmap (TikZ **5-box** flow matching 5 sections below) |
| 3 | Learning Objectives (Bloom's taxonomy, 6 bullets) |

### `\section{Smart Contract Foundations}` (9 frames, 4-12)
| # | Title | Content |
|---|-------|---------|
| 4 | The Vending Machine Analogy | Nick Szabo's analogy: if-then automated execution |
| 5 | History: From Szabo to Ethereum | Timeline: 1994 concept → 2009 Bitcoin Script → 2015 Ethereum |
| 6 | Defining Smart Contracts | Formal definition, key properties (deterministic, immutable, self-executing) |
| 7 | Smart Contracts vs Traditional Contracts | Side-by-side comparison table |
| 8 | How Smart Contracts Execute | Simplified flowchart: deploy → trigger → execute → update state |
| 9 | The Role of Blockchain | Why blockchain is needed: trust, immutability, transparency |
| 10 | Key Properties: Trustlessness | No intermediary needed, code-is-law concept |
| 11 | Key Properties: Immutability and Transparency | Once deployed, visible to all, cannot be altered |
| 12 | Smart Contract Equals Code Plus Blockchain | Visual equation: program + chain = smart contract |

### `\section{Platforms and Regulatory Landscape}` (8 frames, 13-20)
| # | Title | Content |
|---|-------|---------|
| 13 | Ethereum: The Pioneer Platform | Dominant ecosystem, EVM, largest developer community |
| 14 | Beyond Ethereum: Alternative Platforms | Solana (speed), Cardano (formal verification), Polkadot (interop) |
| 15 | Smart Contract Platforms Comparison | Quantitative table: TPS, fees, TVL, language |
| 16 | Legal Status of Smart Contracts | Jurisdictional differences, Ricardian contracts, enforceability |
| 17 | Regulatory Landscape | US, EU (MiCA), Asia approaches |
| 18 | Current Limitations | Scalability, oracle problem, immutability as double-edged sword |
| 19 | The Oracle Problem | How contracts access real-world data, Chainlink overview |
| 20 | Evolution and Future Directions | Layer 2, cross-chain, AI integration, formal verification |

### `\section{Smart Contracts in Business and Finance}` (17 frames, 21-37)
| # | Title | Content |
|---|-------|---------|
| 21 | Why Businesses Care About Smart Contracts | Cost reduction, speed, transparency, disintermediation |
| 22 | Supply Chain Management | Tracking provenance, automated payments on delivery |
| 23 | Supply Chain Case Study | Walmart & IBM Food Trust with results |
| 24 | Insurance: Parametric Smart Contracts | Weather-triggered auto-payouts, flight delay insurance |
| 25 | Insurance Case Study: Etherisc | Decentralized insurance protocol |
| 26 | Real Estate and Property | Tokenized property, automated escrow, fractional ownership |
| 27 | Financial Derivatives and Settlements | Automated settlement, reduced counterparty risk |
| 28 | Trade Finance and Letters of Credit | Cross-border payments, documentary credit automation |
| 29 | DAOs: Organizations as Smart Contracts | Governance, voting, treasury management via code |
| 30 | DAO Case Study: MakerDAO | Decentralized governance example |
| 31 | Healthcare: Data Sharing and Consent | Patient-controlled data access, clinical trial management |
| 32 | Digital Identity and Credentials | Self-sovereign identity, verifiable credentials |
| 33 | Gaming and Digital Assets | In-game economies, provably fair mechanics |
| 34 | Enterprise Adoption Challenges | Integration with legacy systems, privacy, scalability |
| 35 | Cost-Benefit Analysis | Quantitative comparison: traditional vs smart contract processes |
| 36 | Industry Adoption Timeline | TikZ timeline of enterprise milestones |
| 37 | The Disintermediation Thesis | Which middlemen contracts replace, which they don't |

### `\section{How Smart Contracts Work}` (8 frames, 38-45)
| # | Title | Content |
|---|-------|---------|
| 38 | Anatomy of a Smart Contract | Simplified diagram: state variables, functions, events |
| 39 | Smart Contract Lifecycle | Write → Compile → Deploy → Interact → (Upgrade?) |
| 40 | The Ethereum Virtual Machine Simplified | Conceptual EVM: global computer, bytecode execution |
| 41 | Gas: Paying for Computation | Why gas exists, gas price vs gas limit (conceptual only, no formulas) |
| 42 | Reading vs Writing: Free vs Paid | View functions free; state changes cost gas |
| 43 | Events and Logging | How contracts communicate outcomes to outside world |
| 44 | Oracles: Connecting to the Real World | Chainlink, Band Protocol — off-chain data on-chain |
| 45 | Token Standards Overview | ERC-20 (fungible), ERC-721 (NFT), ERC-1155 (multi) |

### `\section{Applications, Security, and Future}` (7 frames, 46-52)
| # | Title | Content |
|---|-------|---------|
| 46 | Decentralized Exchanges | How AMM contracts enable trustless trading (conceptual) |
| 47 | Lending Protocols | How Aave/Compound work: deposit, borrow, liquidate |
| 48 | Stablecoins as Smart Contracts | Algorithmic vs collateralized, how code maintains the peg |
| 49 | Smart Contract Security Best Practices | Audits, formal verification, bug bounties, test coverage |
| 50 | Famous Smart Contract Failures | The DAO hack (2016), Parity wallet, Wormhole bridge |
| 51 | Upgradeability Patterns | Proxy contracts, why immutability sometimes needs workarounds |
| 52 | Smart Contract Development Tools | Hardhat, Foundry, Remix, OpenZeppelin — ecosystem overview |

### Summary and Integration (4 frames, 53-56)
| # | Title | Content |
|---|-------|---------|
| 53 | Key Takeaways | 6-8 bullet summary |
| 54 | Smart Contracts: From L14 to the Course | How this intro connects to L03, L06, L07 |
| 55 | Discussion Questions | 3-4 thought-provoking questions for class |
| 56 | Further Reading and Resources | Books, websites, tools for self-study |

**Total: 3 + 9 + 8 + 17 + 8 + 7 + 4 = 56 frames, 5 `\section{}` commands**

**Code policy:** Zero `[fragile]` frames. Zero `\begin{lstlisting}` blocks. Pseudocode may appear inside TikZ nodes only (e.g., "IF payment received THEN release product"). This is the key differentiator from L03 which has 10+ Solidity code frames.

---

## 4. Mini Intro Lecture (10 frames)

`lectures/smart_contracts_intro.tex` — template: `dao_governance_intro.tex`

| # | Title |
|---|-------|
| 1 | Title Page |
| 2 | What Is a Smart Contract? |
| 3 | The Vending Machine Analogy |
| 4 | Smart Contracts vs Traditional Contracts |
| 5 | Key Platforms |
| 6 | Real-World Applications |
| 7 | How They Work Simplified |
| 8 | Security and Limitations |
| 9 | Why This Matters |
| 10 | Coming Up: The Full Lecture |

---

## 5. Preview Slides (6 frames)

`lectures/smart_contracts_intro_preview.tex` — template: `dao_governance_intro_preview.tex`

| # | Title |
|---|-------|
| 1 | Title Page |
| 2 | Lesson Overview |
| 3 | Key Concepts Preview |
| 4 | What You Will Learn |
| 5 | Pre-Class Preparation |
| 6 | Questions to Consider |

---

## 6. Preclass Handout

`lectures/smart_contracts_preclass.tex` — template: `dao_governance_preclass.tex`

4 activities:
1. Explore a Smart Contract on Etherscan (10 min, individual)
2. The Vending Machine Analogy (5 min, pairs)
3. Compare Platforms (10 min, small groups)
4. Smart Contract Use Case Design (5 min, individual)

Plus glossary of 15 key terms.

---

## 7. Quiz Structure (80 questions)

All quizzes use quoted JSON keys format. Template: `quiz/quiz_dg_part1.html`

| File | Title | Coverage |
|------|-------|----------|
| `quiz_sm_part1.html` | Smart Contract Foundations | Sections 1-2 (frames 4-20) |
| `quiz_sm_part2.html` | Smart Contracts in Business | Section 3 (frames 21-37) |
| `quiz_sm_part3.html` | How Smart Contracts Work | Sections 4-5 (frames 38-52) |
| `quiz_sm_part4.html` | Comprehensive Review | Mixed all sections |

20 questions each, 4 options (A-D), with explanations (3-5 sentences each).

---

## 8. index.html Updates (PRECISE)

### 8a. CSS (insert after line 106, after d13 rules)
```css
.section-head.d14 span{background:#d946ef}
.d14 summary{border-left:3px solid #d946ef}
```
**Color `#d946ef` (fuchsia)** — verified unique against all existing d5-d13 colors: #e11d48, #0ea5e9, #f59e0b, #10b981, #8b5cf6, #ec4899, #14b8a6, #4f46e5, #0d9488.

### 8b. Sidebar nav (insert after line 204, after ZK entries, INSIDE existing `</details>`)
```html
<a href="#sl-sm-mini">Mini-Lecture: Smart Contracts</a>
<a href="#sl-sm-intro">SM INTRO Preview</a>
<a href="#sl-sm-pre">SM Pre-Class Handout</a>
<a href="#sl-sm-main">SM Technical Lecture</a>
```

### 8c. Hero stats (line 209-210)
- Line 209: "13 Lessons" → "14 Lessons"
- Line 210 stats:
  - `13` Lessons → `14`
  - `65` Topics → `70` (Topics = total sections across all lectures; 14 × 5 = 70)
  - `52` Lectures → `56` (add 4: tech + mini + preview + preclass; hero counts all standalone files: 13×4=52, 14×4=56)
  - `56` Quizzes → `60` (add 4: SM-1 through SM-4)
  - `11` Notebooks — unchanged (L14 has no notebook)

### 8d. L14 section HTML (insert between line 858 `</div>` closing ZK quiz-grid and line 859 `</section>`)

This goes INSIDE the existing `<section class="section d5" id="standalone-lectures">` block — a new `<div class="section-head d14">` matching the L06-L13 pattern (NOT a new top-level `<section>`):

```html
<div class="section-head d14" style="margin-top:16px"><span>SM</span><h2>Standalone Lectures: Introduction to Smart Contracts</h2></div>
<div class="lec-grid">
<a href="lectures/smart_contracts_intro.pdf" class="lec-card" style="border-left-color:#d946ef" id="sl-sm-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>Smart Contracts: Visual Introduction</h3>
<p>10 frames &bull; TikZ diagrams &bull; Zero prerequisites</p></a>
<a href="lectures/smart_contracts_intro_preview.pdf" class="lec-card" style="border-left-color:#d946ef" id="sl-sm-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>Smart Contracts: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/smart_contracts_preclass.pdf" class="lec-card" style="border-left-color:#d946ef" id="sl-sm-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>Smart Contracts: Pre-Class Handout</h3>
<p>4 activities &bull; Etherscan exploration, vending machine, platform comparison</p></a>
<a href="lectures/smart_contracts.pdf" class="lec-card" style="border-left-color:#d946ef" id="sl-sm-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>Introduction to Smart Contracts</h3>
<p>56 frames &bull; Beginner-friendly, no code, heavy on diagrams</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_sm_part1.html" class="quiz-card" style="border-left-color:#d946ef">
<div class="quiz-tag">Quiz SM-1</div>
<h3>Smart Contract Foundations</h3>
<p>20 questions &bull; History, definitions, platforms, regulation</p></a>
<a href="quiz/quiz_sm_part2.html" class="quiz-card" style="border-left-color:#d946ef">
<div class="quiz-tag">Quiz SM-2</div>
<h3>Business &amp; Finance Applications</h3>
<p>20 questions &bull; Supply chain, insurance, DAOs, real estate</p></a>
<a href="quiz/quiz_sm_part3.html" class="quiz-card" style="border-left-color:#d946ef">
<div class="quiz-tag">Quiz SM-3</div>
<h3>How Smart Contracts Work</h3>
<p>20 questions &bull; EVM, gas, tokens, DEXs, security</p></a>
<a href="quiz/quiz_sm_part4.html" class="quiz-card" style="border-left-color:#d946ef">
<div class="quiz-tag">Quiz SM-4</div>
<h3>Comprehensive Review</h3>
<p>20 questions &bull; Mixed topics from all sections</p></a>
</div>
```

---

## 9. course_inventory.json Updates

Add L14 entry and update totals:
- `total_lessons`: 13 → 14
- `total_frames_technical_lectures`: 732 → 788 (+56)
- `total_frames_all`: 1113 → 1185 (+56 tech + 10 mini + 6 preview = +72)
- Quizzes: +4 files, +80 questions

---

## 10. Execution Order

| Sprint | Task | Files |
|--------|------|-------|
| 1 | Technical lecture | `smart_contracts.tex` (56 frames) |
| 2 | Mini + preview + preclass | 3 .tex files |
| 3 | 4 quiz HTML files | 80 questions |
| 4 | index.html + inventory | 2 file updates |

---

## 11. L03 vs L14 Differentiation

| Aspect | L03: Ethereum & Smart Contracts | L14: Smart Contracts Intro |
|--------|--------------------------------|---------------------------|
| Prerequisites | Assumes L01-L02 | NONE |
| Code | 10+ Solidity code frames with `[fragile]` | **Zero** code frames, zero `[fragile]` |
| Gas coverage | EIP-1559, gas estimation formulas | Conceptual: "why gas exists" (no math) |
| EVM coverage | Opcodes, stack machine, storage slots | Analogy: "global computer" diagram |
| Focus | Technical depth for developers | Conceptual breadth for all audiences |
| Business apps | Brief mention at end | 17 dedicated frames (Section 3) |

**Overlap acceptance criterion:** No frame in L14 should require understanding Solidity syntax, EVM opcodes, or gas price formulas. Where L03 and L14 cover the same topic (gas, EVM), L14 must use only analogies and diagrams — never technical specifications.

---

## 12. Acceptance Criteria

1. `smart_contracts.tex`: exactly 56 `\begin{frame}` pairs, exactly 5 `\section{}` commands (matching the 5 names in Section 3), `\bottomnote{}` on every content frame
2. `smart_contracts.tex`: **zero** `[fragile]` frames, **zero** `\begin{lstlisting}` blocks
3. `smart_contracts.tex`: Beamer Madrid 8pt 16:9, `\lstdefinelanguage{Solidity}` + `\lstset{}` in preamble (for consistency even though unused), all 7 colors defined
4. `smart_contracts.tex`: all TikZ styles non-parameterized (no `fill=#1`)
5. `smart_contracts_intro.tex`: exactly 10 frames, `\bottomnote{}` each, no Solidity lstdefinelanguage in preamble
6. `smart_contracts_intro_preview.tex`: exactly 6 frames, compact preamble (no `colortbl`, no lstdefinelanguage)
7. `smart_contracts_preclass.tex`: article class, 4 activities, 15-term glossary
8. 4 quiz HTML files: exactly 20 questions each, quoted JSON keys, 3-5 sentence explanations
9. `index.html`: d14 CSS with `#d946ef` (NOT #e11d48), L14 section INSIDE existing d5 `<section>`, hero stats correct (14/70/56/11/60). Inline `border-left-color:#d946ef` on all lec-cards required because `.lec-card` CSS defaults to d5 red.
10. `course_inventory.json`: valid JSON, L14 entry, correct totals

---

## 13. Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| 5-section count confusion | Section names are explicit; roadmap frame 2 has exactly 5 boxes |
| Color collision | `#d946ef` (fuchsia) verified unique against d5-d13 palette |
| L03 content overlap | Zero-code policy + analogy-only approach makes overlap impossible |
| TikZ compilation errors | Non-parameterized styles, `align=center` on multi-line nodes, `Stealth[length=6pt]` arrows |
| index.html placement | Goes INSIDE `<section class="section d5">`, before `</section>` on line 859 |
| Topics stat accuracy | Topics = sections across lectures: 14 lessons × 5 sections = 70 |
