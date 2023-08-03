from block import Block
from blockchain import Blockchain
import time


def main():
    """
    Entry point of the blockchain simulator.
    """
    # Each node represents a computer
    node1 = Blockchain()
    numBlocks = 10

    for n in range(numBlocks):
        data = "Node 1 - Block " + str(n + 1)
        block = Block(data)
        node1.mine(block)

    # Save the blockchain to a file
    node1.save_to_file("node1_blockchain.json")
    print("Node 1 blockchain saved to file.")

    # Simulate a network latency for demonstration purposes
    time.sleep(2)

    # Create second node and load blockchain from file
    node2 = Blockchain.load_from_file("node1_blockchain.json")
    print("Node 2 blockchain loaded from file.")

    numBlocks = 5

    for n in range(numBlocks):
        data = "Node 2 - Block " + str(n + 1)
        block = Block(data)
        node2.mine(block)

    # Print blockchain contents for both nodes
    print("\nNode 1 blockchain:")
    node1.print_blockchain()
    print("\nNode 2 blockchain:")
    node2.print_blockchain()


if __name__ == "__main__":
    main()
