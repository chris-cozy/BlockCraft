from block import Block
from blockchain import Blockchain
import time
from node import Node


def main():
    """
    Entry point of the blockchain simulator.
    """
    try:
        node1_blockchain = Blockchain()
        node1 = Node(node_id=1, blockchain=node1_blockchain)
        num_blocks_to_mine = 5

        for n in range(num_blocks_to_mine):
            data = f"Node {node1.node_id} - Block {n + 1}"
            block = Block(data)
            node1.mine(block)

        # Simulate a network latency for demonstration purposes
        time.sleep(2)

        node2_blockchain = Blockchain()
        node2 = Node(node_id=2, blockchain=node2_blockchain)

        for n in range(num_blocks_to_mine):
            data = f"Node {node1.node_id} - Block {n + 1}"
            block = Block(data)
            node1.mine(block)

        # Achieve consensus
        nodes = [node1, node2]
        node1.blockchain.consensus(nodes)

        # Print final blockchain for each node
        print("\nNode 1 blockchain:")
        node1.blockchain.print_blockchain()
        print("\nNode 2 blockchain:")
        node2.blockchain.print_blockchain()

    except ValueError as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
