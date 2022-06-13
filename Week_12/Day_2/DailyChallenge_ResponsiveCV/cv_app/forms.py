import flask_wtf
import wtforms


class CVform(flask_wtf.FlaskForm):
    first_name = wtforms.StringField('First name',
                                     validators=[wtforms.validators.DataRequired(),
                                                 wtforms.validators.Length(min=2, max=32)])
    last_name = wtforms.StringField('Last name',
                                     validators=[wtforms.validators.DataRequired(),
                                                 wtforms.validators.Length(min=2, max=32)])
    job = wtforms.StringField('Job', validators=[wtforms.validators.DataRequired()])
    bio = wtforms.TextAreaField('Bio')
    work = wtforms.TextAreaField('Work', validators=[wtforms.validators.DataRequired()])
    education = wtforms.TextAreaField('Education', validators=[wtforms.validators.DataRequired()])

    submit = wtforms.SubmitField('Submit')
