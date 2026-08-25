from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/hello")
def hello():
    return {"message": "hello"}



app1= FastAPI()

app1.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost/3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"]
)

@app1.get("/hello")
def hello():
    return {"message": "hello"}



app2= FastAPI()

app2.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:3000"],
    allow_methods= ["GET", "POST"],
    allow_headers= ["Content-Type", "Authorization"],
    allow_credentials= True
)

@app2.get("/profile")
def profile():
    return {
        "username": "rohan",
        "role": "student"
    }