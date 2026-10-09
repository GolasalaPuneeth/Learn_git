from flask import Flask, request, jsonify
from sqlmodel import Session
from uuid import UUID

from db import engine
from models import Students
from repo import StudentRepository


app = Flask(__name__)


@app.route("/students", methods=["POST"])
def create():
    data = request.json

    student = Students(
        name=data["name"],
        age=data["age"],
        marks=data["marks"],
        class_school=data["class_school"]
    )

    with Session(engine) as session:
        repo = StudentRepository(session)
        student = repo.create_student(student)

        return jsonify({
            "id": str(student.id),
            "name": student.name,
            "age": student.age,
            "marks": student.marks,
            "class_school": student.class_school
        })


@app.route("/students", methods=["GET"])
def get_all():
    with Session(engine) as session:
        repo = StudentRepository(session)
        students = repo.get_students()

        result = []

        for student in students:
            result.append({
                "id": str(student.id),
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
                "class_school": student.class_school
            })

        return jsonify(result)


@app.route("/students/<id>", methods=["GET"])
def get_one(id):
    with Session(engine) as session:
        repo = StudentRepository(session)
        student = repo.get_student(UUID(id))

        if student:
            return jsonify({
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
                "class_school": student.class_school
            })

        return jsonify({"message": "Student not found"}), 404


@app.route("/students/<id>", methods=["PUT"])
def update(id):
    data = request.json

    with Session(engine) as session:
        repo = StudentRepository(session)

        student = repo.update_student(UUID(id), data)

        if student:
            return jsonify({
                "id": str(student.id),
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
                "class_school": student.class_school
            })

        return jsonify({"message": "Student not found"}), 404


@app.route("/students/<id>", methods=["DELETE"])
def delete(id):
    with Session(engine) as session:
        repo = StudentRepository(session)

        result = repo.delete_student(UUID(id))

        if result:
            return jsonify({"message": "Student deleted"})

        return jsonify({"message": "Student not found"}), 404


app.run(host='0.0.0.0',port=8001,debug=True)