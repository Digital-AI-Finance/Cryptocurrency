#!/usr/bin/env python3
"""
Web3.py interaction script for SimpleStorage contract.
Demonstrates deployment, transactions, and event listening.

Requirements:
- Local Hardhat node running on http://127.0.0.1:8545
- SimpleStorage.sol compiled with artifacts available
"""

from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import time

# Connection setup
RPC_URL = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Add PoA middleware for development chains
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Verify connection
if not w3.is_connected():
    raise ConnectionError(f"Failed to connect to {RPC_URL}. Is Hardhat running?")

print(f"✓ Connected to Ethereum node")
print(f"  Chain ID: {w3.eth.chain_id}")
print(f"  Latest block: {w3.eth.block_number}\n")

# SimpleStorage contract ABI
CONTRACT_ABI = json.loads('''[
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "internalType": "uint256", "name": "oldValue", "type": "uint256"},
            {"indexed": true, "internalType": "uint256", "name": "newValue", "type": "uint256"},
            {"indexed": true, "internalType": "address", "name": "setter", "type": "address"}
        ],
        "name": "ValueChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"},
            {"indexed": true, "internalType": "address", "name": "retriever", "type": "address"}
        ],
        "name": "ValueRetrieved",
        "type": "event"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "newValue", "type": "uint256"}],
        "name": "setValue",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getValue",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getValueView",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]''')

CONTRACT_BYTECODE = "0x608060405234801561000f575f80fd5b505f80819055506102a98061003e5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c806320965255146100385780635524107714610056578063552410771461005f575b5f80fd5b61004061007b565b60405161004d919061016a565b60405180910390f35b61005d610083565b005b610065610097565b604051610072919061016a565b60405180910390f35b5f5f54905090565b5f805490505f8190556100956100a5565b565b5f5f54905090565b7f93fe6d397c74fdf1402a8b72e47b68512f0510d7b98a4bc4cbdf6ac7108b3c9e5f54336040516100d692919061018e565b60405180910390a1565b5f819050919050565b6100f2816100e0565b82525050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610121826100f8565b9050919050565b61013181610117565b82525050565b5f6040820190506101495f8301856100e9565b6101566020830184610128565b9392505050565b610164816100e0565b82525050565b5f60208201905061017c5f83018461015b565b92915050565b610188816100e0565b82525050565b5f6040820190506101a05f8301856100e9565b6101ad602083018461017f565b939250505056fea2646970667358221220c8e5f8f5e5f5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e564736f6c63430008140033"

# Get default account
account = w3.eth.accounts[0]
print(f"Using account: {account}")
print(f"Balance: {w3.from_wei(w3.eth.get_balance(account), 'ether')} ETH\n")

# Deploy contract
print("Deploying SimpleStorage contract...")
SimpleStorage = w3.eth.contract(abi=CONTRACT_ABI, bytecode=CONTRACT_BYTECODE)

tx_hash = SimpleStorage.constructor().transact({'from': account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"✓ Contract deployed at: {contract_address}")
print(f"  Gas used: {tx_receipt.gasUsed:,}\n")

# Interact with deployed contract
contract = w3.eth.contract(address=contract_address, abi=CONTRACT_ABI)

# Read initial value
initial_value = contract.functions.getValueView().call()
print(f"Initial stored value: {initial_value}\n")

# Set new value
new_value = 42
print(f"Setting value to {new_value}...")
tx_hash = contract.functions.setValue(new_value).transact({'from': account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"✓ Transaction confirmed")
print(f"  Gas used: {tx_receipt.gasUsed:,}\n")

# Read updated value
updated_value = contract.functions.getValueView().call()
print(f"Updated stored value: {updated_value}\n")

# Listen for events in the transaction
print("Events emitted:")
value_changed_filter = contract.events.ValueChanged()
events = value_changed_filter.get_logs(fromBlock=tx_receipt.blockNumber, toBlock=tx_receipt.blockNumber)

for event in events:
    print(f"  ValueChanged event:")
    print(f"    Old value: {event.args.oldValue}")
    print(f"    New value: {event.args.newValue}")
    print(f"    Setter: {event.args.setter}")

print("\n✓ Script completed successfully")
