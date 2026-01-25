# Cryptocurrency Course Specification

## Project Overview

Complete LaTeX-based educational course on cryptocurrency fundamentals (Blockchain, Bitcoin, Ethereum) with integrated Python code examples, Solidity smart contracts, interactive charts, and GitHub Pages deployment. Structured as 4 lessons × 45 minutes with companion materials and final project scaffold.

**Course Level:** BSc (assumes basic programming knowledge)
**Delivery Format:** PDF presentations + GitHub Pages with runnable code
**Target Audience:** University students learning blockchain and cryptocurrency

---

## PART 1: REQUIREMENTS

### 1.1 Course Content Requirements

#### Lesson Structure (4 total, 45 min each)
- **Lesson 1:** Blockchain Fundamentals & Bitcoin
- **Lesson 2:** Hashing, Cryptographic Signatures & Security
- **Lesson 3:** Ethereum & Smart Contracts
- **Lesson 4:** Web3 Integration & DeFi Basics

**Presentation Constraints:**
- Maximum 30 slides per lesson
- Built with LaTeX Beamer (template: `template_beamer_final.tex`)
- Madrid theme required
- Consistent branding and color palette

#### Code Examples (Required Implementations)
- **Blockchain**: POW simulation, merkle trees, transaction validation
- **Hashing**: SHA-256 implementation, rainbow tables concept
- **Signatures**: ECDSA key generation, message signing, verification
- **Web3**: Simple contract interaction examples

**Smart Contracts** (2 required)
- SimpleStorage contract (basic state management)
- ERC-20 token implementation (inherit from OpenZeppelin)

#### Visualizations & Charts (20 total, 5 per lesson)
- Generated via Python + matplotlib
- 300 DPI resolution for PDF integration
- Include: network diagrams, transaction flows, difficulty curves, price charts
- Chart generation scripts must be reproducible and version-pinned

#### GitHub Pages Deployment
- Static site structure matching `Probability_Statistics` repository pattern
- Hosting code examples with syntax highlighting
- Interactive documentation with rendered charts
- Automated PDF generation via GitHub Actions

#### Final Project Scaffold
- Student template for blockchain project implementation
- Includes boilerplate for:
  - Smart contract template (Solidity)
  - Web3 interaction starter code
  - Testing framework setup
  - README with milestones

### 1.2 Deliverable Constraints

**What is Included:**
- 4 PDF lesson presentations
- All Python source code (examples + chart generation)
- All Solidity smart contract source files
- GitHub Pages static site
- GitHub Actions workflow for automated Pages deployment
- TROUBLESHOOTING.md guide
- test_all.sh validation script
- .gitignore for Python/Node/Solidity environments

**What is NOT Included:**
- Student assessment/exams (user responsibility)
- Model solutions for assignments
- Video recordings or narration
- Interactive online components beyond static GitHub Pages

### 1.3 Software Version Pinning

**Critical (must lock):**
- Python 3.10+ (recommend 3.11)
- Node.js 16+ (recommend 18 LTS)
- Solidity 0.8.20
- web3==6.0.0 (exact pin)
- ecdsa==0.18.0 (exact pin)

**Other Important Pins:**
- matplotlib >=3.5.0 (for 300 DPI support)
- requests >=2.25.0
- python-dotenv >=0.19.0
- eth-keys >=0.5.0
- eth-utils >=2.0.0

**Testing & Linting:**
- pytest >=7.0.0
- black (Python formatter)
- solhint (Solidity linter)

### 1.4 Design Guidelines

**NOT Required (User Discretion):**
- Assessment creation
- Model solutions
- Automated grading systems
- Video narration or lecture recordings

---

## PART 2: TECHNICAL SPECIFICATION

### 2.1 Directory Structure

Root structure mirrors `Probability_Statistics` repository layout:

