from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL

sklad = Flask(__name__)
CORS(sklad)

ovocie = ["jablko", "pomaranc", "jahoda"]

@sklad.route("/", methods = ["GET"])
def main(): 
    return jsonify({"ovocie": ovocie}), 200

@sklad.route("/vytvorit", methods = ["POST"])
def create(): 
    data = request.get_json(force = True)
    data_dict = dict(data)
    ovocie.append(data_dict["vytvorit"])
    return jsonify("created"), 201

@sklad.route("/upravit/<id>", methods = ["PUT"])
def update(id):
    data = request.get_json(force = True)
    data_dict = dict(data)
    ovocie[int(id)] = data_dict["upravit"]
    return jsonify("update"), 201

@sklad.route("/vymazat/<id>", methods = ["DELETE"])
def delete(id): 
    del ovocie[int(id)]
    return jsonify("deleted"), 204

if __name__ == "__main__": 
    sklad.run

