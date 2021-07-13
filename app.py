from flask import Flask, request
import requests as rq
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"


@app.route("/variable/<apple>")
def variable(apple):
    return apple + "!"


@app.route("/greeting/<name1>/<name2>")
def greeting(name1,name2):
    return "hello " + name1 + " " + name2