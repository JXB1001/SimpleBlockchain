# Services required from the server:
# - create a new transaction
# - mine a new block
# - return the entire chain

import Chain
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Block Chain Fun!"

@app.route("/chain")
def getChain():
    chain_string = ""
    for block in myBlockChain.chain:
        chain_string += str(block)
        chain_string += '\n'
    print(chain_string)
    return chain_string

if __name__ == "__main__":
    myBlockChain = Chain.Chain()
    myBlockChain.mine_block("The Miner")
    myBlockChain.mine_block("Hello")
    app.run()