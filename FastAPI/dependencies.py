from fastapi import FastAPI, Depends

def common_data():
    return "hello"

app = FastAPI()

@app.get("/")
def home(data = Depends(common_data)):
    return {
        "data": data
    }


def common_data1():
    return {
        "name": "rohan",
        "age": 21
    }

app1 = FastAPI()

@app1.get("/people")
def get_people(data = Depends(common_data1)):
    return data


app2 = FastAPI()

def common_data2(
        page: int,
        limit: int
    ):
    return {
        "page": page,
        "limit": limit
    }

@app2.get("/students")
def get_students(data = Depends(common_data2)):
    return data


app3 = FastAPI()

def get_name(name: str):
    return name

def get_student(
        course: str,
        data = Depends(get_name)
    ):
    return {
        "name": data,
        "course": course
    }

@app3.get("/student")
def get_course(data = Depends(get_student)):
    return data



app4 = FastAPI()

def check_user(username: str):
    return "Welcome "+username

def get_user_info(
        data = Depends(check_user),
        role = "student"
):
    return {
        "user": data,
        "role": role
    }

@app4.get("/profile")
def get_profile(data = Depends(get_user_info)):
    return data