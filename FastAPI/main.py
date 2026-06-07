from fastapi import FastAPI

obj1=FastAPI()

@obj1.get("/student/{id}")
def func1(id):
    return {"message": f"Hello, student {id}!"}

@obj1.get("/teacher/{id}")
def func2(id):
    return {"message": f"Hello, teacher {id}!"}

@obj1.get("/teachers")
def func3():
    return {"message": ["teacher1", "teacher2", "teacher3"]}
