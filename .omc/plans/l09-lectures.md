# L09 Work Plan: DAOs & Governance Standalone Lecture Bundle

## Context

### Original Request
Create the complete L09 DAOs & Governance standalone lecture bundle following the exact patterns established in L04-L08 (most recently the Crypto Trading & Markets bundle). The bundle includes a ~55-frame technical lecture, 10-frame mini-lecture, 6-frame INTRO preview, pre-class handout, 4 HTML quizzes, and GitHub Pages integration.

### Reference Files (Structural Templates)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\crypto_trading_markets.tex` -- Tech lecture template (55 frames, 5 sections, compact preamble, lines 1-52)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\crypto_trading_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble, lines 1-84)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\crypto_trading_markets_intro.tex` -- INTRO preview template (6 frames, compact preamble without colortbl/Solidity, lines 1-35)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\crypto_trading_markets_preclass.tex` -- Pre-class handout template (article-class, 4 activities, glossary, lines 1-60)
- `D:\Joerg\Research\slides\cryptocurrency\quiz\quiz_ct_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data, Dashboard + GitHub nav only)
- `D:\Joerg\Research\slides\cryptocurrency\index.html` -- GitHub Pages (d8 CT subsection pattern at lines 607-643, sidebar links at lines 171-174, hero stats at line 180, CSS classes at lines 93-96)

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

**index.html current state:**
- Hero stats: 32 Lectures, 36 Quizzes (line 180)
- CSS classes defined: d1-d8 (lines 41-96)
- Sidebar: CT entries at lines 171-174, followed by `</details>` at line 175
- CT subsection: lines 607-643, followed by `</section>` at line 644
- D9 CSS does NOT yet exist -- must be added after d8 (line 96)
- DG sidebar links do NOT yet exist -- must be added after CT entries (line 174)
- DG subsection does NOT yet exist -- must be added after CT quiz-grid closing `</div>` (line 643)

---

## Work Objectives

### Core Objective
Produce a complete, self-contained L09 DAOs & Governance lecture bundle that compiles without errors and integrates into the existing GitHub Pages site.

### Deliverables

| # | Deliverable | File Path | Description |
|---|-------------|-----------|-------------|
| 1 | Mini-Lecture | `lectures/dao_governance_intro.tex` | 10-frame TikZ comic introduction, ZERO code |
| 2 | INTRO Preview | `lectures/dao_governance_intro_preview.tex` | 6-frame preview with charts & roadmap |
| 3 | Pre-Class Handout | `lectures/dao_governance_preclass.tex` | Article-class, 4 activities, glossary |
| 4 | Technical Lecture | `lectures/dao_governance.tex` | ~55-frame Beamer presentation, 5 sections, light code (3-4 fragile) |
| 5 | Quiz DG-1 | `quiz/quiz_dg_part1.html` | 20 questions: DAO Fundamentals |
| 6 | Quiz DG-2 | `quiz/quiz_dg_part2.html` | 20 questions: Voting & Governance |
| 7 | Quiz DG-3 | `quiz/quiz_dg_part3.html` | 20 questions: Treasury & Economics |
| 8 | Quiz DG-4 | `quiz/quiz_dg_part4.html` | 20 questions: Attacks/Security & Real-World DAOs |
| 9 | index.html update | `index.html` | d9 violet CSS, DG sidebar links, hero stats (36 Lectures, 40 Quizzes), DG subsection |

### Definition of Done
- All 4 LaTeX files compile with `pdflatex` without errors
- All 4 HTML quiz files render correctly in browser
- index.html displays DG subsection with correct links and sidebar IDs
- Hero stats updated to 36 Lectures, 40 Quizzes
- Frame counts match: 55 tech + 10 mini + 6 intro = 71 frames total
- Exactly 4 `[fragile]` frames with code lstlisting in tech lecture (Frames ~8, ~18, ~30, ~42)
- Color palette matches L04-L08 exactly

---

## Must Have / Must NOT Have

### MUST Have
1. Exact same color palette (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray)
2. Same Beamer theme configuration as crypto_trading_markets.tex
3. Same Solidity language definition and lstset in tech lecture preamble (code frames use Solidity snippets this time, so lstdef is actively used)
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
4. NO reserved style names: `diamond`, `step`, `text`, `signal` -- use unique prefixes like `dgbox`, `dgnode`, `dgstep`
5. Code frames MUST use `[fragile]` option -- every frame containing `lstlisting` environment

---

## 5-Section Topic Breakdown

### Section 1: DAO Fundamentals & Architecture (Frames 4-14, 11 frames)
What DAOs are, how they differ from traditional organizations, smart contract architecture, membership models (token-based, share-based, reputation-based), DAO creation frameworks (Aragon, DAOhaus, Tally), legal wrappers and entity structures.

### Section 2: Voting Mechanisms & Token Governance (Frames 15-26, 12 frames)
On-chain vs off-chain voting, quorum requirements, vote delegation, conviction voting, quadratic voting, Snapshot, Governor contracts (OpenZeppelin), timelocks, proposal lifecycle, vote weighting schemes, plutocracy concerns.

### Section 3: Treasury Management & Economics (Frames 27-38, 12 frames)
DAO treasuries and multi-sig wallets (Gnosis Safe), treasury diversification, grant programs, budgeting proposals, token economics (inflation, buybacks, staking), compensation models, streaming payments (Sablier, Superfluid), financial reporting.

### Section 4: Governance Attacks & Security (Frames 39-48, 10 frames)
Flash loan governance attacks, vote buying, bribery platforms (hidden markets), Sybil attacks on governance, proposal griefing, The DAO hack (2016), governance minimization, defensive mechanisms (timelocks, guardians, veto power), emergency shutdown patterns.

### Section 5: Real-World DAOs & Future (Frames 49-55, 7 frames)
MakerDAO and DSR governance, Uniswap governance, Aave governance, Constitution DAO, governance participation rates, DAO legal frameworks by jurisdiction (Wyoming DAO LLC, MiCA), future of decentralized governance.

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

### TASK 1: Mini-Lecture (`lectures/dao_governance_intro.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM | **Estimated frames:** 10

#### Preamble
- Copy the ENTIRE preamble from `crypto_trading_intro.tex` (verbose style), changing only:
  - Title: `DAOs \& Governance: A Visual Introduction`
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
- Quote: `"The future of organization is decentralized" -- Vitalik Buterin`
- Purple title, blue subtitle

**Frame 2: What is a DAO? (TikZ Comic)**
- 3-panel comic layout (same panel dimensions as crypto_trading_intro.tex):
  - Panel 1: Alice, Bob, and Charlie want to pool money for a project. "Let's start a company!" But who's the boss? They argue.
  - Panel 2: "What if no one is the boss?" They discover DAOs -- code runs the rules, everyone votes. Smart contract in the middle with arrows to all three.
  - Panel 3: They create a DAO! Token holders vote on proposals. Treasury managed by code. "We're all the boss now!"
- Stick figures, speech bubbles, same drawing style as CT intro

**Frame 3: Traditional Org vs DAO**
- Two-column visual:
  - Left: TikZ pyramid hierarchy (CEO -> VPs -> Managers -> Workers) labeled "Traditional"
  - Right: TikZ flat network (all nodes connected equally, smart contract at center) labeled "DAO"
- Key differences block: Hierarchy vs Flat, Borders vs Borderless, Closed vs Transparent

