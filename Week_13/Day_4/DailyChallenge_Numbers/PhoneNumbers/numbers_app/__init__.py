from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = "some_super_secret_password"
app.config['DEBUG'] = True

db_info = {
    'host': 'localhost',
    'database': 'w13_d4_numbers',
    'psw': 'learningSQL',
    'user': 'postgres',
    'port': ''
}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://" \
                                        f"{db_info['user']}:" \
                                        f"{db_info['psw']}@" \
                                        f"{db_info['host']}/" \
                                        f"{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from numbers_app import models, routes