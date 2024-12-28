from sqlmodel import create_engine, Session, SQLModel
from app.models import Student
from typing import Generator
from app.config import settings

# database connection string to connect with db using engine
db_connection_string = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg2")

# create engine which manages the connection to the database and its connection pool
engine = create_engine(db_connection_string, pool_recycle=300)

# funciton that we use in lifespan to create tables in the database using models
def init_db()-> None:
    SQLModel.metadata.create_all(engine)
    
# we use this function as middleware to build session for data transfering with database
def db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
    