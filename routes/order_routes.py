from fastapi import APIRouter
from models.order_model import Order
from database import order_collection
from bson import ObjectId

router = APIRouter()

@router.post("/")
def create_order(order: Order):
    result = order_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id), "message": "Order placed successfully"}

@router.get("/{user_id}")
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    query = {"user_id": user_id}
    orders = order_collection.find(query).skip(offset).limit(limit)
    result = []
    for o in orders:
        o["order_id"] = str(o["_id"])
        del o["_id"]
        result.append(o)
    return result

