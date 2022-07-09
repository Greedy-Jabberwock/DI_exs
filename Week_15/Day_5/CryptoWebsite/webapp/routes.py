import os

from webapp import app, login_manager, bcrypt, db, mail
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message
from webapp.models import Cryptocurrency, User
from webapp.forms import SignUp, Login


# ------------------------ Main --------------------------------------


@app.route('/')
@app.route('/home')
@login_required
def home():
    currencies = Cryptocurrency.query.all()
    return render_template('index.html', cryptos_list=currencies)


@app.route('/details/<int:crypto_id>')
@login_required
def crypto_page(crypto_id):
    return render_template('specifics.html', info=Cryptocurrency.get_info(crypto_id))


@app.route('/account')
@login_required
def account():
    return render_template('account.html')


# ----------------------- Registration part ---------------------------


@login_manager.user_loader
def load_user(user_id):
    user_id = int(user_id)
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    login_form = Login()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('home'))
        flash('Invalid password or username.', 'warning')

    return render_template('login.html', login=login_form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    singup_form = SignUp()
    if singup_form.validate_on_submit():
        data = User(
            username=singup_form.username.data,
            password=bcrypt.generate_password_hash(singup_form.password.data).decode('utf-8'),
            email=singup_form.email.data
        )
        User.save_user_to_db(data)
        login_user(data)
        return redirect(url_for('home'))
    return render_template('signup.html', signup=singup_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/save/<int:currency_id>')
@login_required
def save(currency_id):
    crypto = Cryptocurrency.query.filter_by(id=currency_id).first()
    if crypto not in current_user.cryptos:
        current_user.cryptos.append(crypto)
        db.session.commit()
    else:
        flash('This crypto already in your list.', 'info')
    return redirect(url_for('crypto_page', crypto_id=currency_id))


@app.route('/send_email/<int:currency_id>')
@login_required
def send_email(currency_id):
    info = Cryptocurrency.query.filter_by(id=int(currency_id)).first()
    msg = Message('subject',
                  sender=os.environ['MAIL_USERNAME'],
                  recipients=[os.environ['MAIL_USERNAME']])
    msg.body = f'''
Crypto info: 
- name: {info.name}
- symbol: {info.symbol}
- slug: {info.slug}
- is active: {'yes' if info.is_active else 'no'}
- first historical data: {info.first_historical_data}
- last historical data: {info.last_historical_data}
'''
    msg.html = ''
    mail.send(msg)
    return redirect(url_for('crypto_page', crypto_id=currency_id))
