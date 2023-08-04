from block import Block
import json
import hashlib
import time
import ast


class Blockchain:
    def __init__(self):
        """
        Initialize a new Blockchain instance.
        """
        self.difficulty = 20  # difficulty setting for mining. Increasing this makes the window for acceptable hashes smaller, and increases the time it takes to mine
        self.maxNonce = 2**32
        self.target = 2 ** (256 - self.difficulty)
        self.block = Block("Genesis")
        self.dummy = self.head = self.block
        self.mined_blocks = []  # Store mined blocks for consensus voting

    # Adding blocks to the blockchain once they are mined
    def add(self, block):
        """
        Add a new block to the blockchain.

        :param block: The block to be added.
        """
        if block is None:
            raise ValueError("Invalid block. Cannot add None block.")

        block.prev_hash = self.block.calculate_hash()
        block.blockNum = self.block.blockNum + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block, miner_id):
        """
        Mine a new block and add it to the blockchain.

        :param block: The block to be mined.
        :param miner_id: The ID of the node that mined the block.
        """
        if block is None:
            raise ValueError("Invalid block. Cannot mine None block.")

        block.miner = miner_id

        if block.contract_script:
            try:
                # Execute the smart contract script
                result = self.execute_contract(block.contract_script)
                print("Smart contract executed. Result: ", result)
            except Exception as e:
                raise ValueError("Error executing smart contract.") from e

        for n in range(self.maxNonce):
            block.nonce = n
            if int(block.calculate_hash(), 16) <= self.target:
                self.mined_blocks.append(block)
                print(block)
                break
        else:
            raise ValueError("Mining failed. Couldn't find a valid hash.")

    def is_valid_blockchain(self, blockchain):
        """
        Check if a blockchain is valid.

        :param blockchain: The blockchain to check.
        :return: True if the blockchain is valid, False otherwise.
        """
        # Check the proof of work for each block
        for i, block in enumerate(blockchain):
            if i == 0:  # Skip the genesis block
                continue
            if int(block.calculate_hash(), 16) > self.target:
                return False
            if block.prev_hash != blockchain[i - 1].calculate_hash():
                return False
        return True

    def consensus(self, nodes):
        """
        Achieve consensus among nodes.

        :param nodes: A list of nodes in the network.
        """
        max_length = 0
        max_length_blockchain = None

        for node in nodes:
            potential_blockchain = node.get_mined_blocks()
            if self.is_valid_blockchain(potential_blockchain) and len(potential_blockchain) > max_length:
                max_length = len(potential_blockchain)
                max_length_blockchain = potential_blockchain

        if max_length_blockchain:
            for node in nodes:
                node.update_blockchain(max_length_blockchain)

            self.mined_blocks.clear()

            print("Consensus reached. Updated blockchain:")
            self.print_blockchain()
        else:
            print("Consensus not reached. Current blockchain remains unchanged.")

    def execute_contract(self, contract_script):
        """
        Execute the smart contract script.

        :param contract_script: The smart contract script to be executed.
        :return: The result of the contract execution.
        """
        # We'll support basic arithmetic expressions
        try:
            result = eval(contract_script)
            return result
        except Exception as e:
            raise ValueError("Error executing smart contract.") from e

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
        Convert the blockchain data to JSON format, excluding genesis block.

        :return: The JSON representation of the blockchain data.
        """
        blockchain_json = []
        block = self.dummy
        while block is not None:
            if block.data == "Genesis":
                block = block.next
            blockchain_json.append(block.to_dict())
            block = block.next
        return json.dumps(blockchain_json, indent=2)

    def from_json(self, blockchain_json):
        """
        Create a new Blockchain instance from JSON data.

        :param blockchain_json: The JSON representation of the blockchain data.
        """
        try:
            blockchain_data = json.loads(blockchain_json)
            for block_data in blockchain_data:
                block = Block.from_dict(block_data)
                self.add(block)
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(
                "Invalid JSON data. Cannot load blockchain.") from e

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
