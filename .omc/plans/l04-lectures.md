# Plan: L04 ERC-20 Token Creation -- Standalone Lecture Bundle

## Context

### Original Request
Create the full L04 (ERC-20 Token Creation) standalone lecture bundle and add all materials to the GitHub Pages index.

### Source Material
- `D:/Joerg/Research/slides/cryptocurrency/04_erc20_token_creation/04_erc20_token_creation.tex` (1677 lines, 33 content frames, 5 sections)
- Sections: Token Standards, ERC-20 Functions Deep Dive, Build MyToken, Token Economics, Advanced Topics & Summary

### Design Decision: LIGHT Code
Only 3-4 frames in the technical lecture will contain `lstlisting` code blocks. All other frames use TikZ diagrams, pgfplots charts, booktabs tables, and visual explanations. This is the defining constraint for this bundle.

---

## Work Objectives

### Core Objective
Produce 6 deliverable files (4 LaTeX + 4 HTML quizzes) plus update index.html, following the exact patterns established by L01-L03 bundles.

### Deliverables
1. `lectures/erc20_token_intro.tex` -- Mini-lecture (10 frames, TikZ comics)
2. `lectures/erc20_token_creation_intro.tex` -- INTRO preview (6 frames, charts)
3. `lectures/erc20_token_creation_preclass.tex` -- Pre-class handout (article, 4 activities)
4. `lectures/erc20_token_creation.tex` -- Technical lecture (~55 frames)
5. `quiz/quiz_tc_part1.html` -- Quiz: Token Standards & ERC-20 Interface (20 questions)
6. `quiz/quiz_tc_part2.html` -- Quiz: ERC-20 Functions & Mechanics (20 questions)
7. `quiz/quiz_tc_part3.html` -- Quiz: Building & Deploying Tokens (20 questions)
8. `quiz/quiz_tc_part4.html` -- Quiz: Token Economics & Security (20 questions)
9. `index.html` -- Updated with TC subsection, sidebar links, hero stat bump

### Definition of Done
- All 4 LaTeX files compile without errors using `pdflatex` (double-pass)
- All 4 quiz HTML files load in browser with working KaTeX, scoring, 3-column layout
- index.html displays TC subsection correctly after ES subsection
- Hero stats show: 16 Lectures, 20 Quizzes
- Sidebar has 4 new TC links
- Frame counts: mini=10, intro=6, preclass=2 pages, technical=~55
- Only 3-4 frames in technical lecture use `[fragile]` + lstlisting

---

## Must Have / Must NOT Have

### Must Have
- Compact preamble style for technical lecture (matches `cryptography_security.tex`)
- Verbose preamble style for mini-lecture (matches `blockchain_intro.tex`)
- Article preamble style for pre-class (matches `ethereum_smart_contracts_preclass.tex`)
- Solidity language definition + colors (from `ethereum_smart_contracts.tex` lines 14-44)
- `[fragile]` on every frame that contains lstlisting
- `\bottomnote{}` on every content frame
- `colortbl` package loaded if `\rowcolor` used
- TikZ diagrams as primary visual tool (not code blocks)
- Quiz data format: `{"id":N,"question":"...","options":{"A":"...","B":"...","C":"...","D":"..."},"correct":"X","explanation":"..."}`

### Must NOT Have
- `\rowcolors` combined with `\multicolumn` (known crash)
- `\$` inside pgfplots symbolic x coords (infinite recursion)
- `\lightning` or other symbols requiring non-loaded packages
- `\begin{verbatim}` inside `\activitybox` macro (use `\ttfamily\small`)
- `mindmap` TikZ library unless explicitly loaded in `\usetikzlibrary`
- More than 4 frames with lstlisting code in the technical lecture
- Any frame with lstlisting that lacks `[fragile]`

---

## Task Flow and Dependencies

```
T1 (mini-lecture) ----\
T2 (INTRO preview) ----\
T3 (pre-class handout) --> T6 (index.html update)
T4 (technical lecture) --/
T5 (4 quizzes) ---------/
```

T1-T5 are independent and can execute in parallel.
T6 depends on knowing exact filenames from T1-T5 (already specified, so can also run in parallel).

---

## T1: Mini-Lecture (`lectures/erc20_token_intro.tex`)

### Preamble
Use verbose preamble pattern from `lectures/ethereum_intro.tex` (lines 1-91):
- `\documentclass[8pt,aspectratio=169]{beamer}`, Madrid theme
- Separate `\usepackage` per package
- 12 colors: 10 ml* + lightgray + midgray
- Solidity colors: solkeyword, solstring, solcomment, solnumber
- Solidity `\lstdefinelanguage{Solidity}{...}` block (from ethereum_intro.tex lines 34-45)
- `\usetikzlibrary{arrows.meta, positioning, shapes.geometric, shapes.symbols, calc, decorations.pathmorphing, mindmap}`
- Title: `ERC-20 Token Creation: A Visual Introduction`
- Subtitle: `Standalone Mini-Lecture`
- Author: `Prof.~Dr.~Joerg Osterrieder`
- Institute: `University Lecture Series`

### Frame Spec (10 frames total)

**Frame 1: Title**
- `[plain]` frame
- Centered: title in `\Huge\color{mlpurple}`, subtitle in `\Large\color{mlblue}`
- Tagline quote: `"Your own money -- with rules you write"`
- Author, institute, date

**Frame 2: The Custom Currency Problem (Comic Strip 1)**
- 3-panel TikZ comic strip
- Panel 1: Alice wants to create reward points for her cafe but they only work on paper
- Panel 2: Bob says "What if we could make digital tokens that work everywhere?"
- Panel 3: Speech bubble: "ERC-20 -- one standard, every wallet, every exchange"
- Stick figures with speech bubbles, `mlpurple`/`mlblue` palette

**Frame 3: What Makes a Token? (Visual Diagram)**
- TikZ comparison diagram: left side = physical coins/bills, right side = digital tokens
- Arrow from "Smart Contract" node to token properties: programmable, transferable, divisible
- Color-coded property boxes
- `\bottomnote{Tokens are smart contracts that track balances -- they are programmable money}`

**Frame 4: The ERC-20 Standard (Architecture Diagram)**
- TikZ architecture diagram showing ERC-20 as interface layer
- Top: Wallets, Exchanges, DeFi protocols (consumer boxes)
- Middle: ERC-20 Standard Interface (wide purple bar)
- Bottom: Individual token contracts (USDC, LINK, UNI, etc.)
- Arrows showing how standard enables interoperability
- `\bottomnote{ERC-20 defines 6 functions and 2 events that every fungible token must implement}`

