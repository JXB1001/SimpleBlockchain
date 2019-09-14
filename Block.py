import time
import hashlib

class Block(object):
    def __init__(self, index, proof_number, previous_hash, data):
        """ initial structure of the block class """
        self.blockData = {}
        self.blockData["index"] = index
        self.blockData["proof_number"] = proof_number
        self.blockData["previous_hash"] = previous_hash
        self.blockData["data"] = data
        self.blockData["timestamp"] = time.time()

    def compute_hash(self):
        """ producing a crytographic hash of each block """
        string_block = ""
        for data in self.blockData.values():
            string_block += str(data) + " "
            
        return hashlib.sha256(string_block.encode()).hexdigest()
        
  

