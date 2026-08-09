from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/products/{product_id}/users/{user_id}")
def get_product(
    product_id: int = Path(ge=0, le=1000),
    user_id: int = Path(gt=0, lt=101)
):
    return {"product_id": product_id,
            "user_id": user_id
            }

@app.get("/name/{name}")
def get_name(
    name: str = Path(min_length=3, max_length=20)
):
    return {
        "name": name
    }