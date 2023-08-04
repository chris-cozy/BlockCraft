import datetime
import hashlib
import json


class Block:
    def __init__(self, data, contract_script=None, timestamp=None, miner=None):
        """
        Initialize a new Block instance.

        :param data: The data to be stored in the block.
        :param contract_script: (Optional) The smart contract script to be executed during block mining.
        :param timestamp: (Optional) The timestamp of the block. If not provided, the current timestamp will be used.
        """
        if data is None or not data.strip():
            raise ValueError("Block data cannot be empty.")

        self.block_num = 0
        self.data = data
        self.contract_script = contract_script  # The smart contract script
        self.next = None
        self._hash = None
        self.nonce = 0  # nonce is a pseudo-random number that is utilized as a counter during the process of mining
        self.prev_hash = 0x0
        if timestamp is not None:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.datetime.now()
        self.miner = miner
        self.time_to_mine = None

    # For calculating the attribute on call
    # You can call this method as an attribute
    @property
    def hash(self):
        """
        Calculate and return the hash of the block.

        :return: The hash of the block.
        """
        if self._hash is None:
            self._hash = self.calculate_hash()
        return self._hash

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        :return: The calculated hash of the block.
        """
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_num).encode('utf-8')
        )
        return h.hexdigest()

    def to_dict(self):
        """
        Convert the block data to a dictionary.

        :return: A dictionary representation of the block data.
        """
        return {
            "blockNum": self.block_num,
            "data": self.data,
            "script": self.contract_script,
            "hash": self.hash,
            "nonce": self.nonce,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp.isoformat(),
            "miner": self.miner,
            "time_to_mine": self.time_to_mine,
        }

    @classmethod
    def from_dict(cls, data_dict):
        """
        Create a new Block instance from a dictionary.

        :param data_dict: The dictionary containing the block data.
        :return: A new Block instance created from the dictionary.
        """
        block = cls(data_dict['data'])
        block.block_num = data_dict['blockNum']
        block._hash = data_dict['hash']
        block.nonce = data_dict['nonce']
        block.prev_hash = data_dict['prev_hash']
        block.timestamp = datetime.datetime.fromisoformat(
            data_dict['timestamp'])
        block.miner = data_dict["miner"]
        block.time_to_mine = data_dict["time_to_mine"]
        return block

    def __str__(self):
        """
        Return a string representation of the block.

        :return: A string representation of the block.
        """
        return (
            "\n--------------" +
            "\nBlock Hash: " + str(self.hash) +
            "\nBlockNo: " + str(self.block_num) +
            "\nNode Miner: " + str(self.miner) +
            "\nTime Mining: " + str(self.time_to_mine) +
            "\nBlock Data: " + str(self.data) +
            "\nBlock Script: " + str(self.contract_script) +
            "\nHashes: " + str(self.nonce) +
            "\n--------------"
        )
