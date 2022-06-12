import flask
from Week_12.Day_1.App_structure.app import my_app  # app.app is package_name.variable_name
from Week_12.Day_1.App_structure.app.forms import Login, Contact


@my_app.route("/", methods=['GET', 'POST'])
def index():
    login_form = Login()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        bio = login_form.bio.data

        print(username)
        print(password)
        print(bio)

        return flask.redirect(flask.url_for('home'))

    return flask.render_template('login.html', form=login_form)


@my_app.route('/home', methods=['GET', 'POST'])
def home():
    contact_form = Contact()
    if contact_form.validate_on_submit():
        print(contact_form.firstName.data)
        print(contact_form.lastName.data)
        print(contact_form.age.data)

        return 'contact validation successful'

    return flask.render_template('contact.html', form=contact_form)
