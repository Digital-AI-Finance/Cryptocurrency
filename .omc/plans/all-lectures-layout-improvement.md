# Plan: All Lectures Layout Improvement

**Revision:** 2
**Status:** READY
**Created:** 2026-03-05
**Scope:** 12 lectures (L02 cryptography_security SKIPPED — no issues; L05 defi_fundamentals SKIPPED — already fixed)

---

## 1. Context

### Original Request
Apply the same layout improvements (adjustbox wraps, spacing reductions, section divider consistency) to all other lectures, following the DeFi pattern established in `.omc/plans/defi-layout-improvement.md`.

### Key Document Parameters (shared by ALL lectures)
- `\documentclass[8pt,aspectratio=169]{beamer}` (Madrid theme)
- `\setbeamersize{text margin left=5mm,text margin right=5mm}`
- Usable text width: ~15.2cm (160mm - 2x5mm)
- Usable frame height: ~7.2cm (varies by frame title and footline)
- `adjustbox` package already loaded in all files

### Constraints (HARD)
- ZERO content changes (no text, formulas, data, colors)
- Preserve all frames, frame titles, section structure
- Preserve all `\bottomnote{}` text
- Preserve all TikZ node text, colors, connections
- Only modify: dimensions, positions, scales, spacing, adjustbox wrappers, font sizes on overflowing elements
- Section divider reformatting (Fix F) changes PRESENTATION STRUCTURE only — not lecture content

---

## 2. Objectives

### Core Objective
Eliminate all content overflow and visual inconsistencies so every frame in every lecture renders fully within Beamer's visible area on 16:9 slides.

### Deliverables
1. All CRITICAL overflow issues fixed (14 issues)
2. All MODERATE overflow issues fixed (35 issues)
3. Consistent section divider format across all lectures

### Definition of Done
- All 12 lectures compile without errors
- No frames with visibly clipped or overflowing content
- Section dividers use standard `beamercolorbox{palette quaternary}` + `\Large\bfseries` pattern

---

## 3. Guardrails

### MUST Have
- Every TikZ picture risking horizontal overflow: wrapped in `\adjustbox{max width=\textwidth}` OR scaled/repositioned
- Every TikZ picture risking vertical overflow: wrapped in `\adjustbox{max totalheight=Xcm}` OR spacing reduced
- Non-standard section dividers reformatted to match standard pattern

### MUST NOT Have
- Any change to node text content, formula content, or data values
- Any change to color definitions or color assignments
- Any added or removed frames
- Any change to `\bottomnote{}` text
- Any new packages added

---

## 4. Task List

Tasks are organized by lecture, prioritized by severity (CRITICAL first), then by lecture complexity (most issues first).

---

### LECTURE: stablecoins_cbdcs.tex (L06) — 4 CRITICAL + 4 MODERATE

#### Task 1: Frame 40 "What is a CBDC?" (lines 1667-1727) — CRITICAL

**Problem:** 5-column TikZ table. Column at x=11.5, minimum width=2.3cm → right edge 12.65cm. Overflows by ~1.45cm when centered. NOTE: This tikzpicture is inside `\column{0.56\textwidth}` (line 1684).

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\linewidth}`. Use `\linewidth` (NOT `\textwidth`) because this is inside a column environment.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` (line 1685) INSERT `\adjustbox{max width=\linewidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full 5-column table visible within its column, no right-edge clipping.

---

#### Task 2: Frame 45 "Global CBDC Landscape" (lines 1875-1907) — CRITICAL

**Problem:** 4-column table. "Cancelled" column at x=12.0, minimum width=3.2cm → right edge 13.6cm. Overflows by ~2.4cm — worst overflow in this file.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All 4 columns visible including "Cancelled" column.

---

#### Task 3: Frame 50 "Global Regulatory Landscape" (lines 2079-2123) — CRITICAL

**Problem:** 4-column table. Column at x=10.9, minimum width=3.0cm → right edge 12.4cm. Overflows by ~1.2cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full regulatory table visible.

---

#### Task 4: Frame 53 "Cross-Border Payments Revolution" (lines 2202-2235) — CRITICAL

**Problem:** Headline stat box minimum width=12.5cm centered at x=6.5 → right edge 12.75cm. Overflows by ~1.55cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Headline box fully visible without clipping.

---

#### Task 5: Frame "Liquidation Process" (lines 921-961) — MODERATE

**Problem:** Warning box left edge at 0.1cm (extremely tight against left margin).

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Warning box fully visible on both edges.

---

#### Task 6: Frame "Stablecoin Taxonomy" (lines 255-292) — MODERATE

**Problem:** No adjustbox safety net; rightmost node at 11.8cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Taxonomy tree fully visible.

---

#### Task 7: Frame "Peg Mechanism Overview" (lines 294-335) — MODERATE

**Problem:** Panel 3 right edge at 11.85cm; no adjustbox safety net.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All 3 panels fully visible.

---

#### Task 8: Frame "Terra/LUNA Collapse Timeline" (lines 1311-1356) — MODERATE

**Problem:** Vertical content tight with bottomnote; timeline at y 0.4 to 5.6 = 5.2cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}` as precautionary measure.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Timeline and bottomnote both visible.