**Frame 4: How Voting Works (TikZ Comic)**
- 3-panel layout:
  - Panel 1: Someone proposes: "Let's fund a new DEX!" Proposal goes on-chain. Clock starts ticking.
  - Panel 2: Token holders vote: Alice (100 tokens) votes YES, Bob (50 tokens) votes NO, Charlie (200 tokens) votes YES. "300 YES vs 50 NO!"
  - Panel 3: Proposal passes! Treasury automatically sends funds. No middleman needed. Smart contract executes.

**Frame 5: Types of DAOs**
- TikZ layered diagram with 5 DAO categories:
  - Protocol DAOs (Uniswap, Aave) -- govern DeFi protocols
  - Investment DAOs (The LAO, MetaCartel) -- pool capital
  - Social DAOs (Friends With Benefits) -- community membership
  - Collector DAOs (PleasrDAO) -- collective ownership of assets
  - Service DAOs (Raid Guild) -- freelancer cooperatives
- Color-coded icons for each type

**Frame 6: The DAO Hack (TikZ Comic)**
- 3-panel comic:
  - Panel 1: 2016. The DAO raises $150M in ETH. "The future of investing!" Everyone excited.
  - Panel 2: Hacker finds a reentrancy bug. Drains $60M. "Code is law... even when it's broken." Shocked faces.
  - Panel 3: Ethereum hard forks to reverse the hack. Community splits: ETH (forked) vs ETC (original). "Should we rewrite history?" Debate bubbles.

**Frame 7: Treasury Management**
- TikZ diagram of DAO treasury:
  - Multi-sig wallet at center (3-of-5 signers)
  - Inflows: protocol fees, token sales, grants received
  - Outflows: development grants, contributor salaries, liquidity incentives
  - Color-coded flow arrows

**Frame 8: Governance Attacks**
- TikZ warning diagram:
  - Flash loan attack: Borrow tokens -> Vote -> Repay in same block
  - Vote buying: Dark markets for governance power
  - Whale domination: One holder controls outcome
  - Visual: Shield icon with warning signs

**Frame 9: Famous DAOs**
- TikZ showcase grid (4 panels):
  - MakerDAO: Manages DAI stablecoin, $8B+ TVL
  - Uniswap: DEX governance, UNI token, grant programs
  - Aave: Lending protocol, safety module, risk parameters
  - ENS DAO: Domain name governance, airdrop-to-governance model
- Each with logo placeholder, key stat, governance model summary

**Frame 10: Key Takeaways**
- TikZ numbered boxes (5 takeaways):
  1. DAOs replace hierarchies with smart contracts and token-based voting
  2. Governance mechanisms range from simple majority to quadratic and conviction voting
  3. Treasury management is critical -- multi-sig wallets and transparent budgeting
  4. Governance attacks (flash loans, vote buying) are real threats requiring defensive design
  5. DAOs are evolving from experiments to legitimate organizational structures
- Purple teaser bar at bottom

**Acceptance Criteria (Task 1):**
- [ ] Exactly 10 frames
- [ ] Zero `[fragile]` frames, zero lstlisting
- [ ] All TikZ comics use same panel style as crypto_trading_intro.tex (draw, rounded corners, stick figures)
- [ ] All multi-line TikZ nodes have `align=center`
- [ ] Verbose preamble matching crypto_trading_intro.tex structure
- [ ] Compiles with pdflatex without errors

---

### TASK 2: INTRO Preview (`lectures/dao_governance_intro_preview.tex`)
**Priority:** HIGH | **Complexity:** LOW | **Estimated frames:** 6

#### Preamble
- Compact preamble matching `crypto_trading_markets_intro.tex` exactly
- Same compact style as tech lecture BUT without colortbl, without Solidity definition
- Minimal TikZ libraries: `arrows.meta,positioning,shapes.geometric,calc`
- Title: `DAOs \& Governance: Course Preview`
- Subtitle: `INTRO Preview`

#### Frame Specifications

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Why DAOs & Governance Matter**
- Two-column: pgfplots bar chart (left) + Key Metrics block (right)
- Chart: DAO treasury size growth, number of DAOs, governance participation rates (normalized bars)
- Key metrics: $25B+ in DAO treasuries, 10,000+ DAOs created, <10% average voter turnout, 50+ governance frameworks

**Frame 3: DAO Ecosystem at a Glance**
- TikZ hub diagram (same style as CT "Ecosystem at a Glance"):
  - Center: DAO Ecosystem
  - Spokes: Protocol DAOs (Uniswap, Aave), Investment DAOs (The LAO), Social DAOs (FWB), Governance Tools (Snapshot, Tally), Treasury Tools (Gnosis Safe), Legal Wrappers (Wyoming LLC)
- Color-coded by category

**Frame 4: DAO Growth Trajectory**
- Two-column: pgfplots line chart (left) + Growth Drivers block (right)
- Chart: Number of active DAOs and total treasury value 2019-2025
- Growth drivers: DeFi explosion, token governance adoption, legal recognition, tooling maturation

**Frame 5: Course Coverage**
- TikZ 5-step process flow (same style as CT "Course Coverage"):
  - (1) DAO Fundamentals
  - (2) Voting Mechanisms
  - (3) Treasury & Economics
  - (4) Attacks & Security
  - (5) Real-World & Future
- Sub-labels for each step
- Prerequisites + Outcomes blocks

**Frame 6: What You Will Learn**
- Two-column: Learning Outcomes block (left) + TikZ skill diagram (right)
- Outcomes: DAO architecture, voting mechanisms, treasury management, attack vectors, governance best practices
- TikZ: central "DAO Governance Mastery" node with 5 skill spokes

**Acceptance Criteria (Task 2):**
- [ ] Exactly 6 frames
- [ ] Compact preamble matching crypto_trading_markets_intro.tex
- [ ] pgfplots charts with correct axis styling
- [ ] Compiles with pdflatex without errors

---

### TASK 3: Pre-Class Handout (`lectures/dao_governance_preclass.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM

#### Preamble
- Article-class matching `crypto_trading_markets_preclass.tex` exactly
- `\documentclass[11pt,a4paper]{article}`
- Same packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- Color definitions using HTML format (not RGB)
- Header: `DAOs \& Governance | Lesson 09 | Pre-Class Discovery Handout`
- `\activitybox` and `\fillcell` commands

#### Activity 1: Explore a Live DAO (10 min)
- Visit a DAO governance portal (Tally.xyz, Snapshot.org, or boardroom.io), answer:
  1. Pick a DAO (e.g., Uniswap, Aave, ENS). How many active proposals does it currently have?
  2. What is the quorum requirement? What percentage of tokens typically vote?
  3. Look at a recent passed proposal. What did it change? How many votes for vs against?
  4. Is voting on-chain or off-chain (Snapshot)? What are the gas cost implications?
- Bonus: Screenshot a proposal page and annotate the key governance parameters.

#### Activity 2: Governance Mechanism Comparison (10 min)
- Compare three voting mechanisms using examples:
  1. Simple token voting (1 token = 1 vote): What is the advantage? What is the main criticism?
  2. Quadratic voting (cost = votes^2): How does it help smaller holders? What prevents Sybil attacks?
  3. Conviction voting (votes accumulate over time): How does this differ from snapshot voting? What problem does it solve?
  4. Which mechanism would you choose for a community treasury with 10,000 members? Why?
- Fill-in table: Mechanism | Advantage | Disadvantage | Best For

