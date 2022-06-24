import flask_wtf
import wtforms


class Search(flask_wtf.FlaskForm):
    search = wtforms.StringField('search', validators=[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField('Search')
