# Cryptocurrency Course Plan
## BSc-Level: Build Your Own Cryptocurrency (4 Lessons)

---

## Context

### Original Request
Create a comprehensive 4-lesson course plan for BSc-level students with the ultimate goal of building their own cryptocurrency (ERC-20 token on Ethereum).

### Interview Summary
| Preference | Decision |
|------------|----------|
| **Languages** | Python (fundamentals) + Solidity (smart contracts) |
| **Platform** | Ethereum/EVM - Deploy ERC-20 token |
| **Format** | LaTeX slides (.tex) using `template_beamer_final.tex` + GitHub Pages |
| **Crypto Depth** | Moderate - implement basics in Python, understand mechanics |
| **Deployment** | Local development core + optional testnet section |
| **Duration** | 45 minutes per lesson (compact, focused) |
| **Assessment** | None to create - user provides 5 PDFs + final report |

### Reference Structure
Mirroring `D:\Joerg\Research\slides\Probability_Statistics\`:
- Lesson folders: `01_blockchain_fundamentals/`, `02_cryptography/`, etc.
- Each folder contains: `XX_name.tex`, `XX_name.pdf`, charts subfolder
- Root: `index.html` (GitHub Pages), `template_beamer_final.tex` (copy from parent)
- Notes folder: `notes/L0X_name_notes.tex`

---

## Repository Structure

```
cryptocurrency/
|
|-- index.html                              # GitHub Pages landing page
|-- template_beamer_final.tex               # Beamer template (copy from Probability_Statistics)
|-- README.md                               # Course overview
|
|-- 01_blockchain_fundamentals/
|   |-- 01_blockchain_fundamentals.tex      # Lesson 1 slides
|   |-- 01_blockchain_fundamentals.pdf      # Compiled slides
|   |-- code/
|   |   |-- simple_blockchain.py            # Python blockchain implementation
|   |   |-- block.py                        # Block class
|   |   |-- blockchain.py                   # Blockchain class
|   |   `-- requirements.txt
|   |-- 01_blockchain_structure/            # Chart: blockchain visualization
|   |   |-- 01_blockchain_structure.pdf
|   |   |-- 01_blockchain_structure.py
|   |   `-- thumb.png
|   |-- 02_hash_chain/                      # Chart: hash linking visualization
|   |-- 03_merkle_tree/                     # Chart: merkle tree
|   |-- 04_consensus_comparison/            # Chart: PoW vs PoS
|   `-- 05_decentralization/                # Chart: centralized vs decentralized
|
|-- 02_cryptography_security/
|   |-- 02_cryptography_security.tex
|   |-- 02_cryptography_security.pdf
|   |-- code/
|   |   |-- hashing_demo.py                 # SHA-256 demonstrations
|   |   |-- digital_signatures.py           # ECDSA implementation
|   |   |-- wallet_demo.py                  # Key generation demo
|   |   `-- requirements.txt
|   |-- 01_hash_function/                   # Chart: hash function properties
|   |-- 02_sha256_avalanche/                # Chart: avalanche effect
|   |-- 03_public_private_keys/             # Chart: key pair visualization
|   |-- 04_digital_signature_flow/          # Chart: sign/verify process
|   `-- 05_wallet_architecture/             # Chart: wallet components
|
|-- 03_ethereum_smart_contracts/
|   |-- 03_ethereum_smart_contracts.tex
|   |-- 03_ethereum_smart_contracts.pdf
|   |-- code/
|   |   |-- SimpleStorage.sol               # Basic Solidity contract
|   |   |-- HelloWorld.sol                  # First contract
|   |   |-- web3_interact.py                # Python web3 interaction
|   |   `-- hardhat.config.js               # Hardhat configuration
|   |-- 01_ethereum_architecture/           # Chart: EVM stack
|   |-- 02_gas_mechanics/                   # Chart: gas calculation
|   |-- 03_smart_contract_lifecycle/        # Chart: deploy/interact flow
|   |-- 04_solidity_types/                  # Chart: data types
|   `-- 05_contract_interaction/            # Chart: call vs transaction
|
|-- 04_erc20_token_creation/
|   |-- 04_erc20_token_creation.tex
|   |-- 04_erc20_token_creation.pdf
|   |-- code/
|   |   |-- MyToken.sol                     # Complete ERC-20 token
|   |   |-- deploy.js                       # Deployment script
|   |   |-- test_token.py                   # Token testing
|   |   |-- hardhat.config.js
|   |   `-- package.json
|   |-- 01_erc20_interface/                 # Chart: ERC-20 methods
|   |-- 02_token_flow/                      # Chart: transfer mechanics
|   |-- 03_approval_allowance/              # Chart: approve/transferFrom
|   |-- 04_deployment_steps/                # Chart: deployment workflow
|   `-- 05_token_economics/                 # Chart: supply/distribution
|
|-- notes/
|   |-- L01_blockchain_fundamentals_notes.tex
|   |-- L02_cryptography_security_notes.tex
|   |-- L03_ethereum_smart_contracts_notes.tex
|   `-- L04_erc20_token_creation_notes.tex
|
|-- assessments/                            # User-provided PDFs go here
|   |-- README.md                           # Instructions for assessments
|   `-- final_report_template.md            # Template for final project report
|
|-- project/                                # Final project scaffold
|   |-- README.md                           # Project instructions
|   |-- contracts/
|   |   `-- StudentToken.sol                # Template for student token
|   |-- scripts/
|   |   `-- deploy.js                       # Deployment script template
|   |-- test/
|   |   `-- Token.test.js                   # Test suite template
|   `-- hardhat.config.js
|
`-- .github/
    `-- workflows/
        `-- pages.yml                       # GitHub Pages deployment
