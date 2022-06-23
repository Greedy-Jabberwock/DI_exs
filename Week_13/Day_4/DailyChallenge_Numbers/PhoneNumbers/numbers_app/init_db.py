from faker import Faker
from numbers_app import db
from numbers_app.models import Person, Phonenumber
from random import randint


fake = Faker(['he'])

persons = []
phonenumbers = []

for _ in range(10):
    person = Person(name=fake.name(), email=fake.email(), address=fake.address())
    persons.append(person)

for _ in range(15):
    phone = Phonenumber(number=fake.phone_number(), owner=randint(1, len(persons)))
    phonenumbers.append(phone)

db.session.add_all(persons)
db.session.add_all(phonenumbers)

db.session.commit()
