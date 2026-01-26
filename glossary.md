# Cryptocurrency Course Glossary

A comprehensive reference guide for key terms and concepts covered throughout the cryptocurrency course.

---

## Lesson 1: Blockchain Fundamentals

| Term | Definition | Example |
|------|------------|---------|
| **Blockchain** | A distributed, immutable ledger that records transactions across multiple computers in a chronological, tamper-resistant manner. Each block contains transaction data, a timestamp, and a cryptographic hash linking it to the previous block. | Bitcoin's blockchain has over 800,000 blocks, each storing transaction history that cannot be altered retroactively. |
| **Block** | A unit of data in a blockchain that contains a list of transactions, a timestamp, and a reference (hash) to the previous block. Blocks are grouped together chronologically, forming a chain. | When you send Bitcoin, your transaction is bundled into a block with thousands of other transactions before being added to the blockchain. |
| **Hash** | A cryptographic function that converts input data of any size into a fixed-length string of characters, creating a unique digital fingerprint. Any change to the input produces a completely different hash. | SHA-256 hashes Bitcoin blocks: changing a single character in the input creates an entirely different hash output. |
| **Merkle Tree** | A tree structure used in blockchains where leaf nodes contain transaction hashes, and parent nodes contain hashes of their children, ultimately producing a single root hash representing all transactions. | Bitcoin uses Merkle trees to efficiently verify that a specific transaction is included in a block without downloading the entire block. |
| **Consensus** | A mechanism that allows a distributed network of nodes to agree on the validity and ordering of transactions without requiring a central authority. Consensus ensures all participants maintain identical copies of the ledger. | Bitcoin's Proof of Work consensus requires nodes to solve complex mathematical puzzles so the entire network agrees on which blocks are valid. |
| **Proof of Work (PoW)** | A consensus mechanism requiring miners to solve computationally difficult mathematical puzzles to validate transactions and create new blocks. The first miner to solve the puzzle gets to add the block and receives a reward. | Bitcoin miners compete to solve SHA-256 puzzles, with the first to find a solution earning newly minted bitcoins plus transaction fees. |
| **Proof of Stake (PoS)** | A consensus mechanism where validators are chosen based on the amount of cryptocurrency they hold and are willing to "stake" as collateral. Validators lose their stake if they act dishonestly, creating economic incentives for honesty. | Ethereum 2.0 uses Proof of Stake: validators deposit 32 ETH and are randomly selected to propose blocks, earning rewards for participation. |
| **Genesis Block** | The first block in a blockchain (Block #0), created when the blockchain network launches. It serves as the foundation for all subsequent blocks and typically contains special parameters or messages. | Bitcoin's genesis block (created January 3, 2009) contains the message "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks," referencing that day's news headline. |
| **Nonce** | Short for "number used once," a nonce is a random or pseudo-random number used once in cryptographic applications. In Proof of Work, miners increment the nonce until they find a hash meeting specific difficulty requirements. | A Bitcoin miner might try nonce values 1, 2, 3... until nonce 42,053,847 finally produces a hash starting with the required number of zeros. |
| **Double-spending** | An attack where a user spends the same digital currency twice by sending conflicting transactions to the network. Blockchain consensus mechanisms prevent double-spending by ensuring transactions are permanently recorded. | Without blockchain protections, Alice could send the same digital dollar to both Bob and Carol. Bitcoin's consensus prevents this by confirming transactions permanently. |
| **Node** | A computer running blockchain software that maintains a complete copy of the distributed ledger and validates incoming transactions and blocks. Nodes communicate with each other to maintain network consensus. | A Bitcoin full node stores the entire 500+ GB blockchain history, validates new transactions, and relays them to other nodes in the peer-to-peer network. |
| **51% Attack** | A theoretical attack where a single entity controls over 50% of a blockchain network's computing power (in PoW) or staked coins (in PoS), allowing them to control consensus and potentially reverse transactions. | If an attacker controlled 51% of Bitcoin's mining power, they could theoretically exclude certain transactions or create conflicting transaction histories. |

---

## Lesson 2: Cryptography

| Term | Definition | Example |
|------|------------|---------|
| **SHA-256** | Secure Hash Algorithm 256-bit, a cryptographic hash function that produces a 256-bit (32-byte) hash output. Bitcoin and many blockchains use SHA-256 to hash blocks, creating tamper-evident digital fingerprints. | Hashing the text "Hello" with SHA-256 produces: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969. Changing one letter produces a completely different hash. |
| **Public Key** | The publicly shareable part of an asymmetric cryptographic key pair used for receiving funds, verifying digital signatures, and deriving a blockchain address. Public keys can be freely shared without compromising security. | In Bitcoin, your public key (a 66-character hexadecimal string) is mathematically derived from your private key and visible to everyone, but only you can spend funds sent to it. |
| **Private Key** | A secret, randomly generated number that must be kept confidential and is used to sign transactions, proving ownership and authorization to spend funds. Anyone with the private key can control all funds associated with it. | A Bitcoin private key is a 256-bit number (roughly 2^256 possibilities), stored as a 64-character hexadecimal string. Losing it means losing access to funds forever. |
| **Digital Signature** | A cryptographic proof that a message or transaction was created and authorized by the holder of a specific private key, without revealing the private key itself. Digital signatures ensure authentication and non-repudiation. | When you send Bitcoin, your private key cryptographically signs the transaction, proving you authorized it without exposing your private key to the network. |
| **ECDSA** | Elliptic Curve Digital Signature Algorithm, a public-key cryptographic algorithm used by Bitcoin, Ethereum, and most cryptocurrencies to create digital signatures with smaller key sizes than RSA while maintaining security. | Bitcoin uses ECDSA with the secp256k1 elliptic curve, allowing a 256-bit private key to create cryptographically secure signatures. |
| **Wallet** | Software or hardware that stores private keys and manages cryptocurrency ownership and transactions. Wallets generate addresses, sign transactions, and display account balances. | MetaMask is a browser wallet for Ethereum that stores your private key locally on your device and allows you to sign transactions without exposing your private key to websites. |
| **Seed Phrase** | A human-readable sequence of 12-24 words (mnemonic code) that can mathematically regenerate all private keys for a wallet. Seed phrases follow the BIP39 standard and should be kept private and stored securely. | A seed phrase like "witch collapse practice feed shame open despair community loan hair dress" can regenerate all your cryptocurrency accounts across devices. |
| **Address** | A publicly shareable identifier derived from a public key using cryptographic hashing, used to receive cryptocurrency. Addresses are unique, pseudonymous, and appear on the public blockchain. | A Bitcoin address might look like "1A1z7agoat7SFfukcVBSJi9nrEsrHsyQV5" and anyone can send bitcoin to it, but only the holder of the corresponding private key can spend those funds. |

---

## Lesson 3: Ethereum

| Term | Definition | Example |
|------|------------|---------|
| **Smart Contract** | Self-executing code deployed on the blockchain that automatically executes when predefined conditions are met. Smart contracts eliminate intermediaries by enforcing agreements through code rather than legal contracts. | A simple smart contract might say "when address A sends 1 ETH to this contract and the date is after January 1, 2025, automatically send 1.1 ETH to address B," creating a trustless loan agreement. |
| **EVM** | Ethereum Virtual Machine, the runtime environment that executes smart contract bytecode on every node in the Ethereum network. The EVM is a "world computer" ensuring all nodes execute contracts identically. | When you deploy a Solidity smart contract to Ethereum, it's compiled into EVM bytecode, which thousands of nodes around the world execute in parallel, producing identical results. |
| **Gas** | The unit of computational work required to execute operations on the Ethereum network (transactions, smart contract calls, storage writes). Every operation consumes a specific amount of gas based on complexity. | Transferring ETH costs 21,000 gas, while deploying a complex smart contract might cost 2,000,000+ gas, depending on code size and operations. |
| **Gas Price** | The amount of cryptocurrency (measured in Gwei, a fraction of ETH) paid per unit of gas. Higher gas prices incentivize miners to prioritize your transaction during network congestion. | When Ethereum is congested, gas prices might rise to 100 Gwei per gas (costing $5+ per transaction), but during quiet times might drop to 20 Gwei. |
| **Gas Limit** | The maximum amount of gas a transaction can consume, set by the sender to prevent overspending and protect against infinite loops. If a transaction exceeds its gas limit, execution stops and fees are paid for consumed gas. | When sending ETH, you might set a gas limit of 21,000, ensuring your transaction can't cost more than expected. For a complex smart contract call, you might set a limit of 200,000. |
| **Wei** | The smallest unit of Ether, with 1 ETH = 10^18 Wei. All internal Ethereum calculations use Wei to maintain precision with integer arithmetic, avoiding floating-point errors. | A Ethereum balance of 1.5 ETH is represented internally as 1,500,000,000,000,000,000 Wei (1.5 * 10^18), preventing rounding errors in financial calculations. |
| **Gwei** | A unit of Ether equal to 10^9 Wei (0.000000001 ETH). Gas prices are conventionally quoted in Gwei because transaction fees are usually small fractions of ETH. | Gas price of 50 Gwei × 21,000 gas (ETH transfer) = 1,050,000,000,000 Wei = 0.00105 ETH (approximately $3-4 depending on ETH price). |
| **Solidity** | A high-level programming language specifically designed for writing Ethereum smart contracts. Solidity syntax resembles JavaScript and compiles to EVM bytecode executed on the Ethereum network. | A simple Solidity contract might look like: `contract HelloWorld { function greet() public pure returns (string) { return "Hello"; } }` |
| **ABI** | Application Binary Interface, a JSON file specifying a smart contract's functions, inputs, outputs, and how to interact with it. ABIs allow external applications and wallets to call smart contract functions. | An ERC-20 token ABI includes function definitions like `transfer(address to, uint256 amount)`, allowing wallets and exchanges to call token functions with the correct parameters. |
| **Bytecode** | The low-level machine code compiled from Solidity or other smart contract languages. Bytecode is what actually executes on the EVM and is stored permanently on the blockchain. | Solidity code `contract Foo { uint256 x; }` compiles to bytecode like `60606040...` (hexadecimal), which the EVM interprets as specific operations. |

---

## Lesson 4: ERC-20 Token Standard

| Term | Definition | Example |
|------|------------|---------|
| **ERC-20** | Ethereum Request for Comments #20, the technical standard defining how fungible tokens behave on Ethereum. ERC-20 specifies required functions like transfer(), approve(), and balanceOf(), ensuring token compatibility across wallets and exchanges. | USDC, USDT, DAI, and most Ethereum tokens follow the ERC-20 standard, allowing any ERC-20-compatible wallet or exchange to send, receive, and manage these tokens using the same interface. |
| **Token** | A digital asset created and managed by a smart contract on a blockchain. Tokens can represent ownership (stocks), value (stablecoins), access rights, or utility within an ecosystem. | Uniswap's UNI token represents governance rights and can be staked for fee rebates; USDC is a stablecoin token pegged to the US dollar. |
| **Fungible** | A property where each unit is identical and interchangeable with any other unit, with no distinguishing characteristics. Fungible tokens can be freely mixed and exchanged without loss of value. | Bitcoin is fungible: 1 BTC is identical to any other BTC. Unlike non-fungible tokens (NFTs), there's no difference between your BTC and mine. |
| **totalSupply()** | An ERC-20 function that returns the total number of tokens ever minted and currently in circulation. The supply may be fixed at creation or increase/decrease through minting and burning. | Calling USDC's totalSupply() returns approximately 34 billion, representing the total USDC tokens in existence across all addresses. |
| **balanceOf()** | An ERC-20 function that returns the token balance of a specific address, allowing users to check how many tokens they own without requiring a centralized database. | Calling USDC.balanceOf("0x1234...abcd") returns the number of USDC tokens stored at that Ethereum address. |
| **transfer()** | An ERC-20 function that moves tokens from the caller's address to a recipient address. Transfer requires the sender to have sufficient balance and decrements sender balance while incrementing recipient balance. | Calling USDC.transfer("0x9999...ffff", 100) sends 100 USDC from your address to 0x9999...ffff, updating balances instantly on the blockchain. |
| **approve()** | An ERC-20 function that grants another address (spender) permission to transfer tokens on behalf of the token owner. Approve doesn't move tokens; it only authorizes spending. | Approving a Uniswap smart contract to spend your USDC via USDC.approve(uniswap_address, 1000) allows Uniswap to swap your tokens without you sending them directly. |
| **allowance()** | An ERC-20 function that returns how many tokens an owner has approved for a specific spender to use. It returns the remaining authorization amount. | Calling USDC.allowance("0x1111...aaaa", "0x2222...bbbb") returns how much USDC the spender at 0x2222...bbbb is authorized to transfer on behalf of 0x1111...aaaa. |
| **transferFrom()** | An ERC-20 function that moves tokens from one address to another, requiring prior approval via approve(). Only authorized spenders can call this function with the owner's allowance. | After approving 1000 USDC, a Uniswap smart contract can call USDC.transferFrom(your_address, uniswap_address, 1000) to execute your token swap. |
| **Minting** | The process of creating new tokens and adding them to the total supply. Only the token contract owner typically has minting permissions, increasing the number of tokens in circulation. | A stablecoin protocol might mint 1 million USDC tokens when users deposit 1 million USD, increasing the total supply and assigning those tokens to users' addresses. |
| **Burning** | The process of permanently removing tokens from circulation by sending them to a dead address (an address with no private key) or reducing the total supply through smart contract logic. Burning reduces token supply and may increase the value of remaining tokens. | Token projects sometimes burn a percentage of transaction fees to reduce supply and create scarcity; Ethereum has burned millions of ETH since the London upgrade. |
| **OpenZeppelin** | A widely-trusted open-source library providing audited, reusable smart contract code for ERC-20, ERC-721 (NFTs), access control, and other common blockchain patterns. Using OpenZeppelin reduces bugs and security risks. | Instead of writing ERC-20 from scratch, developers import OpenZeppelin's contracts: `import "@openzeppelin/contracts/token/ERC20/ERC20.sol";` and inherit from ERC20. |
| **Hardhat** | A development environment and testing framework for Ethereum smart contracts that simplifies compilation, deployment, testing, and debugging. Hardhat runs a local Ethereum network for fast development iteration. | Developers use Hardhat to write tests: `const balance = await token.balanceOf(address); expect(balance).to.equal(expectedAmount);` before deploying to the real network. |
| **Decimals** | A parameter specifying how many decimal places a token supports (typically 18 for most Ethereum tokens). Decimals allow fractional tokens while using only integer arithmetic internally. | USDC has 18 decimals, so balances are stored as integers (1 USDC = 1,000,000,000,000,000,000 smallest units), allowing precise fractional amounts like 0.0001 USDC. |

---

## Quick Reference: Term Categories

### Blockchain Infrastructure
Blockchain, Block, Hash, Merkle Tree, Consensus, Node, Genesis Block

### Security & Validation
Proof of Work, Proof of Stake, 51% Attack, Nonce, Double-spending

### Cryptography
SHA-256, Public Key, Private Key, Digital Signature, ECDSA

### User Management
Wallet, Seed Phrase, Address

### Ethereum Execution
EVM, Gas, Gas Price, Gas Limit, Wei, Gwei

### Smart Contract Development
Smart Contract, Solidity, ABI, Bytecode

### Token Standard
ERC-20, Token, Fungible

### ERC-20 Functions
totalSupply(), balanceOf(), transfer(), approve(), allowance(), transferFrom()

### Token Economics
Minting, Burning, Decimals

### Development Tools
OpenZeppelin, Hardhat

---

## Study Tips

- **Start with fundamentals**: Master Blockchain Fundamentals before moving to Ethereum concepts
- **Understand cryptography**: Grasp Public/Private Key concepts before learning about wallets
- **Practice with testnet**: Deploy contracts on Ethereum testnet (Sepolia) to reinforce ERC-20 understanding
- **Reference as needed**: Use this glossary while reviewing slides and writing code
- **Build connections**: Notice how lower-level concepts (hashing, signatures) enable higher-level features (wallets, smart contracts)
