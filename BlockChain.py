class BlockChain(object):
    def __init__(self):
    #building the chain
    def build_genesis(self):
        pass
    #creating the initial block
    def build_block(self, proof_number, previous_hash):
        pass
    #builds new block and adds to the chain
   @staticmethod
    def confirm_validity(block, previous_block):
        pass
    #checks whether the blockchain is valid
    def get_data(self, sender, receiver, amount):
        pass
    # declares data of transactions
    @staticmethod
    def proof_of_work(last_proof):
        pass
    #adds to the security of the blockchain
    @property
    def latest_block(self):
        pass
    #returns the last block in the chain