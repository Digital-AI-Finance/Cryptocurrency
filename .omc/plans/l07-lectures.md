# L07 Work Plan: Stablecoins & CBDCs Standalone Lecture Bundle

## Context

### Original Request
Create the complete L07 Stablecoins & CBDCs standalone lecture bundle following the exact patterns established in L04-L06 (most recently the NFTs & Digital Assets bundle). The bundle includes a 55-frame technical lecture, 10-frame mini-lecture, 6-frame INTRO preview, pre-class handout, 4 HTML quizzes, and GitHub Pages integration.

### Reference Files (Structural Templates)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\nft_digital_assets.tex` -- Tech lecture template (55 frames, 5 sections, 3 fragile code frames)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\nft_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\nft_digital_assets_intro.tex` -- INTRO preview template (6 frames, compact preamble)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\nft_digital_assets_preclass.tex` -- Pre-class handout template (article-class, 4 activities, glossary)
- `D:\Joerg\Research\slides\cryptocurrency\quiz\quiz_nf_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data)
- `D:\Joerg\Research\slides\cryptocurrency\index.html` -- GitHub Pages (NF subsection pattern, d6 class)

### Key Patterns Extracted from Reference Files

**Tech lecture preamble (compact, single-line usepackage):**
```latex
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}
```

**Color palette (EXACT RGB values):**
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

**Frame numbering pattern in tech lecture:**
- Frames 1-3: Opening (Title, Roadmap, TOC)
- Each section starts with a Section Divider frame
- Each section ends with a Summary frame
- Section 1: Frames 4-14 (11 frames)
- Section 2: Frames 15-26 (12 frames)
- Section 3: Frames 27-38 (12 frames)
- Section 4: Frames 39-48 (10 frames)
- Section 5: Frames 49-55 (7 frames)
- Total: 55 frames

**Code frames in NFT lecture:** 3 total with `[fragile]`
- Frame 8: ERC-721 Interface (lstlisting)
- Frame 19: NFT Royalty Mechanics (lstlisting)
- Frame 50: Fractional NFTs (lstlisting)

**Quiz JSON structure:**
```javascript
const quizData = {
    questions: [
        {
            "id": 1,
            "question": "...",
            "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
            "correct": "B",
            "explanation": "..."
        },
        // ... 20 questions total
    ]
};
```

---

## Work Objectives

### Core Objective
Produce a complete, self-contained L07 Stablecoins & CBDCs lecture bundle that compiles without errors and integrates into the existing GitHub Pages site.

### Deliverables

| # | Deliverable | File Path | Description |
|---|-------------|-----------|-------------|
| 1 | Technical Lecture | `lectures/stablecoins_cbdcs.tex` | 55-frame Beamer presentation, 5 sections |
| 2 | Mini-Lecture | `lectures/stablecoins_intro.tex` | 10-frame TikZ comic introduction |
| 3 | INTRO Preview | `lectures/stablecoins_cbdcs_intro.tex` | 6-frame preview with charts/diagrams |
| 4 | Pre-Class Handout | `lectures/stablecoins_cbdcs_preclass.tex` | Article-class, 4 activities, glossary |
| 5 | Quiz SC-1 | `quiz/quiz_sc_part1.html` | 20 questions: Stablecoin Fundamentals |
| 6 | Quiz SC-2 | `quiz/quiz_sc_part2.html` | 20 questions: Collateralized Stablecoins |
| 7 | Quiz SC-3 | `quiz/quiz_sc_part3.html` | 20 questions: Algorithmic Stablecoins |
| 8 | Quiz SC-4 | `quiz/quiz_sc_part4.html` | 20 questions: CBDCs & Advanced Topics |
| 9 | index.html update | `index.html` | Add SC subsection, update hero stats |

### Definition of Done
- All 4 LaTeX files compile with `pdflatex` without errors
- All 4 HTML quiz files render correctly in browser
- index.html displays SC subsection with correct links and sidebar IDs
- Hero stats updated to 28 Lectures, 32 Quizzes
- Frame counts match: 55 tech + 10 mini + 6 intro = 71 frames total
- Exactly 4 `[fragile]` frames with Solidity lstlisting in tech lecture (Frames 19, 31, 44, 52)
- Color palette matches L04-L06 exactly

---

## Must Have / Must NOT Have

### MUST Have
1. Exact same color palette (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray)
2. Same Beamer theme configuration as nft_digital_assets.tex
3. Same Solidity language definition and lstset
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
3. NO style names conflicting with pgf built-ins (diamond, step, text)
4. NO missing `align=center` on multi-line TikZ nodes
5. NO more than 4 `[fragile]` frames
6. NO code in the mini-lecture (zero lstlisting)
7. NO breaking changes to existing index.html content/links

---

## 5-Section Topic Breakdown

### Section 1: Stablecoin Fundamentals (Frames 4-14, 11 frames)
Why stablecoins exist, types overview, peg mechanisms, market landscape, key metrics.

### Section 2: Collateralized Stablecoins (Frames 15-26, 12 frames)
Fiat-backed (USDT, USDC, BUSD), crypto-backed (DAI/MakerDAO), over-collateralization, liquidation, commodity-backed.

### Section 3: Algorithmic Stablecoins (Frames 27-38, 12 frames)
Rebasing mechanisms, seigniorage models, Terra/LUNA collapse case study, Frax partial collateral, failure analysis.

### Section 4: Central Bank Digital Currencies (Frames 39-48, 10 frames)
CBDC motivation, wholesale vs retail, design choices (account vs token), global landscape (China/EU/US), privacy tradeoffs.

### Section 5: Regulation, Risk & Future (Frames 49-55, 7 frames)
MiCA regulation, systemic risk, DeFi integration, cross-border payments, stablecoin trilemma, course summary.

---

## Task Flow and Dependencies

```
Task 1 (Tech Lecture) --------\
Task 2 (Mini-Lecture)  --------\
Task 3 (INTRO Preview) --------+---> Task 9 (index.html) ---> Task 10 (Verification)
Task 4 (Pre-Class)     --------/
Tasks 5-8 (Quizzes)   --------/
```

Tasks 1-8 are independent and can be executed in parallel.
Task 9 depends on all file paths being finalized.
Task 10 depends on all files existing.

---

## Detailed TODOs

### TASK 1: Technical Lecture (`lectures/stablecoins_cbdcs.tex`)
**Priority:** HIGH | **Complexity:** HIGH | **Estimated frames:** 55

#### Preamble (copy from nft_digital_assets.tex exactly)
- Compact single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- All color definitions (mlblue through mlgray + solkeyword/string/comment/number)
- Beamer theme colors, navigation symbols, itemize, margins
- `\bottomnote` command
- Solidity language definition and `\lstset`
- TikZ/pgfplots with `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `Stablecoins \& CBDCs: A Quantitative Deep Dive`
- Subtitle: `Standalone Technical Lecture`

