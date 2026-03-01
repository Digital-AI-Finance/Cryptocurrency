# L13: Privacy & Zero-Knowledge Proofs

## Requirements Summary

| Attribute | Value |
|-----------|-------|
| Topic | Privacy & Zero-Knowledge Proofs |
| Focus | Theory-heavy: deep math (polynomial commitments, circuit design, proof systems, information-theoretic security) |
| Code level | Light: 3-4 Solidity snippets only |
| Quiz prefix | ZK |
| GH Pages color | Teal `#0d9488`, CSS class `d13` |
| Template source | L12 Tokenomics (`tokenomics_mechanism_intro.tex`, `tokenomics_mechanism.tex`, `quiz_tm_part*.html`) |

## Files to Create

| # | File | Type | Description |
|---|------|------|-------------|
| 1 | `lectures/privacy_zk_proofs_intro.tex` | LaTeX | Mini-lecture: 10 frames, TikZ comics, zero code |
| 2 | `lectures/privacy_zk_proofs.tex` | LaTeX | Technical lecture: ~55 frames, 5 sections, 3-4 Solidity snippets |
| 3 | `quiz/quiz_zk_part1.html` | HTML | Quiz ZK-1: ZK Proof Foundations (20 questions) |
| 4 | `quiz/quiz_zk_part2.html` | HTML | Quiz ZK-2: Proof Systems (20 questions) |
| 5 | `quiz/quiz_zk_part3.html` | HTML | Quiz ZK-3: Privacy Coins (20 questions) |
| 6 | `quiz/quiz_zk_part4.html` | HTML | Quiz ZK-4: ZK Applications & Future (20 questions) |
| 7 | `index.html` | HTML | Update: add d13 CSS, sidebar nav, lecture cards, quiz cards |

## Deliverable 1: Mini-Lecture (`privacy_zk_proofs_intro.tex`)

**Template:** Clone exact structure from `tokenomics_mechanism_intro.tex` -- same preamble, same color definitions, same `\bottomnote` command, same TikZ library imports, same `[8pt,aspectratio=169]{beamer}` with Madrid theme.

### Frame-by-Frame Content

