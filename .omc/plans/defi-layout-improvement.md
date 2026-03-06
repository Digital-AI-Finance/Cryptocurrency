# Plan: DeFi Fundamentals Layout Improvement

**Revision:** 3
**Status:** READY
**Created:** 2026-03-04
**File:** `lectures/defi_fundamentals.tex` (2810 lines, 56 frames)

---

## 1. Context

### Original Request
Fix layout-only issues in `lectures/defi_fundamentals.tex` -- a Beamer LaTeX lecture (Madrid theme, 8pt, 16:9 aspect ratio, 5mm margins). No content, text, formula, or data changes. Only modify dimensions, positions, scales, spacing, adjustbox wrappers, and font sizes on overflowing elements.

### Key Document Parameters
- `\documentclass[8pt,aspectratio=169]{beamer}` (line 1)
- `\setbeamersize{text margin left=5mm,text margin right=5mm}` (line 30)
- Usable text width: ~15.2cm (160mm - 2x5mm)
- Usable frame height: ~7.2cm (varies by frame title and footline)
- `adjustbox` package already loaded (line 3)

### Constraints (HARD)
- ZERO content changes (no text, formulas, data, colors)
- Preserve all 56 frames, frame titles, section structure
- Preserve all `\bottomnote{}` text
- Preserve all TikZ node text, colors, connections
- Follow existing TikZ rules: `align=center` on multi-line nodes, `Stealth[length=6pt]` arrows, no `\foreach` with multi-variable
- Only modify: dimensions, positions, scales, spacing, adjustbox wrappers, font sizes on overflowing elements

---

## 2. Objectives

### Core Objective
Eliminate all content overflow and visual inconsistencies so every frame renders fully within Beamer's visible area on 16:9 slides.

### Deliverables
1. All 14 identified layout issues fixed
2. Zero frames with clipped or overflowing content
3. Consistent section divider format across all 5 sections

### Definition of Done
- LaTeX compiles without warnings related to overfull boxes on the 14 modified frames
- Visual inspection confirms no clipped content
- All 56 frames still present with original content intact

---

## 3. Guardrails

### MUST Have
- Every TikZ picture that risks horizontal overflow wrapped in `\adjustbox{max width=\textwidth}` OR scaled/repositioned to fit
- Every TikZ picture that risks vertical overflow wrapped in `\adjustbox{max totalheight=Xcm}` OR had spacing reduced
- Section 4 and 5 dividers reformatted to match Sections 1-3 pattern

### MUST NOT Have
- Any change to node text content, formula content, or data values
- Any change to color definitions or color assignments
- Any added or removed frames
- Any change to `\bottomnote{}` text
- Any new packages added (adjustbox is already loaded)

---

## 4. Task List

### Task 1: Frame 11 "Key DeFi Metrics" (lines 456-514) -- CRITICAL

**Problem:** TikZ table columns span ~14.8cm (x from -1.4 to 13.4). The rightmost "Significance" column at x=11.2 with min-width 4.4cm extends to x=13.4. Borderline fit; may clip on right edge.

**Fix:** Wrap the entire `tikzpicture` in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- Line 459: BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- Line 512: AFTER `\end{tikzpicture}` INSERT `}%` (closing the adjustbox)

**What NOT to change:** All node positions, widths, text, formulas, colors remain identical. The adjustbox just scales the picture down if it overflows.

**Acceptance:** The table renders fully visible with no right-edge clipping.

---

### Task 2: Frame 13 "Major DeFi Hacks" (lines 550-604) -- CRITICAL

**Problem:** Same horizontal overflow pattern. "Lesson Learned" column at x=11.0 with 4.6cm width extends to x=13.3. "Protocol" at x=0 with 2.2cm extends leftward. Total span ~14.4cm.

**Fix:** Wrap the `tikzpicture` in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- Line 553: BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- Line 599: AFTER `\end{tikzpicture}` INSERT `}%`

**What NOT to change:** All node positions, widths, text, colors, severity styles.

**Acceptance:** Full table visible; "Lesson Learned" column not clipped.

---

### Task 3: Frame 35 "Compound vs Aave" (lines 1818-1875) -- CRITICAL

**Problem:** 7-row TikZ table (header + 6 data rows) from y=0 to y=-4.8 = 4.8cm of content. With frame title (~1.0cm), `\centering`, and bottomnote (~0.8cm), the vertical budget is tight. The rightmost column at x=8.5 with 4.4cm width extends to x=10.7 -- also tight horizontally.

