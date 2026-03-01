# Work Plan: Colab Notebook Conversion (Revised)

## Context

### Original Request
Convert the .py scripts in the cryptocurrency course repository to Google Colab notebooks, following the pattern used in the Digital-AI-Finance/Digital-Finance-Introduction repository.

### Repository
- **Location:** `D:/Joerg/Research/slides/cryptocurrency`
- **GitHub:** `https://github.com/Digital-AI-Finance/Cryptocurrency`
- **Branch:** `main`

### Current State
The repository contains three categories of Python files:

**Category A: 20 Chart-Generating Scripts** (in `lesson/topic/` folders)
These use matplotlib to generate PDF/PNG diagrams for beamer presentation slides. Each draws fixed visualizations with hardcoded coordinates (FancyBboxPatch, Rectangle, text at pixel positions) and saves to PDF+PNG at dpi=300.

- **3 scripts with interactive potential** (use hashlib, numpy, or calculation models where students can change inputs and see different outputs):
  1. `02_cryptography_security/02_sha256_avalanche/02_sha256_avalanche.py` -- calls `hashlib.sha256()` on variable inputs; students can change input strings and see bit differences recalculate
  2. `04_erc20_token_creation/05_token_economics/05_token_economics.py` -- uses numpy for parametric supply curves; students can modify inflation rates, burn rates, supply values
  3. `03_ethereum_smart_contracts/02_gas_mechanics/02_gas_mechanics.py` -- contains calculation model (gas used x gas price); students can modify values and see cost changes

- **17 scripts that are purely static** (hardcoded coordinates, fixed text, no variable computation -- converting to notebooks adds zero educational value):
  `01_blockchain_structure`, `02_hash_chain`, `03_merkle_tree`, `04_consensus_comparison`, `05_decentralization`, `01_hash_function`, `03_public_private_keys`, `04_digital_signature_flow`, `05_wallet_architecture`, `01_ethereum_architecture`, `03_smart_contract_lifecycle`, `04_solidity_types`, `05_contract_interaction`, `01_erc20_interface`, `02_token_flow`, `03_approval_allowance`, `04_deployment_steps`

**Category B: 8 Code Demo Scripts** (in `lesson/code/` folders)
Standalone demos teaching blockchain concepts through executable code.

**Category C: 4 Existing Colab Notebooks** (in `notebooks/`)
Already cover ALL 8 code demos (Category B). Mapping confirmed:
- `notebooks/01_blockchain_fundamentals.ipynb` covers `block.py` + `blockchain.py` + `simple_blockchain.py`
- `notebooks/02_cryptography_security.ipynb` covers `hashing_demo.py` + `digital_signatures.py` + `wallet_demo.py`
- `notebooks/03_ethereum_contracts.ipynb` covers `web3_interact.py`
- `notebooks/04_erc20_tokens.ipynb` covers `test_token.py`

No new code demo notebooks are needed. All 8 scripts are fully covered.

**Category D: 20 PNG Images** (already generated alongside each chart script)
Every chart script has a companion `.png` file in the same directory, generated at dpi=300. These can be embedded directly in notebooks.

### Reference Pattern (Digital-Finance-Introduction)
- Notebooks in `day_XX/notebooks/` (per-lesson directories, not top-level)
- First cell: Colab badge as clickable HTML image link
- Naming: `NB01_Topic_Name.ipynb`, `NB02_Topic_Name.ipynb`
- Structure: Badge -> Title -> Learning Objectives -> Setup (`!pip install -q`) -> Sections (markdown + code) -> Exercises -> Takeaways
- NB numbering convention: sequential within each lesson directory, starting at NB01. The NB prefix distinguishes notebooks from other files and enables natural sort order.

### Interview Summary
- Scope decision: Only create notebooks for scripts with genuine interactive/educational value. Do NOT convert static diagram scripts that would just teach matplotlib patch placement.
- Backward compatibility: Keep old notebooks with a redirect cell at top pointing to new location. Update README links to new paths.
- Static diagrams: Embed as PNG images within the enhanced existing notebooks where relevant, using relative paths from the per-lesson directory.

---

## Work Objectives

### Core Objective
Enhance the 4 existing code demo notebooks to follow the reference pattern (per-lesson directories, Colab badges, structured sections). Create 3 new interactive notebooks for the 3 chart scripts that have genuine educational interactivity (one each for SHA-256 Avalanche, Gas Mechanics, and Token Economics). Embed static PNG diagrams within notebooks where they add context. Do NOT create notebooks for the 17 static diagram scripts.

