from .helper import *

def get_avg_product_quantity(product_id):
    orders = get_mongodb_client()
    
    total_orders = orders.count_documents({'products.id': product_id})
    total_quantity = sum([product['quantity'] for order in orders.find({'products.id': product_id}) for product in order['products'] if product['id'] == product_id])
    average = total_quantity / total_orders if total_orders > 0 else 0
    return { "average_product_quantity":average },200