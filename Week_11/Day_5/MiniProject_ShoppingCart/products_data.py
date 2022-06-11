import json


def retrieve_all_products():
    with open('products.json', 'r') as file_obj:
        return json.load(file_obj)


def retrieve_requested_product(product_id):
    all = retrieve_all_products()
    requested_product = None
    for product in all:
        if product['ProductId'] == product_id:
            requested_product = product
    return requested_product


if __name__ == '__main__':
    retrieve_requested_product('HT-1119')
