# L11 Work Plan: Real-World Assets (RWA) & Tokenization Standalone Lecture Bundle

## Context

### Original Request
Create the complete L11 Real-World Assets (RWA) & Tokenization standalone lecture bundle following the exact patterns established in L04-L10 (most recently the Layer 2 Scaling Solutions bundle). The bundle includes a ~55-frame technical lecture, 10-frame mini-lecture, 6-frame INTRO preview, pre-class handout, 4 HTML quizzes, and GitHub Pages integration.

### Reference Files (Structural Templates)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\layer2_scaling.tex` -- Tech lecture template (55 frames, 5 sections, compact preamble, lines 1-52)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\layer2_scaling_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble, lines 1-85)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\layer2_scaling_intro_preview.tex` -- INTRO preview template (6 frames, compact preamble without colortbl/Solidity, lines 1-35)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\layer2_scaling_preclass.tex` -- Pre-class handout template (article-class, 4 activities, glossary, lines 1-60)
- `D:\Joerg\Research\slides\cryptocurrency\quiz\quiz_l2_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data, Dashboard + GitHub nav only)
- `D:\Joerg\Research\slides\cryptocurrency\index.html` -- GitHub Pages (d10 L2 subsection pattern at lines 693-729, sidebar links at lines 183-186, hero stats at line 192, CSS classes at lines 99-100)

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

**index.html current state (AFTER L10 integration):**
- Hero stats: 40 Lectures, 44 Quizzes (line 192)
- CSS classes defined: d1-d10 (lines 41-100)
- Sidebar: L2 entries at lines 183-186, followed by `</details>` at line 187
- L2 subsection: lines 693-729, followed by `</section>` at line 730
- D11 CSS does NOT yet exist -- must be added after d10 (line 100)
- RW sidebar links do NOT yet exist -- must be added after L2 entries (line 186)
- RW subsection does NOT yet exist -- must be added after L2 quiz-grid closing `</div>` (line 729), before `</section>` (line 730)

---

## Work Objectives

### Core Objective
Produce a complete, self-contained L11 Real-World Assets (RWA) & Tokenization lecture bundle that compiles without errors and integrates into the existing GitHub Pages site.

### Deliverables

| # | Deliverable | File Path | Description |
|---|-------------|-----------|-------------|
| 1 | Mini-Lecture | `lectures/rwa_tokenization_intro.tex` | 10-frame TikZ comic introduction, ZERO code |
| 2 | INTRO Preview | `lectures/rwa_tokenization_intro_preview.tex` | 6-frame preview with charts & roadmap |
| 3 | Pre-Class Handout | `lectures/rwa_tokenization_preclass.tex` | Article-class, 4 activities, glossary |
| 4 | Technical Lecture | `lectures/rwa_tokenization.tex` | ~55-frame Beamer presentation, 5 sections, light code (3-4 fragile) |
| 5 | Quiz RW-1 | `quiz/quiz_rw_part1.html` | 20 questions: Tokenization Fundamentals |
| 6 | Quiz RW-2 | `quiz/quiz_rw_part2.html` | 20 questions: Stablecoins Deep Dive |
| 7 | Quiz RW-3 | `quiz/quiz_rw_part3.html` | 20 questions: Security Tokens & Compliance |
| 8 | Quiz RW-4 | `quiz/quiz_rw_part4.html` | 20 questions: Real Estate & Bond Tokenization, RWA Ecosystem & Future |
| 9 | index.html update | `index.html` | d11 teal CSS, RW sidebar links, hero stats (44 Lectures, 48 Quizzes), RW subsection |

### Definition of Done
- All 4 LaTeX files compile with `pdflatex` without errors
- All 4 HTML quiz files render correctly in browser
- index.html displays RW subsection with correct links and sidebar IDs
- Hero stats updated to 44 Lectures, 48 Quizzes
- Frame counts match: 55 tech + 10 mini + 6 intro = 71 frames total
- Exactly 4 `[fragile]` frames with code lstlisting in tech lecture (Frames ~8, ~20, ~31, ~43)
- Color palette matches L04-L10 exactly

---

## Must Have / Must NOT Have

### MUST Have
1. Exact same color palette (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray)
2. Same Beamer theme configuration as layer2_scaling.tex
3. Same Solidity language definition and lstset in tech lecture preamble (code frames use Solidity snippets -- RWA token contracts)
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
4. NO reserved style names: `diamond`, `step`, `text`, `signal` -- use unique prefixes like `rwabox`, `rwanode`, `rwastep`
5. Code frames MUST use `[fragile]` option -- every frame containing `lstlisting` environment

---

## 5-Section Topic Breakdown

### Section 1: Tokenization Fundamentals (Frames 4-14, 11 frames)
What is tokenization (digitizing ownership rights on a blockchain), history of asset digitization, tokenizable asset classes (real estate, bonds, commodities, art, intellectual property, carbon credits), token standards (ERC-20 for fungible, ERC-721 for unique, ERC-1155 for hybrid, ERC-3643/T-REX for compliant security tokens), fractionalization (splitting high-value assets into affordable units), benefits of tokenization (24/7 markets, global access, instant settlement T+0, programmable compliance, reduced intermediaries), challenges (legal recognition, oracle dependency, liquidity bootstrapping).

### Section 2: Stablecoins Deep Dive (Frames 15-25, 11 frames)
Stablecoin taxonomy (fiat-backed, crypto-backed, algorithmic, commodity-backed), USDT mechanics (Tether, largest by market cap, reserve composition controversies), USDC mechanics (Circle, fully reserved, regulated), DAI mechanics (MakerDAO, crypto-collateralized, overcollateralized CDPs), stablecoin reserves and attestation models, depeg risks and mechanisms, Terra/Luna collapse case study (algorithmic stablecoin death spiral, $40B wipeout, contagion effects), regulatory frameworks (EU MiCA stablecoin rules, US stablecoin legislation proposals), stablecoin market dominance ($150B+ market cap).

### Section 3: Security Tokens & Compliance (Frames 26-36, 11 frames)
Security vs utility tokens (legal classification), Howey test (investment contract test: investment of money, common enterprise, expectation of profits, from efforts of others), SEC enforcement actions (Ripple/XRP case), ERC-3643 (T-REX) standard for compliant security tokens, on-chain identity and KYC/AML (claims-based identity, identity registries), transfer restrictions and whitelisting, regulated security token exchanges (tZERO, Securitize Markets, INX), legal wrappers for tokenized assets (SPVs, trusts, DAOs as legal entities), tokenized securities vs traditional securities (settlement, custody, dividend distribution), accredited investor requirements.

### Section 4: Real Estate & Bond Tokenization (Frames 37-47, 11 frames)
Real estate tokenization mechanics (property -> SPV -> token), RealT platform (fractional US real estate on Gnosis Chain, rental yield distribution), Centrifuge protocol (tokenizing real-world credit: invoices, mortgages, trade finance), Maple Finance (institutional lending via tokenized credit pools), bond tokenization (JPMorgan Onyx: intraday repo, Siemens $64M digital bond on Polygon, European Investment Bank EUR 100M bond on Ethereum), credit tokenization and private credit markets on-chain, yield-bearing tokens (tokenized T-bills: Ondo USDY, Franklin Templeton BENJI), institutional adoption drivers (efficiency, transparency, programmability), case studies with real data.

### Section 5: RWA Ecosystem & Future (Frames 48-55, 8 frames)
RWA market size projections ($16T tokenized by 2030 per BCG/ADDX, $10T by 2030 per McKinsey), BlackRock BUIDL fund (tokenized US Treasury fund on Ethereum, $500M+ AUM), Ondo Finance (tokenized treasuries and bonds), MakerDAO RWA vaults (allocating DAI backing to real-world assets, $2B+ in RWA), regulatory landscape and challenges (jurisdictional fragmentation, legal enforceability of on-chain ownership), oracle problem for RWA (linking on-chain tokens to off-chain asset status), interoperability between TradFi and DeFi (Chainlink CCIP, institutional custody solutions), future outlook (central bank experiments, SWIFT tokenization pilots, interbank settlement).

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

### TASK 1: Mini-Lecture (`lectures/rwa_tokenization_intro.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM | **Estimated frames:** 10

#### Preamble
- Copy the ENTIRE preamble from `layer2_scaling_intro.tex` (verbose style), changing only:
  - Title: `Real-World Assets \& Tokenization: A Visual Introduction`
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
- Quote: `"Tokenization of real-world assets is the killer app for blockchain" -- Larry Fink, BlackRock CEO`
- Purple title, blue subtitle

**Frame 2: What is Tokenization? (TikZ Comic)**
- 3-panel comic layout (same panel dimensions as layer2_scaling_intro.tex):
  - Panel 1: Alice owns a $1 million apartment building. "I need cash but I don't want to sell the whole building!" Worried face, thought bubble showing building with price tag.
  - Panel 2: Bob explains: "What if you could split it into 1,000 digital tokens? Each token represents $1,000 of ownership!" TikZ diagram: building on left, arrow, 1000 small token icons on right. Fractionalization concept.
  - Panel 3: "Now anyone worldwide can buy tokens and earn rental income!" Globe with people buying tokens. Monthly rent $5,000 -> distributed proportionally. "Fractional ownership, global access, 24/7 trading!"
- Stick figures, speech bubbles, same drawing style as L2 intro

**Frame 3: Types of Tokenizable Assets**
- TikZ showcase grid (6 panels):
  - Real Estate: buildings, land, REITs -> fractional ownership
  - Bonds & Treasuries: government/corporate debt -> instant settlement
  - Commodities: gold, oil, carbon credits -> verifiable supply chain
  - Art & Collectibles: fine art, luxury goods -> democratized access
  - Private Credit: loans, invoices, trade finance -> transparent risk
  - Intellectual Property: royalties, patents, music rights -> automated payments
- Each panel with an icon, asset name, and one-line benefit
- Color-coded by category

**Frame 4: Token Standards Explained (TikZ Comic)**
- 3-panel layout:
  - Panel 1: ERC-20 tokens are fungible -- "Every token is the same, like dollar bills. 1 USDC = 1 USDC. Great for shares, stablecoins, commodity tokens." Stack of identical coins illustration.
  - Panel 2: ERC-721 tokens are unique -- "Every token is different, like property deeds. Token #42 = Apartment 5B in Manhattan." Each token has a unique ID with different properties attached.
  - Panel 3: ERC-1155 is both -- "Multiple types in one contract. Token ID 1 = fungible gold grams, Token ID 2 = unique artwork." Hybrid illustration showing both types from single contract. "And ERC-3643 adds compliance rules for securities!"
- Color-coded panels

**Frame 5: Stablecoins: The First Killer App**
- TikZ infographic:
  - Center: Stablecoin Universe ($150B+ market cap)
  - Three branches:
    - Fiat-backed (largest): USDT ($90B+, bank reserves), USDC ($30B+, fully audited), diagram showing 1:1 backing
    - Crypto-backed: DAI ($5B+, overcollateralized with ETH/WBTC), diagram showing 150% collateralization
    - Algorithmic (cautionary): UST/Luna ($0 -- collapsed May 2022, $40B wiped out), skull and crossbones icon
  - Key stat callout: "Stablecoins settle $10T+ annually -- more than Visa"

