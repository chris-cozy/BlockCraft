import unittest
import os
from main import main
from blockchain import Blockchain
from block import Block
import time


class IntegrationTest(unittest.TestCase):
    def test_blockchain_integration(self):
        # Define a test scenario
        num_blocks = 5

        # Create a new blockchain instance
        blockchain = Blockchain()

        # Mine blocks and add them to the blockchain
        for n in range(num_blocks):
            data = "Test Block " + str(n + 1)
            block = Block(data)
            blockchain.mine(block)

        # Save the blockchain to a file
        filename = "test_blockchain1.json"
        blockchain.save_to_file(filename)
        self.assertTrue(os.path.exists(filename))

        # Simulate a network latency for demonstration purposes
        time.sleep(1)

        # Create a new blockchain instance and load from file
        new_blockchain = Blockchain.load_from_file(filename)
        filename = "test_blockchain2.json"
        new_blockchain.save_to_file(filename)
        self.assertIsInstance(new_blockchain, Blockchain)


if __name__ == "__main__":
    unittest.main()
