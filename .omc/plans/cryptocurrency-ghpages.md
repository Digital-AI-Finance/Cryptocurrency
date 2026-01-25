# Implementation Plan: Cryptocurrency Course GitHub Pages Site

## Context

### Original Request
Build a full GitHub Pages site for the cryptocurrency course at `D:\Joerg\Research\slides\cryptocurrency\`, following the exact style of the Probability_Statistics reference repository.

### Current State Analysis

**Cryptocurrency Repo:**
- 4 lessons with compiled PDFs:
  - L01: Blockchain Fundamentals (`01_blockchain_fundamentals/`)
  - L02: Cryptography & Security (`02_cryptography_security/`)
  - L03: Ethereum & Smart Contracts (`03_ethereum_smart_contracts/`)
  - L04: ERC-20 Token Creation (`04_erc20_token_creation/`)
- 4 lecture notes with compiled PDFs in `notes/` folder
- 20 charts generated (5 per lesson)
- Basic `index.html` exists - needs quiz section upgrade
- Python and Solidity code examples in each lesson's `code/` folder
- Final project in `project/` folder
- **No quiz system yet** (no `quiz/` folder, no `*_quiz.pdf` files)

**Reference Probability_Statistics Structure:**
1. **index.html** - Full featured with:
   - Sticky nav bar with title and links (Lessons, Quizzes, Charts, GitHub)
   - Sidebar navigation with collapsible sections (color-coded by part)
   - Hero section with course title, subtitle, and stats
   - Lessons section with card grid organized by parts
   - Interactive Quizzes section with HTML quiz cards
   - Quiz PDFs section linking to `*_quiz.pdf` in lesson folders
   - Charts section showing chart thumbnails
   - KaTeX formulas
   - Responsive design

2. **quiz/ folder** containing:
   - Individual HTML quiz files (quiz1.html, quiz2.html, etc.)
   - 20 multiple choice questions per quiz
   - Interactive with immediate feedback
   - Progress tracking
   - KaTeX math rendering
   - Three-column card layout

### Research Findings

**Quiz HTML Structure (from Probability_Statistics):**
- Self-contained HTML files with embedded CSS and JavaScript
- Uses KaTeX for math rendering
- Three-column responsive grid for questions
- Question data stored as JSON in `<script>` block
- Features: progress bar, score tracking, immediate feedback, final results
- Question format: `{ id, question, options: {A, B, C, D}, correct, explanation }`

---

## Work Objectives

### Core Objective
Transform the cryptocurrency course website into a fully-featured GitHub Pages site matching the Probability_Statistics reference, with particular focus on adding an interactive quiz system.

### Deliverables

| # | Deliverable | Type | Location |
|---|-------------|------|----------|
| 1 | Updated index.html | File modification | `index.html` |
| 2 | Quiz 1: Blockchain Fundamentals | New file | `quiz/quiz1.html` |
| 3 | Quiz 2: Cryptography & Security | New file | `quiz/quiz2.html` |
| 4 | Quiz 3: Ethereum & Smart Contracts | New file | `quiz/quiz3.html` |
| 5 | Quiz 4: ERC-20 Token Creation | New file | `quiz/quiz4.html` |

### Definition of Done

- [ ] index.html has Quizzes navigation link in nav bar
- [ ] index.html has sidebar links to quizzes
- [ ] index.html has Interactive Quizzes section with quiz cards
- [ ] index.html has Quiz PDFs section (placeholder for future PDF quizzes)
- [ ] 4 quiz HTML files exist in `quiz/` folder
- [ ] Each quiz has 15-20 multiple choice questions
- [ ] Each quiz is self-contained with CSS/JS
- [ ] Quizzes support KaTeX for formulas
- [ ] All navigation links work correctly
- [ ] Site is responsive on mobile

---

## Guardrails

### Must Have
- Match exact visual style from Probability_Statistics reference
- Use same color scheme (Part I: green #22c55e, Part II: orange #f59e0b)
- Quiz questions must be technically accurate for cryptocurrency/blockchain
- All quizzes must have immediate feedback with explanations
- Progress tracking within each quiz
- Three-column responsive layout for quiz cards

### Must NOT Have
- No external JavaScript dependencies beyond KaTeX CDN
- No server-side components (pure static HTML/CSS/JS)
- No modification to existing lesson PDFs
- No removal of existing code examples section
- No changes to chart structure or paths

---

## Task Flow and Dependencies

```
Task 1: Create quiz/ folder
    |
    +---> Task 2: Create quiz1.html (Blockchain Fundamentals)
    |         |
    +---> Task 3: Create quiz2.html (Cryptography & Security)
    |         |
    +---> Task 4: Create quiz3.html (Ethereum & Smart Contracts)
    |         |
    +---> Task 5: Create quiz4.html (ERC-20 Token Creation)
              |
              v