#### OPENING (Frames 1-3)

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ roadmap with 5 boxes (same style as NFT roadmap):
  - Box 1 (mlblue): `1. Stablecoin\\ Fundamentals`
  - Box 2 (mlgreen): `2. Collateralized\\Stablecoins`
  - Box 3 (mlorange): `3. Algorithmic\\Stablecoins`
  - Box 4 (mlred): `4. Central Bank\\Digital Currencies`
  - Box 5 (mlpurple): `5. Regulation\\Risk \& Future`
- Stealth arrows connecting boxes
- Two-column: Learning Objectives + Prerequisites
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--4}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections covering stablecoin fundamentals to CBDCs and regulation}`

#### SECTION 1: Stablecoin Fundamentals (Frames 4-14)

**Frame 4: Section 1 Divider**
- `beamercolorbox` with palette quaternary
- Title: `Section 1: Stablecoin Fundamentals`
- Subtitle: `Understanding price-stable digital assets and their role in the crypto ecosystem`
- Two-column: What You Will Learn + Frames in This Section
- Learning items:
  - Why stablecoins exist and the problems they solve
  - The three main categories: fiat-backed, crypto-backed, algorithmic
  - How peg mechanisms maintain price stability
  - Market landscape and dominance metrics

**Frame 5: The Volatility Problem**
- Two-column layout
- Left: Block explaining crypto volatility problem for payments/DeFi
- Right: TikZ chart showing BTC price volatility vs stablecoin stability
- Use pgfplots line chart with mlblue for BTC (volatile), mlgreen for USDC (flat ~$1)

**Frame 6: What is a Stablecoin?**
- Definition block: cryptographic token designed to maintain stable value relative to a reference asset
- Core Properties itemize: Pegged (to USD/EUR/gold), Redeemable, Transparent (reserves auditable), Composable (DeFi building block), Programmable
- TikZ diagram: reference asset -> peg mechanism -> stablecoin token

**Frame 7: Stablecoin Taxonomy**
- Full-width TikZ taxonomy tree:
  - Root: Stablecoins
  - Branch 1 (mlblue): Fiat-Collateralized (USDT, USDC, BUSD)
  - Branch 2 (mlgreen): Crypto-Collateralized (DAI, sUSD, LUSD)
  - Branch 3 (mlorange): Algorithmic (UST, FRAX, AMPL)
  - Branch 4 (mlpurple): Commodity-Backed (PAXG, XAUT)
- Use rounded corners boxes with arrows

**Frame 8: Peg Mechanism Overview**
- TikZ diagram showing 3 peg maintenance strategies side by side:
  - Panel 1: Redemption (1 USDC = 1 USD reserve)
  - Panel 2: Over-collateralization (150% collateral ratio)
  - Panel 3: Algorithmic (expand/contract supply)
- Each panel with distinct color

**Frame 9: Stablecoin Market Landscape**
- TikZ table (similar to NFT "by the Numbers" frame):
  - Row 1: Total stablecoin market cap (~$130B+)
  - Row 2: USDT dominance (~65%)
  - Row 3: USDC market share (~20%)
  - Row 4: Daily transaction volume ($50B+)
  - Row 5: Number of active stablecoins (200+)
- Summary bar at bottom

**Frame 10: Stablecoin Market Share Chart**
- pgfplots bar chart or pie-style TikZ showing market dominance:
  - USDT, USDC, DAI, BUSD, TUSD, Others
- Color-coded bars with percentages

**Frame 11: Stablecoin Use Cases**
- TikZ hub-and-spoke diagram (similar to NFT Use Cases frame):
  - Center: Stablecoin Use Cases
  - Spokes: Trading Pairs, DeFi Collateral, Cross-Border Payments, Remittances, Savings/Yield, Merchant Payments
- Each spoke in different color

**Frame 12: De-Peg Events Timeline**
- TikZ timeline showing major de-peg events:
  - 2018: USDT de-peg to $0.85
  - 2022: UST/LUNA collapse ($0 from $1)
  - 2023: USDC brief de-peg during SVB crisis
  - 2023: BUSD wind-down
- Use arrow timeline with colored event markers

**Frame 13: Stablecoin Transaction Volume vs Traditional Finance**
- pgfplots grouped bar chart comparing:
  - Visa daily volume, Mastercard, USDT on-chain, USDC on-chain
- Shows stablecoins approaching TradFi volumes

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 key takeaways, numbered, colored backgrounds)
- Same style as NFT Section 1 Summary

#### SECTION 2: Collateralized Stablecoins (Frames 15-26)

**Frame 15: Section 2 Divider**
- Title: `Section 2: Collateralized Stablecoins`
- Subtitle: `Fiat-backed and crypto-backed approaches to maintaining price stability`
- Learning items:
  - How fiat-backed stablecoins work (USDT, USDC)
  - Crypto-backed stablecoins and over-collateralization (DAI)
  - MakerDAO CDP/Vault mechanics
  - Reserve transparency and audit challenges

**Frame 16: Fiat-Backed Stablecoins: How They Work**
- TikZ flow diagram:
  - User deposits USD -> Issuer mints 1 USDC -> User receives USDC on-chain
  - Reverse: User redeems USDC -> Issuer burns USDC -> User receives USD
- Two-way arrow flow with mlblue/mlgreen

**Frame 17: USDT (Tether) Deep Dive**
- Two-column:
  - Left: Key facts (launch 2014, largest stablecoin, Tether Ltd issuer, multi-chain)
  - Right: TikZ reserve composition breakdown (US Treasuries, cash, commercial paper, etc.)
- Controversy note block

**Frame 18: USDC (Circle) Deep Dive**
- Two-column:
  - Left: Key facts (launch 2018, Circle + Coinbase, regulated, monthly attestations)
  - Right: TikZ reserve comparison with USDT
- Transparency advantage block

**Frame 19: Reserve Composition Comparison [FRAGILE] -- CODE FRAME 1**
- `\begin{frame}[fragile]{Reserve Composition Comparison}`
- Left column: Solidity code for a simple stablecoin mint/burn interface
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IStablecoin {
    function mint(address to, uint256 amount)
        external;
    function burn(address from, uint256 amount)
        external;
    function totalSupply()
        external view returns (uint256);
    function reserveBalance()
        external view returns (uint256);
    function collateralRatio()
        external view returns (uint256);
}
```
- Right column: explanation of functions