### Deliverables
1. **4 ENHANCED existing notebooks** -- moved from top-level `notebooks/` to `{lesson}/notebooks/`, upgraded with Colab badge, learning objectives, and reference-pattern structure
2. **3 NEW interactive notebooks** -- SHA-256 Avalanche (Lesson 02), Gas Mechanics (Lesson 03), Token Economics (Lesson 04)
3. **Updated README.md** -- new notebook table reflecting per-lesson structure, fixed `yourusername` placeholder at line 67/69 and line 287
4. **Backward-compatible old notebooks** -- redirect cell added to each of the 4 original notebooks pointing to new locations
5. **Preserved .py files** -- all original scripts remain untouched

### Definition of Done
- [ ] All 7 notebooks open and run correctly in Google Colab (no errors)
- [ ] Each notebook has Colab badge as first cell with correct GitHub URL
- [ ] Each notebook follows the reference structure (Badge -> Title -> Objectives -> Setup -> Sections -> Exercises -> Takeaways)
- [ ] Interactive notebooks produce visualizations that update based on student input changes
- [ ] Code demo notebooks retain all existing content plus structural enhancements
- [ ] README.md updated with per-lesson notebook links, correct Colab badge URLs, and fixed GitHub URLs
- [ ] All original .py files remain untouched
- [ ] Old notebooks contain redirect cell pointing to new locations
- [ ] `!pip install -q` used consistently for ALL non-stdlib dependencies (matplotlib, numpy, ecdsa, web3)

---

## Must Have / Must NOT Have (Guardrails)

### MUST HAVE
- Colab badge as first markdown cell in every notebook (HTML `<a href>` format matching reference repo)
- Correct GitHub URLs: `https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/{path}`
- `%matplotlib inline` in interactive chart notebooks for Colab rendering
- `!pip install -q` safety net for ALL non-stdlib packages: matplotlib, numpy, ecdsa, web3 (Colab pre-installs most, but safety net ensures reliability)
- Remove all `__file__`-based path logic from notebook code cells
- Do NOT set explicit dpi in notebook `plt.subplots()` calls -- let matplotlib default handle screen display (source scripts use dpi=300 for print, which produces oversized images in notebooks)
- Learning objectives section in every notebook
- At least one exercise/TODO section per notebook
- Key takeaways section in every notebook
- NB numbering: NB01, NB02, etc. sequential within each lesson directory

### MUST NOT HAVE
- No modification of any existing .py file
- No notebooks for the 17 static diagram scripts (these teach matplotlib patch placement, not blockchain concepts)
- No hardcoded local file paths in notebooks
- No `os.path.abspath(__file__)` or `os.path.dirname(__file__)` patterns (these fail in Colab)
- No `dpi=300` in notebook figure creation (use default or dpi=100-150 for screen)
- No dependencies that require system-level installation (apt-get) unless absolutely necessary
- No changes to the beamer/LaTeX slide files
- No `plt.savefig()` in notebooks -- use `plt.show()` for inline display

---

## Code Demo to Notebook Mapping (Explicit)

This confirms that all 8 code demo scripts are already fully covered by the 4 existing notebooks. No new code demo notebooks are needed.

| Existing Notebook | Code Demo Scripts Covered | New Location |
|---|---|---|
| `notebooks/01_blockchain_fundamentals.ipynb` | `01_.../code/block.py`, `blockchain.py`, `simple_blockchain.py` | `01_blockchain_fundamentals/notebooks/NB01_Blockchain_Code_Demo.ipynb` |
| `notebooks/02_cryptography_security.ipynb` | `02_.../code/hashing_demo.py`, `digital_signatures.py`, `wallet_demo.py` | `02_cryptography_security/notebooks/NB01_Cryptography_Code_Demo.ipynb` |
| `notebooks/03_ethereum_contracts.ipynb` | `03_.../code/web3_interact.py` | `03_ethereum_smart_contracts/notebooks/NB01_Ethereum_Code_Demo.ipynb` |
| `notebooks/04_erc20_tokens.ipynb` | `04_.../code/test_token.py` | `04_erc20_token_creation/notebooks/NB01_ERC20_Code_Demo.ipynb` |

Since these are the primary (and in most lessons, the only) notebook per lesson, they are numbered NB01.

---

## Directory Structure After Completion

