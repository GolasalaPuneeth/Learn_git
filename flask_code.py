from flask import Flask, request, jsonify
from sqlmodel import SQLModel,Session
from db import engine
from models import Customers
from repository import Repo


app = Flask(__name__)

SQLModel.metadata.create_all(engine)

@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.json
    customer = Customers(
        cus_id=data["cus_id"],
        f_name=data["f_name"],
        country=data["country"],
        age=data["age"]
    )
    with Session(engine) as session:
        repository = Repo(session)
        customer = repository.create_customer(customer)
        return jsonify({
            "cus_id": customer.cus_id,
            "f_name": customer.f_name,
            "country": customer.country,
            "age": customer.age
        }), 201


# READ ALL
@app.route("/customers", methods=["GET"])
def get_customers():
    with Session(engine) as session:
        repository = Repo(session)
        customers = repository.get_customers()
        data = []
        for customer in customers:
            data.append(customer.model_dump())
        return jsonify(data)


# READ ONE
@app.route("/customers/<int:cus_id>", methods=["GET"])
def get_customer(cus_id):
    with Session(engine) as session:
        repository = Repo(session)
        customer = repository.get_customer(cus_id)
        if customer:
            return jsonify(customer.model_dump())
        return jsonify({
            "message": "Customer not found"
        }), 404


# UPDATE
@app.route("/customers/<int:cus_id>", methods=["PUT"])
def update_customer(cus_id):
    data = request.json
    with Session(engine) as session:
        repository = Repo(session)
        customer = repository.update_customer(
            cus_id,
            data["f_name"],
            data["country"],
            data["age"]
        )
        if customer:
            return jsonify(customer.model_dump())
        return jsonify({
            "message": "Customer not found"
        }), 404


# DELETE
@app.route("/customers/<int:cus_id>", methods=["DELETE"])
def delete_customer(cus_id):
    with Session(engine) as session:
        repository = Repo(session)
        result = repository.delete_customer(cus_id)
        if result:
            return jsonify({
                "message": "Customer deleted successfully"
            })
        return jsonify({
            "message": "Customer not found"
        }), 404


if __name__=='__main__':
    app.run(port=8001,host='0.0.0.0',debug=True)