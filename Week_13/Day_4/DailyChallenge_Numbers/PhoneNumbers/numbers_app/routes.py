from numbers_app import app
from flask import render_template, redirect, url_for, flash
from numbers_app.models import Person, Phonenumber, Nationality
from numbers_app.forms import Search


def get_person_data(person):
    return {'name': person.name,
            'address': person.address,
            'email': person.email,
            'phones': ', '.join((repr(x) for x in person.phonenumbers)) if person.phonenumbers else None,
            'nationalities': ', '.join(x.name for x in person.nationalities)
            }


def define_route(data):
    checker = {
        'names': (x.name for x in Person.query.all()),
        'phones': (x.number for x in Phonenumber.query.all()),
        'nations': (x.name for x in Nationality.query.all())
    }
    if data in checker['names']:
        flash('Found by name.', 'success')
        return redirect(url_for('name_info', name=data))
    elif data in checker['phones']:
        flash('Found by phone.', 'success')
        return redirect(url_for('number_info', phonenumber=data))
    elif data in checker['nations']:
        flash('Found by nationality.', 'success')
        return redirect(url_for('by_nat', nationality=data))
    else:
        flash('Sorry, no results. Try again.', 'danger')
        return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Search()
    if form.validate_on_submit():
        return define_route(form.search.data)
    return render_template('index.html', form=form)


@app.route('/person/by_phone/<phonenumber>')
def number_info(phonenumber):
    phone = Phonenumber.query.filter_by(number=phonenumber).first()
    if phone:
        person = Person.query.filter_by(person_id=phone.owner).first()
        return render_template('by_phone_or_name.html', data=get_person_data(person))
    return render_template('not_found.html')


@app.route('/person/by_name/<name>')
def name_info(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        return render_template('by_phone_or_name.html', data=get_person_data(person))
    return render_template('not_found.html')


@app.route('/people/<nationality>')
def by_nat(nationality):
    people = Nationality.query.filter_by(name=nationality.title()).first().people
    people_info = list()
    for human in people:
        people_info.append(get_person_data(human))
    return render_template('by_nation.html', nationality=nationality,
                           info=people_info)
