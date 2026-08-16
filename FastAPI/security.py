from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.security import HTTPBearer

app = FastAPI()

@app.get("/profile")
def get_profile(authorization: str = Header()):

    if authorization != "bearer abc123":
        raise HTTPException(
            status_code= 401,
            detail= "invalid token"
        )
    return {
        "message": "Access granted"
    }


app2 = FastAPI()

security = HTTPBearer()

@app2.get("/profiles")
def get_profiles(credentials = Depends(security)):
    return {
        "token": credentials.credentials
    }


app3 = FastAPI()

@app3.get("/data")
def get_data(api_key: str = Header(alias="X-API-Key")):
    if api_key != "my-secret-key":
        raise HTTPException(
            status_code= 401,
            detail= "invalid API key"
        )
    return {
        "message": "Access granted"
    }

app4 = FastAPI()

def verify_api_key(api_key: str = Header(alias = "X-API-Key")):
    if api_key != "my-secret-key":
        raise HTTPException(
            status_code = 401,
            detail= "Unauthorized"
        )
    return {
        "message": "Access Granted"
    }

@app4.get("/mydata")
def get_mydata(data = Depends(verify_api_key)):
    return data


app5 = FastAPI()

security = HTTPBearer()

@app5.get("/myprofile")
def verify_profile(credentials = Depends(security)):
    if credentials.credentials != "abc123":
        raise HTTPException(
            status_code= 401,
            detail= "Unauthorized"
        )
    return {
        "message": "Access Granted"
    }