```
cryptocurrency/
  01_blockchain_fundamentals/
    notebooks/                                    # NEW directory
      NB01_Blockchain_Code_Demo.ipynb             # enhanced from notebooks/01_blockchain_fundamentals.ipynb
    01_blockchain_structure/                       # UNCHANGED (PNG used as embedded image)
    code/                                         # UNCHANGED
    ...

  02_cryptography_security/
    notebooks/                                    # NEW directory
      NB01_Cryptography_Code_Demo.ipynb           # enhanced from notebooks/02_cryptography_security.ipynb
      NB02_SHA256_Avalanche_Interactive.ipynb      # NEW interactive notebook
    02_sha256_avalanche/                          # UNCHANGED (source .py stays)
    ...

  03_ethereum_smart_contracts/
    notebooks/                                    # NEW directory
      NB01_Ethereum_Code_Demo.ipynb               # enhanced from notebooks/03_ethereum_contracts.ipynb
      NB02_Gas_Mechanics_Interactive.ipynb         # NEW interactive notebook
    02_gas_mechanics/                             # UNCHANGED (source .py stays)
    ...

  04_erc20_token_creation/
    notebooks/                                    # NEW directory
      NB01_ERC20_Code_Demo.ipynb                  # enhanced from notebooks/04_erc20_tokens.ipynb
      NB02_Token_Economics_Interactive.ipynb       # NEW interactive notebook
    05_token_economics/                           # UNCHANGED (source .py stays)
    ...

  notebooks/                                     # KEPT for backward compatibility
    01_blockchain_fundamentals.ipynb              # redirect cell added at top
    02_cryptography_security.ipynb                # redirect cell added at top
    03_ethereum_contracts.ipynb                   # redirect cell added at top
    04_erc20_tokens.ipynb                         # redirect cell added at top
```

---

## Task Flow and Dependencies

```
Phase 1: Setup (no dependencies)
  T1: Create 4 lesson/notebooks/ directories

Phase 2: Enhance Existing Notebooks (parallel across lessons, depends on T1)
  T2: Move + enhance 01_blockchain_fundamentals.ipynb -> NB01_Blockchain_Code_Demo.ipynb
  T3: Move + enhance 02_cryptography_security.ipynb -> NB01_Cryptography_Code_Demo.ipynb
  T4: Move + enhance 03_ethereum_contracts.ipynb -> NB01_Ethereum_Code_Demo.ipynb
  T5: Move + enhance 04_erc20_tokens.ipynb -> NB01_ERC20_Code_Demo.ipynb

Phase 3: Create Interactive Notebooks (parallel, depends on T1)
  T6: Create NB02_SHA256_Avalanche_Interactive.ipynb (Lesson 02)
  T7: Create NB02_Gas_Mechanics_Interactive.ipynb (Lesson 03)
  T8: Create NB02_Token_Economics_Interactive.ipynb (Lesson 04)

Phase 4: Backward Compatibility + README (depends on T2-T8)
  T9: Add redirect cells to 4 old notebooks in notebooks/
  T10: Update README.md with new notebook table and fix placeholder URLs

Phase 5: Verification (depends on T9-T10)
  T11: Validate all Colab URLs are correct
```

---

## Detailed TODOs

### T1: Create Directory Structure
**Files to create:**
```
01_blockchain_fundamentals/notebooks/
02_cryptography_security/notebooks/
03_ethereum_smart_contracts/notebooks/
04_erc20_token_creation/notebooks/
```
**Acceptance:** All 4 directories exist.

---

### T2: Enhance and Move `01_blockchain_fundamentals.ipynb`
**Source:** `notebooks/01_blockchain_fundamentals.ipynb`
**Destination:** `01_blockchain_fundamentals/notebooks/NB01_Blockchain_Code_Demo.ipynb`
**Code demos covered:** `block.py`, `blockchain.py`, `simple_blockchain.py`

**Changes required:**
1. Insert Colab badge as first markdown cell:
   ```html
   <a href="https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/01_blockchain_fundamentals/notebooks/NB01_Blockchain_Code_Demo.ipynb">
     <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
   </a>
   ```
2. Add "Learning Objectives" section after the title cell:
   ```markdown
   ## Learning Objectives
   By the end of this notebook, you will:
   - Understand the structure of a blockchain block (index, timestamp, hash, nonce)
   - Implement SHA-256 hash calculation for blocks
   - Build a working Proof of Work mining algorithm
   - Create a complete blockchain with chain validation
   - Demonstrate blockchain immutability through tampering detection
   ```
3. Ensure setup cell includes `!pip install -q` for any non-stdlib dependencies (this notebook uses only `hashlib` and `time` -- stdlib only, so no pip needed, but add a comment noting this)
4. Verify "Key Takeaways" section exists (it does -- already present)
5. Retain all existing code cells and markdown unchanged
6. Optionally embed relevant static PNG diagrams (e.g., blockchain_structure.png, hash_chain.png) as reference images in markdown cells using relative paths:
   ```markdown
   ![Blockchain Structure](../01_blockchain_structure/01_blockchain_structure.png)
   ```

