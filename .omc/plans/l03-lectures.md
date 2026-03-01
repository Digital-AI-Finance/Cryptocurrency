# L03 Ethereum & Smart Contracts - Standalone Lectures Plan

## Requirements Summary

Create the full L03 standalone lecture bundle following the established L01/L02 pattern:
- **Mini-lecture**: 10-frame visual introduction with TikZ comics
- **INTRO preview**: 6-frame course preview with charts
- **Pre-class handout**: 2-page article-class discovery activities
- **Technical quantitative lecture**: ~55 frames, 5 sections (same as main deck, expanded)
- **4 quizzes**: 20 questions each, KaTeX-enabled HTML
- **GH Pages update**: Add ES subsection to `index.html`

### User Preferences
- **Sections**: Same 5 sections as main deck (Ethereum vs Bitcoin, Gas & Transactions, Solidity Basics, Deploy & Interact, Summary), expanded with quantitative depth
- **Code focus**: Moderate - key Solidity snippets only, emphasis on architecture diagrams and gas economics charts
- **Frame count**: ~55 frames for technical lecture

## Acceptance Criteria

1. All 6 `.tex` files compile with 0 errors via `pdflatex -interaction=nonstopmode`
2. All PDFs are generated at expected page counts
3. 4 quiz HTML files with exactly 20 questions each
4. `index.html` updated with ES subsection, sidebar links, hero stats
5. Naming convention: `ES` badge (Ethereum & Smart Contracts)
6. All links in `index.html` point to correct file paths

## File Naming Convention

| File | Path |
|------|------|
| Mini-lecture | `lectures/ethereum_intro.tex` → `ethereum_intro.pdf` |
| INTRO preview | `lectures/ethereum_smart_contracts_intro.tex` → `ethereum_smart_contracts_intro.pdf` |
| Pre-class handout | `lectures/ethereum_smart_contracts_preclass.tex` → `ethereum_smart_contracts_preclass.pdf` |
| Technical lecture | `lectures/ethereum_smart_contracts.tex` → `ethereum_smart_contracts.pdf` |
| Quiz 1 | `quiz/quiz_es_part1.html` |
| Quiz 2 | `quiz/quiz_es_part2.html` |
| Quiz 3 | `quiz/quiz_es_part3.html` |
| Quiz 4 | `quiz/quiz_es_part4.html` |

## Tasks

### T1: Mini-Lecture (`lectures/ethereum_intro.tex`, ~10 frames)

**Preamble**: Copy from `lectures/blockchain_intro.tex` (verbose preamble, lines 1-65 pattern) with 12 colors including lightgray/midgray. Add Solidity listings config from `03_ethereum_smart_contracts/03_ethereum_smart_contracts.tex` lines 28-33 (solkeyword, solstring, solcomment, solnumber colors) and lines 58-87 (lstdefinelanguage{Solidity} and lstset).

**Frame-by-Frame Specification:**

| Frame | Title | Content |
|-------|-------|---------|
| 1 | Title slide | "Ethereum & Smart Contracts: A Visual Introduction", plain style |
| 2 | The Programmable Money Problem (Comic 1) | TikZ comic: Alice wants to automate a payment (if condition met, pay Bob). With Bitcoin she can't - needs a "smart" blockchain. 3 panels. |
| 3 | Enter Ethereum (Comic 2) | TikZ comic: Vitalik introduces the EVM - a world computer that runs code. Show contract as a robot that holds money and follows rules. 3 panels. |
| 4 | Bitcoin vs Ethereum Side-by-Side | TikZ comparison table: Bitcoin (digital gold, Script, UTXO, PoW→limited) vs Ethereum (world computer, Solidity/EVM, accounts, PoS). Visual icons for each row. |
| 5 | How Gas Works | TikZ diagram: transaction → EVM execution → gas consumed. Show gas price × gas used = fee. Analogy: car fuel gauge. Color-coded flow. |
| 6 | Smart Contract Lifecycle | TikZ flowchart: Write → Compile → Deploy → Interact → (optionally) Self-destruct. Each step as a colored box with icon. |
| 7 | Your First Smart Contract | Minimal Solidity listing (HelloWorld or SimpleStorage, ~8 lines). Annotated with arrows pointing to key parts: pragma, contract, function, state variable. |
| 8 | Deploying to Ethereum | TikZ diagram: Developer → Remix/Hardhat → Transaction → EVM → Contract gets address. Show the contract living "on-chain" at its address. |
| 9 | Real-World Use Cases | TikZ grid/cards: DeFi (Uniswap), NFTs (ERC-721), DAOs (governance), Stablecoins (USDC). Each with small icon and 1-line description. |
| 10 | Takeaways & What's Next | Summary of 5 key principles with checkmark bullets. TikZ mind map: Ethereum at center → EVM, Gas, Solidity, Deployment, DApps. Bottom note: "Next: ERC-20 token creation". |

