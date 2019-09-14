import Block
import Chain

if __name__ == "__main__":
    blockchain = Chain.Chain()

    print("Starting the Program")
    print(blockchain.chain)

    blockchain.get_data(
        sender="0",
        receiver="Jacob",
        amount=1
    )

    block = blockchain.mine_block("Miner")

    block = blockchain.mine_block("Andrew")

    print("Mining Sucuessful")
    print(blockchain.chain)
    print("\n\n")
    for block in blockchain.chain:
        block.print()
        print("")

