from hashlib import sha256
import json
import time
import timeit

class Block_ex:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        """
        Constructor for the Block class
        :param index: Unique ID of the stock
        :param timestamp: Time of generation of the block
        :param transactions:List of transactions
        :param previous_hash: Hash of preceding block in the chain which this block is part of
        """
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        """
        A function that return the hash of the block contents
        :return: hash of the block "header"
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:

    difficulty = 2 # the difficulty of the PoW algorithm

    def __init__(self):
        """
        Constructor for the Blockchain class
        """
        self.chain = []
        self.unconfirmed_transactions = []

    def create_genesis_block(self):
        """
        A function that generate genesis block and append it to the chain.
        with index and previous hash 0
        """
        genesis_block = Block_ex(0, [], 0,"0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]


    def add_block(self, block):
        """
        A function that adds a block to the chain after verification
        Verification includes:
        - Proof of work: Checking if the proof is valid
        - The previous hash referred in the block and the hash of the latest block in the chain match
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False
        # 如果目前最后一个区块的hash和即将新加入的block的hash不同 返回False

        self.chain.append(block)
        return True

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    @classmethod
    def check_chain_validility(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # remove the hash field to recompute the hash again
            # using 'compute_hash' method
            delattr(block, "hash")

            if not previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash
        return result

    def mine(self):
        """This function serves as an interface to add the pending transactions to the blockchain by adding thme to the block
        and figuring out Proof of Work"""

        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block_ex(index=last_block.index + 1, transactions=self.unconfirmed_transactions,
                          previous_hash=last_block.hash, timestamp=time.time())
        new_block.hash = new_block.compute_hash()
        self.add_block(new_block)
        self.unconfirmed_transactions = []
        return True

#
# # /new_transaction
# def new_transaction():
#     tx_data = request
#
#
# def consensus():
#     """
#     Our naive consnsus algorithm. If a longer valid chain is
#     found, our chain is replaced with it.
#     """
#     global blockchain
#
#     longest_chain = None
#     current_len = len(blockchain.chain)
#
#     for node in peers:
#         response = requests.get('{}chain'.format(node))
#         length = response.json()['length']
#         chain = response.json()['chain']
#         if length > current_len and blockchain.check_chain_validity(chain):
#             current_len = length
#             longest_chain = chain
#
#     if longest_chain:
#         blockchain = longest_chain
#         return True
#
#     return False
#
#
# def announce_new_block(block):
#     """
#     A function to announce to the network once a block has been mined.
#     Other blocks can simply verify the proof of work and add it to their
#     respective chains.
#     """
#     for peer in peers:
#         url = "{}add_block".format(peer)
#         headers = {'Content-Type': "application/json"}
#         requests.post(url,
#                       data=json.dumps(block.__dict__, sort_keys=True),
#                       headers=headers)