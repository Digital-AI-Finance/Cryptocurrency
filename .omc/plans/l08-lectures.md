# L08 Work Plan: Crypto Trading & Markets Standalone Lecture Bundle

## Context

### Original Request
Create the complete L08 Crypto Trading & Markets standalone lecture bundle following the exact patterns established in L04-L07 (most recently the Stablecoins & CBDCs bundle). The bundle includes a 55-frame technical lecture, 10-frame mini-lecture, 6-frame INTRO preview, pre-class handout, 4 HTML quizzes, and GitHub Pages integration.

### Reference Files (Structural Templates)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\stablecoins_cbdcs.tex` -- Tech lecture template (55 frames, 5 sections, 4 fragile code frames)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\stablecoins_intro.tex` -- Mini-lecture template (10 frames, TikZ comics, verbose preamble)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\stablecoins_cbdcs_intro.tex` -- INTRO preview template (6 frames, compact preamble)
- `D:\Joerg\Research\slides\cryptocurrency\lectures\stablecoins_cbdcs_preclass.tex` -- Pre-class handout template (article-class, 4 activities, glossary)
- `D:\Joerg\Research\slides\cryptocurrency\quiz\quiz_sc_part1.html` -- Quiz HTML template (KaTeX 0.16.9, 3-column grid, JSON data)
- `D:\Joerg\Research\slides\cryptocurrency\index.html` -- GitHub Pages (SC subsection pattern, d7 class)

### Key Patterns Extracted from Reference Files

**Tech lecture preamble (compact, single-line usepackage, lines 1-52):**
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

**Code frames: 4 total with `[fragile]`**
- Frame ~8: Simple Order Matching Engine pseudocode
- Frame ~20: Moving Average Crossover Strategy (Python-like)
- Frame ~30: VaR Calculation snippet (Python-like)
- Frame ~42: Simple AMM/DEX swap pseudocode

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
Produce a complete, self-contained L08 Crypto Trading & Markets lecture bundle that compiles without errors and integrates into the existing GitHub Pages site.

### Deliverables

| # | Deliverable | File Path | Description |
|---|-------------|-----------|-------------|
| 1 | Technical Lecture | `lectures/crypto_trading_markets.tex` | 55-frame Beamer presentation, 5 sections |
| 2 | Mini-Lecture | `lectures/crypto_trading_intro.tex` | 10-frame TikZ comic introduction |
| 3 | INTRO Preview | `lectures/crypto_trading_markets_intro.tex` | 6-frame preview with charts/diagrams |
| 4 | Pre-Class Handout | `lectures/crypto_trading_markets_preclass.tex` | Article-class, 4 activities, glossary |
| 5 | Quiz CT-1 | `quiz/quiz_ct_part1.html` | 20 questions: Market Microstructure |
| 6 | Quiz CT-2 | `quiz/quiz_ct_part2.html` | 20 questions: Trading Strategies |
| 7 | Quiz CT-3 | `quiz/quiz_ct_part3.html` | 20 questions: Portfolio & Risk |
| 8 | Quiz CT-4 | `quiz/quiz_ct_part4.html` | 20 questions: DEX/CEX & Regulation |
| 9 | index.html update | `index.html` | Add CT subsection, update hero stats |

### Definition of Done
- All 4 LaTeX files compile with `pdflatex` without errors
- All 4 HTML quiz files render correctly in browser
- index.html displays CT subsection with correct links and sidebar IDs
- Hero stats updated to 32 Lectures, 36 Quizzes
- Frame counts match: 55 tech + 10 mini + 6 intro = 71 frames total
- Exactly 4 `[fragile]` frames with code lstlisting in tech lecture (Frames 8, 20, 30, 42)
- Color palette matches L04-L07 exactly

---

## Must Have / Must NOT Have

### MUST Have
1. Exact same color palette (mlblue, mlpurple, mllavender 1-4, mlorange, mlgreen, mlred, mlgray)
2. Same Beamer theme configuration as stablecoins_cbdcs.tex
3. Same Solidity language definition and lstset (code frames use Python-like pseudocode via lstlisting, but Solidity lstdef must still be present for preamble consistency)
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

## 5-Section Topic Breakdown

### Section 1: Market Microstructure & Order Books (Frames 4-14, 11 frames)
How crypto exchanges work internally, order types, order book mechanics, bid-ask spreads, market depth, price discovery.

### Section 2: Trading Strategies (Frames 15-26, 12 frames)
Momentum strategies, mean-reversion, statistical arbitrage, cross-exchange arbitrage, technical indicators, backtesting concepts.

### Section 3: Portfolio Theory & Risk Management (Frames 27-38, 12 frames)
Modern portfolio theory applied to crypto, VaR, Sharpe ratio, maximum drawdown, correlation matrices, position sizing.

### Section 4: DEX vs CEX & Market Manipulation (Frames 39-48, 10 frames)
Centralized exchange architecture, decentralized exchange mechanics (AMMs, order book DEXs), wash trading, spoofing, front-running, MEV.

### Section 5: Regulation & Future of Crypto Trading (Frames 49-55, 7 frames)
Regulatory frameworks for crypto exchanges, MiCA trading rules, US SEC/CFTC jurisdiction, institutional adoption, algorithmic trading regulation, future outlook.

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

### TASK 1: Technical Lecture (`lectures/crypto_trading_markets.tex`)
**Priority:** HIGH | **Complexity:** HIGH | **Estimated frames:** 55

#### Preamble (copy from stablecoins_cbdcs.tex exactly)
- Compact single-line `\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb,listings,xcolor,colortbl}`
- All color definitions (mlblue through mlgray + solkeyword/string/comment/number)
- Beamer theme colors, navigation symbols, itemize, margins
- `\bottomnote` command
- Solidity language definition and `\lstset`
- TikZ/pgfplots with `\pgfplotsset{compat=1.18}`
- `\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,chains,decorations.pathmorphing,automata,fit}`
- Title: `Crypto Trading \& Markets: A Quantitative Deep Dive`
- Subtitle: `Standalone Technical Lecture`

#### OPENING (Frames 1-3)

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Lecture Roadmap**
- TikZ roadmap with 5 boxes (same style as SC roadmap):
  - Box 1 (mlblue): `1. Market\\Microstructure`
  - Box 2 (mlgreen): `2. Trading\\Strategies`
  - Box 3 (mlorange): `3. Portfolio\\Theory \& Risk`
  - Box 4 (mlred): `4. DEX vs CEX\\\& Manipulation`
  - Box 5 (mlpurple): `5. Regulation\\\& Future`
- Stealth arrows connecting boxes
- Two-column: Learning Objectives + Prerequisites
- `\bottomnote{Duration: 90 minutes | 5 sections | \textasciitilde55 frames | Prerequisite: Lessons 1--5}`

**Frame 3: Table of Contents**
- `\tableofcontents`
- `\bottomnote{Navigate through 5 sections covering market microstructure to regulation and the future of crypto trading}`

#### SECTION 1: Market Microstructure & Order Books (Frames 4-14)

