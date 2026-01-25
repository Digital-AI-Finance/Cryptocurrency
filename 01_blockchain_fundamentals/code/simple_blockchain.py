"""Complete standalone blockchain demonstration."""
import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        new_block = Block(
            len(self.chain),
            transactions,
            self.get_latest_block().hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        print("\n" + "="*60)
        print("BLOCKCHAIN CONTENTS")
        print("="*60)
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"  Timestamp: {time.ctime(block.timestamp)}")
            print(f"  Transactions: {block.transactions}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Nonce: {block.nonce}")
            print(f"  Hash: {block.hash}")
        print("="*60)

if __name__ == "__main__":
    print("Creating blockchain with difficulty 2...")
    bc = Blockchain(difficulty=2)

    print("\nAdding transactions...")
    bc.add_block("Alice sends 10 BTC to Bob")
    bc.add_block("Bob sends 5 BTC to Charlie")
    bc.add_block("Charlie sends 2 BTC to Dave")

    bc.display_chain()

    print(f"\nBlockchain valid: {bc.is_chain_valid()}")

    print("\nAttempting to tamper with block 1...")
    bc.chain[1].transactions = "Alice sends 1000 BTC to Eve (TAMPERED)"
    print(f"Blockchain valid after tampering: {bc.is_chain_valid()}")
