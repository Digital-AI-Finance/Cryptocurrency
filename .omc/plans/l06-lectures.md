# Plan: L06 NFTs & Digital Assets -- Standalone Lecture Bundle

## Context

### Original Request
Create the full L06 (NFTs & Digital Assets) standalone lecture bundle and add all materials to the GitHub Pages index.

### Reference Material (Templates)
- `D:/Joerg/Research/slides/cryptocurrency/lectures/defi_fundamentals.tex` -- Tech lecture template (55 frames, 5 sections, 3 fragile/code frames)
- `D:/Joerg/Research/slides/cryptocurrency/lectures/defi_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble)
- `D:/Joerg/Research/slides/cryptocurrency/lectures/defi_fundamentals_intro.tex` -- INTRO preview template (6 frames, compact preamble)
- `D:/Joerg/Research/slides/cryptocurrency/lectures/defi_fundamentals_preclass.tex` -- Pre-class handout template (article class, 4 activities)
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_df_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data)
- `D:/Joerg/Research/slides/cryptocurrency/index.html` -- GitHub Pages (DF subsection pattern at lines 476-513)

### Design Decision: LIGHT Code
Only 3-4 frames in the technical lecture will contain `lstlisting` code blocks. All other frames use TikZ diagrams, pgfplots charts, booktabs tables, and visual explanations. This is the defining constraint for this bundle.

---

## Work Objectives

### Core Objective
Produce 9 deliverable files (4 LaTeX + 4 HTML quizzes + 1 HTML update) following the exact patterns established by L04-L05 bundles.

### Deliverables
1. `lectures/nft_intro.tex` -- Mini-lecture (10 frames, TikZ comics, NO code)
2. `lectures/nft_digital_assets_intro.tex` -- INTRO preview (6 frames, charts/diagrams)
3. `lectures/nft_digital_assets_preclass.tex` -- Pre-class handout (article, 4 activities, glossary)
4. `lectures/nft_digital_assets.tex` -- Technical lecture (~55 frames, 5 sections)
5. `quiz/quiz_nf_part1.html` -- Quiz NF-1: NFT Fundamentals & Standards (20 questions)
6. `quiz/quiz_nf_part2.html` -- Quiz NF-2: NFT Marketplaces & Trading (20 questions)
7. `quiz/quiz_nf_part3.html` -- Quiz NF-3: NFT Applications & Use Cases (20 questions)
8. `quiz/quiz_nf_part4.html` -- Quiz NF-4: NFT Valuation, Advanced Topics & Future (20 questions)
9. `index.html` -- Updated with NF subsection, sidebar links, hero stat bump

### Definition of Done
- All 4 LaTeX files compile without errors using `pdflatex` (double-pass)
- All 4 quiz HTML files load in browser with working KaTeX, scoring, 3-column layout
- index.html displays NF subsection correctly after DF subsection
- Hero stats show: 24 Lectures, 28 Quizzes
- Sidebar has 4 new NF links (sl-nf-mini, sl-nf-intro, sl-nf-pre, sl-nf-main)
- Frame counts: mini=10, intro=6, preclass=2 pages, technical=~55
- Only 3-4 frames in technical lecture use `[fragile]` + lstlisting

---

## Must Have / Must NOT Have

### Must Have
- Compact preamble for technical lecture (match `defi_fundamentals.tex` lines 1-52 exactly)
- Verbose preamble for mini-lecture (match `defi_intro.tex` lines 1-84 exactly)
- Compact preamble for INTRO preview (match `defi_fundamentals_intro.tex` lines 1-36 exactly)
- Article preamble for pre-class (match `defi_fundamentals_preclass.tex` lines 1-59 exactly)
- Color palette: mlblue (#0066CC), mlpurple (#3333B2), mllavender (4 shades), mlorange, mlgreen, mlred, mlgray
- Solidity language definition + colors (solkeyword, solstring, solcomment, solnumber)
- `[fragile]` on every frame that contains lstlisting
- `\bottomnote{}` on every content frame (not on title/section dividers)
- `colortbl` package loaded in compact preamble
- TikZ diagrams as primary visual tool (not code blocks)
- Quiz data format: `{"id":N,"question":"...","options":{"A":"...","B":"...","C":"...","D":"..."},"correct":"X","explanation":"..."}`
- Quiz prefix: NF (NF-1, NF-2, NF-3, NF-4)
- KaTeX v0.16.9 in quiz HTML
- `\activitybox` macro in pre-class handout
- `\fillcell` macro in pre-class handout

### Must NOT Have
- `\foreach` with `/` multi-variable syntax in TikZ (known LaTeX crash)
- Parameterized styles with `#1` in TikZ (known LaTeX crash)
- Style names conflicting with pgf built-ins: `diamond`, `step`, `text` (known crash)
- `\\` inside TikZ nodes without `align=center` (missing text causes crash)
- `\rowcolors` combined with `\multicolumn` (known crash)
- `\$` inside pgfplots symbolic x coords (infinite recursion)
- `\lightning` or other symbols requiring non-loaded packages
- `\begin{verbatim}` inside `\activitybox` macro (use `\ttfamily\small`)
- `mindmap` TikZ library unless explicitly loaded in `\usetikzlibrary`
- More than 4 frames with lstlisting code in the technical lecture
- Any frame with lstlisting that lacks `[fragile]`
- Code in the mini-lecture (zero code frames)

---

## Task Flow and Dependencies

```
T1 (mini-lecture) --------\
T2 (INTRO preview) --------\
T3 (pre-class handout) -----> T6 (index.html update)
T4 (technical lecture) ----/
T5 (4 quizzes) -----------/
```

T1-T5 are independent and can execute in parallel.
T6 depends on knowing exact filenames from T1-T5 (already specified, so can also run in parallel).

---

## T1: Mini-Lecture (`lectures/nft_intro.tex`)

### Preamble
Use verbose preamble pattern from `lectures/defi_intro.tex` (lines 1-84):
- `\documentclass[8pt,aspectratio=169]{beamer}`, Madrid theme
- Separate `\usepackage` per package (graphicx, booktabs, adjustbox, multicol, amsmath, amssymb, listings, xcolor)
- 12 colors: 10 ml* + lightgray + midgray
- Solidity colors: solkeyword, solstring, solcomment, solnumber
- Solidity `\lstdefinelanguage{Solidity}{...}` block
- Additional beamer colors: section in toc, subsection in toc
- `\setbeamertemplate{enumerate items}[default]`
- `\usetikzlibrary{arrows.meta, positioning, shapes.geometric, shapes.symbols, calc, decorations.pathmorphing, mindmap}`
- Title: `NFTs \& Digital Assets: A Visual Introduction`
- Subtitle: `Standalone Mini-Lecture`
- Author: `Prof.~Dr.~Joerg Osterrieder`
- Institute: `University Lecture Series`

### Frame Spec (10 frames total)

**Frame 1: Title**
- `[plain]` frame
- Centered: title in `\Huge\color{mlpurple}`, subtitle in `\Large\color{mlblue}`
- Tagline quote: `"Own the original -- in a world of infinite copies"`
- Author, institute, date
- Gray rule separator (`\textcolor{mlgray}{\rule{6cm}{0.4pt}}`)

**Frame 2: The Digital Ownership Problem (Comic Strip 1)**
- 3-panel TikZ comic strip using `[remember picture, overlay]`
- Panel borders: `\draw[thick, mlpurple/mlblue/mlgreen, rounded corners=3pt]` at positions (0.1,0.2)-(4.0,4.2), (4.3,0.2)-(8.2,4.2), (8.5,0.2)-(12.4,4.2)
- Panel 1: Alice creates digital art on a laptop, but anyone can right-click and copy it. Stick figure + laptop + art on screen.
- Panel 2: Bob asks "How do you prove you made it? Or that you own it?" Speech bubble with puzzled expression.
- Panel 3: Shows a blockchain certificate/token glowing with "NFT -- Proof of ownership on the blockchain!" Smart contract icon with checkmark.
- `\bottomnote{NFTs solve the digital ownership problem by creating verifiable scarcity on-chain.}`