**Frame 5: Transfer vs Approve (Comic Strip 2)**
- 3-panel comic
- Panel 1: Direct transfer -- Alice sends tokens directly to Bob (simple arrow)
- Panel 2: Approval -- Alice approves DEX to spend her tokens (giving permission)
- Panel 3: TransferFrom -- DEX moves tokens from Alice to pool on her behalf
- Clear visual distinction between `transfer()` and `approve()+transferFrom()`

**Frame 6: Token Supply Models (Visual)**
- TikZ triple diagram (three side-by-side boxes):
  - Fixed: flat horizontal line with "21M cap" label (Bitcoin-like)
  - Inflationary: upward curve with mint arrows
  - Deflationary: downward curve with burn flames
- Simple, conceptual -- no pgfplots (just TikZ shapes)
- `\bottomnote{Token economics (tokenomics) determine long-term value and sustainability}`

**Frame 7: Building Your Token (Flow Diagram)**
- TikZ flowchart: Write -> Compile -> Test -> Deploy
- Each step as a rounded box with icon-like TikZ drawing
- Tools labeled: Solidity, Hardhat, Local Node, Testnet
- Color progression: mlblue -> mlgreen -> mlorange -> mlred
- `\bottomnote{The development workflow follows: write, compile, test locally, deploy to testnet}`

**Frame 8: Real Tokens in the Wild (Data Snapshot)**
- TikZ-drawn table (not booktabs -- use TikZ rectangles for visual appeal):
  - USDC: Stablecoin, $25B supply
  - LINK: Oracle utility, 1B fixed
  - UNI: Governance, inflationary
  - BNB: Exchange utility, deflationary
- Each row color-coded by token type
- `\bottomnote{Over 500,000 ERC-20 tokens exist on Ethereum alone}`

**Frame 9: Security -- The Fine Print (Comic Strip 3)**
- 3-panel comic
- Panel 1: Developer deploys token happily
- Panel 2: Hacker finds exploit (reentrancy bug depicted)
- Panel 3: OpenZeppelin shield appears -- "Use audited libraries!"
- Warning emphasis without being alarmist
- `\bottomnote{Smart contract bugs are permanent -- use OpenZeppelin and get audits before mainnet}`

**Frame 10: Key Takeaways**
- TikZ mind map or summary boxes (5 items):
  1. Tokens = smart contracts tracking balances
  2. ERC-20 = universal standard (6 functions, 2 events)
  3. OpenZeppelin = security foundation
  4. Tokenomics = design matters (supply, distribution)
  5. Test everything before mainnet
- `\bottomnote{Next: Deep dive into ERC-20 functions, building MyToken, and token economics}`

### Acceptance Criteria (T1)
- Exactly 10 frames including title
- No lstlisting code anywhere (pure TikZ visuals)
- All TikZ compiles without errors
- Comic panels use stick-figure style consistent with ethereum_intro.tex

---

## T2: INTRO Preview (`lectures/erc20_token_creation_intro.tex`)

### Preamble
Use compact preamble pattern from `lectures/ethereum_smart_contracts_intro.tex` (lines 1-35):
- Single-line `\usepackage{graphicx,booktabs,...}`
- 10 ml* colors + solkeyword only
- `\usepackage{tikz,pgfplots}`, `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc}`
- Title: `ERC-20 Token Creation: Course Preview`
- Subtitle: `INTRO Preview`

### Frame Spec (6 frames total)

**Frame 1: Title**
- `\titlepage`

**Frame 2: Why Token Standards Matter**
- pgfplots ybar chart comparing:
  - Token ecosystem stats: Number of ERC-20 tokens (500K+), Daily transfers (2M+), Total value locked ($50B+)
  - Use symbolic x coords with safe keys: `{Tokens, Transfers, TVL}`
  - `xticklabels={ERC-20 Tokens (500K+), Daily Transfers (2M+), TVL (\$50B+)}`
- Right column: 4 bullet points on why standards enable the ecosystem
- `\bottomnote{ERC-20 is the most widely adopted token standard in crypto history}`

**Frame 3: The ERC-20 Interface at a Glance**
- TikZ diagram: central "ERC-20" box connected to 6 function boxes and 2 event boxes
- Functions grouped: Read (totalSupply, balanceOf), Transfer (transfer, transferFrom), Approve (approve, allowance)
- Events: Transfer, Approval
- Color-coded by category
- `\bottomnote{Any contract implementing these 8 elements is ERC-20 compliant}`

**Frame 4: Token Economics Spectrum**
- pgfplots line chart showing 3 supply curves over time (x: Years, y: Supply):
  - Fixed supply (flat line at 1M)
  - Inflationary (growing curve, 2% annual)
  - Deflationary (declining curve via burns)
- Use `\addplot` with coordinates (not symbolic x)
- Legend in top-left
- `\bottomnote{Supply model choice fundamentally shapes token value and adoption}`

**Frame 5: Course Coverage**
- TikZ 5-box roadmap (identical style to ethereum_smart_contracts_intro.tex Frame 2):
  - S1: Token Standards
  - S2: ERC-20 Functions
  - S3: Build MyToken
  - S4: Token Economics
  - S5: Advanced & Summary
- Arrows between boxes, annotations below each
- `\bottomnote{From standards to deployment in 55 frames}`

**Frame 6: What You Will Build**
- Two-column layout:
  - Left: Bulleted list of deliverables (MyToken contract, deploy script, test suite, tokenomics design)
  - Right: TikZ architecture diagram showing MyToken with features: mint, burn, batchTransfer, cap
- `\bottomnote{By the end you will deploy your own ERC-20 token to a testnet}`

### Acceptance Criteria (T2)
- Exactly 6 frames including title
- No lstlisting code (charts and diagrams only)
- pgfplots uses safe symbolic coords pattern (simple keys + xticklabels)
- Compiles with pdflatex in 2 passes

---

## T3: Pre-Class Handout (`lectures/erc20_token_creation_preclass.tex`)

### Preamble
Use article preamble pattern from `lectures/ethereum_smart_contracts_preclass.tex` (lines 1-58):
- `\documentclass[11pt,a4paper]{article}`
- Packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, verbatim, amsmath
- 12 colors (HTML format): mlblue, mlpurple, mllavender, mllavender2, mllavender3, mllavender4, mlorange, mlgreen, mlred, mlgray, lightgray, midgray
- Section formatting with `\titleformat`
- Header: `\textbf{ERC-20 Token Creation} \textcolor{mlgray}{|} Lesson 04 \textcolor{mlgray}{|} Pre-Class Discovery Handout`
- `\activitybox{title}{time}{content}` macro
- `\fillcell` macro for tables

