from numbers_app import db


col = db.Column


nationalities_tables = db.Table('nationalities',
                                col('person_id', db.Integer, db.ForeignKey('person.person_id')),
                                col('nat_id', db.Integer, db.ForeignKey('nationality.nat_id'))
                                )


class Person(db.Model):
    # col = db.Column

    person_id = col(db.Integer, primary_key=True)
    name = col(db.String, nullable=False)
    email = col(db.String, nullable=False)
    phonenumbers = db.relationship('Phonenumber', backref='person')
    address = col(db.String, nullable=False)
    nationalities = db.relationship('Nationality',
                                    secondary=nationalities_tables,
                                    back_populates='people')

    def __repr__(self):
        return f'<Person {self.person_id}: {self.name}, {self.phonenumbers},' \
               f'{self.email}, {self.address}, {self.nationalities}>\n'


class Phonenumber(db.Model):
    # col = db.Column

    phone_id = col(db.Integer, primary_key=True)
    number = col(db.String, nullable=False)
    owner = col(db.Integer, db.ForeignKey('person.person_id'))

    def __repr__(self):
        return f'{self.number}'


class Nationality(db.Model):
    # col = db.Column

    nat_id = col(db.Integer, primary_key=True)
    name = col(db.String, nullable=False)
    people = db.relationship('Person',
                             secondary=nationalities_tables,
                             back_populates='nationalities')

    def __repr__(self):
        return f'<{self.name}>'
