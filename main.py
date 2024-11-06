from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Definimos el modelo de datos
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Lista en memoria para almacenar los "items" (diccionarios)
items_db = []
@app.get("/")
async def home():
    return {"message":"Estamos en inicio"}
# CRUD - Crear un item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    # Añadimos el item a la lista
    items_db.append(item)
    return item

# CRUD - Leer todos los items
@app.get("/items/", response_model=List[Item])
async def get_items():
    return items_db

# CRUD - Leer un item por ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

# CRUD - Actualizar un item por ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# CRUD - Eliminar un item por ID
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")