---

### LECTURE: rwa_tokenization.tex (L11) — 3 CRITICAL + 2 MODERATE

#### Task 9: Frame 12 "The Oracle Problem for RWA" (lines 440-483) — CRITICAL

**Problem:** Three zone nodes span 16.4cm total (from x=-2.0 to x=14.4). Overflows by 1.2cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All three zone boxes visible within frame.

---

#### Task 10: Frame 27 "Security vs Utility Tokens" (lines 1165-1223) — CRITICAL

**Problem:** Vertical span ~9.5cm (root at y=3.5 to callout at y=-5.0). Overflows by 2.3cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full token classification tree visible within frame.

---

#### Task 11: Frame 28 "SEC Enforcement & Precedents" (lines 1225-1317) — CRITICAL

**Problem:** Timeline vertical span 8.3cm (cases at y=+2.2 and y=-2.2, insight box at y=-4.2). Overflows by 1.1cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All timeline cases and insight box visible.

---

#### Task 12: Frame 5 "What is Tokenization?" (lines 177-206) — MODERATE

**Problem:** TikZ spans 14.85cm with only 0.075cm margin each side.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full tokenization process visible.

---

#### Task 13: Frame 30 "On-Chain KYC/AML Architecture" (lines 1365-1405) — MODERATE

**Problem:** Vertical 7.4cm (0.2cm over) + ERC-3643 annotation right edge at 15.25cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All layers and annotation visible.

---

### LECTURE: ethereum_smart_contracts.tex (L03) — 2 CRITICAL + 1 MODERATE

#### Task 14: Frame 2 "Lecture Roadmap" (lines 63-112) — CRITICAL

**Problem:** 5 roadmap nodes spaced 3.6cm apart. Node s5 at x=14.4 with min-width=2.6cm → right edge 15.7cm. Overflows by 0.5cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All 5 roadmap boxes visible including rightmost.

---

#### Task 15: Frame 38 "Deployment Transaction" (lines 2175-2226) — CRITICAL

**Problem:** TikZ spans from x=-2.5 to x=15.2 = 17.7cm total. Overflows by 2.5cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full deployment flow visible (tx box, contract box, address box).

---

#### Task 16: Frame 7 "Transaction Types" (lines 334-373) — MODERATE

**Problem:** 4-column tabular with monospaced text, estimated 16-17cm wide, no adjustbox.