**Frame 6: The Terra/Luna Collapse (TikZ Comic)**
- 3-panel comic:
  - Panel 1: "UST was an algorithmic stablecoin -- no real reserves, just math." UST pegged to $1 via LUNA burn/mint mechanism. "When you redeem $1 UST, it mints $1 of LUNA." Diagram of the peg mechanism with circular arrows.
  - Panel 2: "But when everyone tried to exit at once, the death spiral began." UST depeg from $1 to $0.10. LUNA hyperinflation from $80 to $0.00001. Red downward arrows, panicked stick figures running for exits.
  - Panel 3: "$40 billion wiped out in 72 hours. Largest crypto collapse in history." Aftermath: regulatory crackdown, algorithmic stablecoins discredited, Terra founder Do Kwon arrested. Newspaper headline style.

**Frame 7: Security Tokens vs Utility Tokens**
- TikZ side-by-side comparison:
  - Left (mlblue): Security Tokens
    - Represent ownership in real assets
    - Subject to securities law (SEC, MiCA)
    - Howey test applies
    - Require KYC/AML compliance
    - Trade on regulated exchanges
    - Examples: tokenized real estate, tokenized bonds
  - Right (mlgreen): Utility Tokens
    - Provide access to a service/platform
    - Not securities (in theory)
    - No ownership rights
    - Often less regulated
    - Trade on crypto exchanges
    - Examples: ETH (gas), LINK (oracle fees)
  - Center divider: "The Howey Test: Is it an investment of money, in a common enterprise, with expectation of profits, from the efforts of others?"

**Frame 8: BlackRock & Institutional Adoption**
- TikZ timeline / news board:
  - 2023 Q4: BlackRock files for Bitcoin ETF (approved Jan 2024)
  - 2024 Q1: BlackRock launches BUIDL -- tokenized US Treasury fund on Ethereum ($500M+ AUM)
  - 2024: JPMorgan Onyx processes $1B+ daily in tokenized repo transactions
  - 2024: Siemens issues $64M digital bond on Polygon blockchain
  - 2024: Franklin Templeton BENJI fund (tokenized T-bills, $400M+)
  - 2025: SWIFT completes tokenization interoperability pilots with 12+ banks
- Key quote: "In five years, every financial asset will be tokenized" -- Larry Fink
- Institutional logos implied via labeled boxes

**Frame 9: The RWA Market Opportunity**
- TikZ showcase with data:
  - Market size projections (bar chart style):
    - 2024: $5B tokenized (excluding stablecoins)
    - 2027: $50B projected
    - 2030: $10-16T projected (BCG/McKinsey estimates)
  - Breakdown by asset class (pie chart style):
    - Bonds & Treasuries: 40%
    - Real Estate: 25%
    - Private Credit: 15%
    - Commodities: 10%
    - Other (art, IP, carbon): 10%
  - Key stat: "Global real estate alone is $330T -- even 1% tokenization = $3.3T"

**Frame 10: Key Takeaways**
- TikZ numbered boxes (5 takeaways):
  1. Tokenization converts real-world assets into blockchain tokens, enabling fractional ownership and 24/7 global trading
  2. Stablecoins ($150B+ market cap) are the most successful RWA category, settling trillions annually
  3. Security tokens must comply with securities law (Howey test, KYC/AML) unlike utility tokens
  4. Institutional giants (BlackRock, JPMorgan, Franklin Templeton) are actively building on-chain
  5. The RWA market could reach $10-16 trillion by 2030 -- the bridge between TradFi and DeFi
- Teal teaser bar at bottom

**Acceptance Criteria (Task 1):**
- [ ] Exactly 10 frames
- [ ] Zero `[fragile]` frames, zero lstlisting
- [ ] All TikZ comics use same panel style as layer2_scaling_intro.tex (draw, rounded corners, stick figures)
- [ ] All multi-line TikZ nodes have `align=center`
- [ ] Verbose preamble matching layer2_scaling_intro.tex structure
- [ ] Compiles with pdflatex without errors

---

### TASK 2: INTRO Preview (`lectures/rwa_tokenization_intro_preview.tex`)
**Priority:** HIGH | **Complexity:** LOW | **Estimated frames:** 6

#### Preamble
- Compact preamble matching `layer2_scaling_intro_preview.tex` exactly
- Same compact style as tech lecture BUT without colortbl, without Solidity definition
- Minimal TikZ libraries: `arrows.meta,positioning,shapes.geometric,calc`
- Title: `Real-World Assets \& Tokenization: Course Preview`
- Subtitle: `INTRO Preview`

#### Frame Specifications

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Why RWA Tokenization Matters**
- Two-column: pgfplots bar chart (left) + Key Metrics block (right)
- Chart: Traditional asset settlement time vs tokenized, intermediary costs traditional vs tokenized, market accessibility (hours/week) traditional vs tokenized
- Key metrics: $150B+ stablecoin market cap, $16T projected tokenized by 2030, 24/7 trading vs 5-day markets, T+0 settlement vs T+2, 90% fewer intermediaries

**Frame 3: RWA Ecosystem at a Glance**
- TikZ hub diagram (same style as L2 "Ecosystem at a Glance"):
  - Center: RWA Ecosystem
  - Spokes: Stablecoins (USDT, USDC, DAI), Tokenized Treasuries (BUIDL, BENJI, Ondo), Real Estate (RealT, Centrifuge), Private Credit (Maple, Goldfinch), Security Tokens (ERC-3643, Securitize), Infrastructure (Chainlink, SWIFT)
- Color-coded by category

**Frame 4: RWA Market Growth Trajectory**
- Two-column: pgfplots line chart (left) + Growth Drivers block (right)
- Chart: Total RWA value tokenized (excluding stablecoins) and number of active RWA protocols from 2020-2025
- Growth drivers: Institutional adoption (BlackRock, JPMorgan), regulatory clarity (MiCA, stablecoin bills), yield-bearing tokens appeal (tokenized T-bills), DeFi-TradFi convergence

**Frame 5: Course Coverage**
- TikZ 5-step process flow (same style as L2 "Course Coverage"):
  - (1) Tokenization Fundamentals
  - (2) Stablecoins Deep Dive
  - (3) Security Tokens & Compliance
  - (4) Real Estate & Bond Tokenization
  - (5) RWA Ecosystem & Future
- Sub-labels for each step
- Prerequisites + Outcomes blocks

**Frame 6: What You Will Learn**
- Two-column: Learning Outcomes block (left) + TikZ skill diagram (right)
- Outcomes: Token standards, stablecoin mechanics, compliance frameworks, institutional RWA platforms, market projections
- TikZ: central "RWA Mastery" node with 5 skill spokes

**Acceptance Criteria (Task 2):**
- [ ] Exactly 6 frames
- [ ] Compact preamble matching layer2_scaling_intro_preview.tex
- [ ] pgfplots charts with correct axis styling
- [ ] Compiles with pdflatex without errors

---

### TASK 3: Pre-Class Handout (`lectures/rwa_tokenization_preclass.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM

#### Preamble
- Article-class matching `layer2_scaling_preclass.tex` exactly
- `\documentclass[11pt,a4paper]{article}`
- Same packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- Color definitions using HTML format (not RGB)
- Header: `Real-World Assets \& Tokenization | Lesson 11 | Pre-Class Discovery Handout`
- `\activitybox` and `\fillcell` commands

#### Activity 1: Explore the RWA Landscape (10 min)
- Visit RWA.xyz (the canonical RWA data aggregator) and DeFi Llama RWA dashboard, answer:
  1. What is the total value of tokenized real-world assets (excluding stablecoins)? How has it grown over the past year?
  2. List the top 3 RWA protocols by total value locked. For each, note: name, TVL, asset type (treasuries/credit/real estate), and blockchain.
  3. Pick one protocol and explore what assets it tokenizes. How does a user invest? What is the minimum investment?
  4. Compare the yield on a tokenized US Treasury product (e.g., Ondo USDY or Franklin BENJI) vs a traditional brokerage Treasury purchase. What are the differences in access, minimum investment, and settlement time?
- Bonus: Find the total stablecoin market cap on CoinGecko. What percentage of the total crypto market cap do stablecoins represent?
- Fill-in table: Protocol Name | TVL ($) | Asset Type | Chain | Minimum Investment

#### Activity 2: Stablecoin Comparison (10 min)
- Compare the three main stablecoin models across key dimensions:
  1. How does USDT (Tether) maintain its $1 peg? What backs it? Look up the latest Tether attestation report -- what assets are in the reserves?
  2. How does USDC (Circle) maintain its $1 peg? How does its reserve transparency differ from USDT?
  3. How does DAI (MakerDAO) maintain its $1 peg without holding dollars in a bank? What is "overcollateralization" and why is it needed?
  4. What happened to UST/Terra in May 2022? Why did the algorithmic peg fail?
- Fill-in table: Dimension | USDT | USDC | DAI | UST (Collapsed)
  - Rows: Backing Model, Market Cap, Reserve Transparency, Depeg History, Regulatory Status, Issuer

#### Activity 3: Security Token Analysis (5 min)
- Research the regulatory landscape for tokenized securities:
  1. What is the Howey Test? List its four prongs. Look up one SEC enforcement action against a token and explain which Howey prong was violated.
  2. What is ERC-3643 (T-REX)? How does it differ from a regular ERC-20 token? What compliance features does it add?
  3. Find Securitize.io or tZERO. What types of assets can you trade on these platforms? Do they require KYC?
  4. Compare: if you buy a tokenized share of a REIT on Securitize vs a traditional REIT share on a stock exchange, what are the differences in settlement, trading hours, and minimum investment?
- Fill-in: Howey Test Prongs: 1.___ 2.___ 3.___ 4.___

#### Activity 4: Institutional RWA Products (5 min)
- Explore real institutional RWA products:
  1. Look up BlackRock's BUIDL fund. What asset does it tokenize? On which blockchain? What is its current AUM? What is the minimum investment?
  2. Look up Ondo Finance. What products does it offer? What blockchain(s) does it operate on? What yields are available?
  3. Research MakerDAO's (now Sky) RWA vaults. How much of DAI's backing comes from real-world assets? What types of RWA collateral does it accept?
  4. Why are institutions like BlackRock and JPMorgan interested in tokenization? List 3 specific efficiency gains tokenization provides over traditional finance.
- Fill-in table: Product | Issuer | Asset | Chain | AUM | Yield

#### Glossary (14 terms)

