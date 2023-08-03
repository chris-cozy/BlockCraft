from block import Block


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
