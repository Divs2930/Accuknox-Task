import requests
from db import Database

# Initialize the Database object
db = Database()
res = requests.get('https://dummyjson.com/products')

# Check if the request was successful (status code 200)
if res.status_code == 200:
    # Extract the products data from the JSON response
    products = res.json()['products']

    # Create the table in the database if it doesn't exist
    db.createTable()

    # Insert the products into the database
    db.insertProducts(products)

    # Retrieve all products from the database and display them
    all_products = db.getAllProducts()
    print("All Products:")
    for product in all_products:
        print(product)
else:
    print("Error:", res.status_code)