```

---

## Lesson Breakdown

### Lesson 1: Blockchain Fundamentals (45 min)
**File:** `01_blockchain_fundamentals/01_blockchain_fundamentals.tex`

#### Learning Objectives
By the end of this lesson, students will be able to:
1. Define blockchain and explain its core properties (immutability, transparency, decentralization)
2. Describe the structure of a block (header, transactions, hash, previous hash)
3. Explain how blocks form a chain through cryptographic linking
4. Compare centralized vs. decentralized systems
5. Implement a simple blockchain in Python (10-15 lines)

#### Topics (45 min allocation)
| Time | Topic | Content |
|------|-------|---------|
| 0-8 min | What is Blockchain? | History (Bitcoin 2008), definition, real-world applications |
| 8-18 min | Block Structure | Header, body, hash, nonce, timestamp, Merkle root |
| 18-25 min | Chain Formation | Hash linking, why tampering breaks the chain |
| 25-32 min | Consensus Mechanisms | PoW vs PoS overview (brief - not deep dive) |
| 32-40 min | Python Demo | Build simple blockchain in Python (live coding) |
| 40-45 min | Summary & Preview | Key takeaways, preview of cryptography lesson |

#### Charts to Generate
1. `01_blockchain_structure/` - Visual of block components
2. `02_hash_chain/` - How blocks link via hashes
3. `03_merkle_tree/` - Transaction verification structure
4. `04_consensus_comparison/` - PoW vs PoS visual comparison
5. `05_decentralization/` - Centralized vs decentralized network diagram

#### Code Deliverables
- `simple_blockchain.py` - Complete working blockchain (~50 lines)
- `block.py` - Block class with hash calculation
- `blockchain.py` - Chain management with validation

---

### Lesson 2: Cryptography for Blockchain (45 min)
**File:** `02_cryptography_security/02_cryptography_security.tex`

#### Learning Objectives
By the end of this lesson, students will be able to:
1. Explain hash functions and their properties (deterministic, one-way, collision-resistant)
2. Demonstrate the avalanche effect in SHA-256
3. Describe public/private key cryptography (asymmetric encryption)
4. Explain digital signatures and their role in transactions
5. Create a simple wallet (key pair generation) in Python

#### Topics (45 min allocation)
| Time | Topic | Content |
|------|-------|---------|
| 0-10 min | Hash Functions | SHA-256, properties, why blockchains need them |
| 10-15 min | Avalanche Effect | Demo: tiny input change = completely different hash |
| 15-25 min | Public Key Cryptography | Key pairs, asymmetric encryption basics |
| 25-35 min | Digital Signatures | ECDSA, signing transactions, verification |
| 35-42 min | Wallet Demo | Generate keys, derive address in Python |
| 42-45 min | Summary | How crypto enables trustless transactions |

#### Charts to Generate
1. `01_hash_function/` - Input -> Hash -> Output diagram
2. `02_sha256_avalanche/` - Side-by-side hash comparison
3. `03_public_private_keys/` - Key pair relationship visual
4. `04_digital_signature_flow/` - Sign/Verify process flow
5. `05_wallet_architecture/` - Wallet components diagram

#### Code Deliverables
- `hashing_demo.py` - SHA-256 examples with hashlib
- `digital_signatures.py` - ECDSA sign/verify with ecdsa library
- `wallet_demo.py` - Key generation, address derivation

---

### Lesson 3: Ethereum & Smart Contracts (45 min)
**File:** `03_ethereum_smart_contracts/03_ethereum_smart_contracts.tex`

#### Learning Objectives
By the end of this lesson, students will be able to:
1. Explain how Ethereum differs from Bitcoin (smart contracts, EVM)
2. Describe the Ethereum Virtual Machine (EVM) and gas
3. Write a basic Solidity smart contract
4. Understand contract deployment and interaction
5. Use Python web3 library to interact with contracts

#### Topics (45 min allocation)
| Time | Topic | Content |
|------|-------|---------|
| 0-8 min | Ethereum vs Bitcoin | World computer concept, Turing-complete |
| 8-15 min | EVM & Gas | How code executes, gas costs, why gas exists |
| 15-25 min | Solidity Basics | Data types, functions, visibility, state variables |
| 25-35 min | Write First Contract | SimpleStorage.sol - store and retrieve a number |
| 35-42 min | Deploy & Interact | Hardhat local, Python web3 interaction |
| 42-45 min | Summary | Preview of ERC-20 token creation |

#### Charts to Generate
1. `01_ethereum_architecture/` - EVM stack diagram
2. `02_gas_mechanics/` - Gas price, limit, fee calculation
3. `03_smart_contract_lifecycle/` - Write -> Compile -> Deploy -> Interact
4. `04_solidity_types/` - Data types cheat sheet
5. `05_contract_interaction/` - Call vs Transaction diagram

#### Code Deliverables
- `HelloWorld.sol` - Simplest possible contract
- `SimpleStorage.sol` - Store/retrieve value
- `web3_interact.py` - Python script to deploy and call contract
- `hardhat.config.js` - Local development setup

---

### Lesson 4: Create Your ERC-20 Token (45 min)
**File:** `04_erc20_token_creation/04_erc20_token_creation.tex`

#### Learning Objectives
By the end of this lesson, students will be able to:
1. Explain the ERC-20 token standard and its required functions
2. Implement a complete ERC-20 token in Solidity
3. Deploy the token to a local blockchain
4. Transfer tokens and check balances
5. (Optional Advanced) Deploy to Sepolia testnet

#### Topics (45 min allocation)
| Time | Topic | Content |
|------|-------|---------|
| 0-8 min | Token Standards | Why standards matter, ERC-20 interface |
| 8-15 min | ERC-20 Functions | totalSupply, balanceOf, transfer, approve, transferFrom |
| 15-25 min | Build MyToken.sol | Implement all required functions |
| 25-35 min | Deploy & Test | Local deployment, transfer tokens, check balances |
| 35-42 min | Token Economics | Supply models, distribution, real-world examples |
| 42-45 min | Next Steps | Optional testnet deployment, further learning |

#### Charts to Generate
1. `01_erc20_interface/` - All 6 required functions diagram
2. `02_token_flow/` - transfer() mechanics visualization
3. `03_approval_allowance/` - approve/transferFrom flow (DEX pattern)
4. `04_deployment_steps/` - Full deployment workflow
5. `05_token_economics/` - Supply types (fixed, inflationary, deflationary)

#### Code Deliverables
- `MyToken.sol` - Complete ERC-20 implementation
- `deploy.js` - Hardhat deployment script
- `test_token.py` - Python test suite for token

#### Optional Advanced Section (for motivated students)
- Testnet deployment guide (Sepolia)
- MetaMask wallet setup
- Etherscan verification
- Faucet instructions

---

## Deliverables Summary

### Per-Lesson Deliverables
| Lesson | .tex File | Charts | Code Files |
|--------|-----------|--------|------------|
| L01 | 01_blockchain_fundamentals.tex | 5 | 3 Python files |
| L02 | 02_cryptography_security.tex | 5 | 3 Python files |
| L03 | 03_ethereum_smart_contracts.tex | 5 | 2 Solidity + 2 config |
| L04 | 04_erc20_token_creation.tex | 5 | 2 Solidity + 2 scripts |

### Total Deliverables
- **4 LaTeX slide decks** (using template_beamer_final.tex)
- **20 charts** (Python-generated, with thumbnails)
- **4 lecture notes** (notes/ folder)
- **1 GitHub Pages site** (index.html)
- **1 Final project scaffold** (project/ folder)
- **Code examples** per lesson

---

## Final Project Specification

### Project: Create Your Own Cryptocurrency

**Objective:** Students create a unique ERC-20 token with custom parameters.

**Requirements:**
1. **Token Contract** (StudentToken.sol)
   - Custom name and symbol
   - Defined total supply
   - All ERC-20 functions implemented
   - At least one custom feature (e.g., minting cap, burn function, pause)

2. **Deployment**
   - Successful deployment to local Hardhat network
   - (Optional) Deployment to Sepolia testnet

3. **Testing**
   - Transfer tokens between accounts
   - Check balances correctly update
   - Test approve/transferFrom flow

4. **Documentation**
   - Token economics explanation
   - Use case description
   - Technical choices rationale

**Submission:** User provides 5 PDFs + final report (no new assessments to create)

---

## GitHub Pages Structure (index.html)

Based on Probability_Statistics template:

```
Navigation Sidebar:
- I. Foundations (green)
  - 01 Blockchain Fundamentals
  - 02 Cryptography & Security
