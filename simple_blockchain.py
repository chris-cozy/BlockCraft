#this is the code for a simple blockchain. Essentially an immutable linked list
import datetime
import hashlib

#this is the class for each block
class Block:
    blockNum = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prev_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    #function to calculate the hash
    def hash(self):
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
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNum) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

#the class for the blackchain
class Blockchain:

    #difficulty setting for mining. Increasing this makes the window for acceptable hashes smaller, and increases the time it takes
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    #first block
    block = Block("Genesis")
    dummy = head = block

    #function to add blocks to the blockchain
    def add(self, block):

        block.prev_hash = self.block.hash()
        block.blockNum = self.block.blockNum + 1

        self.block.next = block
        self.block = self.block.next

    #function to mine blocks
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

#creates the blockchain and mines the specified block number
blockchain = Blockchain()
numBlocks = 10

for n in range(numBlocks):
    blockchain.mine(Block("Block " + str(n + 1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next