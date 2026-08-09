from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func1():
    return {"message": "Welcome to FastAPI!"}

@app.get("/about")
def func2():
    return {"framework": "FastAPI", "language": "Python"}

@app.get("/square/{num}")
def func3(num: int):
    return {"number": num, "square": num*num}

@app.get("/greet")
def func4(name: str = "Guest", age: int = 22):
    return {"message": f"{name}! is {age} years old."}

@app.get("/numbers")
def user():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]