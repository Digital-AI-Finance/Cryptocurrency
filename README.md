# Build Your Own Cryptocurrency
## BSc Level Course - 4 Lessons

A comprehensive hands-on course teaching blockchain fundamentals through building a fully functional ERC-20 cryptocurrency token.

---

## Course Overview

This 4-lesson course takes students from blockchain basics to creating and deploying their own cryptocurrency on Ethereum. Each lesson combines theoretical concepts with practical implementation, culminating in a final project where students design and deploy their own custom token.

**Total Duration:** 180 minutes (4 x 45 minutes)
**Level:** Undergraduate (BSc)
**Prerequisites:** Basic programming knowledge (Python/JavaScript)

---

## Lesson Structure

| Lesson | Title | Duration | Key Topics | Deliverable |
|--------|-------|----------|------------|-------------|
| **01** | [Blockchain Fundamentals](./01_blockchain_fundamentals) | 45 min | Blocks, Hash Chains, Merkle Trees, Consensus, Decentralization | Simple blockchain in Python |
| **02** | [Cryptography & Security](./02_cryptography_security) | 45 min | Hash Functions, Digital Signatures, Public/Private Keys, Wallets | Secure wallet implementation |
| **03** | [Ethereum & Smart Contracts](./03_ethereum_smart_contracts) | 45 min | EVM Architecture, Gas, Solidity, Contract Lifecycle | First smart contract |
| **04** | [ERC-20 Token Creation](./04_erc20_token_creation) | 45 min | Token Standards, Deployment, Economics, Testing | Your own cryptocurrency |

---

## Prerequisites

### Required Knowledge
- Basic programming experience (any language)
- Understanding of functions, variables, and loops
- Command line familiarity
- No prior blockchain experience needed

### Software Requirements
- **Python 3.10+** - For blockchain fundamentals
- **Node.js 16+** - For Ethereum development
- **Git** - For cloning repository
- **Code Editor** - VS Code recommended

