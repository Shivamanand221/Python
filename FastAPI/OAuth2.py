from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme)):
    return {
        "token": token
    }

app1 =FastAPI()

oauth2_scheme1 = OAuth2PasswordBearer(tokenUrl="token")

@app1.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "rohan" or form_data.password != "12345":
        raise HTTPException(
            status_code= 401,
            detail= "invalid credentials"
        )
    return {
        "access_token": "abc123",
        "token_type": "bearer"
    }

@app1.get("/profile")
def get_profile(token: str= Depends(oauth2_scheme1)):
    return {
        "token": token
    }

app2 =FastAPI()

oauth2_scheme2 = OAuth2PasswordBearer(tokenUrl= "StudentData")

class data:
    def __init__(self, name: str= Form(), age: int= Form()):
        self.name= name
        self.age= age

@app2.post("/StudentData")
def login(form_data: data= Depends()):
    if form_data.name != "rohan" or form_data.age != 21 :
        raise HTTPException(
            status_code= 401,
            detail= "invalid credentials"
        )
    return {
        "access_token": "abc123",
        "token_type": "bearer"
    }

@app2.get("/student")
def get_student(token: str= Depends(oauth2_scheme2)):
    return {
        "token": token
    }

app3= FastAPI()

oauth2_scheme3= OAuth2PasswordBearer(tokenUrl="products")

class ProductFilter:
    def __init__(self, name: str= Form(), category: str= Form(), price: int= Form()):
        self.name= name
        self.category= category
        self.price= price

@app3.post("/products")
def product_info(filter_data: ProductFilter= Depends()):
    if filter_data.name != "iphone" or filter_data.category != "mobile" or filter_data.price != 50000:
        raise HTTPException(
            status_code= 401,
            detail= "invalid credentials"
        )
    return {
        "access_token": "abc123",
        "token_type": "bearer"
    }

@app3.get("/products")
def get_product(token: str = Depends(oauth2_scheme3)):
    return {
        "token": token
    }