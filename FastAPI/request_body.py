from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Product(BaseModel):
#     name: str
#     price: int
#     stock: int

# @app.post("/products")
# def create_product(product: Product):
#     return product

class Student(BaseModel):
    name: str
    age: int

class Course(BaseModel):
    name: str
    duration: int

@app.post("/enroll")
def create_enroll(
    student: Student,
    course: Course
):
    return {
        "student": student,
        "course": course
    }