| Frame | Title | TikZ Content |
|-------|-------|-------------|
| 1 | Title | `Privacy & Zero-Knowledge Proofs: A Visual Introduction`. Quote: "Privacy is the power to selectively reveal oneself to the world" -- Eric Hughes, Cypherpunk Manifesto. 3-panel style not needed here; use centered layout like L12 Frame 1. |
| 2 | What is a Zero-Knowledge Proof? | **3 panels.** Panel 1: Alice (stick figure) wants to prove she knows a secret password to Bob, WITHOUT revealing it. Panel 2: The 3 ZK properties shown as labeled boxes -- Completeness (honest prover convinces), Soundness (cheater fails), Zero-Knowledge (verifier learns nothing). Panel 3: Real-world analogy -- "Waldo" puzzle: proving you found Waldo by covering everything else with a sheet. |
| 3 | Interactive vs Non-Interactive Proofs | **3 panels.** Panel 1: Interactive ZK -- Alice and Bob exchange multiple messages (challenge-response arrows). Label: "Requires back-and-forth, online parties." Panel 2: Non-Interactive (NIZK) -- Alice produces single proof, Bob verifies offline. Arrow: "Common Reference String (CRS)." Panel 3: Fiat-Shamir Heuristic -- transform interactive to non-interactive via hash function replacing verifier's random challenge. |
| 4 | The Math Behind ZK | **2 large panels.** Left panel: "Proving Without Revealing" -- graph showing discrete log problem: given g, p, and y = g^x mod p, find x is hard. Visual: padlock with equation. Right panel: "Commitment Schemes" -- Pedersen commitment C = g^v * h^r. Boxes: Hiding (can't recover v from C), Binding (can't change v after committing). Bottom: "These mathematical hardness assumptions make ZK possible." |
| 5 | SNARKs vs STARKs | **3 panels.** Panel 1: SNARK properties in styled boxes -- Succinct, Non-interactive, ARgument of Knowledge. Key metrics: proof size ~200 bytes, verification O(1). Warning icon: "Requires trusted setup." Panel 2: STARK properties -- Scalable, Transparent (no trusted setup). Key metrics: proof size ~45KB, verification O(log^2 n). Shield icon: "Post-quantum secure." Panel 3: Comparison table -- rows for Trusted Setup (SNARK: yes, STARK: no), Proof Size (SNARK: small, STARK: larger), Quantum Safe (SNARK: no, STARK: yes), Verification (SNARK: fast, STARK: fast). |
| 6 | Privacy Coins Overview | **3 panels.** Panel 1: Monero -- ring signatures shown as circle of signers where true signer is hidden. Label: "Ring signatures + stealth addresses + RingCT." Panel 2: Zcash -- shielded pool with t-addresses (transparent) and z-addresses (private). Arrow shows coins entering shielded pool. Label: "zk-SNARKs power private transactions." Panel 3: Comparison box -- Monero (default private, larger txs, no trusted setup) vs Zcash (opt-in private, smaller shielded txs, trusted setup required). |
| 7 | ZK-Rollups Simplified | **3 panels.** Panel 1: Problem -- Ethereum mainnet congested, high gas fees. Visual: traffic jam of transactions. Panel 2: Solution -- ZK-Rollup bundles 1000s of txs off-chain, generates single proof. Visual: funnel compressing many tx boxes into one small proof box. Panel 3: Result -- proof posted on L1, verified cheaply. Projects: zkSync, StarkNet, Polygon zkEVM. Key stat: "1000x throughput improvement." |
| 8 | Real-World ZK Applications | **4-quadrant layout** (like L12 Frame 4 token utility types). Top-left: "Private Voting" -- ballot box + checkmark, anonymous but verifiable elections. Top-right: "Identity Verification" -- ID card + shield, prove age/citizenship without revealing full ID. Bottom-left: "DeFi Privacy" -- lock icon, private trading, hidden balances (Tornado Cash, Railgun). Bottom-right: "Supply Chain" -- chain links, prove product authenticity without exposing trade secrets. |
| 9 | The ZK Landscape | **2-panel wide layout.** Left: Timeline showing ZK evolution -- 1985 GMR paper, 2012 SNARKs, 2016 Zcash launch, 2018 STARKs paper, 2020 PLONK, 2023 ZK-Rollups mainstream. Right: Ecosystem map -- Research (academia, crypto labs), Infrastructure (proving systems, compilers), Applications (rollups, privacy, identity). Bottom summary bar: "ZK is the most important cryptographic breakthrough since public-key cryptography." |
| 10 | Key Takeaways | **5-box numbered layout** (identical to L12 Frame 10). Box 1: "ZK proofs prove knowledge without revealing it" -- completeness, soundness, zero-knowledge. Box 2: "SNARKs are small but need trusted setup; STARKs are transparent and quantum-safe." Box 3: "Privacy coins (Monero, Zcash) use different cryptographic approaches." Box 4: "ZK-Rollups are scaling Ethereum by orders of magnitude." Box 5: "ZK powers private voting, identity, DeFi, and more." Bottom bar: "Coming Next: Deep dive into proof system math, circuit design, privacy coin internals, and ZK-rollup architecture." |

## Deliverable 2: Technical Lecture (`privacy_zk_proofs.tex`)

**Template:** Clone exact structure from `tokenomics_mechanism.tex` -- same preamble with Solidity lstdefinelanguage, same `\bottomnote`, same TikZ/pgfplots imports, same opening frames (Title, Roadmap, TOC).

### Opening Frames (3 frames)

| Frame | Content |
|-------|---------|
| 1 | `\titlepage` -- "Privacy & Zero-Knowledge Proofs: From Theory to Application" |
| 2 | Lecture Roadmap -- 5-box TikZ flow: 1. ZK Foundations -> 2. Proof Systems -> 3. Privacy Coins -> 4. ZK Applications -> 5. Advanced Topics. Learning Objectives: Formalize ZK proof definitions, compare SNARK/STARK/Bulletproof, analyze privacy coin cryptography, evaluate ZK-rollup architectures, assess future directions. Prerequisites: Lessons 1-5 plus L12 Tokenomics recommended. |
| 3 | Table of Contents via `\tableofcontents` |