**Dependencies:** None (uses only `hashlib`, `time` -- stdlib)
**Acceptance:** Notebook runs without error in Colab, badge link is correct, structure matches reference pattern.

---

### T3: Enhance and Move `02_cryptography_security.ipynb`
**Source:** `notebooks/02_cryptography_security.ipynb`
**Destination:** `02_cryptography_security/notebooks/NB01_Cryptography_Code_Demo.ipynb`
**Code demos covered:** `hashing_demo.py`, `digital_signatures.py`, `wallet_demo.py`

**Changes required:**
1. Insert Colab badge (URL path: `02_cryptography_security/notebooks/NB01_Cryptography_Code_Demo.ipynb`)
2. Add "Learning Objectives" section
3. Ensure `!pip install -q ecdsa` is present in setup cell (already present -- verify)
4. Verify "Key Takeaways" section exists
5. Retain all existing content
6. Optionally embed static PNG diagrams (hash_function.png, public_private_keys.png, digital_signature_flow.png, wallet_architecture.png)

**Dependencies:** `ecdsa` (via pip)
**Acceptance:** Same as T2.

---

### T4: Enhance and Move `03_ethereum_contracts.ipynb`
**Source:** `notebooks/03_ethereum_contracts.ipynb`
**Destination:** `03_ethereum_smart_contracts/notebooks/NB01_Ethereum_Code_Demo.ipynb`
**Code demos covered:** `web3_interact.py`

**Changes required:**
1. Insert Colab badge (URL path: `03_ethereum_smart_contracts/notebooks/NB01_Ethereum_Code_Demo.ipynb`)
2. Add "Learning Objectives" section
3. Ensure `!pip install -q web3` is present in setup cell (already present -- verify)
4. Verify "Key Takeaways" section exists
5. Retain all existing content
6. Optionally embed static PNG diagrams (ethereum_architecture.png, smart_contract_lifecycle.png, solidity_types.png, contract_interaction.png)

**Dependencies:** `web3` (via pip); uses Sepolia testnet public RPC -- works in Colab
**Acceptance:** Same as T2.

---

### T5: Enhance and Move `04_erc20_tokens.ipynb`
**Source:** `notebooks/04_erc20_tokens.ipynb`
**Destination:** `04_erc20_token_creation/notebooks/NB01_ERC20_Code_Demo.ipynb`
**Code demos covered:** `test_token.py`

**Changes required:**
1. Insert Colab badge (URL path: `04_erc20_token_creation/notebooks/NB01_ERC20_Code_Demo.ipynb`)
2. Add "Learning Objectives" section
3. Ensure `!pip install -q web3` is present in setup cell (already present -- verify)
4. Verify "Key Takeaways" section exists
5. Retain all existing content
6. Optionally embed static PNG diagrams (erc20_interface.png, token_flow.png, approval_allowance.png, deployment_steps.png, token_economics.png)

**Dependencies:** `web3` (via pip)
**Acceptance:** Same as T2.

---

### T6: Create `NB02_SHA256_Avalanche_Interactive.ipynb` (NEW)
**Source script:** `02_cryptography_security/02_sha256_avalanche/02_sha256_avalanche.py`
**Destination:** `02_cryptography_security/notebooks/NB02_SHA256_Avalanche_Interactive.ipynb`

**Why this script is interactive:** It calls `hashlib.sha256()` on variable inputs (`input1 = "Bitcoin"`, `input2 = "bitcoin"`). Students can change these strings and see the hash values, binary bit patterns, and difference statistics recalculate dynamically. This teaches the avalanche effect through experimentation, not just a static picture.

**Adaptation guidance:**
1. **Cell 1 (Markdown):** Colab badge
2. **Cell 2 (Markdown):** Title + Learning Objectives
   - Understand the SHA-256 avalanche effect
   - Observe how minimal input changes produce drastically different hashes
   - Quantify bit-level differences between hash outputs
   - Experiment with your own inputs to verify the property
3. **Cell 3 (Code):** Setup
   ```python
   # Setup
   !pip install -q matplotlib numpy
   %matplotlib inline
   import matplotlib.pyplot as plt
   import matplotlib.patches as mpatches
   from matplotlib.patches import FancyBboxPatch, Rectangle
   import hashlib
   ```
