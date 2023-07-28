from flask import Flask, jsonify
from flask_restful import Api, Resource
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


class ProductResource(Resource):
    def get(self):
        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Execute the SQL query to fetch items for sale from the database
            cursor.execute("SELECT name, qty, price FROM items_on_sale")

            # Fetch all the results
            results = [
                {"name": name, "qty": qty, "price": float(price)}
                for (name, qty, price) in cursor
            ]

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Return the results as JSON
            return {"products": results}

        except mysql.connector.Error as e:
            # Handle any database errors
            return {"error": "Failed to fetch products from the database."}


# Add the ProductResource to the API with the URL endpoint '/'
api.add_resource(ProductResource, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
