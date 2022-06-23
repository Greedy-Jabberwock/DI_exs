from pets_app import db
from pets_app.models import Pet, Cart
from datetime import datetime

pet1 = Pet(name='Blacksy', gender='F', breed='German Shepherd',
           date_of_birth=datetime(2018, 10, 3), details='Some info',
           price=2000, image='german_shepherd.jpg')
pet2 = Pet(name='Grumpy', gender='M', breed='British Shorthair',
           date_of_birth=datetime(2019, 12, 20), details='Some info',
           price=1000, image='british_shorthair.jpg')
pet3 = Pet(name='Lessy', gender='F', breed='Collie',
           date_of_birth=datetime(2020, 11, 1), details='Some info',
           price=4000, image='collie.jpg')
pet4 = Pet(name='Jessy', gender='F', breed='Abyssinian',
           date_of_birth=datetime(2016, 7, 21), details='Some info',
           price=2500, image='abyss.jpg')
pet5 = Pet(name='Fluff', gender='M', breed='Siberian',
           date_of_birth=datetime(2015, 10, 9), details='Some info',
           price=2000, image='siberian.jpg')
db.session.add_all((pet1, pet2, pet3, pet4, pet5))
db.session.commit()
