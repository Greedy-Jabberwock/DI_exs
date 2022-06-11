from flask import Flask, render_template, redirect, url_for, request
from products_data import *

app = Flask(__name__)
all_products = retrieve_all_products()
cart_item = []


def find_product(product_id):
    for product in all_products:
        if product['ProductId'] == product_id:
            return product


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products', methods=['GET', 'POST'])
def products():
    return render_template('products.html', products=all_products)


@app.route('/products/<string:product_id>', methods=['GET', 'POST'])
def product_by_id(product_id):
    requested_item = find_product(product_id)
    return render_template('product_page.html', product=requested_item)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    total_price = 0
    for product in cart_item:
        total_price += product['Price']
    return render_template('cart.html', products=cart_item, total=total_price)


@app.route('/add_product_to_cart/<product_id>', methods=['GET', 'POST'])
def add_to_cart(product_id):
    item = find_product(product_id)
    cart_item.append(item)
    return redirect(url_for('cart', products=cart_item))


@app.route('/delete_product_from_cart/<product_id>', methods=['GET', 'POST'])
def remove_from_cart(product_id):
    index = None
    for item in cart_item:
        if item['ProductId'] == product_id:
            index = cart_item.index(item)
    cart_item.pop(index)
    return redirect(url_for('cart', products=cart_item))


if __name__ == '__main__':
    app.run(debug=True)
