from block import Block
from blockchain import Blockchain
import time
from node import Node
import random


def main():
    """
    Entry point of the blockchain simulator.
    """
    try:
        # Create a network of nodes with their respective blockchains
        num_nodes = 5
        nodes = []
        for i in range(num_nodes):
            blockchain = Blockchain()
            node = Node(node_id=i+1, blockchain=blockchain)
            nodes.append(node)

        # Mine blocks concurrently
        num_blocks_to_mine = 10
        for i in range(num_blocks_to_mine):
            for node in nodes:
                data = f"Node {node.node_id} - Block {i}"
                block = Block(data)
                node.mine(block)

        # Achieve consensus
        nodes[random.randint(0, len(nodes) - 1)].blockchain.consensus(nodes)

        # Print final blockchain for each node
        print("\nNode blockchains:")
        for node in nodes:
            print(f"Node {node.node_id} blockchain:")
            node.blockchain.print_blockchain()

    except ValueError as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
