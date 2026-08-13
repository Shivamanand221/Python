from fastapi import FastAPI, Header

app= FastAPI()

@app.get("/info")
def get_info(user_agent: str= Header()):
    return {
        "user_agent": user_agent
    }

app1= FastAPI()

@app1.get("/info")
def get_info(
    user_agent: str = Header(),
    accept: str = Header()
):
    return {
        "user_agent": user_agent,
        "accept": accept
    }

app2 = FastAPI()

@app2.get("/profile")
def get_profile(
    user_agent: str = Header(),
    accept: str = Header(),
    authorization: str = Header()
):
    return {
        "user_agent": user_agent,
        "accept": accept,
        "authorization": authorization
    }