### Document Title Block
```
{\LARGE\color{mlpurple}\textbf{ERC-20 Token Creation}}\\[4pt]
{\large\color{mlblue}Pre-Class Discovery Handout}\\[2pt]
{\small\color{mlgray}Lesson 04 $\cdot$ Complete before class $\cdot$ 25--30 minutes}
```

### Activity Spec (4 activities)

**Activity 1: Explore ERC-20 Tokens on Etherscan (10 min)**
```
\activitybox{Activity 1: Explore ERC-20 Tokens on Etherscan}{10 min}{%
Visit \url{https://etherscan.io/tokens} and pick any ERC-20 token from the top 20. Answer:
\begin{enumerate}
\item What is the token's name, symbol, and contract address?
\item What is the total supply? How many holders does it have?
\item Click the \textbf{Contract} tab -- is the source code verified? What Solidity version was used?
\item Find a recent Transfer event in the \textbf{Events} tab. Who sent tokens to whom, and how many?
\end{enumerate}
\textbf{Bonus:} Check the token's \textbf{Read Contract} tab. Call {\ttfamily\small totalSupply()} and {\ttfamily\small decimals()}. What do they return?
}
```

**Activity 2: ERC-20 Function Matching (5 min)**
```
\activitybox{Activity 2: ERC-20 Function Matching}{5 min}{%
Match each ERC-20 function to its purpose. Write the letter in the blank:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lrl}
\toprule
\textbf{Function} & & \textbf{Purpose} \\
\midrule
{\ttfamily\small totalSupply()}       & \fillcell & A. Check how many tokens a spender can use \\
{\ttfamily\small balanceOf(addr)}     & \fillcell & B. Move tokens on someone else's behalf \\
{\ttfamily\small transfer(to,amt)}    & \fillcell & C. Return the total tokens in existence \\
{\ttfamily\small approve(spender,amt)}& \fillcell & D. Return the token balance of an address \\
{\ttfamily\small allowance(own,sp)}   & \fillcell & E. Send tokens directly from your wallet \\
{\ttfamily\small transferFrom(f,t,a)} & \fillcell & F. Authorize another address to spend tokens \\
\bottomrule
\end{tabular}
\end{center}
}
```

**Activity 3: Token Economics Comparison (10 min)**
```
\activitybox{Activity 3: Token Economics Comparison}{10 min}{%
Research these real tokens and fill in the table:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lcccc}
\toprule
\textbf{Token} & \textbf{Supply Model} & \textbf{Max Supply} & \textbf{Use Case} & \textbf{Standard} \\
\midrule
USDC   & \fillcell & \fillcell & \fillcell & \fillcell \\
LINK   & \fillcell & \fillcell & \fillcell & \fillcell \\
UNI    & \fillcell & \fillcell & \fillcell & \fillcell \\
BNB    & \fillcell & \fillcell & \fillcell & \fillcell \\
\bottomrule
\end{tabular}
\end{center}
\textit{Hint: Use CoinGecko or CoinMarketCap for supply data. Check ``Supply Model'' = Fixed / Inflationary / Deflationary / Elastic.}
}
```

**Activity 4: Design Your Token (5 min)**
```
\activitybox{Activity 4: Design Your Token}{5 min}{%
Before class, sketch your own token design. Fill in:
\begin{enumerate}
\item \textbf{Name:} \fillcell \quad \textbf{Symbol:} \fillcell \quad \textbf{Decimals:} \fillcell
\item \textbf{Supply Model:} $\square$ Fixed \quad $\square$ Inflationary (capped) \quad $\square$ Deflationary
\item \textbf{Max Supply:} \fillcell \quad \textbf{Initial Supply:} \fillcell
\item \textbf{Distribution:} Team \fillcell\% \quad Community \fillcell\% \quad Ecosystem \fillcell\% \quad Liquidity \fillcell\%
\item \textbf{Special Feature} (pick one): $\square$ Burn-on-transfer \quad $\square$ Batch airdrop \quad $\square$ Vesting schedule \quad $\square$ Other: \fillcell
\end{enumerate}
\textit{Bring this design to class -- you will implement it as your MyToken contract!}
}
```

### Acceptance Criteria (T3)
- Fits on exactly 2 pages (A4)
- No `\begin{verbatim}` inside `\activitybox` (use `\ttfamily\small` for code references)
- All 4 activities render correctly
- Total estimated time: 30 minutes
- Compiles with pdflatex in 1 pass

---

## T4: Technical Lecture (`lectures/erc20_token_creation.tex`)

### Preamble
Use compact preamble from `lectures/ethereum_smart_contracts.tex` (lines 1-52) as base:
- Single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- 10 ml* colors
- Solidity colors: solkeyword, solstring, solcomment, solnumber
- All beamer theme settings (lines 19-30)
- `\bottomnote` macro (line 31)
- Solidity language definition (lines 33-43)
- `\lstset{language=Solidity,...}` (line 44)
- `\usepackage{tikz,pgfplots}`, `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- **DO NOT** load `mindmap` library (not needed)
- Title: `ERC-20 Token Creation: A Quantitative Deep Dive`
- Subtitle: `Standalone Technical Lecture`

### KEY CONSTRAINT: Only frames marked [CODE] below use lstlisting (exactly 4 frames)
All other frames use TikZ, pgfplots, booktabs tables, and bullets.

### Complete Frame Spec (~57 frames including title + section dividers)

---

#### Section 0: Opening (3 frames)

**Frame 1: Title**
- `\titlepage`

**Frame 2: Lecture Roadmap**
- TikZ 5-box roadmap (same style as ethereum_smart_contracts.tex Frame 2):
  - Box 1: Token Standards (mlblue!25)
  - Box 2: ERC-20 Functions (mlgreen!20)
  - Box 3: Build MyToken (mlorange!20)
  - Box 4: Token Economics (mlred!15)
  - Box 5: Advanced & Summary (mlpurple!20)
- Arrows between boxes
- Below: Two-column `Learning Objectives` and `Prerequisites`
- `\bottomnote{Duration: 90 minutes | 5 sections | ~55 frames | Prerequisite: Lessons 1-3}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- Duration/prerequisite footer

---

#### Section 1: Token Standards (11 frames: 1 divider + 10 content)

**Frame 4: Section Divider -- Token Standards**
- Centered beamercolorbox: `Section 1: Token Standards`
- Subtitle: `Understanding the building blocks of digital assets`

**Frame 5: What is a Token?**
- Two-column: Left = Coins vs Tokens comparison (bullets), Right = Token use cases (6 bullet categories)
- TikZ: small icon-like boxes for each use case (Utility, Governance, Security, Stablecoin, NFT, Gaming)
- `\bottomnote{Over 500,000 tokens exist on Ethereum alone, demonstrating the power of token standards}`

