from pymongo import MongoClient

# Correct MongoDB URI with encoded password
MONGO_URI = "mongodb+srv://bittukumarprajapati2003:Kumar%40123@cluster0.qma1bzi.mongodb.net/?retryWrites=true&w=majority"

# Create a client connection
client = MongoClient(MONGO_URI)

# Choose the database (you can name it whatever you like, here it's 'api')
db = client["api"]

# Create references to collections
product_collection = db["products"]
order_collection = db["orders"]
