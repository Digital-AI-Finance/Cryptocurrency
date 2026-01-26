// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title StudentToken
 * @dev A feature-rich ERC20 token with minting, burning, and pausable functionality
 * @notice This token demonstrates common ERC20 extensions for educational purposes
 *
 * Features:
 * - Minting: Owner can mint new tokens up to MAX_SUPPLY
 * - Burning: Any holder can burn their own tokens
 * - Pausable: Owner can pause/unpause all transfers in emergencies
 */
contract StudentToken is ERC20, Ownable, Pausable {
    /// @notice Maximum supply that can ever exist (1 million tokens)
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18;

    /// @notice Emitted when new tokens are minted
    /// @param to The address receiving the minted tokens
    /// @param amount The amount of tokens minted
    event TokensMinted(address indexed to, uint256 amount);

    /// @notice Emitted when tokens are burned
    /// @param from The address whose tokens were burned
    /// @param amount The amount of tokens burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor mints initial supply to deployer
     * Initializes with 100,000 tokens (10% of max supply)
     */
    constructor() ERC20("StudentToken", "STU") Ownable(msg.sender) {
        _mint(msg.sender, 100_000 * 10**18);
    }

    /**
     * @notice Mint new tokens to a specified address
     * @dev Only owner can mint, and total supply cannot exceed MAX_SUPPLY
     * @param to The address to receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @notice Burn tokens from caller's balance
     * @dev Any token holder can burn their own tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @notice Pause all token transfers
     * @dev Only owner can pause. Use in emergencies.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause token transfers
     * @dev Only owner can unpause
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Override _update to enforce pause functionality
     * This hook is called on every transfer, mint, and burn
     * @param from Source address (zero for minting)
     * @param to Destination address (zero for burning)
     * @param value Amount of tokens being transferred
     */
    function _update(address from, address to, uint256 value)
        internal
        override
        whenNotPaused
    {
        super._update(from, to, value);
    }
}
