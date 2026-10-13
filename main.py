from flask import Flask, request, jsonify
from sqlmodel import Session
# from uuid import UUID

from db import engine
# from models import Students
from models import Employee
from repo import EmployeeRepository 
# from repo import StudentRepository


app = Flask(__name__)


@app.post("/employee")
def create():
    data = request.json

    employee = Employee(
        first_name = data["first_name"],
        last_name = data["last_name"],
        department = data["department"],
        salary = data["salary"],
        hire_date = data["hire_date"],
        performance_score = data["performance_score"],
        email = data["email"]
    )

    with Session(engine) as session:
        repo = EmployeeRepository(session)
        employee = repo.create_employee(employee)

        return jsonify({
            "employee_id": employee.employee_id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "department": employee.department,
            "salary": employee.salary,
            "hire_date": employee.hire_date,
            "performance_score": employee.performance_score,
            "email": employee.email
        })


@app.get("/employees")
def get_all():
    with Session(engine) as session:
        repo = EmployeeRepository(session)
        employees = repo.get_all_employee()
        result = []
        for employee in employees:
            result.append({
                "employee_id": employee.employee_id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "department": employee.department,
                "salary": employee.salary,
                "hire_date": employee.hire_date,
                "performance_score": employee.performance_score,
                "email": employee.email
            })
        return jsonify(result)


@app.get("/employees/<int:employee_id>")
def get_one(employee_id):
    with Session(engine) as session:
        repo = EmployeeRepository(session)
        employee = repo.get_employee(employee_id)
        if employee:
            return jsonify({
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "department": employee.department,
                "salary": employee.salary,
                "hire_date": employee.hire_date,
                "performance_score": employee.performance_score,
                "email": employee.email
            })
        return jsonify({"message": "employee not found"}), 404


@app.put("/employees/<int:employee_id>")
def update(employee_id):
    data = request.json
    with Session(engine) as session:
        repo = EmployeeRepository(session)
        employee = repo.update_employee(employee_id, data)
        if employee:
            return jsonify({
               "employee_id": employee.employee_id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "department": employee.department,
                "salary": employee.salary,
                "hire_date": employee.hire_date,
                "performance_score": employee.performance_score,
                "email": employee.email
            })
        return jsonify({"message": "employee not found"}), 404


@app.delete("/employees/<int:employee_id>")
def delete(employee_id):
    with Session(engine) as session:
        repo = EmployeeRepository(session)
        result = repo.delete_employee(employee_id)
        if result:
            return jsonify({"message": "employee deleted"})
        return jsonify({"message": "employee not found"}), 404
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8001,debug=True)