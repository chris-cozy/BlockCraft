from block import Block
from blockchain import Blockchain


def main():
    blockchain = Blockchain()
    numBlocks = 10

    for n in range(numBlocks):
        data = "Block " + str(n + 1)
        block = Block(data)
        elapsed_time = blockchain.time_taken_for_mining(block)

        print(f"Block mined in {elapsed_time:.6f} seconds")

    while blockchain.head is not None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next


if __name__ == "__main__":
    main()