**Frame 6: Tokens vs Coins -- Visual Comparison**
- TikZ diagram:
  - Left: "Native Coins" box with BTC, ETH, SOL logos (circles) -- own blockchain
  - Right: "ERC-20 Tokens" box with USDC, LINK, UNI -- run ON Ethereum
  - Central arrow: "Built on top of" pointing from tokens to Ethereum base layer
- `\bottomnote{Coins have their own blockchain; tokens are smart contracts on an existing chain}`

**Frame 7: Why Standards Matter**
- Two-column: Left = Without Standards (red X bullets), Right = With Standards (green check bullets)
- Block: Real-world analogy (gift cards)
- `\bottomnote{ERC = Ethereum Request for Comments | ERC-20 proposed 2015 by Fabian Vogelsteller}`

**Frame 8: The Standardization Timeline**
- TikZ timeline (horizontal):
  - 2015: ERC-20 proposed
  - 2017: ICO boom (ERC-20 explosion)
  - 2018: ERC-721 (NFTs)
  - 2019: ERC-1155 (Multi-token)
  - 2022: ERC-4626 (Vaults)
- Color-coded dots on timeline
- `\bottomnote{Token standards evolved to meet increasingly complex DeFi and NFT use cases}`

**Frame 9: ERC-20 -- The Fungible Token Standard**
- Two-column: Left = definition + fungibility explanation, Right = the interface spec (6 functions + 2 events listed)
- `\bottomnote{Any contract implementing these 6 functions and 2 events is ERC-20 compliant}`

**Frame 10: ERC-20 Interface Architecture**
- Full-width TikZ architecture diagram:
  - Top layer: Consumer apps (Wallets, DEXs, Lending, Portfolio trackers) as boxes
  - Middle: "IERC20 Interface" wide bar with 6 function signatures
  - Bottom: Individual token contracts (each a small box)
  - Arrows: consumers call interface, interface implemented by tokens
- `\bottomnote{The interface pattern enables any new wallet to instantly support any new token}`

**Frame 11: ERC-20 Function Categories**
- TikZ: Three grouped boxes
  - READ (blue): totalSupply(), balanceOf()
  - WRITE-DIRECT (green): transfer()
  - WRITE-DELEGATED (orange): approve(), allowance(), transferFrom()
- Event boxes below: Transfer, Approval
- `\bottomnote{Read functions cost no gas; write functions require a transaction and gas payment}`

**Frame 12: Other Token Standards Comparison**
- Three-column: ERC-721, ERC-1155, ERC-4626 descriptions
- Table at bottom: Standard | Fungible | Use Case | Year
- `\bottomnote{This lecture focuses on ERC-20; other standards build on similar patterns}`

**Frame 13: Token Ecosystem Market Map**
- TikZ visual: concentric circles or grid showing token categories:
  - Center: ERC-20
  - Ring 1: Stablecoins (USDC, DAI, USDT)
  - Ring 2: DeFi (UNI, AAVE, COMP)
  - Ring 3: Utility (LINK, GRT, FIL)
  - Ring 4: Meme (SHIB, PEPE)
- `\bottomnote{The token ecosystem spans from serious financial infrastructure to community-driven experiments}`

**Frame 14: Section 1 Summary -- Key Numbers**
- TikZ "stat card" layout (4 large number boxes):
  - 500K+ ERC-20 tokens on Ethereum
  - 6 required functions
  - 2 required events
  - 2015: year standard proposed
- `\bottomnote{Token standards are the foundation of the entire DeFi ecosystem}`

---

#### Section 2: ERC-20 Functions Deep Dive (13 frames: 1 divider + 12 content)

**Frame 15: Section Divider -- ERC-20 Functions Deep Dive**
- Centered: `Section 2: ERC-20 Functions Deep Dive`
- Subtitle: `Understanding each function in detail`

**Frame 16: totalSupply() and balanceOf() -- Visual**
- TikZ diagram showing:
  - A "Total Supply" meter/gauge at top (showing 1,000,000)
  - Below: mapping visualization -- address boxes pointing to balance amounts
  - Arrows labeled `totalSupply()` and `balanceOf(addr)`
- `\bottomnote{These are view functions -- they read blockchain state without modifying it}`

**Frame 17: The Balance Mapping -- How Tokens Are Stored**
- TikZ visualization of `mapping(address => uint256)`:
  - Left column: 4 Ethereum addresses (truncated hex)
  - Right column: balance amounts
  - Arrows connecting them
  - Caption: "The entire token 'ledger' is just one mapping"
- `\bottomnote{Unlike bank databases, token balances are stored publicly on-chain in a simple mapping}`

**Frame 18: transfer() -- Direct Transfer Flow**
- TikZ flow diagram (no code):
  - Step 1: Caller sends tx with (to, amount)
  - Step 2: Contract checks sender balance >= amount
  - Step 3: Subtract from sender, add to recipient
  - Step 4: Emit Transfer event
  - Step 5: Return true
- Color-coded steps with arrows
- `\bottomnote{transfer() is the simplest token movement -- you send your own tokens directly}`

**Frame 19: transfer() Safety Checks**
- TikZ: Decision tree diagram
  - Is `to` the zero address? -> REVERT
  - Is sender balance >= amount? -> No: REVERT, Yes: continue
  - Execute transfer -> Emit event -> Return true
- Red/green path coloring
- `\bottomnote{Every token function must validate inputs before modifying state -- checks-effects-interactions}`

**Frame 20: approve() and allowance() -- The Delegation Pattern**
- TikZ: Three-actor diagram
  - Owner (left), Spender (middle, e.g., DEX), Recipient (right)
  - Step 1: Owner calls approve(spender, amount)
  - Step 2: Allowance mapping updated
  - Arrow notation showing the delegation relationship
- Real-world analogy: "Like giving a debit card with a spending limit"
- `\bottomnote{Approvals are essential for DeFi -- they let smart contracts move tokens on your behalf}`

**Frame 21: The Allowance Mapping**
- TikZ: nested mapping visualization
  - `mapping(address => mapping(address => uint256))`
  - Outer: Owner addresses
  - Inner: Spender addresses with allowance amounts
  - Grid/matrix visualization
- `\bottomnote{The double mapping allows each owner to set independent allowances for multiple spenders}`

**Frame 22: transferFrom() -- Delegated Transfer**
- TikZ: Complete flow diagram
  - Step 1: Spender calls transferFrom(from, to, amount)
  - Step 2: Check allowance[from][spender] >= amount
  - Step 3: Check balance[from] >= amount
  - Step 4: Deduct allowance, transfer tokens
  - Step 5: Emit Transfer event
