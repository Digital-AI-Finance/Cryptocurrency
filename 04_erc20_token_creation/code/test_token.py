#!/usr/bin/env python3
"""
Test script for MyToken ERC-20 contract using web3.py
Demonstrates transfer, balance checking, and approve/transferFrom
"""

from web3 import Web3
import json

# Configuration
RPC_URL = "http://127.0.0.1:8545"  # Local Hardhat/Ganache node
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"  # Update after deployment

# ERC-20 ABI (standard interface)
ERC20_ABI = json.loads('''[
    {"inputs":[],"name":"name","outputs":[{"type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"symbol","outputs":[{"type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"decimals","outputs":[{"type":"uint8"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"totalSupply","outputs":[{"type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"name":"to","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"type":"bool"}],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"type":"bool"}],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"type":"bool"}],"stateMutability":"nonpayable","type":"function"}
]''')


def main():
    # Connect to blockchain
    print("Connecting to blockchain...")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))

    if not w3.is_connected():
        print("ERROR: Cannot connect to blockchain node")
        return

    print(f"Connected! Chain ID: {w3.eth.chain_id}\n")

    # Load contract
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ERC20_ABI)

    # Get accounts
    accounts = w3.eth.accounts
    owner = accounts[0]
    recipient = accounts[1]
    spender = accounts[2]

    print(f"Owner: {owner}")
    print(f"Recipient: {recipient}")
    print(f"Spender: {spender}\n")

    # Test 1: Get token information
    print("=== Token Information ===")
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    total_supply = contract.functions.totalSupply().call()

    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Decimals: {decimals}")
    print(f"Total Supply: {total_supply / 10**decimals} {symbol}\n")

    # Test 2: Check balances
    print("=== Initial Balances ===")
    owner_balance = contract.functions.balanceOf(owner).call()
    print(f"Owner balance: {owner_balance / 10**decimals} {symbol}")

    recipient_balance = contract.functions.balanceOf(recipient).call()
    print(f"Recipient balance: {recipient_balance / 10**decimals} {symbol}\n")

    # Test 3: Transfer tokens
    print("=== Transfer Test ===")
    transfer_amount = 1000 * 10**decimals  # Transfer 1000 tokens
    print(f"Transferring {transfer_amount / 10**decimals} {symbol} from owner to recipient...")

    tx_hash = contract.functions.transfer(recipient, transfer_amount).transact({'from': owner})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction hash: {tx_hash.hex()}")
    print(f"Status: {'Success' if receipt['status'] == 1 else 'Failed'}\n")

    # Check new balances
    print("=== Updated Balances ===")
    owner_balance = contract.functions.balanceOf(owner).call()
    recipient_balance = contract.functions.balanceOf(recipient).call()
    print(f"Owner balance: {owner_balance / 10**decimals} {symbol}")
    print(f"Recipient balance: {recipient_balance / 10**decimals} {symbol}\n")

    # Test 4: Approve and transferFrom
    print("=== Approve & TransferFrom Test ===")
    approve_amount = 500 * 10**decimals
    print(f"Recipient approving spender for {approve_amount / 10**decimals} {symbol}...")

    tx_hash = contract.functions.approve(spender, approve_amount).transact({'from': recipient})
    w3.eth.wait_for_transaction_receipt(tx_hash)

    allowance = contract.functions.allowance(recipient, spender).call()
    print(f"Allowance: {allowance / 10**decimals} {symbol}\n")

    # TransferFrom
    transfer_from_amount = 200 * 10**decimals
    print(f"Spender transferring {transfer_from_amount / 10**decimals} {symbol} from recipient to owner...")

    tx_hash = contract.functions.transferFrom(recipient, owner, transfer_from_amount).transact({'from': spender})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Status: {'Success' if receipt['status'] == 1 else 'Failed'}\n")

    # Final balances
    print("=== Final Balances ===")
    print(f"Owner: {contract.functions.balanceOf(owner).call() / 10**decimals} {symbol}")
    print(f"Recipient: {contract.functions.balanceOf(recipient).call() / 10**decimals} {symbol}")
    print(f"Remaining allowance: {contract.functions.allowance(recipient, spender).call() / 10**decimals} {symbol}")

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    main()
