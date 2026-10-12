from sqlmodel import SQLModel,Field
from uuid import UUID, uuid4

class Students(SQLModel, table=True):
    __tablename__ = "students"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    age: int
    marks: int
    class_school: int
