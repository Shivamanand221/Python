from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()

@app.post("/uploads")
def upload_file(file: UploadFile = File()):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }


app1 = FastAPI()

@app1.post("/profile")
def create_profile(
        name: str = Form(),
        age: int = Form(),
        file: UploadFile = File()
):
    return {
        "name": name,
        "age": age,
        "filename": file.filename,
        "content_type": file.content_type
    }