| Term | Definition |
|------|-----------|
| **Tokenization** | The process of representing ownership rights to a real-world asset (real estate, bonds, commodities) as a digital token on a blockchain, enabling fractional ownership, 24/7 trading, and programmable compliance. |
| **Real-World Asset (RWA)** | Any tangible or financial asset that exists outside the blockchain (real estate, bonds, commodities, art, intellectual property) that can be represented on-chain through tokenization. |
| **Stablecoin** | A cryptocurrency designed to maintain a stable value relative to a reference asset (usually USD). Types include fiat-backed (USDT, USDC), crypto-backed (DAI), and algorithmic (UST -- collapsed). |
| **Fiat-Backed Stablecoin** | A stablecoin backed 1:1 by reserves of fiat currency or equivalent assets (Treasury bills, commercial paper) held by a centralized issuer. USDT and USDC are the largest examples. |
| **Overcollateralization** | A mechanism where the collateral locked to mint a stablecoin exceeds the value of the stablecoin issued (e.g., $150 of ETH to mint $100 of DAI), providing a safety buffer against price drops. |
| **Security Token** | A digital token that represents an investment contract in a real-world asset, subject to securities regulations (SEC in US, MiCA in EU). Must comply with KYC/AML and transfer restrictions. |
| **Howey Test** | A US Supreme Court test to determine if a transaction is an "investment contract" (security): (1) investment of money, (2) in a common enterprise, (3) with expectation of profits, (4) derived from efforts of others. |
| **ERC-3643 (T-REX)** | An Ethereum token standard for compliant security tokens that adds identity verification (on-chain KYC), transfer restrictions (whitelisting), and compliance rules on top of the ERC-20 interface. |
| **Fractionalization** | The process of dividing a high-value asset into many smaller, affordable units (tokens), enabling investors to own a fraction of an asset they couldn't afford to buy whole. |
| **SPV (Special Purpose Vehicle)** | A legal entity (usually an LLC) created to hold a specific real-world asset, whose ownership shares are then tokenized. The SPV provides the legal link between the token and the underlying asset. |
| **Reserve Attestation** | A periodic audit or report verifying that a stablecoin issuer holds sufficient reserves to back all outstanding tokens. USDC publishes monthly attestations; USDT provides quarterly reports. |
| **Yield-Bearing Token** | A token that generates returns for holders by representing ownership of yield-producing assets (e.g., tokenized Treasury bills paying ~5% APY). Examples: Ondo USDY, Franklin BENJI, Mountain USDM. |
| **MiCA (Markets in Crypto-Assets)** | The European Union's comprehensive regulatory framework for crypto-assets, including specific rules for stablecoin issuers (reserve requirements, redemption rights, ban on interest for e-money tokens). |
| **Tokenized Treasury** | A blockchain-based representation of US Treasury bills or bonds, allowing crypto-native investors to access government bond yields without traditional brokerage accounts. Example: BlackRock BUIDL fund. |

**Acceptance Criteria (Task 3):**
- [ ] Article-class preamble matches layer2_scaling_preclass.tex
- [ ] 4 activities with `\activitybox` command
- [ ] Glossary with 14 terms in tabular format
- [ ] Header says "Lesson 11"
- [ ] Fill-in tables with `\fillcell`
- [ ] Compiles with pdflatex without errors

---

### TASK 4: Technical Lecture (`lectures/rwa_tokenization.tex`)
**Priority:** HIGH | **Complexity:** HIGH | **Estimated frames:** 55

#### Preamble (copy from layer2_scaling.tex exactly)
- Compact single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- All color definitions (mlblue through mlgray + solkeyword/string/comment/number)
- Beamer theme colors, navigation symbols, itemize, margins
- `\bottomnote` command
- Solidity language definition and `\lstset`
- TikZ/pgfplots with `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `Real-World Assets \& Tokenization: Bridging TradFi and DeFi`
- Subtitle: `Standalone Technical Lecture`

#### OPENING (Frames 1-3)

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ roadmap with 5 boxes (same style as L2 roadmap):
  - Box 1 (mlblue): `1. Tokenization\\Fundamentals`
  - Box 2 (mlgreen): `2. Stablecoins\\Deep Dive`
  - Box 3 (mlorange): `3. Security Tokens\\\& Compliance`
  - Box 4 (mlred): `4. Real Estate \&\\Bond Tokenization`
  - Box 5 (mlpurple): `5. RWA Ecosystem\\\& Future`
- ALL boxes MUST have `align=center` since they contain `\\`
- Stealth arrows connecting boxes
- Two-column: Learning Objectives + Prerequisites
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--5}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections from tokenization fundamentals to the future of the RWA ecosystem}`

#### SECTION 1: Tokenization Fundamentals (Frames 4-14)

**Frame 4: Section 1 Divider**
- `beamercolorbox` with palette quaternary
- Title: `Section 1: Tokenization Fundamentals`
- Subtitle: `What is tokenization, asset classes, token standards, and the fractionalization revolution`
- Two-column: What You Will Learn + Frames in This Section
- Learning items:
  - What tokenization means and how it digitizes ownership
  - Tokenizable asset classes: real estate, bonds, commodities, art
  - Token standards: ERC-20, ERC-721, ERC-1155, ERC-3643
  - Benefits: fractional ownership, 24/7 markets, global access

**Frame 5: What is Tokenization?**
- TikZ process flow diagram:
  - Step 1: Real-world asset exists (building, bond, gold bar)
  - Step 2: Legal wrapper created (SPV, trust, or direct registration)
  - Step 3: Smart contract deployed (defines token properties, ownership rules)
  - Step 4: Tokens minted (representing fractional ownership shares)
  - Step 5: Tokens traded on-chain (secondary market, 24/7, global)
  - Step 6: Rights enforced (dividends, rent, redemption via smart contract)
- Each step with icon and one-line description
- Dashed line separating "off-chain legal reality" from "on-chain digital representation"
- `\bottomnote{Tokenization creates a digital twin of asset ownership -- the legal wrapper ensures the token conveys real legal rights}`

**Frame 6: Tokenizable Asset Classes**
- TikZ 6-panel grid (same style as mini-lecture Frame 3 but more detailed):
  - Real Estate ($330T global): residential, commercial, REITs. Fractional ownership enables $50 minimum investments.
  - Bonds & Fixed Income ($130T global): government bonds, corporate bonds, T-bills. T+0 settlement vs T+2.
  - Commodities ($100T+ global): gold (Paxos Gold, Tether Gold), oil, agricultural. Verifiable supply chain.
  - Private Credit ($1.5T): invoices, trade finance, structured credit. Transparent risk assessment.
  - Art & Collectibles: fine art (Masterworks), luxury goods, wine. Democratized access to alternative assets.
  - Carbon Credits & ESG: voluntary carbon markets, renewable energy certificates. Programmable retirement.
- Total addressable market annotation: "$500T+ in global assets"
- `\bottomnote{Even tokenizing 1\% of global real estate (\$330T) would create a \$3.3T on-chain market -- larger than all of DeFi today}`

**Frame 7: Token Standards for RWA**
- TikZ comparison table (styled with colored headers):
  - ERC-20 (mlblue): Fungible. Every token identical. Used for: stablecoins, commodity tokens, fund shares. Examples: USDC, PAXG, BUIDL.
  - ERC-721 (mlgreen): Non-fungible. Each token unique. Used for: property deeds, art certificates, unique assets. Examples: RealT property tokens, art NFTs.
  - ERC-1155 (mlorange): Multi-token. Both fungible and non-fungible in one contract. Used for: gaming assets, mixed portfolios, batch operations. Efficient gas usage.
  - ERC-3643 / T-REX (mlred): Compliant security. ERC-20 + identity + transfer restrictions. Used for: regulated securities, security tokens. Requires KYC/AML.
- Arrows showing ERC-3643 inherits from ERC-20 and adds compliance layer
- `\bottomnote{ERC-3643 is the standard adopted by most security token platforms -- it adds identity verification and transfer restrictions to ERC-20}`

**Frame 8: ERC-20 Token for Asset Tokenization [FRAGILE] -- CODE FRAME 1**
- `\begin{frame}[fragile]{ERC-20 Asset Token Contract}`
- Left column: Solidity snippet for a simplified tokenized asset
```solidity
// Tokenized Real Estate Fund
contract RealEstateFund {
    string public name =
        "NYC Property Fund";
    string public symbol = "NYCPF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256)
        public balanceOf;

    address public manager;
    uint256 public navPerToken;

    constructor(uint256 supply) {
        manager = msg.sender;
        totalSupply = supply;
        balanceOf[msg.sender] = supply;
    }

    function updateNAV(
        uint256 newNAV
    ) external {
        require(msg.sender == manager);
        navPerToken = newNAV;
        emit NAVUpdated(newNAV);
    }
}
```
- Right column: explanation of how an ERC-20 token represents fund shares, NAV (Net Asset Value) updates by fund manager, balanceOf tracks fractional ownership, transfer enables secondary market trading, dividends distributed via separate function
- `\bottomnote{This simplified contract shows the core pattern: tokens represent ownership shares, manager updates NAV, holders can transfer freely}`

**Frame 9: Fractionalization Mechanics**
- TikZ step-by-step visualization:
  - Asset: $10 million Manhattan apartment building
  - Step 1: SPV (LLC) acquires building
  - Step 2: 10,000 tokens minted (1 token = $1,000 = 0.01% ownership)
  - Step 3: Token sale (primary market -- platform like RealT)
  - Step 4: Secondary trading (DEX or regulated exchange, 24/7)
  - Step 5: Rental income: $50,000/month distributed proportionally
    - 100 tokens = $500/month in rent (5 tokens/year buyback equivalent)
  - Step 6: If building sells for $12M, each token redeemable for $1,200
- Comparison callout: Traditional real estate investment = $100K minimum; Tokenized = $50 minimum
- `\bottomnote{Fractionalization is the most transformative aspect of tokenization -- it turns illiquid assets into liquid, accessible investments}`

**Frame 10: Benefits of Tokenization**
- TikZ 6-benefit layout (each in a colored box):
  - 24/7 Global Markets (mlblue): Trade at midnight on Sunday. No market close. Cross-border access.
  - Fractional Ownership (mlgreen): $50 minimum vs $100K+ traditional. Democratized access.
  - Instant Settlement (mlorange): T+0 on-chain vs T+2 traditional equities, T+3 real estate.
  - Programmable Compliance (mlred): KYC/AML enforced by smart contract. Auto-dividend distribution.
  - Reduced Intermediaries (mlpurple): No transfer agents, fewer custodians, lower fees (0.1% vs 2-5%).
  - Transparent Ownership (mlgray): On-chain cap table. Real-time audit trail. Immutable records.
- `\bottomnote{McKinsey estimates tokenization could save financial institutions \$100-200B annually in back-office costs alone}`

**Frame 11: Challenges of Tokenization**
- Two-column:
  - Left: Technical Challenges
    - Oracle problem: how does the blockchain know the building's condition, occupancy, or sale price?
    - Smart contract risk: bugs can lock or drain tokenized assets
    - Scalability: high-value assets need robust, battle-tested chains
    - Interoperability: tokenized assets on different chains can't easily interact
  - Right: Legal & Regulatory Challenges
    - Legal recognition: does a token convey legal ownership? Varies by jurisdiction
    - Cross-border complexity: a US-tokenized building sold to a Japanese investor -- which laws apply?
    - Bankruptcy: if the SPV or platform goes bankrupt, what happens to token holders?
    - Tax reporting: capital gains, rental income, cross-border withholding
- TikZ bridge diagram: "On-chain token" <-- oracle gap --> "Off-chain reality"
- `\bottomnote{The oracle problem is fundamental: a blockchain can verify on-chain state perfectly, but cannot independently verify off-chain reality}`

**Frame 12: The Oracle Problem for RWA**
- TikZ detailed oracle flow:
  - On-chain world (left): smart contract holds token state, balances, compliance rules
  - Off-chain world (right): physical asset condition, legal status, appraisal value, rental payments
  - Bridge (center): Oracles (Chainlink, Pyth, API3)
    - Price feeds: asset valuation updates
    - Proof of reserves: attestations that backing exists
    - Event triggers: rental payment received, insurance claim filed
  - Trust assumption: oracle operator must be honest; multiple oracles reduce single-point-of-failure
  - Attestation types: automated (API data) vs manual (auditor reports)
