from sqlmodel import Session, select
from models import Students


class StudentRepository:

    def __init__(self, session):
        self.session = session

    def create_student(self, student):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get_students(self):
        return self.session.exec(select(Students)).all()

    def get_student(self, id):
        return self.session.get(Students, id)

    def update_student(self, id, data):
        student = self.session.get(Students, id)

        if student:
            student.name = data["name"]
            student.age = data["age"]
            student.marks = data["marks"]
            student.class_school = data["class_school"]

            self.session.commit()
            self.session.refresh(student)

        return student

    def delete_student(self, id):
        student = self.session.get(Students, id)

        if student:
            self.session.delete(student)
            self.session.commit()
            return True

        return False