#### Activity 3: Treasury Analysis (5 min)
- Visit DeepDAO.io or a DAO's treasury dashboard:
  1. What is the total treasury value of MakerDAO? What assets does it hold?
  2. How is the treasury diversified? (ETH, stablecoins, protocol tokens, real-world assets)
  3. Find a recent grant proposal. How much was requested? What was it for?
  4. Calculate: If a DAO has $100M treasury earning 5% APY, how much can it spend annually without depleting capital?
- Fill-in: Treasury Size: $___ | Largest Asset: ___ | Annual Budget: $___

#### Activity 4: Governance Attack Scenarios (5 min)
- Consider these attack scenarios and propose defenses:
  1. An attacker takes a flash loan of 1M governance tokens, votes to drain the treasury, and repays in the same block. How would you prevent this?
  2. A whale holds 40% of governance tokens and consistently votes in their own interest. What mechanism could balance their power?
  3. Someone creates 100 wallets to gain more votes in a quadratic voting system. How do you detect and prevent this?
  4. A malicious proposal passes but has a 48-hour timelock. What emergency mechanism should exist?
- Fill-in table: Attack | Defense Mechanism | Tradeoff

#### Glossary (14 terms)

| Term | Definition |
|------|-----------|
| **DAO (Decentralized Autonomous Organization)** | An organization governed by smart contracts and token holder voting rather than centralized management. Members propose and vote on decisions transparently on-chain. |
| **Governance Token** | A token that grants voting rights in a DAO's decision-making process. Holding more tokens typically means more voting power (in simple token-weighted voting). |
| **Proposal** | A formal suggestion submitted to a DAO for member voting. Proposals can modify protocol parameters, allocate treasury funds, or change governance rules. |
| **Quorum** | The minimum number of votes (or percentage of total supply) required for a governance vote to be considered valid. Prevents decisions by tiny minorities. |
| **Quadratic Voting** | A voting mechanism where the cost of additional votes increases quadratically (1 vote = 1 credit, 2 votes = 4 credits, 3 votes = 9 credits), giving smaller holders more proportional influence. |
| **Delegation** | The act of assigning one's voting power to another address (a delegate) who votes on their behalf. Enables participation without active involvement in every vote. |
| **Timelock** | A mandatory delay between when a governance proposal passes and when it is executed, giving the community time to react to potentially harmful changes. |
| **Multi-sig (Multi-signature Wallet)** | A wallet requiring M-of-N signatures to execute transactions (e.g., 3-of-5 signers must approve). Used for DAO treasury management. |
| **Snapshot Voting** | Off-chain voting using signed messages instead of on-chain transactions, eliminating gas costs. Results are typically enacted via multi-sig execution. |
| **Flash Loan Attack (Governance)** | An attack where an adversary borrows a large amount of governance tokens via flash loan, votes on a malicious proposal, and repays the loan in the same transaction. |
| **Conviction Voting** | A voting mechanism where a voter's influence on a proposal grows over time as they keep their stake committed, favoring sustained community support over flash consensus. |
| **Treasury Diversification** | The practice of holding DAO assets across multiple token types (stablecoins, ETH, protocol tokens) to reduce volatility risk and ensure operational sustainability. |
| **Ragequit** | A mechanism (popularized by Moloch DAO) allowing dissatisfied members to exit with their proportional share of the treasury before a proposal they oppose is executed. |
| **Governance Minimization** | A design philosophy advocating for reducing the scope of governance decisions over time, making protocols more autonomous and less vulnerable to governance attacks. |

**Acceptance Criteria (Task 3):**
- [ ] Article-class preamble matches crypto_trading_markets_preclass.tex
- [ ] 4 activities with `\activitybox` command
- [ ] Glossary with 14 terms in tabular format
- [ ] Header says "Lesson 09"
- [ ] Fill-in tables with `\fillcell`
- [ ] Compiles with pdflatex without errors

---

### TASK 4: Technical Lecture (`lectures/dao_governance.tex`)
**Priority:** HIGH | **Complexity:** HIGH | **Estimated frames:** 55

#### Preamble (copy from crypto_trading_markets.tex exactly)
- Compact single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- All color definitions (mlblue through mlgray + solkeyword/string/comment/number)
- Beamer theme colors, navigation symbols, itemize, margins
- `\bottomnote` command
- Solidity language definition and `\lstset`
- TikZ/pgfplots with `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `DAOs \& Governance: Decentralized Decision-Making`
- Subtitle: `Standalone Technical Lecture`

#### OPENING (Frames 1-3)

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ roadmap with 5 boxes (same style as CT roadmap):
  - Box 1 (mlblue): `1. DAO\\Fundamentals`
  - Box 2 (mlgreen): `2. Voting\\Mechanisms`
  - Box 3 (mlorange): `3. Treasury\\\& Economics`
  - Box 4 (mlred): `4. Governance\\Attacks`
  - Box 5 (mlpurple): `5. Real-World\\DAOs \& Future`
- ALL boxes MUST have `align=center` since they contain `\\`
- Stealth arrows connecting boxes
- Two-column: Learning Objectives + Prerequisites
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--5}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections covering DAO fundamentals to real-world governance and the future}`

#### SECTION 1: DAO Fundamentals & Architecture (Frames 4-14)

**Frame 4: Section 1 Divider**
- `beamercolorbox` with palette quaternary
- Title: `Section 1: DAO Fundamentals \& Architecture`
- Subtitle: `Understanding decentralized organizations and their smart contract foundations`
- Two-column: What You Will Learn + Frames in This Section
- Learning items:
  - What DAOs are and how they differ from traditional organizations
  - Smart contract architecture for DAOs
  - Membership models: token-based, share-based, reputation-based
  - DAO creation frameworks and legal wrappers

**Frame 5: What is a DAO?**
- Two-column layout
- Left: Block explaining DAO concept (organization encoded in smart contracts, no central authority, transparent and permissionless, governed by token holders)
- Right: TikZ diagram showing DAO structure: Smart Contract at center, connected to Members (token holders), Treasury, Proposals, and Execution
- Hub-and-spoke with colored categories

**Frame 6: Traditional Organizations vs DAOs**
- Full-width TikZ comparison:
  - Left panel (mlred): Traditional Corp -- Hierarchical, Board/CEO decisions, Opaque finances, Jurisdiction-bound, Slow to change
  - Right panel (mlgreen): DAO -- Flat/democratic, Token-holder voting, Transparent treasury, Borderless, Programmable rules
  - Center: Transformation arrow with "Smart Contracts" label
- `\bottomnote{DAOs aim to replace trust in people with trust in code -- but code has its own risks}`

**Frame 7: DAO Architecture Overview**
- TikZ layered architecture diagram:
  - Layer 1 (top): User Interface (Tally, Boardroom, Snapshot)
  - Layer 2: Governance Module (proposals, voting, execution)
  - Layer 3: Access Control (roles, permissions, timelocks)
  - Layer 4: Treasury (multi-sig, asset management)
  - Layer 5 (bottom): Blockchain (Ethereum, L2s, cross-chain)
- Arrows showing interaction flows

**Frame 8: Governor Contract [FRAGILE] -- CODE FRAME 1**
- `\begin{frame}[fragile]{Governor Contract}`
- Left column: Solidity snippet for a simplified Governor
```solidity
// Simplified Governor Contract
contract SimpleGovernor {
    struct Proposal {
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 deadline;
        bool executed;
    }

    mapping(uint256 => Proposal)
        public proposals;
    uint256 public proposalCount;

    function propose(string memory desc)
        external returns (uint256) {
        proposalCount++;
        proposals[proposalCount] =
            Proposal(desc, 0, 0,
            block.timestamp + 7 days,
            false);
        return proposalCount;
    }
}
```
- Right column: explanation of proposal creation, storage pattern, OpenZeppelin Governor as production standard