```
cryptocurrency/
├── .github/
│   └── workflows/
│       └── deploy.yml                 # GitHub Pages deployment workflow
├── .omc/
│   └── autopilot/
│       └── spec.md                    # This file
├── docs/
│   ├── _config.yml                    # Jekyll configuration
│   ├── index.md                       # Homepage
│   ├── assets/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── markdown.css
│   │   └── images/
│   │       └── [chart PNGs]
│   ├── lessons/
│   │   ├── 01_blockchain.md
│   │   ├── 02_cryptography.md
│   │   ├── 03_ethereum.md
│   │   └── 04_web3.md
│   ├── code_examples/
│   │   ├── blockchain/
│   │   ├── hashing/
│   │   ├── signatures/
│   │   └── web3/
│   └── pdfs/
│       ├── Lesson_1_Blockchain.pdf
│       ├── Lesson_2_Cryptography.pdf
│       ├── Lesson_3_Ethereum.pdf
│       └── Lesson_4_Web3.pdf
├── src/
│   ├── lessons/
│   │   ├── 01_blockchain/
│   │   │   ├── lesson_01.tex
│   │   │   └── figures/
│   │   ├── 02_cryptography/
│   │   │   ├── lesson_02.tex
│   │   │   └── figures/
│   │   ├── 03_ethereum/
│   │   │   ├── lesson_03.tex
│   │   │   └── figures/
│   │   └── 04_web3/
│   │       ├── lesson_04.tex
│   │       └── figures/
│   ├── code_examples/
│   │   ├── blockchain/
│   │   │   ├── blockchain.py
│   │   │   ├── merkle_tree.py
│   │   │   └── transaction.py
│   │   ├── hashing/
│   │   │   ├── sha256.py
│   │   │   └── rainbow_table.py
│   │   ├── signatures/
│   │   │   ├── ecdsa_keys.py
│   │   │   └── verify_signature.py
│   │   └── web3/
│   │       ├── connect_web3.py
│   │       ├── read_contract.py
│   │       └── send_transaction.py
│   ├── contracts/
│   │   ├── SimpleStorage.sol
│   │   ├── MyCryptoToken.sol
│   │   └── test/
│   │       ├── SimpleStorage.test.js
│   │       └── MyCryptoToken.test.js
│   ├── charts/
│   │   ├── generate_all_charts.py
│   │   ├── chart_definitions.py
│   │   ├── difficulty_curve.py
│   │   ├── network_diagram.py
│   │   ├── tx_flow.py
│   │   └── price_chart.py
│   ├── templates/
│   │   └── template_beamer_final.tex
│   └── final_project/
│       ├── README.md
│       ├── contracts/
│       │   └── MyContract.sol
│       ├── web3_starter.py
│       ├── tests/
│       │   └── test_contract.js
│       └── MILESTONES.md
├── test_all.sh
├── requirements.txt
├── package.json
├── solc_version.txt
├── .gitignore
├── TROUBLESHOOTING.md
├── README.md
└── LICENSE

```

### 2.2 File Inventory

#### Generated vs Manual

**Manually Created (67 files):**
1. Configuration files (.gitignore, requirements.txt, package.json, etc.)
2. LaTeX lesson files (4 .tex files)
3. Python code examples (12 files across 4 categories)
4. Smart contract source code (2 Solidity files)
5. Test files (2 JavaScript test files)
6. Documentation (README.md, TROUBLESHOOTING.md, etc.)
7. Templates (LaTeX Beamer template + others)
8. GitHub Actions workflow
9. Final project scaffold files

**Generated/Compiled (48 files):**
- 4 × PDF lesson presentations (compiled from LaTeX)
- 20 × PNG chart images (5 per lesson)
- 20 × Thumbnail versions of charts
- 4 × Auxiliary LaTeX files (.aux, .nav, .snm, .out per lesson)

**Total Target: 115 files**

### 2.3 Color Palette (Mandatory)

Used throughout visualizations and presentation branding:

