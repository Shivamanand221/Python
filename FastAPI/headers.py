from fastapi import FastAPI, Header

app= FastAPI()

@app.get("/info")
def get_info(user_agent: str= Header()):
    return {
        "user_agent": user_agent
    }