### Section 1: ZK Proof Foundations & Mathematical Basics (~11 frames, Frames 4-14)

| Frame | Title | Content Type |
|-------|-------|-------------|
| 4 | Historical Context: The GMR Paper (1985) | Text + timeline TikZ. Goldwasser-Micali-Rackoff original definition. Motivation: can we prove statements without revealing why they're true? |
| 5 | Formal Definition of ZK Proofs | Math-heavy. Definition: Interactive proof system (P, V) for language L. Three properties stated formally: Completeness (Pr[V accepts] >= 1-e for x in L), Soundness (Pr[V accepts] <= e for x not in L), Zero-Knowledge (exists simulator S such that View_V(P(x,w)) is computationally indistinguishable from S(x)). |
| 6 | The Simulation Paradigm | Two-column. Left: "Real World" -- prover and verifier interact, verifier sees transcript. Right: "Simulated World" -- simulator produces identical-looking transcript WITHOUT the witness. Key insight: if simulated and real are indistinguishable, verifier learned nothing. Formal: computational vs statistical vs perfect ZK. |
| 7 | Commitment Schemes | Math. Pedersen Commitment: C = g^v * h^r where g,h generators of group G of prime order q, v is value, r is randomness. Properties: Perfectly Hiding (information-theoretically), Computationally Binding (under DLog assumption). Table: Pedersen vs Hash-based commitments. |
| 8 | Sigma Protocols: Schnorr's Protocol | TikZ diagram. Three-move protocol: Prover sends commitment a = g^k, Verifier sends challenge e, Prover responds z = k + ex. Verification: g^z = a * y^e. Proof of knowledge of discrete log. SHVZK property. |
| 9 | Polynomial Commitments (KZG) | Math-heavy. Kate-Zaverucha-Goldberg scheme. Commit to polynomial p(x) using elliptic curve pairings: C = [p(s)]_1 where s is secret from trusted setup. Evaluation proof: pi = [(p(s)-p(z))/(s-z)]_1. Verification via pairing: e(C - [p(z)]_1, [1]_2) = e(pi, [s-z]_2). |
| 10 | Arithmetic Circuits | TikZ circuit diagram. How computation is represented as addition and multiplication gates over a finite field F_p. Example: prove x^3 + x + 5 = 35 without revealing x=3. Circuit: input wire x, multiplication gates, addition gates, output wire. R1CS (Rank-1 Constraint System) representation. |
| 11 | From Circuits to R1CS | Math. Constraint format: a_i . s * b_i . s = c_i . s for witness vector s. Example worked through: x^3 + x + 5 = 35 decomposed into intermediate variables and constraints. Matrix representation A, B, C. |
| 12 | QAP: Quadratic Arithmetic Programs | Math. Transform R1CS to QAP via Lagrange interpolation. Polynomials A_j(x), B_j(x), C_j(x) encode constraints. Key equation: A(x) * B(x) - C(x) = H(x) * Z(x) where Z(x) is vanishing polynomial. This is what SNARKs actually prove. |
| 13 | Information-Theoretic Security vs Computational Security | Two-column comparison. Information-theoretic: secure against unbounded adversary, no assumptions, perfect/statistical ZK. Computational: secure against PPT adversaries, relies on hardness assumptions (DLog, pairings), computational ZK. Table: which proof systems achieve which level. |
| 14 | Section 1 Summary | Recap slide with key formulas and concepts in structured boxes. |

### Section 2: Proof Systems -- SNARKs, STARKs, Bulletproofs (~11 frames, Frames 15-25)

