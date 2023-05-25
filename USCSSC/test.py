from typing import Union, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from uuid import UUID, uuid4


app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = str(uuid4)
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

# add product to inventory
@app.post("/api/v1/items")
def add_item(item: Item):
    inventory.append(item)
    return {"name", item.name}

# delete product from inventory
@app.delete("/api/v1/items/{id}")
def delete_item(id: UUID):
    for item in inventory:
        if item.id == id:
            inventory.remove(item)
            return
        
# update quantity of item in inventory
@app.put("/api/v1/items/{id}/qty")
def increment_item(id: UUID, qty: int):
    for item in inventory:
        if item.id == id:
            item.qty += qty
            return item.qty

# update field/description of product
@app.put("/api/v1/items/{id}")
def update_item(id: UUID, item: Item):
    for i, item in enumerate(inventory):
        if item.id == id:
            inventory[i] = item
            return inventory[i]

# search inventory
@app.get("/api/vi/items/inventory")
def search_items():
    results = []
    for item in inventory:
        results.append(item)
        return results
