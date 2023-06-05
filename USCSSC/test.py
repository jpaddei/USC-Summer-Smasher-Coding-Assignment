from typing import Union, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from uuid import UUID, uuid4


app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    variant: str
    sku: str
    price: float
    qty: int
    description: str

db: List[Item] = [
    Item(
        id = uuid4(),
        name = "CZero Pen Brand",
        variant = "Red Pen",
        sku = "CZPR",
        price = 1.00,
        qty = 5,
        description = "High quality pens that are carbon-neutral"
    ),
    Item(
        id = uuid4(),
        name = "CZero Pen Brand",
        variant = "Blue Pen",
        sku = "CZPB",
        price = 1.00,
        qty = 5,
        description = "High quality pens that are carbon-neutral"
    ),
    Item(
        id = uuid4(),
        name = "CZero Pen Brand",
        variant = "Green Pen",
        sku = "CZPG",
        price = 1.00,
        qty = 5,
        description = "High quality pens that are carbon-neutral"
    ),
    Item(
        id = uuid4(),
        name = "Red's Pens",
        variant = "Black Fountain Pen",
        sku = "RPG",
        price = 5.00,
        qty = 100,
        description = "Fountain pens designed by Paul Red"
    ),
    Item(
        id = uuid4(),
        name = "Red's Pens",
        variant = "Purple Fountain Pen",
        sku = "PRG",
        price = 5.00,
        qty = 100,
        description = "Fountain pens designed by Paul Red"
    ),
    Item(
        id = uuid4(),
        name = "Good Quality Pencil",
        variant = "",
        sku = "BYP",
        price = .5,
        qty = 1000,
        description = "Handmade Pencils"
    ),
]

inventory = []

@app.get("/api/v1/items")
def read_item():
    return db

# add product to db
@app.post("/api/v1/items")
def add_item(item: Item):
    db.append(item)
    return {"name", item.name}

# delete product from db
@app.delete("/api/v1/items/{id}")
def delete_item(id: UUID):
    for item in db:
        if item.id == id:
            db.remove(item)
            return
        
# update quantity of item in db
@app.put("/api/v1/items/{id}/qty")
def increment_item(id: UUID, qty: int):
    for item in db:
        if item.id == id:
            item.qty += qty
            return item.qty

# update field/description of product
@app.put("/api/v1/items/{id}")
def update_item(id: int, item: Item):
    update_item_encoded = jsonable_encoder(item)
    db[id] = update_item_encoded
    return update_item_encoded

# search db
@app.get("/api/vi/items/db")
def search_items(query):
    results = []
    for item in db:
        if query.lower() in item.name.lower():
            results.append(item)
        elif query.lower() in item.variant.lower():
            results.append(item)
        elif query.lower() in item.sku.lower():
            results.append(item)   
        elif query.lower() in item.description.lower():
            results.append(item)
        elif query in str(item.qty):
            results.append(item)
        elif query in str(item.price):
            results.append(item)
            

    
    return results