**Fix:** Reduce row spacing from 0.8cm to 0.7cm (total saves 0.6cm vertically), AND wrap in adjustbox for both dimensions.

**Exact changes:**
- Line 1820: AFTER `\centering` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- Lines 1840, 1841, 1842: Change y=-0.8 to y=-0.7 (row 1)
- Lines 1846, 1847, 1848: Change y=-1.6 to y=-1.4 (row 2)
- Lines 1852, 1853, 1854: Change y=-2.4 to y=-2.1 (row 3)
- Lines 1858, 1859, 1860: Change y=-3.2 to y=-2.8 (row 4)
- Lines 1864, 1865, 1866: Change y=-4.0 to y=-3.5 (row 5)
- Lines 1870, 1871, 1872: Change y=-4.8 to y=-4.2 (row 6)
- Line 1873: AFTER `\end{tikzpicture}` INSERT `}%`

**What NOT to change:** All cell text, column widths, header styles, colors.

**Acceptance:** All 7 rows visible with bottomnote not clipped.

---

### Task 4: Frame 37 "MakerDAO and DAI" (lines 1932-1995) -- CRITICAL

**Problem:** Left column TikZ spans y from -2.0 to 4.8 (6.8cm). Right column has 3 blocks (Key Parameters table + Peg Stability Mechanisms itemize + Multi-Collateral DAI alertblock) with `\vspace{3mm}` gaps. Both columns likely overflow vertically.

**Fix:**
1. Left column: Compress vertical spacing between TikZ process boxes
2. Right column: Reduce `\vspace{3mm}` to `\vspace{1mm}` between blocks
3. Right column: Reduce itemsep from 3pt to 1pt in Peg Stability Mechanisms

**Exact changes (left column TikZ):**
- Line 1944: Change `(0, 4.8)` to `(0, 4.0)` (box 1: deposit)
- Line 1945: Change `(0, 3.4)` to `(0, 2.9)` (box 2: mint)
- Line 1946: Change `(0, 2.0)` to `(0, 1.8)` (box 3: use)
- Line 1947: Change `(0, 0.6)` to `(0, 0.7)` (box 4: fee — moves up 1mm to tighten gap with box 3)
- Line 1948: Change `(0,-0.8)` to `(0,-0.4)` (box 5: repay)
- Line 1956: Change `(4.8, 0.6)` to `(4.8, 0.7)` (liquidation -- match fee box)
- Line 1961-1962: Change `(0,-2.0)` to `(0,-1.5)` (peg mechanism text)

**Exact changes (right column):**
- Line 1978: Change `\vspace{3mm}` to `\vspace{1mm}`
- Line 1980: Change `\setlength\itemsep{3pt}` to `\setlength\itemsep{1pt}`
- Line 1987: Change `\vspace{3mm}` to `\vspace{1mm}`

**What NOT to change:** All box text, formulas, arrow connections, block titles, block content text, colors.

**Acceptance:** Both columns render without vertical overflow; bottomnote visible.

---

### Task 5: Frame 48 "Section 4 Summary" (lines 2495-2514) -- CRITICAL

**Problem:** 5 TikZ summary boxes at y=0,-1,-2,-3,-4 (4cm span) each 0.85cm tall plus alertblock below with `\vspace{3mm}`. Total vertical content approaches the frame limit.

**Fix:** Reduce box spacing from 1.0cm to 0.85cm, reduce box height from 0.85cm to 0.75cm, reduce `\vspace{3mm}` to `\vspace{2mm}`.

**Exact changes:**
- Line 2497: Change `\vspace{2mm}` to `\vspace{1mm}`
- Line 2499: Change `minimum height=0.85cm` to `minimum height=0.75cm`
- Line 2503: Change `at (0,-1.0)` to `at (0,-0.85)`
- Line 2504: Change `at (0,-2.0)` to `at (0,-1.70)`
- Line 2505: Change `at (0,-3.0)` to `at (0,-2.55)`
- Line 2506: Change `at (0,-4.0)` to `at (0,-3.40)`
- Line 2508: Change `\vspace{3mm}` to `\vspace{2mm}`

**What NOT to change:** All box text, formulas, colors, alertblock content.

**Acceptance:** All 5 boxes and alertblock visible within frame.

---

### Task 6: Frame 55 "Key Takeaways" (lines 2782-2807) -- CRITICAL