**Fix:** Wrap tabular in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE the `\begin{tabular}` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tabular}` INSERT `}%`

**Acceptance:** Full transaction types table visible.

---

### LECTURE: smart_contracts.tex (L14) — 1 CRITICAL + 3 MODERATE

#### Task 17: Frame "Supply Chain Management" (lines 1205-1271) — CRITICAL

**Problem:** TikZ in 0.55\textwidth column. Node at x=10.0 with min-width=1.8cm at scale=0.82 → right edge 8.94cm > column width 8.36cm.

**Fix:** Change `scale=0.82` to `scale=0.72`.

**Exact changes:**
- Line 1222: Change `scale=0.82` to `scale=0.72` in the tikzpicture options

**Acceptance:** Consumer node fully visible within column boundary.

---

#### Task 18: Frame "History: From Szabo to Ethereum" (lines 239-325) — MODERATE

**Problem:** Timeline at scale=0.95 reaches 13.68cm. Only 1.4cm margin.

**Fix:** Change `scale=0.95` to `scale=0.88`.

**Exact changes:**
- Find `scale=0.95` in the tikzpicture options and change to `scale=0.88`

**Acceptance:** Timeline comfortable within frame with 2.5cm margin.

---

#### Task 19: Frame "How Smart Contracts Execute" (lines 406-456) — MODERATE

**Problem:** Annotation text extends ~10.2cm right + REVERT box at x=-4.0 left. Total ~14.8cm, only 0.4cm margin.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full execution flow visible with comfortable margins.

---

#### Task 20: Sections 2 & 5 divider fixes (lines 630, 1090, 1973, 2572) — MODERATE

**Problem:** Section 2 and 5 have no divider frames. Existing dividers at lines 1090 and 1973 are numbered wrong (labeled Section 2 and 3, should be Section 3 and 4).

**Fix (F):** Add missing divider frames matching the EXISTING full-format pattern in this file (beamercolorbox + vspace + two-column "What You Will Learn" / "Frames in This Section" blocks + bottomnote), and renumber existing ones.

**Exact changes:**

**(a) After line 630** (`\section{Platforms and Regulatory Landscape}`): INSERT a full divider frame matching the pattern at lines 1090-1133:
```latex
% Section 2 Divider
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
  {\Large\bfseries Section 2: Platforms and Regulatory Landscape}\\[6pt]
  {\normalsize Comparing platforms, legal status, regulatory landscape, and current limitations}
\end{beamercolorbox}
\vspace{4mm}
\begin{columns}[T]
\column{0.5\textwidth}
\begin{block}{What You Will Learn}
\footnotesize
\begin{itemize}
  \item Smart contract platform landscape beyond Ethereum
  \item Ethereum vs Solana vs alternative platforms
  \item Legal enforceability and regulatory frameworks
  \item Current limitations and the oracle problem
  \item Security challenges and attack vectors
\end{itemize}
\end{block}
\column{0.5\textwidth}
\begin{block}{Frames in This Section}
\footnotesize
\begin{itemize}
  \item Smart Contract Platforms Overview
  \item Ethereum: The Pioneer Platform
  \item Beyond Ethereum: Alternative Platforms
  \item Legal Status of Smart Contracts
  \item Regulatory Landscape
  \item Current Limitations
  \item The Oracle Problem
  \item Security Challenges Overview
\end{itemize}
\end{block}
\end{columns}
\bottomnote{Section 2 of 5}
\end{frame}
```

**(b) Line 1092:** Change `Section 2: Smart Contracts in Business \& Finance` to `Section 3: Smart Contracts in Business \& Finance`

**(c) Line 1132:** Change `Section 2 of 3` to `Section 3 of 5` in the bottomnote

**(d) Line 1975:** Change `Section 3: How Smart Contracts Work Under the Hood` to `Section 4: How Smart Contracts Work Under the Hood`

**(e) After line 2572** (`\section{Applications, Security, and Future}`): INSERT a full divider frame:
```latex
% Section 5 Divider
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
  {\Large\bfseries Section 5: Applications, Security, and Future}\\[6pt]
  {\normalsize DeFi primitives, security best practices, upgradeability, and course summary}
\end{beamercolorbox}
\vspace{4mm}
\begin{columns}[T]
\column{0.5\textwidth}
\begin{block}{What You Will Learn}
\footnotesize
\begin{itemize}
  \item Decentralized exchanges and AMM mechanics
  \item Lending protocols and stablecoins as contracts
  \item Smart contract security best practices
  \item Famous failures and lessons learned
  \item Upgradeability patterns (proxy, diamond)
