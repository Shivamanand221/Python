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

class Student(BaseModel):
    name: str
    age: int= Field(le=30, ge=18)
    marks: int= Field(le=100, ge=0)

@app5.post("/students")
def student(data: Student):
    return data


#Q.6
app6= FastAPI()

@app6.get("/products/{product_id}")
def product_details(
        product_id: int,
        category: str,
        min_price: int,
        max_price: int
):
    return {
        "product_id":product_id,
        "category": category,
        "min_price": min_price,
        "max_price": max_price
    }

#Q.7
app7= FastAPI()

@app7.post("/login")
def post_data(form_data: OAuth2PasswordRequestForm= Depends()):
    if form_data.username != "rohan" or form_data.password != "12345":
        raise HTTPException(
            status_code=401,
            detail= "Invalid credentials"
        )
    return {"message": "login successful"}


#Q.8
app8=FastAPI()

def check(api_key: str= Header(alias="X-API-KEY")):
    if api_key != "my-secret-key":
        raise HTTPException(
            status_code=401,
            detail="Invalid key"
        )
    return api_key


@app8.get("/secret")
def secrets(api_key: str= Depends(check)):
    return api_key