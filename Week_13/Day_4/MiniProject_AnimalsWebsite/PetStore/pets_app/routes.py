from pets_app import app, db
from flask import render_template, flash, url_for, redirect
from pets_app.models import Pet, Cart
import requests
import json


def get_pet(pet_id):
    return Pet.query.filter_by(pet_id=pet_id).first()


@app.route('/')
def home():
    # responce = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5").json()
    # facts = (x['text'] for x in responce)
    # return render_template('index.html', facts=facts)
    return render_template('index.html')


@app.route('/pets')
def pets():
    return render_template('pets.html', pets=Pet.query.order_by('pet_id').all())


@app.route('/pet/<int:pet_id>')
def pet(pet_id):
    return render_template('pet_page.html', pets_id=pet_id, pet=get_pet(pet_id))


@app.route('/cart')
def cart():
    return render_template('cart.html', cart=Cart.query.first())


@app.route('/add_to_cart/<int:pet_id>')
def add_to_cart(pet_id):
    cart = Cart.query.first()
    if not cart:
        db.session.add(Cart())
        db.session.commit()
    cart.add_to_cart(pet_id)
    flash('Item added to cart!', 'success')
    return redirect(url_for('pets'))


@app.route('/remove_from_cart/<int:pet_id>')
def remove(pet_id):
    Cart.query.first().remove_from_cart(pet_id, remove=True)
    return redirect(url_for('cart'))


@app.route('/change_count/<int:pet_id>/<int:sign>')
def change_count(pet_id, sign):
    cart = Cart.query.first()
    if sign:
        cart.add_to_cart(pet_id)
    else:
        cart.remove_from_cart(pet_id)
    return redirect(url_for('cart'))