\end{itemize}
\end{block}
\column{0.5\textwidth}
\begin{block}{Frames in This Section}
\footnotesize
\begin{itemize}
  \item Decentralized Exchanges
  \item Lending Protocols
  \item Stablecoins as Smart Contracts
  \item Security Best Practices
  \item Famous Smart Contract Failures
  \item Upgradeability Patterns
  \item Key Takeaways
  \item Discussion Questions
\end{itemize}
\end{block}
\end{columns}
\bottomnote{Section 5 of 5}
\end{frame}
```

**Note:** Adding 2 new divider frames increases total frame count by 2. The `% Frame N:` comments throughout the file should be renumbered by the executor to reflect the new ordering.

**Acceptance:** All 5 sections have correctly numbered, full-format divider frames matching the existing pattern in the file.

---

### LECTURE: erc20_token_creation.tex (L04) — 1 CRITICAL + 3 MODERATE

#### Task 21: Frame 13 "Token Ecosystem Market Map" (lines 526-580) — CRITICAL

**Problem:** Pie chart y-span 8.8cm (from y=-4.8 footnote to y=+4.0 FLOKI label). Overflows by 1.6cm.

**Fix:** Add `scale=0.78` to tikzpicture.

**Exact changes:**
- In the `\begin{tikzpicture}[` options, add or change scale to `scale=0.78`

**Acceptance:** Full pie chart with all labels visible within frame.

---

#### Task 22: Frame 14 "Section 1 Summary" (lines 583-615) — MODERATE

**Problem:** 2x2 stat card grid. Combined height ~7.5cm, over by 0.3cm.

**Fix:** Reduce vertical gap between card rows from -3.3 to -3.0. Note: if inner content nodes use ABSOLUTE y-coordinates (not relative to the card container), shift ALL inner nodes within c3/c4 by +0.3 as well. If inner nodes use named references (e.g., `c3.center`), they auto-adjust.

**Exact changes:**
- Change y-coordinate of c3/c4 container nodes from `-3.3` to `-3.0`
- Check and shift any inner nodes with absolute y-coordinates that were relative to the old -3.3 position (shift each by +0.3)

**Acceptance:** All 4 stat cards and bottomnote visible, inner text centered within cards.

---

#### Task 23: Frame 47 "Distribution Visualization" (lines 1958-2024) — MODERATE

**Problem:** Legend row at y=-3.0 leaves only 0.2cm margin.

**Fix:** Move legend entries from y=-3.0 to y=-2.7.

**Exact changes:**
- Change legend y-coordinates from `-3.0` to `-2.7` (and corresponding rectangle coordinates)

**Acceptance:** Pie chart and legend both visible.

---

#### Task 24: Section dividers standardization (5 dividers) — MODERATE

**Problem:** All 5 dividers use `\LARGE` instead of `\Large\bfseries`. Sections 2, 4, 5 use completely different formats (palette primary, full-bleed plain frame).

**Fix (F):** Standardize all 5 dividers to the canonical format.

**Exact changes for each divider:**

**Section 1 (lines 133-141):** Change `\LARGE\textbf{...}` to `\Large\bfseries ...`

**Section 2 (lines 624-633):** Replace entire frame with:
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 2: ERC-20 Functions Deep Dive}\\[6pt]
{\normalsize Core transfer, approval, and allowance functions}
\end{beamercolorbox}
\end{frame}
```

**Section 3 (lines 1208-1216):** Change `\LARGE\bfseries` to `\Large\bfseries`; add `shadow=true` if absent

**Section 4 (lines 1737-1744):** Replace full-bleed `[plain]` frame with standard format:
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 4: Token Economics}\\[6pt]
{\normalsize Designing sustainable token models}
\end{beamercolorbox}
\end{frame}
```

**Section 5 (lines 2206-2213):** Replace full-bleed `[plain]` frame with standard format:
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 5: Advanced Topics \& Summary}\\[6pt]
{\normalsize Next steps and key takeaways}
\end{beamercolorbox}
\end{frame}
```

**Acceptance:** All 5 section dividers visually consistent.

---

### LECTURE: crypto_trading_markets.tex (L08) — 1 CRITICAL + 4 MODERATE

