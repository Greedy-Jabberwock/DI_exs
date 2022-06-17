import flask_wtf
import wtforms

def no_less(form, field):
    if field.data <= 0:
        raise wtforms.ValidationError('Field must be positive number.')


class AddCity(flask_wtf.FlaskForm):

    name = wtforms.StringField(label='City name',
                               validators=[wtforms.validators.InputRequired(),
                                           wtforms.validators.Length(max=15)])
    country = wtforms.StringField(label='Country',
                                  validators=[wtforms.validators.InputRequired()])
    inhabitants = wtforms.IntegerField(label='Inhabitants',
                                       validators=[wtforms.validators.InputRequired(),
                                                   no_less])
    area = wtforms.IntegerField(label='Square')

    description = wtforms.TextAreaField('Description')
    capital = wtforms.BooleanField('Is capital')

    file = wtforms.FileField('City image')

    submit = wtforms.SubmitField('Add city')
