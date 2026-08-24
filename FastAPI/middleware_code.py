from fastapi import FastAPI, Request
import time

app= FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):

    print("Request: ", request.method, request.url)

    response = await call_next(request)

    print("Response sent")

    return response

@app.get("/hello")
def hello():
    return {"message": "hello"}


app2= FastAPI()

@app2.middleware("http")
async def middleware_type(request: Request, call_next):

    print("Request sent", request.method, request.url)

    response = await call_next(request)

    print("Response sent")

    return response

@app2.get("/hello")
def hello():
    return {"message": "hello"}



app3= FastAPI()

@app3.middleware("http")
async def middleware_time(request: Request, call_next):

    start_time= time.time()

    response= await call_next(request)

    end_time= time.time()

    print("Processing time: ",end_time-start_time)

    return response

@app3.get("/hello")
def hello():
    return {"message": "Hello"}



app4= FastAPI()

@app4.middleware("http")
async def middleware_header(request: Request, call_next):

    start_time= time.time()

    response= await call_next(request)

    end_time= time.time()

    processing_time= end_time-start_time

    response.headers["processing_time"]= str(processing_time)

    return response

@app4.get("/hello")
def hello():
    return {"message": "Hello"}