**Frame 3: What is an NFT? (Visual Diagram)**
- Two-column layout: left = fungible items (dollar bills, ETH, ERC-20 tokens -- all identical), right = non-fungible items (art, house deeds, concert tickets -- each unique)
- TikZ comparison with color-coded boxes
- Fungible side in mlblue, non-fungible side in mlgreen
- Arrow/divide between them labeled "Fungible vs Non-Fungible"
- `\bottomnote{Fungible = interchangeable (every dollar is the same). Non-fungible = unique (every NFT is different).}`

**Frame 4: How NFTs Work (Architecture Diagram)**
- TikZ layered stack diagram showing:
  - Layer 1 (bottom): Ethereum blockchain (mlpurple)
  - Layer 2: Smart contract (ERC-721) (mlblue)
  - Layer 3: Token ID + Metadata URI (mlgreen)
  - Layer 4 (top): Image/Art/Asset (mlorange)
- Arrows between layers showing the connection
- Note: "The NFT lives on-chain; the art usually lives off-chain (IPFS)"
- `\bottomnote{An NFT is a smart contract entry pointing to metadata -- the media itself is usually stored off-chain.}`

**Frame 5: NFT Marketplaces (Comic Strip 2)**
- 3-panel TikZ comic strip
- Panel 1: Alice lists her NFT on a marketplace (OpenSea logo mockup). "List for 2 ETH" speech bubble. Laptop with marketplace UI drawn.
- Panel 2: Bob browses and clicks "Buy." Shows wallet connection flow. "Connecting wallet..." node.
- Panel 3: Smart contract transfers NFT to Bob, ETH to Alice. Shows bidirectional arrows. "Instant, trustless, global!" badge.
- `\bottomnote{NFT marketplaces are smart contract platforms -- no middleman holds the assets.}`

**Frame 6: Minting Your First NFT (Process Diagram)**
- TikZ process flow (horizontal steps):
  - Step 1: Create Art (mlorange)
  - Step 2: Upload to IPFS (mlblue)
  - Step 3: Deploy/Call Smart Contract (mlpurple)
  - Step 4: NFT Minted! (mlgreen)
- Stealth arrows between steps
- Below each step, a small annotation (font=\tiny, mlgray)
- `\bottomnote{Minting = creating a new NFT on the blockchain by calling a smart contract function.}`

**Frame 7: NFT Use Cases (Hub-and-Spoke Diagram)**
- Central node: "NFT Use Cases" (mlpurple, ellipse)
- 6 spoke nodes: Digital Art, Gaming Items, Music/Media, Real Estate, Event Tickets, Identity/Credentials
- Each spoke in a different color from the palette
- Lines connecting center to spokes
- `\bottomnote{NFTs extend far beyond art -- they represent any unique digital or real-world asset.}`

**Frame 8: NFTs by the Numbers (Table/Stats)**
- TikZ-drawn statistics table (similar to defi_intro.tex Frame 8 stats style)
- Header row (mlpurple fill, white text): Metric, Value, Context
- Rows: Total NFT sales volume, Number of unique buyers, Top single NFT sale (Beeple $69M), Active collections, Gaming NFT market share
- Summary bar at bottom: "NFTs peaked at $25B+ in 2021 -- now stabilising around $1-5B annually"
- `\bottomnote{Despite market cooling, NFT technology adoption continues in gaming, identity, and real-world assets.}`

**Frame 9: The Risks of NFTs (Comic Strip 3)**
- 3-panel TikZ comic strip
- Panel 1: Developer deploying NFT collection, happy stick figure. "10,000 unique NFTs!"
- Panel 2: Red warning signs -- rug pull (creator disappears), fake collections (copycat art), metadata off-chain (IPFS goes down). Hacker figure with warning symbols.
- Panel 3: Shield shape containing defenses: "Verify contracts", "Check provenance", "On-chain metadata", "Established marketplaces". Shield in mlpurple.
- `\bottomnote{NFT buyers face unique risks: rug pulls, counterfeit collections, and metadata permanence.}`

**Frame 10: Key Takeaways (Summary Boxes)**
- TikZ-drawn summary boxes (5 boxes stacked, matching defi_intro.tex Frame 10)
- Box 1 (mlblue): NFTs = unique digital tokens proving ownership and authenticity on-chain
- Box 2 (mlpurple): ERC-721 is the core standard; ERC-1155 supports both fungible and non-fungible
- Box 3 (mlgreen): Metadata lives off-chain (IPFS/Arweave); only the token ID lives on-chain
- Box 4 (mlorange): Use cases span art, gaming, music, real estate, identity, and credentials
- Box 5 (mlred): Risks include rug pulls, wash trading, metadata loss, and regulatory uncertainty
- Teaser bar (mlpurple fill, white text): "Next: Deep dive into NFT standards, valuation, and advanced topics"
- `\bottomnote{Next: Deep dive into NFT standards, valuation, and advanced topics.}`

### Acceptance Criteria (T1)
- Exactly 10 frames
- Zero code frames (no lstlisting)
- All TikZ nodes with `\\` have `align=center`
- No `\foreach` with `/` syntax
- `\bottomnote` on frames 2-10
- Compiles with `pdflatex` double-pass

---

## T2: INTRO Preview (`lectures/nft_digital_assets_intro.tex`)

