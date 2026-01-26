/**
 * Test Suite for StudentToken
 *
 * Comprehensive tests covering all StudentToken functionality:
 * - Basic ERC20 operations (name, symbol, transfers)
 * - Minting with max supply enforcement
 * - Burning functionality
 * - Pausable mechanism
 * - Event emissions
 *
 * Run tests with:
 *   npx hardhat test
 *   npx hardhat test --grep "minting"  (run specific tests)
 */

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("StudentToken", function () {
  let token;
  let owner;
  let addr1;
  let addr2;

  // Constants matching the contract
  const INITIAL_SUPPLY = ethers.parseEther("100000"); // 100,000 tokens
  const MAX_SUPPLY = ethers.parseEther("1000000"); // 1,000,000 tokens

  beforeEach(async function () {
    // Get test accounts
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy the contract before each test
    const StudentToken = await ethers.getContractFactory("StudentToken");
    token = await StudentToken.deploy();
    await token.waitForDeployment();
  });

  // ============================================================
  // TEST 1 & 2: Basic Token Properties
  // ============================================================
  describe("Deployment", function () {
    it("1. Should have correct name and symbol", async function () {
      expect(await token.name()).to.equal("StudentToken");
      expect(await token.symbol()).to.equal("STU");
    });

    it("2. Should have correct initial supply", async function () {
      const ownerBalance = await token.balanceOf(owner.address);
      expect(await token.totalSupply()).to.equal(INITIAL_SUPPLY);
      expect(ownerBalance).to.equal(INITIAL_SUPPLY);
    });

    it("Should set the correct owner", async function () {
      expect(await token.owner()).to.equal(owner.address);
    });

    it("Should have correct MAX_SUPPLY constant", async function () {
      expect(await token.MAX_SUPPLY()).to.equal(MAX_SUPPLY);
    });
  });

  // ============================================================
  // TEST 3, 4, 5: Minting Functionality
  // ============================================================
  describe("Minting", function () {
    it("3. Owner should be able to mint tokens", async function () {
      const mintAmount = ethers.parseEther("1000");
      await token.mint(addr1.address, mintAmount);
      expect(await token.balanceOf(addr1.address)).to.equal(mintAmount);
      expect(await token.totalSupply()).to.equal(INITIAL_SUPPLY + mintAmount);
    });

    it("4. Non-owner should not be able to mint", async function () {
      const mintAmount = ethers.parseEther("1000");
      await expect(
        token.connect(addr1).mint(addr1.address, mintAmount)
      ).to.be.revertedWithCustomError(token, "OwnableUnauthorizedAccount");
    });

    it("5. Should enforce max supply cap", async function () {
      // Try to mint more than remaining supply
      const remainingSupply = MAX_SUPPLY - INITIAL_SUPPLY;
      const excessAmount = remainingSupply + 1n;

      await expect(
        token.mint(addr1.address, excessAmount)
      ).to.be.revertedWith("Exceeds max supply");
    });

    it("Should allow minting up to exactly max supply", async function () {
      const remainingSupply = MAX_SUPPLY - INITIAL_SUPPLY;
      await token.mint(addr1.address, remainingSupply);
      expect(await token.totalSupply()).to.equal(MAX_SUPPLY);
    });
  });

  // ============================================================
  // TEST 6: Burning Functionality
  // ============================================================
  describe("Burning", function () {
    it("6. User should be able to burn their tokens", async function () {
      // First transfer some tokens to addr1
      const transferAmount = ethers.parseEther("1000");
      await token.transfer(addr1.address, transferAmount);

      // Burn half of them
      const burnAmount = ethers.parseEther("500");
      await token.connect(addr1).burn(burnAmount);

      expect(await token.balanceOf(addr1.address)).to.equal(
        transferAmount - burnAmount
      );
    });

    it("Should not allow burning more than balance", async function () {
      const burnAmount = ethers.parseEther("1000");
      // addr1 has no tokens, so this should fail
      await expect(
        token.connect(addr1).burn(burnAmount)
      ).to.be.revertedWithCustomError(token, "ERC20InsufficientBalance");
    });

    it("Should reduce total supply when burning", async function () {
      const burnAmount = ethers.parseEther("1000");
      await token.burn(burnAmount);
      expect(await token.totalSupply()).to.equal(INITIAL_SUPPLY - burnAmount);
    });
  });

  // ============================================================
  // TEST 7, 8, 9: Pausable Functionality
  // ============================================================
  describe("Pausable", function () {
    it("7. Owner should be able to pause", async function () {
      await token.pause();
      expect(await token.paused()).to.equal(true);
    });

    it("8. Transfers should fail when paused", async function () {
      await token.pause();
      const transferAmount = ethers.parseEther("100");

      await expect(
        token.transfer(addr1.address, transferAmount)
      ).to.be.revertedWithCustomError(token, "EnforcedPause");
    });

    it("9. Owner should be able to unpause", async function () {
      await token.pause();
      expect(await token.paused()).to.equal(true);

      await token.unpause();
      expect(await token.paused()).to.equal(false);

      // Transfers should work again
      const transferAmount = ethers.parseEther("100");
      await token.transfer(addr1.address, transferAmount);
      expect(await token.balanceOf(addr1.address)).to.equal(transferAmount);
    });

    it("Non-owner should not be able to pause", async function () {
      await expect(
        token.connect(addr1).pause()
      ).to.be.revertedWithCustomError(token, "OwnableUnauthorizedAccount");
    });

    it("Non-owner should not be able to unpause", async function () {
      await token.pause();
      await expect(
        token.connect(addr1).unpause()
      ).to.be.revertedWithCustomError(token, "OwnableUnauthorizedAccount");
    });

    it("Minting should fail when paused", async function () {
      await token.pause();
      const mintAmount = ethers.parseEther("1000");

      await expect(
        token.mint(addr1.address, mintAmount)
      ).to.be.revertedWithCustomError(token, "EnforcedPause");
    });

    it("Burning should fail when paused", async function () {
      // First transfer some tokens
      const transferAmount = ethers.parseEther("1000");
      await token.transfer(addr1.address, transferAmount);

      // Then pause
      await token.pause();

      // Try to burn
      await expect(
        token.connect(addr1).burn(transferAmount)
      ).to.be.revertedWithCustomError(token, "EnforcedPause");
    });
  });

  // ============================================================
  // TEST 10: Event Emissions
  // ============================================================
  describe("Events", function () {
    it("10. Should emit correct events", async function () {
      const mintAmount = ethers.parseEther("1000");

      // Test TokensMinted event
      await expect(token.mint(addr1.address, mintAmount))
        .to.emit(token, "TokensMinted")
        .withArgs(addr1.address, mintAmount);

      // Test TokensBurned event
      await expect(token.connect(addr1).burn(mintAmount))
        .to.emit(token, "TokensBurned")
        .withArgs(addr1.address, mintAmount);
    });

    it("Should emit Transfer event on transfers", async function () {
      const transferAmount = ethers.parseEther("100");

      await expect(token.transfer(addr1.address, transferAmount))
        .to.emit(token, "Transfer")
        .withArgs(owner.address, addr1.address, transferAmount);
    });

    it("Should emit Paused and Unpaused events", async function () {
      await expect(token.pause())
        .to.emit(token, "Paused")
        .withArgs(owner.address);

      await expect(token.unpause())
        .to.emit(token, "Unpaused")
        .withArgs(owner.address);
    });
  });

  // ============================================================
  // Additional Transfer Tests
  // ============================================================
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
      const tooManyTokens = ethers.parseEther("1000");

      await expect(
        token.connect(addr1).transfer(addr2.address, tooManyTokens)
      ).to.be.revertedWithCustomError(token, "ERC20InsufficientBalance");
    });

    it("Should update allowances correctly", async function () {
      const approveAmount = ethers.parseEther("100");

      await token.approve(addr1.address, approveAmount);
      expect(await token.allowance(owner.address, addr1.address)).to.equal(
        approveAmount
      );

      // addr1 transfers from owner to addr2 using allowance
      await token
        .connect(addr1)
        .transferFrom(owner.address, addr2.address, approveAmount);
      expect(await token.balanceOf(addr2.address)).to.equal(approveAmount);
      expect(await token.allowance(owner.address, addr1.address)).to.equal(0);
    });
  });
});
