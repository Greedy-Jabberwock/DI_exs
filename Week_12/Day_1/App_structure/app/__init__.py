import flask

my_app = flask.Flask(__name__)
my_app.config['SECRET_KEY'] = 'you-will-never-guess'

from Week_12.Day_1.App_structure.app import routes, forms
