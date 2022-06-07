from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/products')
def products_list():
    return 'products page'


@app.route('/products/<product_id>')
def product_info(product_id):
    return f'product {product_id}'


if __name__ == '__main__':
    app.run(debug=True)
