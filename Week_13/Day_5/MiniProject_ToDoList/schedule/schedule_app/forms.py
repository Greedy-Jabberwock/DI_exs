import wtforms
import flask_wtf


class AddTodo(flask_wtf.FlaskForm):

    task = wtforms.StringField('Task', validators=[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField('Add task')
