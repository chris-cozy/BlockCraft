import datetime
import hashlib


class Block:
    def __init__(self, data):
        self.blockNum = 0
        self.data = data
        self.next = None
        self.hash = None
        self.nonce = 0
        self.prev_hash = 0x0
        self.timestamp = datetime.datetime.now()

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
            "Block Hash: " + str(self.calculate_hash()) +
            "\nBlockNo: " + str(self.blockNum) +
            "\nBlock Data: " + str(self.data) +
            "\nHashes: " + str(self.nonce) +
            "\n--------------"
        )