### T2: INTRO Preview (`lectures/ethereum_smart_contracts_intro.tex`, ~6 frames)

**Preamble**: Compact preamble from `lectures/cryptography_security.tex` (lines 1-31 pattern). Add Solidity listings config. Add `\usepackage{amssymb}`.

**Frame-by-Frame Specification:**

| Frame | Title | Content |
|-------|-------|---------|
| 1 | Title slide | "Ethereum & Smart Contracts: Course Preview" |
| 2 | Why Ethereum Matters | 3 statistics with pgfplots bar chart: ETH market cap, daily transactions, total contracts deployed. Key message: programmable money. |
| 3 | Course Roadmap | TikZ 5-step roadmap: Ethereum Architecture → Gas Mechanics → Solidity → Deployment → Integration. Numbered boxes with arrows. |
| 4 | EVM Architecture Overview | TikZ diagram: Stack-based virtual machine with memory, storage, calldata. Show opcode execution flow. |
| 5 | Gas Economics at a Glance | pgfplots chart: gas prices over time or gas cost by operation type. Table of common operations and their gas costs. |
| 6 | What You'll Build | TikZ: Show progression from HelloWorld → SimpleStorage → full DApp. "By the end: deploy your own contract on testnet." |

### T3: Pre-Class Handout (`lectures/ethereum_smart_contracts_preclass.tex`)

**Preamble**: Article class from `lectures/cryptography_security_preclass.tex` pattern. Include `\activitybox{}` macro.

**Content structure:**
- Title: "Ethereum & Smart Contracts: Pre-Class Discovery"
- Activity 1: "Explore Ethereum" - visit etherscan.io, find a contract, answer questions about its transactions
- Activity 2: "Gas Price Calculator" - given transaction data, calculate gas costs (gas_price × gas_used)
- Activity 3: "Read a Smart Contract" - given a simple Solidity contract, identify state variables, functions, modifiers
- Activity 4: "Smart Contract vs Traditional" - compare Uber (centralized) vs ride-sharing DAO (decentralized), fill in table
- Glossary box with key terms: EVM, Gas, Wei, Gwei, Solidity, ABI, Bytecode

### T4: Technical Quantitative Lecture (`lectures/ethereum_smart_contracts.tex`, ~55 frames)

**Preamble**: Compact preamble from `lectures/cryptography_security.tex` (lines 1-31). Add Solidity listings from L03 main deck. Add `\usepackage{amssymb}`.

**Section 1: Ethereum vs Bitcoin (~11 frames)**

| Frame | Title | Key Content |
|-------|-------|-------------|
| 1 | Title | `\titlepage` |
| 2 | Roadmap | 5-section overview with TikZ roadmap |
| 3 | Bitcoin vs Ethereum: Design Philosophy | TikZ comparison: Digital Gold vs World Computer. UTXO vs Account model diagram. |
| 4 | Account Model Deep Dive | TikZ: EOA (Externally Owned Account) vs Contract Account. Fields: nonce, balance, storageRoot, codeHash. |
| 5 | State Trie Architecture | TikZ: Modified Merkle Patricia Trie. Show how account states are stored. Root hash in block header. |
| 6 | Ethereum Block Structure | TikZ: Block header fields (parentHash, stateRoot, transactionsRoot, receiptsRoot, gasUsed, gasLimit). Compare with Bitcoin block. |
| 7 | Transaction Types | TikZ table: Type 0 (legacy), Type 1 (EIP-2930), Type 2 (EIP-1559). Fields and differences. |
| 8 | EIP-1559 Fee Market | pgfplots: Base fee adjustment mechanism. Chart showing base fee vs block fullness. Formula: new_base_fee = old × (1 + 1/8 × (gas_used - target)/target). |
| 9 | The Merge: PoW → PoS | TikZ timeline: Frontier → Homestead → Metropolis → The Merge (2022) → Shanghai. Show validator economics. |
| 10 | Validator Economics | pgfplots/table: Staking requirements (32 ETH), expected returns, slashing conditions. APR chart. |
| 11 | Ethereum vs Bitcoin Summary Table | Large comparison table with booktabs: 10+ dimensions (consensus, language, state model, fees, finality, etc.) |

