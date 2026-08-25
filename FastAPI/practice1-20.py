from fastapi import FastAPI, HTTPException, Query, Path, Header, Cookie
from fastapi import Request, Response, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator, model_validator
import jwt
from datetime import datetime, timedelta, timezone

#Q.1

app= FastAPI()

@app.get("/users/{user_id}")
def user_info(
    user_id: int,
    name: str
):
    return {
        "user_id": user_id,
        "name": name
    }


#Q.2
app2= FastAPI()

class product_info(BaseModel):
    name: str
    price: int

@app2.post("/products")
def product(details: product_info):
    return details


#Q.3
app3= FastAPI()

@app3.get("/device")
def devices(
    user_agent: str= Header(),
    x_device_id: int= Header()
):
    return {
        "user-agent": user_agent,
        "X-Device-ID": x_device_id
    }

#Q.4
app4= FastAPI()

@app4.post("/register")
def register():
    return JSONResponse(
        status_code=201,
        content={"message": "user registered"}
    )

#Q.5
app5= FastAPI()

@app5.post("/students")
class Student(BaseModel):
    name: str
    age: int= Field(le=30, ge=18)
    marks: int= Field(le=100, ge=0)

def student(data: Student):
    return data
