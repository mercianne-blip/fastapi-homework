from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

# 2. First FastAPI Application
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 3. Path Parameters
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}

# 4. Query Parameters
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/products/")
async def read_products(name: str, page: int = 1):
    return {"name": name, "page": page}

# 5. Request Body
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

@app.post("/items/")
async def create_item(item: Item):
    return item

# 6. Pydantic Models
class User(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(ge=18)

# 8. Response Models
class UserOut(BaseModel):
    username: str
    email: EmailStr

@app.post("/users/", response_model=UserOut)
async def create_user(user: User):
    return user