import wtforms
import flask_wtf


class AddTodo(flask_wtf.FlaskForm):

    task = wtforms.StringField('Task', validators=[wtforms.validators.InputRequired()])
    image = wtforms.StringField('Image', validators=[wtforms.validators.DataRequired(),
                                                     wtforms.validators.URL()])
    submit = wtforms.SubmitField('Add task')
