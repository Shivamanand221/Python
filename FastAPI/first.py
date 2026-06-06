from fastapi import FastAPI

obj1=FastAPI()
@obj1.get("/student/{id}")

def func1(id):
    return {"message": f"Hello, student {id}!"}
