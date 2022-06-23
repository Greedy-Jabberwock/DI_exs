from numbers_app import app
from flask import render_template
from numbers_app.models import Person, Phonenumber


def get_person_data(person):
    return {'name': person.name,
            'address': person.address,
            'email': person.email,
            'phones': ', '.join((repr(x) for x in person.phonenumbers))}


@app.route('/person/by_phone/<phonenumber>')
def number_info(phonenumber):
    try:
        phone = Phonenumber.query.filter_by(number=phonenumber).first().owner
        person = Person.query.filter_by(person_id=phone).first()
        return render_template('index.html', data=get_person_data(person))
    except AttributeError:
        return render_template('not_found.html')


@app.route('/person/by_name/<name>')
def name_info(name):
    person = Person.query.filter_by(name=name).first()
    if not person:
        return render_template('not_found.html')
    return render_template('index.html', data=get_person_data(person))
