#create intial table setup
from sqlmodel import SQLModel
from db import engine
from models import Students

if __name__=="__main__":
    SQLModel.metadata.create_all(engine)
