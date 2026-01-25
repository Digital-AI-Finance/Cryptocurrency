// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StudentToken
 * @dev YOUR NAME - YOUR STUDENT ID
 * @notice Customize this token for your final project
 *
 * INSTRUCTIONS:
 * 1. Replace "YOUR NAME" and "YOUR STUDENT ID" above
 * 2. Change the token name and symbol in the constructor
 * 3. Add at least ONE custom feature from the list below
 * 4. Test your implementation thoroughly
 *
 * SUGGESTED FEATURES (choose at least one):
 * - Minting: Allow owner to mint new tokens
 * - Burning: Allow users to burn their tokens
 * - Pausable: Emergency stop mechanism
 * - Transfer Fee: Charge a small fee on transfers
 * - Whitelist: Only allow transfers to/from whitelisted addresses
 * - Vesting: Lock tokens for a specific period
 * - Staking: Allow users to stake tokens for rewards
 * - Voting: Token holders can vote on proposals
 */
contract StudentToken is ERC20, Ownable {
    // Token parameters - TODO: Adjust these values
    uint256 public constant INITIAL_SUPPLY = 1000000 * 10**18; // 1 million tokens

    // TODO: Add state variables for your custom features here
    // Example: bool public paused;
    // Example: uint256 public transferFeePercent = 1;

    /**
     * @dev Constructor initializes the token
     * TODO: Change "YourTokenName" and "YTN" to your custom values
     */
    constructor()
        ERC20("YourTokenName", "YTN")  // TODO: Customize name and symbol
        Ownable(msg.sender)
    {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // ============================================================
    // TODO: ADD YOUR CUSTOM FEATURES BELOW
    // ============================================================

    /**
     * @dev Example: Mint function (only owner can mint)
     * Uncomment and modify if you want minting functionality
     */
    // function mint(address to, uint256 amount) public onlyOwner {
    //     _mint(to, amount);
    // }

    /**
     * @dev Example: Burn function (anyone can burn their own tokens)
     * Uncomment and modify if you want burning functionality
     */
    // function burn(uint256 amount) public {
    //     _burn(msg.sender, amount);
    // }

    // Add more custom functions here...
}