- `\bottomnote{Unlike DeFi protocols that use on-chain price feeds, RWA oracles often require human attestation -- introducing trust assumptions}`

**Frame 13: Tokenization Market Map**
- TikZ ecosystem diagram (hub-and-spoke):
  - Center: Tokenized Assets
  - Platforms: Securitize, Centrifuge, RealT, Ondo Finance, Maple Finance, Backed Finance
  - Infrastructure: Chainlink (oracles), Fireblocks (custody), SWIFT (interoperability)
  - Blockchains: Ethereum (dominant for RWA), Polygon, Avalanche, Stellar
  - Regulation: SEC (US), MiCA (EU), MAS (Singapore), VARA (Dubai)
  - Standards: ERC-3643, ERC-20, ERC-721
- Color-coded by category, arrows showing relationships
- `\bottomnote{Ethereum dominates RWA tokenization with 60\%+ market share -- security, liquidity, and institutional trust drive this concentration}`

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 key takeaways, numbered, colored backgrounds)
  1. Tokenization digitizes ownership rights on a blockchain via legal wrappers (SPVs) and smart contracts
  2. Asset classes totaling $500T+ (real estate, bonds, commodities, credit, art) are candidates for tokenization
  3. ERC-20 (fungible), ERC-721 (unique), ERC-1155 (hybrid), and ERC-3643 (compliant) are the key token standards
  4. Fractionalization enables $50 minimums vs $100K+ traditional, unlocking global investor access
  5. The oracle problem and legal recognition are fundamental challenges bridging on-chain tokens to off-chain reality

#### SECTION 2: Stablecoins Deep Dive (Frames 15-25)

**Frame 15: Section 2 Divider**
- Title: `Section 2: Stablecoins Deep Dive`
- Subtitle: `Taxonomy, mechanics, reserves, risks, and the regulatory frontier`
- Learning items:
  - Stablecoin taxonomy: fiat-backed, crypto-backed, algorithmic, commodity-backed
  - USDT, USDC, and DAI mechanics in depth
  - Reserve attestation models and depeg risks
  - The Terra/Luna collapse and regulatory response

**Frame 16: Stablecoin Taxonomy**
- TikZ four-quadrant classification:
  - Quadrant 1 (mlblue): Fiat-Backed (centralized, reserve-backed)
    - USDT ($90B+), USDC ($30B+), TUSD, FDUSD
    - Mechanism: 1:1 reserves in bank accounts/T-bills
    - Risk: custodian failure, regulatory seizure, reserve opacity
  - Quadrant 2 (mlgreen): Crypto-Backed (decentralized, overcollateralized)
    - DAI ($5B+), LUSD ($300M+), sUSD
    - Mechanism: lock $150+ of crypto to mint $100 of stablecoin
    - Risk: black swan liquidation cascade, oracle failure
  - Quadrant 3 (mlred): Algorithmic (decentralized, no collateral)
    - UST ($0 -- collapsed), FRAX (hybrid), USDD
    - Mechanism: expand/contract supply via burn/mint
    - Risk: death spiral if confidence lost (proven by Terra)
  - Quadrant 4 (mlorange): Commodity-Backed (centralized, asset-backed)
    - PAXG ($500M+), XAUT ($400M+)
    - Mechanism: each token backed by physical gold in vault
    - Risk: custodian risk, audit frequency
- Market share annotation: fiat-backed = 90%+ of stablecoin market

**Frame 17: USDT (Tether) Mechanics**
- Two-column:
  - Left: How Tether works
    - Largest stablecoin: $90B+ market cap (as of 2024/2025)
    - Issuer: Tether Limited (British Virgin Islands)
    - Peg mechanism: authorized participants deposit USD, receive USDT; redeem USDT for USD
    - Reserve composition (from latest attestation):
      - ~85% US Treasury bills (improvement from 2021)
      - ~10% secured loans
      - ~5% other (BTC, precious metals)
    - Controversy history: 2019 NYAG investigation, undisclosed $850M Bitfinex loan
    - No full audit -- quarterly attestation by BDO Italia
  - Right: TikZ flow diagram:
    - Institutional depositor -> Tether -> USDT minted on Ethereum/Tron/Solana
    - Redemption flow: USDT burned -> USD returned
    - Reserve pool: Treasury bills, cash, secured loans
- `\bottomnote{Tether is the most systemically important stablecoin but also the most controversial -- \$90B+ in circulation, never fully audited}`

**Frame 18: USDC & Reserve Transparency**
- Two-column:
  - Left: How Circle/USDC works
    - Second largest: $30B+ market cap
    - Issuer: Circle (US-regulated money transmitter)
    - Reserves: ~80% short-term US Treasuries, ~20% cash at regulated banks
    - Monthly attestation by Deloitte (Big 4 auditor)
    - Regulated in US, EU (MiCA compliant), Singapore
    - March 2023 depeg: Silicon Valley Bank held $3.3B of reserves -- depeg to $0.87 during SVB collapse, recovered in 48 hours when Fed backstopped deposits
  - Right: TikZ comparison: USDT vs USDC
    - Market cap: USDT 3x larger
    - Attestation: quarterly (BDO) vs monthly (Deloitte)
    - Reserve composition: similar (mostly T-bills)
    - Regulation: minimal vs comprehensive
    - Transparency: opaque vs transparent
    - Depeg history: brief depegs vs SVB depeg
- `\bottomnote{The SVB depeg showed that even well-reserved stablecoins face risk from banking system failures -- diversification of reserves matters}`

**Frame 19: DAI & Crypto-Backed Mechanics**
- Two-column:
  - Left: MakerDAO/DAI architecture
    - Decentralized stablecoin: no single issuer
    - CDP (Collateralized Debt Position) / Vault mechanism:
      - Deposit ETH (or WBTC, stETH, etc.) as collateral
      - Mint DAI up to collateralization ratio (e.g., 150% for ETH)
      - Pay stability fee (interest) on outstanding DAI
      - If collateral ratio drops below threshold, liquidation auction
    - Governance: MKR token holders set parameters (rates, ratios, collateral types)
    - Peg stability module (PSM): allows 1:1 swap with USDC for peg maintenance
    - RWA vaults: $2B+ in real-world assets backing DAI (US Treasuries, commercial loans)
  - Right: TikZ vault diagram:
    - User deposits 1.5 ETH ($3,000) -> Vault contract -> Mints 2,000 DAI
    - Collateral ratio: 150% (healthy)
    - If ETH drops 40%: ratio falls below 150% -> Liquidation triggered
    - Liquidation: collateral sold at auction to repay DAI + penalty
- `\bottomnote{MakerDAO's pivot to RWA collateral is historic: DAI is now backed 40\%+ by real-world assets, blurring the line between DeFi and TradFi}`

**Frame 20: MakerDAO Vault Contract [FRAGILE] -- CODE FRAME 2**
- `\begin{frame}[fragile]{Collateralized Vault Contract}`
- Left column: Solidity snippet for simplified collateral vault
```solidity
// Simplified Collateral Vault
contract StablecoinVault {
    uint256 public constant
        MIN_RATIO = 150; // 150%
    mapping(address => uint256)
        public collateral;
    mapping(address => uint256)
        public debt;

    function deposit()
        external payable {
        collateral[msg.sender]
            += msg.value;
    }

    function borrow(uint256 amount)
        external {
        uint256 colValue =
            collateral[msg.sender]
            * getPrice() / 1e18;
        require(
            colValue * 100
            >= (debt[msg.sender]
            + amount) * MIN_RATIO,
            "Below min ratio"
        );
        debt[msg.sender] += amount;
        // Mint stablecoin to user
    }
}
```
- Right column: explanation of overcollateralization, collateral ratio calculation, liquidation threshold, stability fee accrual, governance parameters (MKR holders vote on MIN_RATIO, stability fee)

**Frame 21: The Terra/Luna Collapse**
- TikZ timeline with 4 phases:
  - Phase 1 (Pre-collapse, May 7 2022): UST at $1.00, LUNA at $80, TVL $18B, Anchor Protocol offering 20% APY on UST deposits. "Too good to be true?"
  - Phase 2 (Depeg begins, May 8-9): Large UST sells ($2B+) overwhelm liquidity pools. UST drops to $0.90. LUNA minted to absorb UST redemptions. Panic begins.
  - Phase 3 (Death spiral, May 10-12): LUNA hyperinflation (supply explodes from 350M to 6.5T). UST falls to $0.10. LUNA falls to $0.0001. Anchor TVL collapses from $18B to near zero.
  - Phase 4 (Aftermath): $40B+ market value destroyed. Contagion: 3AC, Celsius, Voyager, FTX dominoes. Do Kwon arrested (March 2023). Regulatory crackdown on algorithmic stablecoins.
- Red arrows showing cascading losses
- `\bottomnote{Terra/Luna was crypto's Lehman Brothers moment -- the death spiral proved that algorithmic stablecoins without real reserves are inherently fragile}`

**Frame 22: Stablecoin Reserve Models Compared**
- Full-width comparison table (booktabs):
  - Columns: Feature, USDT, USDC, DAI, PAXG
  - Rows: Type, Market Cap, Backing, Collateral Ratio, Auditor, Depeg History, Regulation, Chain Support, Risk Profile
  - USDT: Fiat-backed, $90B+, T-bills/cash/loans, 1:1, BDO Italia (quarterly), Brief depegs, Minimal, Ethereum/Tron/Solana, Custodian + opacity
  - USDC: Fiat-backed, $30B+, T-bills/cash, 1:1, Deloitte (monthly), SVB depeg $0.87, US regulated, Ethereum/Solana/Base, Banking system
  - DAI: Crypto-backed, $5B+, ETH/WBTC/RWA, 150%+, On-chain, Brief MCD migration, Decentralized, Ethereum, Oracle + liquidation
  - PAXG: Commodity-backed, $500M+, Physical gold, 1:1, Withum (monthly), None, NYDFS regulated, Ethereum, Custodian
- `\bottomnote{Each stablecoin model has a different risk profile -- there is no risk-free stablecoin, only different risk tradeoffs}`

**Frame 23: Stablecoin Market Dominance**
- Two-column:
  - Left: pgfplots stacked area chart showing stablecoin market cap growth 2019-2025
    - USDT dominant (green), USDC growing then plateauing (blue), DAI stable (orange), others (gray)
    - Key events annotated: DeFi Summer 2020, Terra collapse 2022, SVB 2023, Bitcoin ETF 2024
  - Right: Key statistics block
    - Total stablecoin market cap: $150B+ (2024/2025)
    - Daily settlement volume: $30-50B (rivaling traditional payment rails)
    - Annual on-chain settlement: $10T+ (comparable to major card networks)
    - USDT market share: ~60%, USDC: ~20%, DAI: ~3%, Others: ~17%
- `\bottomnote{Stablecoins are the most successful blockchain use case by adoption -- settling trillions annually with growing institutional and retail usage}`

**Frame 24: Stablecoin Regulation**
- TikZ regulatory landscape map:
  - European Union (mlblue): MiCA (Markets in Crypto-Assets, effective June 2024)
    - Stablecoin-specific rules (Title III: ARTs, Title IV: EMTs)
    - Reserve requirements: liquid, segregated, 1:1 backing
    - Redemption rights: token holders can redeem at par anytime
    - Ban on interest payments for e-money tokens (EMTs)
    - Market cap cap: $200M daily volume triggers enhanced requirements
  - United States (mlred): Fragmented, no comprehensive federal stablecoin law yet
    - Multiple bills proposed (Lummis-Gillibrand, GENIUS Act)
    - SEC, CFTC, OCC, state regulators all claim jurisdiction
    - State-level: NYDFS regulates Paxos; state money transmitter licenses
  - Singapore / Dubai / Hong Kong (mlgreen): Innovation-friendly frameworks
    - MAS: Payment Services Act covers stablecoins
    - VARA: Dubai regulatory framework
    - HKMA: sandbox for stablecoin issuers
