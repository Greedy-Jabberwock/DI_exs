from flask import Flask, render_template
from faker import Faker
from datetime import datetime, timedelta
import json

app = Flask(__name__)


def create_posts():
    posts = []
    fake = Faker()
    start_date = datetime.now() - timedelta(weeks=100)
    for _ in range(5):
        posts.append({
            'title': fake.text(20),
            'author': fake.name(),
            'content': fake.sentence(40),
            'date': fake.date_between(start_date).strftime('%D')
        })
    posts = sorted(posts, key=lambda x: x['date'])
    with open('posts.json', 'w') as file:
        json.dump(posts, file, indent=4)


@app.route('/')
@app.route('/blog')
@app.route('/<username>')
def blog(username=None):
    return render_template('homepage.html', username=username, title='Welcome')


@app.route('/blog/articles')
def articles():
    with open('posts.json') as file:
        posts = json.load(file)
    return render_template('articles.html', posts=posts,
                           title='Articles')


if __name__ == '__main__':
    create_posts()
    app.run(debug=True, port=666)
