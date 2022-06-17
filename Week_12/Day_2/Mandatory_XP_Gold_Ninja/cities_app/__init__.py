import string
import os
from flask import Flask
from random import choice

basedir = os.path.abspath(os.path.dirname(__file__))

cities_app = Flask(__name__)
cities_app.config['SECRET_KEY'] = ''.join([choice(string.ascii_letters) for _ in range(0, 255)])
cities_app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static')

from Week_12.Day_2.Mandatory_XP_Gold_Ninja.cities_app import routes, forms
