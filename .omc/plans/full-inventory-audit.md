# Full Course Inventory Audit Plan

## Status: REVISION 2 (Addressing Critic Feedback)

## Objective

Perform a comprehensive, fresh audit of every file in the "Build Your Own Cryptocurrency" course. Extract frame counts, section names, frame titles from every TEX file. Count questions in every quiz HTML. Verify all PDFs. Produce an accurate `course_inventory.json`.

## Scope

### Explicit Per-Lesson File Mapping

| Lesson | Mini Lecture | Technical Lecture | Preview Slides | Preclass Handout |
|--------|-------------|-------------------|----------------|------------------|
| L01 Blockchain | `blockchain_intro.tex` | `blockchain_fundamentals.tex` | `blockchain_fundamentals_intro.tex` | `blockchain_fundamentals_preclass.tex` |
| L02 Cryptography | `cryptography_intro.tex` | `cryptography_security.tex` | `cryptography_security_intro.tex` | `cryptography_security_preclass.tex` |
| L03 Ethereum | `ethereum_intro.tex` | `ethereum_smart_contracts.tex` | `ethereum_smart_contracts_intro.tex` | `ethereum_smart_contracts_preclass.tex` |
| L04 ERC-20 | `erc20_token_intro.tex` | `erc20_token_creation.tex` | `erc20_token_creation_intro.tex` | `erc20_token_creation_preclass.tex` |
| L05 DeFi | `defi_intro.tex` | `defi_fundamentals.tex` | `defi_fundamentals_intro.tex` | `defi_fundamentals_preclass.tex` |
| L06 NFT | `nft_intro.tex` | `nft_digital_assets.tex` | `nft_digital_assets_intro.tex` | `nft_digital_assets_preclass.tex` |
| L07 Stablecoins | `stablecoins_intro.tex` | `stablecoins_cbdcs.tex` | `stablecoins_cbdcs_intro.tex` | `stablecoins_cbdcs_preclass.tex` |
| L08 Trading | `crypto_trading_intro.tex` | `crypto_trading_markets.tex` | `crypto_trading_markets_intro.tex` | `crypto_trading_markets_preclass.tex` |
| L09 DAOs | `dao_governance_intro.tex` | `dao_governance.tex` | `dao_governance_intro_preview.tex` | `dao_governance_preclass.tex` |
| L10 Layer 2 | `layer2_scaling_intro.tex` | `layer2_scaling.tex` | `layer2_scaling_intro_preview.tex` | `layer2_scaling_preclass.tex` |
| L11 RWA | `rwa_tokenization_intro.tex` | `rwa_tokenization.tex` | `rwa_tokenization_intro_preview.tex` | `rwa_tokenization_preclass.tex` |
| L12 Tokenomics | `tokenomics_mechanism_intro.tex` | `tokenomics_mechanism.tex` | `tokenomics_mechanism_intro_preview.tex` | `tokenomics_mechanism_preclass.tex` |
| L13 Privacy/ZK | `privacy_zk_proofs_intro.tex` | `privacy_zk_proofs.tex` | `privacy_zk_proofs_intro_preview.tex` | `privacy_zk_proofs_preclass.tex` |

**Naming convention note:** L01-L08 use short-name `{short}_intro.tex` for mini lectures and `{full}_intro.tex` for preview slides. L09-L13 use `{full}_intro.tex` for mini lectures and `{full}_intro_preview.tex` for preview slides.

All files above are in the `lectures/` directory.

### File Count Summary

| Category | Count | Details |
|----------|-------|---------|
| Technical lectures (TEX) | 13 | See mapping table above |
| Mini lectures (TEX) | 13 | See mapping table above |
| Preview slides (TEX) | 13 | See mapping table above |
| Preclass handouts (TEX) | 13 | See mapping table above |
| Lesson lectures (TEX) | 4 | `0N_{name}/0N_{name}.tex` (L01-L04 only) |
| Topic PDFs | 20 | `0N_{name}/NN_{topic}/NN_{topic}.pdf` (L01-L04, 5 per lesson) |
| Standalone quizzes (HTML) | 52 | `quiz/quiz_{prefix}_part{1-4}.html` (13 lessons x 4) |
| Original quizzes (HTML) | 4 | `quiz/quiz{1-4}.html` (L01-L04) |
| Student notes (PDF) | 4 | `notes/L0N_{name}_notes.pdf` (L01-L04 only) |
| Top-level notebooks (ipynb) | 4 | `notebooks/0N_{name}.ipynb` (L01-L04) |
| Per-lesson notebooks (ipynb) | 7 | `0N_*/notebooks/*.ipynb` (L01-L04, 1-2 per lesson) |
| Template | 1 | `template_beamer_final.tex` |
| Other | 4 | `index.html`, `glossary.md`, `assessments/final_report_template.md`, `assessments/README.md` |

**Total: 152 files**

### Per-TEX-File Data to Extract

For each TEX lecture file (technical, mini, preview, lesson):
1. **Frame count**: Count `\begin{frame}` occurrences
2. **Section names**: Extract from `\section{}` commands
3. **Frame titles**: Extract from `\begin{frame}{Title}` and `\frametitle{Title}`

