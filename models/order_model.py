from pydantic import BaseModel
from typing import List

class ProductItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    products: List[ProductItem]
