from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


all_pokemons = get_data('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=898')['results']
pok_str = '/pokemon'


@app.route('/')
def index():
    data = get_data('https://pokeapi.co/api/v2/type/')['results']
    types = [x['name'] for x in data]
    return render_template('types.html',
                           title='Types',
                           names=types)


@app.route('/pokemon/<int:id>')
def pokemon_by_id(id):
    data = get_data(f'https://pokeapi.co/api/v2/pokemon/{id}')
    return redirect(url_for('pokemon_by_name', name=data['name']))


@app.route('/pokemons/byname/<string:name>')
def pokemon_by_name(name):
    data = get_data(f'https://pokeapi.co/api/v2/pokemon/{name}')
    return render_template('pokemon_page.html', title=data['name'].title(),
                           image=data['sprites']['front_default'],
                           name=data['name'])


@app.route('/pokemons/bytype/<string:type>')
def pokemons_by_type(type):
    pokemons = get_data(f'https://pokeapi.co/api/v2/type/{type}')['pokemon']
    names = [x['pokemon']['name'] for x in pokemons]
    return render_template('bytype.html', title=f'{type.title()} pokemons',
                           names=names)


@app.route('/pokemons/all/offset=<int:offset>&limit=<int:limit>')
def all_pokemons(offset=0, limit=20):
    data = get_data(f'https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit={limit}')
    next_offset = offset+20 if data['next'] is not None else offset
    previous = offset-20 if data['previous'] is not None else offset
    all_pokemons = []
    for item in data['results']:
        image = requests.get(item['url']).json()['sprites']['front_default']
        name = item['name']
        all_pokemons.append({'name': name, 'img': image})
    return render_template('all_pokemons.html', title='All pokemons',
                           items=all_pokemons, next=next_offset,
                           previous=previous)


if __name__ == '__main__':
    app.run(debug=True)
