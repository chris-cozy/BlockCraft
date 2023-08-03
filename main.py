from block import Block
from blockchain import Blockchain


def main():
    blockchain = Blockchain()
    numBlocks = 10

    for n in range(numBlocks):
        data = "Block " + str(n + 1)
        block = Block(data)
        blockchain.mine(block)

    while blockchain.head is not None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next


if __name__ == "__main__":
    main()
