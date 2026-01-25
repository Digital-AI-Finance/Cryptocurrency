require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/**
 * Hardhat Configuration for StudentToken Project
 *
 * Documentation: https://hardhat.org/config/
 *
 * IMPORTANT:
 * - Never commit your .env file with real private keys
 * - Use test networks (Sepolia, Goerli) for learning
 * - Keep your private keys secure
 */

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },

  networks: {
    // Local Hardhat network (default)
    hardhat: {
      chainId: 31337,
    },

    // Sepolia testnet (recommended for students)
    // TODO: Add your Infura/Alchemy API key and private key to .env file
    // sepolia: {
    //   url: process.env.SEPOLIA_RPC_URL || "",
    //   accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    //   chainId: 11155111,
    // },

    // Goerli testnet (alternative)
    // goerli: {
    //   url: process.env.GOERLI_RPC_URL || "",
    //   accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    //   chainId: 5,
    // },
  },

  // Etherscan verification (for public networks)
  // etherscan: {
  //   apiKey: process.env.ETHERSCAN_API_KEY || "",
  // },

  // Gas reporter (optional - useful for optimization)
  gasReporter: {
    enabled: process.env.REPORT_GAS === "true",
    currency: "USD",
    coinmarketcap: process.env.COINMARKETCAP_API_KEY,
  },

  // Path configuration
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts",
  },
};