- `\bottomnote{MiCA is the world's first comprehensive crypto regulation -- its stablecoin rules set the global template for reserve and redemption requirements}`

**Frame 25: Section 2 Summary**
- 5-point summary boxes
  1. Stablecoins are the largest RWA category ($150B+ market cap) -- fiat-backed dominate at 90%+ market share
  2. USDT (largest, least transparent), USDC (regulated, Deloitte-audited), DAI (decentralized, overcollateralized) serve different needs
  3. The Terra/Luna collapse ($40B destroyed) proved algorithmic stablecoins without real reserves are fatally flawed
  4. Reserve quality matters: the SVB depeg showed even well-backed stablecoins face banking system contagion risk
  5. MiCA (EU) sets the regulatory template; US regulation remains fragmented across multiple agencies

#### SECTION 3: Security Tokens & Compliance (Frames 26-36)

**Frame 26: Section 3 Divider**
- Title: `Section 3: Security Tokens \& Compliance`
- Subtitle: `Legal classification, the Howey test, ERC-3643, and the regulated token economy`
- Learning items:
  - Security vs utility token classification and the Howey test
  - SEC enforcement actions and regulatory precedents
  - ERC-3643 (T-REX) standard for compliant security tokens
  - Regulated exchanges, legal wrappers, and on-chain KYC/AML

**Frame 27: Security vs Utility Tokens**
- TikZ decision tree:
  - Root: "Is this token a security?"
  - Branch 1: Does the purchaser invest money? (Yes -> continue, No -> likely utility)
  - Branch 2: Is there a common enterprise? (Yes -> continue, No -> likely utility)
  - Branch 3: Is there an expectation of profits? (Yes -> continue, No -> likely utility)
  - Branch 4: Are profits derived from efforts of others? (Yes -> SECURITY TOKEN, No -> likely utility)
  - Security path leads to: SEC registration required OR exemption (Reg D, Reg S, Reg A+)
  - Utility path leads to: May still be regulated depending on jurisdiction
  - Gray area callout: "Many tokens fall in a gray area -- the SEC has sued projects claiming their tokens ARE securities"
- `\bottomnote{The Howey test dates from 1946 (SEC v. W.J. Howey Co.) -- it was designed for orange grove investments but now determines crypto classification}`

**Frame 28: SEC Enforcement & Precedents**
- TikZ case timeline:
  - 2017: The DAO Report -- SEC declares DAO tokens are securities (no enforcement, but warning shot)
  - 2018: SEC fines EtherDelta (unregistered exchange), charges various ICOs
  - 2020: SEC sues Ripple/XRP ($1.3B case) -- alleges XRP is an unregistered security
  - 2023: Ripple partial ruling -- programmatic sales NOT securities, institutional sales ARE securities
  - 2023: SEC sues Coinbase and Binance -- alleges multiple tokens are securities (SOL, ADA, MATIC listed)
  - 2024: SEC approves Bitcoin and Ethereum ETFs -- implicitly NOT securities (commodities)
  - 2025: Regulatory clarity evolving -- FIT21 and market structure bills advancing
- Key insight box: "The SEC uses enforcement as regulation -- sue first, clarify later"
- `\bottomnote{The Ripple ruling created a split: programmatic exchange sales may not be securities, but direct institutional sales are -- a nuanced precedent}`

**Frame 29: The Howey Test in Practice**
- Two-column:
  - Left: Passes Howey Test (IS a security):
    - Token sale funding a project development team
    - Tokens with profit-sharing from company revenue
    - Tokens whose value depends on management team efforts
    - Tokenized real estate with rental yield
    - Tokenized equity or debt instruments
    - Examples: Many 2017 ICO tokens, LBRY Credits (SEC won)
  - Right: Fails Howey Test (NOT a security):
    - Decentralized network tokens where no single party drives value
    - Utility tokens providing access to a live, functioning product
    - Governance tokens with no profit expectation (debatable)
    - Sufficiently decentralized tokens (the "Hinman test" -- Ethereum)
    - Bitcoin (commodity per CFTC)
    - Examples: BTC, ETH (per SEC guidance)
  - Center: Gray zone -- most tokens live here; classification depends on specific facts and circumstances
- `\bottomnote{The distinction often comes down to "sufficient decentralization" -- if no single entity drives the token's value, it may escape security classification}`

**Frame 30: On-Chain KYC/AML Architecture**
- TikZ identity flow diagram:
  - Layer 1: User provides KYC documents (passport, proof of address) to Identity Provider
  - Layer 2: Identity Provider (Securitize ID, Fractal, Civic) verifies and issues on-chain attestation
  - Layer 3: On-chain Identity Registry (smart contract) stores verified claims:
    - isVerified(address) -> bool
    - getCountry(address) -> countryCode
    - isAccredited(address) -> bool
  - Layer 4: Token contract checks Identity Registry BEFORE every transfer
    - Transfer: sender verified? -> receiver verified? -> country restrictions? -> investment limit?
    - If all pass -> transfer executes
    - If any fail -> transfer reverts
  - Annotations: ERC-3643 implements this entire stack
- `\bottomnote{On-chain KYC turns compliance from a manual process into programmable logic -- every transfer is automatically checked against compliance rules}`

**Frame 31: ERC-3643 Security Token [FRAGILE] -- CODE FRAME 3**
- `\begin{frame}[fragile]{ERC-3643 Compliant Transfer}`
- Left column: Solidity snippet for simplified ERC-3643 transfer with identity check
```solidity
// Simplified ERC-3643 Token
contract SecurityToken {
    IIdentityRegistry public
        identityRegistry;
    ICompliance public compliance;

    mapping(address => uint256)
        public balanceOf;

    function transfer(
        address to,
        uint256 amount
    ) external returns (bool) {
        require(
            identityRegistry
                .isVerified(msg.sender),
            "Sender not verified"
        );
        require(
            identityRegistry
                .isVerified(to),
            "Receiver not verified"
        );
        require(
            compliance.canTransfer(
                msg.sender, to, amount
            ),
            "Compliance check failed"
        );
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
```
- Right column: explanation of identity registry checks, compliance module (country restrictions, investor limits, lockup periods), how ERC-3643 wraps ERC-20 with compliance layer, real-world deployment by Tokeny Solutions (500+ deployments)

**Frame 32: Transfer Restriction Patterns**
- TikZ grid of compliance rules (6 panels):
  - Country Restrictions: block transfers to/from sanctioned countries (OFAC list). TikZ: world map with red X on blocked countries.
  - Investor Limits: maximum number of token holders (e.g., Reg D 506(c) = accredited investors only, max 2000 holders before SEC reporting). Counter diagram.
  - Lockup Periods: tokens locked for X months after issuance (vesting schedule). Timeline with lock icons.
  - Transfer Volume Limits: maximum transfer size per period (anti-money laundering). Threshold bar chart.
  - Accreditation Check: only accredited investors ($1M+ net worth or $200K+ income) can hold. Checkbox diagram.
  - Forced Transfer: issuer can forcibly transfer tokens (court order, regulatory action, lost keys recovery). Arrow with lock override icon.
- `\bottomnote{These restrictions exist in traditional securities too -- tokenization makes them programmable and automatic rather than manual and error-prone}`

**Frame 33: Regulated Security Token Exchanges**
- Two-column:
  - Left: Exchange landscape
    - tZERO (US): Overstock-backed, SEC-registered ATS (Alternative Trading System). Trades tokenized equity, real estate, digital securities.
    - Securitize Markets (US): SEC-registered broker-dealer and ATS. Largest platform by number of issuances (500+). End-to-end: issuance + compliance + trading.
    - INX (Israel/US): SEC-registered security token exchange. First SEC-registered IPO on blockchain.
    - SIX Digital Exchange (Switzerland): FINMA-regulated. First fully regulated digital asset exchange by traditional exchange operator.
    - Archax (UK): FCA-regulated. Focused on institutional investors.
  - Right: TikZ comparison: Traditional Exchange vs Security Token Exchange
    - Traditional: T+2 settlement, limited hours (9:30-4:00 ET), minimum $25K+ (often), paper-based cap table
    - Security Token: T+0 settlement, 24/7 trading (potentially), $50+ minimums, on-chain cap table
- `\bottomnote{The security token exchange landscape is still early -- combined daily volume across all STO exchanges is tiny compared to traditional exchanges}`

**Frame 34: Legal Wrappers for Tokenized Assets**
- TikZ legal structure diagram:
  - Pattern 1 (most common): SPV Model
    - Real asset owned by LLC/SPV
    - SPV shares tokenized as ERC-3643 tokens
    - Token holders are legal shareholders of SPV
    - SPV operating agreement governs rights
  - Pattern 2: Trust Model
    - Asset held in trust (e.g., Delaware Statutory Trust)
    - Trust units tokenized
    - Trustee manages asset, distributes returns
  - Pattern 3: DAO Wrapper
    - DAO holds assets through legal entity (Wyoming DAO LLC, Marshall Islands DAO)
    - Governance tokens control asset management decisions
    - Emerging -- legal recognition varies by jurisdiction
  - Key insight: "The token is NOT the asset -- the token represents a CLAIM on the legal entity that owns the asset"
- `\bottomnote{Without a proper legal wrapper, a token is just code -- the legal structure is what gives the token holder enforceable rights to the underlying asset}`

**Frame 35: Tokenized Securities vs Traditional Securities**
- Full-width comparison table (booktabs):
  - Columns: Dimension, Traditional Securities, Tokenized Securities
  - Rows (12): Settlement Time, Trading Hours, Minimum Investment, Custody, Dividend Distribution, Cap Table, Compliance, Cross-Border, Issuance Cost, Secondary Liquidity, Investor Eligibility, Regulatory Status
  - Traditional: T+2 days, 9:30-4:00 M-F, Often $10K+, Custodian bank, Wire transfer (5-10 days), Paper/spreadsheet, Manual (lawyers, transfer agents), Complex (different depositories), $500K-$5M, Established exchanges, Accredited + retail (post-IPO), Well-established
  - Tokenized: T+0 (instant), 24/7 (potentially), $50+, Self-custody or institutional wallet, Smart contract (instant), On-chain (real-time), Automated (ERC-3643), Native (blockchain is global), $50K-$500K, Early-stage exchanges, Mostly accredited (for now), Evolving
- `\bottomnote{Tokenized securities are NOT yet strictly better -- regulatory friction, liquidity, and institutional trust still favor traditional markets for most investors}`

**Frame 36: Section 3 Summary**
- 5-point summary boxes
  1. The Howey test determines if a token is a security: investment of money + common enterprise + profit expectation + from others' efforts
  2. SEC enforces through litigation -- the Ripple ruling created nuance (programmatic vs institutional sales)
  3. ERC-3643 adds identity verification and transfer restrictions to ERC-20, enabling on-chain regulatory compliance
  4. Legal wrappers (SPVs, trusts, DAO LLCs) bridge the gap between on-chain tokens and off-chain legal rights
  5. Regulated security token exchanges exist (tZERO, Securitize) but volumes remain tiny compared to traditional markets

