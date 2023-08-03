from block import Block
import json


class Blockchain:

    # difficulty setting for mining. Increasing this makes the window for acceptable hashes smaller, and increases the time it takes to mine
    difficulty = 20
    maxNonce = 2**32
    target = 2 ** (256 - difficulty)

    def __init__(self):
        self.block = Block("Genesis")
        self.dummy = self.head = self.block

    # Adding blocks to the blockchain once they are mined
    def add(self, block):
        block.prev_hash = self.block.calculate_hash()
        block.blockNum = self.block.blockNum + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.calculate_hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

    def to_json(self):
        blockchain_json = []
        block = self.dummy
        while block is not None:
            blockchain_json.append(block.to_dict())
            block = block.next
        return json.dumps(blockchain_json, indent=2)

    def from_json(self, blockchain_json):
        blockchain_data = json.loads(blockchain_json)
        for block_data in blockchain_data:
            block = Block.from_dict(block_data)
            self.add(block)