**Frame 4: Section 1 Divider**
- `beamercolorbox` with palette quaternary
- Title: `Section 1: Market Microstructure \& Order Books`
- Subtitle: `Understanding how crypto exchanges match orders and discover prices`
- Two-column: What You Will Learn + Frames in This Section
- Learning items:
  - How order books work and how prices form
  - Types of orders: market, limit, stop-loss
  - Bid-ask spread and market depth analysis
  - Liquidity metrics and their significance

**Frame 5: The Crypto Trading Landscape**
- Two-column layout
- Left: Block explaining crypto market overview (24/7 trading, global fragmentation, $50B+ daily volume)
- Right: TikZ diagram showing trading venues: CEX (Binance, Coinbase), DEX (Uniswap, dYdX), OTC desks, dark pools
- Use hub-and-spoke with colored venue categories

**Frame 6: Order Book Anatomy**
- Full-width TikZ order book visualization:
  - Left side (mlgreen): Bid orders (buy) stacked by price descending
  - Right side (mlred): Ask orders (sell) stacked by price ascending
  - Middle: Spread zone highlighted
  - Depth bars showing volume at each price level
- Labels: Best bid, Best ask, Spread, Mid-price
- `\bottomnote{The order book is the core data structure of every exchange -- understanding it is fundamental to trading}`

**Frame 7: Order Types**
- TikZ comparison panel with 4 order types:
  - Panel 1 (mlblue): Market Order -- executes immediately at best available price
  - Panel 2 (mlgreen): Limit Order -- executes only at specified price or better
  - Panel 3 (mlorange): Stop-Loss Order -- triggers market order when price hits threshold
  - Panel 4 (mlred): Stop-Limit Order -- triggers limit order when price hits threshold
- Each with small TikZ icon showing execution logic

**Frame 8: Order Matching Engine [FRAGILE] -- CODE FRAME 1**
- `\begin{frame}[fragile]{Order Matching Engine}`
- Left column: Pseudocode for price-time priority matching
```
# Simple Order Matching Engine
def match_orders(order_book):
    while order_book.has_match():
        best_bid = order_book.top_bid()
        best_ask = order_book.top_ask()

        if best_bid.price >= best_ask.price:
            qty = min(best_bid.qty,
                      best_ask.qty)
            execute_trade(
                price=best_ask.price,
                quantity=qty)
            update_book(best_bid, best_ask,
                        qty)
        else:
            break  # no more matches
```
- Right column: explanation of price-time priority, FIFO matching, partial fills

**Frame 9: Bid-Ask Spread Analysis**
- Two-column:
  - Left: Definition block explaining spread = best ask - best bid
  - Right: pgfplots chart showing spread over time for BTC/USDT (narrow during high volume, wide during low volume)
- Key metrics: typical BTC spread (~0.01%), typical altcoin spread (0.1-1%), spread as cost of immediacy
- Formula: `Spread = P_{ask} - P_{bid}`, Relative Spread = $\frac{P_{ask} - P_{bid}}{P_{mid}} \times 100\%$

**Frame 10: Market Depth & Liquidity**
- TikZ market depth chart:
  - X-axis: Price, Y-axis: Cumulative volume
  - Green curve (bids): rising from left
  - Red curve (asks): rising from right
  - Intersection at mid-price
- Block explaining: thin order books = high slippage, deep books = efficient execution
- Liquidity metrics: bid-ask spread, order book depth, trade volume

**Frame 11: Price Discovery Mechanism**
- TikZ flow diagram showing price discovery:
  - New information arrives -> Informed traders submit orders -> Order book updates -> Price adjusts -> Market consensus
- Feedback loop arrows
- Efficient Market Hypothesis connection block

**Frame 12: Slippage and Market Impact**
- TikZ worked example:
  - Scenario: Buy 10 BTC with thin order book
  - Order book shows: 2 BTC at $40,000, 3 BTC at $40,050, 5 BTC at $40,150
  - Average fill price: weighted calculation
  - Slippage: difference from mid-price
- Color-coded cost breakdown

**Frame 13: Exchange Fee Structures**
- TikZ comparison table:
  - Maker fees vs Taker fees
  - Binance: 0.1%/0.1% (base), Coinbase: 0.4%/0.6%, Kraken: 0.16%/0.26%
  - Volume-based tiers
  - DEX fees: Uniswap 0.3%, Curve 0.04%
- Fee impact calculation on trading P&L

**Frame 14: Section 1 Summary**
- TikZ summary boxes (5 key takeaways, numbered, colored backgrounds)
- Same style as SC Section 1 Summary
  1. Order books match buyers and sellers via price-time priority
  2. Bid-ask spread is the cost of immediacy; it widens in low liquidity
  3. Market depth determines slippage for large orders
  4. Exchange fees vary significantly; makers often pay less than takers
  5. Price discovery in crypto is continuous and global (24/7 across venues)

#### SECTION 2: Trading Strategies (Frames 15-26)

**Frame 15: Section 2 Divider**
- Title: `Section 2: Trading Strategies`
- Subtitle: `Systematic approaches to profiting from crypto market dynamics`
- Learning items:
  - Momentum and trend-following strategies
  - Mean-reversion and statistical arbitrage
  - Cross-exchange arbitrage mechanics
  - Technical indicators and backtesting principles

**Frame 16: Trading Strategy Taxonomy**
- TikZ taxonomy tree:
  - Root: Trading Strategies
  - Branch 1 (mlblue): Trend Following (momentum, breakout)
  - Branch 2 (mlgreen): Mean Reversion (Bollinger, RSI-based)
  - Branch 3 (mlorange): Arbitrage (cross-exchange, triangular, statistical)
  - Branch 4 (mlred): Market Making (bid-ask capture, inventory risk)
  - Branch 5 (mlpurple): Event-Driven (news, on-chain signals)
- Rounded corners boxes with arrows

**Frame 17: Momentum & Trend Following**
- Two-column:
  - Left: Explanation of momentum effect in crypto (prices that went up tend to keep going up)
  - Right: pgfplots chart showing BTC price with 50-day and 200-day moving averages
  - Golden cross / death cross signals marked
- Key concept: "The trend is your friend until it bends"

**Frame 18: Moving Average Crossover**
- TikZ diagram showing crossover strategy logic:
  - Fast MA crosses above Slow MA -> BUY signal (green arrow)
  - Fast MA crosses below Slow MA -> SELL signal (red arrow)
  - Price line with both MAs overlaid
- Parameters: fast period (e.g., 20), slow period (e.g., 50)
- pgfplots visualization with synthetic data

**Frame 19: Bollinger Bands & Mean Reversion**
- Two-column:
  - Left: Definition of Bollinger Bands (20-day SMA +/- 2 standard deviations)
  - Right: pgfplots chart showing price oscillating within bands
  - Mean reversion signal: buy when price touches lower band, sell at upper band
- Formula: Upper = SMA + $k \times \sigma$, Lower = SMA - $k \times \sigma$

