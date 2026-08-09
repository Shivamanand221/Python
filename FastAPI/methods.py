from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return{"message": "Getting users"}

@app.post("/users")
def create_user():
    return {"message": "creating user"}

@app.put("/users")
def update_user():
    return {"message": "updating user"}

@app.patch("/users")
def partial_update_user():
    return {"message": "partially updating user"}

@app.delete("/users")
def delete_user():
    return {"message": "delete user"}