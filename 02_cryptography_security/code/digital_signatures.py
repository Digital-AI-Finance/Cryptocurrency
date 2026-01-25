"""Digital signature demonstration using ECDSA."""
from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
import hashlib


def create_keypair():
    """Generate a new ECDSA key pair."""
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key


def sign_message(private_key: SigningKey, message: str) -> bytes:
    """Sign a message using the private key."""
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = private_key.sign_digest(message_hash, sigencode=lambda r, s, order: r.to_bytes(32, 'big') + s.to_bytes(32, 'big'))
    return signature


def verify_signature(public_key: VerifyingKey, message: str, signature: bytes) -> bool:
    """Verify a signature using the public key."""
    try:
        message_hash = hashlib.sha256(message.encode()).digest()
        public_key.verify_digest(signature, message_hash, sigdecode=lambda sig, order: (int.from_bytes(sig[:32], 'big'), int.from_bytes(sig[32:], 'big')))
        return True
    except BadSignatureError:
        return False


def demonstrate_signatures():
    """Demonstrate digital signature creation and verification."""
    print("=" * 70)
    print("DIGITAL SIGNATURE DEMONSTRATION")
    print("=" * 70)

    # Create key pair
    private_key, public_key = create_keypair()
    print("\n1. Generated key pair (SECP256k1 curve)")
    print(f"   Private key: {private_key.to_string().hex()[:32]}...")
    print(f"   Public key:  {public_key.to_string().hex()[:32]}...")

    # Sign a message
    message = "Transfer 10 BTC to Alice"
    signature = sign_message(private_key, message)
    print(f"\n2. Signed message: '{message}'")
    print(f"   Signature: {signature.hex()[:32]}...")

    # Verify valid signature
    is_valid = verify_signature(public_key, message, signature)
    print(f"\n3. Verification with correct public key: {is_valid}")

    # Tamper with message
    tampered_message = "Transfer 100 BTC to Alice"
    is_valid_tampered = verify_signature(public_key, tampered_message, signature)
    print(f"\n4. Verification with tampered message: {is_valid_tampered}")

    # Verify with wrong key
    _, wrong_public_key = create_keypair()
    is_valid_wrong_key = verify_signature(wrong_public_key, message, signature)
    print(f"\n5. Verification with wrong public key: {is_valid_wrong_key}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_signatures()
