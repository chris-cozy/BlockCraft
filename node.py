class Node:
    def __init__(self, node_id, blockchain):
        self.node_id = node_id
        self.blockchain = blockchain

    def mine(self, block):
        self.blockchain.mine(block, self.node_id)

    def vote_for_blockchain(self, blockchain):
        return self.blockchain.vote_for_blockchain(blockchain)

    def get_mined_blocks(self):
        return self.blockchain.mined_blocks

    def update_blockchain(self, new_blocks):
        for block in new_blocks:
            self.blockchain.add(block)