**Frame 9: Membership Models**
- TikZ comparison panel with 3 membership types:
  - Panel 1 (mlblue): Token-Based -- hold ERC-20 tokens, 1 token = 1 vote, freely transferable (Uniswap, Compound)
  - Panel 2 (mlgreen): Share-Based -- non-transferable shares, ragequit mechanism, member approval required (Moloch DAO)
  - Panel 3 (mlorange): Reputation-Based -- earned through contributions, non-transferable, meritocratic (DAOstack)
- Each with pros/cons bullet points

**Frame 10: Token-Based DAO Deep Dive**
- Two-column:
  - Left: Mechanics of token governance -- token distribution, whale concentration risks, governance extractable value
  - Right: TikZ pie chart showing typical governance token distribution: Team 20%, Investors 15%, Community Treasury 40%, Liquidity Mining 15%, Airdrop 10%
- Token distribution as governance power distribution

**Frame 11: DAO Creation Frameworks**
- TikZ grid of frameworks:
  - Aragon: modular, plug-and-play governance, Aragon Court for disputes
  - DAOhaus: Moloch-based, share-based, ragequit support
  - Tally: Governor-compatible, delegation UI, on-chain voting
  - Snapshot: off-chain voting, gasless, signature-based
  - Colony: reputation-based, task management, budget allocation
- Color-coded with key features listed

**Frame 12: Legal Status of DAOs**
- TikZ world map schematic with jurisdiction highlights:
  - Wyoming (USA): DAO LLC recognized since 2021
  - Marshall Islands: DAO LLC framework
  - Switzerland: Association model for DAOs
  - EU/MiCA: No specific DAO framework yet, but regulatory pressure
  - Cayman Islands: Foundation company model
- Legal wrapper concept: DAO + legal entity = limited liability + regulatory compliance
- `\bottomnote{Legal wrapping is essential for DAOs interacting with the traditional world -- contracts, bank accounts, and liability protection}`

**Frame 13: DAO Lifecycle**
- TikZ flow diagram showing DAO lifecycle:
  - Ideation -> Token Design -> Smart Contract Deployment -> Community Building -> Governance Activation -> Ongoing Operations -> Evolution/Sunset
- Feedback loop arrows from Operations back to Governance
- Time estimates for each phase

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 key takeaways, numbered, colored backgrounds)
  1. DAOs are organizations governed by smart contracts and token-holder consensus
  2. Three membership models: token-based (liquid), share-based (ragequit), reputation-based (earned)
  3. Governor contracts (OpenZeppelin) are the standard for on-chain governance
  4. Framework tools (Aragon, Tally, Snapshot) simplify DAO creation
  5. Legal wrappers (Wyoming LLC, Swiss Association) bridge DAOs to traditional law

#### SECTION 2: Voting Mechanisms & Token Governance (Frames 15-26)

**Frame 15: Section 2 Divider**
- Title: `Section 2: Voting Mechanisms \& Token Governance`
- Subtitle: `How decentralized decisions get made -- from simple voting to advanced mechanisms`
- Learning items:
  - On-chain vs off-chain voting tradeoffs
  - Token-weighted voting and its plutocracy problem
  - Advanced mechanisms: quadratic, conviction, holographic consensus
  - Delegation, timelocks, and proposal lifecycle

**Frame 16: Proposal Lifecycle**
- TikZ flow diagram with 6 stages:
  - Stage 1 (mlblue): Discussion (forum, Discord)
  - Stage 2 (mlgreen): Formal Proposal (on-chain or Snapshot)
  - Stage 3 (mlorange): Voting Period (3-7 days typical)
  - Stage 4 (mlred): Quorum Check (minimum participation)
  - Stage 5 (mlpurple): Timelock (24-48 hour delay)
  - Stage 6 (mlblue): Execution (automatic via smart contract)
- Decision diamond at Stage 4: passes quorum? Yes -> Stage 5, No -> Rejected
- Time annotations

**Frame 17: On-Chain vs Off-Chain Voting**
- TikZ comparison table:
  - On-Chain: Binding, gas costs, tamper-proof, transparent, slow
  - Off-Chain (Snapshot): Gasless, fast, flexible, requires trust for execution, signature-based
  - Hybrid: Vote off-chain, execute on-chain (optimistic governance)
- When to use each: critical parameter changes = on-chain, signaling = off-chain
- Cost comparison: typical governance vote gas cost vs free Snapshot

**Frame 18: Voting Weight Calculation [FRAGILE] -- CODE FRAME 2**
- `\begin{frame}[fragile]{Voting Weight Calculation}`
- Left column: Solidity voting weight logic
```solidity
// Voting Weight with Delegation
contract VotingPower {
    mapping(address => uint256) balances;
    mapping(address => address) delegates;

    function getVotingPower(
        address voter
    ) public view returns (uint256) {
        uint256 power = 0;
        // Direct holdings
        if (delegates[voter] == address(0))
            power += balances[voter];
        // Delegated power
        // (simplified - real impl uses
        //  checkpoints for snapshots)
        for (uint i = 0;
             i < voterList.length; i++) {
            if (delegates[voterList[i]]
                == voter) {
                power += balances[
                    voterList[i]];
            }
        }
        return power;
    }
}
```
- Right column: explanation of vote delegation, checkpoint mechanism, snapshot block, ERC20Votes

**Frame 19: Simple Token Voting**
- Two-column:
  - Left: Mechanics -- 1 token = 1 vote, majority wins, quorum threshold
  - Right: TikZ visualization showing vote distribution: Whale (40% tokens) vs many small holders (60% combined but only 20% vote)
- The plutocracy problem: wealth = governance power
- Voter apathy: typical turnout <10%

**Frame 20: Quadratic Voting**
- Two-column:
  - Left: Formula and mechanics -- cost of N votes = N^2 credits
  - Table: 1 vote = 1 credit, 2 votes = 4, 3 votes = 9, 10 votes = 100
  - Right: TikZ comparison bar chart: Token voting vs Quadratic voting outcome for same proposal
  - Shows how quadratic voting amplifies majority preference over wealthy minority
- Formula: $\text{Cost} = (\text{votes})^2$, so $\text{votes} = \sqrt{\text{credits}}$
- Sybil vulnerability discussion

**Frame 21: Conviction Voting**
- TikZ time-series diagram:
  - X-axis: Time, Y-axis: Conviction (accumulated voting power)
  - Multiple voters staking over time, conviction curves rising
  - Threshold line: when cumulative conviction exceeds threshold, proposal passes
  - Visualization of "slow consensus" -- no snapshot, continuous support required
- Key advantage: reduces governance attacks, rewards sustained commitment
- Used by: 1Hive, Gitcoin

**Frame 22: Vote Delegation**
- TikZ delegation graph:
  - Central hub: Professional Delegate (known identity, voting record)
  - Spokes: Multiple small token holders delegating to the hub
  - Metrics: delegate voting participation rate, alignment scores
  - Delegation platforms: Tally, Agora, Karma
- Why delegate? Gas costs, expertise, time constraints
- Liquid democracy concept: delegate can be changed anytime