**Section 2: Gas & Transactions (~11 frames)**

| Frame | Title | Key Content |
|-------|-------|-------------|
| 12 | Gas: The Execution Fuel | TikZ: Why gas exists - prevent infinite loops, allocate resources. Analogy diagram. |
| 13 | Gas Cost Table | booktabs table: Common EVM opcodes and their gas costs (ADD=3, MUL=5, SSTORE=20000, etc.). Color-coded by category. |
| 14 | Gas Limit & Block Space | pgfplots: Block gas limit (30M), target (15M). Chart showing gas utilization over blocks. |
| 15 | EIP-1559 Deep Dive | TikZ: Base fee + priority fee. Burning mechanism. Flow diagram: User → Base fee (burned) + Priority fee (validator). |
| 16 | Transaction Lifecycle | TikZ flowchart: Sign → Broadcast → Mempool → Block inclusion → Execution → Receipt. Each step with timing estimates. |
| 17 | Transaction Receipt & Logs | TikZ: Receipt structure (status, gasUsed, logs). Show how events are emitted and indexed. |
| 18 | Estimating Gas Costs | Formula frames: gasEstimate × gasPrice = cost in Wei. Convert Wei → Gwei → ETH → USD. Worked example. |
| 19 | Gas Optimization Patterns | TikZ grid: 6 optimization techniques (storage packing, short-circuiting, batch operations, etc.) with gas savings estimates. |
| 20 | MEV: Maximal Extractable Value | TikZ: Sandwich attacks, frontrunning. Show transaction ordering in mempool. |
| 21 | Layer 2 Gas Savings | pgfplots bar chart: Gas costs on L1 vs Optimism vs Arbitrum vs zkSync. 10-100x savings visualization. |
| 22 | Gas Section Summary | Key formulas and takeaways in colored boxes. |

**Section 3: Solidity Basics (~12 frames)**

| Frame | Title | Key Content |
|-------|-------|-------------|
| 23 | Solidity: The Smart Contract Language | TikZ: Solidity in the ecosystem. Compiler pipeline: .sol → Compiler → ABI + Bytecode. |
| 24 | Contract Structure | Annotated Solidity listing: pragma, imports, contract declaration, state variables, constructor, functions, events, modifiers. |
| 25 | Data Types Overview | TikZ grid: Value types (uint, int, address, bool, bytes) vs Reference types (arrays, mappings, structs). Size/gas for each. |
| 26 | Storage vs Memory vs Calldata | TikZ: Three data locations. Cost comparison table. When to use each. Diagram showing persistence. |
| 27 | Functions & Visibility | TikZ matrix: public/private/internal/external × state-changing/view/pure. Color-coded grid. |
| 28 | Function Modifiers | Solidity listing: require, modifier pattern (onlyOwner), ReentrancyGuard. Before/after execution flow. |
| 29 | Events & Logging | Solidity listing: event declaration, emit syntax. TikZ: How logs are stored (topics + data). Indexed vs non-indexed. |
| 30 | Mappings & Arrays | Solidity examples: mapping(address => uint), dynamic arrays. Storage layout diagram in TikZ (slot calculation via keccak256). |
| 31 | Inheritance & Interfaces | TikZ: Diamond inheritance problem. Solidity: contract B is A. Interface pattern for ERC standards. |
| 32 | Error Handling | Solidity: require vs assert vs revert vs custom errors. Gas refund behavior for each. Comparison table. |
| 33 | Common Design Patterns | TikZ grid: Ownable, Pausable, Proxy (upgradeable), Factory, State Machine. One-line description each. |
| 34 | Solidity Section Summary | Key syntax reference card in colored boxes. |