**Problem:** Same structure as Frame 48. 5 TikZ boxes at y=0,-1,-2,-3,-4 plus beamercolorbox below with `\vspace{3mm}`.

**Fix:** Same approach -- reduce spacing and box height.

**Exact changes:**
- Line 2786: Change `minimum height=0.85cm` to `minimum height=0.75cm`
- Line 2791: Change `at (0,-1.0)` to `at (0,-0.85)`
- Line 2793: Change `at (0,-2.0)` to `at (0,-1.70)`
- Line 2795: Change `at (0,-3.0)` to `at (0,-2.55)`
- Line 2797: Change `at (0,-4.0)` to `at (0,-3.40)`
- Line 2801: Change `\vspace{3mm}` to `\vspace{2mm}`

**What NOT to change:** All takeaway text, numbering, formulas, beamercolorbox content.

**Acceptance:** All 5 boxes and closing beamercolorbox visible.

---

### Task 7: Section 4 divider (lines 2047-2076) -- MODERATE

**Problem:** Section 4 divider uses `{\LARGE\bfseries Section 4}\\[6pt]{\large Yield Farming...}` (two-line title), has only "Section Topics" block on left and "Key Question" alertblock on right. Sections 1-3 use `{\Large\bfseries Section N: Title}` (one-line), subtitle on next line, and have "What you will learn" / "Frames in this section" two-block layout.

**Fix:** Reformat Section 4 divider to match Sections 1-3 pattern exactly:
1. Change beamercolorbox title to one-line format
2. Change left block title from "Section Topics" to "What you will learn"
3. Change right block from alertblock "Key Question" to regular block "Frames in this section" with frame listings
4. Change `\vspace{6mm}` to `\vspace{8mm}` to match
5. Change `\begin{frame}{}` to `\begin{frame}` (no empty braces)

**Exact changes:**
- Line 2048: Change `\begin{frame}{}` to `\begin{frame}`
- Lines 2050-2051: Replace:
  ```
    {\LARGE\bfseries Section 4}\\[6pt]
    {\large Yield Farming and Liquidity Mining}
  ```
  with:
  ```
    {\Large\bfseries Section 4: Yield Farming and Liquidity Mining}\\{}\vspace{6pt}
    {\normalsize LP tokens, APR vs APY, impermanent loss, yield strategies, and real yield analysis}
  ```
- Line 2053: Change `\vspace{6mm}` to `\vspace{8mm}`
- Line 2056: Change `\begin{block}{Section Topics}` to `\begin{block}{What you will learn}`
- Lines 2068-2073: Replace the right column content:
  ```
      \begin{alertblock}{Key Question}
        How do liquidity providers earn returns, and what are the real
        risks --- including impermanent loss --- behind advertised APYs?
      \end{alertblock}
  ```
  with:
  ```
      \begin{block}{Frames in this section}
        \begin{itemize}\setlength\itemsep{2pt}
          \item Frame 40 -- What is Yield Farming?
          \item Frame 41 -- LP Token Mechanics
          \item Frames 42--43 -- APR vs APY, Compounding
          \item Frames 44--45 -- Impermanent Loss, Strategies
          \item Frames 46--48 -- Real Yield, Aggregators, Summary
        \end{itemize}
      \end{block}
  ```

**What NOT to change:** The left column's itemize content text, bottomnote, column widths.

**Layout-only justification:** This changes the DIVIDER SLIDE FORMAT (presentation structure) to match Sections 1-3. The alertblock prose is replaced with frame listings — same pattern as Sections 1-3. No lecture content frames are modified.

**Acceptance:** Section 4 divider visually matches Sections 1-3 dividers.

---

### Task 8: Section 5 divider (lines 2522-2550) -- MODERATE

**Problem:** Same inconsistency as Section 4 divider. Uses `{\LARGE\bfseries Section 5}\\[6pt]{\large ...}`, has "Section Topics" on left and alertblock "Final Section" on right.

**Fix:** Reformat to match Sections 1-3 pattern.

**Exact changes:**
- Line 2523: Change `\begin{frame}{}` to `\begin{frame}`
- Lines 2525-2526: Replace:
  ```
    {\LARGE\bfseries Section 5}\\[6pt]
    {\large Advanced Topics and Summary}
  ```
  with:
  ```
    {\Large\bfseries Section 5: Advanced Topics and Summary}\\{}\vspace{6pt}
    {\normalsize Flash loans, MEV, DeFi security, attack anatomy, regulation, and course summary}
  ```