#### Task 25: Frame 7 "Order Types in Crypto Markets" (lines 307-383) — CRITICAL

**Problem:** 4th panel rectangle extends to x=15.3cm. Bottom comparison bar also to x=15.3. Overflows by 0.3cm.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All 4 order type panels fully visible.

---

#### Task 26: Frame 6 "Order Book Anatomy" (lines 206-304) — MODERATE

**Problem:** Title node at y=6.3, tight vertical with bottomnote.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full order book diagram visible.

---

#### Task 27: Frame 13 "Exchange Fee Structures" (lines 656-737) — MODERATE

**Problem:** Title node at y=6.3, tight vertical with bottomnote.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full fee structure table visible.

---

#### Task 28: Frame 36 "Portfolio Construction" (lines 1988-2053) — MODERATE

**Problem:** Title at y=6.3, content to y=5.8 — tight vertical.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full portfolio diagram visible.

---

#### Task 29: Frame 37 "Risk Monitoring Dashboard" (lines 2056-2153) — MODERATE

**Problem:** Title at y=6.3, top panels to y=5.9 — tight vertical.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Full dashboard with all 6 panels visible.

---

### LECTURE: nft_digital_assets.tex (L07) — 1 CRITICAL + 5 MODERATE

#### Task 30: Frame 36 "NFT Ticketing" (lines 1548-1584) — CRITICAL

**Problem:** Node at x=12.0 with minimum width=3.2cm → right edge 13.6cm. Tight clipping.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All ticketing nodes visible.

---

#### Task 31: Frame 2 "Lecture Roadmap" (lines 65-101) — MODERATE

**Problem:** 5-box chain spans ~11.9cm at frame level. Precautionary wrap to ensure safety margin.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

Note: This tikzpicture is at frame level (not inside a column), so `\textwidth` is correct.

**Acceptance:** All 5 roadmap boxes visible with safety margin.

---

#### Task 32: Frame 16 "NFT Marketplace Landscape" (lines 626-664) — MODERATE

**Problem:** Top node at y=5.6 with 0.8cm height → top at 6.0cm, at usable boundary.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All marketplace nodes visible.

---

#### Task 33: Frame 21 "Floor Price Mechanics" (lines 875-912) — MODERATE

**Problem:** "Floor Price" annotation at y=6.1, above axis top at 6.0cm.

**Fix:** Wrap pgfplots in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Floor price annotation visible.

---

#### Task 34: Frame 25 "Gas Costs and Layer-2 NFTs" (lines 1034-1078) — MODERATE

**Problem:** pgfplots height=5.5cm + nodes near coords push to ~6.3cm total.

**Fix:** Reduce axis height from 5.5cm to 4.8cm.

**Exact changes:**
- Change `height=5.5cm` to `height=4.8cm` in the axis options

**Acceptance:** Bar chart with all value labels visible.

---

#### Task 35: Frame 53 "NFT Composability" (lines 2258-2295) — MODERATE

**Problem:** Nodes at x=11.6 with min-width=2.4cm → right edge 12.8cm. Visually crowded.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All composability nodes visible.

---

### LECTURE: dao_governance.tex (L09) — 4 MODERATE

#### Task 36: Frame 16 "Proposal Lifecycle" (lines 819-897) — MODERATE

**Problem:** Stacked content (TikZ + vspace + 3 column blocks) totals ~7.24cm, at the limit.

**Fix:** Remove `\vspace{2mm}` between tikzpicture and columns.

**Exact changes:**
- Remove or change `\vspace{2mm}` to `\vspace{0mm}` between the `\end{tikzpicture}` and `\begin{columns}`

**Acceptance:** All 3 blocks and TikZ diagram visible.

---

#### Task 37: Frame 27 Section 3 divider (lines 1623-1662) — MODERATE

**Problem:** Non-standard TikZ-based divider with `\large\bfseries` (should be `\Large\bfseries`), custom fill color, no beamercolorbox.

**Fix (F):** Replace TikZ nodes with standard beamercolorbox pattern.

