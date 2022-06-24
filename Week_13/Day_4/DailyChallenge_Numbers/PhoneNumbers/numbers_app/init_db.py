from faker import Faker
from numbers_app import db
from numbers_app.models import Person, Phonenumber, Nationality, nationalities_tables
from random import randint, choice


# fake = Faker()
#
# persons = []
# phonenumbers = []
# model_nation = []

# nationalities = ['Great Britain', 'German', 'Israel', 'Poland', 'Holland',
#                  'Japan', 'Lichtenstein', 'Chechz', 'Bulgaria', 'Australia']
#
#
# for nation in nationalities:
#     nationality = Nationality(name=nation)
#     model_nation.append(nationality)
#
# for _ in range(10):
#     person = Person(name=fake.name(), email=fake.email(), address=fake.address())
#     persons.append(person)
# #
# for _ in range(15):
#     phone = Phonenumber(number=fake.phone_number(), owner=randint(1, 10))
#     phonenumbers.append(phone)


# db.session.add_all(model_nation)
# db.session.add_all(persons)
# db.session.add_all(phonenumbers)

# db.session.commit()

# for i in range(1, Person.query.count()+1):
#     person = Person.query.get(i)
#     print(person)
#     for _ in range(randint(1, 2)):
#         nationality = Nationality.query.get(randint(1, Nationality.query.count()))
#         print(nationality)
#         person.nationalities.append(nationality)
#     print(person)
#     db.session.add(person)
#     db.session.commit()