### Preamble
Use compact preamble from `defi_fundamentals_intro.tex` (lines 1-36):
- `\documentclass[8pt,aspectratio=169]{beamer}`, Madrid theme
- Single `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor}`
- 10 ml* colors only (no lightgray/midgray)
- solkeyword color only (no full Solidity language def)
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc}`
- Title: `NFTs \& Digital Assets: Course Preview`
- Subtitle: `INTRO Preview`

### Frame Spec (6 frames total)

**Frame 1: Title**
- `\begin{frame}` + `\titlepage` + `\end{frame}`

**Frame 2: Why NFTs Matter**
- Two-column layout: left = pgfplots ybar chart, right = block with key metrics
- Chart: symbolic x coords = {Sales Volume, Unique Buyers, Collections}, bar data showing relative scale
- Key Metrics block (checkmark items):
  - $25B+ peak annual sales volume
  - 2M+ unique buyers/sellers
  - 100K+ active collections
  - Gaming, art, real estate applications
- `\bottomnote{NFTs are reshaping digital ownership across art, gaming, and real-world assets.}`

**Frame 3: NFT Ecosystem at a Glance**
- Hub-and-spoke TikZ diagram (matching defi_fundamentals_intro.tex Frame 3 style)
- Center node: "NFT Ecosystem" (cbox style, mlpurple fill, white text)
- 4 spoke nodes (sbox style):
  - Art & Collectibles (mlblue) -- CryptoPunks, BAYC
  - Gaming & Metaverse (mlgreen) -- Axie Infinity, The Sandbox
  - Music & Media (mlorange) -- Royal, Sound.xyz
  - Real-World Assets (mlred) -- Real estate, luxury goods
- Stealth arrows from center to spokes
- `\bottomnote{The NFT ecosystem spans digital and physical assets, with new use cases emerging rapidly.}`

**Frame 4: NFT Market Trajectory**
- Two-column layout: left = pgfplots line chart, right = block with growth drivers
- Chart: x=Year (2017-2025), y=Sales Volume (USD billions) / Collections (scaled)
  - Sales line (mlblue, solid): (2017,0.01)(2018,0.05)(2019,0.1)(2020,0.3)(2021,25)(2022,10)(2023,3)(2024,5)
  - Collections line (mlgreen, dashed): (2017,1)(2018,3)(2019,5)(2020,10)(2021,50)(2022,80)(2023,90)(2024,100)
- Growth Drivers block:
  - Profile picture (PFP) collections drove 2021 boom
  - Gaming NFTs creating sustained utility
  - Real-world asset tokenization emerging
  - Regulatory clarity improving adoption
- `\bottomnote{NFT market survived the 2022 downturn and is finding sustainable use cases.}`

**Frame 5: Course Coverage**
- TikZ process-step roadmap (matching defi_fundamentals_intro.tex Frame 5)
- 5 boxes connected by Stealth arrows:
  - (1) NFT Fundamentals
  - (2) Marketplaces & Trading
  - (3) Applications & Use Cases
  - (4) Valuation & Analytics
  - (5) Advanced & Future
- Below each box, tiny gray annotation:
  - ERC-721, ERC-1155, metadata
  - OpenSea, royalties, pricing
  - Art, gaming, RWA, music
  - Rarity, floor price, wash trading
  - Fractional, dynamic, soulbound
- Two-column block: Prerequisites (blockchain + ERC-20 knowledge) and Outcomes (evaluate NFTs quantitatively)
- `\bottomnote{From NFT fundamentals to advanced topics in 55 frames.}`

**Frame 6: What You Will Learn**
- Two-column layout: left = Learning Outcomes block, right = hub-and-spoke TikZ
- Learning Outcomes (4 checkmark items):
  - NFT standards -- ERC-721/ERC-1155 mechanics and metadata
  - Marketplace analysis -- pricing mechanisms, royalties, fees
  - Valuation metrics -- rarity scores, floor prices, wash trading detection
  - Future directions -- dynamic NFTs, soulbound tokens, regulatory landscape
- Hub node: "NFT Mastery" (mlpurple)
- 4 spoke nodes: Standards, Markets, Valuation, Future
- `\bottomnote{By the end you will be able to evaluate any NFT project quantitatively.}`

### Acceptance Criteria (T2)
- Exactly 6 frames
- Zero code frames
- All TikZ nodes with `\\` have `align=center`
- `\bottomnote` on frames 2-6
- Compiles with `pdflatex` double-pass

---

## T3: Pre-Class Handout (`lectures/nft_digital_assets_preclass.tex`)

### Preamble
Use article preamble from `defi_fundamentals_preclass.tex` (lines 1-59):
- `\documentclass[11pt,a4paper]{article}`
- geometry: margin=2cm, top=2.4cm
- Packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- HTML-format color definitions (e.g., `\definecolor{mlblue}{HTML}{0066CC}`)
- `\titleformat` for section (mlpurple, rule) and subsection (mlblue, bullet)
- fancyhdr: header = "NFTs & Digital Assets | Lesson 06 | Pre-Class Discovery Handout"
- `\activitybox` and `\fillcell` macros

### Document Title
```
\begin{center}
{\LARGE\color{mlpurple}\textbf{NFTs \& Digital Assets}}\\[4pt]
{\large\color{mlblue}Pre-Class Discovery Handout}\\[2pt]
{\small\color{mlgray}Lesson 06 $\cdot$ Complete before class $\cdot$ 25--30 minutes}
\end{center}
```

### Activity 1: Explore NFT Marketplaces (10 min)
Visit OpenSea.io and explore the marketplace. Answer:
1. What are the top 3 collections by total volume? What is the floor price of each?
2. Pick one collection -- how many total items does it have? How many unique owners?
3. Click on any individual NFT -- what metadata does it show (traits, rarity, history)?
4. Find the "Activity" tab -- what does "wash trading" look like in transaction history?
Bonus: Compare OpenSea with Blur.io. How do their fee structures differ?

### Activity 2: NFT Metadata Investigation (5 min)
Look up a CryptoPunk or BAYC NFT on etherscan.io:
1. Find the smart contract address. What standard does it implement (ERC-721 or ERC-1155)?
2. Look at the `tokenURI` function output. Where does the metadata point to (IPFS, HTTP, on-chain)?
3. If the metadata points to IPFS, what happens if the IPFS gateway goes down?
4. What is the difference between on-chain and off-chain metadata storage?
Fill-in table: Collection | Standard | Metadata Location | Risk Level

### Activity 3: NFT Valuation Comparison (10 min)
Research each collection using their official websites and NFT analytics tools:
Fill-in table with columns: Collection | Floor Price | Total Volume | Unique Holders | Rarity Tool
Rows: CryptoPunks, Bored Ape Yacht Club, Azuki, Pudgy Penguins

### Activity 4: Design Your NFT Collection (5 min)
Fill-in form:
1. Collection Name: ___
2. Collection Size: ___
3. Asset Type: [ ] Art [ ] Gaming [ ] Music [ ] Utility [ ] Identity [ ] Other
4. Metadata Storage: [ ] On-chain [ ] IPFS [ ] Arweave [ ] Centralized Server
5. Royalty Percentage: ___%
6. Target Marketplace: [ ] OpenSea [ ] Blur [ ] Magic Eden [ ] Custom
7. Risk Assessment: [ ] Metadata loss [ ] Rug pull [ ] Low liquidity [ ] Regulatory

### Glossary (12 terms)

| Term | Definition |
|------|-----------|
| **NFT** | Non-Fungible Token. A unique digital asset on a blockchain representing ownership of a specific item (art, music, game item, etc.), implemented via standards like ERC-721. |
| **ERC-721** | The Ethereum standard for non-fungible tokens. Each token has a unique ID and cannot be divided or exchanged 1:1 with another token. |
| **ERC-1155** | A multi-token standard supporting both fungible and non-fungible tokens in a single contract, enabling batch transfers and gas efficiency. |
| **Metadata** | Data describing an NFT's properties (name, description, image, traits). Usually stored off-chain (IPFS/Arweave) and referenced by a URI stored on-chain. |
| **Floor Price** | The lowest listed price for any NFT in a given collection, serving as the minimum entry price for buyers. |
| **Minting** | The process of creating a new NFT by calling a smart contract function, which assigns a unique token ID and records ownership on the blockchain. |
| **Royalties** | A percentage of secondary sales automatically sent to the original creator via smart contract enforcement (typically 2.5--10%). |
| **IPFS** | InterPlanetary File System. A decentralized storage protocol commonly used to host NFT metadata and media files, referenced via content-addressed hashes. |
| **Wash Trading** | The practice of buying and selling the same NFT between wallets controlled by the same person to artificially inflate volume and price. |
| **Soulbound Token (SBT)** | A non-transferable NFT representing credentials, reputation, or identity, proposed by Vitalik Buterin in 2022. |
| **Rarity Score** | A numerical measure of how rare an NFT's combination of traits is within a collection, often calculated using statistical methods. |
| **Token URI** | The on-chain function that returns a URL pointing to the NFT's metadata (typically a JSON file on IPFS or a centralized server). |

### Footer
`\noindent\textcolor{mlgray}{\small\textit{Prepared by Prof.\ Dr.\ Joerg Osterrieder \,\textbullet\, NFTs \& Digital Assets --- Lesson 06 \,\textbullet\, Pre-Class Discovery Handout}}`

### Acceptance Criteria (T3)
- 4 activities with timing annotations
- 12+ glossary terms in booktabs table
- `\activitybox` macro used for all 4 activities
- Header shows "NFTs & Digital Assets | Lesson 06"
- Compiles with `pdflatex` double-pass
- No `\begin{verbatim}` inside `\activitybox`

---

## T4: Technical Lecture (`lectures/nft_digital_assets.tex`)

### Preamble
Use compact preamble from `defi_fundamentals.tex` (lines 1-47):
- `\documentclass[8pt,aspectratio=169]{beamer}`, Madrid theme
- Single `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- 10 ml* colors + 4 Solidity colors
- Compact beamer color setup (lines 19-30)
- `\bottomnote` command (line 31)
- Full Solidity `\lstdefinelanguage` and `\lstset` (lines 33-44)
- `\usepackage{tikz,pgfplots}` + compat=1.18
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `NFTs \& Digital Assets: A Quantitative Deep Dive`
- Subtitle: `Standalone Technical Lecture`