- Real-world example callout: "Uniswap calls transferFrom when you swap"
- `\bottomnote{transferFrom() is the workhorse of DeFi -- every swap, lend, and stake uses it}`

**Frame 23: Approval Attack -- The Race Condition**
- TikZ: timing diagram showing the approve race condition
  - Timeline 1: Owner approves 100
  - Timeline 2: Owner changes to 50
  - Problem: Spender can spend 100 + 50 = 150 in between
  - Solution: Set to 0 first, then to new value
- `\bottomnote{The approval race condition is a known ERC-20 issue -- always reset to 0 before changing}`

**Frame 24: Events -- Transfer and Approval**
- TikZ: Event emission diagram
  - Transfer event: from/to/value fields with "indexed" tags
  - Approval event: owner/spender/value fields with "indexed" tags
  - Arrows to consumers: Block explorers, Wallets, DeFi dashboards
- `\bottomnote{Events are stored in transaction logs -- cheap storage but cannot be read by other contracts}`

**Frame 25: How Events Power the Ecosystem**
- TikZ: Event flow architecture
  - Smart contract emits events
  - Events stored in logs (blocks)
  - Indexed by topics (up to 3)
  - Consumed by: Etherscan, MetaMask, The Graph, custom dApps
- `\bottomnote{Without events, there would be no way to efficiently track token transfers off-chain}`

**Frame 26: [CODE] Complete ERC-20 Skeleton**
- `[fragile]` frame
- lstlisting with Solidity style: minimal ERC-20 contract (~25 lines)
  - State variables: name, symbol, decimals, totalSupply
  - The two mappings (_balances, _allowances)
  - Both events
  - Constructor with initial mint
  - balanceOf, transfer (signatures only, body as comments)
- `\bottomnote{This skeleton shows the minimal structure -- production code should use OpenZeppelin}`

**Frame 27: Function Gas Costs Comparison**
- pgfplots horizontal bar chart:
  - totalSupply(): ~2.5K gas (view, free externally)
  - balanceOf(): ~2.5K gas (view)
  - transfer(): ~52K gas
  - approve(): ~46K gas
  - transferFrom(): ~60K gas
  - batchTransfer(10): ~300K gas
- `\bottomnote{View functions are free when called externally; write functions cost real ETH in gas}`

---

#### Section 3: Build MyToken (12 frames: 1 divider + 11 content)

**Frame 28: Section Divider -- Build MyToken**
- Centered: `Section 3: Build MyToken`
- Subtitle: `Hands-on: Creating a complete ERC-20 token`

**Frame 29: MyToken Specification**
- Two-column: Left = spec table (Name, Symbol, Decimals, Max Supply, Initial Supply), Right = features and inheritance
- Same table content as original slide 15 but using booktabs table
- `\bottomnote{This design balances simplicity with useful features for learning and experimentation}`

**Frame 30: Design Architecture**
- TikZ: Inheritance diagram
  - OpenZeppelin ERC20 box (top-left, blue)
  - OpenZeppelin Ownable box (top-right, green)
  - MyToken box (bottom center, purple) with arrows "is" pointing up to both
  - MyToken custom functions listed inside: mint(), burn(), burnFrom(), batchTransfer()
- `\bottomnote{Multiple inheritance lets MyToken combine standard token functionality with access control}`

**Frame 31: OpenZeppelin -- Why Not Reinvent the Wheel?**
- Two-column comparison:
  - Left: "Writing from scratch" with red X items (1000+ lines, unaudited, error-prone)
  - Right: "Using OpenZeppelin" with green check items (8 lines, battle-tested, audited)
- TikZ: Shield icon with "1B+ value secured" callout
- `\bottomnote{OpenZeppelin contracts secure over \$1 billion in value -- never reinvent the wheel}`

**Frame 32: [CODE] MyToken.sol -- The Complete Contract**
- `[fragile]` frame
- lstlisting: The full MyToken contract (~30 lines):
  ```solidity
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.20;
  import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
  import "@openzeppelin/contracts/access/Ownable.sol";
  contract MyToken is ERC20, Ownable {
      uint256 public constant MAX_SUPPLY = 1000000 * 10**18;
      constructor() ERC20("MyToken", "MTK") Ownable(msg.sender) {
          _mint(msg.sender, 100000 * 10**18);
      }
      function mint(address to, uint256 amount) public onlyOwner {
          require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
          _mint(to, amount);
      }
      function burn(uint256 amount) public { _burn(msg.sender, amount); }
      function batchTransfer(address[] calldata to, uint256[] calldata amt) public {
          require(to.length == amt.length, "Length mismatch");
          for (uint i = 0; i < to.length; i++) _transfer(msg.sender, to[i], amt[i]);
      }
  }
  ```
- `\bottomnote{Full contract: ~20 lines of custom code plus all inherited ERC-20 and Ownable functionality}`

**Frame 33: Constructor Deep Dive**
- TikZ: Step-by-step constructor execution diagram
  - Step 1: ERC20("MyToken", "MTK") sets name and symbol
  - Step 2: Ownable(msg.sender) sets deployer as owner
  - Step 3: _mint(msg.sender, 100000 * 10**18) creates initial tokens
  - Visual: boxes with arrows showing state changes
- `\bottomnote{The constructor runs exactly once during deployment -- it initializes all inherited contracts}`

**Frame 34: The 10^18 Decimals Explained**
- TikZ: Scale diagram
  - 1 token (human-readable) = 10^18 base units (on-chain)
  - Like: 1 ETH = 10^18 wei
  - Visual: zoom into a "1 MTK" coin showing it contains 10^18 atomic units
  - Comparison table: ETH/wei, USD/cents, MTK/base units
- `\bottomnote{18 decimals allow fractional token amounts down to 0.000000000000000001 MTK}`

**Frame 35: Mint Function -- Supply Control**
- TikZ: Mint flow diagram
  - Guard 1: onlyOwner modifier (who can call?)
  - Guard 2: totalSupply() + amount <= MAX_SUPPLY (cap check)
  - Action: _mint(to, amount)
  - Result: new tokens created, balance updated, Transfer event emitted
  - Visual: "Tokens appear from address(0)"
- `\bottomnote{The MAX\_SUPPLY cap prevents unlimited inflation -- a key tokenomics design decision}`

**Frame 36: Burn Function -- Deflationary Mechanics**
- TikZ: Burn flow diagram (mirror of mint)
  - burn(): sender burns own tokens
  - burnFrom(): requires allowance first
  - Action: _burn(from, amount)
  - Result: tokens destroyed, sent to address(0), Transfer event emitted
  - Visual: "Tokens vanish to address(0)" with flame icon
- `\bottomnote{Burning reduces total supply permanently -- creating scarcity and potential value appreciation}`

