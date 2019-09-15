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
    return "myChain"

if __name__ == "__main__":
    app.run()