#### SECTION 4: Real Estate & Bond Tokenization (Frames 37-47)

**Frame 37: Section 4 Divider**
- Title: `Section 4: Real Estate \& Bond Tokenization`
- Subtitle: `Platforms, institutional adoption, yield-bearing tokens, and real-world case studies`
- Learning items:
  - Real estate tokenization mechanics and platforms (RealT, Centrifuge)
  - Bond tokenization by institutions (JPMorgan, Siemens, EIB)
  - Private credit markets on-chain (Maple Finance, Goldfinch)
  - Yield-bearing tokens: tokenized T-bills and institutional products

**Frame 38: Real Estate Tokenization Architecture**
- TikZ end-to-end flow:
  - Step 1: Property acquisition -- identify property, conduct due diligence, appraise value ($2M duplex in Detroit)
  - Step 2: Legal structuring -- create SPV (LLC), transfer property ownership to SPV
  - Step 3: Token issuance -- deploy ERC-20 or ERC-3643 contract, mint tokens (e.g., 2,000 tokens at $1,000 each)
  - Step 4: Primary sale -- offer tokens to verified investors via platform (KYC required)
  - Step 5: Property management -- tenant pays rent, property manager maintains building
  - Step 6: Yield distribution -- smart contract distributes rental income to token holders proportionally
  - Step 7: Secondary trading -- token holders can sell on secondary market for liquidity
  - Step 8: Exit event -- property sold, proceeds distributed, tokens burned
- Annotation: "The legal structure ensures token = legal ownership share"
- `\bottomnote{Real estate tokenization combines PropTech, DeFi, and securities law -- each step requires expertise in legal, technical, and regulatory domains}`

**Frame 39: RealT Platform Deep Dive**
- Two-column:
  - Left: RealT details
    - Pioneer in real estate tokenization (launched 2019)
    - Properties: US residential (Detroit, Chicago, Cleveland, etc.)
    - Blockchain: Gnosis Chain (formerly xDAI) -- low fees, fast transactions
    - Token standard: ERC-20 (each property = separate token)
    - Minimum investment: ~$50 per token
    - Rental yield: distributed weekly in USDC via smart contract
    - Average yield: 8-12% APY (rental income)
    - Portfolio: 500+ properties tokenized
    - DeFi integration: RealT tokens as collateral on RMM (RealT Money Market)
  - Right: TikZ RealT property card:
    - Address: 123 Main St, Detroit MI
    - Property value: $60,000
    - Token price: $50/token, 1200 tokens
    - Weekly rent: $150 (distributed proportionally)
    - Annual yield: ~10% APY
    - Occupancy: 95%
    - Last NAV update: 2024-Q4
- `\bottomnote{RealT is the largest tokenized real estate platform by number of properties -- 500+ US residential properties available to global investors for \$50+}`

**Frame 40: Centrifuge Protocol**
- Two-column:
  - Left: Centrifuge architecture
    - Tokenizes real-world credit (NOT just real estate):
      - Trade finance invoices
      - Revenue-based financing
      - US Treasury bills
      - Mortgage-backed loans
      - Warehouse credit lines
    - Centrifuge Chain: Substrate-based blockchain (connects to Ethereum via bridge)
    - Pool structure: Senior tranche (lower risk, lower yield) + Junior tranche (higher risk, higher yield)
    - Tinlake: the DeFi lending protocol for Centrifuge assets
    - Major integration: MakerDAO uses Centrifuge pools as RWA collateral ($200M+)
    - TVL: $300M+
  - Right: TikZ pool tranche diagram:
    - Asset originator -> Assets -> Centrifuge Pool
    - Pool splits into: Senior Tranche (DROP tokens, 4-6% APY, first loss protection) + Junior Tranche (TIN tokens, 10-15% APY, absorbs first losses)
    - Investor chooses risk/return tradeoff
- `\bottomnote{Centrifuge pioneered structured credit on-chain -- tranching allows different risk appetites, exactly like traditional asset-backed securities}`

**Frame 41: Maple Finance & On-Chain Credit**
- Two-column:
  - Left: Maple Finance details
    - Institutional undercollateralized lending on-chain
    - Pool delegates (credit experts) assess borrower creditworthiness
    - Borrowers: crypto market makers, trading firms, fintech companies
    - Lending: USDC or wETH, fixed-term loans
    - History: launched 2021, $2B+ total lending volume
    - Post-2022 crisis: bad debts from Alameda Research, Orthogonal Trading defaults
    - Recovery: pivoted to institutional-grade underwriting, over-collateralized pools
    - Maple Direct: compliant lending to institutions
  - Right: TikZ lending flow:
    - Lenders (USDC) -> Maple Pool -> Pool Delegate (credit assessment) -> Borrower (market maker)
    - Repayment: Borrower -> interest + principal -> Pool -> Lenders
    - Default: Pool Delegate absorbs first loss (skin in game) -> Junior tranche absorbs next
- `\bottomnote{Maple's 2022 defaults (\$50M+) showed that undercollateralized on-chain lending carries real credit risk -- just like traditional banking}`

**Frame 42: Bond Tokenization Case Studies**
- TikZ case study cards (4 cases):
  - Case 1 (mlblue): JPMorgan Onyx
    - Tokenized repo transactions ($1B+ daily volume)
    - Intraday settlement (vs overnight traditional)
    - JPM Coin for instant payment settlement
    - Onyx Digital Assets: tokenized T-bills, money market funds
  - Case 2 (mlgreen): Siemens Digital Bond
    - $64M bond issued on Polygon (June 2023)
    - 1-year maturity, registered under German electronic securities law
    - First major corporate bond on public blockchain
  - Case 3 (mlorange): European Investment Bank
    - EUR 100M bond on Ethereum (2021, first), EUR 50M on Project Venus with BIS (2023)
    - Working with BNP Paribas, Goldman Sachs, Societe Generale
  - Case 4 (mlred): World Bank (Bond-i)
    - AUD 110M bond on Ethereum (2018) -- first blockchain bond by multilateral development bank
    - Managed by Commonwealth Bank of Australia
- `\bottomnote{Bond tokenization is the fastest-growing institutional RWA category -- savings come from instant settlement, 24/7 operations, and automated coupon payments}`

**Frame 43: Yield-Bearing Token Contract [FRAGILE] -- CODE FRAME 4**
- `\begin{frame}[fragile]{Yield-Bearing Token (Tokenized T-Bill)}`
- Left column: Solidity snippet for simplified yield-bearing token
```solidity
// Simplified Yield-Bearing Token
contract TokenizedTBill {
    string public name =
        "Tokenized US T-Bill";
    uint256 public totalShares;
    uint256 public totalAssets;

    mapping(address => uint256)
        public shares;

    function deposit(
        uint256 usdcAmount
    ) external {
        uint256 newShares =
            totalAssets == 0
            ? usdcAmount
            : usdcAmount
              * totalShares
              / totalAssets;
        shares[msg.sender] += newShares;
        totalShares += newShares;
        totalAssets += usdcAmount;
        // Transfer USDC from user
    }

    function rebase(
        uint256 yieldAmount
    ) external onlyManager {
        totalAssets += yieldAmount;
        // Share price increases
    }
}
```
- Right column: explanation of rebasing vault pattern (ERC-4626 compatible), how yield accrues (manager updates totalAssets as T-bills earn interest), share price = totalAssets / totalShares increases over time, examples: Ondo USDY ($5.2% APY), Franklin BENJI ($5.0% APY), MakerDAO sDAI

**Frame 44: Yield-Bearing Token Landscape**
- TikZ product comparison grid:
  - Ondo USDY (mlblue): Tokenized T-bills + bank deposits, $300M+ AUM, 5.2% APY, Ethereum/Solana/Mantle, minimum $500, accredited investors only
  - Franklin BENJI (mlgreen): Franklin Templeton OnChain US Gov Money Fund, $400M+ AUM, 5.0% APY, Stellar/Polygon, institutional, first US-registered fund on public blockchain
  - BlackRock BUIDL (mlorange): BlackRock USD Institutional Digital Liquidity Fund, $500M+ AUM, ~5% APY, Ethereum, $5M minimum, institutional only
  - MakerDAO sDAI (mlpurple): DAI Savings Rate, $2B+ deposits, 5-8% APY (variable), Ethereum, no minimum, permissionless
  - Mountain USDM (mlred): Yield-bearing stablecoin, $200M+, ~5% APY, Ethereum, permissionless
- Key stat: "$2B+ in tokenized treasuries alone (excluding sDAI)"
- `\bottomnote{Yield-bearing tokens brought the "risk-free rate" on-chain -- DeFi users can now earn Treasury yields without leaving the blockchain ecosystem}`

**Frame 45: Institutional Adoption Drivers**
- TikZ four-pillar diagram:
  - Pillar 1: Efficiency (mlblue)
    - T+0 settlement vs T+2 (saves $7B+ annually in collateral costs)
    - 24/7 operations (no market close, no settlement delay)
    - Automated coupon/dividend payments via smart contract
  - Pillar 2: Transparency (mlgreen)
    - Real-time on-chain audit trail
    - Automated compliance reporting
    - Instant cap table visibility
  - Pillar 3: Access (mlorange)
    - Fractional ownership enables new investor pools
    - Global distribution without local custodians
    - Lower issuance costs ($50K vs $500K+ traditional)
  - Pillar 4: Programmability (mlpurple)
    - Programmable compliance (ERC-3643)
    - Automated corporate actions (dividends, splits, buybacks)
    - Composability with DeFi (collateral, lending, trading)
- `\bottomnote{The institutional case for tokenization is fundamentally about efficiency -- Goldman Sachs estimates tokenization could save \$7B+ in annual collateral costs}`

**Frame 46: Private Credit On-Chain**
- Two-column:
  - Left: On-chain credit protocols
    - Goldfinch: emerging market lending (India, Kenya, SE Asia), $100M+ originated, borrowers are fintech companies lending to local businesses
    - Credix: Latin American credit markets, trade finance and consumer lending
    - Clearpool: institutional permissioned lending pools
    - TrueFi: uncollateralized lending to vetted institutions
    - Total on-chain private credit: $500M+ active, $4B+ cumulative
    - Default rates: historically 2-5% (similar to traditional private credit)
  - Right: TikZ credit flow:
    - DeFi lender (USDC) -> Protocol -> Credit assessment -> Real-world borrower (fintech)
    - Borrower lends to: local businesses, consumers, trade finance
    - Repayment: borrower -> protocol -> lender + yield (8-15% APY)
    - Risk: borrower default, currency risk, regulatory risk
- `\bottomnote{On-chain private credit brings DeFi yields to real-economy lending -- but carries real credit risk, as 2022 defaults demonstrated}`

**Frame 47: Section 4 Summary**
- 5-point summary boxes
  1. Real estate tokenization (RealT, 500+ properties) enables $50 minimum investments with weekly rental yield distribution
  2. Centrifuge and Maple Finance bring structured credit on-chain with tranche-based risk/return profiles
  3. Major institutions are active: JPMorgan ($1B+ daily repo), Siemens ($64M bond on Polygon), EIB (EUR 100M on Ethereum)
  4. Yield-bearing tokens (BUIDL, USDY, BENJI) brought the risk-free rate on-chain, attracting $2B+ in tokenized treasuries
  5. Institutional adoption is driven by efficiency (T+0 settlement), transparency (on-chain audit), and programmability (automated compliance)

