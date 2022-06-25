from schedule_app import app
from flask import render_template, redirect, url_for, flash
from schedule_app.forms import AddTodo
from schedule_app.models import Todo


def get_task(todo_id):
    return Todo.query.filter_by(id=todo_id).first()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddTodo()
    if form.validate_on_submit():
        task = Todo(details=form.task.data)
        task.save_task_to_db()
        return redirect(url_for('index'))
    tasks = Todo.get_tasks()
    return render_template('index.html', form=form, task_list=tasks)


@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    current_task = get_task(todo_id)
    current_task.set_task_as_complete()
    return redirect(url_for('index'))


@app.route('/remove/<int:todo_id>')
def remove_task(todo_id):
    current_task = get_task(todo_id)
    current_task.remove_task()
    return redirect(url_for('index'))


@app.route('/remove_all')
def remove_all():
    Todo.remove_all()
    return redirect(url_for('index'))
