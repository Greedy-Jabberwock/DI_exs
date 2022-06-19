import json
import os

from flask import render_template, redirect, url_for
from Week_12.Day_2.Mandatory_XP_Gold_Ninja.cities_app import cities_app
from Week_12.Day_2.Mandatory_XP_Gold_Ninja.cities_app.forms import AddCity


def get_list_of_cities():
    filename = 'cities_around_the_world.json'
    if os.path.getsize(filename) > 0:
        with open(filename) as f:
            return json.load(f)
    else: # the else is redundant
        return []


list_of_cities = get_list_of_cities()


@cities_app.route('/')
def index():
    return render_template('index.html', cities=list_of_cities)


@cities_app.route('/add_city', methods=['GET', 'POST'])
def add_city():
    form = AddCity()
    if form.validate_on_submit():
        global list_of_cities
        city = {
                'name': form.name.data,
                'country': form.country.data,
                'inhabitants': form.inhabitants.data,
                'area': form.area.data,
                'description': form.description.data,
                'capital': form.capital.data,
                'file': form.file.data
            }
        if city not in list_of_cities:
            list_of_cities.append(city)
            with open('cities_around_the_world.json', 'w') as file:
                json.dump(list_of_cities, file, indent=4)
        return redirect(url_for('index'))

    return render_template('add_form.html', form=form)
