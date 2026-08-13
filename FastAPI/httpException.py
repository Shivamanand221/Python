from fastapi import FastAPI, HTTPException

app= FastAPI()

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id == 999:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student_id
    }

app1 = FastAPI()

@app1.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id > 3 or product_id < 1:
        raise HTTPException(
            status_code= 404,
            detail= "product not found."
        )
    return {
        "product_id": product_id,
        "message": "product found"
    }


app2 = FastAPI()

@app2.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in [1,2,3]:
        raise HTTPException(
            status_code= 404,
            detail= "user not found"
        )
    return {
        "user id": user_id,
        "message": "user found"
    }