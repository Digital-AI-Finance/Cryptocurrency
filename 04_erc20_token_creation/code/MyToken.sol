// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyToken
 * @dev ERC-20 token implementation with minting and burning capabilities
 * @notice This contract demonstrates standard token functionality
 */
contract MyToken is ERC20, Ownable {
    // Maximum supply cap for the token
    uint256 public constant MAX_SUPPLY = 1000000 * 10**18;  // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that initializes the token
     * @notice Mints initial supply to the contract deployer
     */
    constructor() ERC20("MyToken", "MTK") Ownable(msg.sender) {
        // Mint 100,000 tokens to the deployer (10% of max supply)
        _mint(msg.sender, 100000 * 10**18);
    }

    /**
     * @dev Mint new tokens to a specified address
     * @param to Address that will receive the minted tokens
     * @param amount Amount of tokens to mint (in wei, i.e., with decimals)
     * @notice Only the owner can mint tokens
     * @notice Cannot exceed MAX_SUPPLY
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens from the caller's balance
     * @param amount Amount of tokens to burn (in wei)
     * @notice Any token holder can burn their own tokens
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burn tokens from a specified address (requires allowance)
     * @param from Address from which tokens will be burned
     * @param amount Amount of tokens to burn
     * @notice Requires the caller to have sufficient allowance
     */
    function burnFrom(address from, uint256 amount) public {
        _spendAllowance(from, msg.sender, amount);
        _burn(from, amount);
    }

    /**
     * @dev Returns the number of decimals used for token amounts
     * @return uint8 Number of decimals (18)
     * @notice Overridden for clarity, though OpenZeppelin default is already 18
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }

    /**
     * @dev Batch transfer to multiple addresses
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to transfer
     * @notice Arrays must be of equal length
     */
    function batchTransfer(address[] calldata recipients, uint256[] calldata amounts) public {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        require(recipients.length > 0, "Empty arrays");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Cannot transfer to zero address");
            _transfer(msg.sender, recipients[i], amounts[i]);
        }
    }
}
