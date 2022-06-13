from flask import Flask

cv_app = Flask(__name__)
cv_app.config['SECRET_KEY'] = 'top_secret_key'

from Week_12.Day_2.DailyChallenge_ResponsiveCV.cv_app import routes
