from app import app, db
from app.models import Book
from flask import flash, render_template, abort


@app.route('/')
def index():
    flash('This is a flashed message', 'green')
    books = [book.title for book in Book.query.order_by(Book.title.asc())]
    flash('And another one!', 'red')
    return render_template('index.html', books=books)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'MyModel': Book
    }


