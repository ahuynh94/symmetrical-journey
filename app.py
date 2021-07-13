from flask import flask, request
import requests as rq
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"