4. **Cell 4 (Markdown):** Explain the avalanche effect concept
5. **Cell 5 (Code):** Define `hash_to_binary()` helper function (extracted from source)
6. **Cell 6 (Markdown):** Explain how we will compare two inputs
7. **Cell 7 (Code):** Define `input1` and `input2` as variables at the TOP of the cell, prominently marked with comments like `# CHANGE THESE TO EXPERIMENT`. Compute hashes and print hex + binary representations. Do NOT use dpi parameter.
8. **Cell 8 (Markdown):** Explain bit-level comparison
9. **Cell 9 (Code):** Draw the binary bit comparison visualization (the colored block grid from the source). Use `plt.show()` instead of `plt.savefig()`. Remove all `os.path` logic.
10. **Cell 10 (Markdown):** Statistics interpretation
11. **Cell 11 (Code):** Compute and display difference statistics (X out of 256 bits differ, percentage)
12. **Cell 12 (Markdown):** Exercise
    - "Change `input1` to your name and `input2` to your name with one letter capitalized differently. How many bits differ?"
    - "Try two completely different long strings. Is the difference percentage similar to a small change?"
    - "What happens when both inputs are identical?"
13. **Cell 13 (Markdown):** Key Takeaways about avalanche effect, its importance for blockchain security, why SHA-256 is considered cryptographically secure

**Key differences from source script:**
- Remove `main()`, `os.path`, `plt.savefig()`, `plt.close()`
- Do NOT set `dpi=300` -- omit dpi parameter entirely
- Split monolithic function into step-by-step cells
- Make `input1` and `input2` prominently editable variables
- Add `plt.show()` after figure construction

**Acceptance:** Notebook runs without error. Changing `input1`/`input2` and re-running produces visibly different hash outputs and bit comparisons. Students learn about avalanche effect through hands-on experimentation.

---

### T7: Create `NB02_Gas_Mechanics_Interactive.ipynb` (NEW)
**Source script:** `03_ethereum_smart_contracts/02_gas_mechanics/02_gas_mechanics.py`
**Destination:** `03_ethereum_smart_contracts/notebooks/NB02_Gas_Mechanics_Interactive.ipynb`

**Why this script is interactive:** It contains the calculation model `Gas Fee = Gas Used x Gas Price`. Students can modify gas_used, gas_price_gwei, and eth_price_usd to see how transaction costs change. The source script hardcodes 21,000 gas and 50 Gwei -- making these into editable variables creates a genuine calculator.

**Adaptation guidance:**
1. **Cell 1 (Markdown):** Colab badge
2. **Cell 2 (Markdown):** Title + Learning Objectives
   - Understand the Ethereum gas fee model (Gas Fee = Gas Used x Gas Price)
   - Calculate transaction costs for different operation types
   - Compare costs across different gas price environments
   - Understand EIP-1559 base fee + priority tip model
3. **Cell 3 (Code):** Setup
   ```python
   !pip install -q matplotlib
   %matplotlib inline
   import matplotlib.pyplot as plt
   import matplotlib.patches as patches
   from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
   ```
4. **Cell 4 (Markdown):** Explain the gas fee formula conceptually
5. **Cell 5 (Code):** Define editable parameters at TOP of cell:
   ```python
   # === CHANGE THESE TO EXPERIMENT ===
   gas_used = 21000        # Simple transfer: 21000, Token transfer: ~65000, Uniswap swap: ~150000
   gas_price_gwei = 50     # Low: 10, Medium: 50, High: 200
   eth_price_usd = 2000    # Current ETH price in USD
   ```
   Calculate and print: gas fee in ETH, gas fee in USD, gas fee in Gwei.
6. **Cell 6 (Markdown):** Explain gas costs for different operation types (SSTORE, SLOAD, ADD, etc.)
7. **Cell 7 (Code):** Create a comparison table/bar chart showing costs for different transaction types (simple transfer, token transfer, Uniswap swap, NFT mint) using the student's gas_price_gwei. Use `plt.show()`, no dpi parameter.
8. **Cell 8 (Markdown):** Explain EIP-1559 and base fee + priority tip
9. **Cell 9 (Code):** EIP-1559 calculator with editable base_fee and priority_tip variables
10. **Cell 10 (Markdown):** Exercise
    - "How much would a Uniswap swap cost at 200 Gwei gas price?"
    - "At what gas price does a simple transfer exceed $10?"
    - "Compare the cost of deploying a contract (~3,000,000 gas) at 10 Gwei vs 100 Gwei"
11. **Cell 11 (Markdown):** Key Takeaways about gas mechanics, why gas exists, EIP-1559 improvements

**Key differences from source script:**
- Extract the calculation model into editable variables (source hardcodes values)
- Remove all `os.path`, `plt.savefig()`, `plt.close()`, dpi=300
- Add computation cells that let students see numerical results, not just a diagram
- Keep relevant parts of the visual layout but focus on the interactive calculator
- The static diagram portion can reference the existing PNG: `![Gas Mechanics Diagram](../02_gas_mechanics/02_gas_mechanics.png)`

