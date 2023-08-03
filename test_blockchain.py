import unittest
from block import Block
from blockchain import Blockchain


class TestBlock(unittest.TestCase):
    def test_block_creation(self):
        # Test block creation with data and timestamp
        data = "Test Block"
        block = Block(data)
        self.assertEqual(block.data, data)
        self.assertEqual(block.blockNum, 0)
        self.assertEqual(block.nonce, 0)
        self.assertEqual(block.prev_hash, 0x0)

        # Test block creation with empty data (should raise ValueError)
        with self.assertRaises(ValueError):
            Block("")

    def test_block_hash(self):
        # Test block hash calculation
        data = "Test Block"
        block = Block(data)
        self.assertIsNotNone(block.hash)
        self.assertEqual(block.hash, block.calculate_hash())


class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_blockchain_creation(self):
        # Test blockchain creation
        self.assertIsNotNone(self.blockchain)
        self.assertEqual(self.blockchain.difficulty, 20)
        self.assertEqual(self.blockchain.maxNonce, 2**32)
        self.assertEqual(self.blockchain.target, 2**(256 - 20))
        self.assertIsNotNone(self.blockchain.block)
        self.assertIsNotNone(self.blockchain.dummy)
        self.assertIsNotNone(self.blockchain.head)

    def test_mine_block(self):
        data = "Test Data"
        block = Block(data)
        self.blockchain.mine(block)
        # Ensure the mined block is added to the blockchain
        self.assertEqual(self.blockchain.block, block)

    def test_add_block(self):
        data = "Test Data"
        block = Block(data)
        self.blockchain.add(block)
        # Ensure the block is correctly added to the blockchain
        self.assertEqual(self.blockchain.block, block)

    def test_time_taken_for_mining(self):
        data = "Test Data"
        block = Block(data)
        time_taken = self.blockchain.time_taken_for_mining(block)
        # Ensure the time taken is a positive value
        self.assertGreaterEqual(time_taken, 0)

    def test_save_and_load_blockchain(self):
        data1 = "Test Data 1"

        # Create and mine blocks in the first blockchain
        blockchain1 = Blockchain()
        for _ in range(3):
            block = Block(data1)
            blockchain1.mine(block)

        # Save the first blockchain to a file
        blockchain1.save_to_file("test_blockchain.json")

        # Create a second blockchain and load data from the file
        blockchain2 = Blockchain.load_from_file("test_blockchain.json")

        # Ensure both blockchains have the same content
        block1 = blockchain1.head
        block2 = blockchain2.head
        while block1 is not None and block2 is not None:
            self.assertEqual(block1.data, block2.data)
            block1 = block1.next
            block2 = block2.next


if __name__ == "__main__":
    unittest.main()
