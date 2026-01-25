"""SHA-256 hashing demonstration."""
import hashlib


def sha256_hash(data: str) -> str:
    """Compute SHA-256 hash of the input string."""
    return hashlib.sha256(data.encode()).hexdigest()


def demonstrate_avalanche():
    """Show how small changes produce completely different hashes."""
    text1 = "Hello, Blockchain!"
    text2 = "Hello, Blockchain."  # Only difference: ! vs .

    hash1 = sha256_hash(text1)
    hash2 = sha256_hash(text2)

    print("=" * 70)
    print("AVALANCHE EFFECT DEMONSTRATION")
    print("=" * 70)
    print(f"\nText 1: '{text1}'")
    print(f"Hash 1: {hash1}")
    print(f"\nText 2: '{text2}'")
    print(f"Hash 2: {hash2}")

    # Count differing bits
    diff_bits = bin(int(hash1, 16) ^ int(hash2, 16)).count('1')
    print(f"\nDiffering bits: {diff_bits} out of 256 ({diff_bits/256*100:.1f}%)")
    print("=" * 70)


def demonstrate_determinism():
    """Show that the same input always produces the same hash."""
    text = "Cryptocurrency rocks!"

    print("\n" + "=" * 70)
    print("DETERMINISM DEMONSTRATION")
    print("=" * 70)
    print(f"\nInput: '{text}'")

    for i in range(3):
        print(f"Hash attempt {i+1}: {sha256_hash(text)}")

    print("\nNote: All hashes are identical (deterministic)")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_avalanche()
    demonstrate_determinism()
