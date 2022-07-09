import json
from requests import Session, Timeout, TooManyRedirects
from flask_login import UserMixin
from webapp import db


cryptos_table = db.Table('crypto',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                         db.Column('crypto_id', db.Integer, db.ForeignKey('cryptocurrency.id'))
                         )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    cryptos = db.relationship('Cryptocurrency', secondary=cryptos_table)

    @staticmethod
    def save_user_to_db(new_record):
        db.session.add(new_record)
        db.session.commit()


class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String, nullable=False)
    symbol = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)
    first_historical_data = db.Column(db.String, nullable=False)
    last_historical_data = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_info(crypto_id):
        url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'

        parameters = {'id': crypto_id}

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
        }

        session = Session()
        session.headers.update(headers)

        try:
            responce = session.get(url, params=parameters)
            data = json.loads(responce.text)
            return data['data'][str(crypto_id)]
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    @staticmethod
    def save_to_db(crypto):
        currency = Cryptocurrency(
            id=crypto['id'],
            name=crypto['name'],
            symbol=crypto['symbol'],
            slug=crypto['slug'],
            first_historical_data=crypto['first_historical_data'][0:10],
            last_historical_data=crypto['last_historical_data'][0:10],
            is_active=crypto['is_active']
        )
        db.session.add(currency)
        db.session.commit()
