from bson import ObjectId

#from Fast_api.models import detail_helper
from database import item_collection,detail_collection
from models import item_helper,detail_helper
from schemas import ItemModel,DetailModel

async def add_item(item: ItemModel) -> dict:
    new_item = await item_collection.insert_one(item.dict())
    created_item = await item_collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

async def add_detail(detail:DetailModel) -> dict:
    new_detail = await  detail_collection.insert_one(detail.dict())
    created_detail = await detail_collection.find_one({"_id": new_detail.inserted_id})
    return detail_helper(created_detail)

async def retrieve_items():
    try:
        items = []
        async for item in item_collection.find():
            items.append(item_helper(item))
        return items
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
async  def retrieve_details():
    details = []
    async for detail in detail_collection.find():
        details.append(detail_helper(detail))
    return details

async def retrieve_item(id: str):
    item = await item_collection.find_one({"_id": ObjectId(id)})
    return item_helper(item) if item else None