**Frame 37: Batch Transfer -- Efficiency Pattern**
- TikZ: Visual comparison
  - Left: "N separate transactions" (N boxes, each with gas cost)
  - Right: "1 batch transaction" (single box, one gas overhead)
  - Gas savings calculation: N*52K vs 1*overhead + N*25K internal
- `\bottomnote{Batch transfers save gas for airdrops and payroll -- one transaction instead of many}`

**Frame 38: Development Workflow**
- TikZ: 6-step workflow diagram (horizontal chain)
  - Setup: mkdir, npm init, hardhat init
  - Install: OpenZeppelin contracts
  - Write: MyToken.sol
  - Compile: npx hardhat compile
  - Test: npx hardhat test
  - Deploy: npx hardhat run scripts/deploy.js
- Each step as a rounded box with tool icon
- `\bottomnote{Hardhat is the most popular Ethereum development environment}`

**Frame 39: [CODE] Deploy Script**
- `[fragile]` frame
- lstlisting with JavaScript style:
  ```javascript
  const hre = require("hardhat");
  async function main() {
      const [deployer] = await hre.ethers.getSigners();
      console.log("Deploying with:", deployer.address);
      const MyToken = await hre.ethers.getContractFactory("MyToken");
      const token = await MyToken.deploy();
      await token.waitForDeployment();
      console.log("MyToken deployed to:", await token.getAddress());
  }
  main().catch(e => { console.error(e); process.exit(1); });
  ```
- Need to add `\lstdefinestyle{javascript}{...}` in preamble (same as original source lines 81-100, but simpler: just keywords and basic style)
- Alternatively, use the Solidity style with `language=` override
- `\bottomnote{Run: npx hardhat run scripts/deploy.js --network localhost}`

**Frame 40: Testing Strategy**
- TikZ: Test pyramid
  - Bottom (wide): Unit tests -- individual functions (transfer, mint, burn)
  - Middle: Integration tests -- multi-step flows (approve + transferFrom)
  - Top (narrow): End-to-end -- deploy + interact on local chain
- Right: Test categories with example counts
- `\bottomnote{Always test on local network first, then testnet, and only then consider mainnet}`

---

#### Section 4: Token Economics (11 frames: 1 divider + 10 content)

**Frame 41: Section Divider -- Token Economics**
- Centered: `Section 4: Token Economics`
- Subtitle: `Designing sustainable token models`

**Frame 42: Supply Models -- The Big Three**
- pgfplots chart: 3 supply curves over 10 years
  - Fixed: flat line at 1M
  - Inflationary: concave curve from 500K to 1.2M (2% annual)
  - Deflationary: convex curve from 1M down to 700K (1% burn)
- x-axis: Years (0-10), y-axis: Supply (thousands)
- `\bottomnote{Token economics (tokenomics) significantly impacts long-term value and utility}`

**Frame 43: Fixed Supply -- Digital Scarcity**
- TikZ: Bitcoin-style halving chart
  - Visual blocks showing decreasing issuance over time
  - Total cap: 21M BTC, 1M MTK
  - Scarcity argument with demand/supply arrows
- Pros/cons bullets in two columns
- `\bottomnote{Fixed supply creates predictable scarcity -- but cannot adapt to ecosystem growth}`

**Frame 44: Inflationary Models -- Rewarding Participation**
- TikZ: Flow diagram showing mint -> distribution -> staking -> rewards loop
  - Staking rewards cycle
  - Inflation rate governance
  - Examples: ETH post-merge (~0.5%), UNI (2% annual)
- `\bottomnote{Inflationary models incentivize participation but must balance against dilution}`

**Frame 45: Deflationary Models -- Burn Mechanics**
- TikZ: Burn mechanism diagram
  - Sources: transaction fees, buyback-and-burn, manual burns
  - Visual: tokens flowing into "burn furnace" (address(0))
  - Examples: BNB quarterly burns, EIP-1559 base fee burn
- `\bottomnote{Deflationary pressure increases scarcity -- but excessive burning can reduce liquidity}`

**Frame 46: Distribution Strategies**
- Two-column with table and bullets (from original slide 25)
- Table: Method | Typical %
  - Team & Founders: 15-20%
  - Investors/VCs: 10-20%
  - Public Sale: 10-30%
  - Community/Airdrops: 10-20%
  - Ecosystem Fund: 20-30%
  - Liquidity: 5-15%
- Right: Vesting schedules, green/red flags
- `\bottomnote{Transparent tokenomics build trust -- always publish distribution details}`

**Frame 47: Distribution Visualization**
- pgfplots pie chart or TikZ pie:
  - 5 slices showing typical distribution for a well-designed token
  - Color-coded with percentages
  - Legend at bottom
- `\bottomnote{Distribution determines initial decentralization and long-term governance power}`

**Frame 48: Vesting Schedules -- Preventing Dumps**
- TikZ: Vesting timeline diagram
  - Cliff period (6-12 months): 0% unlocked
  - Linear vesting (12-36 months): gradual unlock
  - Full unlock milestone
  - Comparison: "With vesting" (gradual) vs "Without" (instant dump risk)
- `\bottomnote{Vesting protects early investors by preventing large token dumps after launch}`

**Frame 49: Real-World Token Economics**
- Table (from original slide 26): Token | Type | Supply Model | Max Supply | Use Case
  - USDC, LINK, UNI, AAVE, BNB, MATIC
- Two-column below: Successful patterns + Questions to ask
- `\bottomnote{Study successful tokens to understand what makes sustainable token economics}`

**Frame 50: [CODE] Tokenomics in Code**
- `[fragile]` frame
- lstlisting: 3 small code snippets side by side showing supply model implementations
  - Fixed: constructor mints MAX_SUPPLY, no mint function
  - Inflationary: mint function with onlyOwner
  - Deflationary: transfer override with fee burn
- Keep code minimal (~15 lines total across 3 snippets)
- `\bottomnote{Supply model choice is encoded permanently in the smart contract -- choose wisely}`

**Frame 51: Token Valuation Frameworks**
- TikZ: Framework comparison
  - Equation of Exchange: MV = PQ adapted for tokens
  - Network Value: Metcalfe's law (V proportional to n^2)
  - Discounted Utility: future cash flows from token use
- Qualitative overview (no complex math)
- `\bottomnote{Token valuation is an emerging field -- no single framework captures all value drivers}`

---

#### Section 5: Advanced Topics & Summary (8 frames: 1 divider + 7 content)

**Frame 52: Section Divider -- Advanced Topics & Summary**
- Centered: `Section 5: Advanced Topics & Summary`
- Subtitle: `Next steps and key takeaways`

