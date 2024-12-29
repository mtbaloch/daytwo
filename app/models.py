# we need sqlmodel orm to create models for creating database tables
# but we can also create models that we can use to validate/handle request or response

from sqlmodel import SQLModel, Field
import uuid
from datetime import date
from typing import Optional
# we define explicityly that we are goint to using this model to create
#  table in the database
class Student(SQLModel, table=True):
    # entity
    __tablename__ = "students"
    student_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    last_name: str
    father_name: str
    date_of_birth: date
    gender: str
    grade: str
    email: str = Field(unique=True, index=True)
    phone: str

class CreateStudent(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    father_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    grade: Optional[str] = None
    email: Optional[str] = Field(default=None, unique=True, index=True)
    phone: Optional[str] = None
    