### 5 Sections

| Section | Frames | Topic |
|---------|--------|-------|
| 1. NFT Fundamentals & Standards | 4-14 (11 frames) | What NFTs are, ERC-721, ERC-1155, metadata, on-chain vs off-chain |
| 2. NFT Marketplaces & Trading | 15-26 (12 frames) | OpenSea, Blur, pricing, royalties, auction mechanics, fees |
| 3. NFT Applications & Use Cases | 27-38 (12 frames) | Art, gaming, music, real-world assets, identity, credentials |
| 4. NFT Valuation & Analytics | 39-48 (10 frames) | Rarity scores, floor price, wash trading, market analysis |
| 5. Advanced Topics & Future | 49-55 (7 frames) | Fractional NFTs, dynamic NFTs, soulbound tokens, regulation, summary |

### Frame-by-Frame Specification

#### Section 0: Opening (Frames 1-3)

**Frame 1: Title** (no bottomnote)
- `\begin{frame}` + `\titlepage` + `\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ horizontal process-step diagram (5 boxes, Stealth arrows) -- match `defi_fundamentals.tex` Frame 2 exactly in style
- Boxes: (1) NFT Fundamentals, (2) Marketplaces & Trading, (3) Applications, (4) Valuation & Analytics, (5) Advanced Topics
- Colors: mlblue!25, mlgreen!20, mlorange!20, mlred!15, mlpurple!20
- Two-column block below: Learning Objectives (5 items) + Prerequisites (4 items)
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--5}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections covering NFT fundamentals to advanced topics}`

#### Section 1: NFT Fundamentals & Standards (Frames 4-14)

**Frame 4: Section Divider** (no bottomnote)
- `\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}` -- match defi_fundamentals.tex pattern exactly
- Title: "Section 1: NFT Fundamentals & Standards"
- Subtitle: "Defining NFTs, token standards, metadata, and storage"
- Two-column block: "What you will learn" (4 items) + "Frames in this section" (frame list)
- `\bottomnote{Section 1 | Frames 4--14 | NFT Fundamentals \& Standards}`

**Frame 5: What is a Non-Fungible Token?**
- Two-column layout
- Left column: Definition block + Core Properties block (5 items: unique, indivisible, verifiable, transferable, programmable)
- Right column: TikZ comparison diagram -- Fungible (3 identical blue coins) vs Non-Fungible (3 different colored unique items)
- `\bottomnote{Non-fungible means each token is unique and not interchangeable with any other token}`

