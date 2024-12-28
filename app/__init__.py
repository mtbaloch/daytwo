# we import FastAPI from fastapi
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from app.db import init_db, db_session
from app.models import Student
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