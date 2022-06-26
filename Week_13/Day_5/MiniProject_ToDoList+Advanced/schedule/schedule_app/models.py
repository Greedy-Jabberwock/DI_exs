from schedule_app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    image = db.relationship('Image', backref='todo', uselist=False)

    def set_task_as_complete(self):
        Todo.query.filter_by(id=self.id).update(dict(completed=True))
        db.session.commit()

    def save_task_to_db(self, img_src):
        db.session.add(self)
        db.session.commit()
        img = Image(source=img_src, todo_id=self.id)
        db.session.add(img)
        db.session.commit()

    def remove_task(self):
        task = Todo.query.get(self.id)
        img = Image.query.filter_by(todo_id=self.id).first()
        db.session.delete(task)
        db.session.delete(img)
        db.session.commit()

    @staticmethod
    def remove_all():
        db.drop_all()
        db.create_all()
        db.session.commit()

    @staticmethod
    def get_tasks():
        return Todo.query.order_by(Todo.id).all()

    def __repr__(self):
        return f'<Todo {self.id}, {self.details}>'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(500), nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

    def __repr__(self):
        return f'<Image {self.source}>'