**Frame 20: Crypto-Backed Stablecoins: Overview**
- TikZ comparison diagram:
  - Fiat-backed: 1:1 reserve, centralized, custodial
  - Crypto-backed: 150%+ collateral, decentralized, non-custodial
- Pros/cons boxes for each

**Frame 21: MakerDAO and DAI**
- TikZ flow diagram of CDP/Vault mechanics:
  - User deposits ETH -> Vault created -> DAI minted (up to 66% of collateral value)
  - Liquidation threshold shown
  - Stability fee arrow
- Key metrics in side block

**Frame 22: Over-Collateralization Mechanics**
- TikZ worked example:
  - Deposit: 10 ETH at $2000 = $20,000
  - Collateral ratio: 150%
  - Max DAI: $20,000 / 1.5 = $13,333
  - Liquidation price calculation
- Color-coded safe/warning/danger zones

**Frame 23: Liquidation Process**
- TikZ step diagram showing liquidation cascade:
  - Step 1: ETH price drops below liquidation ratio
  - Step 2: Keeper triggers liquidation
  - Step 3: Collateral auctioned
  - Step 4: Debt repaid, penalty charged
  - Step 5: Remaining collateral returned
- Red warning colors for danger states

**Frame 24: Multi-Collateral DAI**
- TikZ diagram showing multiple collateral types feeding into DAI:
  - ETH, WBTC, USDC, stETH, real-world assets
  - Each with different collateral ratios
  - PSM (Peg Stability Module) for USDC

**Frame 25: Commodity-Backed Stablecoins**
- Two-column:
  - Left: PAXG (Pax Gold) -- backed by London Good Delivery gold bars
  - Right: XAUT (Tether Gold) -- backed by gold reserves
- TikZ comparison table: backing, custody, redemption, regulatory

**Frame 26: Section 2 Summary**
- 5-point summary boxes (same pattern as Section 1 Summary)

#### SECTION 3: Algorithmic Stablecoins (Frames 27-38)

**Frame 27: Section 3 Divider**
- Title: `Section 3: Algorithmic Stablecoins`
- Subtitle: `Achieving price stability through smart contract mechanisms without full collateral`
- Learning items:
  - How algorithmic stablecoins attempt to maintain peg
  - Rebasing, seigniorage, and fractional approaches
  - The Terra/LUNA collapse: anatomy of a death spiral
  - Why most algorithmic stablecoins fail

**Frame 28: Algorithmic Stablecoin Concept**
- TikZ diagram:
  - Above peg: Protocol mints more tokens (expand supply)
  - Below peg: Protocol burns tokens / incentivizes buying (contract supply)
  - Target: $1.00 center line
- Supply/demand visualization

**Frame 29: Rebasing Mechanism (Ampleforth)**
- TikZ step diagram:
  - Price > $1.05: Positive rebase (wallet balances increase proportionally)
  - Price < $0.95: Negative rebase (wallet balances decrease proportionally)
  - Price $0.95-$1.05: No rebase
- AMPL-specific flow with example numbers

**Frame 30: Seigniorage Model**
- TikZ two-token diagram:
  - Stablecoin (e.g., UST) -- maintains peg
  - Governance/Absorber token (e.g., LUNA) -- absorbs volatility
  - Mint/burn arbitrage loop between them
- Arrow-based flow showing the economic incentive

**Frame 31: Terra/LUNA Architecture [FRAGILE] -- CODE FRAME 2**
- `\begin{frame}[fragile]{Terra/LUNA Architecture}`
- Left: Solidity-style pseudocode for mint/burn swap
```solidity
// Simplified Terra swap logic
contract TerraSwap {
    uint256 public ustSupply;
    uint256 public lunaPrice;

    // Mint UST by burning LUNA
    function mintUST(uint256 lunaAmount)
        external {
        uint256 ustAmount = lunaAmount
            * lunaPrice / 1e18;
        ustSupply += ustAmount;
        // burn lunaAmount from sender
    }

    // Redeem UST for LUNA
    function redeemUST(uint256 ustAmount)
        external {
        uint256 lunaAmount = ustAmount
            * 1e18 / lunaPrice;
        ustSupply -= ustAmount;
        // mint lunaAmount to sender
    }
}
```
- Right: explanation of the arbitrage mechanism

**Frame 32: Terra/LUNA Collapse Timeline**
- TikZ timeline (similar to De-Peg Events frame but detailed):
  - May 7, 2022: Large UST sell-off begins
  - May 8: UST de-pegs to $0.98
  - May 9: LUNA supply hyperinflates
  - May 10: UST falls to $0.60
  - May 12: UST at $0.10, LUNA near zero
  - May 13: Chain halted
- Use mlred gradient for severity

**Frame 33: Death Spiral Mechanics**
- TikZ circular diagram showing the feedback loop:
  - UST below peg -> Arbitrageurs redeem UST for LUNA -> LUNA supply increases -> LUNA price drops -> Confidence drops -> More UST selling -> UST further below peg
- Circular arrows with intensifying red

**Frame 34: Anchor Protocol and the 20% Yield**
- Two-column:
  - Left: How Anchor offered ~20% APY on UST deposits
  - Right: TikZ diagram showing unsustainable yield source (subsidized by LFG reserves)
- Warning box about unsustainable yields

**Frame 35: Lessons from Algorithmic Failures**
- TikZ table of failed algorithmic stablecoins:
  - Basis Cash, Empty Set Dollar, Iron Finance, UST
  - Columns: Name, Mechanism, Peak Market Cap, Failure Mode, Date