**Frame 53: Deployment Workflow -- Local to Mainnet**
- TikZ: 4-stage deployment pipeline
  - Stage 1: Local Hardhat node (green, safe)
  - Stage 2: Testnet (Sepolia) (yellow, practice)
  - Stage 3: Audit (orange, verification)
  - Stage 4: Mainnet (red, real money)
- Gates between stages with requirements
- `\bottomnote{Each stage adds risk -- never skip testing stages}`

**Frame 54: Testnet Deployment Guide**
- Table: Network | Faucet | Speed (Sepolia, Goerli, Mumbai)
- TikZ: 5-step visual process
  - Get testnet ETH -> Configure Hardhat -> Set env vars -> Deploy -> Verify on Etherscan
- `\bottomnote{Testnet deployment is essential practice -- treat it like production}`

**Frame 55: Security Considerations**
- alertblock: Disclaimer about educational code
- Two-column: Common vulnerabilities (red) / Best practices (green)
  - Reentrancy, integer overflow, access control, front-running, approval race
  - OpenZeppelin, checks-effects-interactions, ReentrancyGuard, Pausable, multi-sig
- `\bottomnote{Smart contract bugs are permanent and can result in total loss of funds}`

**Frame 56: Security Tools Landscape**
- TikZ: Tool categories diagram
  - Static analysis: Slither, Solhint
  - Symbolic execution: Mythril, Manticore
  - Formal verification: Certora, K Framework
  - Audit firms: OpenZeppelin, Trail of Bits, Consensys Diligence
- `\bottomnote{Use multiple security tools -- no single tool catches everything}`

**Frame 57: Final Project Overview**
- Two-column: Project spec (deliverables) / Evaluation criteria
  - Custom token, test suite, testnet deploy, README
  - Code quality, test coverage, security, creativity
- `\bottomnote{This project integrates all 4 lessons: blockchain, cryptography, smart contracts, and tokens}`

**Frame 58: Key Takeaways**
- TikZ: 5 key takeaway boxes (one per section)
  - S1: Tokens = programmable money on smart contracts
  - S2: 6 functions + 2 events = universal interface
  - S3: OpenZeppelin + Hardhat = professional toolchain
  - S4: Tokenomics determines long-term success
  - S5: Security first -- always audit before mainnet
- `\bottomnote{You now have the foundation to build, deploy, and evaluate ERC-20 tokens}`

**Frame 59: Course Completion**
- Table: Course summary (4 lessons)
- Two-column: "You can now" / "Continue learning"
  - Continue: NFTs, DeFi, DAOs, L2, Security auditing
- `\bottomnote{The blockchain space evolves rapidly -- continuous learning is essential}`

### Frame Count Summary
- Opening: 3 (title, roadmap, TOC)
- Section 1: 11 (1 divider + 10 content)
- Section 2: 13 (1 divider + 12 content)
- Section 3: 13 (1 divider + 12 content -- note: includes frame 40 testing strategy but frame 28-40 = 13)
- Section 4: 11 (1 divider + 10 content)
- Section 5: 8 (1 divider + 7 content)
- **Total: 59 frames** (including 5 section dividers and 1 title = 53 content frames)

### Code Frames (exactly 4 with [fragile]):
1. Frame 26: Complete ERC-20 Skeleton
2. Frame 32: MyToken.sol Complete Contract
3. Frame 39: Deploy Script (JavaScript)
4. Frame 50: Tokenomics in Code (3 small snippets)

### Acceptance Criteria (T4)
- Frame count between 55-60
- Exactly 4 frames use lstlisting + [fragile]
- All other frames use TikZ/pgfplots/tables
- No pgfplots symbolic coords with `\$` characters
- No `\rowcolors` + `\multicolumn` combinations
- `colortbl` loaded for any `\rowcolor` usage
- Every content frame has `\bottomnote{}`
- Compiles with pdflatex double-pass

---

## T5: Quizzes (4 HTML files)

### Template
Use exact HTML/CSS/JS from `quiz/quiz_cs_part1.html`. Key elements:
- KaTeX CDN (v0.16.9)
- CSS variables: --mlpurple, --mlblue, --quiz-accent, etc.
- Nav bar: title, link back to index
- 3-column grid layout
- Quiz data format: `const quizData = { questions: [{id, question, options:{A,B,C,D}, correct, explanation}] }`
- JavaScript: initQuiz, renderQuestions, selectAnswer, advanceQuestions, showResults

### Quiz TC-1: Token Standards & ERC-20 Interface (20 questions)
**File:** `quiz/quiz_tc_part1.html`
**Title:** `Quiz TC-1: Token Standards & ERC-20 Interface`
**Topic coverage:**
- Q1-5: Tokens vs coins, token use cases
- Q6-10: Why standards matter, interoperability
- Q11-15: ERC-20 required functions and events
- Q16-18: Other standards (ERC-721, ERC-1155, ERC-4626)
- Q19-20: Fungibility, token standard history

### Quiz TC-2: ERC-20 Functions & Mechanics (20 questions)
**File:** `quiz/quiz_tc_part2.html`
**Title:** `Quiz TC-2: ERC-20 Functions & Mechanics`
**Topic coverage:**
- Q1-4: totalSupply(), balanceOf(), view functions
- Q5-8: transfer() mechanics, safety checks, gas costs
- Q9-12: approve(), allowance(), delegation pattern
- Q13-16: transferFrom(), the approve+transferFrom flow
- Q17-18: Events (Transfer, Approval), indexed parameters
- Q19-20: Approval race condition, gas costs comparison

### Quiz TC-3: Building & Deploying Tokens (20 questions)
**File:** `quiz/quiz_tc_part3.html`
**Title:** `Quiz TC-3: Building & Deploying Tokens`
**Topic coverage:**
- Q1-4: OpenZeppelin benefits, inheritance
- Q5-8: Constructor, decimals (10^18), initial minting
- Q9-12: mint() with onlyOwner, MAX_SUPPLY cap, burn mechanics
- Q13-16: batchTransfer, development workflow (Hardhat)
- Q17-18: Compilation artifacts, testing strategy
- Q19-20: Deploy scripts, Hardhat commands

### Quiz TC-4: Token Economics & Security (20 questions)
**File:** `quiz/quiz_tc_part4.html`
**Title:** `Quiz TC-4: Token Economics & Security`
**Topic coverage:**
- Q1-4: Fixed/inflationary/deflationary supply models
- Q5-8: Distribution strategies, vesting schedules
- Q9-12: Real-world token economics (USDC, LINK, UNI, BNB)
- Q13-15: Token valuation frameworks
- Q16-18: Security vulnerabilities (reentrancy, front-running, approval race)
- Q19-20: Security best practices, audit tools, mainnet readiness