| Frame | Title | Content Type |
|-------|-------|-------------|
| 15 | Taxonomy of Proof Systems | TikZ tree diagram. Root: ZK Proof Systems. Branch 1: Interactive (Sigma protocols). Branch 2: Non-Interactive. Under NIZK: SNARKs (Groth16, PLONK, Marlin), STARKs (FRI-based), Bulletproofs (range proofs). Key differentiators: trusted setup, proof size, prover time, verifier time. |
| 16 | Groth16: The Classic SNARK | Math + diagram. Trusted setup produces CRS (toxic waste problem). Proof = 3 group elements (~200 bytes). Verification = 3 pairings. Pairing equation: e(A, B) = e(alpha, beta) * e(C, delta) * product. Table: Groth16 concrete numbers. |
| 17 | The Trusted Setup Ceremony | TikZ illustration. Multi-party computation: each participant contributes randomness, multiplies into CRS, destroys their share. "Powers of Tau" ceremony. Security: only ONE honest participant needed. Risk: if ALL collude, can forge proofs. Zcash Sprout vs Sapling ceremonies. |
| 18 | PLONK: Universal SNARKs | Math. Universal and updatable SRS. Permutation argument. Custom gates. Key advantage: single trusted setup for all circuits (vs Groth16's per-circuit setup). Gate equation: q_L*a + q_R*b + q_O*c + q_M*a*b + q_C = 0. Copy constraints via permutation polynomial. |
| 19 | STARKs: Transparent Proofs | Math + diagram. No trusted setup -- uses public randomness (hash functions only). FRI (Fast Reed-Solomon Interactive Oracle Proof) protocol. Proof of Low Degree Testing. Proof size ~45-200KB but verification O(log^2 n). Post-quantum secure (no elliptic curves). |
| 20 | FRI Protocol Deep Dive | Math. Polynomial commitment via Merkle trees + folding. Split polynomial p(x) = p_even(x^2) + x*p_odd(x^2). Recursive folding reduces degree by half each round. Verification: Merkle path checks + consistency checks. Visual: folding diagram showing degree reduction. |
| 21 | Bulletproofs: No Trusted Setup, Small Proofs | Math. Inner product argument. Proof size O(log n). No trusted setup. Used in Monero for range proofs. Key equation: prove knowledge of vectors a, b such that <a,b> = c and commit(a), commit(b). Recursive halving protocol. |
| 22 | Proof Systems Comparison | Large comparison table. Columns: Groth16, PLONK, STARKs, Bulletproofs. Rows: Trusted Setup, Proof Size, Prover Time, Verifier Time, Post-Quantum, Used By. Fill with concrete numbers where possible. |
| 23 | Recursive Proofs & Proof Composition | Concept diagram. Proving that a proof is valid inside another proof. Nova folding scheme. IVC (Incrementally Verifiable Computation). Application: blockchain light clients, accumulation schemes. |
| 24 | ZK Proof Verification in Solidity | **Solidity snippet #1.** Groth16 verifier contract showing pairing precompile usage (ecPairing at 0x08). Show verifyProof function with proof struct and public inputs. ~25-30 lines. |
| 25 | Section 2 Summary | Recap table + key insight boxes. |

### Section 3: Privacy Coins -- Monero, Zcash, Comparison (~11 frames, Frames 26-36)

| Frame | Title | Content Type |
|-------|-------|-------------|
| 26 | Why Blockchain Privacy Matters | Two-column. Left: Bitcoin's pseudonymity problem -- chain analysis, address clustering, exchange KYC links. Right: Privacy as fundamental right vs regulatory concerns. Chainalysis stats on Bitcoin traceability. |
| 27 | Ring Signatures | Math + TikZ. Concept: sign message on behalf of a group, verifier knows someone in group signed but not who. CryptoNote ring signature construction. Diagram: ring of n public keys, actual signer hidden among decoys. Linkability tag prevents double-spending. |
| 28 | Stealth Addresses | Math + diagram. One-time destination addresses. Diffie-Hellman key exchange: sender generates R = rG, receiver computes shared secret P = H(rA)G + B. Only receiver can detect and spend. Used in Monero for receiver privacy. |
| 29 | RingCT: Confidential Transactions | Math. Pedersen commitment to hide transaction amounts: C = aH + bG. Range proofs (Bulletproofs) prove amount is positive without revealing it. Homomorphic property: C(a) + C(b) = C(a+b). Monero's implementation. |
| 30 | Monero Architecture | Comprehensive diagram. Full stack: ring signatures (sender privacy) + stealth addresses (receiver privacy) + RingCT (amount privacy) + Dandelion++ (network privacy). Transaction flow from construction to mining. Default privacy for all transactions. |
| 31 | Zcash: zk-SNARKs for Privacy | Diagram + math. Shielded pool architecture. JoinSplit (Sprout) vs Spend/Output (Sapling) vs Action (Orchard). Note commitment tree. Nullifier set for double-spend prevention. Turnstile mechanism between transparent and shielded pools. |
| 32 | Zcash Circuit Design | Math. What the Sapling circuit proves: spending note exists in commitment tree, nullifier correctly derived, value balance preserved, signature authorization. Circuit constraints ~100K. Groth16 proof generation. |
| 33 | Monero vs Zcash: Detailed Comparison | Large comparison table. Rows: Privacy Model (default vs opt-in), Cryptographic Basis (ring sigs vs SNARKs), Trusted Setup (no vs yes), Transaction Size (~2KB vs ~2KB shielded), Scalability, Regulatory Response, Adoption, Auditability. |
| 34 | Other Privacy Solutions | Overview. Tornado Cash (Ethereum mixer, OFAC sanctions), Railgun (on-chain privacy), Secret Network (encrypted smart contracts), Aztec (ZK-rollup with privacy), Mina (succinct blockchain). Brief description of each approach. |
| 35 | Privacy Mixer Solidity Pattern | **Solidity snippet #2.** Simplified deposit/withdraw pattern inspired by Tornado Cash. Merkle tree of commitments, nullifier hash for withdrawal, ZK proof verification. ~30 lines showing the interface/core logic. |
| 36 | Section 3 Summary | Recap with comparison matrix. |

### Section 4: ZK Applications -- Rollups, Identity, Voting, DeFi (~11 frames, Frames 37-47)

| Frame | Title | Content Type |
|-------|-------|-------------|
| 37 | ZK-Rollups: Architecture | Comprehensive diagram. L2 operator collects transactions, builds state tree, generates ZK proof of correct state transition, posts proof + state root on L1. Sequencer, prover, verifier contract. Data availability: calldata vs blobs (EIP-4844). |
| 38 | zkEVM: Types and Tradeoffs | Table + diagram. Vitalik's zkEVM types: Type 1 (fully Ethereum-equivalent), Type 2 (EVM-equivalent), Type 2.5 (EVM-equivalent with gas cost changes), Type 3 (almost EVM-equivalent), Type 4 (language-equivalent). Projects mapped: Taiko (T1), Scroll/Polygon (T2), zkSync (T4). |
| 39 | ZK-Rollup State Verification | Math. State transition function: S_{n+1} = STF(S_n, T_n). ZK proof proves: starting from committed state root R_n, applying transactions T_n, produces new state root R_{n+1}. Verification on L1: check proof against public inputs (old root, new root, tx data hash). |
| 40 | ZK-Rollup Verifier Contract | **Solidity snippet #3.** L1 verifier contract that accepts proofs and updates state root. Show: state root storage, verifyBatch function, proof verification call, state root update. ~25-30 lines. |
| 41 | Zero-Knowledge Identity (Self-Sovereign) | Diagram. Prove attributes about yourself (age >= 18, citizen of country X, credit score > 700) without revealing the actual values. W3C Verifiable Credentials + ZK proofs. Issuer -> Holder -> Verifier flow. Selective disclosure. |
| 42 | ZK Voting Systems | Diagram + concept. Requirements: eligibility verification, vote privacy, tally correctness, coercion resistance. MACI (Minimum Anti-Collusion Infrastructure): encrypt votes with coordinator key, ZK proof of correct tally. Prevent bribery/coercion. |
| 43 | Private DeFi | Overview. Private order books (prevent front-running/MEV), confidential token balances, private lending (hide collateral ratios), dark pools. Protocol examples: Penumbra, Aztec, Railgun. Tradeoffs: privacy vs composability vs auditability. |
| 44 | ZK Machine Learning (zkML) | Emerging field. Prove ML model inference was computed correctly without revealing model weights or input data. Applications: private AI, verifiable AI, model marketplace. Current limitations: proving large neural networks is extremely expensive. |
| 45 | ZK Bridges | Diagram. Cross-chain verification using ZK proofs. Prove state of chain A on chain B without running full node. Light client proofs. Examples: zkBridge, Succinct, Polyhedra. Security advantage over multisig bridges. |
| 46 | ZK Coprocessors | Concept. Offload heavy computation from smart contracts, prove correctness with ZK. Axiom, RISC Zero, Brevis. Pattern: query historical blockchain data, compute off-chain, verify ZK proof on-chain. Access any historical state cheaply. |
| 47 | Section 4 Summary | Recap all applications in structured grid. |

### Section 5: Advanced Topics & Future Directions (~8 frames, Frames 48-55)

| Frame | Title | Content Type |
|-------|-------|-------------|
| 48 | Proving System Frontiers | Current research: Lasso/Jolt (lookup-based), HyperNova (folding), Binius (binary fields), Circle STARKs. Trend toward faster provers and smaller proofs. |
| 49 | Hardware Acceleration | GPU proving, FPGA/ASIC provers, distributed proving networks. Projects: Ingonyama, Cysic, Ulvetanna. Prover cost economics. Goal: real-time proving for consumer applications. |
| 50 | Post-Quantum ZK | Lattice-based commitments, hash-based SNARKs (STARKs already post-quantum). Preparing for quantum computers. NIST standardization impact on ZK systems. |
| 51 | Regulatory & Ethical Dimensions | Privacy vs compliance tension. Travel Rule, FATF guidance, OFAC sanctions (Tornado Cash). Selective disclosure as middle ground. Compliance-friendly privacy: proof of non-inclusion in sanctions list. |
| 52 | ZK Developer Ecosystem | **Solidity snippet #4 (optional).** Overview of tools: Circom (circuit DSL), Noir (Aztec), Cairo (StarkNet), Halo2 (Zcash/Scroll), SP1 (RISC Zero). Short snippet showing a simple Circom circuit compiled to verifier. Alternatively, show a simple ZK proof generation call. |
| 53 | The Road Ahead | Predictions and open problems. Client-side proving on mobile, universal ZK (prove any computation), privacy-preserving compliance, ZK as internet infrastructure. Vision: "Verify, don't trust" extends to everything. |
| 54 | Course Summary & Key Takeaways | 6-box summary covering all 5 sections. Key formulas, key systems, key applications. |
| 55 | Questions & Discussion | Discussion prompts. Further reading: ZKP.science, Vitalik's blog posts, IACR ePrint, RareSkills ZK Book. |

### Solidity Snippets Summary (3-4 total)

| # | Location | Content | Lines |
|---|----------|---------|-------|
| 1 | Frame 24 (Section 2) | Groth16 verifier contract with pairing precompile | ~25-30 |
| 2 | Frame 35 (Section 3) | Privacy mixer deposit/withdraw pattern | ~25-30 |
| 3 | Frame 40 (Section 4) | ZK-Rollup L1 verifier contract | ~25-30 |
| 4 | Frame 52 (Section 5, optional) | Circom-to-Solidity or simple proof call | ~15-20 |

## Deliverable 3: Quizzes (4 HTML files, 20 questions each)

**Template:** Clone exact structure from `quiz/quiz_tm_part1.html`. Same CSS, same nav, same JS quiz engine. Only change: quiz data, title, nav text, color accent.

### Quiz ZK-1: ZK Proof Foundations (20 questions)

Topics: ZK definition, completeness/soundness/zero-knowledge, interactive vs non-interactive, commitment schemes, Pedersen commitments, Schnorr protocol, sigma protocols, polynomial commitments, arithmetic circuits, R1CS, QAP, Fiat-Shamir heuristic, simulation paradigm, information-theoretic vs computational security, common reference string, witness, prover/verifier model, GMR paper history, NP languages.

Question IDs: `zk1_q1` through `zk1_q20`.

### Quiz ZK-2: Proof Systems (20 questions)

Topics: Groth16 specifics, PLONK universal SRS, STARK transparency, FRI protocol, Bulletproofs inner product, trusted setup ceremonies, powers of tau, toxic waste, proof sizes, verification times, prover complexity, recursive proofs, Nova folding, pairing-based vs hash-based, Kate commitments, permutation arguments, custom gates, lookup arguments, proof composition, IVC.

Question IDs: `zk2_q1` through `zk2_q20`.

### Quiz ZK-3: Privacy Coins (20 questions)

Topics: Ring signatures, stealth addresses, RingCT, Monero architecture, Zcash shielded pools, JoinSplit vs Sapling vs Orchard, nullifiers, note commitments, Monero vs Zcash tradeoffs, Tornado Cash, mixers, chain analysis, pseudonymity vs anonymity, default vs opt-in privacy, transaction sizes, regulatory landscape, OFAC sanctions, Dandelion++, privacy pools, selective disclosure.

Question IDs: `zk3_q1` through `zk3_q20`.

### Quiz ZK-4: ZK Applications & Future (20 questions)

Topics: ZK-rollup architecture, zkEVM types, state transition proofs, data availability, ZK identity, self-sovereign identity, ZK voting (MACI), private DeFi, zkML, ZK bridges, ZK coprocessors, hardware acceleration, post-quantum ZK, lattice-based schemes, Circom/Noir/Cairo, developer tools, regulatory challenges, prover economics, client-side proving, future directions.

Question IDs: `zk4_q1` through `zk4_q20`.

### Quiz HTML Structure (per file)

```
Title: "Quiz ZK-{N}: {Subtitle} | Build Your Own Cryptocurrency"
Nav title: "Build Your Own Cryptocurrency"
Nav links: Home (../index.html), Quiz ZK-1..4 (relative links)
Color accent: --quiz-accent: #0d9488 (teal to match d13)
Quiz data: const quizData = { questions: [ { id, question, options: {A,B,C,D}, correct, explanation }, ... ] }
20 questions per file, 4 options each, explanation for correct answer
```

## Deliverable 4: GH Pages Update (`index.html`)

### CSS Additions

Add d13 class styles after the existing d12 styles:

```css
.section-head.d13 span{background:#0d9488}
.d13 summary{border-left:3px solid #0d9488}
```

### Sidebar Navigation

Add under the existing `</details>` for TM entries:

```html
<a href="#sl-zk-mini">Mini-Lecture: Privacy & ZK</a>
<a href="#sl-zk-main">ZK Technical Lecture</a>
```

### Lecture Section

Add new section after the TM section (after line ~762 in current index.html), before the Notebooks section:

```html
<div class="section-head d13" style="margin-top:16px"><span>ZK</span><h2>Standalone Lectures: Privacy & Zero-Knowledge Proofs</h2></div>
<div class="lec-grid">
  <a href="lectures/privacy_zk_proofs_intro.pdf" class="lec-card" style="border-left-color:#0d9488" id="sl-zk-mini">
    <div class="lec-tag mini">Mini-Lecture</div>
    <h3>Privacy & ZK Proofs: Visual Introduction</h3>
    <p>10 frames &bull; TikZ comics &bull; Zero code</p>
  </a>
  <a href="lectures/privacy_zk_proofs.pdf" class="lec-card" style="border-left-color:#0d9488" id="sl-zk-main">
    <div class="lec-tag main">Technical Lecture</div>
    <h3>Privacy & ZK Proofs: From Theory to Application</h3>
    <p>~55 frames &bull; Proof systems, privacy coins, ZK-rollups, deep math</p>
  </a>
</div>
```

### Quiz Section

Add 4 quiz cards after the lecture cards:

```html
<div class="quiz-grid">
  <a href="quiz/quiz_zk_part1.html" class="quiz-card" style="border-left-color:#0d9488">
    <div class="quiz-tag">Quiz ZK-1</div>
    <h3>ZK Proof Foundations</h3>
    <p>20 questions &bull; Definitions, commitments, circuits, R1CS</p>
  </a>
  <a href="quiz/quiz_zk_part2.html" class="quiz-card" style="border-left-color:#0d9488">
    <div class="quiz-tag">Quiz ZK-2</div>
    <h3>Proof Systems</h3>
    <p>20 questions &bull; Groth16, PLONK, STARKs, Bulletproofs</p>
  </a>
  <a href="quiz/quiz_zk_part3.html" class="quiz-card" style="border-left-color:#0d9488">
    <div class="quiz-tag">Quiz ZK-3</div>
    <h3>Privacy Coins</h3>
    <p>20 questions &bull; Monero, Zcash, ring signatures, shielded pools</p>
  </a>
  <a href="quiz/quiz_zk_part4.html" class="quiz-card" style="border-left-color:#0d9488">
    <div class="quiz-tag">Quiz ZK-4</div>
    <h3>ZK Applications & Future</h3>
    <p>20 questions &bull; Rollups, identity, voting, zkML, regulation</p>
  </a>
</div>
```

### Hero Stats Update

Update the Lectures count from `42` to `44` and Quizzes count from `48` to `52`.

## Implementation Order

| Step | Task | Depends On |
|------|------|------------|
| 1 | Create `lectures/privacy_zk_proofs_intro.tex` (mini-lecture) | None |
| 2 | Create `lectures/privacy_zk_proofs.tex` (technical lecture) | None |
| 3 | Create `quiz/quiz_zk_part1.html` | None |
| 4 | Create `quiz/quiz_zk_part2.html` | None |
| 5 | Create `quiz/quiz_zk_part3.html` | None |
| 6 | Create `quiz/quiz_zk_part4.html` | None |
| 7 | Update `index.html` (CSS + sidebar + sections + stats) | Steps 1-6 |

Steps 1-6 are independent and can be parallelized. Step 7 depends on all previous steps being complete.

## Acceptance Criteria

- [ ] Mini-lecture compiles with pdflatex, produces exactly 10 frames
- [ ] Mini-lecture uses only TikZ for visuals, zero code/lstlisting
- [ ] Technical lecture compiles with pdflatex, produces ~55 frames
- [ ] Technical lecture has exactly 5 `\section{}` commands matching the defined sections
- [ ] Technical lecture contains 3-4 Solidity `lstlisting` blocks (no more)
- [ ] Technical lecture is theory-heavy with deep math (polynomial commitments, circuit design, proof system comparisons, information-theoretic security)
- [ ] Each quiz has exactly 20 questions with id prefix `zk{N}_q{M}`
- [ ] Each quiz question has 4 options (A-D), one correct answer, and an explanation
- [ ] Quiz HTML files use teal accent color `#0d9488`
- [ ] `index.html` has d13 CSS classes with color `#0d9488`
- [ ] `index.html` sidebar has ZK navigation entries
- [ ] `index.html` has ZK lecture section with 2 lecture cards + 4 quiz cards
- [ ] `index.html` hero stats updated (Lectures: 44, Quizzes: 52)
- [ ] All links in `index.html` point to correct file paths

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| LaTeX compilation errors from complex math | Use standard amsmath commands; test all `$...$` inline math and `\[...\]` display math |
| TikZ complexity in mini-lecture | Follow L12 panel layout exactly; keep coordinate systems consistent |
| Math notation inconsistency | Use consistent notation throughout (bold for vectors, calligraphic for sets, standard crypto notation) |
| Solidity snippets too long | Hard limit each to ~30 lines; use comments to indicate omitted sections |
| Quiz questions too easy/hard | Mix difficulty: ~5 easy, ~10 medium, ~5 hard per quiz; include both definitional and analytical questions |
| Index.html edit breaks existing content | Only add new CSS classes and HTML sections; do not modify existing entries |

## Commit Strategy

Single commit after all 7 files are created/updated:

```
Add L13 Privacy & Zero-Knowledge Proofs standalone lectures, quizzes, and GH Pages
```
