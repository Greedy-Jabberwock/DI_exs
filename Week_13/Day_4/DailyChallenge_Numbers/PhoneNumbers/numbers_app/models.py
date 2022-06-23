from numbers_app import db


class Person(db.Model):
    col = db.Column

    person_id = col(db.Integer, primary_key=True)
    name = col(db.String, nullable=False)
    email = col(db.String, nullable=False)
    phonenumbers = db.relationship('Phonenumber', backref='person')
    address = col(db.String, nullable=False)

    def __repr__(self):
        return f'<Person {self.person_id}: {self.name}, {self.phonenumbers},' \
               f'{self.email}, {self.address}>'


class Phonenumber(db.Model):
    col = db.Column

    phone_id = col(db.Integer, primary_key=True, autoincrement=True)
    number = col(db.String, nullable=False)
    owner = col(db.Integer, db.ForeignKey('person.person_id'))

    def __repr__(self):
        return f'{self.number}'
