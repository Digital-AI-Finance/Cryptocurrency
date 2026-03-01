# Plan: L02 Standalone Lectures -- Full Bundle (Cryptography & Security)

## 1. Context

### Original Request
Create a complete standalone lecture ecosystem for Lesson 02 (Cryptography & Security):
1. A 10-slide mini-lecture (Pattern A) -- broad cryptography overview with TikZ comics and pgfplots
2. A full technical quantitative lecture bundle (Pattern B) -- INTRO preview, pre-class handout, 50-70 frame main lecture, and 4-part quiz (80 questions)

All materials added to the GH Pages `index.html` as a new CS subsection within the existing Standalone Lectures section.

### Interview Summary
- Mini-lecture: ALL cryptography topics (broad overview: hash functions, public/private keys, digital signatures, wallets, crypto attacks)
- Technical lecture: NEW STANDALONE (do not modify existing `02_cryptography_security/02_cryptography_security.tex`)
- Format: LaTeX beamer `.tex` files
- Ecosystem: FULL BUNDLE (INTRO preview + pre-class handout + main lecture + 4-part quiz with 80 questions)
- GH Pages: Add CS subsection within existing Standalone Lectures section on `index.html`

### Codebase Facts (from research)
- **Beamer template**: Canonical preamble in `02_cryptography_security/02_cryptography_security.tex` (lines 1-91) -- Madrid theme, 8pt, 169 aspect ratio, 12 colors, `\bottomnote{}` macro, `pythonstyle` listing style
- **L01 compact preamble**: `lectures/blockchain_fundamentals.tex` uses a single-line compact preamble (lines 1-31) -- same theme/colors but more concise; suitable as direct template
- **Color palette**: mlblue (#0066CC), mlpurple (#3333B2), mllavender family (4 levels), mlorange, mlgreen, mlred, mlgray, lightgray, midgray. **Note:** T2/T3 use the full 12-color palette (copied from `blockchain_intro.tex`). T5 uses the 10-color compact palette from `blockchain_fundamentals.tex` which omits `lightgray` and `midgray` -- this is sufficient since those two colors are not used in beamer content frames.
- **Theme config**: palette primary/secondary/tertiary/quaternary, structure, frametitle, block title/body
- **Custom macro**: `\bottomnote{}` -- vfill + rule + footnotesize bold text (beamer only, NOT available in article class)
- **Listings style**: `python` style defined with course colors
- **Existing L02**: 32 frames (`\begin{frame}` blocks), 5 sections (Hash Functions, Public Key Cryptography, Digital Signatures, Cryptocurrency Wallets, Summary). Uses `\includegraphics` for 5 PNG/PDF diagram references, 3 Python code demos. Content is introductory-level -- the new technical lecture MUST go deeper with formal mathematics, additional topics (symmetric crypto, ZK proofs, post-quantum), and all-TikZ/pgfplots visuals.
- **Quiz format**: HTML with KaTeX, CSS variables matching course colors, nav bar with mlpurple-to-mlblue gradient, progress bar, stat badges, `loadNextQuestions()` pagination in groups of 3, 20 questions per quiz, 4 options (A/B/C/D), correct answer + explanation
- **GH Pages**: `index.html` (437 lines) with sidebar nav, hero stats, lesson/notebook/quiz/notes/resources sections. Standalone Lectures section (d5 class, rose #e11d48 color) already exists with BF subsection -- CS subsection must be added within same section.
- **`lectures/` directory**: Already exists with 4 L01 files (blockchain_intro.tex, blockchain_fundamentals_intro.tex, blockchain_fundamentals_preclass.tex, blockchain_fundamentals.tex)
- **Existing quizzes**: `quiz/quiz1.html` through `quiz/quiz4.html` (original), `quiz/quiz_bf_part1.html` through `quiz_bf_part4.html` (L01 standalone)
- **Article-class preamble**: Used for pre-class handout (see `lectures/blockchain_fundamentals_preclass.tex`), includes `\activitybox` macro, fancyhdr header format, compact list spacing

---

## 2. Work Objectives

### Core Objective
Produce a complete standalone lecture ecosystem for Cryptography & Security that complements (but does not duplicate) the existing L02 slide deck, following the exact patterns established by the L01 standalone lectures.

### Deliverables

| ID | File | Type | Description |
|----|------|------|-------------|
| D1 | `lectures/cryptography_intro.tex` | Mini-lecture | 10-slide beamer with TikZ comics + pgfplots chart |
| D2 | `lectures/cryptography_security_intro.tex` | INTRO preview | 6-slide preview deck with TikZ + pgfplots |
| D3 | `lectures/cryptography_security_preclass.tex` | Pre-class handout | 2-page article-class discovery activities |
| D4 | `lectures/cryptography_security.tex` | Technical lecture | 50-70 frame lecture with 15+ TikZ diagrams, 8 sections |
| D5a | `quiz/quiz_cs_part1.html` | Quiz Part 1 | Hash Functions & Symmetric Crypto (20 questions) |
| D5b | `quiz/quiz_cs_part2.html` | Quiz Part 2 | Asymmetric Crypto & Digital Signatures (20 questions) |
| D5c | `quiz/quiz_cs_part3.html` | Quiz Part 3 | Key Management & Wallets (20 questions) |
| D5d | `quiz/quiz_cs_part4.html` | Quiz Part 4 | Protocols, Attacks & Post-Quantum (20 questions) |
| D6 | `index.html` (modified) | GH Pages | New CS subsection within Standalone Lectures section |

### Definition of Done
1. All 9 files exist in the correct locations (4 new `.tex`, 4 new `.html`, 1 modified `.html`)
2. All `.tex` files compile with `pdflatex` without errors (user verifies)
3. All beamer `.tex` files use the exact same beamer preamble (Madrid, same colors, same `\bottomnote{}`)
4. Mini-lecture has exactly 10 frames with at least 2 TikZ comic strip elements and 1 pgfplots chart
5. INTRO preview has exactly 6 frames with 2+ TikZ and 3+ pgfplots
6. Pre-class handout is article class, 2 pages, with 5 discovery activities
7. Technical lecture has 50-70 frames, 8 sections, 15+ TikZ diagrams, 5+ pgfplots charts
8. Each quiz has exactly 20 questions in the exact HTML/CSS/JS format as `quiz/quiz1.html`
9. `index.html` has a new CS subsection within the Standalone Lectures section
10. No existing files modified (except `index.html`)
11. Content in D4 is deeper, more quantitative, and more TikZ-heavy than existing L02 (covers topics NOT in existing L02: symmetric crypto, ZK proofs, sponge construction, post-quantum, signature aggregation, secret sharing)

---

## 3. Guardrails

### MUST HAVE
- Identical beamer preamble to L01 standalone lectures (colors, theme, `\bottomnote{}`)
- `\usepackage{tikz}` and `\usepackage{pgfplots}` added where needed
- TikZ libraries: `arrows.meta`, `positioning`, `shapes.geometric`, `shapes.symbols`, `calc`, `decorations.pathmorphing`
- For T5 technical lecture additionally: `chains`, `automata` libraries
- pgfplots `compat=1.18`
- Quiz HTML/CSS/JS structure identical to `quiz/quiz1.html`
- Quiz nav links point to `../index.html` for Dashboard
- All content technically accurate and appropriate for BSc level
- Mathematical formulations in the technical lecture (hash properties formal, elliptic curve math, birthday bound, ZK proof structure)
- Author: Prof. Dr. Joerg Osterrieder
- Institute: University Lecture Series
- Pre-class handout uses article class with `\activitybox{}` macro (same as L01 pre-class)
- All TikZ/pgfplots use course colors (mlblue, mlpurple, mlorange, mlgreen, mlred)

### MUST NOT HAVE
- Any modifications to existing `02_cryptography_security/02_cryptography_security.tex`
- Any modifications to existing `quiz/quiz1.html` through `quiz/quiz4.html`
- Any modifications to existing L01 standalone files (`lectures/blockchain_*.tex`, `quiz/quiz_bf_*.html`)
- External image dependencies (all visuals via TikZ/pgfplots inline)
- Content that merely duplicates the existing L02 slides
- Hardcoded dates (use `\today`)
- Non-compiling LaTeX (no undefined commands, missing packages)
- Use of `\bottomnote{}` in article-class documents (T4)
- Use of `\includegraphics` (all diagrams must be TikZ/pgfplots)

---

## 4. Task Flow

### Dependency Graph

```
T1 (verify lectures/ dir exists)
  |
  +---> T2 (mini-lecture D1) --------+
  |                                   |
  +---> T3 (INTRO preview D2) -------+
  |                                   |
  +---> T4 (pre-class handout D3) ---+---> T8 (index.html update D6)
  |                                   |
  +---> T5 (technical lecture D4) ---+
                                      |
T6 (quiz part 1-2, D5a+D5b) --------+
T7 (quiz part 3-4, D5c+D5d) --------+
```

**Parallelizable groups:**
- Group A: T2 + T3 + T4 (independent LaTeX files)
- Group B: T6 + T7 (independent quiz HTML files)
- T5 runs alone (largest deliverable, 50-70 frames)
- T8 runs last (depends on all file paths being finalized)

---

## 5. Detailed Tasks

### T1: Verify `lectures/` Directory Exists
**Priority:** P0 (prerequisite)
**Effort:** Trivial
**Action:** `ls lectures/` to confirm directory exists (it already does from L01). No action needed unless missing.
**Acceptance Criteria:**
- [ ] Directory `D:/Joerg/Research/slides/cryptocurrency/lectures/` exists and contains L01 files

---

### T2: Mini-Lecture -- `lectures/cryptography_intro.tex` (D1)
**Priority:** P1
**Effort:** Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/cryptography_intro.tex`

**Specification:**
Exactly 10 frames. Same beamer preamble as L01 mini-lecture (`lectures/blockchain_intro.tex` lines 1-65) with TikZ/pgfplots packages. Title: "Cryptography for Blockchain: A Visual Introduction", Subtitle: "Standalone Mini-Lecture".

**Frame-by-frame content:**

| Frame | Title | Content | Visual |
|-------|-------|---------|--------|
| 1 | Title slide | "Cryptography for Blockchain: A Visual Introduction" + hook: "The math that makes trustless money possible" | Plain title layout (use `\titlepage` inside centered layout, same as `blockchain_intro.tex` frame 1) |
| 2 | The Secret Message Problem | TikZ comic: Alice wants to send a secret message to Bob, but Eve is eavesdropping on the channel. Speech bubbles show the dilemma. | TikZ comic (3 stick figures: Alice on left, Bob on right, Eve in middle with ear to channel. Speech bubbles. Use mlblue for Alice, mlgreen for Bob, mlred for Eve) |
| 3 | One-Way Functions: The Meat Grinder | Core concept: Hash functions turn any input into a fixed-size fingerprint, but you cannot reverse the process. SHA-256 always produces 256 bits. | TikZ comic (meat grinder diagram: input text feeds into a grinder shape, hash output comes out. Arrow showing "easy" direction, crossed arrow showing "impossible" reverse. Include example: "Hello" -> "2cf24dba...") |
| 4 | The Avalanche Effect | Tiny input change causes completely different output. "Hello" vs "hello" produce entirely different hashes. ~50% of bits flip. | TikZ diagram: two parallel paths, input1 and input2 differ by 1 char, outputs shown as colored bit strips with highlighted differences. Include formula: Hamming distance ~ n/2 |
| 5 | Public & Private Keys | Lock and key analogy for asymmetric crypto. Public key = address anyone can send to. Private key = only you can unlock. Mathematical relationship: Q = d x G. | TikZ diagram: padlock (public key) and physical key (private key). Arrow from private to public labeled "easy (ECC multiply)". Crossed arrow from public to private labeled "infeasible (discrete log)". |
| 6 | Digital Signatures: Proving Ownership | Signing flow: Alice signs with private key, anyone verifies with public key. Three properties: authenticity, integrity, non-repudiation. | TikZ flow diagram: Message -> Hash -> Sign(private key) -> Signature. Verification path: Message + Signature + Public Key -> Valid/Invalid. Use mlgreen for valid checkmark, mlred for invalid X. |
| 7 | Wallet Architecture: From Seed to Address | Key derivation tree: random entropy -> mnemonic seed (12-24 words) -> master key -> child keys -> addresses. BIP-32/39/44 standards. | TikZ tree diagram: seed at root, branching to master key, then child keys at leaves. Each level labeled with the derivation step. Use mlpurple for seed, mlblue for keys, mlgreen for addresses. |
| 8 | Real-World Attacks on Cryptography | Three attack categories: brute force (try all keys), birthday attack (collision finding), side-channel (timing, power analysis). Visual showing attacker strategies. | TikZ diagram: three panels side-by-side. Panel 1: brute force as combinatorial explosion (2^256 keys). Panel 2: birthday attack as party collision analogy (23 people = 50% match). Panel 3: side-channel as spy measuring timing/power. |
| 9 | Crypto by the Numbers | Key size vs security strength comparison. 128-bit, 192-bit, 256-bit security levels. Comparison: AES-128, ECDSA-256, RSA-3072 all provide ~128-bit security. | pgfplots grouped bar chart: x-axis = security level (80, 128, 192, 256 bits), y-axis = key size in bits. Three bar groups: symmetric (AES), ECC, RSA. Shows ECC efficiency vs RSA bloat. |
| 10 | Takeaways & Crypto Principles | Checklist of cryptographic principles for blockchain: (1) Never reuse keys, (2) Verify before trusting, (3) Use standard algorithms, (4) Protect private keys, (5) Assume quantum is coming. | Structured checklist layout with colored checkmarks. Summary box with "Cryptography = the foundation of trustless systems" |

**Preamble template:**
Copy `lectures/blockchain_intro.tex` lines 1-65 (beamer preamble WITHOUT listings). This includes: documentclass, Madrid theme, colors, beamercolor settings, navigation/itemize/margin config, `\bottomnote{}` macro, TikZ/pgfplots with libraries. Change `\title`, `\subtitle`, `\author`, `\institute`, `\date` to match L02.

**Acceptance Criteria:**
- [ ] Exactly 10 `\begin{frame}` ... `\end{frame}` blocks
- [ ] At least 2 frames with TikZ comic strip elements (stick figures, speech bubbles) -- frames 2 and 3
- [ ] At least 1 frame with a pgfplots chart (axis environment) -- frame 9
- [ ] Uses `\bottomnote{}` on content frames (frames 2-10)
- [ ] Title: "Cryptography for Blockchain: A Visual Introduction"
- [ ] Subtitle: "Standalone Mini-Lecture"
- [ ] Author: Prof. Dr. Joerg Osterrieder
- [ ] Institute: University Lecture Series
- [ ] All TikZ diagrams use course colors (mlblue, mlpurple, mlorange, mlgreen, mlred)
- [ ] No `\includegraphics` calls -- all visuals are TikZ/pgfplots
- [ ] Compiles with pdflatex (no external images required)

---

### T3: INTRO Preview -- `lectures/cryptography_security_intro.tex` (D2)
**Priority:** P1
**Effort:** Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/cryptography_security_intro.tex`

**Specification:**
Exactly 6 frames. Preview deck teasing the full technical lecture. Mix of TikZ and pgfplots. Title: "Cryptography & Security: Course Preview", Subtitle: "INTRO Preview -- What You Will Learn".

**Frame-by-frame content:**

| Frame | Title | Visual Type | Content |
|-------|-------|-------------|---------|
| 1 | Title | -- | "Cryptography & Security: Course Preview" + subtitle "INTRO Preview -- What You Will Learn" |
| 2 | Hash Function Anatomy | TikZ | Detailed diagram: input message -> padding -> block splitting -> iterative compression (Merkle-Damgard) -> final digest. Show SHA-256 internal structure with 512-bit blocks, 64 rounds label, 256-bit state. Use mlblue for data flow, mlpurple for operations. |
| 3 | ECDSA Signature Flow | TikZ | Complete ECDSA signing and verification flow: (1) message -> hash(m) = e, (2) random k -> point R = kG, (3) r = R.x mod n, (4) s = k^-1(e + dr) mod n, (5) output (r,s). Verification: compute u1, u2, check point. Use color-coded boxes for each step. |
| 4 | Key Sizes vs Security Levels | pgfplots | Grouped bar chart comparing key sizes needed for equivalent security: x-axis = security level (80, 128, 192, 256 bits), bar groups = Symmetric (AES), ECC (NIST curves), RSA. Data: 80-bit: AES-80/ECC-160/RSA-1024; 128-bit: AES-128/ECC-256/RSA-3072; 192-bit: AES-192/ECC-384/RSA-7680; 256-bit: AES-256/ECC-521/RSA-15360. |
| 5 | Algorithm Performance Comparison | pgfplots | Bar chart: encryption/signing speed (operations/second) for RSA-2048, ECDSA-P256, Ed25519, AES-256-GCM. Show that symmetric is orders of magnitude faster. Log scale y-axis. Approximate values: AES ~1M ops/s, Ed25519 ~70K, ECDSA ~20K, RSA-sign ~1K. |
| 6 | Crypto Adoption Timeline | pgfplots | Line chart: HTTPS adoption rate over years (2010-2025). Data points: 2010: ~20%, 2013: ~30%, 2015: ~40%, 2017: ~55%, 2019: ~80%, 2021: ~90%, 2023: ~95%, 2025: ~97%. Shows accelerating adoption of cryptographic protocols. Add secondary line for blockchain wallet growth (millions): 2013: 0.5M, 2015: 5M, 2017: 20M, 2019: 45M, 2021: 80M, 2023: 90M, 2025: 100M. |

**Preamble:** Same as T2 (copy `lectures/blockchain_intro.tex` lines 1-65, change title/subtitle).

**Acceptance Criteria:**
- [ ] Exactly 6 `\begin{frame}` ... `\end{frame}` blocks
- [ ] At least 2 TikZ diagrams (frames 2, 3)
- [ ] At least 3 pgfplots charts (frames 4, 5, 6)
- [ ] Uses identical beamer preamble + TikZ/pgfplots packages
- [ ] Title: "Cryptography & Security: Course Preview"
- [ ] Subtitle: "INTRO Preview -- What You Will Learn"
- [ ] Author: Prof. Dr. Joerg Osterrieder
- [ ] No `\includegraphics` calls
- [ ] Compiles with pdflatex

---

### T4: Pre-Class Handout -- `lectures/cryptography_security_preclass.tex` (D3)
**Priority:** P1
**Effort:** Low-Medium
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/cryptography_security_preclass.tex`

**Specification:**
This is NOT a beamer document. It is an `article` class document, 2 pages, designed as a pre-class discovery handout. Follow `lectures/blockchain_fundamentals_preclass.tex` exactly for structure.

**Document class:** `\documentclass[11pt,a4paper]{article}`

**Preamble template (copy from `lectures/blockchain_fundamentals_preclass.tex` lines 1-50):**
```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=2cm]{geometry}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{hyperref}

% Course color palette (same 12 colors)
\definecolor{mlblue}{HTML}{0066CC}
... (all 12 colors) ...

% Section heading colors (same as L01 preclass)
\titleformat{\section}{...}
\titleformat{\subsection}{...}
\titlespacing*{...}

% Header/footer -- change to L02 content
\fancyhead[L]{\small\color{mlpurple}\textbf{Cryptography \& Security} \textcolor{mlgray}{|} Lesson 02 \textcolor{mlgray}{|} Pre-Class Discovery Handout}
\fancyhead[R]{\small\color{mlgray}Prof.\ Dr.\ Joerg Osterrieder}

% Compact list spacing (same)
% \activitybox macro (same)
```

**IMPORTANT:** The `\bottomnote{}` macro is NOT available in article class. Do not use it. Use the `\activitybox{}` macro for activities (same as L01 preclass).

**Page 1: "How Does Cryptography Protect Your Money?"**
- Activity 1: "The Caesar Cipher" -- Students encrypt "BLOCKCHAIN" using a shift of 3 (-> "EORFNFKDLQ"). Then try to break a classmate's cipher. Discover why simple ciphers are insecure. Connect to Kerckhoffs's principle: security must reside in the key, not the algorithm.
- Activity 2: "Hash It Yourself" -- Given 3 short strings ("cat", "Cat", "cats"), students compute a simple hash: sum of ASCII values mod 256. Observe that tiny changes (capitalization, extra letter) produce different results. Relate to the avalanche effect in SHA-256.
- Activity 3: "The Envelope Analogy" -- Paper exercise: Write a secret message, put it in an "envelope" (fold paper). Give your public "address" (your name) to a classmate. They can send you sealed envelopes but cannot read them. Only you can open. Connect to asymmetric cryptography.

**Page 2: "Why Can't You Fake a Signature?"**
- Activity 4: "Sign and Verify" -- Students write a message, sign it with their unique mark. Pass to neighbor. Neighbor tries to verify it's authentic. Then try to forge a classmate's signature. Discuss why digital signatures are unforgeable (mathematical binding vs physical copying). Connect to ECDSA.
- Activity 5: "The Key Management Challenge" -- Scenario: You have 5 cryptocurrency wallets. How many private keys do you need? What if you lose one? What if you write them down and someone finds the paper? Discuss HD wallets and seed phrases as solutions. Connect to BIP-32/39.
- Reflection Questions (3 open-ended):
  1. Why is it important that hash functions are one-way? What would happen if you could reverse SHA-256?
  2. If quantum computers could break current encryption, what would happen to Bitcoin? What solutions exist?
  3. Why do we say "not your keys, not your coins"? What are the trade-offs of self-custody vs exchange custody?

**Acceptance Criteria:**
- [ ] Uses `article` class, NOT beamer
- [ ] Exactly 2 pages when compiled
- [ ] Uses same course colors (mlblue, mlpurple, etc.)
- [ ] Contains 5 discovery activities using `\activitybox` macro
- [ ] Contains 3 reflection questions
- [ ] Header: "Cryptography & Security | Lesson 02 | Pre-Class Discovery Handout"
- [ ] Same preamble structure as `lectures/blockchain_fundamentals_preclass.tex`
- [ ] Does NOT use `\bottomnote{}` (not available in article class)
- [ ] Compiles with pdflatex

---

### T5: Technical Quantitative Lecture -- `lectures/cryptography_security.tex` (D4)
**Priority:** P0 (largest deliverable)
**Effort:** High
**Depends on:** T1
**File:** `D:/Joerg/Research/slides/cryptocurrency/lectures/cryptography_security.tex`

**Specification:**
50-70 frames, 8 sections, 15+ TikZ diagrams, 5+ pgfplots charts, mathematical formulations, quantitative focus. Content must be DIFFERENT and DEEPER than existing L02. Must cover topics NOT in the existing L02: symmetric cryptography, sponge construction, Schnorr signatures, signature aggregation, zero-knowledge proofs, commitment schemes, secret sharing, post-quantum candidates.

**Preamble:**
Copy `lectures/blockchain_fundamentals.tex` lines 1-36 verbatim (compact beamer preamble with colors, listings style, TikZ/pgfplots with full library set including `chains` and `automata`). Change `\title`, `\subtitle` to L02.

```latex
\title{Cryptography \& Security: A Quantitative Deep Dive}
\subtitle{Standalone Technical Lecture}
\author{Prof.~Dr.~Joerg Osterrieder}
\institute{University Lecture Series}
\date{\today}
```

**Section Plan (8 sections, ~55 frames):**

#### Section 1: Introduction & Motivation (5 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 1 | Title slide | "Cryptography & Security: A Quantitative Deep Dive" | -- (titlepage) |
| 2 | History of Cryptography Timeline | Timeline: Scytale (700 BC) -> Caesar cipher -> Enigma (1940s) -> DES (1977) -> RSA (1978) -> AES (2001) -> Bitcoin/ECDSA (2009) -> Post-quantum (2024) | TikZ timeline diagram (same pattern as L01 blockchain_fundamentals.tex frame 2) |
| 3 | Kerckhoffs's Principle | "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge." Formal: security rests in key space, not algorithm secrecy. Contrast with "security through obscurity." | TikZ: two paths -- "obscurity" (lock with hidden mechanism, mlred X) vs "Kerckhoffs" (published algorithm + secret key, mlgreen checkmark) |
| 4 | Threat Model & Attack Taxonomy | Formal classification: passive vs active attacks, known-plaintext vs chosen-plaintext vs chosen-ciphertext. CIA triad: Confidentiality, Integrity, Availability. | TikZ: attack taxonomy tree diagram with 3 levels |
| 5 | Course Roadmap | 8-section overview with icons for each section | -- (structured itemize) |

#### Section 2: Hash Functions Deep Dive (7 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 6 | Hash Function Formal Properties | Three properties with formal definitions: (1) Preimage resistance: given h, infeasible to find m s.t. H(m)=h. (2) Second preimage: given m1, infeasible to find m2 != m1 s.t. H(m1)=H(m2). (3) Collision resistance: infeasible to find any m1 != m2 s.t. H(m1)=H(m2). Hierarchy: collision resistance => second preimage resistance. | -- (formal math definitions) |
| 7 | Merkle-Damgard Construction | Internal structure: message padding (append 1, zeros, length), split into 512-bit blocks, iterative compression: state_0 = IV, state_i = f(state_{i-1}, block_i), digest = finalize(state_n). SHA-256 uses this structure. | TikZ: pipeline diagram showing IV -> f(block1) -> state1 -> f(block2) -> ... -> digest. Boxes for compression function, arrows for data flow. |
| 8 | SHA-256 Internals | 64 rounds per block. Operations: Ch, Maj, Sigma0, Sigma1, sigma0, sigma1. Message schedule: W_0..W_63 expanded from 16 input words. State: 8 working variables a-h. Round function detail. | TikZ: round function diagram showing state variables a-h, additions, rotations, Ch/Maj functions. Compact but accurate. |
| 9 | Sponge Construction (Keccak/SHA-3) | Alternative to Merkle-Damgard. State = rate + capacity. Absorb phase: XOR input blocks into rate portion, apply permutation. Squeeze phase: extract output blocks from rate portion. Keccak uses 1600-bit state (r=1088, c=512 for SHA3-256). | TikZ: sponge diagram showing absorb/squeeze phases with state split into rate (r) and capacity (c) portions. Arrows for permutation function f. |
| 10 | Birthday Bound & Collision Probability | Birthday paradox: P(collision among n items from space of size N) approx 1 - e^{-n^2/(2N)}. For SHA-256: N = 2^256, need ~2^128 hashes for 50% collision probability. Birthday attack complexity: O(2^{n/2}) vs brute force O(2^n). | pgfplots: collision probability curve. x-axis = number of hashes (log scale), y-axis = P(collision). Mark the 50% point at 2^128. |
| 11 | Hash Function Comparison | Comparison table + chart: SHA-256 vs SHA-3 vs BLAKE3 vs RIPEMD-160. Properties: output size, block size, rounds, speed (MB/s), quantum resistance. BLAKE3 fastest, SHA-3 most different construction. | pgfplots: horizontal bar chart comparing throughput (MB/s) of SHA-256 (~250), SHA-3-256 (~200), BLAKE3 (~4000), RIPEMD-160 (~350) on typical hardware. |
| 12 | Hash Applications in Blockchain | Four applications with formal notation: (1) Block linking: H(Block_i) stored in Block_{i+1}, (2) Merkle root: M(txs) = H(H(tx1||tx2) || H(tx3||tx4)), (3) PoW puzzle: find nonce s.t. H(header||nonce) < target, (4) Address derivation: addr = RIPEMD160(SHA256(pubkey)). | TikZ: four-panel diagram, one panel per application, showing the hash flow for each |

#### Section 3: Symmetric Cryptography (5 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 13 | Symmetric Encryption Formal | Definition: E_k(m) = c, D_k(c) = m, same key k for both. Required properties: correctness (D_k(E_k(m)) = m for all m), security (ciphertext reveals nothing about plaintext without k). Key space: |K| must be large enough to resist brute force. | -- (formal definitions with math) |
| 14 | AES Overview | Advanced Encryption Standard. Block size: 128 bits. Key sizes: 128/192/256 bits (10/12/14 rounds). Operations per round: SubBytes (S-box), ShiftRows, MixColumns, AddRoundKey. State represented as 4x4 byte matrix. | TikZ: AES round diagram showing 4x4 state matrix flowing through SubBytes -> ShiftRows -> MixColumns -> AddRoundKey, with key schedule feeding in. |
| 15 | Block Cipher Modes | ECB (insecure: same plaintext -> same ciphertext), CBC (chained, needs IV), CTR (counter mode, parallelizable), GCM (authenticated encryption). Show ECB penguin problem. | TikZ: four small diagrams, one per mode. ECB shows identical blocks mapping to identical ciphertext. CBC shows chaining with XOR. CTR shows counter + encrypt + XOR. |
| 16 | The Key Exchange Problem | Alice and Bob need a shared key but have no secure channel. Diffie-Hellman: g^a mod p shared publicly, compute g^{ab} mod p. Computational Diffie-Hellman assumption. | TikZ: Diffie-Hellman exchange diagram: Alice picks a, sends g^a. Bob picks b, sends g^b. Both compute g^{ab}. Eve sees g^a, g^b but cannot compute g^{ab}. Color-coded arrows. |
| 17 | Symmetric vs Asymmetric Trade-offs | Performance comparison: AES ~1 Gbps vs RSA ~10 Kbps for encryption. Hybrid approach: use asymmetric to exchange symmetric key, then symmetric for data. TLS handshake as real-world example. | pgfplots: log-scale bar chart comparing throughput: AES-256-GCM (~1000 MB/s), ChaCha20 (~900 MB/s), RSA-2048-encrypt (~10 MB/s), RSA-2048-sign (~0.5 MB/s), ECDSA-sign (~5 MB/s). |

#### Section 4: Asymmetric Cryptography (7 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 18 | RSA Mathematics | Key generation: choose primes p, q. n = pq. phi(n) = (p-1)(q-1). Choose e s.t. gcd(e, phi(n))=1. Compute d = e^{-1} mod phi(n). Public key: (n,e). Private key: d. Encryption: c = m^e mod n. Decryption: m = c^d mod n. Security: factoring n is hard. | -- (mathematical derivation, step by step) |
| 19 | Elliptic Curve Fundamentals | Curve equation: y^2 = x^3 + ax + b over finite field F_p. Point addition: geometric (line through P,Q intersects curve at R, reflect). Point doubling: tangent line at P. Scalar multiplication: Q = dP (repeated addition). | TikZ: elliptic curve over reals showing point addition geometry: draw curve, points P and Q, line through them, intersection R', reflection to R = P + Q. |
| 20 | ECDSA Key Generation | secp256k1 parameters: p (256-bit prime), a=0, b=7, G (generator point), n (order). Private key: random d in [1, n-1]. Public key: Q = dG. Security: given Q and G, finding d requires solving ECDLP (infeasible for 256-bit). | -- (parameter table + formal generation steps) |
| 21 | The Discrete Logarithm Problem | Given G and Q = dG on elliptic curve, find d. Best known classical algorithm: Pollard's rho, O(sqrt(n)) ~ 2^128 for secp256k1. Compare: integer factoring (sub-exponential) vs ECDLP (exponential) -- why ECC keys are smaller. | pgfplots: comparison chart of attack complexity. x-axis = key size (bits), y-axis = operations needed (log scale). Two curves: RSA factoring (sub-exponential, GNFS) vs ECDLP (square root). Shows ECC advantage. |
| 22 | Ed25519 & Curve25519 | Modern alternatives to secp256k1. Curve25519: Montgomery curve, y^2 = x^3 + 486662x^2 + x mod 2^255 - 19. Advantages: constant-time implementation (side-channel resistant), faster than NIST curves, designed by Bernstein. Ed25519 = EdDSA on twisted Edwards curve. | -- (comparison table: secp256k1 vs Ed25519 vs P-256) |
| 23 | Elliptic Curve Point Multiplication | How Q = dG is computed efficiently: double-and-add algorithm. Example with small curve: binary expansion of d, sequence of doublings and additions. Time complexity: O(log d) point operations. | TikZ: step-by-step double-and-add diagram for d=11 (binary 1011): G -> 2G -> 2G+G=3G -> 6G -> 6G+G=7G -> ... Show each step as point on curve (abstract) |
| 24 | Why Blockchain Chose ECC | Three reasons: (1) Key size efficiency (256-bit ECC = 3072-bit RSA), (2) Signature size (64 bytes for ECDSA), (3) Performance (faster signing than RSA). Bitcoin: secp256k1. Ethereum: secp256k1. Newer chains: Ed25519 (Solana, Cardano). | -- (comparison summary + adoption table) |

#### Section 5: Digital Signatures (7 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 25 | ECDSA Formalization | Signing: (1) e = H(m), (2) pick random k, (3) (x1,y1) = kG, (4) r = x1 mod n, (5) s = k^{-1}(e + dr) mod n, (6) output (r,s). Verification: (1) e = H(m), (2) w = s^{-1} mod n, (3) u1 = ew, u2 = rw, (4) (x1,y1) = u1*G + u2*Q, (5) valid iff r = x1 mod n. | TikZ: two-column flow diagram. Left: signing steps with color-coded boxes. Right: verification steps. Arrows connecting corresponding elements. |
| 26 | Schnorr Signatures | Simpler than ECDSA. Signing: pick random k, R = kG, e = H(R||P||m), s = k - e*d. Signature: (R, s). Verification: sG = R - eP. Advantages: provably secure in ROM, linear (enables aggregation), simpler. Bitcoin Taproot (BIP-340) uses Schnorr. | TikZ: compact signing/verification flow, simpler than ECDSA diagram. Highlight "linearity" property with annotation. |
| 27 | Signature Aggregation (MuSig) | Multi-signature: n parties each with key pair (d_i, P_i). Aggregate public key: P_agg = sum(P_i). Aggregate signature: single (R, s) that validates against P_agg. Key aggregation: non-interactive. Benefits: privacy (looks like single sig), space savings, fee reduction. | TikZ: diagram showing n signers with individual keys converging into a single aggregate key and signature. Show on-chain footprint comparison: n individual sigs vs 1 aggregate sig. |
| 28 | Multi-Sig Schemes | m-of-n multisig: m signatures required from n possible signers. Bitcoin P2SH multisig. Ethereum: smart contract multisig (Gnosis Safe). Threshold signatures: no on-chain footprint, uses Shamir secret sharing for key distribution. | TikZ: 2-of-3 multisig diagram showing 3 key holders, any 2 can sign. Decision tree showing which combinations are valid. |
| 29 | Nonce Reuse Vulnerability | If same k is used for two different messages, private key can be recovered. Given (r, s1) for m1 and (r, s2) for m2 (same r because same k): d = (s1*e2 - s2*e1) / (s2*r - s1*r) mod n. Sony PS3 hack (2010): ECDSA nonce reuse leaked private key. | TikZ: attack diagram showing two signatures with same r value, arrows to private key extraction formula. Red warning box. |
| 30 | Batch Verification | Verify n signatures simultaneously faster than n individual verifications. For Schnorr: random linear combination. For ECDSA: requires pairing or batching tricks. Speedup: ~2x for large batches. Critical for blockchain node performance. | pgfplots: line chart. x-axis = number of signatures (10, 100, 1000). y-axis = verification time (ms). Two lines: individual verification (linear) vs batch verification (sublinear). |
| 31 | Signature Schemes Comparison | Table + chart comparing ECDSA, Schnorr, Ed25519, BLS. Properties: signature size, verification speed, aggregation support, quantum resistance, blockchain adoption. | pgfplots: grouped bar chart. x-axis = scheme name. Bars: signing speed, verification speed, signature size. Show Ed25519 fastest, BLS smallest aggregated, ECDSA most adopted. |

#### Section 6: Key Management & Wallets (6 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 32 | BIP-39: Mnemonic Seeds | Entropy (128-256 bits) -> checksum (first ENT/32 bits of SHA256) -> split into 11-bit groups -> map to 2048-word list -> 12-24 word mnemonic. PBKDF2 with passphrase to derive 512-bit seed. Example: 128 bits -> 4-bit checksum -> 132 bits -> 12 words. | TikZ: flow diagram: entropy bits -> append checksum -> split into 11-bit groups -> word lookup table -> mnemonic phrase. Show actual bit-level breakdown. |
| 33 | BIP-32: Hierarchical Deterministic Wallets | Master key from seed via HMAC-SHA512. Child key derivation: CKD function. Normal derivation: CKD((K_par, c_par), i) = HMAC-SHA512(c_par, K_par || i). Hardened derivation: uses private key (i >= 2^31). | TikZ: HD wallet tree. Root = master key. Level 1: purpose (m/44'). Level 2: coin type (m/44'/0' for BTC, m/44'/60' for ETH). Level 3: account. Level 4: change. Level 5: address index. |
| 34 | BIP-44: Multi-Account Hierarchy | Derivation path: m / purpose' / coin_type' / account' / change / address_index. Examples: m/44'/0'/0'/0/0 (first Bitcoin address), m/44'/60'/0'/0/0 (first Ethereum address). Enables one seed -> unlimited wallets across chains. | -- (path structure + examples table) |
| 35 | Key Derivation Security Analysis | Extended public key: allows deriving child public keys without private key (watch-only wallets). Risk: if extended public key + any child private key is leaked, master private key can be computed. Hardened derivation prevents this. | TikZ: security model diagram. Normal derivation: xpub -> child pub keys (safe). But xpub + child privkey -> master privkey (DANGER). Hardened: breaks this chain. |
| 36 | Hardware Wallet Architecture | Secure element chip: key generation and signing happen inside tamper-resistant hardware. PIN protection, screen verification, firmware updates. Attack surface: supply chain, firmware, side-channel. Comparison: Ledger (secure element) vs Trezor (general MCU). | TikZ: hardware wallet internals diagram: host computer <-> USB <-> MCU <-> secure element. Show trust boundary around secure element. |
| 37 | Wallet Recovery & Inheritance | Shamir's Secret Sharing for seed backup: split seed into n shares, any k can reconstruct. Social recovery wallets (Ethereum): guardian-based recovery without seed phrase. Time-locked transactions for inheritance. | TikZ: Shamir's Secret Sharing diagram: secret S split into 5 shares (S1-S5), any 3 can reconstruct. Show polynomial interpolation concept visually (3 points define a degree-2 polynomial). |

#### Section 7: Cryptographic Protocols (6 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 38 | Zero-Knowledge Proofs: Concept | Prover convinces verifier of statement truth without revealing any information beyond the statement's validity. Properties: completeness (honest prover convinces), soundness (cheating prover fails), zero-knowledge (verifier learns nothing else). Ali Baba cave analogy. | TikZ: Ali Baba cave diagram. Circular cave with a locked door. Prover enters, goes left or right. Verifier calls out a side. Prover emerges from correct side (proves knowledge of key without showing it). |
| 39 | ZK-SNARKs & ZK-STARKs | SNARKs: Succinct Non-interactive Arguments of Knowledge. Trusted setup required. Constant-size proofs (~200 bytes). Used in Zcash. STARKs: Scalable Transparent ARguments of Knowledge. No trusted setup. Larger proofs but quantum-resistant. Used in StarkNet. | -- (comparison table + properties) |
| 40 | Commitment Schemes | Two-phase protocol: Commit(m, r) = H(m || r), then Reveal(m, r). Properties: hiding (commitment reveals nothing about m), binding (cannot change m after committing). Pedersen commitments: C = mG + rH (homomorphic: C1 + C2 = (m1+m2)G + (r1+r2)H). | TikZ: two-phase diagram. Phase 1: Prover computes C = H(m||r), sends C to Verifier. Phase 2: Prover reveals (m, r), Verifier checks H(m||r) = C. Show binding and hiding properties with annotations. |
| 41 | Secret Sharing (Shamir) | Polynomial-based: secret s is constant term of degree-(k-1) polynomial p(x). Generate n points (shares): (i, p(i)) for i=1..n. Any k shares reconstruct p(x) via Lagrange interpolation. Fewer than k shares reveal nothing about s (information-theoretic security). | TikZ: plot showing a degree-2 polynomial (parabola). Mark 5 points on it (shares). Highlight that any 3 points determine the polynomial, but 2 points leave infinite possibilities. |
| 42 | Homomorphic Encryption Basics | Compute on encrypted data without decrypting. Partially homomorphic: RSA (multiplicative), Paillier (additive). Fully homomorphic (FHE): any computation. Performance: FHE is ~10000x slower than plaintext computation. Blockchain use: confidential transactions, private smart contracts. | -- (formal definitions + performance comparison) |
| 43 | Ring Signatures & Stealth Addresses | Ring signatures: signer is anonymous within a group. Used in Monero for sender privacy. Stealth addresses: one-time addresses for receiver privacy. Diffie-Hellman exchange creates unique address per transaction. Together: full transaction privacy. | TikZ: ring signature diagram. Circle of n public keys, one is the actual signer but verifier cannot determine which. Arrow from "message" to ring, output is valid signature. |

#### Section 8: Attacks & Post-Quantum (9 frames)
| Frame | Title | Content | TikZ/pgfplots |
|-------|-------|---------|---------------|
| 44 | Birthday Attack Detailed | Generic attack on hash functions. Complexity: O(2^{n/2}) for n-bit hash. For SHA-256: 2^128 operations (still infeasible). For MD5 (128-bit): 2^64 operations (feasible, MD5 is broken). Method: generate random inputs, store hashes, find collision via birthday paradox. | pgfplots: comparison of attack complexity for different hash sizes. x-axis = hash output size (128, 160, 256, 512 bits). y-axis = birthday attack complexity (log scale). Horizontal line at "feasible" threshold (~2^80). Shows MD5 below threshold, SHA-256 well above. |
| 45 | Length Extension Attack | Vulnerability of Merkle-Damgard hashes: given H(m) and length of m (but not m itself), can compute H(m || padding || m') for arbitrary m'. Affects: SHA-256, SHA-1, MD5. Not affected: SHA-3 (sponge), HMAC, truncated hashes. Mitigation: use HMAC(k, m) = H(k XOR opad || H(k XOR ipad || m)). | TikZ: attack diagram showing how the internal state after processing m becomes the IV for processing the extension. Show HMAC structure as defense. |
| 46 | Side-Channel Attacks | Timing attacks: measure execution time to infer secret key bits. Power analysis: monitor power consumption during crypto operations. Electromagnetic emanation: capture EM leaks. Cache attacks: exploit CPU cache timing. Mitigations: constant-time code, masking, shielding. | TikZ: three-panel diagram. Panel 1: timing trace with data-dependent variations. Panel 2: power trace showing correlations with key bits. Panel 3: cache access pattern revealing secret data. |
| 47 | Quantum Computing: Shor's Algorithm | Factors integers in polynomial time: O((log n)^3). Breaks RSA, DSA, ECDSA (reduces ECDLP to polynomial time). Timeline: current quantum computers ~1000 qubits, need ~4000 logical qubits for RSA-2048. Estimated: 2030-2040 for cryptographically relevant QC. | pgfplots: timeline chart. x-axis = year (2020-2040). y-axis = qubits (log scale). Plot current progress curve + projected growth. Horizontal lines at RSA-2048 break threshold and ECDSA-256 break threshold. |
| 48 | Quantum Computing: Grover's Algorithm | Speeds up brute-force search: O(2^{n/2}) instead of O(2^n). Effect on symmetric crypto: AES-128 -> 2^64 (insecure), AES-256 -> 2^128 (still secure). Effect on hash functions: preimage resistance halved. Mitigation: double key sizes. | -- (impact table: algorithm, classical security, post-quantum security, recommendation) |
| 49 | Post-Quantum Cryptography Candidates | NIST PQC standardization (2024): CRYSTALS-Kyber (lattice-based KEM, now ML-KEM), CRYSTALS-Dilithium (lattice-based signatures, now ML-DSA), FALCON (lattice-based, compact signatures), SPHINCS+ (hash-based signatures, conservative). Key sizes: ML-KEM-768 public key = 1184 bytes (vs ECDH = 32 bytes). | pgfplots: grouped bar chart comparing key/signature sizes. x-axis = scheme. Bars: public key size, signature size. Groups: ECDSA, ML-DSA-65, FALCON-512, SPHINCS+-128s. Show the size inflation of post-quantum schemes. |
| 50 | Blockchain Post-Quantum Migration | Challenge: billions of existing addresses use ECDSA. Migration strategies: (1) soft fork to add PQ signature types, (2) hybrid signatures (classical + PQ), (3) commit-reveal for existing funds. Bitcoin: quantum-safe address migration proposals. Ethereum: account abstraction enables PQ signatures per-account. | TikZ: migration roadmap diagram. Current state -> Hybrid phase (both classical + PQ) -> Full PQ phase. Show timeline and key milestones. |
| 51+ | Summary & Key Formulas | Formula reference sheet: hash properties, ECDSA signing/verification, birthday bound, Diffie-Hellman, Shamir's threshold. Key takeaways per section. | -- (structured reference) |
| 52+ | Questions & Discussion | Open-ended prompts: (1) When will quantum computers threaten Bitcoin? (2) Is perfect privacy possible on a public blockchain? (3) What is the right trade-off between usability and security in key management? | -- |

**Total frame target:** ~55 frames (Sec1: 5 + Sec2: 7 + Sec3: 5 + Sec4: 7 + Sec5: 7 + Sec6: 6 + Sec7: 6 + Sec8: 9 = 52 frames, within 50-70 range; Summary and Questions frames are included in Section 8's count)

**Acceptance Criteria:**
- [ ] 50-70 `\begin{frame}` blocks (target: ~55)
- [ ] Exactly 8 `\section{}` commands
- [ ] At least 15 distinct TikZ pictures (`\begin{tikzpicture}`)
- [ ] At least 5 pgfplots charts (`\begin{axis}`)
- [ ] Mathematical formulations: hash properties (preimage, collision), ECDSA signing/verification, birthday bound formula, Diffie-Hellman exchange, Shamir polynomial, Schnorr signature
- [ ] Uses `\bottomnote{}` on content frames
- [ ] Title: "Cryptography & Security: A Quantitative Deep Dive"
- [ ] Subtitle: "Standalone Technical Lecture"
- [ ] Content does NOT duplicate existing L02 (deeper, more formal, covers symmetric crypto, ZK proofs, post-quantum -- topics absent from existing L02)
- [ ] All TikZ/pgfplots use course colors
- [ ] No `\includegraphics` calls
- [ ] Preamble matches `lectures/blockchain_fundamentals.tex` lines 1-36 structure (full preamble + title block, then modify title/subtitle)
- [ ] Compiles with pdflatex

---

### T6: Quiz Parts 1-2 -- `quiz/quiz_cs_part1.html` and `quiz/quiz_cs_part2.html` (D5a, D5b)
**Priority:** P1
**Effort:** Medium
**Depends on:** None (independent)
**Files:**
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_cs_part1.html`
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_cs_part2.html`

**HTML Template Pattern (from `quiz/quiz1.html`):**
- Copy entire `quiz/quiz1.html` file as template
- Keep exact same CSS (all styles verbatim)
- Keep exact same JS logic (all functions verbatim)
- Same nav structure: title in `.nav-title`, links to `../index.html` (Dashboard) and GitHub
- Same quiz container, header, stats, progress bar, questions-row, next button, results card
- KaTeX loaded for math rendering
- Replace: `<title>`, `.nav-title` text, `.quiz-title` text, `quizData.questions` array

**Quiz Part 1: Hash Functions & Symmetric Crypto (20 questions)**
Nav title: "Quiz CS-1: Hash Functions & Symmetric Crypto"

Topic distribution:
- Hash function properties (preimage, collision, second preimage resistance) -- 4 questions
- SHA-256 specifics (output size, block size, rounds, Merkle-Damgard) -- 3 questions
- Avalanche effect and Hamming distance -- 2 questions
- Birthday bound and collision probability -- 2 questions
- Sponge construction / SHA-3 -- 2 questions
- AES overview (block size, key sizes, rounds) -- 3 questions
- Block cipher modes (ECB, CBC, CTR, GCM) -- 2 questions
- Key exchange (Diffie-Hellman) -- 2 questions

**Quiz Part 2: Asymmetric Crypto & Digital Signatures (20 questions)**
Nav title: "Quiz CS-2: Asymmetric Crypto & Digital Signatures"

Topic distribution:
- RSA mathematics (key generation, encryption, security basis) -- 3 questions
- Elliptic curve fundamentals (curve equation, point addition, scalar multiplication) -- 3 questions
- ECDSA signing and verification steps -- 3 questions
- Discrete logarithm problem -- 2 questions
- Schnorr signatures (properties, advantages over ECDSA) -- 2 questions
- Signature aggregation (MuSig) -- 2 questions
- Multi-sig schemes (m-of-n, threshold) -- 2 questions
- Nonce reuse vulnerability -- 1 question
- Ed25519 / Curve25519 -- 1 question
- Batch verification -- 1 question

**Question format (per quiz1.html pattern):**
```javascript
{
    "id": 1,
    "question": "Question text with $KaTeX$ math where appropriate?",
    "options": {
        "A": "First option (no letter prefix in value)",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
    },
    "correct": "B",
    "explanation": "Explanation of why the correct answer is correct and why others are wrong."
}
```

**CRITICAL format notes:**
- `options` is an OBJECT with keys `"A"`, `"B"`, `"C"`, `"D"` -- NOT an array
- `correct` is a LETTER STRING (e.g., `"B"`) -- NOT a 0-indexed integer
- Option values must NOT include letter prefixes (e.g., write `"First option"` not `"A) First option"`)

**Acceptance Criteria:**
- [ ] Each file has exactly 20 questions in the `quizData.questions` array
- [ ] Each question has `options` as an object with keys `"A"`, `"B"`, `"C"`, `"D"` (NOT an array)
- [ ] Each question has `correct` as a letter string (e.g., `"B"`) -- NOT a 0-indexed integer
- [ ] Option values have NO letter prefix (e.g., `"First option"` not `"A) First option"`)
- [ ] Each question has an `explanation` field
- [ ] HTML/CSS/JS structure matches `quiz/quiz1.html` exactly (same CSS, same JS, only content differs)
- [ ] Nav links: Dashboard -> `../index.html`, GitHub -> repo URL
- [ ] KaTeX loaded for math rendering
- [ ] Questions use KaTeX math notation where appropriate (e.g., `$O(2^{n/2})$`, `$H(m)$`)
- [ ] No duplicate questions between Part 1 and Part 2
- [ ] No duplicate questions with existing quizzes (`quiz/quiz1.html` through `quiz4.html`, `quiz_bf_part*.html`)
- [ ] Quiz titles match: "Quiz CS-1: Hash Functions & Symmetric Crypto" / "Quiz CS-2: Asymmetric Crypto & Digital Signatures"

---

### T7: Quiz Parts 3-4 -- `quiz/quiz_cs_part3.html` and `quiz/quiz_cs_part4.html` (D5c, D5d)
**Priority:** P1
**Effort:** Medium
**Depends on:** None (independent)
**Files:**
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_cs_part3.html`
- `D:/Joerg/Research/slides/cryptocurrency/quiz/quiz_cs_part4.html`

**Quiz Part 3: Key Management & Wallets (20 questions)**
Nav title: "Quiz CS-3: Key Management & Wallets"

Topic distribution:
- BIP-39 mnemonic seeds (entropy, checksum, word list, PBKDF2) -- 4 questions
- BIP-32 hierarchical deterministic wallets (key derivation, hardened vs normal) -- 4 questions
- BIP-44 derivation paths (purpose, coin type, account, change, index) -- 3 questions
- Hardware wallet architecture (secure element, PIN, trust boundary) -- 3 questions
- Hot vs cold wallets (trade-offs, use cases) -- 2 questions
- Extended public keys and watch-only wallets -- 2 questions
- Wallet recovery and Shamir's Secret Sharing -- 2 questions

**Quiz Part 4: Protocols, Attacks & Post-Quantum (20 questions)**
Nav title: "Quiz CS-4: Protocols, Attacks & Post-Quantum"

Topic distribution:
- Zero-knowledge proofs (properties, SNARKs vs STARKs) -- 3 questions
- Commitment schemes (hiding, binding, Pedersen) -- 2 questions
- Secret sharing (Shamir, threshold, reconstruction) -- 2 questions
- Ring signatures and stealth addresses -- 2 questions
- Birthday attack (complexity, affected algorithms) -- 2 questions
- Length extension attack (affected constructions, HMAC defense) -- 1 question
- Side-channel attacks (timing, power analysis, mitigations) -- 2 questions
- Shor's algorithm (impact on RSA, ECC) -- 2 questions
- Grover's algorithm (impact on symmetric crypto, hash functions) -- 2 questions
- Post-quantum candidates (NIST PQC: ML-KEM, ML-DSA, FALCON, SPHINCS+) -- 2 questions

**Acceptance Criteria:**
- [ ] Same as T6 criteria (including: `options` as object with `"A"`-`"D"` keys, `correct` as letter string, no letter prefixes in option values)
- [ ] No duplicate questions across all 4 CS quiz parts
- [ ] No duplicate questions with existing quizzes
- [ ] Nav titles: "Quiz CS-3: Key Management & Wallets" / "Quiz CS-4: Protocols, Attacks & Post-Quantum"

---

### T8: GH Pages Update -- `index.html` (D6)
**Priority:** P1
**Effort:** Low-Medium
**Depends on:** T2, T3, T4, T5, T6, T7 (needs final file paths confirmed)
**File:** `D:/Joerg/Research/slides/cryptocurrency/index.html` (MODIFY existing)

**Changes Required:**

1. **Update hero stats**: Change Lectures count from 4 to 8, Quizzes count from 8 to 12
   ```html
   <!-- Before -->
   <span><b>4</b><small>Lectures</small></span>
   <span><b>8</b><small>Quizzes</small></span>
   <!-- After -->
   <span><b>8</b><small>Lectures</small></span>
   <span><b>12</b><small>Quizzes</small></span>
   ```

2. **Add sidebar nav entries** inside the existing `<details class="d5">` block for Standalone Lectures:
   ```html
   <details class="d5" open><summary>Standalone Lectures</summary>
   <!-- Existing BF entries -->
   <a href="#sl-mini">Mini-Lecture: Blockchain</a>
   <a href="#sl-intro">INTRO Preview</a>
   <a href="#sl-pre">Pre-Class Handout</a>
   <a href="#sl-main">Technical Lecture</a>
   <!-- NEW CS entries -->
   <a href="#sl-cs-mini">Mini-Lecture: Crypto</a>
   <a href="#sl-cs-intro">CS INTRO Preview</a>
   <a href="#sl-cs-pre">CS Pre-Class Handout</a>
   <a href="#sl-cs-main">CS Technical Lecture</a>
   </details>
   ```

3. **Add CS subsection** WITHIN the existing `<section class="section d5" id="standalone-lectures">`, AFTER the BF quizzes grid (after line 321's closing `</div>`) and BEFORE the section's closing `</section>` tag (line 322).

   **New CS subsection structure (insert before `</section>` on line 322):**

   ```html
   <div class="section-head d5" style="margin-top:16px"><span>CS</span><h2>Standalone Lectures: Cryptography &amp; Security</h2></div>

   <div class="lec-subsection">Mini-Lecture</div>
   <div class="lec-grid">
   <a href="lectures/cryptography_intro.pdf" class="lec-card" id="sl-cs-mini">
   <div><span class="lec-num">CS</span><span class="lec-title">Cryptography &amp; Security</span></div>
   <div class="lec-meta">10-slide visual introduction with TikZ comics</div>
   </a>
   </div>

   <div class="lec-subsection">Technical Lecture Bundle</div>
   <div class="lec-grid">
   <a href="lectures/cryptography_security_intro.pdf" class="lec-card" id="sl-cs-intro">
   <div><span class="lec-num">INTRO</span><span class="lec-title">CS Course Preview</span></div>
   <div class="lec-meta">6-slide preview deck with charts</div>
   </a>
   <a href="lectures/cryptography_security_preclass.pdf" class="lec-card" id="sl-cs-pre">
   <div><span class="lec-num">PRE</span><span class="lec-title">Pre-Class Handout</span></div>
   <div class="lec-meta">2-page discovery activities</div>
   </a>
   <a href="lectures/cryptography_security.pdf" class="lec-card" id="sl-cs-main">
   <div><span class="lec-num">90min</span><span class="lec-title">Cryptography &amp; Security</span></div>
   <div class="lec-meta">55+ frame quantitative deep dive</div>
   </a>
   </div>

   <div class="lec-subsection">Associated Quizzes</div>
   <div class="quiz-grid">
   <a href="quiz/quiz_cs_part1.html" class="quiz-card">
   <div><span class="quiz-num">CS-1</span><span class="quiz-title">Hash Functions &amp; Symmetric Crypto</span></div>
   <div class="quiz-meta">20 questions</div>
   </a>
   <a href="quiz/quiz_cs_part2.html" class="quiz-card">
   <div><span class="quiz-num">CS-2</span><span class="quiz-title">Asymmetric Crypto &amp; Digital Signatures</span></div>
   <div class="quiz-meta">20 questions</div>
   </a>
   <a href="quiz/quiz_cs_part3.html" class="quiz-card">
   <div><span class="quiz-num">CS-3</span><span class="quiz-title">Key Management &amp; Wallets</span></div>
   <div class="quiz-meta">20 questions</div>
   </a>
   <a href="quiz/quiz_cs_part4.html" class="quiz-card">
   <div><span class="quiz-num">CS-4</span><span class="quiz-title">Protocols, Attacks &amp; Post-Quantum</span></div>
   <div class="quiz-meta">20 questions</div>
   </a>
   </div>
   ```

4. **No new CSS needed** -- the existing d5/lec-card/lec-grid/quiz-card classes already handle the styling (rose #e11d48 color).

**Acceptance Criteria:**
- [ ] CS subsection visible within the Standalone Lectures section
- [ ] CS subsection appears AFTER the BF subsection
- [ ] Mini-lecture card with "CS" badge linking to `lectures/cryptography_intro.pdf`
- [ ] INTRO card linking to `lectures/cryptography_security_intro.pdf`
- [ ] PRE card linking to `lectures/cryptography_security_preclass.pdf`
- [ ] 90min card linking to `lectures/cryptography_security.pdf`
- [ ] 4 quiz cards (CS-1 through CS-4) linking to correct quiz HTML files
- [ ] All links are relative paths (no absolute URLs)
- [ ] Hero stats updated: Lectures = 8, Quizzes = 12
- [ ] Sidebar navigation updated with CS entries
- [ ] Existing BF subsection and all other sections unchanged
- [ ] Page renders correctly (valid HTML)

---

## 6. Commit Strategy

| Commit | Tasks | Message |
|--------|-------|---------|
| C1 | T2, T3, T4 | "feat: add cryptography mini-lecture, INTRO preview, and pre-class handout" |
| C2 | T5 | "feat: add 55-frame quantitative cryptography & security lecture" |
| C3 | T6, T7 | "feat: add 4-part cryptography & security quiz (80 questions)" |
| C4 | T8 | "feat: add CS subsection to standalone lectures on GH Pages" |

---

## 7. Risk Identification

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TikZ compilation errors in complex crypto diagrams | Medium | High | Use well-tested TikZ patterns from L01. Keep diagrams modular. Avoid exotic libraries. Test elliptic curve TikZ with simple coordinates. |
| pgfplots data accuracy (crypto performance numbers) | Medium | Medium | Use approximate but defensible data points from published benchmarks. Add footnotes citing sources. Label as "approximate" where needed. |
| Quiz question overlap with existing quiz2 (Cryptography & Security) | Medium | Medium | Cross-reference all 20 questions in `quiz/quiz2.html` before writing. New quizzes focus on DEEPER topics (sponge construction, ZK proofs, post-quantum) not covered in existing quiz2. |
| LaTeX preamble mismatch with L01 | Low | High | Copy preamble verbatim from L01 lectures. Only change title/subtitle/author fields. |
| index.html breaking existing BF subsection | Low | High | Insert new CS subsection AFTER BF subsection. Never modify BF HTML. Test that both subsections render. |
| Content overlap with existing L02 (32 frames) | Medium | Medium | Existing L02 covers hash functions, public key crypto, digital signatures, and wallets at an introductory level with `\includegraphics` diagrams and Python code demos. New lecture MUST add: symmetric crypto (AES, block cipher modes), sponge construction, Schnorr signatures, ZK proofs, commitment schemes, secret sharing, length extension attacks, post-quantum crypto, ring signatures -- all absent from existing L02. |
| T5 file too large for single agent | Medium | Medium | T5 targets ~55 frames. Can be split into sub-tasks: T5a (sections 1-4, ~24 frames), T5b (sections 5-8, ~31 frames) if needed. |
| Elliptic curve TikZ diagrams too complex | Low | Medium | Use abstract/simplified curve representations. Do not attempt to plot actual secp256k1 over finite fields. Use smooth curves over reals for visual clarity. |

---

## 8. Verification Steps

| Step | Command/Check | Pass Criteria |
|------|---------------|---------------|
| V1 | `ls lectures/cryptography*.tex lectures/cryptography_security*.tex` | 4 new `.tex` files present (cryptography_intro.tex, cryptography_security_intro.tex, cryptography_security_preclass.tex, cryptography_security.tex) |
| V2 | `ls quiz/quiz_cs_*` | 4 `.html` files present (quiz_cs_part1.html through part4.html) |
| V3 | Frame count in D1 | `grep -c '\\begin{frame}' lectures/cryptography_intro.tex` = 10 |
| V4 | Frame count in D2 | `grep -c '\\begin{frame}' lectures/cryptography_security_intro.tex` = 6 |
| V5 | Frame count in D4 | `grep -c '\\begin{frame}' lectures/cryptography_security.tex` in range [50, 70] |
| V6 | Section count in D4 | `grep -c '\\section{' lectures/cryptography_security.tex` = 8 |
| V7 | TikZ count in D4 | `grep -c 'begin{tikzpicture}' lectures/cryptography_security.tex` >= 15 |
| V8 | pgfplots count in D4 | `grep -c 'begin{axis}' lectures/cryptography_security.tex` >= 5 |
| V9 | Question count per quiz | `grep -c '"id":' quiz/quiz_cs_partN.html` = 20 for each N in {1,2,3,4} |
| V10 | Index.html validity | Open in browser, verify CS subsection renders within Standalone Lectures, all links work |
| V11 | No existing file changes | `git diff --name-only` shows only `index.html` as modified existing file; all others are new files |
| V12 | Preamble consistency | Compare preamble of each new beamer `.tex` with `lectures/blockchain_intro.tex` (for T2/T3) or `lectures/blockchain_fundamentals.tex` (for T5) -- colors, theme, macros must match |
| V13 | Quiz HTML consistency | Compare CSS/JS structure of new quiz files with `quiz/quiz1.html` -- must be identical except question data, title, and nav-title |
| V14 | Article class check for T4 | `grep 'documentclass.*article' lectures/cryptography_security_preclass.tex` returns match; `grep 'bottomnote' lectures/cryptography_security_preclass.tex` returns NO match |
| V15 | No \includegraphics | `grep -c 'includegraphics' lectures/cryptography_intro.tex lectures/cryptography_security_intro.tex lectures/cryptography_security.tex` = 0 for all three |

---

## 9. Execution Notes for Implementers

### LaTeX Preamble Templates

**For T2 and T3 (mini-lecture, INTRO preview -- no code listings needed):**
Copy `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_intro.tex` lines 1-65 verbatim. This includes:
- documentclass, Madrid theme, graphicx/booktabs/adjustbox/multicol/amsmath/listings/xcolor packages
- 12 color definitions (mlblue through midgray)
- beamercolor settings (palette primary/secondary/tertiary/quaternary, structure, title, frametitle, block title/body)
- navigation symbols removed, itemize items, margins
- `\bottomnote{}` macro definition
- TikZ and pgfplots packages with libraries

Then change ONLY the `\title{}`, `\subtitle{}`, and keep author/institute/date the same.

**For T5 (technical lecture -- includes listings style for pseudocode):**
Copy `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_fundamentals.tex` lines 1-36 verbatim. This is the compact preamble including the title block. Then modify `\title{}`, `\subtitle{}` for L02. The preamble includes:
- Same documentclass, theme, packages (single-line combined)
- Same 10 color definitions (compact format; omits `lightgray` and `midgray` vs the full 12-color palette in `blockchain_intro.tex`, but this is sufficient since those two colors are not used in beamer content frames)
- Same beamercolor settings (compact)
- `\bottomnote{}` macro (compact)
- `\lstdefinestyle{python}{...}` and `\lstset{style=python}`
- TikZ/pgfplots with full library set including `chains` and `automata`

Then change ONLY `\title{}`, `\subtitle{}`.

**For T4 (article class -- completely different preamble):**
Copy `D:/Joerg/Research/slides/cryptocurrency/lectures/blockchain_fundamentals_preclass.tex` lines 1-50 verbatim. Change:
- `\fancyhead[L]` to: `{\small\color{mlpurple}\textbf{Cryptography \& Security} \textcolor{mlgray}{|} Lesson 02 \textcolor{mlgray}{|} Pre-Class Discovery Handout}`
- Keep everything else identical

**CRITICAL:** T4 must NOT use `\bottomnote{}` (not defined in article class). Use the `\activitybox{}` macro for activities.

### Quiz HTML Template
`D:/Joerg/Research/slides/cryptocurrency/quiz/quiz1.html` is the canonical template. Copy the entire file, then replace:
1. `<title>` tag content (e.g., "Quiz CS-1: Hash Functions & Symmetric Crypto | Build Your Own Cryptocurrency")
2. `.nav-title` text (e.g., "Quiz CS-1: Hash Functions & Symmetric Crypto")
3. `.quiz-title` text in the quiz-header section
4. The `quizData.questions` array (replace all 20 question objects)

Keep ALL CSS (lines 10-295 approximately) and ALL JS (lines 337-770 approximately) completely unchanged.

### TikZ Comic Strip Pattern (for T2 stick figures and speech bubbles)
```latex
\begin{tikzpicture}
  % Stick figure (Alice)
  \draw[thick,mlblue] (0,0) circle (0.3); % head
  \draw[thick,mlblue] (0,-0.3) -- (0,-1.2); % body
  \draw[thick,mlblue] (0,-0.6) -- (-0.5,-1); % left arm
  \draw[thick,mlblue] (0,-0.6) -- (0.5,-1); % right arm
  \draw[thick,mlblue] (0,-1.2) -- (-0.3,-1.8); % left leg
  \draw[thick,mlblue] (0,-1.2) -- (0.3,-1.8); % right leg
  \node[below,font=\tiny\bfseries,mlblue] at (0,-1.9) {Alice};
  % Speech bubble
  \node[draw,rounded corners,fill=mllavender4,text width=3cm,align=center,font=\small] at (2.5, 0.5) {I need to send Bob a secret message!};
  \draw[->,thick] (1.2, 0.3) -- (0.4, 0.1);
\end{tikzpicture}
```

### pgfplots Chart Pattern
```latex
\begin{tikzpicture}
\begin{axis}[
  width=0.9\textwidth, height=5cm,
  xlabel={X Label}, ylabel={Y Label},
  grid=major, grid style={gray!30},
  title style={font=\bfseries},
  every axis label/.style={font=\small},
  tick label style={font=\tiny},
  legend style={font=\tiny, at={(0.97,0.97)}, anchor=north east}
]
\addplot[mlblue, thick, mark=*] coordinates { (1,10) (2,20) (3,30) };
\addplot[mlorange, thick, mark=square*] coordinates { (1,15) (2,25) (3,35) };
\legend{Series A, Series B}
\end{axis}
\end{tikzpicture}
```

### Elliptic Curve TikZ Pattern (for T5)
Use smooth curves over reals for visual clarity -- do NOT attempt to plot finite field points.
```latex
\begin{tikzpicture}[scale=0.8]
  % Axes
  \draw[->] (-2.5,0) -- (3.5,0) node[right] {$x$};
  \draw[->] (0,-3) -- (0,3) node[above] {$y$};
  % Curve y^2 = x^3 + 7 (approximate)
  \draw[thick,mlblue,domain=-1.9:2.5,samples=100] plot (\x, {sqrt(\x*\x*\x + 7)});
  \draw[thick,mlblue,domain=-1.9:2.5,samples=100] plot (\x, {-sqrt(\x*\x*\x + 7)});
  % Points P and Q
  \fill[mlred] (P) circle (2pt) node[above left] {$P$};
  \fill[mlgreen] (Q) circle (2pt) node[above right] {$Q$};
\end{tikzpicture}
```

---

## 10. Post-Implementation: PDF Compilation

The `index.html` links point to `.pdf` files but no task in this plan produces those PDFs. They must be compiled manually by the user after all `.tex` files are created.

**Compilation commands (run from the repository root):**

```bash
# Mini-lecture
cd lectures && pdflatex cryptography_intro.tex && pdflatex cryptography_intro.tex && cd ..

# INTRO preview
cd lectures && pdflatex cryptography_security_intro.tex && pdflatex cryptography_security_intro.tex && cd ..

# Pre-class handout
cd lectures && pdflatex cryptography_security_preclass.tex && pdflatex cryptography_security_preclass.tex && cd ..

# Technical lecture (run twice for cross-references)
cd lectures && pdflatex cryptography_security.tex && pdflatex cryptography_security.tex && cd ..
```

**Notes:**
- Each file is compiled twice to resolve cross-references (TOC, page numbers).
- Requires a working TeX distribution (e.g., TeX Live, MiKTeX) with `pdflatex` on PATH.
- Required packages: `tikz`, `pgfplots`, `listings`, `beamer`, `geometry`, `enumitem`, `xcolor`, `hyperref`, `amsmath`, `booktabs`, `adjustbox`, `multicol`.
- Until these commands are run, the PDF links on `index.html` will return 404.