**Section 4: Deploy & Interact (~12 frames)**

| Frame | Title | Key Content |
|-------|-------|-------------|
| 35 | Development Environment | TikZ: Hardhat vs Foundry vs Remix. Feature comparison. Recommended workflow diagram. |
| 36 | Compilation Process | TikZ flowchart: .sol → solc compiler → ABI (JSON) + Bytecode (hex). Show what each output means. |
| 37 | ABI: The Contract Interface | Annotated ABI JSON snippet. TikZ: How ABI encodes function calls (4-byte selector + encoded params). |
| 38 | Deployment Transaction | TikZ: Special transaction with to=null, data=bytecode+constructor_args. Show how contract gets its address (keccak256(sender, nonce)). |
| 39 | CREATE vs CREATE2 | TikZ comparison: CREATE (nonce-based) vs CREATE2 (salt-based, deterministic). Address derivation formulas. Use cases. |
| 40 | Interacting with Contracts | TikZ: Call vs Transaction. Read (free, no state change) vs Write (costs gas, state change). Web3.js/ethers.js code pattern. |
| 41 | Testing Smart Contracts | Solidity test listing: setUp, test functions. TikZ: Test pyramid (unit → integration → fork tests). Coverage metrics. |
| 42 | Security Vulnerabilities | TikZ grid: Top 5 vulnerabilities (reentrancy, integer overflow, access control, front-running, oracle manipulation). Each with severity badge. |
| 43 | The DAO Hack Case Study | TikZ timeline: Deploy → Exploit → Hard fork. Code snippet showing the reentrancy vulnerability. $60M impact. |
| 44 | Upgradeability Patterns | TikZ: Proxy pattern (Proxy → Implementation). Storage layout preservation. UUPS vs Transparent proxy comparison. |
| 45 | Contract Verification & Etherscan | TikZ: Verified vs unverified contracts. Process: submit source → compiler matches bytecode → green checkmark. |
| 46 | Deploy Section Summary | Key deployment checklist in colored boxes. |

**Section 5: Summary & Integration (~9 frames)**

| Frame | Title | Key Content |
|-------|-------|-------------|
| 47 | Full Stack DApp Architecture | TikZ: Frontend (React) ↔ Ethers.js ↔ Ethereum node (Infura/Alchemy) ↔ Smart Contract ↔ IPFS. Complete stack diagram. |
| 48 | Token Standards Overview | TikZ grid: ERC-20 (fungible), ERC-721 (NFT), ERC-1155 (multi), ERC-4626 (vault). Key functions for each. |
| 49 | DeFi Building Blocks | TikZ: AMM formula (x·y=k), liquidity pools, flash loans. Show how protocols compose (money legos). |
| 50 | Ethereum Scaling Roadmap | TikZ timeline: Sharding → Danksharding → Proto-danksharding (EIP-4844). L2 ecosystem map. |
| 51 | Cross-Chain & Bridges | TikZ: Bridge architecture (lock-and-mint, burn-and-release). Security considerations. |
| 52 | Smart Contract Auditing | TikZ: Audit process flowchart. Tools: Slither, Mythril, Echidna. Cost/time estimates. |
| 53 | Ethereum by the Numbers | pgfplots: Key metrics dashboard - TVL, daily users, gas burned since EIP-1559, validator count. |
| 54 | Career Paths in Ethereum | TikZ: Smart contract dev, auditor, MEV researcher, protocol engineer, DApp developer. Salary ranges. |
| 55 | Course Takeaways | 5 key principles with colored boxes. TikZ mind map: Ethereum → EVM, Gas, Solidity, Deploy, DApps. "Next: Build your own ERC-20 token." |

### T5: Quizzes (4 HTML files, 20 questions each)

Follow exact HTML format from `quiz/quiz_cs_part1.html`: KaTeX-enabled, options as object with "A"/"B"/"C"/"D" keys, correct as letter string, explanation field.