### Acceptance Criteria (T5)
- Each quiz has exactly 20 questions
- Each question has exactly 4 options (A-D)
- Correct answer is a single letter string
- Explanation provided for every question
- KaTeX renders any math (e.g., `$10^{18}$`, `$O(n)$`)
- Nav title matches quiz identifier
- All quiz files follow identical HTML structure

---

## T6: Index.html Update

### Changes Required

**1. Hero Stats (line 153)**
Change:
```html
<span><b>12</b><small>Lectures</small></span>
```
To:
```html
<span><b>16</b><small>Lectures</small></span>
```

Change:
```html
<span><b>16</b><small>Quizzes</small></span>
```
To:
```html
<span><b>20</b><small>Quizzes</small></span>
```

**2. Sidebar -- Add TC links (after line 147, before `</details>` at line 148)**
Insert:
```html
<a href="#sl-tc-mini">Mini-Lecture: Tokens</a>
<a href="#sl-tc-intro">TC INTRO Preview</a>
<a href="#sl-tc-pre">TC Pre-Class Handout</a>
<a href="#sl-tc-main">TC Technical Lecture</a>
```

**3. New TC Subsection (after ES section closing `</div>` at approximately line 421, before notebooks section)**
Insert full TC subsection block following the exact pattern of the ES subsection (lines 377-421):
```html
<div class="section-head d5" style="margin-top:16px"><span>TC</span><h2>Standalone Lectures: ERC-20 Token Creation</h2></div>

<div class="lec-subsection">Mini-Lecture</div>
<div class="lec-grid">
<a href="lectures/erc20_token_intro.pdf" class="lec-card" id="sl-tc-mini">
<div><span class="lec-num">TC</span><span class="lec-title">ERC-20 Token Creation</span></div>
<div class="lec-meta">10-slide visual introduction with TikZ comics</div>
</a>
</div>

<div class="lec-subsection">Technical Lecture Bundle</div>
<div class="lec-grid">
<a href="lectures/erc20_token_creation_intro.pdf" class="lec-card" id="sl-tc-intro">
<div><span class="lec-num">INTRO</span><span class="lec-title">TC Course Preview</span></div>
<div class="lec-meta">6-slide preview deck with charts</div>
</a>
<a href="lectures/erc20_token_creation_preclass.pdf" class="lec-card" id="sl-tc-pre">
<div><span class="lec-num">PRE</span><span class="lec-title">Pre-Class Handout</span></div>
<div class="lec-meta">2-page discovery activities</div>
</a>
<a href="lectures/erc20_token_creation.pdf" class="lec-card" id="sl-tc-main">
<div><span class="lec-num">90min</span><span class="lec-title">ERC-20 Token Creation</span></div>
<div class="lec-meta">55+ frame quantitative deep dive</div>
</a>
</div>

<div class="lec-subsection">Associated Quizzes</div>
<div class="quiz-grid">
<a href="quiz/quiz_tc_part1.html" class="quiz-card">
<div><span class="quiz-num">TC-1</span><span class="quiz-title">Token Standards & ERC-20 Interface</span></div>
<div class="quiz-meta">20 questions</div>
</a>
<a href="quiz/quiz_tc_part2.html" class="quiz-card">
<div><span class="quiz-num">TC-2</span><span class="quiz-title">ERC-20 Functions & Mechanics</span></div>
<div class="quiz-meta">20 questions</div>
</a>
<a href="quiz/quiz_tc_part3.html" class="quiz-card">
<div><span class="quiz-num">TC-3</span><span class="quiz-title">Building & Deploying Tokens</span></div>
<div class="quiz-meta">20 questions</div>
</a>
<a href="quiz/quiz_tc_part4.html" class="quiz-card">
<div><span class="quiz-num">TC-4</span><span class="quiz-title">Token Economics & Security</span></div>
<div class="quiz-meta">20 questions</div>
</a>
</div>
```

### Acceptance Criteria (T6)
- Hero stats show 16 Lectures and 20 Quizzes
- Sidebar has 4 TC entries under Standalone Lectures
- TC subsection appears after ES subsection, before notebooks section
- All 4 lecture PDFs and 4 quiz HTML links resolve correctly
- HTML is valid, no broken tags

---

## Risk Mitigations

| Risk | Mitigation |
|------|------------|
| pgfplots `\$` in symbolic coords | Use simple keys (`Tokens`, `Transfers`) + `xticklabels` for display text |
| `\rowcolors` + `\multicolumn` crash | Do not use `\rowcolors`; use manual `\rowcolor` per row if needed |
| `\begin{verbatim}` in activitybox | Use `{\ttfamily\small code}` instead |
| lstlisting without `[fragile]` | All 4 code frames explicitly marked `[fragile]` in plan |
| Missing `colortbl` package | Included in preamble `\usepackage{...,colortbl}` |
| TikZ mindmap without library | Do not use mindmap style; use regular TikZ nodes instead |
| Quiz KaTeX rendering | Test `$10^{18}$` and `$O(n)$` patterns render correctly |
| Frame overflow (too dense) | Target ~55-59 frames; cut section 4 or 5 if needed |
| JavaScript lstdefinestyle | Add simple JavaScript style in preamble for Frame 39 |

---

## Execution Order

Recommended parallel execution:
- **Batch 1 (parallel):** T1, T2, T3, T5 (all independent)
- **Batch 2 (parallel with batch 1 if filenames known):** T4 (longest task)
- **Batch 3 (after all):** T6 (index.html update)

Within T4, the executor should write frames in section order, ensuring the 4 [fragile] code frames are placed exactly at positions 26, 32, 39, and 50.

---

## Commit Strategy

| Commit | Contents |
|--------|----------|
| 1 | Add L04 mini-lecture (erc20_token_intro.tex) |
| 2 | Add L04 INTRO preview (erc20_token_creation_intro.tex) |
| 3 | Add L04 pre-class handout (erc20_token_creation_preclass.tex) |
| 4 | Add L04 technical lecture (erc20_token_creation.tex) |
| 5 | Add L04 quizzes (quiz_tc_part1-4.html) |
| 6 | Update index.html with TC subsection and stats |

Alternative: single commit "Add L04 ERC-20 Token Creation standalone lecture bundle" if preferred.

---

## Success Criteria

1. All 4 LaTeX files compile without errors (`pdflatex` double-pass)
2. All 4 quiz HTML files load correctly in browser
3. index.html renders TC subsection and updated stats
4. Technical lecture has exactly 4 `[fragile]` code frames
5. Technical lecture has 55-60 total frames
6. Mini-lecture has exactly 10 frames
7. INTRO preview has exactly 6 frames
8. Pre-class handout fits on 2 A4 pages
9. Each quiz has exactly 20 questions with proper format
