from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI(title="JSON Data API without Database")

# Model for incoming request data (creating/updating)
class ItemSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True



# Model for response data (includes generated ID)
class ItemResponse(ItemSchema):
    id: int



# ==========================================
# 2. In-Memory Data Store (Simulating DB)
# ==========================================
db_items: List[dict] = [
    {"id": 1, "name": "Laptop", "description": "High performance", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Wireless Mouse", "description": "Ergonomic design", "price": 29.99, "in_stock": True},
]



# Helper variable to keep track of autoincrementing IDs
id_counter = 3



# READ ALL items
@app.get("/items", response_model=List[ItemResponse])
def get_all_items():
    return db_items



# READ ONE item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    for item in db_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Item with ID {item_id} not found"
    )



# CREATE a new item from JSON payload
@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemSchema):
    global id_counter
    
    # Convert Pydantic object to Python dictionary
    new_item = item.model_dump()
    new_item["id"] = id_counter
    
    db_items.append(new_item)
    id_counter += 1
    
    return new_item



# UPDATE an existing item
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated_item: ItemSchema):
    for index, item in enumerate(db_items):
        if item["id"] == item_id:
            new_data = updated_item.model_dump()
            new_data["id"] = item_id  # Preserve existing ID
            db_items[index] = new_data
            return new_data
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Item with ID {item_id} not found"
    )



# DELETE an item
@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: int):
    for index, item in enumerate(db_items):
        if item["id"] == item_id:
            removed_item = db_items.pop(index)
            return {"message": f"Item '{removed_item['name']}' deleted successfully"}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Item with ID {item_id} not found"
    )