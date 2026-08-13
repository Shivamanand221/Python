from fastapi import FastAPI

app = FastAPI()

app.get("/students", status_code= 200)
def get_student():
    return {"message": "get student worked"}

app.post("/students", status_code= 201)
def create_student():
    return {"message": "Student Created"}

app.delete("/students/{student_id}", status_code= 204)
def delete_student(student_id: int):
    return