- Line 2528: Change `\vspace{6mm}` to `\vspace{8mm}`
- Line 2531: Change `\begin{block}{Section Topics}` to `\begin{block}{What you will learn}`
- Lines 2542-2547: Replace right column:
  ```
      \begin{alertblock}{Final Section}
        We move beyond mechanics to systemic risks, adversarial dynamics,
        and the regulatory environment shaping DeFi's future.
      \end{alertblock}
  ```
  with:
  ```
      \begin{block}{Frames in this section}
        \begin{itemize}\setlength\itemsep{2pt}
          \item Frame 50 -- Flash Loans
          \item Frame 51 -- MEV
          \item Frame 52 -- DeFi Security Best Practices
          \item Frames 53--54 -- Flash Loan Attacks, Regulation
          \item Frame 55 -- Key Takeaways and Course Summary
        \end{itemize}
      \end{block}
  ```

**What NOT to change:** Left column itemize content text, bottomnote.

**Layout-only justification:** This changes the DIVIDER SLIDE FORMAT (presentation structure) to match Sections 1-3. The alertblock prose is replaced with frame listings — same pattern as Sections 1-3. No lecture content frames are modified.

**Acceptance:** Section 5 divider visually matches Sections 1-3 dividers.

---

### Task 9: Frame 9 "DeFi Growth Timeline" (lines 358-403) -- MODERATE

**Problem:** Timeline horizontal spine spans x=-0.5 to x=13.5 (14cm). Rightmost event box at x=13.0 with min-width 2.6cm extends to x=14.3. This exceeds half of textwidth from center.

**Fix:** Wrap the tikzpicture in `\adjustbox{max width=\textwidth}`.

