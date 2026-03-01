# Plan: L12 Tokenomics & Mechanism Design

## Requirements (from interview)
- **Topic:** Tokenomics & Mechanism Design
- **Focus:** Design-oriented — how to design a token economy
- **Code level:** Light (3-4 Solidity snippets)
- **Quiz prefix:** TM
- **GH Pages color:** Indigo #4f46e5 (class d12)
- **Deliverables:** Mini-lecture + Technical lecture + 4 quizzes + GH Pages update
- **No L11 gap handling** — user chose to skip L11

## Files to Create

| File | Type | Description |
|------|------|-------------|
| `lectures/tokenomics_mechanism_intro.tex` | Mini-lecture | 10 frames, TikZ comics, zero code |
| `lectures/tokenomics_mechanism_intro.pdf` | Compiled | pdflatex output |
| `lectures/tokenomics_mechanism.tex` | Technical lecture | ~55 frames, 5 sections, design-oriented |
| `lectures/tokenomics_mechanism.pdf` | Compiled | pdflatex output |
| `quiz/quiz_tm_part1.html` | Quiz | Token Fundamentals & Supply Models (20 Q) |
| `quiz/quiz_tm_part2.html` | Quiz | Bonding Curves & Pricing Mechanisms (20 Q) |
| `quiz/quiz_tm_part3.html` | Quiz | Incentive Design & Game Theory (20 Q) |
| `quiz/quiz_tm_part4.html` | Quiz | Token Design Framework & Case Studies (20 Q) |
| `index.html` | Updated | Add L12 section with d12 indigo styling |

## Implementation Steps

### Step 1: Create Mini-Lecture TEX (10 frames)
Use `lectures/layer2_scaling_intro.tex` as template. Structure:
- Frame 1: Title slide
- Frame 2: What is Tokenomics? (TikZ diagram: token ecosystem)
- Frame 3: Supply Models (fixed, inflationary, deflationary — TikZ comparison)
- Frame 4: Token Utility Types (payment, governance, staking, access)
- Frame 5: Bonding Curves Visualized (TikZ price-vs-supply curve)
- Frame 6: Incentive Alignment (TikZ game theory payoff matrix)
- Frame 7: Token Distribution (TikZ pie chart: team, investors, community)
- Frame 8: Vesting & Unlock Schedules (TikZ timeline)
- Frame 9: Case Study: UNI vs MKR (TikZ comparison boxes)
- Frame 10: Key Takeaways + Questions

### Step 2: Create Technical Lecture TEX (~55 frames, 5 sections)
Use `lectures/layer2_scaling.tex` as template. Structure:

**Section 1: Token Fundamentals & Supply Economics (~11 frames)**
- Token taxonomy, utility vs security, supply models
- Inflation/deflation mechanics, burn mechanisms
- Market cap, fully diluted valuation, circulating supply

**Section 2: Bonding Curves & Pricing Mechanisms (~11 frames)**
- Constant product, linear, polynomial, sigmoid curves
- Mathematical formulations with equations
- Bancor formula, augmented bonding curves

**Section 3: Incentive Design & Game Theory (~11 frames)**
- Nash equilibrium in token systems
- Staking incentives, slashing conditions
- Tragedy of the commons in token governance
- Token sinks and faucets framework

**Section 4: Token Design Framework (~11 frames)**
- Step-by-step token design methodology
- Value capture mechanisms
- Distribution strategies (fair launch, ICO, airdrop)
- Vesting schedules and cliff periods
- 3-4 Solidity snippets: simple vesting, bonding curve, staking

**Section 5: Case Studies & Pitfalls (~11 frames)**
- UNI: governance token design analysis
- MKR/DAI: dual-token stability system
- CRV: vote-escrowed tokenomics (veCRV)
- Common pitfalls: mercenary capital, death spirals, governance attacks

### Step 3: Compile Both TEX to PDF
Run from `lectures/` directory, two passes each:
```bash
cd lectures
pdflatex -interaction=nonstopmode tokenomics_mechanism_intro.tex
pdflatex -interaction=nonstopmode tokenomics_mechanism_intro.tex
pdflatex -interaction=nonstopmode tokenomics_mechanism.tex
pdflatex -interaction=nonstopmode tokenomics_mechanism.tex
```

### Step 4: Create 4 Quiz HTML Files
Use `quiz/quiz_l2_part1.html` as template. Each quiz: 20 questions, multiple-choice (4 options), with explanations. Quiz prefix TM.

### Step 5: Update index.html
Add L12 section after L10 (Layer 2 Scaling) with:
- CSS: `.d12` indigo (#4f46e5) color classes
- Sidebar: L12 navigation entries
- Main: Lecture cards (mini + technical) + quiz grid (4 quizzes)
- Update hero stats count

### Step 6: Git Add, Commit, Push
Stage all new files, commit, push with HTTP/1.1 workaround.

### Step 7: Run Link Checker
Verify all links pass with `python check_links.py --strict`.

## Acceptance Criteria
- [ ] Mini-lecture: 10 frames, compiles to PDF without errors
- [ ] Technical lecture: ~55 frames, 5 sections, 3-4 Solidity snippets, compiles to PDF
- [ ] 4 quiz HTML files with 20 questions each
- [ ] index.html updated with d12 indigo section
- [ ] `check_links.py --strict` passes (0 broken, 0 untracked)
- [ ] Pushed to remote

## Risks
- **LaTeX compilation:** MiKTeX package auto-install may prompt; use `-interaction=nonstopmode`
- **Large commit:** Binary PDFs unavoidable

PLAN_READY: .omc/plans/l12-lectures.md
