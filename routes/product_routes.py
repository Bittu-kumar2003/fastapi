# from fastapi import APIRouter, Query
# from models.product_model import Product
# from database import product_collection
# from bson import ObjectId
# import re

# router = APIRouter()

# @router.post("/")
# def create_product(product: Product):
#     result = product_collection.insert_one(product.dict())
#     return {"id": str(result.inserted_id), "message": "Product created successfully"}

# @router.get("/")
# def list_products(name: str = "", size: str = "", limit: int = 10, offset: int = 0):
#     query = {}
#     if name:
#         query["name"] = {"$regex": re.compile(name, re.IGNORECASE)}
#     if size:
#         query["sizes"] = size
    
#     products = product_collection.find(query).skip(offset).limit(limit)
#     result = []
#     for p in products:
#         p["id"] = str(p["_id"])
#         del p["_id"]
#         result.append(p)
#     return result
from fastapi import APIRouter, Query
from models.product_model import Product
from database import product_collection
from bson import ObjectId
import re

router = APIRouter()

# Create a new product
@router.post("/")
def create_product(product: Product):
    # Convert model to dictionary and insert into MongoDB
    result = product_collection.insert_one(product.dict())
    return {
        "id": str(result.inserted_id),
        "message": "Product created successfully"
    }

# List products with optional name search, pagination
@router.get("/")
def list_products(name: str = "", limit: int = 10, offset: int = 0):
    query = {}

    # Add name filter (case-insensitive partial match)
    if name:
        query["name"] = {"$regex": re.compile(name, re.IGNORECASE)}

    # Fetch data from MongoDB with pagination
    products = product_collection.find(query).skip(offset).limit(limit)

    # Format and return response
    result = []
    for p in products:
        p["id"] = str(p["_id"])
        del p["_id"]
        result.append(p)

    return result