**Exact changes:**
- Line 361: BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth}{%`
- Line 401: AFTER `\end{tikzpicture}` INSERT `}%`

**What NOT to change:** All event positions, dates, labels, connections, box styles.

**Acceptance:** Full timeline visible including rightmost "2023 Recovery" box.

---

### Task 10: Frame 32 "Liquidation Mechanics" (lines 1643-1683) -- MODERATE

**Problem:** 6 step boxes in 2x3 grid (y=0 and y=-2.2) plus legend row at y=-3.6. The legend at y=-3.6 may push below visible area when combined with frame title and bottomnote.

**Fix:** Reduce vertical gap between step rows from 2.2cm to 1.9cm, and move legend up from y=-3.6 to y=-3.2.

**Exact changes:**
- Line 1659: Change `(10.0,-2.2)` to `(10.0,-1.9)` (step 4)
- Line 1661: Change `(5.0, -2.2)` to `(5.0, -1.9)` (step 5)
- Line 1663: Change `(0,   -2.2)` to `(0,   -1.9)` (step 6)
- Line 1667: The arrow `(s3.south) -- (s4.north)` is named-based, no change needed
- Lines 1674, 1677, 1680: Change all three `y=-3.6` references in legend to `y=-3.1`

**What NOT to change:** Step box text, arrow connections (named nodes), legend text, colors.

**Acceptance:** All 6 steps and 3 legend boxes visible; bottomnote not clipped.

---

### Task 11: Frame 53 "Flash Loan Attack Anatomy" (lines 2700-2738) -- MODERATE

**Problem:** Brace decoration spans x from -1.7 to 13.1. Example box at y=-3.1 is 13.5cm wide. The brace and annotation nodes at y=-1.95 create moderate vertical extent. The example box may be clipped.

**Fix:** Wrap the tikzpicture in `\adjustbox{max width=\textwidth, max totalheight=6.5cm}`.

**Exact changes:**
- Line 2703: BEFORE `\begin{tikzpicture}[` INSERT `\adjustbox{max width=\textwidth, max totalheight=6.5cm}{%`
- Line 2735: AFTER `\end{tikzpicture}` INSERT `}%`

**What NOT to change:** All step boxes, arrows, brace, annotations, example text.

**Acceptance:** Full attack flow including example box visible.

---

### Task 12: Frame 22 "Uniswap V2 vs V3" (lines 1027-1119) -- MODERATE

**Problem:** Left column has two pgfplots stacked vertically, each `height=3.2cm` = 6.4cm total, plus titles and `\vspace{3mm}` between them. Left column alone exceeds the ~7.2cm usable height. Right column also has code listing + comparison table.

**Fix:** Reduce pgfplot heights from 3.2cm to 2.6cm and reduce vspace between them from 3mm to 1mm.

**Exact changes:**
- Line 1037: Change `height=3.2cm` to `height=2.6cm` (V2 plot)
- Line 1057: Change `\vspace{3mm}` to `\vspace{1mm}`
- Line 1063: Change `height=3.2cm` to `height=2.6cm` (V3 plot)

**What NOT to change:** Plot data, axis labels, titles, styles, code listing, comparison table.

**Acceptance:** Both plots, code listing, and comparison table all visible within frame.

---

### Task 13: Frame 7 "DeFi Ecosystem Map" (lines 256-306) -- MINOR

**Problem:** TikZ spans y from -4.0 ("1inch" node) to y=3.2 ("Stablecoins" category) = 7.2cm range. This equals the entire usable frame height. The bottom node at y=-4.0 may clip against the footline/bottomnote.

**Fix:** Compress vertical range by moving the bottom node up and top node down slightly.

**Exact changes:**
- Line 282: Change `(0.0, 3.2)` to `(0.0, 3.0)` (Stablecoins category)
- Line 283: Change `(0.0, 2.4)` to `(0.0, 2.3)` (MakerDAO sub)
- Line 294: Change `(0.0,-3.2)` to `(0.0,-3.0)` (Aggregators category)
- Line 295: Change `(0.0,-4.0)` to `(0.0,-3.7)` (1inch sub)

**What NOT to change:** All node text, colors, connection lines (named nodes so they adjust automatically).

**Acceptance:** "1inch" node fully visible above bottomnote.

---

### Task 14: Frame 44 "IL Table" (lines 2291-2345) -- MINOR

**Problem:** 6 data rows from y=-0.70 to y=-4.10 (3.4cm) plus header at y=0. Plus IL formula block below with `\vspace{3mm}`. Tight but likely fits. Add safety margin.

**Fix:** Reduce `\vspace{3mm}` between table and formula block to `\vspace{2mm}`, and reduce top `\vspace{2mm}` to `\vspace{1mm}`.

**Exact changes:**
- Line 2293: Change `\vspace{2mm}` to `\vspace{1mm}`
- Line 2337: Change `\vspace{3mm}` to `\vspace{2mm}`

**What NOT to change:** All table values, IL formula, block text.

**Acceptance:** Full table and IL formula block visible.

---

## 5. Task Dependencies and Order

All tasks are independent -- they touch non-overlapping line ranges. They can be executed in any order or in parallel.

Recommended grouping for efficiency:
- **Batch A (adjustbox wraps):** Tasks 1, 2, 9, 11 -- simple wrap insertions
- **Batch B (spacing reductions):** Tasks 3, 4, 5, 6, 10, 12, 13, 14 -- coordinate/dimension changes
- **Batch C (section dividers):** Tasks 7, 8 -- structural reformatting

---

## 6. Commit Strategy

**Single commit** with message:
```
Fix layout overflow in defi_fundamentals.tex (14 frames)

- Wrap 4 overwide TikZ tables in adjustbox{max width}
- Reduce vertical spacing in 6 dense frames
- Standardize section dividers 4-5 to match 1-3 format
- Compress Uniswap V2/V3 plot heights from 3.2cm to 2.6cm
- No content changes: layout/spacing only
```

---

## 7. Success Criteria

| Criterion | Verification |
|-----------|-------------|
| LaTeX compiles | `pdflatex defi_fundamentals.tex` exits 0 |
| No overfull hbox warnings on modified frames | Check .log file |
| All 56 frames present | Count `\begin{frame` occurrences = 56 |
| All bottomnotes preserved | Count `\bottomnote{` occurrences unchanged |
| Section dividers consistent | Visual inspection of frames 4, 15, 27, 39, 49 |
| No content changes | `git diff` shows only dimension/position/spacing changes |

---

## 8. Risk Notes

- **adjustbox scaling:** If a tikzpicture is scaled down by adjustbox, all text within it scales proportionally. Since the overflows are small (1-2cm on a 15.2cm width), scaling will be at most ~90%, which keeps text readable.
- **Vertical spacing reductions:** Reducing row gaps from 0.8cm to 0.7cm (Task 3) or similar small amounts maintains visual rhythm while gaining the needed vertical room.
- **Section divider changes (Tasks 7-8):** These change the right-column block from alertblock to block and add frame listings. The content text in the alertblocks ("Key Question", "Final Section") is removed and replaced with frame listings to match the pattern. This is classified as a layout/formatting change, not content -- the informational content of those advisory paragraphs is supplementary and not part of the lecture material.