- Pattern recognition block

**Frame 36: Fractional-Algorithmic Approach (Frax)**
- TikZ diagram of Frax's hybrid model:
  - Partially collateralized (e.g., 90% USDC + 10% algorithmic)
  - Collateral ratio adjusts based on demand
  - FXS governance token absorbs volatility
- Comparison with pure algorithmic

**Frame 37: Stablecoin Trilemma**
- TikZ triangle diagram:
  - Vertex 1: Price Stability
  - Vertex 2: Capital Efficiency
  - Vertex 3: Decentralization
- Position different stablecoins on the triangle (USDC near stability+centralized, DAI near stability+decentralized, UST attempted all three)

**Frame 38: Section 3 Summary**
- 5-point summary boxes

#### SECTION 4: Central Bank Digital Currencies (Frames 39-48)

**Frame 39: Section 4 Divider**
- Title: `Section 4: Central Bank Digital Currencies`
- Subtitle: `Government-issued digital money: motivations, architectures, and global initiatives`
- Learning items:
  - Why central banks are exploring digital currencies
  - Wholesale vs retail CBDC design choices
  - Account-based vs token-based models
  - Global CBDC landscape and pilot programs

**Frame 40: What is a CBDC?**
- Two-column:
  - Left: Definition block + key properties (legal tender, direct liability of central bank, programmable, digital-native)
  - Right: TikZ comparison: Cash vs Bank Deposit vs Stablecoin vs CBDC
- Four-row comparison matrix

**Frame 41: CBDC Motivation**
- TikZ hub-and-spoke:
  - Center: Why CBDCs?
  - Spokes: Financial Inclusion, Payment Efficiency, Monetary Policy Innovation, Counter Private Stablecoins, Reduce Cash Handling Costs, Cross-Border Payments
- Each spoke colored distinctly

**Frame 42: Wholesale vs Retail CBDC**
- TikZ side-by-side panels:
  - Left panel (mlblue): Wholesale CBDC -- interbank settlement, central bank -> commercial banks, Helvetia/mBridge examples
  - Right panel (mlgreen): Retail CBDC -- consumer/merchant use, central bank -> public (direct or intermediated), e-CNY/e-EUR examples
- Architecture diagrams in each

**Frame 43: CBDC Architecture Models**
- TikZ layered diagram showing 3 models:
  - Model 1: Direct (central bank maintains all accounts)
  - Model 2: Intermediated (commercial banks distribute, central bank ledger)
  - Model 3: Hybrid (two-tier with some direct access)
- Pros/cons annotations

**Frame 44: Account-Based vs Token-Based [FRAGILE] -- CODE FRAME 3**
- `\begin{frame}[fragile]{Account-Based vs Token-Based}`
- Left: Solidity interface for account-based CBDC
```solidity
// Account-based CBDC model
interface IAccountCBDC {
    function balanceOf(address account)
        external view returns (uint256);
    function transfer(
        address to, uint256 amount
    ) external returns (bool);
    function freeze(address account)
        external; // regulatory
    function setSpendingLimit(
        address account, uint256 limit
    ) external;
}
```
- Right: explanation comparing account vs token approaches

**Frame 45: Global CBDC Landscape**
- TikZ world-map-style overview (stylized, not actual map):
  - Launched: Nigeria (eNaira), Bahamas (Sand Dollar), Jamaica (JAM-DEX)
  - Pilot: China (e-CNY), India (e-Rupee), Sweden (e-Krona)
  - Research: EU (Digital Euro), US (FedNow context), UK (Britcoin)
  - Canceled: Ecuador
- Color-coded status indicators

**Frame 46: China's Digital Yuan (e-CNY)**
- Two-column:
  - Left: Key facts (pilot since 2020, 260M+ wallets, two-tier model, programmable)
  - Right: TikZ architecture diagram (PBOC -> commercial banks -> users/merchants)
- Metrics table: transaction volume, geographic coverage

**Frame 47: Privacy in CBDCs**
- TikZ spectrum diagram:
  - Full anonymity (cash) <---------> Full surveillance (CBDC worst case)
  - Positions: Cash, crypto, tiered privacy CBDC, full-surveillance CBDC
- Privacy-preserving techniques block: zero-knowledge proofs, tiered limits

**Frame 48: Section 4 Summary**
- 5-point summary boxes

#### SECTION 5: Regulation, Risk & Future (Frames 49-55)

**Frame 49: Section 5 Divider**
- Title: `Section 5: Regulation, Risk \& Future`
- Subtitle: `Regulatory frameworks, systemic risks, and the future of programmable money`
- Learning items:
  - Major regulatory frameworks (MiCA, US proposals)
  - Systemic risk from stablecoin concentration
  - DeFi integration and composability
  - Cross-border payment transformation

**Frame 50: Regulatory Landscape**
- TikZ table comparing regulatory approaches:
  - EU (MiCA): reserve requirements, authorization, asset-referenced vs e-money tokens
  - US: Proposed stablecoin bills, OCC guidance
  - Singapore: MAS framework
  - Japan: revised Payment Services Act
- Color-coded strictness levels

**Frame 51: Systemic Risk Analysis**
- TikZ risk diagram:
  - Central node: Stablecoin Systemic Risk
  - Connected risks: Reserve quality, Concentration (USDT dominance), Bank run dynamics, Contagion to DeFi, Regulatory uncertainty
- Red/orange risk coloring

**Frame 52: Stablecoins in DeFi [FRAGILE] -- CODE FRAME 4**
- `\begin{frame}[fragile]{Stablecoins in DeFi}`
- Left: Solidity interface for a lending pool using stablecoins
```solidity
// Stablecoin lending pool
interface IStableLend {
    function deposit(
        address stablecoin, uint256 amt
    ) external returns (uint256 shares);
    function borrow(
        address stablecoin, uint256 amt
    ) external;
    function getAPY(address stablecoin)
        external view returns (uint256);
    function liquidate(
        address borrower
    ) external;
}
```
- Right: explanation of stablecoin role in DeFi (TVL, lending, AMM pairs)

