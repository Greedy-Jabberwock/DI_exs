import flask
from Week_12.Day_2.DailyChallenge_ResponsiveCV.cv_app import cv_app
from Week_12.Day_2.DailyChallenge_ResponsiveCV.cv_app.forms import CVform


user_data = None


@cv_app.route('/', methods=['GET', 'POST'])
def index():
    cv_form = CVform()
    if cv_form.validate_on_submit():
        global user_data
        user_data = {
            'first_name': cv_form.first_name.data,
            'last_name': cv_form.last_name.data,
            'job': cv_form.job.data,
            'bio': cv_form.bio.data,
            'work': cv_form.work.data,
            'education': cv_form.education.data
        }

        return flask.redirect(flask.url_for('about', data=user_data))

    return flask.render_template('start_page.html', form=cv_form)


@cv_app.route('/home', methods=['GET', 'POST'])
def home():
    return flask.render_template('index.html', data=user_data)


@cv_app.route('/project', methods=['GET', 'POST'])
def project():
    return flask.render_template('project.html', data=user_data)


@cv_app.route('/about', methods=['GET', 'POST'])
def about():
    return flask.render_template('about.html', data=user_data)
