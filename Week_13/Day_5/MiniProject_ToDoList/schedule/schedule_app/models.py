from schedule_app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def set_task_as_complete(self):
        Todo.query.filter_by(id=self.id).update(dict(completed=True))
        db.session.commit()

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_task(self):
        task = Todo.query.get(self.id)
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def remove_all():
        Todo.query.delete()
        db.session.commit()

    @staticmethod
    def get_tasks():
        return Todo.query.all()

    def __repr__(self):
        return f'<Todo {self.id}, {self.details}>'