| Name | Hex Value | RGB | Use |
|------|-----------|-----|-----|
| ML Blue | #0066CC | (0, 102, 204) | Primary: headings, accents |
| ML Orange | #FF7F0E | (255, 127, 14) | Secondary: highlights, warnings |
| ML Green | #2CA02C | (44, 160, 44) | Success: positive indicators |
| ML Red | #D62728 | (214, 39, 40) | Alert: errors, negative |
| ML Purple | #3333B2 | (51, 51, 178) | Tertiary: links, details |

**Implementation:**
- Define as Python constants in `chart_definitions.py`
- Use in matplotlib figure generation
- Include in LaTeX preamble as xcolor definitions
- Document in GitHub Pages style guide

### 2.4 LaTeX Configuration

**Template Base:** `template_beamer_final.tex`

**Preamble Requirements:**
```latex
\documentclass[10pt]{beamer}
\usetheme{Madrid}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{hyperref}

% Define color palette
\definecolor{mlblue}{HTML}{0066CC}
\definecolor{mlorange}{HTML}{FF7F0E}
\definecolor{mlgreen}{HTML}{2CA02C}
\definecolor{mlred}{HTML}{D62728}
\definecolor{mlpurple}{HTML}{3333B2}

% Custom beamer colors
\setbeamercolor{structure}{fg=mlblue}
\setbeamercolor{alerted text}{fg=mlred}

% Code listing style for Python/Solidity
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{mlblue},
    commentstyle=\color{mlpurple}\itshape,
    stringstyle=\color{mlgreen},
    breaklines=true,
    showstringspaces=false
}
```

**Per-Lesson Constraints:**
- 30 slides maximum
- Include title, content, and summary slides
- Embed generated chart PNGs (300 DPI)
- Code examples with syntax highlighting
- Consistent footer with lesson number and page count

### 2.5 Chart Generation

**Tool:** Python with matplotlib

**Specifications:**
- Resolution: 300 DPI (300 dots per inch)
- Format: PNG (transparent background)
- Dimensions: 1600×1200 pixels (4:3 aspect ratio)
- Font: Sans-serif (Helvetica preferred)
- Font size: 12pt labels, 14pt titles

**Master Script:** `src/charts/generate_all_charts.py`
- Calls individual chart generation functions
- Saves to `src/lessons/NN_*/figures/`
- Generates both full-size and thumbnail versions (400×300)
- Logs generation time and DPI verification

**Required Charts by Lesson:**

**Lesson 1 (Blockchain):**
1. Bitcoin network topology diagram
2. Block structure visualization
3. Merkle tree example
4. POW difficulty curve
5. Transaction throughput timeline

**Lesson 2 (Cryptography):**
1. ECDSA key generation flowchart
2. Hash function output distribution
3. Signature verification process
4. Security timeline (timeline of attacks/breaks)
5. Key size vs security strength

**Lesson 3 (Ethereum):**
1. Ethereum architecture diagram
2. Smart contract lifecycle
3. Gas estimation chart
4. Account types comparison (EOA vs Contract)
5. State transition diagram

**Lesson 4 (Web3):**
1. Web3.py connection architecture
2. DeFi protocol stack diagram
3. Transaction flow (Web2 vs Web3)
4. Price chart (historical crypto data)
5. Liquidity pool mechanics

### 2.6 GitHub Pages Deployment

**Infrastructure:**
- Static Jekyll site in `/docs` directory
- Automated PDF generation via GitHub Actions
- Charts deployed as PNG assets
- Code examples hosted with syntax highlighting