**Frame 53: Cross-Border Payments Revolution**
- TikZ comparison:
  - Traditional: Bank -> Correspondent Bank -> SWIFT -> Correspondent Bank -> Bank (3-5 days, high fees)
  - Stablecoin/CBDC: Sender -> Blockchain -> Receiver (minutes, low fees)
  - mBridge project example
- Time and cost comparison metrics

**Frame 54: The Future of Programmable Money**
- TikZ three-panel forward-looking:
  - Panel 1: Stablecoin evolution (fully regulated, interoperable)
  - Panel 2: CBDC deployment (privacy-preserving, programmable)
  - Panel 3: Convergence (stablecoin-CBDC coexistence, tokenized deposits)
- Timeline projections

**Frame 55: Key Takeaways and Course Summary**
- TikZ 5-box summary (matching NFT Frame 55 style):
  - Box 1 (mlblue): Stablecoins solve crypto volatility through different peg mechanisms
  - Box 2 (mlpurple): Collateralized stablecoins dominate but face reserve transparency challenges
  - Box 3 (mlgreen): Algorithmic stablecoins remain experimental; Terra/LUNA showed catastrophic failure modes
  - Box 4 (mlorange): CBDCs represent government response; design choices involve fundamental tradeoffs
  - Box 5 (mlred): Regulation is accelerating globally; stablecoins and CBDCs will reshape financial infrastructure
- Purple teaser bar: `Next: Advanced topics in cryptocurrency regulation and institutional adoption`

**Acceptance Criteria (Task 1):**
- [ ] Exactly 55 frames with correct numbering
- [ ] 5 sections with divider and summary frames
- [ ] Exactly 4 `[fragile]` frames with lstlisting (Frames 19, 31, 44, 52)
- [ ] Preamble matches nft_digital_assets.tex exactly
- [ ] All TikZ multi-line nodes have `align=center`
- [ ] No `\foreach` with `/` multi-variable syntax
- [ ] No parameterized styles with `#1`
- [ ] `\bottomnote` on every frame
- [ ] Compiles with pdflatex without errors

---

### TASK 2: Mini-Lecture (`lectures/stablecoins_intro.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM | **Estimated frames:** 10

#### Preamble
- Copy the ENTIRE preamble from `nft_intro.tex` lines 1-84, changing only:
  - Title: `Stablecoins \& CBDCs: A Visual Introduction`
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
- Quote: `"In the world of crypto, stability is the hardest trick to pull off"`
- Purple title, blue subtitle

**Frame 2: The Price Stability Problem (TikZ Comic)**
- 3-panel comic layout (same panel dimensions as nft_intro.tex):
  - Panel 1: Alice wants to buy coffee with Bitcoin. Price: 0.001 BTC
  - Panel 2: By the time she pays, BTC dropped 10%. Coffee now costs 0.0011 BTC. Bob (merchant) confused.
  - Panel 3: Solution: Use stablecoins! USDC stays at $1. Both happy.
- Stick figures, speech bubbles, same drawing style as NFT intro

**Frame 3: What is a Stablecoin?**
- Two-column visual comparison:
  - Left: Volatile Crypto (BTC/ETH with wavy price line)
  - Right: Stablecoins (USDC/USDT with flat $1 line)
- TikZ with colored boxes, arrows, labels

**Frame 4: Types of Stablecoins (TikZ Comic)**
- 3-panel layout:
  - Panel 1: Fiat-backed -- banker holding USD reserves, minting tokens
  - Panel 2: Crypto-backed -- vault overflowing with ETH, smaller amount of DAI coming out
  - Panel 3: Algorithmic -- robot trying to balance supply/demand scales
- Each panel labeled with type name

**Frame 5: How Stablecoins Maintain Their Peg**
- TikZ layered diagram:
  - Layer 1: Reserve backing (1 USDC = 1 USD in bank)
  - Layer 2: Arbitrage (buy at $0.99, redeem for $1.00)
  - Layer 3: Smart contract logic (auto-adjust supply)
- Upward arrows showing dependency

**Frame 6: The Terra/LUNA Disaster (TikZ Comic)**
- 3-panel comic:
  - Panel 1: UST and LUNA working together happily. "We keep each other stable!"
  - Panel 2: Massive sell pressure. UST de-pegs. LUNA supply explodes. "Death spiral!"
  - Panel 3: Both collapsed to near zero. "$60 billion lost in days." Gravestone imagery.

**Frame 7: What is a CBDC?**
- TikZ comparison grid:
  - Cash: physical, anonymous, no interest
  - Bank deposit: digital, tracked, some interest
  - Stablecoin: digital, pseudonymous, DeFi yields
  - CBDC: digital, government-issued, programmable
- Color-coded quadrants

**Frame 8: CBDCs Around the World**
- TikZ stylized world view:
  - China e-CNY (launched pilot), EU Digital Euro (research), US (exploring)
  - Status indicators: green (live), yellow (pilot), blue (research)
- Simple geographic layout with country badges

**Frame 9: Risks and Benefits (TikZ Comic)**
- 3-panel layout:
  - Panel 1: Benefits shield -- stability, DeFi access, inclusion
  - Panel 2: Risks warning -- de-peg events, regulatory crackdowns, surveillance
  - Panel 3: Balance scales -- future requires careful design
- Same comic style

**Frame 10: Key Takeaways**
- TikZ numbered boxes (5 takeaways):
  1. Stablecoins bridge crypto volatility to real-world value
  2. Fiat-backed dominate; algorithmic attempts mostly failed
  3. Terra/LUNA taught the industry about death spiral risk
  4. CBDCs are the government answer to private stablecoins
  5. Regulation will shape which stablecoins survive
- Purple teaser bar at bottom

**Acceptance Criteria (Task 2):**
- [ ] Exactly 10 frames
- [ ] Zero `[fragile]` frames, zero lstlisting
- [ ] All TikZ comics use same panel style as nft_intro.tex (draw, rounded corners, stick figures)
- [ ] All multi-line TikZ nodes have `align=center`
- [ ] Verbose preamble matching nft_intro.tex structure
- [ ] Compiles with pdflatex without errors

---

### TASK 3: INTRO Preview (`lectures/stablecoins_cbdcs_intro.tex`)
**Priority:** HIGH | **Complexity:** LOW | **Estimated frames:** 6