### Recommended Resources
- [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)
- [Solidity Documentation](https://docs.soliditylang.org/)
- [Hardhat Tutorial](https://hardhat.org/tutorial)

---

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/cryptocurrency-course.git
cd cryptocurrency-course
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `ecdsa` - Elliptic curve cryptography
- `web3` - Ethereum interaction
- `matplotlib` & `numpy` - Data visualization
- `Pillow` - Image processing

### 3. Install Node Dependencies
```bash
npm install
```

This installs:
- `hardhat` - Ethereum development environment
- `@nomicfoundation/hardhat-toolbox` - Testing and deployment tools
- `@openzeppelin/contracts` - Secure token contracts

### 4. Run Python Blockchain Examples
```bash
# Lesson 01 - Build a simple blockchain
python 01_blockchain_fundamentals/code/blockchain.py

# Lesson 02 - Create a wallet with signatures
python 02_cryptography_security/code/wallet.py
```

### 5. Deploy Your Token
```bash
# Start local Ethereum node (keep terminal open)
npx hardhat node

# In a new terminal, deploy the token
npx hardhat run 04_erc20_token_creation/code/deploy.js --network localhost

# Run tests
npx hardhat test
```

---

## Repository Structure

```
cryptocurrency-course/
│
├── 01_blockchain_fundamentals/          # Lesson 1: Blockchain Basics
│   ├── 01_blockchain_structure/         # Block anatomy
│   ├── 02_hash_chain/                   # Cryptographic linking
│   ├── 03_merkle_tree/                  # Efficient verification
│   ├── 04_consensus_comparison/         # PoW vs PoS
│   ├── 05_decentralization/             # Network topology
│   └── code/                            # Python blockchain implementation
│
├── 02_cryptography_security/            # Lesson 2: Crypto & Security
│   ├── 01_hash_function/                # SHA-256 basics
│   ├── 02_sha256_avalanche/             # Avalanche effect demo
│   ├── 03_public_private_keys/          # Asymmetric cryptography
│   ├── 04_digital_signature_flow/       # Signing & verification
│   ├── 05_wallet_architecture/          # Wallet structure
│   └── code/                            # Python crypto implementation
│
├── 03_ethereum_smart_contracts/         # Lesson 3: Ethereum & Solidity
│   ├── 01_ethereum_architecture/        # EVM overview
│   ├── 02_gas_mechanics/                # Gas pricing
│   ├── 03_smart_contract_lifecycle/     # Deployment flow
│   ├── 04_solidity_types/               # Data types
│   ├── 05_contract_interaction/         # Calling contracts
│   └── code/                            # Solidity examples
│
├── 04_erc20_token_creation/             # Lesson 4: Create Your Token
│   ├── 01_erc20_interface/              # ERC-20 standard
│   ├── 02_token_flow/                   # Transfer mechanics
│   ├── 03_approval_allowance/           # Delegated transfers
│   ├── 04_deployment_steps/             # Deployment guide
│   ├── 05_token_economics/              # Tokenomics design
│   └── code/
│       ├── MyToken.sol                  # Example ERC-20 contract
│       └── deploy.js                    # Deployment script
│
├── assessments/                         # Course Assessments
│   ├── final_report_template.md         # Final project template
│   └── README.md                        # Assessment guidelines
│
├── project/                             # Final Project Scaffold
│   ├── contracts/                       # Student token contracts
│   ├── scripts/                         # Deployment scripts
│   ├── test/                            # Test files
│   └── hardhat.config.js                # Project configuration
│
├── .github/workflows/                   # CI/CD automation
├── hardhat.config.js                    # Main Hardhat config
├── package.json                         # Node dependencies
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

---

## Learning Outcomes

By completing this course, students will be able to:

### Technical Skills
- ✅ Build a blockchain from scratch in Python
- ✅ Implement cryptographic hash functions and digital signatures
- ✅ Write and deploy Solidity smart contracts
- ✅ Create ERC-20 compliant cryptocurrency tokens
- ✅ Test contracts using Hardhat framework
- ✅ Deploy to local and public Ethereum networks

### Conceptual Understanding
- ✅ Explain blockchain immutability and consensus mechanisms
- ✅ Analyze security properties of cryptographic primitives
- ✅ Evaluate trade-offs in token economics
- ✅ Design decentralized applications (dApps)

---

## Final Project

Students create their own cryptocurrency with:

1. **Custom Token Contract** - Unique name, symbol, and supply
2. **Advanced Features** - Minting, burning, or pausing capabilities
3. **Test Suite** - Comprehensive unit tests
4. **Deployment** - To testnet (Sepolia/Goerli)
5. **Technical Report** - Architecture and design decisions

**Submission:** See [assessments/final_report_template.md](./assessments/final_report_template.md)

---

## Additional Resources

### Documentation
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf) - Technical specification
- [ERC-20 Token Standard](https://eips.ethereum.org/EIPS/eip-20) - Official EIP
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) - Security best practices

### Tools
- [Remix IDE](https://remix.ethereum.org/) - Browser-based Solidity IDE
- [Etherscan](https://etherscan.io/) - Blockchain explorer
- [MetaMask](https://metamask.io/) - Browser wallet

### Community
- [Ethereum Stack Exchange](https://ethereum.stackexchange.com/)
- [r/ethdev](https://reddit.com/r/ethdev)
- [Hardhat Discord](https://hardhat.org/discord)

---

## Troubleshooting

### Python Issues
```bash
# Install specific version
pip install ecdsa==0.18.0

# Use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Node/Hardhat Issues
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# Reset Hardhat network
npx hardhat clean
```

### Common Errors
- **"Module not found"** - Run `npm install` or `pip install -r requirements.txt`
- **"Network not running"** - Ensure `npx hardhat node` is running in separate terminal
- **"Gas estimation failed"** - Check contract syntax or increase gas limit

---

## Contributing

This course material is open for contributions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add new example'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Ethereum Foundation** - For blockchain infrastructure
- **OpenZeppelin** - For secure contract libraries
- **Hardhat** - For development tooling
- **Students & Contributors** - For feedback and improvements

---

## Contact

For questions or feedback:
- **Issues:** [GitHub Issues](https://github.com/yourusername/cryptocurrency-course/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/cryptocurrency-course/discussions)

---

**Ready to build your cryptocurrency? Start with [Lesson 01: Blockchain Fundamentals](./01_blockchain_fundamentals)!**