| Quiz | File | Topic Coverage |
|------|------|---------------|
| ES-1 | `quiz/quiz_es_part1.html` | Ethereum Architecture & Account Model (Section 1) |
| ES-2 | `quiz/quiz_es_part2.html` | Gas Mechanics & EIP-1559 (Section 2) |
| ES-3 | `quiz/quiz_es_part3.html` | Solidity Fundamentals (Section 3) |
| ES-4 | `quiz/quiz_es_part4.html` | Deployment, Security & Integration (Sections 4-5) |

### T6: GitHub Pages Update (`index.html`)

1. Add sidebar links inside `<details class="d5">` block:
   - `<a href="#sl-es-mini">Mini-Lecture: Ethereum</a>`
   - `<a href="#sl-es-intro">ES INTRO Preview</a>`
   - `<a href="#sl-es-pre">ES Pre-Class Handout</a>`
   - `<a href="#sl-es-main">ES Technical Lecture</a>`

2. Add ES subsection AFTER CS subsection (before `</section>` of standalone-lectures):
   - Section header: `<span>ES</span><h2>Standalone Lectures: Ethereum & Smart Contracts</h2>`
   - Mini-lecture card → `lectures/ethereum_intro.pdf`
   - INTRO card → `lectures/ethereum_smart_contracts_intro.pdf`
   - PRE card → `lectures/ethereum_smart_contracts_preclass.pdf`
   - 90min card → `lectures/ethereum_smart_contracts.pdf`
   - 4 quiz cards → `quiz/quiz_es_part1-4.html`

3. Update hero stats: `<b>12</b><small>Lectures</small>` → `<b>12</b>`, `<b>16</b><small>Quizzes</small>` → `<b>16</b>`

## Preamble References

- **Mini-lecture preamble**: Based on `lectures/blockchain_intro.tex` (verbose, lines 1-65 pattern)
  - 12 colors including lightgray, midgray
  - Full beamer theme configuration
  - TikZ + pgfplots + amssymb
  - Add Solidity lstdefinelanguage from L03 main deck
  - `\bottomnote{}` macro

- **Technical lecture preamble**: Based on `lectures/cryptography_security.tex` (compact, lines 1-31)
  - 10 colors (no lightgray/midgray)
  - Compact single-line packages
  - TikZ + pgfplots + amssymb
  - Add Solidity lstdefinelanguage from L03 main deck
  - `\bottomnote{}` macro
  - `lstset{style=python}` → change to `lstset` for Solidity

- **INTRO preview preamble**: Same as technical lecture compact preamble

- **Pre-class handout preamble**: Article class from `lectures/cryptography_security_preclass.tex`
  - `\activitybox{}` macro for interactive activities

## Known Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| TikZ `step` style name conflict | Use `procstep` for all custom step styles (learned from L02) |
| `fill=#1` in beamer frames | Never use parameterized TikZ styles with `#1` inside frames |
| `\checkmark` outside math mode | Always use `$\checkmark$` and include `amssymb` package |
| TikZ nodes with `\\` line breaks | Always add `align=center` (or `align=left`) to nodes using `\\` |
| pgfplots arithmetic overflow | Use pre-computed coordinates for extreme values |
| Solidity listings in beamer | Use `fragile` option on frames containing `\lstlisting` or `lstlisting` environment |

## Execution Order

1. **T4** (Technical lecture, sections 1-3, ~34 frames) - executor-high
2. **T1** (Mini-lecture, 10 frames) - executor-high (parallel with T4)
3. **T4 continued** (Technical lecture, sections 4-5, ~21 frames) - executor-high
4. **T2** (INTRO preview, 6 frames) - executor (parallel with T3)
5. **T3** (Pre-class handout) - executor (parallel with T2)
6. **T5** (4 quizzes) - executor (parallel, 2+2)
7. **T6** (index.html update) - executor
8. **Compile all** - build-fixer for any errors
9. **Architect verification** - architect

## Definition of Done

- [ ] All `.tex` files compile with 0 errors
- [ ] Mini-lecture: 10 pages PDF
- [ ] INTRO preview: 6 pages PDF
- [ ] Pre-class handout: PDF generated
- [ ] Technical lecture: ~55 pages PDF
- [ ] 4 quizzes: 20 questions each, valid HTML
- [ ] index.html: ES subsection with all links, updated hero stats
- [ ] All file paths in index.html point to existing files
- [ ] Architect verification: APPROVED
