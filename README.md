# **BlockCraft - Simple Blockchain Simulator**

BlockCraft is a simple blockchain simulator that emulates the behavior of a decentralized blockchain network. It provides basic functionalities for mining blocks, adding transactions, and saving/loading the blockchain data to/from files. The simulator is designed as an educational tool to understand the fundamental concepts of blockchain technology.

## **Features**

- Create a blockchain network with multiple nodes (computers).
- Simulate mining blocks with a Proof-of-Work (PoW) consensus algorithm.
- Add custom data (transactions) to blocks.
- Saving and loading blockchain data to/from an external file

## Requirements

- Python 3.7 or higher

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/BlockCraft.git
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

4. Run the blockchain simulator

   ```bash
   python main.py
   ```

## \***\*How to Use\*\***

- Upon running the simulator, two nodes (representing computers) will be created.
- Each node will mine a specified number of blocks and add them to the blockchain.
- The blockchain data will be saved to a file named **`node1_blockchain.json`**.
- After a brief network latency simulation, the second node will load the blockchain from the file and continue mining additional blocks.
- The contents of the blockchain for both nodes will be printed at the end of the simulation.

## **Documentation**

### **`main.py`**

The **`main.py`** script serves as the entry point for the BlockCraft blockchain simulator. It creates two nodes (representing computers) in the blockchain network and simulates mining blocks with custom data. The blockchain data of the first node is saved to a file, and the second node loads the saved blockchain and continues mining additional blocks.

### **`block.py`**

The **`block.py`** module contains the **`Block`** class, which represents an individual block in the blockchain. It includes methods to calculate the block's hash, convert block data to a dictionary, and load block data from a dictionary.

- **`Block(data, timestamp=None)`**: Initializes a new **`Block`** instance with the given data and an optional timestamp. If no timestamp is provided, the current timestamp is used.
- **`calculate_hash()`**: Calculates the hash of the block using the block's data, previous hash, timestamp, nonce, and block number.
- **`to_dict()`**: Converts the block data to a dictionary.
- **`from_dict(data_dict)`**: Creates a new **`Block`** instance from a dictionary containing the block data.
- **`__str__()`**: Returns a string representation of the block, displaying its hash, block number, data, nonce, and previous hash.

### **`blockchain.py`**

The **`blockchain.py`** module contains the **`Blockchain`** class, which represents the blockchain network. It includes methods to add blocks, mine blocks, calculate the time taken for mining, convert the blockchain data to JSON format, load the blockchain data from JSON, save the blockchain to a file, and load the blockchain from a file.

- **`Blockchain()`**: Initializes a new **`Blockchain`** instance with the default difficulty setting for mining.
- **`add(block)`**: Adds a new block to the blockchain.
- **`mine(block)`**: Mines a new block using the Proof-of-Work (PoW) consensus algorithm and adds it to the blockchain.
- **`time_taken_for_mining(block)`**: Calculates the time taken to mine a block.
- **`to_json()`**: Converts the blockchain data to JSON format.
- **`from_json(blockchain_json)`**: Creates a new **`Blockchain`** instance from JSON data.
- **`save_to_file(filename)`**: Saves the blockchain data to an external file.
- **`load_from_file(filename)`**: Loads the blockchain data from an external file and creates a new **`Blockchain`** instance.
- **`print_blockchain()`**: Prints the contents of the blockchain.

## **Customization**

You can customize the behavior of the blockchain simulator by modifying the **`main.py`**, **`block.py`**, and **`blockchain.py`** files. The following parameters can be adjusted:

- Mining difficulty (self.difficulty) in **`blockchain.py`**: Increasing the difficulty makes mining blocks more computationally expensive and takes longer.
- Number of blocks to mine (numBlocks) in **`main.py`**: Change the value to specify how many blocks each node should mine.

## **Contributions**

Contributions to BlockCraft are welcome! Whether it's bug fixes, new features, or improvements to the documentation, feel free to open a pull request.

## **License**

This project is licensed under the MIT License - see the **[LICENSE](https://opensource.org/license/mit/)** file for details.

## **Credits**

BlockCraft is inspired by various blockchain tutorials and resources available online. The original implementation and improvements were made by [Chris Cozy](https://github.com/chris-cozy).