**Acceptance:** Notebook runs without error. Changing gas_used/gas_price_gwei/eth_price_usd and re-running produces different cost calculations. Students learn gas mechanics through experimentation.

---

### T8: Create `NB02_Token_Economics_Interactive.ipynb` (NEW)
**Source script:** `04_erc20_token_creation/05_token_economics/05_token_economics.py`
**Destination:** `04_erc20_token_creation/notebooks/NB02_Token_Economics_Interactive.ipynb`

**Why this script is interactive:** It uses numpy for parametric supply curves across three models (fixed, inflationary, deflationary). Students can modify initial supply, inflation rate, burn rate, and time horizon to see how different tokenomics strategies affect supply over time.

**Adaptation guidance:**
1. **Cell 1 (Markdown):** Colab badge
2. **Cell 2 (Markdown):** Title + Learning Objectives
   - Compare three token supply models: fixed, inflationary, deflationary
   - Understand how inflation rate and burn rate affect long-term supply
   - Visualize supply curves with different parameters
   - Design your own tokenomics strategy
3. **Cell 3 (Code):** Setup
   ```python
   !pip install -q matplotlib numpy
   %matplotlib inline
   import matplotlib.pyplot as plt
   import numpy as np
   ```
4. **Cell 4 (Markdown):** Explain the three token supply models conceptually
5. **Cell 5 (Code):** Define editable parameters:
   ```python
   # === CHANGE THESE TO EXPERIMENT ===
   initial_supply = 1_000_000    # Initial token supply
   years = 10                     # Time horizon
   inflation_rate = 0.05          # 5% annual inflation
   burn_rate = 0.03               # 3% annual burn rate
   ```
6. **Cell 6 (Code):** Compute supply curves for all three models using numpy:
   - Fixed: constant at `initial_supply`
   - Inflationary: `initial_supply * (1 + inflation_rate) ** t`
   - Deflationary: `initial_supply * (1 - burn_rate) ** t`
   Plot all three on a single chart with `plt.show()`. No dpi parameter.
7. **Cell 7 (Markdown):** Explain real-world examples (Bitcoin = fixed, Ethereum = inflationary with burn, BNB = deflationary)
8. **Cell 8 (Code):** Side-by-side detailed comparison (recreate the three-panel layout from source, but with editable values). Reference the static PNG for the original diagram: `![Token Economics](../05_token_economics/05_token_economics.png)`
9. **Cell 9 (Markdown):** Exercise
   - "What inflation rate causes supply to double in 5 years? (Hint: rule of 70)"
   - "Design a model that is inflationary for 5 years then deflationary -- plot it"
   - "If Ethereum burns 0.5% of supply annually while inflating at 1%, what happens long-term?"
10. **Cell 10 (Code):** Starter code for the exercise:
    ```python
    # TODO: Design your own tokenomics model
    # my_supply = np.zeros(years)
    # for year in range(years):
    #     ...
    ```
11. **Cell 11 (Markdown):** Key Takeaways about tokenomics, importance of supply model in token design, real-world implications

**Key differences from source script:**
- Extract hardcoded supply values (1.0M, 1.5M, 2.5M, 0.8M, 0.5M) into parametric calculations with editable rates
- Remove all `os.path`, `plt.savefig()`, `plt.close()`, dpi=300
- Add numpy-based parametric curves instead of hardcoded box sizes
- Keep the three-model comparison concept but make it data-driven
- Students can see how changing a single parameter shifts the entire curve

**Acceptance:** Notebook runs without error. Changing inflation_rate/burn_rate/initial_supply and re-running produces visibly different supply curves. Students learn tokenomics through parameter experimentation.

---

### T9: Add Redirect Cells to Old Notebooks
**Decision (FIRM):** Keep all 4 old notebooks in `notebooks/` with a redirect cell prepended. Do NOT delete them. Existing Colab URLs in the README are live links that external users may have bookmarked.

For each of the 4 notebooks in `notebooks/`, prepend a new first cell (markdown):

```markdown
> **This notebook has moved!**
>
> The latest version is now at:
> [`{lesson}/notebooks/NB01_{Name}_Code_Demo.ipynb`](https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/{lesson}/notebooks/NB01_{Name}_Code_Demo.ipynb)
>
> This copy is kept for backward compatibility. Please use the link above for the most current version.
```