**Exact changes:** Replace the TikZ heading section with:
```latex
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 3: Treasury Management \& Economics}\\[6pt]
{\normalsize How DAOs manage billions in assets and design sustainable token economies}
\end{beamercolorbox}
```

**Acceptance:** Section 3 divider matches Sections 1-2 format.

---

#### Task 38: Frame 39 Section 4 divider (lines 2324-2355) — MODERATE

**Problem:** Non-standard TikZ nodes with mlred fill, no beamercolorbox.

**Fix (F):** Replace TikZ nodes with standard beamercolorbox.

**Exact changes:** Replace the TikZ heading section with:
```latex
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 4: Governance Attacks \& Security}\\[6pt]
{\normalsize Understanding and defending against threats to decentralized governance}
\end{beamercolorbox}
```

**Acceptance:** Section 4 divider matches Sections 1-2 format.

---

#### Task 39: Frame 49 Section 5 divider (lines 2782-2813) — MODERATE

**Problem:** Non-standard TikZ nodes with mlblue fill, no beamercolorbox.

**Fix (F):** Replace TikZ nodes with standard beamercolorbox.

**Exact changes:** Replace the TikZ heading section with:
```latex
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 5: Real-World DAOs \& Future of Governance}\\[6pt]
{\normalsize Case studies, participation challenges, and the road ahead}
\end{beamercolorbox}
```

**Acceptance:** Section 5 divider matches Sections 1-2 format.

---

### LECTURE: privacy_zk_proofs.tex (L13) — 1 CRITICAL + 3 MODERATE

#### Task 40: Frame "Proof Systems Comparison" (lines 1038-1053) — CRITICAL

**Problem:** 6-column tabular spec but only 5 header entries. Table ~16cm wide, no adjustbox.

**Fix:** Fix column spec mismatch AND wrap in adjustbox.

