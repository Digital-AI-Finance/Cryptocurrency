// Hardhat deployment script for MyToken ERC-20 contract
const hre = require("hardhat");

async function main() {
  console.log("Starting MyToken deployment...\n");

  // Get the contract factory
  const MyToken = await hre.ethers.getContractFactory("MyToken");

  // Get deployer account
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contract with account:", deployer.address);

  // Get deployer balance
  const balance = await hre.ethers.provider.getBalance(deployer.address);
  console.log("Account balance:", hre.ethers.formatEther(balance), "ETH\n");

  // Deploy the contract
  console.log("Deploying MyToken...");
  const token = await MyToken.deploy();
  await token.waitForDeployment();

  const tokenAddress = await token.getAddress();
  console.log("MyToken deployed to:", tokenAddress);

  // Get token details
  const name = await token.name();
  const symbol = await token.symbol();
  const decimals = await token.decimals();
  const totalSupply = await token.totalSupply();
  const maxSupply = await token.MAX_SUPPLY();
  const ownerBalance = await token.balanceOf(deployer.address);

  console.log("\n--- Token Details ---");
  console.log("Name:", name);
  console.log("Symbol:", symbol);
  console.log("Decimals:", decimals);
  console.log("Total Supply:", hre.ethers.formatUnits(totalSupply, decimals), symbol);
  console.log("Max Supply:", hre.ethers.formatUnits(maxSupply, decimals), symbol);
  console.log("Owner Balance:", hre.ethers.formatUnits(ownerBalance, decimals), symbol);

  console.log("\n--- Deployment Summary ---");
  console.log("Contract Address:", tokenAddress);
  console.log("Owner Address:", deployer.address);
  console.log("\nDeployment complete!");
}

// Execute deployment
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Deployment failed:", error);
    process.exit(1);
  });
