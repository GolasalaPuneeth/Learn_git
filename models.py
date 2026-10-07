from sqlmodel import Field, SQLModel


class Customers(SQLModel, table=True):
    cus_id: int = Field(primary_key=True)
    f_name: str
    country: str
    age: int


#db.py-configuration
#models.py-tables configuration
#irepo.py-abstractmethod 
#repo.py-structure/source