**Frame 20: Strategy Implementation [FRAGILE] -- CODE FRAME 2**
- `\begin{frame}[fragile]{Strategy Implementation}`
- Left column: Python-like pseudocode for moving average crossover
```
# Moving Average Crossover Strategy
import numpy as np

def ma_crossover(prices, fast=20,
                 slow=50):
    fast_ma = sma(prices, fast)
    slow_ma = sma(prices, slow)
    signals = []

    for i in range(1, len(prices)):
        if (fast_ma[i] > slow_ma[i] and
            fast_ma[i-1] <= slow_ma[i-1]):
            signals.append(("BUY", i))
        elif (fast_ma[i] < slow_ma[i] and
              fast_ma[i-1] >= slow_ma[i-1]):
            signals.append(("SELL", i))
    return signals
```
- Right column: explanation of signal generation, parameter sensitivity, overfitting risk

**Frame 21: Cross-Exchange Arbitrage**
- TikZ flow diagram:
  - Exchange A: BTC at $39,950
  - Exchange B: BTC at $40,050
  - Arbitrageur: Buy on A, sell on B, profit $100 minus fees and transfer costs
  - Timing arrows showing execution window
- Risk factors: transfer delay, price movement during transfer, counterparty risk

**Frame 22: Triangular Arbitrage**
- TikZ triangle diagram:
  - BTC/USDT -> ETH/BTC -> ETH/USDT -> back to USDT
  - Each edge labeled with exchange rate
  - Profit if product of rates != 1
- Worked example with specific rates showing small profit opportunity
- Note: requires ultra-low latency, typically bots only

**Frame 23: Statistical Arbitrage (Pairs Trading)**
- Two-column:
  - Left: Concept explanation -- find two correlated assets, trade the spread
  - Right: pgfplots showing BTC and ETH normalized prices diverging then converging
  - Signal: spread exceeds 2 standard deviations -> enter trade
- Cointegration test block

**Frame 24: Technical Indicators Overview**
- TikZ table of common indicators:
  - RSI (Relative Strength Index): momentum, 0-100 scale, overbought >70, oversold <30
  - MACD: trend, signal line crossovers
  - Volume Profile: support/resistance from volume distribution
  - OBV (On-Balance Volume): accumulation/distribution
  - Fibonacci Retracements: support/resistance levels
- Color-coded by category (momentum/trend/volume)

**Frame 25: Backtesting Principles**
- TikZ pipeline flow:
  - Historical Data -> Strategy Logic -> Signal Generation -> Execution Simulation -> Performance Metrics
- Key pitfalls listed:
  - Survivorship bias, look-ahead bias, overfitting, transaction costs omission
- Validation: in-sample vs out-of-sample, walk-forward analysis

**Frame 26: Section 2 Summary**
- 5-point summary boxes
  1. Momentum strategies exploit trending behavior but suffer in ranging markets
  2. Mean reversion works when assets oscillate around fair value
  3. Arbitrage opportunities exist but require speed and capital
  4. Technical indicators provide signals but are not predictive on their own
  5. Backtesting is essential but must account for biases and real-world frictions

#### SECTION 3: Portfolio Theory & Risk Management (Frames 27-38)

**Frame 27: Section 3 Divider**
- Title: `Section 3: Portfolio Theory \& Risk Management`
- Subtitle: `Quantitative frameworks for constructing and managing crypto portfolios`
- Learning items:
  - Modern Portfolio Theory applied to crypto assets
  - Value at Risk (VaR) and Expected Shortfall
  - Sharpe ratio and risk-adjusted performance
  - Maximum drawdown and position sizing

**Frame 28: Modern Portfolio Theory in Crypto**
- Two-column:
  - Left: MPT concept -- diversification reduces unsystematic risk
  - Right: TikZ efficient frontier plot (risk vs return)
  - Individual assets plotted: BTC, ETH, SOL, stablecoins
  - Efficient frontier curve showing optimal portfolios
- Key insight: crypto correlations are high, limiting diversification benefits

**Frame 29: Crypto Correlation Matrix**
- TikZ heatmap-style correlation matrix:
  - Assets: BTC, ETH, SOL, ADA, DOT, BNB
  - Color scale: dark red (1.0) through white (0.0) to blue (-1.0)
  - Most crypto pairs: 0.6-0.9 correlation
- Block: "High correlation during crashes reduces diversification exactly when you need it most"

