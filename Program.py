import Block

if __name__ == "__main__":
    myBlock = Block.Block(0, 0, 0, "my first block")
    myHash = myBlock.compute_hash()
    print(myHash)