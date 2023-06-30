# LLBackendAssignment

This is a sample Flask application that demonstrates basic usage.

## Installation

1. Clone the repository:
    eg: git clone git@github.com:abhineshmathew/LLBackendAssignment.git


2. Create a virtual environment:
    python3 -m venv venv


3. Activate the virtual environment:
    For Linux/Mac: source venv/bin/activate

4. Install the dependencies:
    pip install -r requirements.txt


5. Set up environment variables:
    Create a `.env` file in the root directory of the project.
    Add the below environment variables.

    HOST=localhost
    PORT=27017
    DB_NAME=lovelocal
    COLLECTION_NAME=orders

    FLASK_APP=app
    FLASK_ENV=development


6. Run the application:
    python -m flask run

7. Open your web browser and hit the below URL for inserting dummy data
    http://127.0.0.1:5000/api/orders/loaddata




## API Details

1. To insert dummy data to DB : http://127.0.0.1:5000/api/orders/loaddata
2. Get order details with order ID : http://127.0.0.1:5000/api/orders/<int:order_id>
3. Get avg product count of total order : http://127.0.0.1:5000/api/orders/average-products
4. Get avg product quantity with product ID : http://127.0.0.1:5000/api/product/<int:product_id>/average-quantity

Note: Replace order ID (<int:order_id>)  and product ID (<int:product_id>) with actual data.