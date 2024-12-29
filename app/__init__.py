# we import FastAPI from fastapi
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from app.db import init_db, db_session
from app.models import Student, CreateStudent
from app.config import settings

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Lifespan start")
    try:
        init_db()
        print("Database initialized and tables created")
    except Exception as e:
        print(f"Error initializing database: {e}")
    yield
    print("Lifespan end")


# Initialize the fastapi instance to create a server
app = FastAPI(
    title= settings.TITLE,
    description= settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=life_span
)

# Root Get Route to check whether our api is up or down.
@app.get("/")
async def root():
    return {"messag":"API is running successfully"}

@app.get("/test-db")
async def test_db(session: Session = Depends(db_session)):
    print(session)
    return {"message":"Database connection successful"}

# create a student POST endpoint to create a new student
@app.post("/students", status_code=status.HTTP_201_CREATED)
async def create_new_student(student_data: Student, session: Session = Depends(db_session)):
    try:
        # accept data from frontend in function as student_data, then asign student_data
        # to data variable
        data = student_data
        
        statement = select(Student).where(Student.email == data.email)
        isEmailAlreadyExist = session.exec(statement)
        
        if isEmailAlreadyExist:
            raise HTTPException(status_code=401, detail="user with this email already exist.")
        # here, we add our data into session
        session.add(data)
        # commit the data to the database table
        session.commit()
        
        # here we return the created student data from database
        session.refresh(data)
        print(data)
        
        return {"status":True, "message":"student created successfully", "student_data":data}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



# get single student from database and send to the client
@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
async def get_single_students(student_id: str, session: Session= Depends(db_session)):
    print(student_id)
    statement = select(Student).where(Student.student_id == student_id)
    isStudentExist = session.exec(statement).first()
        
    if isStudentExist :
        return {"status":True, "message":"Student fetched successfully", "students_data":isStudentExist} 
    else: 
           
        raise HTTPException(status_code=404, detail="user not found")
    


# delete route to delete student on the basis of id in the database
@app.delete("/students/{student_id}")
async def delete_single_user(student_id: str, session: Session = Depends(db_session)):
    
    if student_id is None:
        raise HTTPException(status_code=422, detail="student_id is rquired")
    statement = select(Student).where(Student.student_id == student_id)
    student = session.exec(statement).first()
    
    if student:
        session.delete(student)
        session.commit()
        return {"status":True, "message":"Student deleted successfully", "student_id":student.student_id}
    
    raise HTTPException(status_code=404, detail="student not found")



# get all students from database and send to the client
@app.get("/students", status_code=status.HTTP_200_OK)
async def get_all_students(session: Session= Depends(db_session)):
    
    statement = select(Student)
    students = session.exec(statement).all()
    
    return {"status":True, "message":"Students fetched successfully", "students_data":students}


    
# create a put request to update the student data in database
# for this purpose we need two types of data
# 1. student_id to check whether student exist or not
# 2. data, that we want to change in our database
@app.put("/students/{student_id}")
async def update_single_student(student_id: str, student_data: CreateStudent, session: Session = Depends(db_session)):
    # validate data
    student_id = student_id
    
    if student_id is None:
        raise HTTPException(status_code=422, detail="Student_id is required.")
    
    statement = select(Student).where(Student.student_id == student_id)
    student = session.exec(statement).first()
        
    if student is None:
        raise HTTPException(status_code=404, detail="Student_id not found")
    
    if student:
        student.first_name = student_data.first_name  or student.first_name
        student.last_name = student_data.last_name  or student.last_name
        student.father_name = student_data.father_name or student.father_name
        student.date_of_birth = student_data.date_of_birth or student.date_of_birth
        student.grade = student_data.grade or student.grade
        student.gender = student_data.gender or student.gender
        student.email = student_data.email or student.email
        student.phone = student_data.phone or student.phone
    
    session.add(student)
    
    session.commit()
    
    session.refresh(student)
    
    return {"status":True, "message":"student updated successfully", "student_data":student}
    