from block import Block
from blockchain import Blockchain
import time
from node import Node
import random
import threading


def mine_concurrently(node, data, finish_times, first_finished):
    """
    Mine blocks concurrently for a specific time.

    :param node: The node performing the mining.
    :param mining_time: The time (in seconds) for mining.
    """
    block = Block(data, miner=node.node_id)
    node.mine(block)

    finish_times[node.node_id] = time.time()
    first_finished.set()  # Ensure that other threads are aware that a thread has finished


def main():
    """
    Entry point of the blockchain simulator.
    """
    try:
        # Create central blockchain
        source_blockchain = Blockchain()
        # Create a network of nodes
        num_nodes = 5
        nodes = []
        for i in range(num_nodes):
            node_blockchain = Blockchain()
            node = Node(node_id=i+1, blockchain=node_blockchain)
            nodes.append(node)

        # Mine blocks concurrently
        rounds = 10
        current_round = 0
        while current_round < rounds:
            data = f"Round {current_round}"
            # Create shared variable for tracking the first thread that finishes
            first_finished = threading.Event()
            finish_times = {}

            # Create threads for concurrent mining
            threads = []
            for node in nodes:
                thread = threading.Thread(
                    target=mine_concurrently, args=(node, data, finish_times, first_finished))
                threads.append(thread)
                thread.start()

            first_finished.wait()

            # Wait for all threads to finish
            for thread in threads:
                # thread.join()
                if thread.is_alive():
                    thread.join(timeout=0)

            first_finished.clear()

            node_won_id = min(finish_times, key=finish_times.get)
            print(f'\nNode {node_won_id} finished first.')

            node_won = nodes[node_won_id - 1]
            potential_block = node_won.blockchain.mined_block

            # Achieve consensus
            if source_blockchain.consensus(nodes, potential_block):
                source_blockchain.add(potential_block)
                print(str(potential_block))

            for node in nodes:
                node.blockchain.mined_block = None
                node.blockchain = source_blockchain

            # Sleep before starting next round
            time.sleep(1)
            current_round += 1

        print("\nBlockChain:")
        source_blockchain.print_blockchain()

    except ValueError as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
