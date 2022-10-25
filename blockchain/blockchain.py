from flask import Flask, render_template
import requests 


class Blockchain():

    def __init__(self):
        self.transactions = []
        self.chain = []

# instantiating the blockchain
blockchain = Blockchain()

# instantiating the node
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