#### Preamble
- Compact preamble matching `nft_digital_assets_intro.tex` exactly
- Minimal TikZ libraries: `arrows.meta,positioning,shapes.geometric,calc`
- Title: `Stablecoins \& CBDCs: Course Preview`
- Subtitle: `INTRO Preview`

#### Frame Specifications

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Why Stablecoins & CBDCs Matter**
- Two-column: pgfplots bar chart (left) + Key Metrics block (right)
- Chart: Stablecoin market cap, CBDC pilot programs, daily transaction volume (normalized)
- Key metrics: $130B+ stablecoin market cap, 130+ countries exploring CBDCs, $50B+ daily volume, 65% USDT dominance

**Frame 3: Stablecoin & CBDC Ecosystem at a Glance**
- TikZ hub diagram (same style as NFT "Ecosystem at a Glance"):
  - Center: Stablecoin & CBDC Ecosystem
  - Spokes: Fiat-Backed (USDT, USDC), Crypto-Backed (DAI, LUSD), Algorithmic (FRAX), CBDCs (e-CNY, Digital Euro)
- Color-coded by type

**Frame 4: Market Trajectory**
- Two-column: pgfplots line chart (left) + Growth Drivers block (right)
- Chart: Stablecoin total market cap 2018-2024
- Growth drivers: DeFi adoption, institutional interest, regulatory frameworks, cross-border payments

**Frame 5: Course Coverage**
- TikZ 5-step process flow (same style as NFT "Course Coverage"):
  - (1) Stablecoin Fundamentals
  - (2) Collateralized Stablecoins
  - (3) Algorithmic Stablecoins
  - (4) CBDCs
  - (5) Regulation & Future
- Sub-labels for each step
- Prerequisites + Outcomes blocks

**Frame 6: What You Will Learn**
- Two-column: Learning Outcomes block (left) + TikZ skill diagram (right)
- Outcomes: peg mechanisms, collateral models, CBDC architectures, regulatory frameworks
- TikZ: central "Stablecoin & CBDC Mastery" node with 4 skill spokes

**Acceptance Criteria (Task 3):**
- [ ] Exactly 6 frames
- [ ] Compact preamble matching nft_digital_assets_intro.tex
- [ ] pgfplots charts with correct axis styling
- [ ] Compiles with pdflatex without errors

---

### TASK 4: Pre-Class Handout (`lectures/stablecoins_cbdcs_preclass.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM

#### Preamble
- Article-class matching `nft_digital_assets_preclass.tex` exactly
- `\documentclass[11pt,a4paper]{article}`
- Same packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- Color definitions using HTML format (not RGB)
- Header: `Stablecoins \& CBDCs | Lesson 07 | Pre-Class Discovery Handout`
- `\activitybox` and `\fillcell` commands

#### Activity 1: Explore Stablecoin Markets (10 min)
- Visit CoinGecko stablecoins page, answer:
  1. What are the top 5 stablecoins by market cap? What blockchain are they primarily on?
  2. Pick one stablecoin -- what is its 24h trading volume vs market cap ratio?
  3. Check the price chart -- has it ever significantly de-pegged? When?
  4. Compare USDT and USDC -- what differences do you notice in reserve reporting?
- Bonus: Compare stablecoin dominance chart over the last 2 years.

#### Activity 2: MakerDAO Vault Investigation (5 min)
- Visit Oasis.app or DeFi Llama MakerDAO page, answer:
  1. What collateral types does MakerDAO accept?
  2. What is the current collateral ratio requirement for ETH vaults?
  3. What is the DAI Savings Rate (DSR)?
  4. How much total collateral is locked in MakerDAO?
- Fill-in table: Collateral Type | Min Ratio | Stability Fee | TVL

#### Activity 3: CBDC Tracker Research (10 min)
- Visit Atlantic Council CBDC tracker, complete table:
  - China e-CNY | Status | Architecture | Privacy Model | Pilot Scale
  - EU Digital Euro | ... | ... | ... | ...
  - US Digital Dollar | ... | ... | ... | ...
  - India e-Rupee | ... | ... | ... | ...

#### Activity 4: Design Your Stablecoin (5 min)
- Fill-in form:
  1. Stablecoin Name: ___
  2. Peg Target: [ ] USD [ ] EUR [ ] Gold [ ] Basket [ ] Other
  3. Mechanism: [ ] Fiat-backed [ ] Crypto-backed [ ] Algorithmic [ ] Hybrid
  4. Collateral Ratio: ____%
  5. Reserve Transparency: [ ] Daily attestation [ ] Monthly audit [ ] Annual [ ] None
  6. Target Use Case: [ ] Payments [ ] DeFi [ ] Cross-border [ ] Savings
  7. Biggest Risk: [ ] De-peg [ ] Regulatory [ ] Bank run [ ] Smart contract

#### Glossary (12+ terms)

| Term | Definition |
|------|-----------|
| **Stablecoin** | A cryptocurrency designed to maintain a stable value relative to a reference asset (usually USD). Achieved through collateral reserves, algorithmic mechanisms, or a combination. |
| **Peg** | The target price a stablecoin aims to maintain (e.g., 1 USDC = 1 USD). Maintaining the peg requires active mechanisms such as redemption guarantees or supply adjustments. |
| **De-peg** | When a stablecoin's market price diverges significantly from its target peg. Can be temporary (USDC during SVB) or permanent (UST collapse). |
| **Collateral Ratio** | The ratio of collateral value to stablecoin value issued. Fiat-backed: 100%. Crypto-backed: typically 150%+ to absorb volatility. |
| **Over-collateralization** | Requiring more collateral than the value of stablecoins minted (e.g., $150 ETH to mint $100 DAI), providing a safety buffer against price drops. |
| **Liquidation** | The forced sale of collateral when its value drops below the minimum ratio, protecting the protocol from undercollateralization. |
| **CDP / Vault** | Collateralized Debt Position. A smart contract that locks crypto collateral and mints stablecoins against it. Used by MakerDAO for DAI. |
| **Algorithmic Stablecoin** | A stablecoin that maintains its peg through algorithmic supply adjustments rather than holding collateral reserves. Most have failed historically. |
| **Death Spiral** | A self-reinforcing feedback loop where loss of confidence causes selling, which further breaks the peg, causing more selling. Exemplified by Terra/LUNA. |
| **CBDC** | Central Bank Digital Currency. A digital form of fiat money issued directly by a central bank as legal tender, distinct from commercial bank deposits. |
| **Wholesale CBDC** | A CBDC restricted to financial institutions for interbank settlement, improving speed and reducing counterparty risk in large-value payments. |
| **Retail CBDC** | A CBDC available to the general public for everyday transactions, potentially replacing or supplementing physical cash. |
| **Seigniorage** | The profit a currency issuer makes from the difference between face value and production cost. In algorithmic stablecoins, captured when new tokens are minted above peg. |
| **Peg Stability Module (PSM)** | A MakerDAO mechanism allowing 1:1 swaps between DAI and approved stablecoins (like USDC) to maintain the DAI peg with minimal slippage. |

