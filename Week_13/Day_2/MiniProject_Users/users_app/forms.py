import re
import wtforms
from wtforms.validators import DataRequired, Length, InputRequired, ValidationError, Regexp
from flask_wtf import FlaskForm

string_pattern = r'^[a-zA-Z]+\s?[a-zA-Z]+$'
string_message = 'Only digits with one space allowed.'
digit_pattern = r'^[0-9]+-?[0-9]+$'
digit_message = 'Only digits with one "-" allowed.'


class AddUser(FlaskForm):
    user_name = wtforms.StringField('User name', validators=[Length(2), InputRequired(), Regexp(string_pattern, message=string_message)])
    city = wtforms.StringField('City', validators=[Length(2), InputRequired(), Regexp(string_pattern, message=string_message)])
    street = wtforms.StringField('Street', validators=[Length(2), InputRequired(), Regexp(string_pattern, message=string_message)])
    zipcode = wtforms.StringField('Zipcode', validators=[Length(2), InputRequired(), Regexp(digit_pattern, message=digit_message)])
    submit = wtforms.SubmitField('Add user')


class Login(FlaskForm):
    user_name = wtforms.StringField('User name', validators=[Length(2), InputRequired(), Regexp(string_pattern, message=string_message)])
    city = wtforms.StringField('City', validators=[Length(2), InputRequired(), Regexp(string_pattern, message=string_message)])
    submit = wtforms.SubmitField('LogIn')
