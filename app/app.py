from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017")
db = client["orders"]
orders = db["orders"]

# Endpoint for health check
@app.route("/", methods=["GET"])
def status():
    return {'status':'online'}, 200

# Endpoint to load data to the collection
@app.route("/api/orders/loaddata",methods=["GET"])
def load_data():

    # Delete all documents in the collection
    orders.delete_many({})

    # Load the JSON data into the collection
    result=[]
    with open("assignment.json", "r") as f:
        data = json.load(f)

    result = orders.insert_many(data)
    
    return {'inserted_count': len(result.inserted_ids)}, 200


# Endpoint for fetching an order by order id
@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    try:
        order = orders.find_one({"order_id": order_id},{'_id': False})
        if order:
            return order,200
        else:
            return {'error': 'order not found'},404
    except:
        return {'error': 'Invalid order ID'},400
    

# Endpoint for fetching avg product count from all orders
@app.route("/api/orders/average-products", methods=["GET"])
def get_avg_product_count():
    total_orders = orders.count_documents({})
    total_products = sum([order['product_count'] for order in orders.find()])
    average = total_products / total_orders if total_orders > 0 else 0
    return { "average_product_count":average },200


#Endpoint for find avg for a specific product
@app.route("/api/product/<int:product_id>/average-quantity", methods=["GET"])
def get_avg_product_quantity(product_id):
    total_orders = orders.count_documents({'products.id': product_id})
    total_quantity = sum([product['quantity'] for order in orders.find({'products.id': product_id}) for product in order['products'] if product['id'] == product_id])
    average = total_quantity / total_orders if total_orders > 0 else 0
    return { "average_product_quantity":average },200

if __name__ == '__main__':
    app.run(debug=True)