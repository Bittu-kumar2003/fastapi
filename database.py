import os
from pymongo import MongoClient

# Get Mongo URI from environment variable or fallback to default
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://bittukumarprajapati2003:Kumar%40123@cluster0.qma1bzi.mongodb.net/?retryWrites=true&w=majority")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Select database
db = client["api"]

# Select collections
product_collection = db["products"]
order_collection = db["orders"]
