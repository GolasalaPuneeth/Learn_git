from sqlmodel import create_engine


postgres_url = "postgresql://postgres:Admin123@localhost:5435/my_costume_database"

engine = create_engine(postgres_url, echo=True)