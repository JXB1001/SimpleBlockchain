from Block import Block

class Chain(object):
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genesis()

    def build_genesis(self):
        """ creating the inital block """
        self.build_block(proof_number=0,previous_hash=0)

    def build_block(self, proof_number, previous_hash):
        """ build new block and adds to the chain """
        block = Block(
            index = len(self.chain),
            proof_number = proof_number,
            previous_hash = previous_hash,
            data = self.current_data
        )
        self.current_data = []
        self.chain.append(block)
        return block
   
    @staticmethod
    def confirm_validity(block, previous_block):
        """ checks weather the blockchain is valid """
        if previous_block.index + 1 != block.index:
            return False
        elif previous_block.compute_hash != block.previous_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False
        return True

    def get_data(self, sender, receiver, amount):
        """ declares data of transactions """
        self.current_data.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        """ adds to the security of the blockchain """
        pass

    @property
    def latest_block(self):
        """ returns the last block in the chain """
        return self.chain[-1]

    def mine_block(self, miner):
        self.get_data(sender="0",receiver=miner,amount=1)

        last_block = self.latest_block
        last_proof_number = last_block.get_proof_number()
        proof_number = self.proof_of_work(last_proof_number)

        last_hash = last_block.compute_hash
        block = self.build_block(proof_number, last_hash)

        return vars(block)