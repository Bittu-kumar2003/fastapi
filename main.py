from fastapi import FastAPI
from routes.product_routes import router as ProductRouter
from routes.order_routes import router as OrderRouter

app = FastAPI(
    title="Ecommerce API",
    description="API for managing products and orders in an ecommerce application.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ecommerce API!"}

# Include product routes
app.include_router(ProductRouter, prefix="/products", tags=["Products"])

# Include order routes
app.include_router(OrderRouter, prefix="/orders", tags=["Orders"])