- II. Development (orange)
  - 03 Ethereum & Smart Contracts
  - 04 ERC-20 Token Creation

Main Content:
- Hero: "Build Your Own Cryptocurrency" / "BSc Course - 4 Lessons"
- Stats: "4 Lessons" | "20 Charts" | "1 Token"
- Lesson cards linking to PDFs
- Charts section with thumbnails
- Code downloads section
- Final project link
```

---

## Prerequisites

### Student Prerequisites
- Basic programming (any language, Python preferred)
- Understanding of data structures (lists, dictionaries)
- Comfort with command line
- No blockchain knowledge required

### Technical Setup
- Python 3.8+
- Node.js 16+ (for Hardhat)
- VS Code (recommended)
- MetaMask browser extension (optional, for testnet)

### Python Dependencies
```
hashlib (built-in)
ecdsa==0.18.0
web3==6.0.0
```

### Node Dependencies
```
hardhat
@openzeppelin/contracts
ethers
```

---

## Success Criteria

### Course Success
- [ ] All 4 lessons delivered within 45 minutes each
- [ ] Students can explain blockchain fundamentals
- [ ] Students can implement basic cryptographic operations in Python
- [ ] Students can write and deploy Solidity smart contracts
- [ ] Students successfully create their own ERC-20 token

### Technical Success
- [ ] All code examples run without errors
- [ ] Charts render correctly in LaTeX
- [ ] GitHub Pages site is functional
- [ ] Local deployment works on Hardhat

---

## Implementation Order

1. **Phase 1: Setup**
   - Copy template_beamer_final.tex to cryptocurrency/
   - Create folder structure
   - Initialize package.json for Hardhat

2. **Phase 2: Lesson 1**
   - Write 01_blockchain_fundamentals.tex
   - Create Python blockchain code
   - Generate 5 charts

3. **Phase 3: Lesson 2**
   - Write 02_cryptography_security.tex
   - Create crypto demo code
   - Generate 5 charts

4. **Phase 4: Lesson 3**
   - Write 03_ethereum_smart_contracts.tex
   - Create Solidity examples
   - Generate 5 charts

5. **Phase 5: Lesson 4**
   - Write 04_erc20_token_creation.tex
   - Create ERC-20 token code
   - Generate 5 charts

6. **Phase 6: Polish**
   - Create index.html (GitHub Pages)
   - Write lecture notes
   - Create final project scaffold
   - Test all code

---

## Notes

- **45-minute constraint**: Each lesson is tightly focused. Deep dives should be in supplementary materials or notes.
- **Assessment**: User will provide 5 PDFs + final report. No quiz HTML files needed.
- **LaTeX template**: Use exact same template as Probability_Statistics for visual consistency.
- **Charts**: Follow same structure (subfolder with .py, .pdf, thumb.png).
