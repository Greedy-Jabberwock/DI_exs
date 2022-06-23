from pets_app import db
from datetime import datetime


class Pet(db.Model):
    column = db.Column

    pet_id = column(db.Integer, primary_key=True, autoincrement=True)
    name = column(db.String, nullable=False, unique=True)
    gender = column(db.String, nullable=False)
    breed = column(db.String, nullable=False)
    date_of_birth = column(db.Date, nullable=False, default=datetime.now().strftime('%m/%d/%Y'))
    details = column(db.Text, nullable=False)
    price = column(db.Integer, nullable=False)
    image = column(db.String, nullable=False)
    cart_id = column(db.Integer, db.ForeignKey('cart.cart_id'))

    def __repr__(self):
        return f'<Pet: {self.pet_id}, {self.name}, {self.image}>'


class Cart(db.Model):
    column = db.Column

    cart_id = column(db.Integer, primary_key=True, autoincrement=True)
    pets = db.relationship('Pet', backref='cart')
    numbers_of_pets = column(db.Integer, default=0)

    def __repr__(self):
        return f'<Cart {self.cart_id}, {self.pets}>'

    def check_id_in_cart(self, pet_id):
        if pet_id in [x.pet_id for x in self.pets]:
            return True
        return False

    def add_to_cart(self, pet_id):
        pet = Pet.query.filter_by(pet_id=pet_id).first()
        setattr(pet, 'cart_id', self.cart_id)
        cart = Cart.query.first()
        setattr(cart, 'numbers_of_pets', self.numbers_of_pets + 1)
        db.session.commit()

    def remove_from_cart(self, pet_id):
        pet = Pet.query.filter_by(pet_id=pet_id).first()
        setattr(pet, 'cart_id', None)
        db.session.commit()

    def get_all_data(self):
        return {'id': self.cart_id, 'pets': self.pets}

    def get_total(self):
        return sum([x.price for x in self.pets]) if self.pets else 0


