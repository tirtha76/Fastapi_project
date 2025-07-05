from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.items_db
item_collection: Collection = database.get_collection("items")
detail_collection: Collection = database.get_collection("details")