**Acceptance Criteria (Task 4):**
- [ ] Article-class preamble matches nft_digital_assets_preclass.tex
- [ ] 4 activities with `\activitybox` command
- [ ] Glossary with 12+ terms in tabular format
- [ ] Header says "Lesson 07"
- [ ] Fill-in tables with `\fillcell`
- [ ] Compiles with pdflatex without errors

---

### TASK 5: Quiz SC-1 (`quiz/quiz_sc_part1.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz SC-1: Stablecoin Fundamentals`
- 20 questions covering Section 1 topics:
  - Stablecoin definition and purpose (Q1-Q4)
  - Types/taxonomy of stablecoins (Q5-Q8)
  - Peg mechanisms and arbitrage (Q9-Q12)
  - Market landscape and metrics (Q13-Q16)
  - De-peg events and risks (Q17-Q20)
- Format: A/B/C/D multiple choice with explanations
- **Note:** The existing quiz template has NO prev/next inter-quiz navigation links. Do NOT add prev/next links. The nav section contains only Dashboard and GitHub links. Copy this pattern as-is.
- Copy CSS/JS structure from quiz_nf_part1.html exactly

**Acceptance Criteria:**
- [ ] KaTeX v0.16.9 linked
- [ ] CSS variables match template
- [ ] 3-column grid layout
- [ ] 20 questions with JSON data
- [ ] All questions have correct answer and explanation
- [ ] Renders correctly in browser

---

