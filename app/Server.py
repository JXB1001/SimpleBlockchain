# Services required from the server:
# - create a new transaction
# - mine a new block
# - return the entire chain

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()