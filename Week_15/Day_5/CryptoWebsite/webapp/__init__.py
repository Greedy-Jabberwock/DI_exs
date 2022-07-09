from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from webapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in or sign up to access this page.'
login_manager.login_message_category = 'warning'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from webapp import routes, models
