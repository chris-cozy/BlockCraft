import datetime
import hashlib
import json


class Block:
    def __init__(self, data, timestamp=None):
        if data is None or not data.strip():
            raise ValueError("Block data cannot be empty.")

        self.blockNum = 0
        self.data = data
        self.next = None
        self._hash = None
        # nonce is a pseudo-random number that is utilized as a counter during the process of mining
        self.nonce = 0
        self.prev_hash = 0x0
        if timestamp is not None:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.datetime.now()

    # For calculating the attribute on call
    # You can call this method as an attribute
    @property
    def hash(self):
        if self._hash is None:
            self._hash = self.calculate_hash()
        return self._hash

    def calculate_hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNum).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return (
            "Block Hash: " + str(self.hash) +
            "\nBlockNo: " + str(self.blockNum) +
            "\nBlock Data: " + str(self.data) +
            "\nHashes: " + str(self.nonce) +
            "\n--------------"
        )

    def to_dict(self):
        return {
            "blockNum": self.blockNum,
            "data": self.data,
            "hash": self.hash,
            "nonce": self.nonce,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data_dict):
        block = cls(data_dict['data'])
        block.blockNum = data_dict['blockNum']
        block.hash = data_dict['hash']
        block.nonce = data_dict['nonce']
        block.prev_hash = data_dict['prev_hash']
        block.timestamp = datetime.datetime.fromisoformat(
            data_dict['timestamp'])
        return block
