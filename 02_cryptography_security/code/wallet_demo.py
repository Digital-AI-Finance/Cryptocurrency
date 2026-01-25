"""Cryptocurrency wallet demonstration - key generation and address derivation."""
from ecdsa import SigningKey, SECP256k1
import hashlib
from typing import Tuple


def generate_keypair() -> Tuple[str, str]:
    """Generate a new ECDSA key pair."""
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()

    private_key_hex = private_key.to_string().hex()
    public_key_hex = public_key.to_string().hex()

    return private_key_hex, public_key_hex


def public_key_to_ethereum_address(public_key_hex: str) -> str:
    """Derive Ethereum-style address from public key.

    Process:
    1. Hash public key with Keccak-256
    2. Take last 20 bytes
    3. Add '0x' prefix
    """
    # Note: Using SHA-256 instead of Keccak-256 for simplicity
    # (Keccak-256 requires additional library)
    public_key_bytes = bytes.fromhex(public_key_hex)
    hash_digest = hashlib.sha256(public_key_bytes).digest()

    # Take last 20 bytes
    address_bytes = hash_digest[-20:]
    address = '0x' + address_bytes.hex()

    return address


def demonstrate_wallet():
    """Demonstrate wallet key generation and address derivation."""
    print("=" * 70)
    print("CRYPTOCURRENCY WALLET DEMONSTRATION")
    print("=" * 70)

    # Generate key pair
    private_key, public_key = generate_keypair()

    print("\n1. GENERATED KEY PAIR")
    print("-" * 70)
    print(f"Private Key (hex):")
    print(f"  {private_key}")
    print(f"\nPublic Key (hex, uncompressed):")
    print(f"  {public_key}")

    # Derive Ethereum-style address
    address = public_key_to_ethereum_address(public_key)

    print("\n2. DERIVED ETHEREUM-STYLE ADDRESS")
    print("-" * 70)
    print(f"Address: {address}")

    print("\n3. KEY MANAGEMENT WARNINGS")
    print("-" * 70)
    print("⚠️  NEVER share your private key!")
    print("⚠️  Loss of private key = loss of funds (irreversible)")
    print("⚠️  Public key and address can be safely shared")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_wallet()