**Files to modify:**
- `notebooks/01_blockchain_fundamentals.ipynb` -- redirect to `01_blockchain_fundamentals/notebooks/NB01_Blockchain_Code_Demo.ipynb`
- `notebooks/02_cryptography_security.ipynb` -- redirect to `02_cryptography_security/notebooks/NB01_Cryptography_Code_Demo.ipynb`
- `notebooks/03_ethereum_contracts.ipynb` -- redirect to `03_ethereum_smart_contracts/notebooks/NB01_Ethereum_Code_Demo.ipynb`
- `notebooks/04_erc20_tokens.ipynb` -- redirect to `04_erc20_token_creation/notebooks/NB01_ERC20_Code_Demo.ipynb`

**Acceptance:** Each old notebook has a visible redirect notice as its first cell. Old Colab URLs still work (notebook still runs). New Colab URL in the redirect is correct.

---

### T10: Update README.md
**File:** `README.md`

**Changes required:**

1. **Fix placeholder URLs** (lines 67 and 287):
   - Change `yourusername/cryptocurrency-course` to `Digital-AI-Finance/Cryptocurrency` in:
     - Line 67: `git clone` URL
     - Line 287: Issues URL
     - Line 288: Discussions URL

2. **Replace the "Interactive Notebooks" table** (lines 18-27) with a per-lesson structure:

```markdown
## Interactive Notebooks

Each lesson includes interactive notebooks you can run directly in Google Colab.

### Lesson 1: Blockchain Fundamentals
| Notebook | Topic | Open in Colab |
|----------|-------|---------------|
| NB01 Blockchain Code Demo | Build blocks, chains, and proof of work | [![Open In Colab](badge)](url) |

### Lesson 2: Cryptography & Security
| Notebook | Topic | Open in Colab |
|----------|-------|---------------|
| NB01 Cryptography Code Demo | Hashing, signatures, wallets | [![Open In Colab](badge)](url) |
| NB02 SHA-256 Avalanche Interactive | Experiment with the avalanche effect | [![Open In Colab](badge)](url) |

### Lesson 3: Ethereum & Smart Contracts
| Notebook | Topic | Open in Colab |
|----------|-------|---------------|
| NB01 Ethereum Code Demo | Web3 interaction, Sepolia testnet | [![Open In Colab](badge)](url) |
| NB02 Gas Mechanics Interactive | Calculate and compare gas costs | [![Open In Colab](badge)](url) |

### Lesson 4: ERC-20 Token Creation
| Notebook | Topic | Open in Colab |
|----------|-------|---------------|
| NB01 ERC-20 Code Demo | Token testing and deployment | [![Open In Colab](badge)](url) |
| NB02 Token Economics Interactive | Model supply curves and tokenomics | [![Open In Colab](badge)](url) |
```

All Colab badge URLs must use the pattern:
```
https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/{lesson}/notebooks/{notebook}.ipynb
```

**Acceptance:** All 7 Colab badge links are correct and clickable. Placeholder URLs fixed. Table renders correctly in GitHub markdown.

---

### T11: Validate All Colab URLs

Construct and verify all 7 Colab URLs follow this exact pattern:
```
https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/{path}
```

**URLs to validate (7 total):**
1. `.../01_blockchain_fundamentals/notebooks/NB01_Blockchain_Code_Demo.ipynb`
2. `.../02_cryptography_security/notebooks/NB01_Cryptography_Code_Demo.ipynb`
3. `.../02_cryptography_security/notebooks/NB02_SHA256_Avalanche_Interactive.ipynb`
4. `.../03_ethereum_smart_contracts/notebooks/NB01_Ethereum_Code_Demo.ipynb`
5. `.../03_ethereum_smart_contracts/notebooks/NB02_Gas_Mechanics_Interactive.ipynb`
6. `.../04_erc20_token_creation/notebooks/NB01_ERC20_Code_Demo.ipynb`
7. `.../04_erc20_token_creation/notebooks/NB02_Token_Economics_Interactive.ipynb`

Also validate the 4 redirect URLs in the old notebooks match the new paths.

**Acceptance:** All 11 URLs (7 in README + 4 in redirects) are syntactically correct. Full validation requires push to GitHub.

---

## Notebook Template (Reference for Enhanced Code Demo Notebooks)

```
Cell 1 [Markdown]:
  <a href="https://colab.research.google.com/github/Digital-AI-Finance/Cryptocurrency/blob/main/{path}">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>

Cell 2 [Markdown]:
  # {Topic Title}

  **Course:** Build Your Own Cryptocurrency
  **Lesson:** {Lesson Number} - {Lesson Title}

  ## Learning Objectives
  By the end of this notebook, you will:
  - Understand {concept 1}
  - Be able to {skill 1}
  - Know how to {skill 2}

Cell 3 [Code]:
  # Setup
  !pip install -q {dependencies}   # Include for ALL non-stdlib packages
  import ...

Cell 4+ [Existing content preserved]:
  ... (all existing markdown and code cells retained as-is)

Cell N-1 [Markdown] (if not already present):
  ## Exercise
  ...

Cell N [Markdown] (if not already present):
  ## Key Takeaways
  ...
```

