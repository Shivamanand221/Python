from fastapi import FastAPI, Cookie, Response

app = FastAPI()

@app.get("/profile")
def get_profile(session_id: str = Cookie()):
    return {
        "session_id": session_id
    }


app1 = FastAPI()

@app1.get("/login")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123"
        )
    return {
        "message": "logged in"
    }


app2 = FastAPI()

@app2.get("/logout")
def logout(response: Response):
    response.delete_cookie(
        key= "session_id",
        value= "abc123"
    )
    return {
        "message": "logged out"
    }