**Frame 23: Quorum and Thresholds**
- TikZ multi-scenario visualization:
  - Scenario A: 5% quorum, vote passes with 3% participation (too low -- tiny minority decides)
  - Scenario B: 20% quorum, vote fails to reach quorum (governance gridlock)
  - Scenario C: Adaptive quorum (Compound's Bravo) -- quorum adjusts based on controversy
- Common thresholds: Uniswap 4% (~40M UNI), Compound 1%, Aave 2%
- Tradeoff: high quorum = security but gridlock risk

**Frame 24: Holographic Consensus**
- Two-column:
  - Left: The scalability problem -- every proposal requires quorum, leading to voter fatigue
  - Right: TikZ flow showing holographic consensus (DAOstack):
    - Prediction market: stakers bet on proposal outcome
    - If enough stake, proposal gets "boosted" to simple majority (no quorum needed)
    - Stakers rewarded if prediction correct
- Combines prediction markets with governance for scalability

**Frame 25: Timelocks and Execution**
- TikZ timeline showing timelock mechanism:
  - Proposal passes vote (T=0)
  - Timelock period begins (e.g., 48 hours)
  - Community can review and react
  - Emergency guardian can veto during timelock
  - Execution (T=48h) -- proposal enacted on-chain
- OpenZeppelin TimelockController reference
- Why timelocks matter: protection against governance attacks, allow exit before harmful changes

**Frame 26: Section 2 Summary**
- 5-point summary boxes
  1. Proposal lifecycle: discussion -> vote -> quorum check -> timelock -> execution
  2. On-chain voting is binding but costly; off-chain (Snapshot) is free but requires trust
  3. Quadratic voting reduces plutocracy; conviction voting rewards sustained support
  4. Delegation enables participation without active voting -- liquid democracy in practice
  5. Timelocks provide critical safety buffer between vote passage and execution

#### SECTION 3: Treasury Management & Economics (Frames 27-38)

**Frame 27: Section 3 Divider**
- Title: `Section 3: Treasury Management \& Economics`
- Subtitle: `How DAOs manage billions in assets and design sustainable token economies`
- Learning items:
  - Multi-sig treasury architecture (Gnosis Safe)
  - Treasury diversification and risk management
  - Grant programs and budget allocation
  - Token economics: inflation, buybacks, and sustainability

**Frame 28: DAO Treasury Overview**
- Two-column:
  - Left: Definition -- DAO treasury = collectively owned pool of assets controlled by governance
  - Right: TikZ bar chart showing top DAO treasuries (approximate values):
    - Uniswap: $3B+ (mostly UNI)
    - Optimism: $1B+ (OP)
    - Arbitrum: $2B+ (ARB)
    - Lido: $300M+
    - Aave: $200M+
- Key insight: most treasuries are concentrated in their own governance token -- a major risk

**Frame 29: Multi-Sig Treasury Architecture**
- TikZ architecture diagram:
  - Gnosis Safe at center (M-of-N multi-signature)
  - Signer roles: Core contributors, elected council, protocol-owned
  - Transaction flow: Proposal -> Multi-sig approval -> Execution
  - Guard modules: spending limits, whitelisted recipients, time delays
- Common configurations: 3-of-5 for small DAOs, 5-of-9 for large protocols
- `\bottomnote{Gnosis Safe manages over \$50B in digital assets across the ecosystem}`

**Frame 30: Treasury Management Function [FRAGILE] -- CODE FRAME 3**
- `\begin{frame}[fragile]{Treasury Management Contract}`
- Left column: Solidity treasury management snippet
```solidity
// DAO Treasury with Spending Limits
contract DAOTreasury {
    address public governance;
    mapping(address => uint256)
        public spendingCaps;
    uint256 public totalBudget;

    modifier onlyGovernance() {
        require(msg.sender == governance,
            "Not governance");
        _;
    }

    function allocateBudget(
        address recipient,
        uint256 amount
    ) external onlyGovernance {
        require(amount <= spendingCaps[
            recipient],
            "Exceeds spending cap");
        totalBudget -= amount;
        payable(recipient).transfer(
            amount);
        emit BudgetAllocated(
            recipient, amount);
    }
}
```
- Right column: explanation of governance-gated execution, spending caps, budget tracking, event emission for transparency

**Frame 31: Treasury Diversification**
- TikZ portfolio allocation diagram:
  - Risk tiers:
    - Conservative (40%): Stablecoins (USDC, DAI) for operational expenses
    - Moderate (30%): ETH and blue-chip DeFi for growth
    - Protocol Token (20%): Own governance token for incentives
    - Yield (10%): Staked assets, LP positions for passive income
  - Color-coded risk bands
- Why diversify? Governance token concentration risk -- if token drops 90%, treasury drops 90%

**Frame 32: Grant Programs**
- TikZ funnel diagram:
  - Grant applications submitted (top, wide)
  - Committee review and shortlisting
  - Community vote or committee approval
  - Milestone-based funding release
  - Impact reporting and accountability
- Examples: Uniswap Grants ($75M allocated), Aave Grants, Optimism RetroPGF
- Grant categories: Development, Research, Community, Marketing

**Frame 33: Streaming Payments**
- TikZ timeline showing streaming payment concept:
  - Traditional: Lump sum payment at proposal execution (risk of misuse)
  - Streaming: Continuous payment per second (Sablier, Superfluid, Llamapay)
  - Claimable amount increases linearly over time
  - Cancel stream if milestones not met
- Advantages: reduced trust requirements, automatic payroll, revocable

**Frame 34: Token Economics -- Supply Side**
- TikZ supply dynamics diagram:
  - Inflationary forces: staking rewards, liquidity mining, contributor compensation
  - Deflationary forces: token burns, buybacks, fee routing
  - Equilibrium: sustainable emission rate
- pgfplots chart: token supply over time with different emission schedules
- Examples: MKR burns from stability fees, UNI inflation schedule (2% perpetual after 4 years)

**Frame 35: Token Economics -- Demand Side**
- TikZ value accrual flowchart:
  - Protocol revenue -> Treasury -> Buyback or distribute to stakers
  - Governance utility: voting rights, proposal power
  - Access utility: fee discounts, premium features
  - Staking utility: security, yield, ve-model (vote-escrowed)
- The ve-model (Curve): lock tokens for longer = more voting power + more rewards
- `\bottomnote{Token value ultimately depends on the protocol's ability to generate sustainable revenue and direct it to token holders}`

**Frame 36: Compensation Models**
- TikZ comparison of compensation approaches:
  - Model 1: Fixed salary in stablecoins (predictable, no upside)
  - Model 2: Token-based compensation (aligned incentives, volatile)
  - Model 3: Hybrid (base salary + token bonus, most common)
  - Model 4: Retroactive rewards (Optimism RetroPGF, rewards past contributions)
- Vesting schedules: 1-4 year vesting with cliff, token streaming
- Contributor types: Core team, part-time, bounty hunters

**Frame 37: Financial Reporting & Transparency**
- TikZ dashboard mockup:
  - Panel 1: Treasury balance over time (line chart)
  - Panel 2: Monthly spending by category (bar chart)
  - Panel 3: Token holder distribution (pie chart)
  - Panel 4: Revenue vs expenditure (waterfall)
- Tools: DeBank, Zerion, Dune Analytics dashboards
- The transparency advantage: all transactions are on-chain and auditable

**Frame 38: Section 3 Summary**
- 5-point summary boxes
  1. DAO treasuries hold billions but face concentration risk in their own governance tokens
  2. Multi-sig wallets (Gnosis Safe) provide secure, multi-party treasury management
  3. Grant programs and streaming payments enable accountable resource allocation
  4. Token economics must balance inflationary incentives with deflationary sustainability
  5. On-chain transparency is a unique advantage -- every transaction is publicly auditable

#### SECTION 4: Governance Attacks & Security (Frames 39-48)

**Frame 39: Section 4 Divider**
- Title: `Section 4: Governance Attacks \& Security`
- Subtitle: `Understanding and defending against threats to decentralized governance`
- Learning items:
  - Flash loan governance attacks and prevention
  - Vote buying, bribery, and dark markets
  - Sybil attacks on governance systems
  - Defensive mechanisms: timelocks, guardians, veto power

**Frame 40: Governance Attack Taxonomy**
- TikZ taxonomy tree:
  - Root: Governance Attacks
  - Branch 1 (mlred): Economic Attacks (flash loans, vote buying, bribery)
  - Branch 2 (mlorange): Sybil Attacks (identity splitting, quadratic gaming)
  - Branch 3 (mlpurple): Social Attacks (proposal griefing, voter fatigue, apathy exploitation)
  - Branch 4 (mlblue): Technical Attacks (smart contract bugs, front-running votes)
- Rounded corners boxes with arrows

**Frame 41: Flash Loan Governance Attacks**
- TikZ step-by-step attack flow:
  - Step 1: Attacker borrows 10M governance tokens via flash loan (0 collateral)
  - Step 2: Attacker votes on malicious proposal (e.g., drain treasury)
  - Step 3: Proposal passes instantly (attacker has majority)
  - Step 4: Attacker repays flash loan in same transaction
  - Step 5: Treasury drained, attacker profits
- Defense: snapshot voting power at proposal creation block, not at vote time
- Real example: Beanstalk Farms ($182M attack, April 2022)

**Frame 42: Governance Attack Scenario [FRAGILE] -- CODE FRAME 4**
- `\begin{frame}[fragile]{Flash Loan Governance Attack}`
- Left column: Pseudocode showing attack flow
```solidity
// Flash Loan Governance Attack
contract GovernanceAttack {
    function attack(
        address lender,
        address governor,
        uint256 proposalId
    ) external {
        // Step 1: Borrow tokens
        IFlashLender(lender)
            .flashLoan(10_000_000e18);

        // Step 2: Vote with
        //         borrowed tokens
        IGovernor(governor)
            .castVote(
                proposalId,
                1 // FOR
            );

        // Step 3: Repay in same tx
        IERC20(token).transfer(
            lender, 10_000_000e18);
    }
}
```
- Right column: explanation of why this works (voting power checked at call time), defenses (ERC20Votes with checkpoints, snapshot at proposal creation), Compound's GovernorBravo solution

**Frame 43: Vote Buying & Bribery**
- TikZ flow diagram:
  - Briber offers $X per vote to token holders
  - Dark market: voters prove their vote via commit-reveal or delegation
  - Hidden bribery platforms: Convex (legitimate incentive alignment) vs dark vote markets
  - Impact: governance becomes pay-to-play
- The "governance is a market" thesis
- Defense: vote privacy (MACI), shielded voting

**Frame 44: Sybil Attacks on Governance**
- TikZ Sybil visualization:
  - Real scenario: 1 person creates 100 wallets
  - In token voting: no advantage (same total tokens)
  - In quadratic voting: 100x more influence (sqrt(1)*100 > sqrt(100))
  - In airdrop-based governance: multiple claims
- Sybil resistance methods: Gitcoin Passport, Worldcoin/proof-of-personhood, social graph analysis, minimum token holding period
- Tradeoff: privacy vs Sybil resistance

**Frame 45: The DAO Hack (2016)**
- TikZ historical timeline with technical detail:
  - April 2016: The DAO launches on Ethereum, raises 11.5M ETH (~$150M)
  - June 2016: Reentrancy vulnerability exploited, 3.6M ETH drained (~$60M)
  - July 2016: Ethereum community debates response
  - Hard fork: Ethereum (ETH) reverses hack vs Ethereum Classic (ETC) keeps original chain
- Technical detail: recursive call to withdraw before balance update
- Legacy: "Code is law" debate, led to improved auditing practices

**Frame 46: Defensive Mechanisms**
- TikZ defense-in-depth diagram (concentric rings):
  - Ring 1 (outermost): Timelock delays (24-48 hours minimum)
  - Ring 2: Guardian/veto role (can cancel during timelock)
  - Ring 3: Vote snapshot at proposal creation (anti-flash-loan)
  - Ring 4: Quorum requirements (prevent minority capture)
  - Ring 5 (innermost): Emergency shutdown (circuit breaker, pause)
- Each ring labeled with mechanism and which attack it prevents

**Frame 47: Governance Minimization**
- Two-column:
  - Left: Philosophy -- reduce the attack surface by reducing what governance controls
  - Progressive decentralization: team control -> DAO governance -> autonomous protocol
  - Right: TikZ spectrum showing governance scope over time:
    - Day 1: Team controls everything
    - Year 1: DAO controls parameters
    - Year 3: DAO controls upgrades
    - Year 5+: Protocol is immutable, governance only for grants
- Examples: Uniswap v3 (minimal governance), MakerDAO (extensive governance)
- `\bottomnote{The safest governance decision is one that doesn't need to be made -- immutable code can't be attacked via governance}`

**Frame 48: Section 4 Summary**
- 5-point summary boxes
  1. Flash loan attacks exploit instant token borrowing for vote manipulation -- snapshot voting is the defense
  2. Vote buying and bribery create pay-to-play governance -- vote privacy (MACI) is an emerging solution
  3. Sybil attacks undermine quadratic and identity-based voting -- proof-of-personhood is an open problem
  4. The 2016 DAO hack ($60M) was a watershed moment -- it split Ethereum and catalyzed security auditing
  5. Defense-in-depth (timelocks, guardians, snapshots, emergency shutdown) is essential for robust governance

#### SECTION 5: Real-World DAOs & Future (Frames 49-55)

**Frame 49: Section 5 Divider**
- Title: `Section 5: Real-World DAOs \& Future of Governance`
- Subtitle: `Case studies, participation challenges, and the road ahead`
- Learning items:
  - MakerDAO, Uniswap, and Aave governance case studies
  - Governance participation rates and voter apathy
  - Legal frameworks for DAOs by jurisdiction
  - The future of decentralized governance

**Frame 50: MakerDAO Governance**
- Two-column:
  - Left: Governance structure -- MKR token holders govern DAI stablecoin system
  - Key parameters: stability fees, collateral ratios, DSR (DAI Savings Rate)
  - Executive votes: continuous approval voting (hat system)
  - Right: TikZ governance flow: Forum discussion -> Signal poll -> Executive vote -> Spell execution
- Endgame Plan: SubDAOs, MetaDAOs, real-world asset integration
- Complexity concern: hundreds of governance decisions per year

**Frame 51: Uniswap & Aave Governance**
- TikZ side-by-side comparison:
  - Uniswap: UNI token, Governor Bravo, 4% quorum (~40M UNI), 7-day voting, 2-day timelock, fee switch debate
  - Aave: AAVE token, Governance v3, Safety Module, Risk DAO, cross-chain governance
- Key governance decisions:
  - Uniswap: fee switch, BSL license exceptions, deployment on new chains
  - Aave: risk parameter updates, new asset listings, protocol upgrades
- Participation rates comparison

**Frame 52: Governance Participation Crisis**
- TikZ data visualization:
  - Bar chart: average voter turnout by major DAO
    - MakerDAO: ~5% of MKR
    - Uniswap: ~3% of UNI
    - Compound: ~4% of COMP
    - Aave: ~2% of AAVE
  - Trendline showing participation declining over time
- Root causes: voter fatigue, gas costs, complexity, rational ignorance
- Solutions: delegation, gasless voting, incentivized participation, governance mining

**Frame 53: DAO Legal Frameworks**
- TikZ jurisdiction comparison table:
  - Wyoming (USA): DAO LLC since 2021, limited liability, smart contract as operating agreement
  - Marshall Islands: DAO LLC, more flexible than Wyoming
  - Switzerland: Association (Verein), foundation model
  - Singapore: Foundation company
  - EU/MiCA: No DAO-specific framework, token regulation applies
  - Cayman Islands: Foundation company, exempted limited partnership
- Key question: Is a DAO a general partnership by default? (Ooki DAO case -- CFTC sued a DAO)

**Frame 54: The Future of DAO Governance**
- TikZ three-panel forward-looking:
  - Panel 1: Governance Evolution -- AI-assisted governance, automated parameter tuning, cross-chain voting
  - Panel 2: Participation Innovation -- gasless voting everywhere, governance rewards, gamification, delegation marketplaces
  - Panel 3: Legal Integration -- global DAO standards, regulatory clarity, DAO-to-DAO collaboration, real-world legal recognition
- Timeline projections for each trend

**Frame 55: Key Takeaways and Course Summary**
- TikZ 5-box summary (matching CT Frame 55 style):
  - Box 1 (mlblue): DAO Fundamentals -- smart contracts replace hierarchies; membership can be token-based, share-based, or reputation-based
  - Box 2 (mlpurple): Voting Mechanisms -- from simple token voting to quadratic and conviction voting; delegation enables scalable participation
  - Box 3 (mlgreen): Treasury Management -- multi-sig wallets, diversification, and streaming payments enable accountable resource allocation
  - Box 4 (mlorange): Security -- flash loan attacks, vote buying, and Sybil attacks are real threats; defense-in-depth is essential
  - Box 5 (mlred): Real-World DAOs -- MakerDAO, Uniswap, and Aave demonstrate both the promise and challenges of decentralized governance
- Purple teaser bar: `Next: Advanced topics in decentralized identity, cross-chain governance, and DAO-to-DAO coordination`

**Acceptance Criteria (Task 4):**
- [ ] Exactly 55 frames with correct numbering
- [ ] 5 sections with divider and summary frames
- [ ] Exactly 4 `[fragile]` frames with lstlisting (Frames ~8, ~18, ~30, ~42)
- [ ] Preamble matches crypto_trading_markets.tex exactly (lines 1-52)
- [ ] All TikZ multi-line nodes have `align=center`
- [ ] No `\foreach` with `/` multi-variable syntax
- [ ] No parameterized styles with `#1`
- [ ] No reserved style names (diamond, step, text, signal)
- [ ] `\bottomnote` on every frame
- [ ] Compiles with pdflatex without errors

---

### TASK 5: Quiz DG-1 (`quiz/quiz_dg_part1.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz DG-1: DAO Fundamentals`
- 20 questions covering Section 1 topics:
  - DAO definition and properties (Q1-Q4)
  - Traditional organizations vs DAOs (Q5-Q7)
  - DAO architecture and Governor contracts (Q8-Q11)
  - Membership models: token, share, reputation (Q12-Q15)
  - DAO frameworks and legal status (Q16-Q20)
- Format: A/B/C/D multiple choice with explanations
- **Nav:** Dashboard + GitHub links ONLY (NO prev/next inter-quiz navigation). Copy quiz_ct_part1.html nav pattern.
- Copy CSS/JS structure from quiz_ct_part1.html exactly
- CSS variable: `--quiz-accent: #8b5cf6` (violet, same as existing template)

**Acceptance Criteria:**
- [ ] KaTeX v0.16.9 linked
- [ ] CSS variables match template
- [ ] 3-column grid layout
- [ ] 20 questions with JSON data
- [ ] All questions have correct answer and explanation
- [ ] Renders correctly in browser

---

### TASK 6: Quiz DG-2 (`quiz/quiz_dg_part2.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz DG-2: Voting & Governance`
- 20 questions covering Section 2 topics:
  - Proposal lifecycle and stages (Q1-Q3)
  - On-chain vs off-chain voting (Q4-Q6)
  - Token-weighted voting and plutocracy (Q7-Q9)
  - Quadratic and conviction voting (Q10-Q13)
  - Delegation and liquid democracy (Q14-Q16)
  - Quorum, thresholds, and timelocks (Q17-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 7: Quiz DG-3 (`quiz/quiz_dg_part3.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz DG-3: Treasury & Economics`
- 20 questions covering Section 3 topics:
  - DAO treasury overview and scale (Q1-Q3)
  - Multi-sig wallets and Gnosis Safe (Q4-Q6)
  - Treasury diversification strategies (Q7-Q9)
  - Grant programs and streaming payments (Q10-Q13)
  - Token economics: supply and demand (Q14-Q17)
  - Compensation models and transparency (Q18-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 8: Quiz DG-4 (`quiz/quiz_dg_part4.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz DG-4: Attacks/Security & Real-World DAOs`
- 20 questions covering Sections 4-5 topics:
  - Flash loan governance attacks (Q1-Q3)
  - Vote buying and bribery (Q4-Q6)
  - Sybil attacks and defenses (Q7-Q9)
  - The DAO hack (2016) (Q10-Q11)
  - Defensive mechanisms (Q12-Q14)
  - Governance minimization (Q15)
  - MakerDAO, Uniswap, Aave governance (Q16-Q18)
  - Participation crisis, legal frameworks, future (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 9: GitHub Pages Update (`index.html`)
**Priority:** HIGH | **Complexity:** LOW

#### Changes Required

**1. Add d9 CSS class (after d8 styles, around line 96):**
Insert AFTER line 96 (`.d8 summary{border-left:3px solid #10b981}`), BEFORE the `.lec-grid` rule (line 97):
```css
.section-head.d9 span{background:#8b5cf6}
.d9 summary{border-left:3px solid #8b5cf6}
```

**2. Add DG sidebar links (after CT entries, before `</details>` at line 175):**
Insert AFTER line 174 (`<a href="#sl-ct-main">CT Technical Lecture</a>`), BEFORE `</details>`:
```html
<a href="#sl-dg-mini">Mini-Lecture: DAOs & Governance</a>
<a href="#sl-dg-intro">DG INTRO Preview</a>
<a href="#sl-dg-pre">DG Pre-Class Handout</a>
<a href="#sl-dg-main">DG Technical Lecture</a>
```

**3. Update hero stats (line 180):**
- Lectures: 32 -> 36
- Quizzes: 36 -> 40

**4. Add DG subsection (after CT quiz-grid closing `</div>` at line 643, before `</section>` at line 644):**

```html
<div class="section-head d9" style="margin-top:16px"><span>DG</span><h2>Standalone Lectures: DAOs &amp; Governance</h2></div>
<div class="lec-grid">
<a href="lectures/dao_governance_intro.pdf" class="lec-card" id="sl-dg-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>DAOs &amp; Governance: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p></a>
<a href="lectures/dao_governance_intro_preview.pdf" class="lec-card" id="sl-dg-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>DAOs &amp; Governance: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/dao_governance_preclass.pdf" class="lec-card" id="sl-dg-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>DAOs &amp; Governance: Pre-Class Handout</h3>
<p>4 activities &bull; DAO exploration, voting mechanisms, treasury analysis</p></a>
<a href="lectures/dao_governance.pdf" class="lec-card" id="sl-dg-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>DAOs &amp; Governance: Decentralized Decision-Making</h3>
<p>~55 frames &bull; Voting, treasury, attacks, real-world DAOs</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_dg_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz DG-1</div>
<h3>DAO Fundamentals</h3>
<p>20 questions &bull; Architecture, membership, frameworks</p></a>
<a href="quiz/quiz_dg_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz DG-2</div>
<h3>Voting &amp; Governance</h3>
<p>20 questions &bull; Quadratic, conviction, delegation</p></a>
<a href="quiz/quiz_dg_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz DG-3</div>
<h3>Treasury &amp; Economics</h3>
<p>20 questions &bull; Multi-sig, grants, tokenomics</p></a>
<a href="quiz/quiz_dg_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz DG-4</div>
<h3>Attacks/Security &amp; Real-World DAOs</h3>
<p>20 questions &bull; Flash loans, Sybil, governance cases</p></a>
</div>
```

**Acceptance Criteria (Task 9):**
- [ ] d9 CSS class exists with violet #8b5cf6 and renders correctly
- [ ] DG sidebar links present with correct IDs
- [ ] Hero stats show 36 Lectures, 40 Quizzes
- [ ] DG subsection appears after CT subsection
- [ ] All href paths are correct (PDF for lectures, HTML for quizzes)
- [ ] All sidebar IDs match: sl-dg-mini, sl-dg-intro, sl-dg-pre, sl-dg-main
- [ ] No existing content broken

---

### TASK 10: Verification
**Priority:** CRITICAL | **Depends on:** Tasks 1-9

1. **LaTeX compilation check:**
   - `pdflatex dao_governance.tex` -- must compile without errors
   - `pdflatex dao_governance_intro.tex` -- must compile without errors
   - `pdflatex dao_governance_intro_preview.tex` -- must compile without errors
   - `pdflatex dao_governance_preclass.tex` -- must compile without errors

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
   - Hero stats show correct numbers (36 Lectures, 40 Quizzes)
   - DG sidebar IDs exist and scroll correctly
   - All DG lecture/quiz href paths are valid
   - d9 CSS class renders violet #8b5cf6

---

## Commit Strategy

### Commit 1: Core lecture files
```
Add L09 DAOs & Governance lecture bundle (4 LaTeX files)

- dao_governance.tex: 55-frame technical lecture (5 sections)
- dao_governance_intro.tex: 10-frame mini-lecture with TikZ comics
- dao_governance_intro_preview.tex: 6-frame INTRO preview
- dao_governance_preclass.tex: Pre-class handout (4 activities, glossary)
```

### Commit 2: Quiz files
```
Add DG-1 through DG-4 interactive quizzes for DAOs & Governance

- quiz_dg_part1.html: DAO Fundamentals (20 questions)
- quiz_dg_part2.html: Voting & Governance (20 questions)
- quiz_dg_part3.html: Treasury & Economics (20 questions)
- quiz_dg_part4.html: Attacks/Security & Real-World DAOs (20 questions)
```

### Commit 3: GitHub Pages integration
```
Add DAOs & Governance section to GitHub Pages landing page

- Add DG subsection with d9 violet color class (#8b5cf6)
- Add sidebar navigation links
- Update hero stats: 36 Lectures, 40 Quizzes
```

---

## Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| TikZ compilation errors from `\\` in nodes | MANDATE `align=center` on every node containing `\\`. Verify with grep before compile. |
| `\foreach` multi-variable syntax crash | BAN `/` syntax entirely. Use separate `\foreach` loops or manual placement. |
| Parameterized style `#1` conflict | BAN `#1` in all custom TikZ styles. Use fixed styles only. |
| Style name conflict with pgf built-ins | Use unique prefixes (e.g., `dgbox`, `dgnode`, `dgstep`) for all custom style names. Avoid: diamond, step, text, signal. |
| lstlisting in non-fragile frame | Every frame with lstlisting MUST have `[fragile]` option. Verify with grep. |
| Color mismatch with L04-L08 | Copy color definitions verbatim from crypto_trading_markets.tex, character by character. |
| Code frames use Solidity this time | The 4 code frames use Solidity snippets (Governor, VotingPower, Treasury, Attack). The Solidity lstdef in preamble is actively used. Ensure `language=Solidity` is set. |
| index.html regression | Only add content after CT section. Do not modify any existing HTML elements. |
| pdflatex not available | Use `pdflatex` with `-interaction=nonstopmode` for error detection. Fall back to error-log review. |
| Overly long TikZ lines causing Beamer overflow | Test with 8pt font size. Use `\scriptsize` and `\tiny` aggressively in TikZ nodes. |
| Solidity code too long for fragile frames | Keep code snippets to 15-20 lines max. Use comments to indicate omitted parts. Pseudocode simplifications acceptable. |
| Quiz accent color mismatch | The existing quiz template already uses `--quiz-accent: #8b5cf6` (violet). DG quizzes match by default. |

---

## Success Criteria

| Criterion | Verification Method |
|-----------|-------------------|
| All 4 LaTeX files compile cleanly | `pdflatex -interaction=nonstopmode` returns exit 0 |
| Tech lecture has exactly 55 frames | `grep -c "\\begin{frame}" dao_governance.tex` = 55 |
| Mini-lecture has exactly 10 frames | `grep -c "\\begin{frame}" dao_governance_intro.tex` = 10 |
| INTRO has exactly 6 frames | `grep -c "\\begin{frame}" dao_governance_intro_preview.tex` = 6 |
| Exactly 4 fragile frames in tech lecture | `grep -c "\[fragile\]" dao_governance.tex` = 4 |
| 80 quiz questions total (4 x 20) | JSON question count per file = 20 |
| All quiz explanations non-empty | No `"explanation": ""` in any quiz |
| index.html hero shows 36/40 | Visual inspection of rendered page |
| DG sidebar IDs work | Click each sidebar link, verify scroll |
| No TikZ safety violations | Automated grep checks pass |
| Color palette exact match | Diff color definitions against crypto_trading_markets.tex |
| d9 violet CSS applied correctly | Visual inspection: #8b5cf6 violet for DG section |

---

## File Path Summary (All Deliverables)

```
D:\Joerg\Research\slides\cryptocurrency\
  lectures\
    dao_governance_intro.tex             (Task 1 - Mini-lecture, 10 frames)
    dao_governance_intro_preview.tex     (Task 2 - INTRO preview, 6 frames)
    dao_governance_preclass.tex          (Task 3 - Pre-class handout)
    dao_governance.tex                   (Task 4 - Tech lecture, 55 frames)
  quiz\
    quiz_dg_part1.html                   (Task 5 - Quiz DG-1, 20 questions)
    quiz_dg_part2.html                   (Task 6 - Quiz DG-2, 20 questions)
    quiz_dg_part3.html                   (Task 7 - Quiz DG-3, 20 questions)
    quiz_dg_part4.html                   (Task 8 - Quiz DG-4, 20 questions)
  index.html                             (Task 9 - GitHub Pages update)
```