**Frame 6: Fungible vs Non-Fungible: A Visual Comparison**
- Full-width TikZ table/grid
- Left half: Fungible tokens (ETH, USDC, DAI) -- each marked "= identical"
- Right half: Non-fungible (CryptoPunk #7804, BAYC #3749, Azuki #9605) -- each marked "!= unique"
- Bottom comparison row: "1 ETH = 1 ETH" vs "Punk #7804 != Punk #3100"
- `\bottomnote{Fungibility is about substitutability -- fungible tokens are interchangeable, NFTs are not}`

**Frame 7: ERC-721: The NFT Standard**
- Two-column layout
- Left: Block listing ERC-721 interface functions (balanceOf, ownerOf, transferFrom, approve, safeTransferFrom, tokenURI) as itemized list with descriptions
- Right: TikZ architecture diagram showing contract -> tokenId -> owner mapping, with metadata URI connection
- `\bottomnote{ERC-721 was proposed in January 2018 (EIP-721) and is the foundation for most NFT projects}`

**Frame 8: ERC-721 Interface [FRAGILE] -- CODE FRAME 1 of 3-4**
- `\begin{frame}[fragile]{ERC-721 Interface}`
- Two-column layout
- Left: Explanation of key functions, when each is called
- Right: `\begin{lstlisting}[language=Solidity, caption={}]` showing:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC721 {
    function balanceOf(address owner)
        external view returns (uint256);
    function ownerOf(uint256 tokenId)
        external view returns (address);
    function transferFrom(
        address from, address to,
        uint256 tokenId
    ) external;
    function approve(
        address to, uint256 tokenId
    ) external;
    function tokenURI(uint256 tokenId)
        external view returns (string memory);
}
```
- `\bottomnote{The ERC-721 interface defines the minimal functions every NFT contract must implement}`

**Frame 9: ERC-1155: The Multi-Token Standard**
- Two-column layout
- Left: Block explaining ERC-1155 advantages (batch transfers, gas efficiency, mixed fungible/non-fungible)
- Right: TikZ diagram showing single contract managing both fungible (coins) and non-fungible (unique items) tokens
- Comparison table (small, TikZ-drawn): ERC-721 vs ERC-1155 on key features
- `\bottomnote{ERC-1155 supports both fungible and non-fungible tokens in a single contract, reducing gas costs}`

**Frame 10: NFT Metadata Architecture**
- Full-width TikZ diagram showing the metadata flow:
  - On-chain: Contract -> tokenId -> tokenURI()
  - Off-chain: URI -> IPFS/Arweave/HTTP -> JSON metadata -> image/media
- JSON structure shown in a TikZ box (not lstlisting, just text):
  ```
  { "name": "...", "description": "...",
    "image": "ipfs://...", "attributes": [...] }
  ```
- Color-coded: on-chain elements in mlpurple, off-chain in mlblue, media in mlorange
- `\bottomnote{NFT metadata follows the ERC-721 Metadata JSON Schema -- name, description, image, and attributes}`

**Frame 11: On-Chain vs Off-Chain Storage**
- Comparison table (TikZ-drawn, not tabular)
- Header: Storage Method | Cost | Permanence | Decentralization | Examples
- Rows: On-chain (highest cost, permanent, fully decentralized, Art Blocks), IPFS (moderate, depends on pinning, moderate, most NFTs), Arweave (moderate, permanent, high, permaweb), HTTP/S3 (cheapest, fragile, centralized, early NFTs)
- Warning box (mlred): "If the server hosting metadata goes down, the NFT becomes a pointer to nothing"
- `\bottomnote{Storage choice is the most critical design decision for NFT longevity -- on-chain is safest but most expensive}`

**Frame 12: Token ID and Ownership Mapping**
- TikZ diagram showing the internal data structure of an ERC-721 contract:
  - `mapping(uint256 => address)` owners
  - `mapping(address => uint256)` balances
  - `mapping(uint256 => address)` approvals
- Visual: tokenIds (1, 2, 3, 4, 5) pointing to owner addresses
- Transfer flow shown with arrows
- `\bottomnote{An NFT contract is fundamentally a mapping from token IDs to owner addresses}`

**Frame 13: NFT Minting Process**
- TikZ horizontal process flow (6 steps):
  1. Creator uploads media to IPFS
  2. Gets content hash (CID)
  3. Calls mint() on contract
  4. Contract assigns new tokenId
  5. Sets tokenURI to IPFS CID
  6. Emits Transfer(0x0, creator, tokenId) event
- Each step in a rounded rectangle with Stealth arrows
- Event emission highlighted in mlorange
- `\bottomnote{Minting emits a Transfer event from the zero address -- this is how wallets and indexers detect new NFTs}`

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 items stacked, matching defi_fundamentals.tex Frame 14 style)
- Box 1 (mlblue): NFTs are unique, indivisible tokens representing ownership of specific assets
- Box 2 (mlgreen): ERC-721 is the core standard; ERC-1155 supports multi-token contracts
- Box 3 (mlorange): Metadata usually lives off-chain (IPFS/Arweave); tokenURI links on-chain to off-chain
- Box 4 (mlpurple): Storage permanence varies: on-chain > Arweave > IPFS > HTTP
- Box 5 (mlred): Minting creates a new tokenId and emits Transfer from zero address
- `\bottomnote{Section 1 complete -- next: NFT Marketplaces \& Trading}`

#### Section 2: NFT Marketplaces & Trading (Frames 15-26)

**Frame 15: Section Divider**
- Same pattern as Frame 4
- Title: "Section 2: NFT Marketplaces & Trading"
- Subtitle: "Platforms, pricing mechanics, royalties, and market structure"
- `\bottomnote{Section 2 | Frames 15--26 | NFT Marketplaces \& Trading}`

**Frame 16: NFT Marketplace Landscape**
- TikZ ecosystem map (matching Frame 7 of defi_fundamentals.tex)
- Center: "NFT Markets" (ellipse, mlpurple)
- Spokes: OpenSea (mlblue), Blur (mlgreen), Magic Eden (mlorange, Solana), LooksRare (mlred), Foundation (mlpurple), Rarible (mllavender)
- Sub-nodes under each with market share or specialty
- `\bottomnote{The NFT marketplace landscape has shifted from OpenSea dominance to competitive multi-platform trading}`

**Frame 17: How NFT Trading Works**
- TikZ flow diagram showing:
  - Seller lists NFT (sets price or starts auction)
  - Buyer connects wallet
  - Smart contract executes: NFT to buyer, ETH to seller, royalty to creator, fee to platform
  - Settlement on-chain
- All arrows labeled with what flows (NFT, ETH, fees)
- `\bottomnote{NFT trades are atomic on-chain transactions -- payment and delivery happen simultaneously}`

**Frame 18: Pricing Mechanisms**
- Three-column TikZ comparison:
  - Fixed Price: seller sets price, buyer pays it
  - English Auction: ascending bids, highest wins (traditional)
  - Dutch Auction: price descends over time, first buyer wins (used for mints)
- Each column with a small TikZ illustration of the price curve
- `\bottomnote{Dutch auctions are popular for NFT mints because they help discover fair market price}`

**Frame 19: Royalty Mechanics [FRAGILE] -- CODE FRAME 2 of 3-4**
- `\begin{frame}[fragile]{NFT Royalty Mechanics}`
- Two-column layout
- Left: Explanation of creator royalties, EIP-2981, marketplace enforcement challenges
- Right: `\begin{lstlisting}[language=Solidity, caption={}]`
```solidity
// EIP-2981 Royalty Standard
interface IERC2981 {
    function royaltyInfo(
        uint256 tokenId,
        uint256 salePrice
    ) external view returns (
        address receiver,
        uint256 royaltyAmount
    );
}
// Example: 5% royalty
// salePrice = 1 ether
// royaltyAmount = 0.05 ether
```
- `\bottomnote{EIP-2981 standardizes royalty queries but enforcement depends on marketplace cooperation}`

**Frame 20: Marketplace Fee Comparison**
- TikZ-drawn comparison table
- Header: Platform | Trading Fee | Creator Royalty | Optional Royalty? | Chain
- Rows: OpenSea (2.5%, yes, optional, Ethereum), Blur (0%, optional, yes, Ethereum), Magic Eden (2%, optional, yes, Solana), LooksRare (2%, yes, optional, Ethereum), Foundation (5%, yes, enforced, Ethereum)
- Color-coded rows
- `\bottomnote{The royalty wars of 2022-23 led most platforms to make creator royalties optional}`

**Frame 21: Floor Price Mechanics**
- TikZ diagram showing a collection's price distribution
- pgfplots bar chart: x-axis = listed price ranges, y-axis = number of listings
- Floor price marked with a red dashed line at the lowest bar
- Annotations: "Floor sweep" (buying up cheap listings), "Paper hands" (selling below floor)
- `\bottomnote{Floor price is the minimum entry cost for a collection -- it is the most-watched metric in NFT trading}`

**Frame 22: Order Book vs AMM for NFTs**
- Two-column comparison
- Left: Traditional order book model (OpenSea) -- TikZ with bid/ask columns
- Right: AMM model for NFTs (Sudoswap) -- TikZ with bonding curve
- Sudoswap bonding curve formula: `price = base + delta * n`
- `\bottomnote{NFT AMMs like Sudoswap bring instant liquidity but work best for floor-priced items}`

**Frame 23: NFT Lending and Collateralization**
- TikZ diagram showing NFT-collateralized lending:
  - User deposits NFT as collateral
  - Protocol lends ETH/stablecoins
  - If price drops below threshold: liquidation
- Protocols mentioned: NFTfi, BendDAO, Blend (by Blur)
- `\bottomnote{NFT lending unlocks liquidity for holders without selling -- but liquidation risk is significant due to illiquidity}`

**Frame 24: Wash Trading Detection**
- TikZ flow diagram showing wash trading pattern:
  - Wallet A sells to Wallet B (same owner)
  - Price inflated artificially
  - Volume appears high
- Detection methods: cluster analysis, profit analysis, timing patterns
- Warning statistics: "Estimated 40-70% of NFT volume in 2022 was wash trading"
- `\bottomnote{Wash trading inflates volume metrics -- always verify organic trading activity before investing}`

**Frame 25: Gas Costs and Layer-2 NFTs**
- TikZ comparison showing gas costs:
  - Ethereum mainnet: mint = ~$5-50, transfer = ~$2-20
  - Polygon: mint = ~$0.01, transfer = ~$0.001
  - Optimism/Arbitrum: intermediate costs
  - Solana (for reference): near-zero
- Bar chart showing relative costs
- `\bottomnote{Layer-2 and alternative chains dramatically reduce NFT gas costs, enabling mass-market adoption}`

**Frame 26: Section 2 Summary**
- 5 stacked summary boxes (same style as Frame 14)
- `\bottomnote{Section 2 complete -- next: NFT Applications \& Use Cases}`

#### Section 3: NFT Applications & Use Cases (Frames 27-38)

**Frame 27: Section Divider**
- Title: "Section 3: NFT Applications & Use Cases"
- `\bottomnote{Section 3 | Frames 27--38 | NFT Applications \& Use Cases}`

**Frame 28: Digital Art NFTs**
- Two-column: left = key milestones (Beeple $69M, CryptoPunks, Art Blocks generative), right = TikZ timeline of art NFT history
- `\bottomnote{Digital art NFTs proved that verifiable scarcity can create real value for digital creators}`

**Frame 29: Profile Picture (PFP) Collections**
- TikZ diagram showing PFP collection structure:
  - Base layers + trait layers = unique combinations
  - Example: 10,000 items, 7 trait categories, 150+ trait values
  - Rarity distribution visualization
- Key collections: CryptoPunks, BAYC, Azuki, Doodles
- `\bottomnote{PFP collections use algorithmic generation to create thousands of unique but thematically consistent NFTs}`

**Frame 30: Generative Art NFTs**
- Explanation of on-chain generative art (Art Blocks model)
- TikZ diagram: transaction hash -> random seed -> generative algorithm -> unique artwork
- Key insight: art is created at mint time, not before
- `\bottomnote{Generative art NFTs are unique because the artwork is created on-chain at the moment of minting}`

**Frame 31: Gaming NFTs**
- TikZ ecosystem showing gaming NFT flow:
  - Player earns in-game items (NFTs)
  - Items tradeable on marketplace
  - Interoperable across games (theoretical)
- Examples: Axie Infinity (play-to-earn), The Sandbox (virtual land), Gods Unchained (trading cards)
- `\bottomnote{Gaming NFTs give players true ownership of in-game assets -- but interoperability remains largely theoretical}`

**Frame 32: Music and Media NFTs**
- TikZ flow showing creator -> mint music NFT -> fans purchase -> royalties flow back
- Platforms: Royal (fractional music ownership), Sound.xyz (limited editions), Audius (streaming)
- Comparison: traditional streaming ($0.003/play) vs NFT patronage model
- `\bottomnote{Music NFTs let artists earn directly from fans without intermediary platforms taking 70-80\% of revenue}`

**Frame 33: Real-World Asset (RWA) Tokenization**
- TikZ process flow:
  - Physical asset (real estate, luxury goods, fine art)
  - Legal wrapper (SPV/LLC)
  - NFT representation on-chain
  - Fractional ownership possible
- Examples: Propy (real estate), Courtyard (luxury goods), 4K (wine)
- `\bottomnote{RWA tokenization bridges physical and digital ownership -- legal frameworks are still evolving}`

**Frame 34: Identity and Credential NFTs**
- TikZ diagram showing:
  - University diploma as SBT (soulbound token)
  - Professional certifications
  - Event attendance (POAPs)
  - Membership passes
- Key distinction: transferable vs non-transferable (soulbound)
- `\bottomnote{Credential NFTs and soulbound tokens may replace traditional paper certificates and membership cards}`

**Frame 35: Domain Names as NFTs**
- TikZ architecture: ENS (.eth) and Unstoppable Domains
- Shows: wallet address -> human-readable name -> NFT ownership
- Process: register name -> NFT minted -> resolves to address
- `\bottomnote{Blockchain domain names are NFTs that map human-readable names to wallet addresses}`

**Frame 36: NFT Ticketing**
- TikZ event flow: organizer mints ticket NFTs -> fans purchase -> attend event -> ticket becomes collectible POAP
- Advantages: anti-counterfeiting, secondary market control, post-event utility
- `\bottomnote{NFT tickets solve counterfeiting while giving organizers control over secondary market pricing}`

**Frame 37: Intellectual Property and Licensing**
- TikZ IP licensing flow:
  - Creator mints NFT with commercial rights
  - Buyer gets specific rights (CC0, commercial use, derivative rights)
  - Smart contract tracks licensing chain
- Examples: BAYC commercial rights, CC0 collections (Nouns, Moonbirds pivot)
- `\bottomnote{NFTs can encode intellectual property rights -- but legal enforcement is still evolving}`

**Frame 38: Section 3 Summary**
- 5 stacked summary boxes
- `\bottomnote{Section 3 complete -- next: NFT Valuation \& Analytics}`

#### Section 4: NFT Valuation & Analytics (Frames 39-48)

**Frame 39: Section Divider**
- Title: "Section 4: NFT Valuation & Analytics"
- `\bottomnote{Section 4 | Frames 39--48 | NFT Valuation \& Analytics}`

**Frame 40: NFT Valuation Challenges**
- Two-column: left = block listing challenges (illiquidity, subjectivity, wash trading, no cash flows), right = TikZ comparison of traditional asset valuation vs NFT valuation
- `\bottomnote{NFT valuation is fundamentally different from traditional finance -- there are no discounted cash flow models}`

**Frame 41: Rarity Scoring Methods**
- TikZ diagram showing rarity calculation:
  - Trait frequency method: `rarity = 1 / (trait_frequency)`
  - Statistical rarity: product of all trait probabilities
  - Information content: `-log2(probability)`
- Example: 10,000 collection, trait appears 500 times -> frequency = 5% -> rarity = 20
- `\bottomnote{Rarity scores quantify how uncommon an NFT's trait combination is within its collection}`

**Frame 42: Rarity Score Worked Example**
- Full-width TikZ calculation walkthrough:
  - NFT with 5 traits, each trait's frequency shown
  - Step-by-step rarity calculation
  - Final normalized score
- Fill-in table format (similar to AMM calculation in defi preclass)
- `\bottomnote{Always verify rarity rankings across multiple tools -- different methods can produce different rankings}`

**Frame 43: Floor Price Analysis**
- pgfplots chart: x-axis = time (30 days), y-axis = floor price (ETH)
- Line chart with support/resistance annotations
- Metrics below: 7d change, 30d change, all-time high, all-time low
- `\bottomnote{Floor price trends reveal market sentiment -- sustained floor above previous lows signals strength}`

**Frame 44: NFT Market Metrics Table**
- TikZ-drawn metrics table (matching Frame 11 of defi_fundamentals.tex style)
- Metrics: Floor Price, Market Cap (floor * supply), Volume (24h/7d), Unique Holders (%), Listed Ratio, Royalty Revenue
- Columns: Metric, Definition, Typical Range, Significance
- `\bottomnote{These six metrics provide a quantitative framework for evaluating any NFT collection}`

**Frame 45: Wash Trading Analytics**
- pgfplots chart showing real vs inflated volume
- Two lines: reported volume (mlblue) vs estimated organic volume (mlgreen)
- Detection heuristics listed: self-trading, circular patterns, unprofitable trades
- `\bottomnote{Research estimates 40-70\% of NFT trading volume in 2022 was wash trading -- always verify organic metrics}`

**Frame 46: NFT Index Construction**
- TikZ diagram showing how NFT price indices are built:
  - Repeat sales method (like Case-Shiller for real estate)
  - Hedonic regression (trait-based pricing)
  - Machine learning approaches
- Formula: `P(t) = alpha + sum(beta_j * trait_j) + epsilon`
- `\bottomnote{NFT indices are essential for portfolio analysis but face sparse data and selection bias challenges}`

**Frame 47: Portfolio Analysis with NFTs**
- TikZ diagram showing NFT as alternative asset in portfolio:
  - Correlation matrix visualization (NFTs vs BTC, ETH, S&P 500)
  - Diversification benefit discussion
  - Liquidity risk highlighted
- `\bottomnote{NFTs show low correlation with traditional assets but high illiquidity risk limits their portfolio utility}`

**Frame 48: Section 4 Summary**
- 5 stacked summary boxes
- `\bottomnote{Section 4 complete -- next: Advanced Topics \& Future}`

#### Section 5: Advanced Topics & Future (Frames 49-55)

**Frame 49: Section Divider**
- Title: "Section 5: Advanced Topics & Future"
- `\bottomnote{Section 5 | Frames 49--55 | Advanced Topics \& Future}`

**Frame 50: Fractional NFTs [FRAGILE] -- CODE FRAME 3 of 3-4**
- `\begin{frame}[fragile]{Fractional NFTs}`
- Two-column layout
- Left: Explanation of fractionalizing high-value NFTs, vault mechanics, ERC-20 fractions
- Right: `\begin{lstlisting}[language=Solidity, caption={}]`
```solidity
// Simplified NFT Fractionalization
contract FractionalVault {
    IERC721 public nft;
    uint256 public tokenId;
    ERC20 public fractions;

    function fractionalize(
        address _nft, uint256 _id,
        uint256 totalFractions
    ) external {
        IERC721(_nft).transferFrom(
            msg.sender, address(this), _id
        );
        fractions.mint(
            msg.sender, totalFractions
        );
    }
}
```
- `\bottomnote{Fractional NFTs lower the barrier to entry for expensive collections by splitting ownership into ERC-20 tokens}`

**Frame 51: Dynamic NFTs (dNFTs)**
- TikZ diagram showing dynamic NFT mechanics:
  - On-chain trigger (oracle, time, user action)
  - Metadata update
  - Visual change
- Examples: sports NFTs that update with player stats, weather-responsive art, game character evolution
- `\bottomnote{Dynamic NFTs can change their metadata based on external data -- blurring the line between static and interactive}`

**Frame 52: Soulbound Tokens (SBTs)**
- TikZ diagram showing SBT properties:
  - Non-transferable (no transfer function)
  - Tied to identity/address
  - Use cases: diplomas, certifications, reputation, DAO voting history
- Vitalik Buterin's 2022 paper reference
- `\bottomnote{Soulbound tokens represent identity and reputation -- they cannot be bought or sold, only earned}`

**Frame 53: NFT Composability and Nesting**
- TikZ diagram showing:
  - ERC-6551: token-bound accounts (NFTs owning other NFTs)
  - Nested NFTs (game character carrying equipment items)
  - Composable NFTs (combining traits from multiple tokens)
- `\bottomnote{ERC-6551 gives every NFT its own wallet, enabling NFTs to own assets and interact with protocols}`

**Frame 54: NFT Regulation Landscape**
- TikZ world map style diagram (simplified rectangles for regions):
  - US (SEC scrutiny, securities classification)
  - EU (MiCA framework applicability)
  - Asia (varying approaches: Japan favorable, China banned)
- Key regulatory questions: Are NFTs securities? IP rights enforcement? AML/KYC requirements?
- `\bottomnote{NFT regulation is evolving rapidly -- the classification of NFTs as securities remains a central debate}`

**Frame 55: Key Takeaways and Course Summary**
- TikZ summary boxes (5 boxes, matching defi_fundamentals.tex Frame 55 style)
- Box 1 (mlblue): NFTs create verifiable digital ownership via ERC-721/ERC-1155 standards
- Box 2 (mlpurple): Marketplace dynamics: floor price, royalties, wash trading are key metrics
- Box 3 (mlgreen): Applications span art, gaming, music, RWA, identity, and credentials
- Box 4 (mlorange): Valuation requires rarity analysis, market metrics, and wash trading detection
- Box 5 (mlred): Future: dynamic NFTs, soulbound tokens, ERC-6551, and evolving regulation
- Teaser bar: "Explore further: fractional ownership, on-chain generative art, and real-world asset tokenization"
- `\bottomnote{End of lecture -- 55 frames covering NFT fundamentals to advanced topics.}`

### Code Frame Summary (Technical Lecture)
| Frame | Title | Code Content |
|-------|-------|-------------|
| 8 | ERC-721 Interface | IERC721 interface definition |
| 19 | Royalty Mechanics | IERC2981 royalty interface |
| 50 | Fractional NFTs | FractionalVault contract |
| (optional 4th) | -- | Reserve slot if needed for ERC-1155 or ERC-6551 |

Total: 3 confirmed [fragile] frames (max 4 allowed).

### Acceptance Criteria (T4)
- Exactly 55 frames (numbered in comments)
- 5 sections with `\section{}` commands
- 3-4 frames maximum with `[fragile]` + lstlisting
- `\bottomnote{}` on all content frames (not title/section dividers -- but section dividers DO have bottomnote per L05 pattern)
- All TikZ nodes with `\\` have `align=center` (either inline or via style)
- No `\foreach` with `/` multi-variable syntax
- No parameterized styles with `#1`
- No style names: diamond, step, text
- Compiles with `pdflatex` double-pass

---

## T5: Quizzes (4 HTML files)

### Common Structure (all 4 quizzes)
Match `quiz/quiz_df_part1.html` exactly:
- DOCTYPE html, lang="en"
- KaTeX v0.16.9 CSS + JS + auto-render
- CSS variables: --mlpurple, --mlblue, --quiz-accent, --correct, --incorrect, etc.
- Nav bar: gradient mlpurple to mlblue, title + Dashboard/GitHub links
- 3-column grid layout (`.questions-row`)
- JSON quizData with 20 questions each
- Each question: id, question, options (A/B/C/D), correct, explanation
- Progress bar, score badge, results card
- Responsive: 2-col at 900px, 1-col at 600px
- Next button for pagination (6 questions at a time + 2 final)

### Quiz NF-1: NFT Fundamentals & Standards (`quiz/quiz_nf_part1.html`)
- Title: "Quiz NF-1: NFT Fundamentals & Standards"
- 20 questions covering Section 1 topics:
  - Q1-4: NFT definition, fungibility, uniqueness properties
  - Q5-8: ERC-721 standard, interface functions, balanceOf, ownerOf
  - Q9-12: ERC-1155 multi-token, batch transfers, gas efficiency
  - Q13-16: Metadata architecture, tokenURI, JSON schema, attributes
  - Q17-20: On-chain vs off-chain storage, IPFS, Arweave, minting process

### Quiz NF-2: NFT Marketplaces & Trading (`quiz/quiz_nf_part2.html`)
- Title: "Quiz NF-2: NFT Marketplaces & Trading"
- 20 questions covering Section 2 topics:
  - Q1-4: Marketplace landscape, OpenSea, Blur, fee structures
  - Q5-8: Pricing mechanisms, fixed price, English auction, Dutch auction
  - Q9-12: Royalty mechanics, EIP-2981, enforcement challenges
  - Q13-16: Floor price, wash trading detection, organic volume
  - Q17-20: NFT lending, AMM models (Sudoswap), gas costs, L2 NFTs

### Quiz NF-3: NFT Applications & Use Cases (`quiz/quiz_nf_part3.html`)
- Title: "Quiz NF-3: NFT Applications & Use Cases"
- 20 questions covering Section 3 topics:
  - Q1-4: Digital art NFTs, Beeple, CryptoPunks, Art Blocks
  - Q5-8: PFP collections, generative art, trait rarity
  - Q9-12: Gaming NFTs, play-to-earn, virtual land, interoperability
  - Q13-16: Music NFTs, RWA tokenization, legal frameworks
  - Q17-20: Identity NFTs, credentials, domain names, ticketing, IP licensing

### Quiz NF-4: NFT Valuation, Advanced Topics & Future (`quiz/quiz_nf_part4.html`)
- Title: "Quiz NF-4: NFT Valuation, Advanced Topics & Future"
- 20 questions covering Sections 4-5 topics:
  - Q1-4: Valuation challenges, illiquidity, subjectivity
  - Q5-8: Rarity scoring methods, trait frequency, information content
  - Q9-12: Market metrics, floor price analysis, index construction
  - Q13-16: Fractional NFTs, dynamic NFTs, ERC-6551
  - Q17-20: Soulbound tokens, regulation, future directions

### Acceptance Criteria (T5)
- Each quiz: exactly 20 questions with 4 options (A-D)
- Each question has explanation field
- KaTeX renders any math formulas
- 3-column grid layout works
- Progress tracking and scoring functional
- Nav links: Dashboard -> `../index.html`, GitHub -> repository
- Question IDs sequential: 1-20 per quiz

---

## T6: Index.html Update

### Changes Required

**1. Sidebar: Add NF links after DF links (inside `<details class="d5" open>` block)**
After `<a href="#sl-df-main">DF Technical Lecture</a>`, add:
```html
<a href="#sl-nf-mini">Mini-Lecture: NFTs</a>
<a href="#sl-nf-intro">NF INTRO Preview</a>
<a href="#sl-nf-pre">NF Pre-Class Handout</a>
<a href="#sl-nf-main">NF Technical Lecture</a>
```

**2. Hero Stats: Bump counts**
- Lectures: 20 -> 24 (adding 4 lecture PDFs)
- Quizzes: 24 -> 28 (adding 4 quizzes)

**3. NF Subsection: Add after DF quiz-grid `</div>` (after line ~513)**
```html
<div class="section-head d6" style="margin-top:16px"><span>NF</span><h2>Standalone Lectures: NFTs &amp; Digital Assets</h2></div>
<div class="lec-grid">
<a href="lectures/nft_intro.pdf" class="lec-card" id="sl-nf-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>NFTs &amp; Digital Assets: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p>
</a>
<a href="lectures/nft_digital_assets_intro.pdf" class="lec-card" id="sl-nf-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>NFTs &amp; Digital Assets: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/nft_digital_assets_preclass.pdf" class="lec-card" id="sl-nf-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>NFTs &amp; Digital Assets: Pre-Class Handout</h3>
<p>4 activities &bull; NFT exploration, metadata, valuation</p></a>
<a href="lectures/nft_digital_assets.pdf" class="lec-card" id="sl-nf-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>NFTs &amp; Digital Assets: Quantitative Deep Dive</h3>
<p>~55 frames &bull; Standards, markets, valuation</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_nf_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz NF-1</div>
<h3>NFT Fundamentals &amp; Standards</h3>
<p>20 questions &bull; ERC-721, ERC-1155, metadata</p></a>
<a href="quiz/quiz_nf_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz NF-2</div>
<h3>NFT Marketplaces &amp; Trading</h3>
<p>20 questions &bull; Floor price, royalties, fees</p></a>
<a href="quiz/quiz_nf_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz NF-3</div>
<h3>NFT Applications &amp; Use Cases</h3>
<p>20 questions &bull; Art, gaming, RWA, identity</p></a>
<a href="quiz/quiz_nf_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz NF-4</div>
<h3>NFT Valuation &amp; Advanced Topics</h3>
<p>20 questions &bull; Rarity, metrics, SBTs, regulation</p></a>
</div>
```

**4. CSS: Add d6 class**
After `.d5 .lcard-num{background:#fff1f2;color:#e11d48}`, add:
```css
.d6 summary{border-left:3px solid #0ea5e9}
.d6 .lcard-num{background:#e0f2fe;color:#0ea5e9}
```

### Acceptance Criteria (T6)
- NF subsection visible after DF subsection
- All 4 lecture cards link to correct PDF paths
- All 4 quiz cards link to correct HTML paths
- Sidebar IDs: sl-nf-mini, sl-nf-intro, sl-nf-pre, sl-nf-main
- Hero stats: 24 Lectures, 28 Quizzes
- d6 class styling applied

---

## Commit Strategy

### Commit 1: LaTeX lecture files
```
Add L06 NFT & Digital Assets standalone lecture bundle (4 LaTeX files)
```
Files: `lectures/nft_intro.tex`, `lectures/nft_digital_assets_intro.tex`, `lectures/nft_digital_assets_preclass.tex`, `lectures/nft_digital_assets.tex`

### Commit 2: Quiz HTML files
```
Add NFT quiz suite (4 HTML quizzes, 80 questions total)
```
Files: `quiz/quiz_nf_part1.html`, `quiz/quiz_nf_part2.html`, `quiz/quiz_nf_part3.html`, `quiz/quiz_nf_part4.html`

### Commit 3: Index update
```
Update GitHub Pages index with NF subsection and bump hero stats
```
Files: `index.html`

---

## Risk Mitigations

### TikZ Compilation Issues (HIGH risk)
- **Mitigation 1:** Every TikZ node containing `\\` MUST have `align=center` in its style
- **Mitigation 2:** No `\foreach` with multi-variable `/` syntax (e.g., `\foreach \x/\y` is FORBIDDEN; use separate loops)
- **Mitigation 3:** No parameterized styles (`#1` in style definitions) -- these conflict with beamer's frame argument parsing
- **Mitigation 4:** Avoid style names that conflict with pgf/TikZ built-ins: `diamond`, `step`, `text`, `circle` (as custom style)
- **Mitigation 5:** Test compilation after every 10 frames during implementation

### lstlisting / Fragile Frame Issues (MEDIUM risk)
- **Mitigation:** Every frame with `\begin{lstlisting}` MUST have `[fragile]` in `\begin{frame}[fragile]{...}`
- **Mitigation:** Maximum 4 such frames in the entire technical lecture
- **Mitigation:** No lstlisting in mini-lecture (zero code policy)

### Metadata/Encoding Issues (LOW risk)
- **Mitigation:** Use `&` as `\&` in LaTeX titles
- **Mitigation:** Use `&amp;` in HTML
- **Mitigation:** UTF-8 encoding for all files

### Quiz JSON Issues (LOW risk)
- **Mitigation:** Validate JSON structure: each question has id, question, options (A-D), correct, explanation
- **Mitigation:** Escape special characters in question/explanation strings
- **Mitigation:** Test KaTeX rendering for any math formulas

---

## Build/Compile Verification Steps

After implementation, verify:

1. **LaTeX compilation (all 4 files):**
```bash
cd lectures/
pdflatex nft_intro.tex && pdflatex nft_intro.tex
pdflatex nft_digital_assets_intro.tex && pdflatex nft_digital_assets_intro.tex
pdflatex nft_digital_assets_preclass.tex && pdflatex nft_digital_assets_preclass.tex
pdflatex nft_digital_assets.tex && pdflatex nft_digital_assets.tex
```
Each should produce 0 errors on double-pass.

2. **Frame count verification:**
```bash
grep -c "\\\\begin{frame}" nft_intro.tex          # Should be 10
grep -c "\\\\begin{frame}" nft_digital_assets_intro.tex  # Should be 6
grep -c "\\\\begin{frame}" nft_digital_assets.tex        # Should be 55
```

3. **Fragile frame audit:**
```bash
grep -c "\\[fragile\\]" nft_digital_assets.tex    # Should be 3-4
grep -c "lstlisting" nft_digital_assets.tex        # Should be 3-4 begin + 3-4 end
```

4. **TikZ safety audit:**
```bash
grep -n "\\\\\\\\" nft_*.tex | grep -v "align"     # Should find ZERO lines without align
grep "\\\\foreach.*/" nft_*.tex                     # Should find ZERO matches
```

5. **Quiz HTML validation:**
- Open each quiz_nf_part{1-4}.html in browser
- Verify 20 questions load
- Answer one question -- verify scoring works
- Check KaTeX renders math

6. **Index.html validation:**
- Open index.html in browser
- Verify NF subsection appears after DF
- All 8 links (4 lecture + 4 quiz) clickable
- Hero stats show 24 Lectures, 28 Quizzes
- Sidebar NF links scroll to correct sections

---

## Success Criteria

- [ ] 4 LaTeX files compile without errors (0 errors, 0 undefined references)
- [ ] Frame counts: mini=10, intro=6, technical=55
- [ ] Code frames in technical lecture: 3-4 maximum
- [ ] All TikZ diagrams render correctly (no missing text, no overflow)
- [ ] 4 quiz HTML files functional (80 total questions, all with explanations)
- [ ] index.html updated: NF subsection, sidebar links, hero stats
- [ ] Color palette consistent across all files (mlblue, mlpurple, mllavender*, mlorange, mlgreen, mlred, mlgray)
- [ ] Preamble patterns match L05 DeFi templates exactly
- [ ] No TikZ safety violations (align, foreach, parameterized styles)

---

## File Manifest

| # | File Path | Type | Size Est. |
|---|-----------|------|-----------|
| 1 | `lectures/nft_intro.tex` | LaTeX beamer | ~700 lines |
| 2 | `lectures/nft_digital_assets_intro.tex` | LaTeX beamer | ~300 lines |
| 3 | `lectures/nft_digital_assets_preclass.tex` | LaTeX article | ~180 lines |
| 4 | `lectures/nft_digital_assets.tex` | LaTeX beamer | ~2800 lines |
| 5 | `quiz/quiz_nf_part1.html` | HTML/JS | ~600 lines |
| 6 | `quiz/quiz_nf_part2.html` | HTML/JS | ~600 lines |
| 7 | `quiz/quiz_nf_part3.html` | HTML/JS | ~600 lines |
| 8 | `quiz/quiz_nf_part4.html` | HTML/JS | ~600 lines |
| 9 | `index.html` | HTML (edit) | ~30 lines added |

All file paths are relative to: `D:\Joerg\Research\slides\cryptocurrency\`