#### SECTION 5: RWA Ecosystem & Future (Frames 48-55)

**Frame 48: Section 5 Divider**
- Title: `Section 5: RWA Ecosystem \& Future`
- Subtitle: `Market projections, regulatory landscape, interoperability, and the future of tokenized finance`
- Learning items:
  - RWA market size projections ($10-16T by 2030)
  - BlackRock BUIDL and Ondo Finance as category leaders
  - MakerDAO's RWA pivot and DeFi-TradFi convergence
  - Regulatory challenges and the path to mainstream adoption

**Frame 49: RWA Market Size Projections**
- Two-column:
  - Left: pgfplots bar chart showing market projections by source:
    - BCG/ADDX (2022 report): $16.1T tokenized by 2030
    - McKinsey (2023 report): $5T by 2030 (conservative), $10T (base case)
    - Citibank (2023): $4T-$5T by 2030
    - Current (2024/2025): ~$5B tokenized (excl. stablecoins)
    - Growth multiple: 1000-3000x in 5-6 years
  - Right: Breakdown by asset class (projected 2030):
    - Tokenized funds & bonds: $5T (40%)
    - Tokenized real estate: $3T (25%)
    - Tokenized trade finance: $2T (15%)
    - Tokenized securities: $1T (8%)
    - Other (art, IP, carbon, commodities): $1.5T (12%)
- `\bottomnote{Even conservative estimates project 1000x growth -- the question is not if tokenization will happen, but how fast regulation and infrastructure enable it}`

**Frame 50: BlackRock BUIDL Fund**
- Two-column:
  - Left: BUIDL details
    - Product: BlackRock USD Institutional Digital Liquidity Fund
    - Asset: Short-term US Treasury bills
    - Blockchain: Ethereum (primary), expanding to Avalanche, Polygon, Optimism, Arbitrum via Securitize
    - AUM: $500M+ (largest tokenized fund)
    - Minimum: $5M (institutional)
    - Yield: ~5% APY (passes through T-bill yield)
    - Token: daily NAV rebase, instant transfers
    - Partners: Securitize (platform), BNY Mellon (custody), PwC (audit)
    - Significance: BlackRock = $10T AUM, world's largest asset manager, validates tokenization
  - Right: TikZ BUIDL architecture:
    - Investor deposits USDC -> Securitize (KYC) -> BUIDL tokens minted
    - BlackRock invests in T-bills via BNY Mellon
    - Yield accrues daily -> token value increases
    - Redemption: BUIDL -> USDC (same-day)
    - DeFi composability: BUIDL as collateral on Aave, Compound (planned)
- `\bottomnote{When the world's largest asset manager (\$10T AUM) launches a tokenized fund on Ethereum, it signals institutional conviction that blockchain is the future of finance}`

**Frame 51: Ondo Finance**
- Two-column:
  - Left: Ondo products
    - USDY: yield-bearing stablecoin backed by T-bills and bank deposits, 5.2% APY, $300M+
    - OUSG: tokenized short-term US government bonds
    - Multi-chain: Ethereum, Solana, Mantle, Sui, Aptos
    - Ondo Global Markets: planned tokenized equities and ETFs
    - Flux Finance: DeFi lending protocol for tokenized treasuries
    - Investment: backed by Pantera, Coinbase Ventures, Founders Fund
    - Regulatory approach: Reg D/Reg S exemptions, KYC required
  - Right: TikZ Ondo ecosystem:
    - Traditional finance (T-bills, bonds) -> Ondo -> On-chain tokens (USDY, OUSG)
    - DeFi integration: USDY as collateral, OUSG in Flux lending
    - Cross-chain bridging: Ondo tokens on 5+ chains
    - Future: tokenized equities (Ondo Global Markets)
- `\bottomnote{Ondo is the bridge between TradFi yield and DeFi composability -- its multi-chain approach makes Treasury yields accessible across the crypto ecosystem}`

**Frame 52: MakerDAO's RWA Pivot**
- Two-column:
  - Left: MakerDAO (now Sky) RWA journey
    - 2020: First RWA collateral (Centrifuge assets)
    - 2022: $500M allocated to US Treasuries (via Monetalis Clydesdale)
    - 2023: RWA allocation reaches $2B+ (largest DeFi-to-TradFi bridge)
    - 2024: RWA represents 40%+ of DAI backing
    - Collateral types:
      - US Treasury bills ($1.5B+ via BlockTower, Monetalis)
      - Centrifuge pools (trade finance, real estate)
      - Coinbase USDC institutional custody
    - Revenue: RWA vaults generate 60%+ of MakerDAO's revenue
    - Controversy: centralization concerns -- DAI now depends heavily on TradFi assets
  - Right: TikZ DAI backing pie chart:
    - Crypto collateral: 45% (ETH, WBTC, stETH)
    - RWA / US Treasuries: 40%
    - PSM (USDC 1:1): 10%
    - Other: 5%
- `\bottomnote{MakerDAO's RWA pivot is the most significant DeFi-TradFi convergence event -- \$2B+ in Treasury bills backing a decentralized stablecoin}`

**Frame 53: Regulatory Challenges & Legal Gaps**
- TikZ four-challenge layout:
  - Challenge 1 (mlred): Jurisdictional Fragmentation
    - A token issued in Singapore, traded in EU, held by US investor -- which law applies?
    - No global standard for tokenized securities
    - MiCA (EU) vs SEC (US) vs MAS (Singapore) vs VARA (Dubai) -- all different rules
  - Challenge 2 (mlorange): Legal Enforceability
    - Does a token convey LEGAL ownership? Only if the legal wrapper is properly structured.
    - Bankruptcy priority: if SPV goes bankrupt, are token holders secured creditors?
    - Smart contract bugs: who is liable if the distribution contract has a bug?
  - Challenge 3 (mlblue): Cross-Border Settlement
    - KYC/AML standards differ by country
    - Tax withholding on cross-border dividends
    - Currency conversion and FX risk for international investors
  - Challenge 4 (mlpurple): The Oracle Problem (Revisited)
    - Physical asset can deteriorate, be damaged, or change status without blockchain update
    - Who ensures the building hasn't burned down? Who updates the oracle?
    - Insurance, auditing, and dispute resolution remain off-chain
- `\bottomnote{Regulation is the biggest barrier to RWA growth -- technology is ready, legal frameworks are not, and fragmentation across jurisdictions creates friction}`

**Frame 54: TradFi-DeFi Convergence**
- TikZ convergence diagram:
  - Left side: Traditional Finance (moving right)
    - Banks adopting blockchain (JPMorgan Onyx, Goldman Sachs GS DAP)
    - SWIFT testing tokenized asset settlement (12+ bank pilot, 2024)
    - Asset managers launching tokenized funds (BlackRock, Franklin Templeton, WisdomTree)
    - Central banks exploring tokenized CBDCs and wholesale settlement
  - Right side: DeFi (moving left)
    - MakerDAO adding T-bill collateral
    - Aave considering RWA as collateral
    - Centrifuge, Ondo bridging to institutional credit
    - Chainlink CCIP enabling cross-chain institutional transfers
  - Center: Convergence zone
    - Compliant DeFi (permissioned pools within DeFi protocols)
    - Institutional DeFi (Aave Arc, Compound Treasury, Maple Direct)
    - Regulated on-chain exchanges (Securitize, tZERO)
  - Future vision: "Programmable, compliant, 24/7 financial markets"
- `\bottomnote{The convergence is bidirectional: TradFi is coming to blockchain AND DeFi is becoming regulated -- the middle ground is "institutional DeFi"}`

**Frame 55: Key Takeaways and Course Summary**
- TikZ 5-box summary (matching L2 Frame 55 style):
  - Box 1 (mlblue): Tokenization Fundamentals -- tokenization digitizes asset ownership via blockchain + legal wrappers; ERC-3643 enables compliant security tokens
  - Box 2 (mlpurple): Stablecoins -- $150B+ market, fiat-backed dominates; Terra/Luna proved algorithmic models are fatally flawed; MiCA sets regulatory template
  - Box 3 (mlgreen): Security Tokens & Compliance -- Howey test determines classification; on-chain KYC/AML via identity registries; SPVs bridge legal and digital worlds
  - Box 4 (mlorange): Real Estate & Bonds -- RealT (500+ properties), JPMorgan ($1B+ daily), BlackRock BUIDL ($500M+); yield-bearing tokens bring risk-free rate on-chain
  - Box 5 (mlred): RWA Future -- $10-16T projected by 2030; TradFi and DeFi converging; regulation is the biggest barrier; institutional conviction is accelerating
- Teal teaser bar: `Next: Advanced topics in DeFi-TradFi integration, CBDC design, and cross-chain institutional infrastructure`

**Acceptance Criteria (Task 4):**
- [ ] Exactly 55 frames with correct numbering
- [ ] 5 sections with divider and summary frames
- [ ] Exactly 4 `[fragile]` frames with lstlisting (Frames ~8, ~20, ~31, ~43)
- [ ] Preamble matches layer2_scaling.tex exactly (lines 1-52)
- [ ] All TikZ multi-line nodes have `align=center`
- [ ] No `\foreach` with `/` multi-variable syntax
- [ ] No parameterized styles with `#1`
- [ ] No reserved style names (diamond, step, text, signal)
- [ ] `\bottomnote` on every frame
- [ ] Compiles with pdflatex without errors

---

### TASK 5: Quiz RW-1 (`quiz/quiz_rw_part1.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz RW-1: Tokenization Fundamentals`
- 20 questions covering Section 1 topics:
  - What is tokenization and its core process (Q1-Q3)
  - Tokenizable asset classes and market sizes (Q4-Q6)
  - Token standards: ERC-20, ERC-721, ERC-1155, ERC-3643 (Q7-Q10)
  - Fractionalization mechanics and benefits (Q11-Q13)
  - Benefits of tokenization (24/7 markets, settlement, access) (Q14-Q16)
  - Challenges: oracle problem, legal recognition, interoperability (Q17-Q19)
  - SPV and legal wrapper concepts (Q20)
- Format: A/B/C/D multiple choice with explanations
- **Nav:** Dashboard + GitHub links ONLY (NO prev/next inter-quiz navigation). Copy quiz_l2_part1.html nav pattern.
- Copy CSS/JS structure from quiz_l2_part1.html exactly
- CSS variable: `--quiz-accent: #8b5cf6` (violet, same as existing template)

**Acceptance Criteria:**
- [ ] KaTeX v0.16.9 linked
- [ ] CSS variables match template
- [ ] 3-column grid layout
- [ ] 20 questions with JSON data
- [ ] All questions have correct answer and explanation
- [ ] Renders correctly in browser

---

