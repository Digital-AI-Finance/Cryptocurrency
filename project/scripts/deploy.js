/**
 * Deployment Script for StudentToken
 *
 * This script deploys your StudentToken contract to the specified network.
 *
 * Usage:
 *   npx hardhat run scripts/deploy.js --network localhost
 *   npx hardhat run scripts/deploy.js --network sepolia
 */

const hre = require("hardhat");

async function main() {
  console.log("Starting StudentToken deployment...");

  // Get the deployer account
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with account:", deployer.address);

  // Get account balance
  const balance = await hre.ethers.provider.getBalance(deployer.address);
  console.log("Account balance:", hre.ethers.formatEther(balance), "ETH");

  // Deploy the contract
  const StudentToken = await hre.ethers.getContractFactory("StudentToken");
  console.log("Deploying StudentToken...");

  const token = await StudentToken.deploy();
  await token.waitForDeployment();

  const tokenAddress = await token.getAddress();
  console.log("StudentToken deployed to:", tokenAddress);

  // Display token information
  const name = await token.name();
  const symbol = await token.symbol();
  const totalSupply = await token.totalSupply();

  console.log("\nToken Details:");
  console.log("  Name:", name);
  console.log("  Symbol:", symbol);
  console.log("  Total Supply:", hre.ethers.formatEther(totalSupply));
  console.log("  Owner:", await token.owner());

  // TODO: Add verification step for public networks
  // if (hre.network.name === "sepolia") {
  //   console.log("\nWaiting for block confirmations...");
  //   await token.deploymentTransaction().wait(6);
  //   await hre.run("verify:verify", {
  //     address: tokenAddress,
  //     constructorArguments: [],
  //   });
  // }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
