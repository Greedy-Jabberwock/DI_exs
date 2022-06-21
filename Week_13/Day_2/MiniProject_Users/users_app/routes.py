from flask import render_template, redirect, url_for, flash, request
from users_app import app, db
from users_app.models import Users
from users_app.forms import AddUser, Login
from re import findall


current_user = None


def get_form_data(form):
    data = {
        'user_name': form.user_name.data,
        'city': form.city.data,
        'street': form.street.data,
        'zipcode': form.zipcode.data,
    }
    return data


def add_to_database(info):
    print(info['zipcode'])
    row = Users(name=info['user_name'], city=info['city'], street=info['street'], zipcode=info['zipcode'], status='User')
    db.session.add(row)
    db.session.commit()


def exists_in_table(form):
    name = form.user_name.data
    city = form.city.data
    if len(findall('[0-9]', name)) > 0 or len(findall('[0-9]', city)) > 0:
        flash('Digits are not allowed!', 'warning')
    return bool(Users.query.filter_by(name=name, city=city).all())


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if exists_in_table(form):
            flash('You are logged in!', 'success')
            global current_user
            current_user = Users.query.filter_by(name=form.user_name.data, city=form.city.data).first()
            return redirect(url_for('index'))
        else:
            flash('You need to sign up first!', 'danger')
            return redirect(url_for('add_user'))
    return render_template('login.html', form=form)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        form_data = get_form_data(form)
        add_to_database(form_data)
        return redirect(url_for('login'))
    return render_template('add_user.html', form=form)


@app.route('/home')
def index():
    return render_template('index.html', user=Users, current_user=current_user)


@app.route('/exercise')
def exercise():
    return render_template('exercise.html', user=Users)




