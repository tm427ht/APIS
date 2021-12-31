from flask import Flask, request, jsonify
from flask_cors import CORS 
import mysql.connector as sql 

app = Flask(__name__)
CORS(app)

database = sql.connect(
    host="147.232.40.14",
    user="kr124gz",
    password="Mieg2fei",
    database="kr124gz"
)

cursor = database.cursor(dictionary = True)

def ddl_readline(file_name, values=[]):
    with open(file_name) as file:
        return file.read().format(*values).strip('\n')

@app.route("/customers", methods = ["GET"])
def get_customers():
    query = ddl_readline("DDL/CUSTOMERS/SELECT.ddl")
    cursor.execute(query)
    return jsonify(cursor.fetchall()), 200

@app.route("/customers", methods = ["POST"])
def post_customers(): 
    data = dict(request.get_json(force = True))
    values = [data["Name"], data["Address"], data["PhoneNumber"]]
    query = ddl_readline("DDL/CUSTOMERS/INSERT.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("New customer has been added."), 201

@app.route("/customers", methods = ["PUT"])
def put_customers(): 
    data = dict(request.get_json(force = True))
    values = [data["Name"], data["Address"], data["PhoneNumber"], data["Id"]]
    query = ddl_readline("DDL/CUSTOMERS/UPDATE.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("Customer has been updated"), 201

@app.route("/customers/<id>", methods = ["DELETE"])
def delete_customers(id):
    query = ddl_readline("DDL/CUSTOMERS/DELETE.ddl", [id])
    cursor.execute(query)
    database.commit()
    return jsonify(f"Customer with id {id} has been deleted."), 204

@app.route("/products", methods = ["GET"])
def get_products():
    query = ddl_readline("DDL/PRODUCTS/SELECT.ddl")
    cursor.execute(query)
    return jsonify(cursor.fetchall()), 200

@app.route("/products", methods = ["POST"])
def post_products(): 
    data = dict(request.get_json(force = True))
    values = [data["Name"], data["Quantity"], data["Price"]]
    query = ddl_readline("DDL/PRODUCTS/INSERT.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("New product has been added"), 201

@app.route("/products", methods = ["PUT"])
def put_products(): 
    data = dict(request.get_json(force = True))
    values = [data["Name"], data["Quantity"], data["Price"], data["Id"]]
    query = ddl_readline("DDL/PRODUCTS/UPDATE.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("Product has been updated"), 201

@app.route("/products/<id>", methods = ["DELETE"])
def delete_products(id):
    query = ddl_readline("DDL/PRODUCTS/DELETE.ddl", [id])
    cursor.execute(query)
    database.commit()
    return jsonify(f"Product with id {id} has been deleted."), 204

@app.route("/orders", methods = ["GET"])
def get_orders():
    query = ddl_readline("DDL/ORDERS/SELECT.ddl")
    cursor.execute(query)
    return jsonify(cursor.fetchall()), 200

@app.route("/orders", methods = ["POST"])
def post_order(): 
    data = dict(request.get_json(force = True))
    values = [data["Quantity"], data["CustomerId"], data["ProductId"]]
    query = ddl_readline("DDL/ORDERS/INSERT.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("New order has been added"), 201

@app.route("/orders", methods = ["PUT"])
def put_orders(): 
    data = dict(request.get_json(force = True))
    values = [data["Quantity"], data["CustomerId"], data["ProductId"], data["Id"]]
    query = ddl_readline("DDL/ORDERS/UPDATE.ddl", values)
    cursor.execute(query)
    database.commit()
    return jsonify("Order has been updated"), 201

@app.route("/orders/<id>", methods = ["DELETE"])
def delete_orders(id):
    query = ddl_readline("DDL/ORDERS/DELETE.ddl", [id])
    cursor.execute(query)
    database.commit()
    return jsonify(f"Order with id {id} has been deleted."), 204

if __name__ == "__main__":
    app.run()
