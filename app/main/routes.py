from app.main import bp
from .orders import *
from .products import *


# Endpoint to dump data from JSON to mongoDB
bp.add_url_rule('/api/orders/loaddata', 'load_data', load_data, methods=['GET'])

# Endpoint to fetch avg product count
bp.add_url_rule('/api/orders/average-products', 'get_avg_product_count', get_avg_product_count, methods=['GET'])

# Endpoint to fetch order details with order ID
bp.add_url_rule('/api/orders/<int:order_id>', 'get_order', get_order, methods=['GET'])

# Endpoint to fetch avg quantity of a product with product ID
bp.add_url_rule('/api/product/<int:product_id>/average-quantity', 'get_avg_product_quantity', get_avg_product_quantity, methods=['GET'])
