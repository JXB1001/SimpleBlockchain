import time
import hashlib
import random

class Block(object):
    def __init__(self, index, proof_number, previous_hash, data):
        """ initial structure of the block class """
        self.block_data = {}
        self.block_data["index"] = index
        self.block_data["proof_number"] = proof_number
        self.block_data["previous_hash"] = previous_hash
        self.block_data["data"] = data
        self.block_data["timestamp"] = time.time()

    def get_proof_number(self):
        return self.block_data["proof_number"]

    def randomise_proof_number(self):
        self.block_data["proof_number"] = random.randint(0, 10**30)

    def compute_hash(self):
        """ producing a crytographic hash of each block """
        string_block = ""
        for data in self.block_data.values():
            string_block += str(data) + " "
            
        return hashlib.sha256(string_block.encode()).hexdigest()

    def print(self):
        print(self.block_data)
        
  

