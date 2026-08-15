from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
def create_user(
    username: str = Form(),
    password: str = Form()
):
    return {
        "username": username,
        "password": password
    }

app1 = FastAPI()

@app1.post("/feedback")
def create_feedback(
    name: str = Form(),
    rating: int = Form(),
    feedback: str = Form()
):
    return {
        "name": name,
        "rating": rating,
        "feedback": feedback
    }