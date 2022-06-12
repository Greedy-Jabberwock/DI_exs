import flask_wtf
import wtforms


class NumOfChars:
    def __init__(self, str_length):
        self.str_length = str_length

    def __call__(self, form, field):
        if len(field.data) < self.str_length:
            raise wtforms.ValidationError('Field must be bigger then 5 characters')


class Login(flask_wtf.FlaskForm):
    username = wtforms.StringField('Name')
    password = wtforms.PasswordField('Password', [wtforms.validators.DataRequired(), NumOfChars(5)])
    bio = wtforms.StringField('Bio')
    submit = wtforms.SubmitField('Submit')


class Contact(flask_wtf.FlaskForm):
    firstName = wtforms.StringField('First name', [wtforms.validators.DataRequired(), NumOfChars(2)])
    lastName = wtforms.StringField('Last name', [wtforms.validators.DataRequired(), NumOfChars(2)])
    age = wtforms.IntegerField('Age: ', [wtforms.validators.DataRequired(), wtforms.validators.NumberRange(0, 120)])
    submit = wtforms.SubmitField('Submit')