## Notebook Template (Reference for NEW Interactive Notebooks)

```
Cell 1 [Markdown]:
  Colab badge (same format as above)

Cell 2 [Markdown]:
  Title + Learning Objectives

Cell 3 [Code]:
  Setup with !pip install -q and %matplotlib inline

Cell 4 [Markdown]:
  Concept explanation

Cell 5 [Code]:
  Helper functions (extracted from source script)

Cell 6 [Markdown]:
  What we are about to do

Cell 7 [Code]:
  # === CHANGE THESE TO EXPERIMENT ===
  param1 = ...   # Explanation of what this controls
  param2 = ...   # Explanation of what this controls
  [computation and visualization]
  plt.show()     # Never plt.savefig()

Cell 8+ [Markdown/Code alternating]:
  Additional analysis, comparisons, deeper exploration

Cell N-1 [Markdown]:
  Exercise with specific, measurable tasks

Cell N [Markdown]:
  Key Takeaways
```

---

## Risk Identification and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Old Colab URLs break after move | CERTAIN | HIGH | Keep old notebooks with redirect cell (T9); update README links (T10) |
| `blockchain.py` imports from `block.py` (relative import) | CERTAIN | MEDIUM | In notebook version, Block class is already inline (existing notebook handles this) |
| `web3_interact.py` requires running Hardhat node | CERTAIN | HIGH | Existing notebook already uses Sepolia testnet public RPC |
| `test_token.py` requires deployed contract | CERTAIN | HIGH | Existing notebook already handles this as conceptual walkthrough |
| matplotlib version differences in Colab | LOW | MEDIUM | Stick to basic matplotlib API; avoid version-specific features |
| Colab badge URLs break if repo is renamed | LOW | MEDIUM | Use consistent `Digital-AI-Finance/Cryptocurrency` throughout |
| PNG images not rendering via relative paths in Colab | MEDIUM | LOW | Colab supports relative paths for images in same repo; verify during T11 |
| dpi=300 from source scripts producing oversized images | CERTAIN | MEDIUM | Do NOT copy dpi parameter to notebooks; let matplotlib use default |

---

## Commit Strategy

```
Commit 1: "Create per-lesson notebook directories"
  - Create 4 directories with .gitkeep:
    01_blockchain_fundamentals/notebooks/
    02_cryptography_security/notebooks/
    03_ethereum_smart_contracts/notebooks/
    04_erc20_token_creation/notebooks/

Commit 2: "Move and enhance code demo notebooks to per-lesson structure"
  - 4 enhanced NB01 notebooks in their lesson directories
  - Colab badge, learning objectives, reference pattern structure added

Commit 3: "Add interactive notebooks for SHA-256 avalanche, gas mechanics, and token economics"
  - 3 new NB02 interactive notebooks
  - 02_cryptography_security/notebooks/NB02_SHA256_Avalanche_Interactive.ipynb
  - 03_ethereum_smart_contracts/notebooks/NB02_Gas_Mechanics_Interactive.ipynb
  - 04_erc20_token_creation/notebooks/NB02_Token_Economics_Interactive.ipynb

Commit 4: "Add backward compatibility redirects and update README"
  - Redirect cells in 4 old notebooks
  - README.md updated with per-lesson table and fixed placeholder URLs
```

---

## Success Criteria

1. **Completeness:** 7 total notebooks (4 enhanced + 3 new interactive) across 4 lesson directories
2. **Colab-Ready:** Every notebook has working Colab badge and runs without error
3. **Educational Value:** Interactive notebooks let students experiment with parameters and see results change; static diagrams referenced as PNG images where relevant
4. **Pattern Compliance:** Structure matches Digital-Finance-Introduction reference (badge, objectives, setup, sections, exercises, takeaways)
5. **Non-Destructive:** All original .py files and beamer materials untouched; old notebooks preserved with redirects
6. **Discoverability:** README.md provides clear per-lesson navigation to all 7 notebooks with correct Colab badges
7. **No Wasted Notebooks:** Zero notebooks that merely call `plt.show()` on hardcoded matplotlib diagrams -- every notebook has genuine interactive or educational coding value
8. **Backward Compatible:** Old Colab URLs still function; redirect cells guide users to new locations
