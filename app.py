from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL


app = Flask(__name__)
CORS(app)

product = {
    "ID" : {0, 1, 2, 3},
    "Price" : {150.99, 100.99, 120.99, 200.99},
    "Name" : {"Volkswagen", "LandRover", "Peugeot", "Skoda"}
}

@app.route("/", methods=["GET"])
def main():
    return jsonify({"ovocie":ovocie}),200

@app.route("/vytvorit", methods=["POST"])
def create():
    data = request.get_json(force=True)
    data_dict = dict(data)
    product.append(data_dict["vytvorit"])
    return jsonify("created"),201

@app.route("/upravit/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    product[int(id)] = data_dict["upravit"]
    return jsonify("updated"),201

@app.route("/vymazat/<id>", methods=["DELETE"])
def delete(id):
    del product[int(id)]
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
