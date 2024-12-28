# we need sqlmodel orm to create models for creating database tables
# but we can also create models that we can use to validate/handle request or response

from sqlmodel import SQLModel, Field
import uuid
from datetime import date
# we define explicityly that we are goint to using this model to create
#  table in the database
class Student(SQLModel, table=True):
    # entity
    __tablename__ = "students"
    student_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    last_name: str
    father_name: str
    date_of_birth: date
    gender: str
    grade: str
    email: str = Field(unique=True, index=True)
    phone: str
    