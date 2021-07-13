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


@app.route("/parse_arguments")
def parse_arguments ():
    args=request.args
    name = args["name"]
    job = args["job"]
    height = args["height"]

    return "hello " + name + " " + job + " " + height 


@app.route("/pokemon/<name>")
def pokemon(name):
    pokemondata = rq.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    name = pokemondata["name"]
    iid = pokemondata["id"]
    tyype = pokemondata["types"][0]["type"]["name"]
    return f"{name} is an {tyype} pokemon with {iid}"