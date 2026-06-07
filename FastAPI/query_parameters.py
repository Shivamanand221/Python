from fastapi import FastAPI

app= FastAPI()

@app.get("/users")
def get_users(name):
    return {"Name":name}

@app.get("/products")
def get_users(limit: int=10):
    return {"limit": limit}

@app.get("/items")
def get_users(name: str = None, price: int=10):
    return {"Name": name, "price": price}
