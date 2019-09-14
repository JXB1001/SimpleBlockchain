import Block
import Chain

if __name__ == "__main__":
    blockchain = Chain.Chain()

    print("Starting the Program")
    print(blockchain.chain)

    last_block = blockchain.latest_block
    last_proof_number = last_block.get_proof_number()
    proof_number = blockchain.proof_of_work(last_proof_number)

    blockchain.get_data(
        sender="0",
        receiver="Jacob",
        amount=1
    )

    last_hash = last_block.compute_hash()
    block = blockchain.mine_block("Jacob")

    print("Mining Sucuessful")
    print(blockchain.chain)