### TASK 6: Quiz RW-2 (`quiz/quiz_rw_part2.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz RW-2: Stablecoins Deep Dive`
- 20 questions covering Section 2 topics:
  - Stablecoin taxonomy and classification (Q1-Q3)
  - USDT mechanics, reserves, and controversies (Q4-Q6)
  - USDC mechanics and SVB depeg event (Q7-Q9)
  - DAI, MakerDAO, overcollateralization, CDPs (Q10-Q13)
  - Terra/Luna collapse mechanics and aftermath (Q14-Q16)
  - Stablecoin market dominance and usage statistics (Q17-Q18)
  - Regulatory landscape: MiCA, US stablecoin legislation (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 7: Quiz RW-3 (`quiz/quiz_rw_part3.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz RW-3: Security Tokens & Compliance`
- 20 questions covering Section 3 topics:
  - Security vs utility token classification (Q1-Q2)
  - Howey test: four prongs and application (Q3-Q5)
  - SEC enforcement actions and Ripple case (Q6-Q8)
  - ERC-3643 standard and on-chain KYC/AML (Q9-Q12)
  - Transfer restrictions and compliance patterns (Q13-Q15)
  - Regulated security token exchanges (tZERO, Securitize) (Q16-Q17)
  - Legal wrappers: SPVs, trusts, DAO LLCs (Q18-Q19)
  - Tokenized vs traditional securities comparison (Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 8: Quiz RW-4 (`quiz/quiz_rw_part4.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz RW-4: Real Estate, Bonds & RWA Future`
- 20 questions covering Sections 4-5 topics:
  - Real estate tokenization mechanics and RealT (Q1-Q3)
  - Centrifuge, Maple Finance, and on-chain credit (Q4-Q6)
  - Bond tokenization: JPMorgan, Siemens, EIB case studies (Q7-Q9)
  - Yield-bearing tokens: BUIDL, USDY, BENJI (Q10-Q12)
  - RWA market size projections and growth drivers (Q13-Q14)
  - BlackRock BUIDL and Ondo Finance (Q15-Q16)
  - MakerDAO RWA pivot and DeFi-TradFi convergence (Q17-Q18)
  - Regulatory challenges and future outlook (Q19-Q20)
- **Nav:** Dashboard + GitHub links ONLY. Copy template nav.

**Acceptance Criteria:** Same as Task 5.

---

### TASK 9: GitHub Pages Update (`index.html`)
**Priority:** HIGH | **Complexity:** LOW

#### Changes Required

**1. Add d11 CSS class (after d10 styles, line 100):**
Insert AFTER line 100 (`.d10 summary{border-left:3px solid #ec4899}`), BEFORE the `.lec-grid` rule (line 101):
```css
.section-head.d11 span{background:#14b8a6}
.d11 summary{border-left:3px solid #14b8a6}
```

**2. Add RW sidebar links (after L2 entries, before `</details>` at line 187):**
Insert AFTER line 186 (`<a href="#sl-l2-main">L2 Technical Lecture</a>`), BEFORE `</details>`:
```html
<a href="#sl-rw-mini">Mini-Lecture: RWA & Tokenization</a>
<a href="#sl-rw-intro">RW INTRO Preview</a>
<a href="#sl-rw-pre">RW Pre-Class Handout</a>
<a href="#sl-rw-main">RW Technical Lecture</a>
```

**3. Update hero stats (line 192):**
- Lectures: 40 -> 44
- Quizzes: 44 -> 48

**4. Add RW subsection (after L2 quiz-grid closing `</div>` at line 729, before `</section>` at line 730):**

```html
<div class="section-head d11" style="margin-top:16px"><span>RW</span><h2>Standalone Lectures: Real-World Assets &amp; Tokenization</h2></div>
<div class="lec-grid">
<a href="lectures/rwa_tokenization_intro.pdf" class="lec-card" id="sl-rw-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>RWA & Tokenization: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p></a>
<a href="lectures/rwa_tokenization_intro_preview.pdf" class="lec-card" id="sl-rw-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>RWA & Tokenization: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/rwa_tokenization_preclass.pdf" class="lec-card" id="sl-rw-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>RWA & Tokenization: Pre-Class Handout</h3>
<p>4 activities &bull; RWA exploration, stablecoin comparison, security tokens</p></a>
<a href="lectures/rwa_tokenization.pdf" class="lec-card" id="sl-rw-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>RWA & Tokenization: Bridging TradFi and DeFi</h3>
<p>~55 frames &bull; Stablecoins, security tokens, institutional adoption</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_rw_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz RW-1</div>
<h3>Tokenization Fundamentals</h3>
<p>20 questions &bull; Asset classes, token standards, fractionalization</p></a>
<a href="quiz/quiz_rw_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz RW-2</div>
<h3>Stablecoins Deep Dive</h3>
<p>20 questions &bull; USDT, USDC, DAI, Terra/Luna, regulation</p></a>
<a href="quiz/quiz_rw_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz RW-3</div>
<h3>Security Tokens &amp; Compliance</h3>
<p>20 questions &bull; Howey test, ERC-3643, KYC/AML, legal wrappers</p></a>
<a href="quiz/quiz_rw_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz RW-4</div>
<h3>Real Estate, Bonds &amp; RWA Future</h3>
<p>20 questions &bull; RealT, BUIDL, Ondo, market projections</p></a>
</div>
```

**Acceptance Criteria (Task 9):**
- [ ] d11 CSS class exists with teal #14b8a6 and renders correctly
- [ ] RW sidebar links present with correct IDs (sl-rw-mini, sl-rw-intro, sl-rw-pre, sl-rw-main)
- [ ] Hero stats show 44 Lectures, 48 Quizzes
- [ ] RW subsection appears after L2 subsection
- [ ] All href paths are correct (PDF for lectures, HTML for quizzes)
- [ ] No existing content broken

---

### TASK 10: Verification
**Priority:** CRITICAL | **Depends on:** Tasks 1-9

1. **LaTeX compilation check:**
   - `pdflatex rwa_tokenization.tex` -- must compile without errors
   - `pdflatex rwa_tokenization_intro.tex` -- must compile without errors
   - `pdflatex rwa_tokenization_intro_preview.tex` -- must compile without errors
   - `pdflatex rwa_tokenization_preclass.tex` -- must compile without errors

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
   - Hero stats show correct numbers (44 Lectures, 48 Quizzes)
   - RW sidebar IDs exist and scroll correctly
   - All RW lecture/quiz href paths are valid
   - d11 CSS class renders teal #14b8a6

---

## Commit Strategy

### Commit 1: Core lecture files
```
Add L11 Real-World Assets & Tokenization lecture bundle (4 LaTeX files)

- rwa_tokenization.tex: 55-frame technical lecture (5 sections)
- rwa_tokenization_intro.tex: 10-frame mini-lecture with TikZ comics
- rwa_tokenization_intro_preview.tex: 6-frame INTRO preview
- rwa_tokenization_preclass.tex: Pre-class handout (4 activities, glossary)
```

### Commit 2: Quiz files
```
Add RW-1 through RW-4 interactive quizzes for RWA & Tokenization

- quiz_rw_part1.html: Tokenization Fundamentals (20 questions)
- quiz_rw_part2.html: Stablecoins Deep Dive (20 questions)
- quiz_rw_part3.html: Security Tokens & Compliance (20 questions)
- quiz_rw_part4.html: Real Estate, Bonds & RWA Future (20 questions)
```

### Commit 3: GitHub Pages integration
```
Add RWA & Tokenization section to GitHub Pages landing page

- Add RW subsection with d11 teal color class (#14b8a6)
- Add sidebar navigation links
- Update hero stats: 44 Lectures, 48 Quizzes
```

---

## Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| TikZ compilation errors from `\\` in nodes | MANDATE `align=center` on every node containing `\\`. Verify with grep before compile. |
| `\foreach` multi-variable syntax crash | BAN `/` syntax entirely. Use separate `\foreach` loops or manual placement. |
| Parameterized style `#1` conflict | BAN `#1` in all custom TikZ styles. Use fixed styles only. |
| Style name conflict with pgf built-ins | Use unique prefixes (e.g., `rwabox`, `rwanode`, `rwastep`) for all custom style names. Avoid: diamond, step, text, signal. |
| lstlisting in non-fragile frame | Every frame with lstlisting MUST have `[fragile]` option. Verify with grep. |
| Color mismatch with L04-L10 | Copy color definitions verbatim from layer2_scaling.tex, character by character. |
| Code frames use Solidity | The 4 code frames use Solidity snippets (AssetToken, VaultContract, SecurityToken, YieldToken). The Solidity lstdef in preamble is actively used. Ensure `language=Solidity` is set. |
| index.html regression | Only add content after L2 section. Do not modify any existing HTML elements. |
| pdflatex not available | Use `pdflatex` with `-interaction=nonstopmode` for error detection. Fall back to error-log review. |
| Overly long TikZ lines causing Beamer overflow | Test with 8pt font size. Use `\scriptsize` and `\tiny` aggressively in TikZ nodes. |
| Solidity code too long for fragile frames | Keep code snippets to 15-20 lines max. Use comments to indicate omitted parts. Pseudocode simplifications acceptable. |
| Quiz accent color mismatch | The existing quiz template already uses `--quiz-accent: #8b5cf6` (violet). RW quizzes match by default. |
| Rapidly evolving RWA landscape | Use data accurate as of late 2024/early 2025. Note approximate TVL/AUM/yield figures. Avoid overly specific stats that will date quickly. |
| Regulatory complexity overwhelming students | Keep legal explanations practical with concrete examples. Reserve detailed jurisdictional analysis for bottomnotes. |
| Terra/Luna topic sensitivity | Present factually with dates, numbers, and mechanism explanation. Avoid sensationalism. Focus on the technical failure mode. |

---

## Success Criteria

| Criterion | Verification Method |
|-----------|-------------------|
| All 4 LaTeX files compile cleanly | `pdflatex -interaction=nonstopmode` returns exit 0 |
| Tech lecture has exactly 55 frames | `grep -c "\\begin{frame}" rwa_tokenization.tex` = 55 |
| Mini-lecture has exactly 10 frames | `grep -c "\\begin{frame}" rwa_tokenization_intro.tex` = 10 |
| INTRO has exactly 6 frames | `grep -c "\\begin{frame}" rwa_tokenization_intro_preview.tex` = 6 |
| Exactly 4 fragile frames in tech lecture | `grep -c "\[fragile\]" rwa_tokenization.tex` = 4 |
| 80 quiz questions total (4 x 20) | JSON question count per file = 20 |
| All quiz explanations non-empty | No `"explanation": ""` in any quiz |
| index.html hero shows 44/48 | Visual inspection of rendered page |
| RW sidebar IDs work | Click each sidebar link, verify scroll |
| No TikZ safety violations | Automated grep checks pass |
| Color palette exact match | Diff color definitions against layer2_scaling.tex |
| d11 teal CSS applied correctly | Visual inspection: #14b8a6 teal for RW section |

---

## File Path Summary (All Deliverables)

```
D:\Joerg\Research\slides\cryptocurrency\
  lectures\
    rwa_tokenization_intro.tex             (Task 1 - Mini-lecture, 10 frames)
    rwa_tokenization_intro_preview.tex     (Task 2 - INTRO preview, 6 frames)
    rwa_tokenization_preclass.tex          (Task 3 - Pre-class handout)
    rwa_tokenization.tex                   (Task 4 - Tech lecture, 55 frames)
  quiz\
    quiz_rw_part1.html                     (Task 5 - Quiz RW-1, 20 questions)
    quiz_rw_part2.html                     (Task 6 - Quiz RW-2, 20 questions)
    quiz_rw_part3.html                     (Task 7 - Quiz RW-3, 20 questions)
    quiz_rw_part4.html                     (Task 8 - Quiz RW-4, 20 questions)
  index.html                               (Task 9 - GitHub Pages update)
```
