from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import mysql.connector
from decimal import Decimal

app = Flask(__name__)
api = Api(app)

# Configuration for MySQL database connection
db_config = {
    "user": "root",
    "password": "root",
    "host": "db-mysql",  # The name of the MySQL container in the Docker Compose network
    "port": "3306",
    "database": "products",  # Make sure the database name matches the one in the MySQL container
}

# Request parser for parsing form data
parser = reqparse.RequestParser()
parser.add_argument(
    "product_name", type=str, required=True, help="Product name cannot be blank."
)
parser.add_argument(
    "quantity", type=int, required=True, help="Quantity cannot be blank."
)
parser.add_argument("price", type=str, required=True, help="Price cannot be blank.")


class AddProduct(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            product_name = args["product_name"]
            quantity = args["quantity"]
            price = Decimal(args["price"])

            # Connect to the MySQL database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Check if the product already exists in the database
            cursor.execute(
                "SELECT * FROM items_on_sale WHERE name = %s", (product_name,)
            )
            existing_product = cursor.fetchone()

            if existing_product:
                # If the product exists, update its quantity
                cursor.execute(
                    "UPDATE items_on_sale SET qty = %s WHERE name = %s",
                    (quantity, product_name),
                )
            else:
                # If the product does not exist, insert a new row
                cursor.execute(
                    "INSERT INTO items_on_sale (name, qty, price) VALUES (%s, %s, %s)",
                    (product_name, quantity, price),
                )

            # Commit the changes to the database
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return {"message": "Product added successfully."}, 200

        except mysql.connector.Error as e:
            # Handle any database errors
            return {"error": "Failed to add product to the database."}, 500


class UpdateQuantity(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            product_name = args["product_name"]
            new_quantity = args["quantity"]

            # Connect to the MySQL database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Check if the product exists in the database
            cursor.execute(
                "SELECT * FROM items_on_sale WHERE name = %s", (product_name,)
            )
            existing_product = cursor.fetchone()

            if existing_product:
                # If the product exists, update its quantity
                cursor.execute(
                    "UPDATE items_on_sale SET qty = %s WHERE name = %s",
                    (new_quantity, product_name),
                )
                # Commit the changes to the database
                connection.commit()

                # Close the cursor and connection
                cursor.close()
                connection.close()

                return {"message": "Quantity updated successfully."}, 200
            else:
                # If the product does not exist, return an error message
                return {"error": "Product not found."}, 404

        except mysql.connector.Error as e:
            # Handle any database errors
            return {"error": "Failed to update quantity in the database."}, 500


api.add_resource(AddProduct, "/add_product")
api.add_resource(UpdateQuantity, "/update_quantity")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