**Exact changes:**
- Change `{lccccc}` to `{lcccc}` (remove one `c` to match the 5 actual columns: 1 label + 4 data)
- BEFORE `\begin{tabular}` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tabular}` INSERT `}%`

**Acceptance:** Table renders correctly with all columns visible.

---

#### Task 41: Frame "Taxonomy of ZK Proof Systems" table (lines 709-718) — MODERATE

**Problem:** 5-column inline tabular with no adjustbox. ~14-16cm wide at \footnotesize.

**Fix:** Wrap tabular in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tabular}` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tabular}` INSERT `}%`

**Acceptance:** ZK proof comparison table fully visible.

---

#### Task 42: Frame "Monero: Privacy by Default" (lines 1410-1454) — MODERATE

**Problem:** Side annotation nodes may extend beyond right edge of centered picture.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All layer annotations visible.

---

#### Task 43: Missing section dividers (all 5 sections) — MODERATE

**Problem:** File has 5 `\section{}` commands but zero visual divider frames.

**Fix (F):** Add standard divider frame after each `\section{}` command.

**Exact changes:** After each `\section{}` command, insert a divider frame:

**After line 137** (`\section{ZK Proof Foundations & Mathematical Basics}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 1: ZK Proof Foundations \& Mathematical Basics}\\[6pt]
{\normalsize Zero-knowledge concepts, interactive proofs, and mathematical foundations}
\end{beamercolorbox}
\end{frame}
```

**After line 679** (`\section{Proof Systems -- SNARKs, STARKs, Bulletproofs}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 2: Proof Systems --- SNARKs, STARKs, Bulletproofs}\\[6pt]
{\normalsize Comparing proof systems: setup, verification, proof size, and trade-offs}
\end{beamercolorbox}
\end{frame}
```

**After line 1206** (`\section{Privacy Coins}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 3: Privacy Coins}\\[6pt]
{\normalsize Monero, Zcash, and privacy-preserving transaction mechanisms}
\end{beamercolorbox}
\end{frame}
```

**After line 1761** (`\section{ZK Applications}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 4: ZK Applications}\\[6pt]
{\normalsize ZK-rollups, identity systems, voting, and real-world deployments}
\end{beamercolorbox}
\end{frame}
```

**After line 2357** (`\section{Advanced Topics & Future}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 5: Advanced Topics \& Future}\\[6pt]
{\normalsize Recursive proofs, cross-chain privacy, regulation, and emerging trends}
\end{beamercolorbox}
\end{frame}
```

**Note:** Adding 5 new divider frames increases total frame count by 5.

**Acceptance:** All 5 sections have visual divider frames with correct titles.

---

### LECTURE: tokenomics_mechanism.tex (L12) — 4 MODERATE

#### Task 44: Missing section dividers (all 5 sections) — MODERATE

**Problem:** File has 5 `\section{}` commands but zero visual divider frames.

**Fix (F):** Add standard divider frame after each `\section{}` command.

**Exact changes:** After each `\section{}` command, insert a divider frame:

**After line 137** (`\section{Token Fundamentals & Supply Economics}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 1: Token Fundamentals \& Supply Economics}\\[6pt]
{\normalsize Token types, supply mechanics, and valuation fundamentals}
\end{beamercolorbox}
\end{frame}
```

**After line 603** (`\section{Bonding Curves & Pricing Mechanisms}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 2: Bonding Curves \& Pricing Mechanisms}\\[6pt]
{\normalsize Automated pricing, bonding curve mathematics, and AMM design}
\end{beamercolorbox}
\end{frame}
```

**After line 1067** (`\section{Incentive Design & Game Theory}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 3: Incentive Design \& Game Theory}\\[6pt]
{\normalsize Mechanism design, staking incentives, and Nash equilibria in token systems}
\end{beamercolorbox}
\end{frame}
```

**After line 1520** (`\section{Token Design Framework}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 4: Token Design Framework}\\[6pt]
{\normalsize Systematic methodology for designing sustainable token economies}
\end{beamercolorbox}
\end{frame}
```

**After line 2037** (`\section{Case Studies & Pitfalls}`):
```latex
\begin{frame}{}
\begin{beamercolorbox}[sep=12pt,center,rounded=true,shadow=true]{palette quaternary}
{\Large\bfseries Section 5: Case Studies \& Pitfalls}\\[6pt]
{\normalsize Real-world tokenomics successes, failures, and lessons learned}
\end{beamercolorbox}
\end{frame}
```

**Note:** Adding 5 new divider frames increases total frame count by 5.

**Acceptance:** All 5 sections have visual divider frames with correct titles.

---

#### Task 45: Frame "Token Taxonomy" (lines 181-207) — MODERATE

**Problem:** TikZ at scale=0.85, picture off-center (runs from x≈0 to x≈11.1).

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Taxonomy tree centered and fully visible.

---

#### Task 46: Frame "Token Design Methodology" (lines 1523-1563) — MODERATE

**Problem:** 7-step chain at scale=0.8; node s7 right edge at 11.28cm, tight.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** All 7 methodology steps visible.

---

#### Task 47: Frame "Token Utility Matrix" (lines 1850-1894) — MODERATE

**Problem:** Rotated Y-axis label at x=-5.8 may be clipped if picture not centered correctly.

**Fix:** Wrap tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tikzpicture}` INSERT `}%`

**Acceptance:** Axis labels and matrix content fully visible.

---

### LECTURE: layer2_scaling.tex (L10) — 1 MODERATE

#### Task 48: Section 2/3/4 divider vspace inconsistency (lines 901, 1622, 2334) — MODERATE

**Problem:** Sections 2, 3, 4 dividers have `\vspace{10mm}` before the beamercolorbox; Section 1 does not.

**Fix (C):** Remove `\vspace{10mm}` from all three dividers to match Section 1.

**Exact changes:**
- Line ~903: Remove `\vspace{10mm}`
- Line ~1624: Remove `\vspace{10mm}`
- Line ~2336: Remove `\vspace{10mm}`

**Acceptance:** All 4 section dividers have consistent vertical spacing.

---

### LECTURE: blockchain_fundamentals.tex (L01) — 1 MODERATE

#### Task 49: Frame 52 "Smart Contract Platforms Comparison" (lines 2151-2192) — MODERATE

**Problem:** 5-column tabular with l-spec columns at \small font. Estimated 17-18cm wide, no adjustbox.

