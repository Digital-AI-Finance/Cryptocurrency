# Final Project: Create Your Own Cryptocurrency

## Objective
Create a unique ERC-20 token with custom parameters and at least one additional feature.

## Requirements

### Minimum Requirements
1. **Token Contract** (StudentToken.sol)
   - Custom name and symbol
   - Defined total supply (choose your own)
   - All ERC-20 functions implemented correctly
   - At least ONE custom feature

2. **Deployment**
   - Successfully deploy to local Hardhat network
   - Demonstrate transfer functionality

3. **Testing**
   - Write at least 3 test cases
   - All tests must pass

### Custom Feature Ideas
Choose at least one:
- **Minting cap**: Maximum tokens that can ever be minted
- **Burn function**: Allow holders to destroy tokens
- **Pause/unpause**: Emergency stop mechanism
- **Ownership**: Add owner-only functions
- **Transfer fees**: Small percentage on each transfer

## Getting Started

1. Copy `contracts/StudentToken.sol` as your starting point
2. Modify the token parameters
3. Add your custom feature
4. Write tests in `test/`
5. Deploy using `scripts/deploy.js`

## Commands

```bash
# Compile your contract
npx hardhat compile

# Run tests
npx hardhat test

# Start local node
npx hardhat node

# Deploy (in new terminal)
npx hardhat run scripts/deploy.js --network localhost
```

## Submission
Fill out the report template in `../assessments/final_report_template.md`
