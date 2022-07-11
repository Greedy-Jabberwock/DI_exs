from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from webapp.models import Cryptocurrency
import json


def populate():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map' # you can export all the constans to sperate file called consatns 
    parameters = {
        'listing_status': 'active',
        'limit': '20',
        'sort': 'cmc_rank'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633', # this value you can export to environment variable
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for crypto in data['data']:
            Cryptocurrency.save_to_db(crypto)
            # print(crypto)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)