**GitHub Actions Workflow** (`deploy.yml`):
```yaml
name: Build and Deploy to GitHub Pages

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Python dependencies
        run: |
          pip install -r requirements.txt
      - name: Generate charts
        run: python src/charts/generate_all_charts.py
      - name: Set up LaTeX
        run: |
          sudo apt-get update
          sudo apt-get install -y texlive-latex-base texlive-latex-extra
      - name: Compile LaTeX to PDF
        run: |
          cd src/lessons/01_blockchain && pdflatex -interaction=nonstopmode lesson_01.tex
          cd ../02_cryptography && pdflatex -interaction=nonstopmode lesson_02.tex
          cd ../03_ethereum && pdflatex -interaction=nonstopmode lesson_03.tex
          cd ../04_web3 && pdflatex -interaction=nonstopmode lesson_04.tex
      - name: Copy PDFs to docs
        run: |
          cp src/lessons/01_blockchain/lesson_01.pdf docs/pdfs/Lesson_1_Blockchain.pdf
          cp src/lessons/02_cryptography/lesson_02.pdf docs/pdfs/Lesson_2_Cryptography.pdf
          cp src/lessons/03_ethereum/lesson_03.pdf docs/pdfs/Lesson_3_Ethereum.pdf
          cp src/lessons/04_web3/lesson_04.pdf docs/pdfs/Lesson_4_Web3.pdf
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

### 2.7 Quality Assurance

**test_all.sh Script:**
Validates:
- [ ] All Python files import correctly (no syntax errors)
- [ ] All Solidity files compile with solc 0.8.20
- [ ] All chart generation completes without errors
- [ ] All LaTeX files compile to valid PDFs
- [ ] All code examples run without exceptions
- [ ] No dead links in documentation

**Example Commands:**
```bash
# Python syntax check
python -m py_compile src/code_examples/**/*.py

