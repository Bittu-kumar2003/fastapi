# main.py

from fastapi import FastAPI
from routes.product_routes import router as ProductRouter
from routes.order_routes import router as OrderRouter

app = FastAPI()

# 👇 Ye line add karo
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ecommerce API!"}

app.include_router(ProductRouter, prefix="/products", tags=["Products"])
app.include_router(OrderRouter, prefix="/orders", tags=["Orders"])
