from sqlmodel import Session, select
# from models import Students
from models import Employee


# class StudentRepository:

#     def __init__(self, session):
#         self.session = session

#     def create_student(self, student):
#         self.session.add(student)
#         self.session.commit()
#         self.session.refresh(student)
#         return student

#     def get_students(self):
#         return self.session.exec(select(Students)).all()

#     def get_student(self, id):
#         return self.session.get(Students, id)

#     def update_student(self, id, data):
#         student = self.session.get(Students, id)

#         if student:
#             student.name = data["name"]
#             student.age = data["age"]
#             student.marks = data["marks"]
#             student.class_school = data["class_school"]

#             self.session.commit()
#             self.session.refresh(student)

#         return student

#     def delete_student(self, id):
#         student = self.session.get(Students, id)

#         if student:
#             self.session.delete(student)
#             self.session.commit()
#             return True

#         return False


class EmployeeRepository:

    def __init__(self, session):
        self.session = session

    def create_employee(self, employee):
        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)
        return employee

    def get_all_employee(self):
        return self.session.exec(select(Employee)).all()

    def get_employee(self, employee_id):
        return self.session.get(Employee, employee_id)

    def update_employee(self, employee_id, data):
        employee = self.session.get(Employee, employee_id)
        if employee:
            employee.first_name = data["first_name"]
            employee.last_name = data["last_name"]
            employee.department = data["department"]
            employee.salary = data["salary"]
            employee.hire_date = data["hire_date"]
            employee.performance_score = data["performance_score"]
            employee.email = data["email"]
            
            self.session.commit()
            self.session.refresh(employee)
        return employee

    def delete_employee(self, employee_id):
        employee = self.session.get(Employee, employee_id)
        if employee:
            self.session.delete(employee)
            self.session.commit()
            return True
        return False
