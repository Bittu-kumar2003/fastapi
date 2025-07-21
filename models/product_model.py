# from pydantic import BaseModel
# from typing import List

# class Product(BaseModel):
#     name: str
#     description: str
#     price: float
#     sizes: List[str]
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str
    brand: Optional[str] = None
    rating: Optional[float] = None
    stock: Optional[int] = None

