from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

app= FastAPI()

SECRET_KEY= "my-secret-key"

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm= Depends()):
    if form_data.username != "rohan" or form_data.password != "12345":
        raise HTTPException(
            status_code= 401,
            detail= "invalid credentials"
        )

    data = {
        "sub": form_data.username,
        "role": "student"
    }

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm = "HS256"
    )
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/profile")
def get_profile(token: str= Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid token"
        )

    return {
        "username": payload["sub"],
        "role": payload["role"]
    }


app2= FastAPI()

class auth:
    def __init__(self, user_id: int, role: str):
        self.user_id= user_id
        self.role= role


@app2.post("/token")
def post_token(form_data: auth= Depends()):

    if form_data.user_id != 101 or form_data.role != "admin":
        raise HTTPException(
            status_code= 403,
            detail= "Admin access denied"
        )

    data = {
        "user_id": form_data.user_id,
        "role": form_data.role
    }

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm= "HS256"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app2.get("/dashboard")
def get_role(token: str= Depends(oauth2_scheme)):
    
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid token"
        )

    if payload["role"] != "admin":
        raise HTTPException(
            status_code= 403,
            detail= "Admin access denied"
        )

    return {
            "user_id": payload["user_id"],
            "role": payload["role"]
        }