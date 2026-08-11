from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()

"""
class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/students", response_model=Student)
def get_student():
    return {
        "name": "abcde",
        "age": 21,
        "course": "def",
        "password": "string123"
    }
"""

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

@app.get("/students", response_model=StudentResponse)
def get_students():
    return {
        "id": 1,
        "name": "abcde",
        "age": 19,
        "course": "eng",
        "marks": 76,
        "password": "secret123"
    }