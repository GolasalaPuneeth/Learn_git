from sqlmodel import SQLModel,Field
from datetime import date


class Employee(SQLModel, table=True):
    __tablename__ = "employee"
    employee_id: int | None=Field(default=None,primary_key=True)
    first_name: str
    last_name: str
    department: str
    salary: float
    hire_date : date
    performance_score : int
    email : str
