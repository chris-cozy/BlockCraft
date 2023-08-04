# **BlockCraft**

![https://img.shields.io/badge/blockchain-simulator-brightgreen](https://img.shields.io/badge/blockchain-simulator-brightgreen)

BlockCraft is a simple blockchain simulator that emulates the behavior of a decentralized blockchain network. It provides basic functionalities for mining blocks, adding transactions, and saving/loading the blockchain data to/from files. The simulator is designed as an educational tool to understand the fundamental concepts of blockchain technology.

## **Features**

- Create a decentralized blockchain network with multiple nodes.
- Simulate mining of blocks with proof-of-work (PoW) consensus algorithm.
- Execute simple smart contracts during block mining.
- Achieve consensus among nodes to add blocks to the blockchain.
- Mine blocks concurrently using threading.
- Customize blockchain parameters like difficulty and max nonce.
- View and explore the entire blockchain using a user-friendly web interface.
- Simulate real-world scenarios with randomized mining times.
- Handle mining failure and gracefully resolve forks.

## **Requirements**

- Python 3.7
- Flask (for the web interface)

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/chris-cozy/BlockCraft.git
   cd BlockCraft
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

1. Run the blockchain simulator:

   ```bash
   python main.py
   ```

Upon running the simulator, a blockchain network with five nodes will be created.

The blockchain will run for ten rounds. During each round, every node will mine a block. The node which finishes first will call the other nodes for a consensus on the block’s validity.

If the block is valid, it will be added to the official blockchain and each node will update their version.

The contents of the official blockchain will be printed at the end of the simulation.

## **Configuration**

You can configure various blockchain parameters by editing the main.py file:

- **`difficulty`**: Set the difficulty level for mining (higher values make mining more challenging). (`blockchain.py`)
- **`maxNonce`**: Set the maximum value for the nonce during mining. (`blockchain.py`)
- **`rounds`**: Set the number of rounds for concurrent mining. (`main.py`)

## **Smart Contracts**

You can experiment with simple smart contracts by adding Python expressions in the **`contract_script`** parameter while mining a block. The simulator will execute the script during mining and display the result.

## **Contributing**

Contributions to BlockCraft are welcome! Whether it's bug fixes, new features, or improvements to the documentation, feel free to open a pull request.

## **License**

This project is licensed under the MIT License - see the **[LICENSE](https://opensource.org/license/mit/)** file for details.

## **Acknowledgments**

BlockCraft is inspired by various blockchain tutorials and resources available online. The original implementation and improvements were made by [Chris Cozy](https://github.com/chris-cozy).

## **Disclaimer**

This blockchain simulator is intended for educational purposes only and is not suitable for use in production environments. It does not fully implement the security measures required for a real-world blockchain system.