Task 6: Update index.html with quiz section
              |
              v
Task 7: Verification and link testing
```

**Parallelizable:** Tasks 2-5 can run in parallel (independent quiz files)
**Sequential:** Task 6 depends on Tasks 2-5 being complete

---

## Detailed TODOs

### Task 1: Create Quiz Directory Structure
**Priority:** HIGH | **Complexity:** LOW | **Dependencies:** None

**Actions:**
1. Create `quiz/` folder in repository root

**Acceptance Criteria:**
- [ ] `quiz/` directory exists at `D:\Joerg\Research\slides\cryptocurrency\quiz\`

---

### Task 2: Create Quiz 1 - Blockchain Fundamentals
**Priority:** HIGH | **Complexity:** MEDIUM | **Dependencies:** Task 1

**Actions:**
1. Create `quiz/quiz1.html` using Probability_Statistics quiz template
2. Update title to "Quiz 1: Blockchain Fundamentals | Build Your Own Cryptocurrency"
3. Update nav links (Dashboard: `../index.html`, GitHub: Cryptocurrency repo)
4. Create 15-20 multiple choice questions covering:
   - What is blockchain (distributed ledger, immutability)
   - Block structure (header, transactions, hash)
   - Hash functions and their properties
   - Merkle trees
   - Consensus mechanisms (PoW, PoS comparison)
   - Decentralization concepts
   - Genesis block
   - Chain validation
   - Double-spending problem
   - Network nodes and types

**Question Topics (15-20 questions):**
1. Definition of blockchain
2. Properties of a distributed ledger
3. Block header components
4. Previous hash linking
5. Cryptographic hash function properties
6. Merkle tree purpose and structure
7. Proof of Work mechanism
8. Proof of Stake mechanism
9. PoW vs PoS comparison
10. Mining difficulty adjustment
11. Genesis block characteristics
12. Decentralization benefits
13. Double-spending prevention
14. Byzantine fault tolerance
15. Full nodes vs light nodes
16. Chain reorganization
17. Block time and finality
18. 51% attack concept
19. Network propagation
20. Immutability guarantees

**Acceptance Criteria:**
- [ ] File exists at `quiz/quiz1.html`
- [ ] Has 15-20 questions with 4 options each
- [ ] Each question has explanation
- [ ] KaTeX renders properly for any formulas
- [ ] Navigation links work
- [ ] Responsive on mobile

---

### Task 3: Create Quiz 2 - Cryptography & Security
**Priority:** HIGH | **Complexity:** MEDIUM | **Dependencies:** Task 1

**Actions:**
1. Create `quiz/quiz2.html` using same template
2. Update title to "Quiz 2: Cryptography & Security"
3. Create 15-20 questions covering:
   - Hash functions (SHA-256, Keccak)
   - Avalanche effect
   - Public/private key cryptography
   - ECDSA (Elliptic Curve Digital Signature Algorithm)
   - Digital signatures
   - Wallet generation
   - Seed phrases / BIP-39
   - Key derivation
   - Address formats
   - Security best practices

**Question Topics (15-20 questions):**
1. SHA-256 output size
2. Hash function one-way property
3. Collision resistance
4. Avalanche effect definition
5. Symmetric vs asymmetric cryptography
6. Public key derivation
7. Private key security
8. ECDSA curve (secp256k1)
9. Digital signature process
10. Signature verification
11. Wallet types (hot/cold)
12. HD wallet (BIP-32)
13. Mnemonic phrases (BIP-39)
14. Entropy in key generation
15. Checksum verification
16. Address derivation path
17. Multi-signature wallets
18. Hardware wallet security
19. Common attack vectors
20. Best practices for key storage

**Acceptance Criteria:**
- [ ] File exists at `quiz/quiz2.html`
- [ ] Has 15-20 questions with explanations
- [ ] KaTeX works for crypto formulas
- [ ] Same visual style as Quiz 1

---

### Task 4: Create Quiz 3 - Ethereum & Smart Contracts
**Priority:** HIGH | **Complexity:** MEDIUM | **Dependencies:** Task 1

**Actions:**
1. Create `quiz/quiz3.html`
2. Update title to "Quiz 3: Ethereum & Smart Contracts"
3. Create 15-20 questions covering:
   - Ethereum architecture
   - EVM (Ethereum Virtual Machine)
   - Gas mechanics
   - Smart contract basics
   - Solidity fundamentals
   - Contract lifecycle
   - State and storage
   - Events and logs
   - Contract interaction patterns
   - Security considerations

**Question Topics (15-20 questions):**
1. Ethereum vs Bitcoin key difference
2. EVM purpose and function
3. Gas definition
4. Gas price vs gas limit
5. Wei, Gwei, Ether conversions
6. Smart contract definition
7. Contract deployment process
8. Solidity data types
9. Visibility modifiers (public, private, etc.)
10. State variables vs local variables
11. Mapping data structure
12. Events and emit keyword
13. Constructor function
14. Fallback/receive functions
15. msg.sender and msg.value
16. require vs assert vs revert
17. Contract inheritance
18. Interface definition
19. Reentrancy vulnerability
20. Contract upgradeability

**Acceptance Criteria:**
- [ ] File exists at `quiz/quiz3.html`
- [ ] Has 15-20 questions with Solidity code examples where relevant
- [ ] KaTeX renders code blocks properly
- [ ] Questions cover practical smart contract knowledge

---

### Task 5: Create Quiz 4 - ERC-20 Token Creation
**Priority:** HIGH | **Complexity:** MEDIUM | **Dependencies:** Task 1

**Actions:**
1. Create `quiz/quiz4.html`
2. Update title to "Quiz 4: ERC-20 Token Creation"
3. Create 15-20 questions covering:
   - ERC-20 standard
   - Required functions
   - Token metadata
   - Transfer mechanics
   - Approval/allowance pattern
   - Minting and burning
   - Deployment process
   - Testing strategies
   - Token economics
   - Real-world considerations

**Question Topics (15-20 questions):**
1. ERC-20 definition and purpose
2. Required ERC-20 functions list
3. totalSupply() function
4. balanceOf() function
5. transfer() function
6. approve() function
7. allowance() function
8. transferFrom() function
9. Token decimals convention
10. Transfer event requirements
11. Approval event requirements
12. Minting new tokens
13. Burning tokens
14. OpenZeppelin usage
15. Hardhat deployment
16. Testing with ethers.js
17. Testnet deployment
18. Token verification on Etherscan
19. Supply cap implementation
20. Tokenomics considerations

**Acceptance Criteria:**
- [ ] File exists at `quiz/quiz4.html`
- [ ] Has 15-20 questions
- [ ] Includes practical ERC-20 code snippets
- [ ] Covers full token creation workflow

---

### Task 6: Update index.html with Quiz Section
**Priority:** HIGH | **Complexity:** MEDIUM | **Dependencies:** Tasks 2-5

**Actions:**
1. Add "Quizzes" link to nav bar (after Lessons, before Charts)
2. Add quiz links to sidebar navigation under each Part
3. Add new "Interactive Quizzes" section after lessons section:
   - Section header with Q icon (purple #8b5cf6)
   - 4-column grid with quiz cards
   - Each card shows quiz number, title, question count
   - Green gradient background for cards (matching reference)
4. Add "Quiz PDFs" section (placeholder text noting quizzes are interactive only)
5. Update hero stats to show quiz count

**HTML Additions:**

**Nav links addition:**
```html
<a href="#quizzes">Quizzes</a>
```

**Sidebar quiz links under each Part:**
```html
<li><a href="quiz/quiz1.html">Q01 Quiz</a></li>
```

**New Quizzes Section (after lessons, before charts):**
```html
<section class="section" id="quizzes">
<div class="section-head" style="border-color:#8b5cf6"><span style="background:#8b5cf6">Q</span><h2>Interactive Quizzes (60+ questions)</h2></div>
<div class="lgrid" style="grid-template-columns:repeat(4,1fr)">
<!-- Quiz cards matching Probability_Statistics style -->
</div>
</section>
```

**Acceptance Criteria:**
- [ ] Nav bar has Quizzes link
- [ ] Sidebar has quiz links under each Part
- [ ] Interactive Quizzes section visible with 4 quiz cards
- [ ] Cards link to correct quiz files
- [ ] Cards show question count
- [ ] Matches Probability_Statistics visual style

---

### Task 7: Verification and Testing
**Priority:** HIGH | **Complexity:** LOW | **Dependencies:** Task 6

**Actions:**
1. Open index.html in browser
2. Verify all navigation links work
3. Test each quiz file:
   - Questions display correctly
   - Options are clickable
   - Feedback shows on answer
   - Score updates
   - Progress bar works
   - Results screen shows
   - "Try Again" resets quiz
   - "Dashboard" link returns to index
4. Test responsive design on mobile viewport
5. Verify KaTeX renders any formulas

**Acceptance Criteria:**
- [ ] All 4 quiz links from index work
- [ ] All quizzes complete without JavaScript errors
- [ ] Navigation back to dashboard works
- [ ] Mobile responsive layout works
- [ ] No console errors

---

## Commit Strategy

| Commit | Content | Message |
|--------|---------|---------|
| 1 | quiz/ folder + quiz1.html | "Add interactive quiz for Blockchain Fundamentals (L01)" |
| 2 | quiz2.html | "Add interactive quiz for Cryptography & Security (L02)" |
| 3 | quiz3.html | "Add interactive quiz for Ethereum & Smart Contracts (L03)" |
| 4 | quiz4.html | "Add interactive quiz for ERC-20 Token Creation (L04)" |
| 5 | index.html updates | "Update index.html with quizzes section and navigation" |

**Alternative: Single commit**
"Add interactive quiz system with 4 quizzes and update index.html"

---

## Success Criteria

### Functional
- [ ] All 4 interactive quizzes work end-to-end
- [ ] Index page shows quiz section matching reference style
- [ ] All navigation links functional
- [ ] Quizzes track progress and score correctly

### Visual
- [ ] Quiz section matches Probability_Statistics style
- [ ] Color coding consistent (Part I: green, Part II: orange, Quizzes: purple)
- [ ] Responsive design works on mobile
- [ ] Cards have proper hover states

### Content
- [ ] 60+ total quiz questions across 4 quizzes
- [ ] All questions technically accurate for blockchain/crypto
- [ ] Explanations are educational and clear
- [ ] Code snippets properly formatted

---

## Files to Create/Modify

| File | Action | Size Estimate |
|------|--------|---------------|
| `quiz/quiz1.html` | CREATE | ~35KB |
| `quiz/quiz2.html` | CREATE | ~35KB |
| `quiz/quiz3.html` | CREATE | ~35KB |
| `quiz/quiz4.html` | CREATE | ~35KB |
| `index.html` | MODIFY | Add ~2KB |

**Total new content:** ~140KB

---

## Technical Notes

### Quiz HTML Template Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz N: Title | Build Your Own Cryptocurrency</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <style>/* Embedded CSS from reference */</style>
</head>
<body>
    <nav><!-- Navigation --></nav>
    <main class="quiz-container">
        <div class="quiz-header"><!-- Title + Stats --></div>
        <div class="progress-bar-container"><!-- Progress --></div>
        <div class="questions-row" id="questionsRow"></div>
        <div class="results-card" id="resultsCard"><!-- Results --></div>
    </main>
    <script>
        const quizData = { questions: [/* Question array */] };
        // Quiz logic functions
    </script>
</body>
</html>
```

### Color Scheme
- Part I (Foundations): `#22c55e` (green)
- Part II (Development): `#f59e0b` (orange)
- Quizzes: `#8b5cf6` (purple)
- Correct answers: `#22c55e`
- Incorrect answers: `#ef4444`

---

## Execution Notes

This plan is ready for execution. The tasks can be parallelized as follows:

**Parallel execution (Tasks 2-5):** Create all 4 quiz files simultaneously since they are independent.

**Sequential (Task 6):** Update index.html after quizzes are created.

**Final (Task 7):** Verify everything works together.

Estimated total effort: 2-3 hours with parallel execution.