# Solidity compilation
solc --version  # Check == 0.8.20
solc src/contracts/*.sol --optimize

# LaTeX compilation
pdflatex -interaction=nonstopmode src/lessons/01_blockchain/lesson_01.tex

# Test all.sh orchestration
bash test_all.sh  # Returns 0 if all pass, 1 if any fail
```

### 2.8 Smart Contract Specifications

**SimpleStorage.sol:**
- Stores and retrieves a single uint256 value
- Functions: `set(uint256 _value)`, `get() returns (uint256)`
- Event: `ValueChanged(uint256 newValue)`
- No inheritance required
- Gas estimation: ~45k deployment, ~5k per set

**MyCryptoToken.sol (ERC-20):**
- Inherits from OpenZeppelin ERC20 contract
- Constructor: `MyCryptoToken(uint256 initialSupply)`
- Standard ERC-20 functions: transfer, approve, transferFrom, balanceOf
- Optional: Custom mint/burn functions
- Testing: Transfer, approval, balance checks

**Compilation Target:** Solidity 0.8.20 (pinned)

### 2.9 Documentation Requirements

**README.md (root):**
- Course overview and target audience
- Quick start (clone, install dependencies, generate charts)
- Structure overview (lessons, code examples, contracts)
- GitHub Pages link
- Contributing guidelines
- License

**TROUBLESHOOTING.md:**
- LaTeX installation issues (Windows, macOS, Linux)
- Python/Node version conflicts
- Solidity compiler setup
- Chart generation failures
- PDF rendering issues
- Common import errors
- Solutions for 10+ known issues

**.gitignore:**
- `__pycache__/`, `*.pyc`, `*.pyo`
- `.DS_Store`, `Thumbs.db`
- `node_modules/`, `package-lock.json`
- LaTeX auxiliary files: `*.aux`, `*.log`, `*.nav`, `*.snm`, `*.out`, `*.toc`
- Generated PDFs: `src/lessons/**/*.pdf`
- Solidity build artifacts: `build/`, `dist/`
- Environment: `.env`, `.venv/`, `venv/`
- IDE: `.vscode/`, `.idea/`, `*.swp`

**Final Project README:**
- Student learning objectives
- Project milestones (4-5 checkpoints)
- Acceptance criteria per milestone
- Setup instructions
- Testing guidance
- Submission guidelines

---

## PART 3: IMPLEMENTATION SEQUENCE

### Phase 1: Foundation (Days 1-2)

**Deliverables:**
- [ ] Project directory structure created
- [ ] All configuration files (requirements.txt, package.json, .gitignore, etc.)
- [ ] LaTeX template (template_beamer_final.tex) finalized
- [ ] GitHub Actions workflow file (deploy.yml)
- [ ] Empty .md documentation files

**Dependencies:** None

**Estimated Time:** 4-6 hours

### Phase 2: Code Examples (Days 2-3)

**Deliverables:**
- [ ] All 12 Python code example files
- [ ] Basic imports and function skeletons
- [ ] docstrings and comments for each example
- [ ] All files pass `python -m py_compile`

**Dependencies:** Phase 1 complete

**Estimated Time:** 8-12 hours

### Phase 3: Smart Contracts (Days 3-4)

**Deliverables:**
- [ ] SimpleStorage.sol (complete, tested)
- [ ] MyCryptoToken.sol with ERC-20 inheritance
- [ ] JavaScript test files for both contracts
- [ ] All files pass solc 0.8.20 compilation
- [ ] Test suite runs and passes

**Dependencies:** Phase 1 complete

**Estimated Time:** 6-8 hours

### Phase 4: Chart Generation System (Days 4-5)

**Deliverables:**
- [ ] chart_definitions.py with color palette constants
- [ ] Individual chart generation functions (5 per lesson)
- [ ] generate_all_charts.py orchestration script
- [ ] All 20 PNG files generated at 300 DPI
- [ ] Thumbnail versions created
- [ ] Generation script logs success/failure

**Dependencies:** Phase 1 complete

**Estimated Time:** 10-14 hours

### Phase 5: LaTeX Lessons (Days 5-7)

**Deliverables:**
- [ ] lesson_01.tex (Blockchain, <=30 slides)
- [ ] lesson_02.tex (Cryptography, <=30 slides)
- [ ] lesson_03.tex (Ethereum, <=30 slides)
- [ ] lesson_04.tex (Web3, <=30 slides)
- [ ] All PDFs compile cleanly
- [ ] Charts embedded (300 DPI verified)
- [ ] Code examples formatted with syntax highlighting
- [ ] Consistent branding and color usage

**Dependencies:** Phase 4 complete (charts required)

**Estimated Time:** 16-20 hours

### Phase 6: Documentation (Days 7-8)

**Deliverables:**
- [ ] README.md (complete, with quick start)
- [ ] TROUBLESHOOTING.md (10+ known issues + solutions)
- [ ] Final project scaffold complete
- [ ] docs/index.md (GitHub Pages homepage)
- [ ] All documentation links verified

**Dependencies:** Phases 1-5 complete

**Estimated Time:** 6-8 hours

### Phase 7: GitHub Pages & CI/CD (Days 8-9)

**Deliverables:**
- [ ] Jekyll configuration (_config.yml)
- [ ] GitHub Pages directory structure
- [ ] PDFs copied to docs/pdfs/
- [ ] Charts copied to docs/assets/images/
- [ ] Code examples displayed on website
- [ ] GitHub Actions workflow tested and passing
- [ ] Site publicly accessible

**Dependencies:** Phases 1-6 complete

**Estimated Time:** 4-6 hours

### Phase 8: Quality Assurance (Days 9-10)

**Deliverables:**
- [ ] test_all.sh script complete
- [ ] All Python code runs without errors
- [ ] All LaTeX compiles without warnings
- [ ] All Solidity contracts compile
- [ ] All charts generate successfully
- [ ] GitHub Actions build passes
- [ ] PDF rendering verified in web browser

**Dependencies:** Phases 1-7 complete

**Estimated Time:** 4-6 hours

### Phase 9: Final Integration & Release (Day 10)

**Deliverables:**
- [ ] All files committed to repository
- [ ] GitHub Pages live and functional
- [ ] README includes working links to all resources
- [ ] Final project scaffold tested
- [ ] LICENSE file added
- [ ] Release notes created

**Dependencies:** Phase 8 passing

**Estimated Time:** 2-4 hours

**Total Estimated Duration:** 8-10 days (60-80 hours)

---

## PART 4: SUCCESS CRITERIA

### Technical Verification Checklist

- [ ] All 4 PDF lessons compile without errors
- [ ] All 20 charts generated at 300 DPI
- [ ] All Python code examples import and run
- [ ] All Solidity contracts compile with solc 0.8.20
- [ ] All JavaScript tests pass
- [ ] GitHub Actions workflow completes successfully
- [ ] GitHub Pages site is publicly accessible
- [ ] test_all.sh returns exit code 0

### Content Verification Checklist

- [ ] Lesson 1: Blockchain fundamentals covered (max 30 slides)
- [ ] Lesson 2: Cryptography and signatures explained (max 30 slides)
- [ ] Lesson 3: Ethereum and smart contracts covered (max 30 slides)
- [ ] Lesson 4: Web3 integration demonstrated (max 30 slides)
- [ ] All 5 code examples per lesson implemented
- [ ] All 5 charts per lesson generated and embedded
- [ ] SimpleStorage contract fully implemented and tested
- [ ] ERC-20 token inherits from OpenZeppelin
- [ ] Final project scaffold includes all required components

### Documentation Verification Checklist

- [ ] README.md includes quick start instructions
- [ ] TROUBLESHOOTING.md covers 10+ known issues
- [ ] Final project README includes milestones
- [ ] All links in documentation are valid
- [ ] .gitignore prevents commits of build artifacts
- [ ] GitHub Pages displays all lessons and code examples
- [ ] Version pins documented and enforced

---

## PART 5: DEPENDENCY & PINNED VERSIONS

### Python Environment (requirements.txt)

```
python>=3.10
matplotlib>=3.5.0
requests>=2.25.0
python-dotenv>=0.19.0
web3==6.0.0
ecdsa==0.18.0
eth-keys>=0.5.0
eth-utils>=2.0.0
pytest>=7.0.0
black>=22.0.0
```

### Node.js Environment (package.json)

```json
{
  "engines": {
    "node": ">=16.0.0"
  },
  "devDependencies": {
    "hardhat": "^2.12.0",
    "solidity-coverage": "^0.8.0",
    "@nomicfoundation/hardhat-toolbox": "^2.0.0"
  }
}
```

### Solidity Compiler

- **Required:** solc version 0.8.20 (exactly)
- **Verification:** `solc --version` must output `0.8.20`

---

## PART 6: NOTES & CONSTRAINTS

### Out of Scope

This specification does NOT include:
- Student assessments or exams
- Model solutions for assignments
- Video production or narration
- Interactive tools (games, simulators)
- Live blockchain network deployment (testnet only for examples)
- Mobile applications
- Advanced topics beyond BSc level

### Assumptions

- Users have basic programming knowledge (Python, JavaScript)
- LaTeX is installed on build system
- Node.js and Python development environments available
- GitHub account with Pages enabled
- Internet access for downloading dependencies

### Future Extensions (Post-Release)

- Interactive online quizzes
- Jupyter notebook versions of code examples
- Docker container for reproducible environment
- Video lecture recordings
- Model solutions (in separate private repo)
- Advanced topics (Layer 2, DeFi protocols, NFTs)

---

## PART 7: REFERENCES

**Reference Repository:** `Probability_Statistics` (structure and deployment pattern)

**External Resources:**
- [LaTeX Beamer Documentation](https://ctan.org/pkg/beamer)
- [OpenZeppelin ERC-20 Contract](https://docs.openzeppelin.com/contracts/4.x/erc20)
- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Solidity Documentation](https://docs.soliditylang.org/)

---

## Document Information

- **Version:** 1.0
- **Last Updated:** 2026-01-25
- **Author:** Autopilot Specification System
- **Status:** Ready for Implementation
- **Next Step:** Begin Phase 1 (Foundation)
