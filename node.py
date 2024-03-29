class Node:
    def __init__(self, node_id, blockchain):
        self.node_id = node_id
        self.blockchain = blockchain

    def mine(self, block):
        self.blockchain.mine(block, self.node_id)
