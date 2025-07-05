from http.client import responses

from fastapi import FastAPI, HTTPException
from crud import add_item, retrieve_items, retrieve_item,add_detail,retrieve_details
from schemas import ItemModel, ItemResponse,DetailModel,DetailResponce

app = FastAPI()

@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemModel):
    return await add_item(item)

@app.get("/items/", response_model=list[ItemResponse])
async def get_items():
    return await retrieve_items()

@app.post("/details", response_model = DetailResponce)
async def create_detail(detail: DetailModel):
    return await add_detail(detail)

@app.get("/details/", response_model =list[DetailResponce])
async def get_details():
    return await retrieve_details()
@app.get("/items/{id}", response_model=ItemResponse)
async def get_item(id: str):
    item = await retrieve_item(id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")