For each preclass handout:
- Line count only (these are article-class, not beamer)

### Per-Quiz Data to Extract

For each quiz HTML:
1. **Question count**: Count `"question":` occurrences (more robust than `"id":` — semantically unambiguous, only appears inside question objects)
2. **Quiz title**: Extract from page title or header
3. **Quiz prefix**: Extract from filename

## Implementation Plan

### Task 1: Extract Data from All 13 Technical Lectures
- Use `grep -c '\\begin{frame}'` for frame counts
- Use `grep '\\section{'` for section names
- Use `grep '\\begin{frame}{'` and `grep '\\frametitle{'` for frame titles
- Files: all 13 from the "Technical Lecture" column in the mapping table
- **Acceptance Criteria:** Frame count, section list, and frame title list for each of 13 files.

### Task 2: Extract Data from All 13 Mini Lectures
- Same grep approach as Task 1
- Files: all 13 from the "Mini Lecture" column in the mapping table
- **Acceptance Criteria:** Frame count and frame title list for each of 13 files.

### Task 3: Extract Data from All 13 Preview Slides
- Same grep approach
- **Explicit file list:** `blockchain_fundamentals_intro.tex`, `cryptography_security_intro.tex`, `ethereum_smart_contracts_intro.tex`, `erc20_token_creation_intro.tex`, `defi_fundamentals_intro.tex`, `nft_digital_assets_intro.tex`, `stablecoins_cbdcs_intro.tex`, `crypto_trading_markets_intro.tex`, `dao_governance_intro_preview.tex`, `layer2_scaling_intro_preview.tex`, `rwa_tokenization_intro_preview.tex`, `tokenomics_mechanism_intro_preview.tex`, `privacy_zk_proofs_intro_preview.tex`
- **Acceptance Criteria:** Frame count and frame title list for each of 13 files.

### Task 4: Extract Preclass Handout Data
- Count lines for each of 13 preclass TEX files
- **Acceptance Criteria:** Line count for each of 13 files.

### Task 5: Count Quiz Questions
- For all 56 quiz HTML files, count `"question":` occurrences (robust — only appears inside question objects, unlike `"id":` which could appear in other contexts)
- Extract quiz title from each file
- **Acceptance Criteria:** Question count and title for each of 56 quiz files.

### Task 6: Audit Lesson Lectures, Notes, Notebooks, Topic PDFs
- 4 lesson lectures (L01-L04): count frames, extract sections and titles
- 4 notes PDFs: confirm existence
- 11 notebooks total:
  - 4 top-level: `notebooks/01_blockchain_fundamentals.ipynb`, `notebooks/02_cryptography_security.ipynb`, `notebooks/03_ethereum_contracts.ipynb`, `notebooks/04_erc20_tokens.ipynb`
  - 7 per-lesson: `01_*/notebooks/NB01_*.ipynb`, `02_*/notebooks/NB01_*.ipynb`, `02_*/notebooks/NB02_*.ipynb`, `03_*/notebooks/NB01_*.ipynb`, `03_*/notebooks/NB02_*.ipynb`, `04_*/notebooks/NB01_*.ipynb`, `04_*/notebooks/NB02_*.ipynb`
- 20 topic PDFs: enumerate all sub-topic PDFs per lesson (5 per L01-L04)
- **Acceptance Criteria:** Complete data for L01-L04 supplementary materials, all 11 notebooks confirmed.

### Task 7: Build Comprehensive course_inventory.json
- **Step 1:** Read existing `course_inventory.json` to extract schema and static metadata fields (`color`, `gh_pages_class`, `quiz_prefix`, etc.) that do not require re-verification.
- **Step 2:** Assemble all extracted data into a fresh JSON file, preserving the existing schema structure.
- Include frame titles for ALL lectures (technical, mini, lesson)
- Include accurate summary counts computed as arithmetic sums
- Include 11 notebooks (4 top-level + 7 per-lesson)
- Include remaining gaps_and_observations (only truly missing items)
- **Acceptance Criteria:**
  - Valid JSON (`python -m json.tool`)
  - All frame counts verified by grep
  - All quiz question counts verified
  - All file references point to existing files
  - Summary totals are arithmetic sums of per-lesson data
  - Static metadata (`color`, `gh_pages_class`, `quiz_prefix`) preserved from existing JSON

## Execution Strategy

Use bash `grep -c` commands to efficiently extract frame counts across all files in batch. Use grep to extract section names and frame titles. This avoids reading 50+ full TEX files and keeps token usage minimal. Run independent grep batches in parallel.

## Verification

- [ ] Every TEX file in `lectures/` is accounted for (52 TEX files = 13x4 categories)
- [ ] Every quiz HTML in `quiz/` is accounted for (56 total)
- [ ] All 11 notebooks inventoried
- [ ] Frame counts match `grep -c '\\begin{frame}'` for each file
- [ ] Question counts match `grep -c '"question":'` for each quiz
- [ ] Summary totals = sum of per-lesson counts
- [ ] JSON is valid (`python -m json.tool`)
- [ ] No file references to non-existent files
- [ ] Static metadata preserved from previous inventory
