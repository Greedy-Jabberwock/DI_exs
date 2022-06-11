import json

from flask import Flask, render_template, url_for

app = Flask(__name__)

with open('product_db.json') as db:
    all_products = json.load(db)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')


@app.route('/products', methods=['GET', 'POST'])
def products_list():
    return render_template('products.html', title='Products',
                           products=all_products)


@app.route('/products/<product_id>', methods=['GET', 'POST'])
def product_info(product_id):
    curr_product = None
    for product in all_products:
        if product['ProductId'] == product_id:
            curr_product = product
    return render_template('product_page.html', title=product['ProductId'],
                           product=curr_product)


if __name__ == '__main__':
    app.run(debug=True)
