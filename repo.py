from sqlmodel import Session, select
from models import Employee
from db import engine


class EmployeeRepository:

    def __init__(self, session):
        self.session = session

    def create_employee(self, employee):
        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)
        return employee

    def get_all_employee(self):
        with Session(engine) as session:
            return self.session.exec(select(Employee)).all()

    def get_employee(self, employee_id):
        with Session(engine) as session:
            return self.session.get(Employee, employee_id)

    def update_employee(self, employee_id, data):
        with Session(engine) as session:
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
        with Session(engine) as session:
            employee = self.session.get(Employee, employee_id)
            if employee:
                self.session.delete(employee)
                self.session.commit()
                return True
            return False