### TASK 6: Quiz SC-2 (`quiz/quiz_sc_part2.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz SC-2: Collateralized Stablecoins`
- 20 questions covering Section 2 topics:
  - Fiat-backed mechanics (USDT, USDC) (Q1-Q5)
  - Reserve composition and audits (Q6-Q8)
  - Crypto-backed mechanics (DAI) (Q9-Q12)
  - Over-collateralization and liquidation (Q13-Q16)
  - MakerDAO specifics and commodity-backed (Q17-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 7: Quiz SC-3 (`quiz/quiz_sc_part3.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz SC-3: Algorithmic Stablecoins`
- 20 questions covering Section 3 topics:
  - Algorithmic peg mechanisms (Q1-Q4)
  - Rebasing and seigniorage models (Q5-Q8)
  - Terra/LUNA collapse details (Q9-Q13)
  - Fractional approaches (Frax) (Q14-Q16)
  - Stablecoin trilemma and failure analysis (Q17-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 8: Quiz SC-4 (`quiz/quiz_sc_part4.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz SC-4: CBDCs & Advanced Topics`
- 20 questions covering Sections 4-5 topics:
  - CBDC definition and motivation (Q1-Q4)
  - Wholesale vs retail, account vs token (Q5-Q8)
  - Global CBDC landscape (Q9-Q12)
  - Privacy and design tradeoffs (Q13-Q15)
  - Regulation (MiCA, US) (Q16-Q18)
  - Systemic risk and future (Q19-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 9: GitHub Pages Update (`index.html`)
**Priority:** HIGH | **Complexity:** LOW

#### Changes Required

**1. Add d7 CSS class (after d6 styles):**
```css
.section-head.d7 span{background:#f59e0b}
.d7 summary{border-left:3px solid #f59e0b}
```
*Note: Do NOT add `.d7 .lcard-num` -- the SC HTML uses `lec-tag` classes, not `lcard-num`. The `lec-tag` and `quiz-tag` classes are intentionally unstyled (same as DF/NF sections). Copy the HTML pattern as-is for consistency.*

**2. Add SC sidebar links (after NF entries in the Standalone Lectures details):**
```html
<a href="#sl-sc-mini">Mini-Lecture: Stablecoins</a>
<a href="#sl-sc-intro">SC INTRO Preview</a>
<a href="#sl-sc-pre">SC Pre-Class Handout</a>
<a href="#sl-sc-main">SC Technical Lecture</a>
```

**3. Update hero stats:**
- Lectures: 24 -> 28
- Quizzes: 28 -> 32

**4. Add SC subsection (after NF quiz-grid closing div, before `</section>`):**
```html
<div class="section-head d7" style="margin-top:16px"><span>SC</span><h2>Standalone Lectures: Stablecoins &amp; CBDCs</h2></div>
<div class="lec-grid">
<a href="lectures/stablecoins_intro.pdf" class="lec-card" id="sl-sc-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>Stablecoins &amp; CBDCs: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p></a>
<a href="lectures/stablecoins_cbdcs_intro.pdf" class="lec-card" id="sl-sc-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>Stablecoins &amp; CBDCs: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/stablecoins_cbdcs_preclass.pdf" class="lec-card" id="sl-sc-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>Stablecoins &amp; CBDCs: Pre-Class Handout</h3>
<p>4 activities &bull; Market research, CBDC tracker</p></a>
<a href="lectures/stablecoins_cbdcs.pdf" class="lec-card" id="sl-sc-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>Stablecoins &amp; CBDCs: Quantitative Deep Dive</h3>
<p>~55 frames &bull; Peg mechanisms, Terra collapse, CBDCs</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_sc_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz SC-1</div>
<h3>Stablecoin Fundamentals</h3>
<p>20 questions &bull; Types, pegs, market landscape</p></a>
<a href="quiz/quiz_sc_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz SC-2</div>
<h3>Collateralized Stablecoins</h3>
<p>20 questions &bull; USDT, USDC, DAI, liquidation</p></a>
<a href="quiz/quiz_sc_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz SC-3</div>
<h3>Algorithmic Stablecoins</h3>
<p>20 questions &bull; Terra/LUNA, rebasing, Frax</p></a>
<a href="quiz/quiz_sc_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz SC-4</div>
<h3>CBDCs &amp; Advanced Topics</h3>
<p>20 questions &bull; e-CNY, Digital Euro, regulation</p></a>
</div>
```

**Acceptance Criteria (Task 9):**
- [ ] d7 CSS class exists and renders correctly
- [ ] SC sidebar links present with correct IDs
- [ ] Hero stats show 28 Lectures, 32 Quizzes
- [ ] SC subsection appears after NF subsection
- [ ] All href paths are correct
- [ ] All sidebar IDs match: sl-sc-mini, sl-sc-intro, sl-sc-pre, sl-sc-main
- [ ] No existing content broken

---

### TASK 10: Verification
**Priority:** CRITICAL | **Depends on:** Tasks 1-9

1. **LaTeX compilation check:**
   - `pdflatex stablecoins_cbdcs.tex` -- must compile without errors
   - `pdflatex stablecoins_intro.tex` -- must compile without errors
   - `pdflatex stablecoins_cbdcs_intro.tex` -- must compile without errors
   - `pdflatex stablecoins_cbdcs_preclass.tex` -- must compile without errors

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

5. **Quiz verification:**
   - Each quiz file has exactly 20 questions in JSON
   - All `correct` values are A, B, C, or D
   - All `explanation` fields are non-empty
   - Nav links chain correctly

6. **index.html verification:**
   - Hero stats show correct numbers
   - SC sidebar IDs exist
   - All SC lecture/quiz href paths are valid

---

## Commit Strategy

### Commit 1: Core lecture files
```
Add L07 Stablecoins & CBDCs lecture bundle (4 LaTeX files)

- stablecoins_cbdcs.tex: 55-frame technical lecture (5 sections)
- stablecoins_intro.tex: 10-frame mini-lecture with TikZ comics
- stablecoins_cbdcs_intro.tex: 6-frame INTRO preview
- stablecoins_cbdcs_preclass.tex: Pre-class handout (4 activities, glossary)
```

### Commit 2: Quiz files
```
Add SC-1 through SC-4 interactive quizzes for Stablecoins & CBDCs

- quiz_sc_part1.html: Stablecoin Fundamentals (20 questions)
- quiz_sc_part2.html: Collateralized Stablecoins (20 questions)
- quiz_sc_part3.html: Algorithmic Stablecoins (20 questions)
- quiz_sc_part4.html: CBDCs & Advanced Topics (20 questions)
```

### Commit 3: GitHub Pages integration
```
Add Stablecoins & CBDCs section to GitHub Pages landing page

- Add SC subsection with d7 color class
- Add sidebar navigation links
- Update hero stats: 28 Lectures, 32 Quizzes
```

---

## Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| TikZ compilation errors from `\\` in nodes | MANDATE `align=center` on every node containing `\\`. Verify with grep before compile. |
| `\foreach` multi-variable syntax crash | BAN `/` syntax entirely. Use separate `\foreach` loops or manual placement. |
| Parameterized style `#1` conflict | BAN `#1` in all custom TikZ styles. Use fixed styles only. |
| Style name conflict with pgf built-ins | Use unique prefixes (e.g., `scbox`, `scnode`) for all custom style names. Avoid: diamond, step, text, signal. |
| lstlisting in non-fragile frame | Every frame with lstlisting MUST have `[fragile]` option. |
| Color mismatch with L04-L06 | Copy color definitions verbatim from nft_digital_assets.tex, character by character. |
| Quiz nav link chain broken | Verify prev/next links form correct sequence: nf_part4 -> sc_part1 -> sc_part2 -> sc_part3 -> sc_part4. |
| index.html regression | Only add content after NF section. Do not modify any existing HTML elements. |
| pdflatex not available | Use `pdflatex` with `-interaction=nonstopmode` for error detection. Fall back to error-log review. |
| Overly long TikZ lines causing Beamer overflow | Test with 8pt font size. Use `\scriptsize` and `\tiny` aggressively in TikZ nodes. |

---

## Success Criteria

| Criterion | Verification Method |
|-----------|-------------------|
| All 4 LaTeX files compile cleanly | `pdflatex -interaction=nonstopmode` returns exit 0 |
| Tech lecture has exactly 55 frames | `grep -c "\\begin{frame}" stablecoins_cbdcs.tex` = 55 |
| Mini-lecture has exactly 10 frames | `grep -c "\\begin{frame}" stablecoins_intro.tex` = 10 |
| INTRO has exactly 6 frames | `grep -c "\\begin{frame}" stablecoins_cbdcs_intro.tex` = 6 |
| Exactly 4 fragile frames in tech lecture | `grep -c "\[fragile\]" stablecoins_cbdcs.tex` = 4 |
| 80 quiz questions total (4 x 20) | JSON question count per file = 20 |
| All quiz explanations non-empty | No `"explanation": ""` in any quiz |
| index.html hero shows 28/32 | Visual inspection of rendered page |
| SC sidebar IDs work | Click each sidebar link, verify scroll |
| No TikZ safety violations | Automated grep checks pass |
| Color palette exact match | Diff color definitions against nft_digital_assets.tex |

---

## File Path Summary (All Deliverables)

```
D:\Joerg\Research\slides\cryptocurrency\
  lectures\
    stablecoins_cbdcs.tex           (Task 1 - Tech lecture, 55 frames)
    stablecoins_intro.tex           (Task 2 - Mini-lecture, 10 frames)
    stablecoins_cbdcs_intro.tex     (Task 3 - INTRO preview, 6 frames)
    stablecoins_cbdcs_preclass.tex  (Task 4 - Pre-class handout)
  quiz\
    quiz_sc_part1.html              (Task 5 - Quiz SC-1, 20 questions)
    quiz_sc_part2.html              (Task 6 - Quiz SC-2, 20 questions)
    quiz_sc_part3.html              (Task 7 - Quiz SC-3, 20 questions)
    quiz_sc_part4.html              (Task 8 - Quiz SC-4, 20 questions)
  index.html                        (Task 9 - GitHub Pages update)
```