**Fix:** Wrap tabular in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- BEFORE `\begin{tabular}` INSERT `\adjustbox{max width=\textwidth}{%`
- AFTER `\end{tabular}` INSERT `}%`

**Acceptance:** Full 5-column comparison table visible.

---

## 5. Task Dependencies and Execution Order

All tasks within a lecture are independent (non-overlapping line ranges). Tasks across lectures are also fully independent. **All 49 tasks can be executed in parallel.**

### Recommended execution grouping (by lecture, parallel batches):

**Batch 1 (highest priority — most CRITICAL issues):**
- L06 stablecoins_cbdcs: Tasks 1-8 (4 CRITICAL + 4 MODERATE)
- L11 rwa_tokenization: Tasks 9-13 (3 CRITICAL + 2 MODERATE)

**Batch 2 (CRITICAL issues):**
- L03 ethereum_smart_contracts: Tasks 14-16 (2 CRITICAL + 1 MODERATE)
- L14 smart_contracts: Tasks 17-20 (1 CRITICAL + 3 MODERATE)

**Batch 3 (CRITICAL + MODERATE):**
- L04 erc20_token_creation: Tasks 21-24 (1 CRITICAL + 3 MODERATE)
- L08 crypto_trading_markets: Tasks 25-29 (1 CRITICAL + 4 MODERATE)

**Batch 4 (MODERATE only):**
- L07 nft_digital_assets: Tasks 30-35 (1 CRITICAL + 5 MODERATE)
- L09 dao_governance: Tasks 36-39 (4 MODERATE)

**Batch 5 (MODERATE only):**
- L13 privacy_zk_proofs: Tasks 40-43 (1 CRITICAL + 3 MODERATE)
- L12 tokenomics_mechanism: Tasks 44-47 (4 MODERATE)
- L10 layer2_scaling: Task 48 (1 MODERATE)
- L01 blockchain_fundamentals: Task 49 (1 MODERATE)

---

## 6. Commit Strategy

**Single commit** per batch (or single commit for all if done together):
```
Fix layout overflow in 12 lecture files (49 fixes)

- Wrap overwide TikZ/tables in adjustbox{max width} (30+ frames)
- Reduce vertical spacing and scale in dense frames
- Standardize section dividers to beamercolorbox pattern
- Add missing section dividers in tokenomics and privacy lectures
- Fix section numbering in smart_contracts.tex
- No content changes: layout/spacing only
```

---

## 7. Success Criteria

| Criterion | Verification |
|-----------|-------------|
| All 12 lectures compile | `pdflatex <file>.tex` exits 0 for all 12 |
| No added overfull hbox warnings on modified frames | Check .log files |
| Frame counts preserved | Count `\begin{frame` occurrences: unchanged for most files; +2 for L14 (missing Sec 2+5 dividers), +5 for L12 tokenomics (all 5 dividers), +5 for L13 privacy (all 5 dividers) |
| All bottomnotes preserved | Count `\bottomnote{` unchanged |
| Section dividers consistent | Visual inspection confirms beamercolorbox pattern |
| No content changes | `git diff` shows only dimension/position/spacing/structure changes |

---

## 8. Risk Notes

- **adjustbox scaling:** Frames wrapped in adjustbox will scale proportionally. Since overflows are generally 0.3-2.5cm on 15.2cm width, maximum scaling is ~85%, keeping text readable at 8pt base.
- **Section divider additions (L12, L13):** Adding 10 new section divider frames (5 per file) increases total frame count. These are structural additions matching the course standard, not content changes.
- **Section renumbering (L14):** Renumbering dividers from "Section 2" to "Section 3" etc. changes visible text on divider slides. This is a structural correction (fixing mislabeling), not a content change.
- **Column-context adjustbox:** Task 1 uses `\linewidth` instead of `\textwidth` because its tikzpicture is inside a `\column{0.56\textwidth}` environment. All other adjustbox tasks use `\textwidth` at frame level.
- **tabular vs tikzpicture adjustbox:** Wrapping a tabular in adjustbox uses the same syntax but the tabular must be inside the adjustbox braces, not vice versa.
