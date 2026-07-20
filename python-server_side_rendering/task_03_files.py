from flask import Flask, render_template, request
import json
import csv

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

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    
    error_message = None
    products_data = []
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message, products=[])
    
    try:
        if source == 'json':
            products_data = read_json_products()
        elif source == 'csv':
            products_data = read_csv_products()
        
        # Filter by id if provided
        if product_id:
            filtered_products = [p for p in products_data if str(p['id']) == str(product_id)]
            if not filtered_products:
                error_message = "Product not found"
                return render_template('product_display.html', error=error_message, products=[])
            products_data = filtered_products
    
    except FileNotFoundError:
        error_message = "Data file not found"
        return render_template('product_display.html', error=error_message, products=[])
    except Exception as e:
        error_message = f"Error reading file: {str(e)}"
        return render_template('product_display.html', error=error_message, products=[])
    
    return render_template('product_display.html', products=products_data, error=None)

def read_json_products():
    """Read products from JSON file"""
    with open('products.json', 'r') as file:
        products = json.load(file)
    return products

def read_csv_products():
    """Read products from CSV file"""
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert id and price to appropriate types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)