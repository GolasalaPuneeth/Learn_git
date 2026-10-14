from sqlmodel import Session, select
from models import Employee
from db import engine


class EmployeeRepository:

    def create_employee(self, employee):
        with Session(engine) as session:        
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return employee

    def get_all_employee(self):
        with Session(engine) as session:
            return session.exec(select(Employee)).all()

    def get_employee(self, employee_id):
        with Session(engine) as session:
            return session.get(Employee, employee_id)

    def update_employee(self, employee_id, data):
        with Session(engine) as session:
            employee = session.get(Employee, employee_id)
            if employee:
                employee.first_name = data["first_name"]
                employee.last_name = data["last_name"]
                employee.department = data["department"]
                employee.salary = data["salary"]
                employee.hire_date = data["hire_date"]
                employee.performance_score = data["performance_score"]
                employee.email = data["email"]
                
                session.commit()
                session.refresh(employee)
            return employee

    def delete_employee(self, employee_id):
        with Session(engine) as session:
            employee = session.get(Employee, employee_id)
            if employee:
                session.delete(employee)
                session.commit()
                return True
            return False
