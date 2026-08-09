from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}


@app.get("/products")
def get_products():
    return {"products": ["Laptop", "Phone"]}