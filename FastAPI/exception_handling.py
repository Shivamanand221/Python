from fastapi import FastAPI, HTTPException

app= FastAPI()

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 101:
        raise HTTPException(
            status_code= 404,
            detail= "Student not found"
        )

    return {
        "id": 101,
        "name": "rohan"
    }


app1= FastAPI()

@app1.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id != 101:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )

    return {
        "id": 101,
        "name": "laptop"
    }


app2= FastAPI()

@app2.get("/students/{student_id}")
def get_students(student_id: int):

    students= {
        101: "Rohan",
        102: "Aman",
        103: "Rahul"
    }

    if student_id not in students:
        raise HTTPException(
            status_code= 404,
            detail= "Student not found"
        )

    return {
        "id": student_id,
        "name": students[student_id]
    }


app3= FastAPI()

@app3.get("/products/{product_id}")
def get_products(product_id: int):

    products = {
        101: {"name": "Laptop", "price": 50000},
        102: {"name": "Phone", "price": 30000},
        103: {"name": "Tablet", "price": 20000}
    }

    if product_id not in products:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )
    
    if products[product_id]["price"]>30000:
        raise HTTPException(
            status_code= 400,
            detail= "Product is too expensive"
        )

    return {
        "id": product_id,
        "name": products[product_id]["name"],
        "price": products[product_id]["price"]
    }