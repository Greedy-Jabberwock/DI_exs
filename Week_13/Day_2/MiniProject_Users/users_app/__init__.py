import json
from random import choice
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Very_Secret_Key'
app.config['DEBUG'] = True

db_info = {
    'host': 'localhost',
    'database': 'w13_d2_users',
    'psw': 'learningSQL',
    'user': 'postgres',
    'port': ''
}
app.config[
    'SQLALCHEMY_DATABASE_URI'
    ] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from users_app import models, routes


def populate():
    with open('users.json', 'r') as file_obj:
        json_data = json.load(file_obj)
        for user in json_data:
            user_address = user['address']
            model = models.Users(
                name=user['name'],
                street=user_address['street'],
                city=user_address['city'],
                zipcode=user_address['zipcode']
            )
            db.session.add(model)
            db.session.commit()


def update_status():
    roles = ['User', 'Admin']
    for user in models.Users.query.all():
        user_role = choice(roles)
        setattr(user, 'status', user_role)
        if user_role == 'Admin':
            roles.pop()
        db.session.commit()
    print(models.Users.query.all())
