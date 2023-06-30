import os
from pymongo import MongoClient

def get_mongodb_client():
    client = MongoClient('mongodb://'+os.getenv('HOST')+':'+os.getenv('PORT')+'/')
    db = client[os.getenv('DB_NAME')]
    orders = db[os.getenv('COLLECTION_NAME')]
    return orders

    