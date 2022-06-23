from pets_app import app, db
from flask import render_template, flash, url_for, redirect
from pets_app.models import Pet, Cart


def get_pet(pet_id):
    return Pet.query.filter_by(pet_id=pet_id).first()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pets')
def pets():
    return render_template('pets.html', pets=Pet.query.all())


@app.route('/pet/<int:pet_id>')
def pet(pet_id):
    return render_template('pet_page.html', pets_id=pet_id, pet=get_pet(pet_id))


@app.route('/cart')
def cart():
    cart = Cart.query.first()
    return render_template('cart.html', cart=cart)


@app.route('/add_to_cart/<int:pet_id>')
def add_to_cart(pet_id):
    cart = Cart.query.first()
    if not cart:
        db.session.add(Cart(numbers_of_pets=0))
        db.session.commit()
    cart.add_to_cart(pet_id)
    flash('Item added to cart!', 'success')
    return redirect(url_for('cart'))


@app.route('/remove_from_cart/<int:pet_id>')
def remove(pet_id):
    cart = Cart.query.first()
    if cart:
        cart.remove_from_cart(pet_id)
    return redirect(url_for('cart'))