**Frame 30: Value at Risk (VaR) [FRAGILE] -- CODE FRAME 3**
- `\begin{frame}[fragile]{Value at Risk (VaR)}`
- Left column: Python-like VaR calculation
```
# Historical VaR Calculation
import numpy as np

def calculate_var(returns,
                  confidence=0.95,
                  horizon=1):
    sorted_returns = np.sort(returns)
    index = int((1 - confidence)
                * len(sorted_returns))
    var_1d = abs(sorted_returns[index])

    # Scale to horizon (sqrt-T rule)
    var_hd = var_1d * np.sqrt(horizon)

    # Portfolio VaR
    portfolio_value = 100000  # USD
    dollar_var = portfolio_value * var_hd
    return var_hd, dollar_var
```
- Right column: explanation of VaR interpretation, confidence levels (95%, 99%), limitations (doesn't measure tail risk beyond threshold)

**Frame 31: Expected Shortfall (CVaR)**
- Two-column:
  - Left: Definition -- average loss beyond VaR threshold (answers "if things go bad, how bad?")
  - Right: TikZ distribution plot showing return distribution
  - VaR threshold marked, shaded tail region
  - CVaR = average of shaded tail
- Formula: $ES_\alpha = E[L | L > VaR_\alpha]$
- Comparison: VaR tells threshold, CVaR tells average severity

**Frame 32: Sharpe Ratio & Risk-Adjusted Returns**
- Two-column:
  - Left: Formula and interpretation
  - Formula: $S = \frac{R_p - R_f}{\sigma_p}$
  - Where $R_p$ = portfolio return, $R_f$ = risk-free rate, $\sigma_p$ = portfolio std dev
  - Right: TikZ bar chart comparing Sharpe ratios of different strategies
  - Buy-and-hold BTC, 60/40 BTC/ETH, MA crossover, equal-weight top 10
- Interpretation: >1 good, >2 very good, >3 excellent (sustained is rare in crypto)

**Frame 33: Sortino Ratio & Downside Risk**
- Two-column:
  - Left: Sortino formula -- penalizes only downside volatility
  - Formula: $Sortino = \frac{R_p - R_f}{\sigma_{downside}}$
  - Right: TikZ comparison of two strategies with same Sharpe but different Sortino
  - Strategy A: symmetric volatility. Strategy B: low downside, high upside (better Sortino)
- Why it matters: crypto returns are highly skewed

**Frame 34: Maximum Drawdown**
- TikZ portfolio value chart over time:
  - Peak to trough highlighted with red shading
  - Recovery period shown with dashed line
  - MDD formula: $MDD = \frac{Trough - Peak}{Peak}$
- Historical examples:
  - BTC 2017-18: -84% drawdown
  - BTC 2021-22: -77% drawdown
  - ETH 2022: -82% drawdown
- Recovery time analysis

**Frame 35: Position Sizing**
- TikZ decision tree for position sizing:
  - Kelly Criterion: $f^* = \frac{p \cdot b - q}{b}$ where p=win prob, b=win/loss ratio, q=1-p
  - Fixed fractional: risk X% of portfolio per trade
  - Volatility-based: size inversely proportional to asset volatility
- Worked example with specific numbers
- Warning: full Kelly is aggressive; half-Kelly commonly used

**Frame 36: Portfolio Construction**
- TikZ layered portfolio diagram:
  - Core (60%): BTC + ETH (large-cap, high liquidity)
  - Satellite (25%): L1 alts (SOL, ADA, AVAX)
  - Tactical (10%): DeFi tokens, momentum plays
  - Cash/Stables (5%): USDC/USDT for dry powder
- Rebalancing trigger: when allocation drifts >5% from target

**Frame 37: Risk Monitoring Dashboard**
- TikZ dashboard mockup with 6 panels:
  - Panel 1: Portfolio P&L (line chart)
  - Panel 2: VaR gauge (current vs limit)
  - Panel 3: Correlation heatmap (mini)
  - Panel 4: Drawdown tracker
  - Panel 5: Position concentration (pie)
  - Panel 6: Volatility regime indicator
- Real-time risk management concept

**Frame 38: Section 3 Summary**
- 5-point summary boxes
  1. MPT applies to crypto but high correlations limit diversification
  2. VaR quantifies downside risk; CVaR measures tail severity
  3. Sharpe and Sortino ratios enable risk-adjusted strategy comparison
  4. Maximum drawdown matters more than volatility for long-term investors
  5. Position sizing (Kelly, fixed fractional) prevents catastrophic losses

#### SECTION 4: DEX vs CEX & Market Manipulation (Frames 39-48)

**Frame 39: Section 4 Divider**
- Title: `Section 4: DEX vs CEX \& Market Manipulation`
- Subtitle: `Exchange architectures and the dark side of crypto markets`
- Learning items:
  - Centralized exchange architecture and risks
  - Decentralized exchange mechanics (AMMs, CLOBs)
  - Common manipulation tactics: wash trading, spoofing, front-running
  - MEV and sandwich attacks in DeFi

**Frame 40: Centralized Exchange (CEX) Architecture**
- TikZ layered architecture diagram:
  - Layer 1: User Interface (web, mobile, API)
  - Layer 2: Matching Engine (order book, price-time priority)
  - Layer 3: Risk Engine (margin checks, position limits)
  - Layer 4: Settlement (internal ledger, wallet management)
  - Layer 5: Custody (hot wallets, cold storage)
- Centralization risks: single point of failure, hacks, insolvency (FTX)

**Frame 41: CEX Risks & Failures**
- TikZ timeline of major exchange failures:
  - 2014: Mt. Gox ($460M lost)
  - 2016: Bitfinex ($72M hack)
  - 2019: QuadrigaCX ($190M locked)
  - 2022: FTX ($8B+ customer funds misused)
  - 2023: Various smaller exchanges
- "Not your keys, not your coins" principle block

**Frame 42: DEX Architecture & AMMs [FRAGILE] -- CODE FRAME 4**
- `\begin{frame}[fragile]{DEX Architecture \& AMMs}`
- Left column: Pseudocode for constant product AMM swap
```
# Constant Product AMM (x * y = k)
def swap_exact_input(reserve_x,
                     reserve_y,
                     amount_in,
                     fee=0.003):
    amount_in_with_fee = (
        amount_in * (1 - fee))
    k = reserve_x * reserve_y

    new_reserve_x = (
        reserve_x + amount_in_with_fee)
    new_reserve_y = k / new_reserve_x
    amount_out = (
        reserve_y - new_reserve_y)
    return amount_out
```
- Right column: explanation of x*y=k invariant, impermanent loss concept, concentrated liquidity

**Frame 43: CEX vs DEX Comparison**
- TikZ comparison table (two panels side by side):
  - CEX: Custodial, KYC required, fast execution, fiat on-ramp, counterparty risk
  - DEX: Non-custodial, permissionless, on-chain settlement, smart contract risk, no fiat
- Metrics: latency (ms vs seconds), throughput (millions vs thousands TPS), liquidity depth
- Hybrid models: dYdX (order book on-chain), Blur (aggregator)

**Frame 44: Wash Trading**
- TikZ flow diagram showing wash trading:
  - Trader A (= Trader B, same entity) places buy and sell orders
  - Trades execute, volume inflates, but no real economic transfer
  - Purpose: inflate volume metrics, manipulate rankings, earn fee rebates
- Estimated prevalence: some studies suggest 50-90% of reported crypto volume is wash
- Detection methods: statistical analysis, network graph analysis

**Frame 45: Spoofing & Layering**
- TikZ order book visualization showing spoofing:
  - Step 1: Place large buy wall (1000 BTC at $39,500) -- creates illusion of support
  - Step 2: Other traders buy, pushing price up
  - Step 3: Cancel the large order before it fills
  - Step 4: Sell at the higher price
- Before/after order book snapshots

**Frame 46: Front-Running & MEV**
- TikZ blockchain mempool visualization:
  - User submits swap transaction (buy 100 ETH)
  - Searcher sees pending transaction in mempool
  - Sandwich attack: Searcher buys ETH first (front-run) -> User's trade executes at worse price -> Searcher sells ETH (back-run)
  - Profit = price impact extracted from user
- MEV (Maximal Extractable Value) definition and scale ($1B+ cumulative on Ethereum)

**Frame 47: Market Manipulation Detection**
- TikZ flow showing detection approaches:
  - Statistical methods: Benford's law, volume anomaly detection, order-to-trade ratio
  - Network analysis: cluster wallets, identify connected entities
  - Pattern recognition: spoofing signatures, wash trade loops
- Regulatory challenge: cross-jurisdictional, pseudonymous

**Frame 48: Section 4 Summary**
- 5-point summary boxes
  1. CEXs offer speed and fiat access but introduce custodial and counterparty risk
  2. DEXs provide trustless trading via AMMs but face slippage and smart contract risk
  3. Wash trading inflates volumes; estimating real crypto market activity is difficult
  4. Spoofing, layering, and front-running exploit information asymmetries
  5. MEV is a unique DeFi problem where miners/validators extract value from users

#### SECTION 5: Regulation & Future of Crypto Trading (Frames 49-55)

**Frame 49: Section 5 Divider**
- Title: `Section 5: Regulation \& Future of Crypto Trading`
- Subtitle: `Regulatory frameworks shaping the future of digital asset markets`
- Learning items:
  - Major regulatory frameworks for crypto exchanges
  - MiCA and US regulatory approaches
  - Institutional adoption and its market impact
  - The future: algorithmic trading regulation, tokenized assets

**Frame 50: Global Regulatory Landscape**
- TikZ table comparing regulatory approaches:
  - EU (MiCA): exchange licensing, market abuse rules, transparency requirements
  - US: SEC (securities) vs CFTC (commodities) jurisdiction battle, proposed bills
  - Singapore: MAS framework, licensed exchanges
  - Japan: FSA registered exchanges, strict custody rules
- Color-coded strictness levels

**Frame 51: MiCA Trading Provisions**
- Two-column:
  - Left: Key MiCA provisions for trading
  - Market abuse prohibition (insider trading, manipulation)
  - Exchange authorization requirements
  - Custody and segregation rules
  - Transparency and reporting obligations
  - Right: TikZ timeline showing MiCA implementation phases
- Impact assessment block

**Frame 52: Institutional Adoption**
- TikZ progression diagram:
  - 2017: Retail-dominated, ICO boom
  - 2020: Corporate treasury (MicroStrategy, Tesla)
  - 2021: ETF proposals, traditional exchanges add crypto
  - 2024: Bitcoin spot ETFs approved, institutional custody
  - 2025+: Tokenized securities, regulated DeFi
- Impact on market structure: deeper liquidity, tighter spreads, lower volatility

**Frame 53: Algorithmic Trading Regulation**
- Two-column:
  - Left: Current landscape -- largely unregulated in crypto, regulated in TradFi (MiFID II)
  - Right: TikZ comparison of TradFi algo requirements vs crypto
  - Requirements: kill switches, risk limits, testing, registration
  - Crypto gap: no circuit breakers, no pre-trade risk checks on many exchanges
- Future direction: convergence with TradFi standards

**Frame 54: The Future of Crypto Trading**
- TikZ three-panel forward-looking:
  - Panel 1: Market structure evolution (24/7 regulated markets, cross-chain liquidity)
  - Panel 2: Technology convergence (AI-driven strategies, real-time risk, DeFi-CeFi bridges)
  - Panel 3: Regulatory clarity (global standards, investor protection, innovation balance)
- Timeline projections

**Frame 55: Key Takeaways and Course Summary**
- TikZ 5-box summary (matching SC Frame 55 style):
  - Box 1 (mlblue): Market microstructure -- order books, spreads, and liquidity form the foundation of all trading
  - Box 2 (mlpurple): Systematic strategies (momentum, mean-reversion, arbitrage) can be backtested but beware overfitting
  - Box 3 (mlgreen): Risk management (VaR, Sharpe, drawdown) is not optional -- it determines long-term survival
  - Box 4 (mlorange): DEXs democratize access but introduce new risks; manipulation remains prevalent across venues
  - Box 5 (mlred): Regulation is converging globally; institutional adoption is transforming market structure
- Purple teaser bar: `Next: Advanced topics in DeFi risk management and quantitative crypto finance`

**Acceptance Criteria (Task 1):**
- [ ] Exactly 55 frames with correct numbering
- [ ] 5 sections with divider and summary frames
- [ ] Exactly 4 `[fragile]` frames with lstlisting (Frames 8, 20, 30, 42)
- [ ] Preamble matches stablecoins_cbdcs.tex exactly
- [ ] All TikZ multi-line nodes have `align=center`
- [ ] No `\foreach` with `/` multi-variable syntax
- [ ] No parameterized styles with `#1`
- [ ] `\bottomnote` on every frame
- [ ] Compiles with pdflatex without errors

---

### TASK 2: Mini-Lecture (`lectures/crypto_trading_intro.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM | **Estimated frames:** 10

#### Preamble
- Copy the ENTIRE preamble from `stablecoins_intro.tex` (verbose style), changing only:
  - Title: `Crypto Trading \& Markets: A Visual Introduction`
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
- Quote: `"Markets can remain irrational longer than you can remain solvent" -- John Maynard Keynes`
- Purple title, blue subtitle

**Frame 2: How Do Crypto Exchanges Work? (TikZ Comic)**
- 3-panel comic layout (same panel dimensions as stablecoins_intro.tex):
  - Panel 1: Alice wants to buy ETH. She places a limit order on the exchange. "I'll pay up to \$2000 for 1 ETH!"
  - Panel 2: Bob wants to sell ETH. He places an ask. "I'll sell 1 ETH for \$2000!" The matching engine connects them.
  - Panel 3: Trade executes! Alice gets ETH, Bob gets USDT. Exchange takes a tiny fee. Both satisfied.
- Stick figures, speech bubbles, same drawing style as SC intro

**Frame 3: The Order Book**
- Two-column visual:
  - Left: TikZ order book with green bids stacked below, red asks stacked above
  - Right: Key terms block -- Best bid, Best ask, Spread, Depth
- Visual metaphor: order book as "supply and demand in real-time"

**Frame 4: Trading Strategies for Beginners (TikZ Comic)**
- 3-panel layout:
  - Panel 1: "Buy Low, Sell High" -- character looking at a dip, buying with confidence
  - Panel 2: "Follow the Trend" -- character riding a wave (moving average) upward
  - Panel 3: "Arbitrage" -- character buying cheap on Exchange A, selling expensive on Exchange B, pocketing the difference
- Each panel labeled with strategy name

**Frame 5: What is Risk?**
- TikZ layered diagram:
  - Layer 1: Portfolio value going up and down (wavy line)
  - Layer 2: Volatility envelope around the line
  - Layer 3: Maximum drawdown highlighted (peak to trough)
- Simple explanation: risk = the chance you lose money, measured by volatility and drawdown

**Frame 6: The Sharpe Ratio Explained (TikZ Comic)**
- 3-panel comic:
  - Panel 1: Strategy A made 50% return! "Amazing!" But it swung +/- 40% along the way. "Terrifying..."
  - Panel 2: Strategy B made 20% return. "Modest." But it swung only +/- 5%. "Smooth ride!"
  - Panel 3: Sharpe Ratio: B wins! Return per unit of risk is what matters. Character holding trophy.

**Frame 7: CEX vs DEX**
- TikZ comparison grid:
  - CEX: Centralized, fast, requires KYC, custodial ("they hold your keys")
  - DEX: Decentralized, smart contracts, no KYC, non-custodial ("you control your keys")
- Color-coded quadrants with icons (building for CEX, chain links for DEX)

**Frame 8: Market Manipulation (TikZ Comic)**
- 3-panel layout:
  - Panel 1: Whale places huge buy wall. Small traders see it: "The price must be going up!" They buy.
  - Panel 2: Whale cancels the order and sells at the inflated price. "That's spoofing!"
  - Panel 3: Character reading newspaper: "90% of reported volume might be fake." Warning sign: "Always verify data."

**Frame 9: Regulation is Coming**
- TikZ progression:
  - 2020: Wild West (minimal rules)
  - 2023: MiCA passed in EU, SEC enforcement in US
  - 2025: Licensed exchanges, investor protection, market surveillance
  - Future: Global standards, institutional-grade markets
- Traffic light analogy: red (banned), yellow (regulated), green (licensed)

**Frame 10: Key Takeaways**
- TikZ numbered boxes (5 takeaways):
  1. Crypto markets operate 24/7 with order books matching buyers and sellers
  2. Strategies like momentum, mean-reversion, and arbitrage have clear logic but real risks
  3. Risk management (Sharpe, VaR, drawdown) separates gamblers from traders
  4. DEXs offer freedom but CEXs offer convenience -- both have tradeoffs
  5. Regulation is transforming crypto from Wild West to regulated financial markets
- Purple teaser bar at bottom

**Acceptance Criteria (Task 2):**
- [ ] Exactly 10 frames
- [ ] Zero `[fragile]` frames, zero lstlisting
- [ ] All TikZ comics use same panel style as stablecoins_intro.tex (draw, rounded corners, stick figures)
- [ ] All multi-line TikZ nodes have `align=center`
- [ ] Verbose preamble matching stablecoins_intro.tex structure
- [ ] Compiles with pdflatex without errors

---

### TASK 3: INTRO Preview (`lectures/crypto_trading_markets_intro.tex`)
**Priority:** HIGH | **Complexity:** LOW | **Estimated frames:** 6

#### Preamble
- Compact preamble matching `stablecoins_cbdcs_intro.tex` exactly
- Same compact style as tech lecture BUT without colortbl, without Solidity definition
- Minimal TikZ libraries: `arrows.meta,positioning,shapes.geometric,calc`
- Title: `Crypto Trading \& Markets: Course Preview`
- Subtitle: `INTRO Preview`

#### Frame Specifications

**Frame 1: Title**
- `\begin{frame}\titlepage\end{frame}`

**Frame 2: Why Crypto Trading & Markets Matter**
- Two-column: pgfplots bar chart (left) + Key Metrics block (right)
- Chart: Daily crypto trading volume, number of exchanges, algorithmic trading share (normalized)
- Key metrics: $50B+ daily volume, 500+ exchanges globally, 70%+ algorithmic trading, 24/7/365 operation

**Frame 3: Trading & Markets Ecosystem at a Glance**
- TikZ hub diagram (same style as SC "Ecosystem at a Glance"):
  - Center: Crypto Trading Ecosystem
  - Spokes: CEX (Binance, Coinbase), DEX (Uniswap, dYdX), Derivatives (futures, options), OTC Desks, Lending Markets, Aggregators
- Color-coded by type

**Frame 4: Market Growth Trajectory**
- Two-column: pgfplots line chart (left) + Growth Drivers block (right)
- Chart: Global crypto trading volume 2018-2025
- Growth drivers: Institutional entry, DeFi maturation, regulatory clarity, tokenized assets

**Frame 5: Course Coverage**
- TikZ 5-step process flow (same style as SC "Course Coverage"):
  - (1) Market Microstructure
  - (2) Trading Strategies
  - (3) Portfolio & Risk
  - (4) DEX vs CEX
  - (5) Regulation & Future
- Sub-labels for each step
- Prerequisites + Outcomes blocks

**Frame 6: What You Will Learn**
- Two-column: Learning Outcomes block (left) + TikZ skill diagram (right)
- Outcomes: order book mechanics, quantitative strategies, risk frameworks, exchange architectures, regulatory landscape
- TikZ: central "Crypto Trading Mastery" node with 5 skill spokes

**Acceptance Criteria (Task 3):**
- [ ] Exactly 6 frames
- [ ] Compact preamble matching stablecoins_cbdcs_intro.tex
- [ ] pgfplots charts with correct axis styling
- [ ] Compiles with pdflatex without errors

---

### TASK 4: Pre-Class Handout (`lectures/crypto_trading_markets_preclass.tex`)
**Priority:** HIGH | **Complexity:** MEDIUM

#### Preamble
- Article-class matching `stablecoins_cbdcs_preclass.tex` exactly
- `\documentclass[11pt,a4paper]{article}`
- Same packages: inputenc, fontenc, geometry, xcolor, enumitem, titlesec, fancyhdr, hyperref, booktabs, tabularx, verbatim, amsmath, amssymb
- Color definitions using HTML format (not RGB)
- Header: `Crypto Trading \& Markets | Lesson 08 | Pre-Class Discovery Handout`
- `\activitybox` and `\fillcell` commands

#### Activity 1: Explore a Live Order Book (10 min)
- Visit a crypto exchange (Binance, Coinbase, or use TradingView), answer:
  1. What is the current bid-ask spread for BTC/USDT? How does it compare to ETH/USDT?
  2. Look at the order book depth -- are there large buy or sell walls? At what price levels?
  3. Place a hypothetical limit order for $10,000 worth of BTC -- how much slippage would you experience?
  4. How does the spread change during different hours of the day? Check at two different times.
- Bonus: Screenshot the order book and annotate bid, ask, spread, and depth.

#### Activity 2: Backtest a Simple Strategy (10 min)
- Visit TradingView or CoinGecko charts for BTC, answer:
  1. Add a 20-day and 50-day simple moving average. How many crossovers occurred in the last 6 months?
  2. Identify the golden cross (bullish) and death cross (bearish) signals. Were they profitable?
  3. Add Bollinger Bands (20-day, 2 std dev). How many times did BTC touch the lower band?
  4. Would a mean-reversion strategy (buy at lower band, sell at upper band) have been profitable?
- Fill-in table: Signal Date | Type (Buy/Sell) | Price | Outcome (Profit/Loss)

#### Activity 3: Risk Metrics Calculation (5 min)
- Using BTC's last 30 days of daily returns (from CoinGecko or Yahoo Finance):
  1. Calculate the daily standard deviation (volatility)
  2. Estimate the 95% 1-day VaR (= 1.65 x daily std dev)
  3. If your portfolio is $10,000 in BTC, what is your dollar VaR?
  4. What was the maximum drawdown in the last 30 days?
- Fill-in: Daily Std Dev: ___ | 95% VaR: ___% | Dollar VaR: $___ | Max Drawdown: ___%

#### Activity 4: CEX vs DEX Comparison (5 min)
- Compare one CEX (Binance or Coinbase) and one DEX (Uniswap or SushiSwap):
  1. What fees does each charge for a swap/trade?
  2. Does the CEX require KYC? How long does verification take?
  3. For the DEX, what is the estimated slippage for a $10,000 swap?
  4. Which would you choose for a large trade ($100,000+) and why?
- Fill-in table: Feature | CEX | DEX | Your Preference

#### Glossary (14 terms)

| Term | Definition |
|------|-----------|
| **Order Book** | A real-time list of buy (bid) and sell (ask) orders organized by price level. The core data structure of centralized exchanges enabling price discovery. |
| **Bid-Ask Spread** | The difference between the highest buy price (best bid) and the lowest sell price (best ask). Represents the cost of immediate execution and a proxy for liquidity. |
| **Slippage** | The difference between the expected execution price and the actual fill price, caused by insufficient liquidity at the desired price level. Increases with order size. |
| **Market Maker** | A participant who provides liquidity by continuously quoting bid and ask prices, profiting from the spread while bearing inventory risk. |
| **Momentum Strategy** | A trading approach that buys assets with recent positive returns and sells those with negative returns, based on the empirical observation that trends tend to persist. |
| **Mean Reversion** | A strategy based on the tendency of prices to return to their historical average. Buys when price is below average, sells when above. |
| **Arbitrage** | The simultaneous purchase and sale of the same asset on different markets to profit from price discrepancies, theoretically risk-free. |
| **Value at Risk (VaR)** | A statistical measure estimating the maximum potential loss over a given time horizon at a specified confidence level (e.g., 95% VaR = loss exceeded only 5% of the time). |
| **Sharpe Ratio** | A measure of risk-adjusted return calculated as (portfolio return - risk-free rate) / portfolio standard deviation. Higher is better. |
| **Maximum Drawdown** | The largest peak-to-trough decline in portfolio value before a new peak is reached. A key measure of downside risk for traders and investors. |
| **AMM (Automated Market Maker)** | A smart contract that provides liquidity using a mathematical formula (e.g., x*y=k) instead of an order book. Used by DEXs like Uniswap. |
| **MEV (Maximal Extractable Value)** | The profit that block producers or searchers can extract by including, excluding, or reordering transactions within a block. Includes front-running and sandwich attacks. |
| **Wash Trading** | The practice of simultaneously buying and selling the same asset to create artificial trading volume, misleading other market participants about true liquidity. |
| **Spoofing** | Placing large orders with the intent to cancel before execution, creating a false impression of supply or demand to manipulate prices. Illegal in regulated markets. |

**Acceptance Criteria (Task 4):**
- [ ] Article-class preamble matches stablecoins_cbdcs_preclass.tex
- [ ] 4 activities with `\activitybox` command
- [ ] Glossary with 14 terms in tabular format
- [ ] Header says "Lesson 08"
- [ ] Fill-in tables with `\fillcell`
- [ ] Compiles with pdflatex without errors

---

### TASK 5: Quiz CT-1 (`quiz/quiz_ct_part1.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz CT-1: Market Microstructure`
- 20 questions covering Section 1 topics:
  - Order book mechanics and structure (Q1-Q4)
  - Order types: market, limit, stop-loss (Q5-Q8)
  - Bid-ask spread and slippage (Q9-Q12)
  - Market depth and liquidity (Q13-Q16)
  - Price discovery and exchange fees (Q17-Q20)
- Format: A/B/C/D multiple choice with explanations
- **Note:** The existing quiz template has NO prev/next inter-quiz navigation links. Do NOT add prev/next links. The nav section contains only Dashboard and GitHub links. Copy this pattern as-is.
- Copy CSS/JS structure from quiz_sc_part1.html exactly

**Acceptance Criteria:**
- [ ] KaTeX v0.16.9 linked
- [ ] CSS variables match template
- [ ] 3-column grid layout
- [ ] 20 questions with JSON data
- [ ] All questions have correct answer and explanation
- [ ] Renders correctly in browser

---

### TASK 6: Quiz CT-2 (`quiz/quiz_ct_part2.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz CT-2: Trading Strategies`
- 20 questions covering Section 2 topics:
  - Momentum and trend-following (Q1-Q4)
  - Moving averages and crossover signals (Q5-Q8)
  - Mean reversion and Bollinger Bands (Q9-Q12)
  - Arbitrage types (cross-exchange, triangular, statistical) (Q13-Q16)
  - Technical indicators and backtesting (Q17-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 7: Quiz CT-3 (`quiz/quiz_ct_part3.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz CT-3: Portfolio Theory & Risk`
- 20 questions covering Section 3 topics:
  - Modern Portfolio Theory in crypto (Q1-Q4)
  - Value at Risk and Expected Shortfall (Q5-Q8)
  - Sharpe ratio, Sortino ratio (Q9-Q12)
  - Maximum drawdown and position sizing (Q13-Q16)
  - Portfolio construction and risk monitoring (Q17-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 8: Quiz CT-4 (`quiz/quiz_ct_part4.html`)
**Priority:** MEDIUM | **Complexity:** MEDIUM

- Title: `Quiz CT-4: DEX/CEX & Regulation`
- 20 questions covering Sections 4-5 topics:
  - CEX architecture and risks (Q1-Q4)
  - DEX mechanics and AMMs (Q5-Q8)
  - Market manipulation: wash trading, spoofing (Q9-Q12)
  - MEV, front-running, sandwich attacks (Q13-Q15)
  - Regulation: MiCA, US SEC/CFTC (Q16-Q18)
  - Future of crypto trading (Q19-Q20)
- **Note:** No prev/next inter-quiz navigation. Copy template nav (Dashboard + GitHub links only).

**Acceptance Criteria:** Same as Task 5.

---

### TASK 9: GitHub Pages Update (`index.html`)
**Priority:** HIGH | **Complexity:** LOW

#### Changes Required

**1. Add d8 CSS class (after d7 styles, around line 94):**
```css
.section-head.d8 span{background:#10b981}
.d8 summary{border-left:3px solid #10b981}
```
*Note: Do NOT add `.d8 .lcard-num` -- the CT HTML uses `lec-tag` classes, not `lcard-num`. The `lec-tag` and `quiz-tag` classes are intentionally unstyled (same as DF/NF/SC sections). Copy the HTML pattern as-is for consistency.*

**2. Add CT sidebar links (after SC entries in the Standalone Lectures details, before `</details>`):**
```html
<a href="#sl-ct-mini">Mini-Lecture: Crypto Trading</a>
<a href="#sl-ct-intro">CT INTRO Preview</a>
<a href="#sl-ct-pre">CT Pre-Class Handout</a>
<a href="#sl-ct-main">CT Technical Lecture</a>
```

**3. Update hero stats:**
- Lectures: 28 -> 32
- Quizzes: 32 -> 36

**4. Add CT subsection (after SC quiz-grid closing `</div>`, before `</section>`):**
The CT subsection goes between the SC closing div (after quiz_sc_part4 card) and the `</section>` tag that closes the standalone lectures section (currently line 601).

```html
<div class="section-head d8" style="margin-top:16px"><span>CT</span><h2>Standalone Lectures: Crypto Trading &amp; Markets</h2></div>
<div class="lec-grid">
<a href="lectures/crypto_trading_intro.pdf" class="lec-card" id="sl-ct-mini">
<div class="lec-tag mini">Mini-Lecture</div>
<h3>Crypto Trading &amp; Markets: Visual Introduction</h3>
<p>10 frames &bull; TikZ comics &bull; Zero code</p></a>
<a href="lectures/crypto_trading_markets_intro.pdf" class="lec-card" id="sl-ct-intro">
<div class="lec-tag intro">INTRO Preview</div>
<h3>Crypto Trading &amp; Markets: Course Preview</h3>
<p>6 frames &bull; Charts &amp; roadmap</p></a>
<a href="lectures/crypto_trading_markets_preclass.pdf" class="lec-card" id="sl-ct-pre">
<div class="lec-tag pre">Pre-Class</div>
<h3>Crypto Trading &amp; Markets: Pre-Class Handout</h3>
<p>4 activities &bull; Order books, backtesting, risk metrics</p></a>
<a href="lectures/crypto_trading_markets.pdf" class="lec-card" id="sl-ct-main">
<div class="lec-tag main">Technical Lecture</div>
<h3>Crypto Trading &amp; Markets: Quantitative Deep Dive</h3>
<p>~55 frames &bull; Microstructure, strategies, risk, regulation</p></a>
</div>
<div class="quiz-grid">
<a href="quiz/quiz_ct_part1.html" class="quiz-card">
<div class="quiz-tag">Quiz CT-1</div>
<h3>Market Microstructure</h3>
<p>20 questions &bull; Order books, spreads, liquidity</p></a>
<a href="quiz/quiz_ct_part2.html" class="quiz-card">
<div class="quiz-tag">Quiz CT-2</div>
<h3>Trading Strategies</h3>
<p>20 questions &bull; Momentum, mean-reversion, arbitrage</p></a>
<a href="quiz/quiz_ct_part3.html" class="quiz-card">
<div class="quiz-tag">Quiz CT-3</div>
<h3>Portfolio Theory &amp; Risk</h3>
<p>20 questions &bull; VaR, Sharpe, drawdown, sizing</p></a>
<a href="quiz/quiz_ct_part4.html" class="quiz-card">
<div class="quiz-tag">Quiz CT-4</div>
<h3>DEX/CEX &amp; Regulation</h3>
<p>20 questions &bull; AMMs, manipulation, MiCA</p></a>
</div>
```

**Acceptance Criteria (Task 9):**
- [ ] d8 CSS class exists and renders correctly
- [ ] CT sidebar links present with correct IDs
- [ ] Hero stats show 32 Lectures, 36 Quizzes
- [ ] CT subsection appears after SC subsection
- [ ] All href paths are correct
- [ ] All sidebar IDs match: sl-ct-mini, sl-ct-intro, sl-ct-pre, sl-ct-main
- [ ] No existing content broken

---

### TASK 10: Verification
**Priority:** CRITICAL | **Depends on:** Tasks 1-9

1. **LaTeX compilation check:**
   - `pdflatex crypto_trading_markets.tex` -- must compile without errors
   - `pdflatex crypto_trading_intro.tex` -- must compile without errors
   - `pdflatex crypto_trading_markets_intro.tex` -- must compile without errors
   - `pdflatex crypto_trading_markets_preclass.tex` -- must compile without errors

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

6. **index.html verification:**
   - Hero stats show correct numbers (32 Lectures, 36 Quizzes)
   - CT sidebar IDs exist
   - All CT lecture/quiz href paths are valid

---

## Commit Strategy

### Commit 1: Core lecture files
```
Add L08 Crypto Trading & Markets lecture bundle (4 LaTeX files)

- crypto_trading_markets.tex: 55-frame technical lecture (5 sections)
- crypto_trading_intro.tex: 10-frame mini-lecture with TikZ comics
- crypto_trading_markets_intro.tex: 6-frame INTRO preview
- crypto_trading_markets_preclass.tex: Pre-class handout (4 activities, glossary)
```

### Commit 2: Quiz files
```
Add CT-1 through CT-4 interactive quizzes for Crypto Trading & Markets

- quiz_ct_part1.html: Market Microstructure (20 questions)
- quiz_ct_part2.html: Trading Strategies (20 questions)
- quiz_ct_part3.html: Portfolio Theory & Risk (20 questions)
- quiz_ct_part4.html: DEX/CEX & Regulation (20 questions)
```

### Commit 3: GitHub Pages integration
```
Add Crypto Trading & Markets section to GitHub Pages landing page

- Add CT subsection with d8 emerald color class
- Add sidebar navigation links
- Update hero stats: 32 Lectures, 36 Quizzes
```

---

## Risk Mitigations

| Risk | Mitigation |
|------|-----------|
| TikZ compilation errors from `\\` in nodes | MANDATE `align=center` on every node containing `\\`. Verify with grep before compile. |
| `\foreach` multi-variable syntax crash | BAN `/` syntax entirely. Use separate `\foreach` loops or manual placement. |
| Parameterized style `#1` conflict | BAN `#1` in all custom TikZ styles. Use fixed styles only. |
| Style name conflict with pgf built-ins | Use unique prefixes (e.g., `ctbox`, `ctnode`) for all custom style names. Avoid: diamond, step, text, signal. |
| lstlisting in non-fragile frame | Every frame with lstlisting MUST have `[fragile]` option. |
| Color mismatch with L04-L07 | Copy color definitions verbatim from stablecoins_cbdcs.tex, character by character. |
| Code frames use Python not Solidity | The 4 code frames use Python-like pseudocode. Keep Solidity lstdef in preamble for consistency but do NOT use Solidity syntax in code frames. Use `language=Python` or plain lstlisting for Python pseudocode. |
| index.html regression | Only add content after SC section. Do not modify any existing HTML elements. |
| pdflatex not available | Use `pdflatex` with `-interaction=nonstopmode` for error detection. Fall back to error-log review. |
| Overly long TikZ lines causing Beamer overflow | Test with 8pt font size. Use `\scriptsize` and `\tiny` aggressively in TikZ nodes. |
| Math formulas in beamer | Use `$...$` for inline math. Ensure all special characters escaped. Test VaR/Sharpe formulas carefully. |

---

## Success Criteria

| Criterion | Verification Method |
|-----------|-------------------|
| All 4 LaTeX files compile cleanly | `pdflatex -interaction=nonstopmode` returns exit 0 |
| Tech lecture has exactly 55 frames | `grep -c "\\begin{frame}" crypto_trading_markets.tex` = 55 |
| Mini-lecture has exactly 10 frames | `grep -c "\\begin{frame}" crypto_trading_intro.tex` = 10 |
| INTRO has exactly 6 frames | `grep -c "\\begin{frame}" crypto_trading_markets_intro.tex` = 6 |
| Exactly 4 fragile frames in tech lecture | `grep -c "\[fragile\]" crypto_trading_markets.tex` = 4 |
| 80 quiz questions total (4 x 20) | JSON question count per file = 20 |
| All quiz explanations non-empty | No `"explanation": ""` in any quiz |
| index.html hero shows 32/36 | Visual inspection of rendered page |
| CT sidebar IDs work | Click each sidebar link, verify scroll |
| No TikZ safety violations | Automated grep checks pass |
| Color palette exact match | Diff color definitions against stablecoins_cbdcs.tex |
| d8 emerald CSS applied correctly | Visual inspection: #10b981 emerald for CT section |

---

## File Path Summary (All Deliverables)

```
D:\Joerg\Research\slides\cryptocurrency\
  lectures\
    crypto_trading_markets.tex           (Task 1 - Tech lecture, 55 frames)
    crypto_trading_intro.tex             (Task 2 - Mini-lecture, 10 frames)
    crypto_trading_markets_intro.tex     (Task 3 - INTRO preview, 6 frames)
    crypto_trading_markets_preclass.tex  (Task 4 - Pre-class handout)
  quiz\
    quiz_ct_part1.html                   (Task 5 - Quiz CT-1, 20 questions)
    quiz_ct_part2.html                   (Task 6 - Quiz CT-2, 20 questions)
    quiz_ct_part3.html                   (Task 7 - Quiz CT-3, 20 questions)
    quiz_ct_part4.html                   (Task 8 - Quiz CT-4, 20 questions)
  index.html                             (Task 9 - GitHub Pages update)
```
