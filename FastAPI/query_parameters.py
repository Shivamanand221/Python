from fastapi import FastAPI, Query

app= FastAPI()

"""
@app.get("/users")
def get_users(name):
    return {"Name":name}

@app.get("/products")
def get_users(limit: int=10):
    return {"limit": limit}

@app.get("/items")
def get_users(name: str = None, price: int=10):
    return {"Name": name, "price": price}

@app.get("/category")
def get_category(
    name: str = "shivam",
    price: int =2 00,
    age: int = 20
):
    return {
        "Name": name,
        "price": price,
        "age": age
        }
"""

#@app.get("/products/{product_id}")
#def get_product(product_id: int):
#    return {"product_id": product_id}

@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id: int, order_id: int):
    return {
        "user_id": user_id,
        "order_id": order_id
    }

"""
@app.get("/products")
def get_product(
    product_id: int,
    category: str= "all"
):
    return{
        "product_id": product_id,
        "category": category
    }
"""

"""
@app.get("/users")
def get_users(
    user_id: int = Query(ge=1, le=10000),
    name: str = Query(min_length=3, max_length=20)
):
    return {
        "user_id": user_id,
        "name": name
    }
"""

@app.get("/search")
def get_search(
    keyword: str = Query(min_length=3, max_length=10),
    tag: list[str] = Query(min_length=2)
):
    return {
        "keyword": keyword,
        "tag": tag
    }