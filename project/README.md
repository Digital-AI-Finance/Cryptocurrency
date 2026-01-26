# StudentToken - ERC20 Token Project

A feature-rich ERC20 token built with Solidity and Hardhat, demonstrating advanced token functionality including minting, burning, and pausable transfers.

## Features

- **ERC20 Standard**: Full ERC20 compliance with name, symbol, and 18 decimals
- **Minting**: Owner can mint new tokens up to the maximum supply cap (1,000,000 STU)
- **Burning**: Any token holder can burn their own tokens
- **Pausable**: Owner can pause/unpause all transfers in emergencies
- **Access Control**: Owner-only functions protected by OpenZeppelin's Ownable

## Token Details

| Property | Value |
|----------|-------|
| Name | StudentToken |
| Symbol | STU |
| Decimals | 18 |
| Initial Supply | 100,000 STU |
| Max Supply | 1,000,000 STU |

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18.0.0 or higher)
  - Download from: https://nodejs.org/
  - Verify: `node --version`

- **npm** (v9.0.0 or higher, comes with Node.js)
  - Verify: `npm --version`

- **Git** (optional, for version control)
  - Download from: https://git-scm.com/

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd project
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```
   This will install Hardhat, OpenZeppelin contracts, and testing libraries.

3. **Verify installation:**
   ```bash
   npx hardhat --version
   ```

## Compile the Contract

Compile the Solidity smart contract:

```bash
npx hardhat compile
```

**Expected output:**
```
Compiled 1 Solidity file successfully (evm target: paris).
```

This creates the contract artifacts in the `artifacts/` directory.

## Run Tests

Execute the test suite to verify all functionality:

```bash
npx hardhat test
```

**Expected output:**
```
  StudentToken
    Deployment
      1. Should have correct name and symbol
      2. Should have correct initial supply
      Should set the correct owner
      Should have correct MAX_SUPPLY constant
    Minting
      3. Owner should be able to mint tokens
      4. Non-owner should not be able to mint
      5. Should enforce max supply cap
      Should allow minting up to exactly max supply
    Burning
      6. User should be able to burn their tokens
      Should not allow burning more than balance
      Should reduce total supply when burning
    Pausable
      7. Owner should be able to pause
      8. Transfers should fail when paused
      9. Owner should be able to unpause
      Non-owner should not be able to pause
      Non-owner should not be able to unpause
      Minting should fail when paused
      Burning should fail when paused
    Events
      10. Should emit correct events
      Should emit Transfer event on transfers
      Should emit Paused and Unpaused events
    Transfers
      Should transfer tokens between accounts
      Should fail if sender doesn't have enough tokens
      Should update allowances correctly

  23 passing
```

### Run Specific Tests

```bash
# Run only minting tests
npx hardhat test --grep "Minting"

# Run only pausable tests
npx hardhat test --grep "Pausable"

# Run with gas reporting
npm run test:gas
```

## Deploy to Local Network

### Step 1: Start a local Hardhat node

Open a terminal and run:

```bash
npx hardhat node
```

This starts a local Ethereum network at `http://127.0.0.1:8545/` with pre-funded test accounts.

**Keep this terminal running!**

### Step 2: Deploy the contract

Open a **new terminal** and run:

```bash
npx hardhat run scripts/deploy.js --network localhost
```

**Expected output:**
```
Deploying StudentToken...
StudentToken deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3
Owner: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
Initial supply: 100000.0 STU
```

Save the contract address for interacting with your token!

## Interact with Your Token

After deployment, you can interact with your token using the Hardhat console:

```bash
npx hardhat console --network localhost
```

Then in the console:

```javascript
// Get the deployed contract
const Token = await ethers.getContractFactory("StudentToken");
const token = await Token.attach("YOUR_CONTRACT_ADDRESS");

// Check token name
await token.name();  // "StudentToken"

// Check your balance (owner)
const [owner] = await ethers.getSigners();
const balance = await token.balanceOf(owner.address);
console.log(ethers.formatEther(balance), "STU");  // "100000.0 STU"

// Transfer tokens
const [_, recipient] = await ethers.getSigners();
await token.transfer(recipient.address, ethers.parseEther("100"));

// Mint new tokens (owner only)
await token.mint(recipient.address, ethers.parseEther("500"));

// Burn tokens
await token.burn(ethers.parseEther("50"));

// Pause transfers (owner only)
await token.pause();

// Unpause transfers (owner only)
await token.unpause();
```

## Project Structure

```
project/
├── contracts/
│   └── StudentToken.sol    # Main token contract
├── scripts/
│   └── deploy.js           # Deployment script
├── test/
│   └── Token.test.js       # Test suite (23 tests)
├── hardhat.config.js       # Hardhat configuration
├── package.json            # Project dependencies
└── README.md               # This file
```

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run compile` | Compile Solidity contracts |
| `npm run test` | Run all tests |
| `npm run test:coverage` | Run tests with coverage report |
| `npm run test:gas` | Run tests with gas usage report |
| `npm run node` | Start local Hardhat network |
| `npm run deploy:local` | Deploy to local network |

## Contract Functions

### Read Functions
- `name()` - Returns token name ("StudentToken")
- `symbol()` - Returns token symbol ("STU")
- `decimals()` - Returns 18
- `totalSupply()` - Returns current total supply
- `balanceOf(address)` - Returns balance of an address
- `allowance(owner, spender)` - Returns allowance
- `MAX_SUPPLY()` - Returns maximum supply cap
- `paused()` - Returns pause status
- `owner()` - Returns contract owner

### Write Functions
- `transfer(to, amount)` - Transfer tokens
- `approve(spender, amount)` - Approve allowance
- `transferFrom(from, to, amount)` - Transfer using allowance
- `mint(to, amount)` - Mint new tokens (owner only)
- `burn(amount)` - Burn your tokens
- `pause()` - Pause all transfers (owner only)
- `unpause()` - Unpause transfers (owner only)

## Troubleshooting

### "Cannot find module" errors
Run `npm install` to ensure all dependencies are installed.

### Compilation errors
- Ensure you're using Node.js v18+
- Delete `artifacts/` and `cache/` folders, then recompile:
  ```bash
  npx hardhat clean
  npx hardhat compile
  ```

### Tests failing
- Make sure you haven't modified the contract constants
- Check that INITIAL_SUPPLY in tests matches the contract (100,000)

### Deployment fails
- Ensure the local node is running (`npx hardhat node`)
- Use `--network localhost` when deploying

## Learning Resources

- [Hardhat Documentation](https://hardhat.org/docs)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Solidity Documentation](https://docs.soliditylang.org)
- [Ethereum Development](https://ethereum.org/developers)

## License

MIT License - See LICENSE file for details.
