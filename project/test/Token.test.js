/**
 * Test Suite for StudentToken
 *
 * This is a template test file. Add more tests based on your custom features.
 *
 * Run tests with:
 *   npx hardhat test
 *   npx hardhat test --grep "deployment"  (run specific tests)
 */

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("StudentToken", function () {
  let token;
  let owner;
  let addr1;
  let addr2;

  const INITIAL_SUPPLY = ethers.parseEther("1000000"); // 1 million tokens

  beforeEach(async function () {
    // Get test accounts
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy the contract before each test
    const StudentToken = await ethers.getContractFactory("StudentToken");
    token = await StudentToken.deploy();
    await token.waitForDeployment();
  });

  describe("Deployment", function () {
    it("Should set the correct token name and symbol", async function () {
      // TODO: Update these values to match your token
      expect(await token.name()).to.equal("YourTokenName");
      expect(await token.symbol()).to.equal("YTN");
    });

    it("Should assign the total supply to the owner", async function () {
      const ownerBalance = await token.balanceOf(owner.address);
      expect(await token.totalSupply()).to.equal(ownerBalance);
      expect(ownerBalance).to.equal(INITIAL_SUPPLY);
    });

    it("Should set the correct owner", async function () {
      expect(await token.owner()).to.equal(owner.address);
    });
  });

  describe("Transfers", function () {
    it("Should transfer tokens between accounts", async function () {
      const transferAmount = ethers.parseEther("100");

      // Transfer from owner to addr1
      await token.transfer(addr1.address, transferAmount);
      expect(await token.balanceOf(addr1.address)).to.equal(transferAmount);

      // Transfer from addr1 to addr2
      await token.connect(addr1).transfer(addr2.address, transferAmount);
      expect(await token.balanceOf(addr2.address)).to.equal(transferAmount);
      expect(await token.balanceOf(addr1.address)).to.equal(0);
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const initialOwnerBalance = await token.balanceOf(owner.address);
      const tooMuchTokens = initialOwnerBalance + 1n;

      await expect(
        token.connect(addr1).transfer(owner.address, tooMuchTokens)
      ).to.be.reverted;
    });
  });

  // ============================================================
  // TODO: ADD TESTS FOR YOUR CUSTOM FEATURES BELOW
  // ============================================================

  describe("Custom Features", function () {
    // Example: Test minting functionality
    // it("Should allow owner to mint new tokens", async function () {
    //   const mintAmount = ethers.parseEther("1000");
    //   await token.mint(addr1.address, mintAmount);
    //   expect(await token.balanceOf(addr1.address)).to.equal(mintAmount);
    // });

    // Example: Test burning functionality
    // it("Should allow users to burn their tokens", async function () {
    //   const burnAmount = ethers.parseEther("100");
    //   await token.transfer(addr1.address, burnAmount);
    //   await token.connect(addr1).burn(burnAmount);
    //   expect(await token.balanceOf(addr1.address)).to.equal(0);
    // });

    // Add your custom feature tests here...
  });
});
