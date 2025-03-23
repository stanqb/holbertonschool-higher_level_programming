from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def read_json_data():
    """Read product data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_data():
    """Read product data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to integer and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []


def read_sql_data():
    """Read product data from SQLite database"""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })

        conn.close()
        return products
    except sqlite3.Error:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Initialize variables
    products_data = []
    error_message = None

    # Check source parameter
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        products_data = read_sql_data()
    else:
        error_message = "Wrong source"

    # Filter by ID if provided and no error
    if not error_message and product_id:
        try:
            product_id = int(product_id)
            filtered_products = [
                p for p in products_data if p['id'] == product_id
            ]
            if filtered_products:
                products_data = filtered_products
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"

    return render_template('product_display.html',
                           products=products_data,
                           error=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
