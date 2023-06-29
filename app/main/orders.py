from .helper import *
import json

def get_order(order_id):
    try:
        orders = get_mongodb_client()
        order = orders.find_one({"order_id": order_id},{'_id': False})
        if order:
            return order,200
        else:
            return {'error': 'order not found'},404
    except:
        return {'error': 'Invalid order ID'},400
    

def get_avg_product_count():
    orders = get_mongodb_client()

    total_orders = orders.count_documents({})
    total_products = sum([order['product_count'] for order in orders.find()])
    average = total_products / total_orders if total_orders > 0 else 0
    return { "average_product_count":average },200

def load_data():
    orders = get_mongodb_client()

    # Delete all documents in the collection
    orders.delete_many({})

    # Load the JSON data into the collection
    result=[]
    with open("assignment.json", "r") as f:
        data = json.load(f)

    result = orders.insert_many(data)
   
    return {'inserted_count': len(result.inserted_ids)}, 200