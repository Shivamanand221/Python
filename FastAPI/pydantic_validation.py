from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

app = FastAPI()

# class Student(BaseModel):
#     name: str
#     age: int
#     course: str
#     marks: int = 0

# @app.post("/students")
# def create_student(student: Student):
#     return student


# Nested Models

# class Address(BaseModel):
#     city: str
#     pincode: int

# class Student(BaseModel):
#     name: str
#     age: int
#     address: Address

# @app.post("/students")
# def student_details(student: Student):
#     return {
#         "student": student
#     }




# class Student(BaseModel):
#     name: str
#     age: int
#     course: str
#     marks: int = 0
#     subjects: list[str]
#     nickname: str | None = None

# @app.post("/students")
# def create_student(student: Student):
#     return student



# class Student(BaseModel):
#     name: str = Field(min_length=3, max_length=20)
#     age: int = Field(ge=18, le=100)
#     course: str = Field(min_length=2, max_length=30)
#     marks: int = Field(default=0, ge=0, le=100)
#     subjects: list[str]
#     nickname: str | None = None

# @app.post("/students")
# def create_student(student: Student):
#     return student



# Custom Validation
"""
class Student(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if value.lower()== "admin":
            raise ValueError("Name cannnot be admin")
        return value

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be greater than or equal to 18")
        return value

@app.post("/students")
def create_student(student: Student):
    return student
"""



# Model Validation

class Student(BaseModel):
    age: int
    course: str

    @model_validator(mode="after")
    def validate_student(self):
        if self.age< 18 and self.course.lower()== "fastapi":
            raise ValueError("Students under 18 cannot take FastAPI")
        return self

@app.post("/students")
def create_student(student: Student):
    return student