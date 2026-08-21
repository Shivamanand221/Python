import jwt

SECRET_KEY = "my-secret-key"

data = {
    "sub": "rohan",
    "role": "student"
}

token = jwt.encode(
    data,
    SECRET_KEY,
    algorithm= "HS256"
)

print(token)

decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print(decoded)