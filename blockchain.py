from block import Block
import json
import hashlib
import time


class Blockchain:
    def __init__(self):
        """
        Initialize a new Blockchain instance.
        """
        # difficulty setting for mining. Increasing this makes the window for acceptable hashes smaller, and increases the time it takes to mine
        self.difficulty = 20
        self.maxNonce = 2**32
        self.target = 2 ** (256 - self.difficulty)
        self.block = Block("Genesis")
        self.dummy = self.head = self.block

    # Adding blocks to the blockchain once they are mined
    def add(self, block):
        """
        Add a new block to the blockchain.

        :param block: The block to be added.
        """
        block.prev_hash = self.block.calculate_hash()
        block.blockNum = self.block.blockNum + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        """
        Mine a new block and add it to the blockchain.

        :param block: The block to be mined.
        """
        for n in range(self.maxNonce):
            block.nonce = n
            if int(block.calculate_hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break

    def time_taken_for_mining(self, block):
        """
        Calculate the time taken to mine a block.

        :param block: The block to be mined.
        :return: The time taken for mining in seconds.
        """
        start_time = time.time()
        self.mine(block)
        end_time = time.time()
        return end_time - start_time

    def to_json(self):
        """
        Convert the blockchain data to JSON format.

        :return: The JSON representation of the blockchain data.
        """
        blockchain_json = []
        block = self.dummy
        while block is not None:
            blockchain_json.append(block.to_dict())
            block = block.next
        return json.dumps(blockchain_json, indent=2)

    def from_json(self, blockchain_json):
        """
        Create a new Blockchain instance from JSON data.

        :param blockchain_json: The JSON representation of the blockchain data.
        """
        blockchain_data = json.loads(blockchain_json)
        for block_data in blockchain_data:
            block = Block.from_dict(block_data)
            self.add(block)

    def save_to_file(self, filename):
        """
        Save the blockchain data to an external file

        :param filename: Name of the file to save the data to.
        """
        blockchain_json = self.to_json()
        with open(filename, 'w') as file:
            file.write(blockchain_json)

    @classmethod
    def load_from_file(cls, filename):
        """
        Load the blockchain data from an external file

        :param filename: Name of the file to download the data from.
        """
        with open(filename, 'r') as file:
            blockchain_json = file.read()
        blockchain = cls()
        blockchain.from_json(blockchain_json)
        return blockchain

    def print_blockchain(self):
        """
        Print the contents of the blockchain.
        """
        while self.head is not None:
            print(self.head)
            self.head = self.head.next
