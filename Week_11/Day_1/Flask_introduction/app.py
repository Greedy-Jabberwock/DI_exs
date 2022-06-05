from flask import Flask, render_template

app = Flask(__name__)


# view
@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/<username>')
def index(username: str):
    return render_template('index.html', username=username)


@app.route('/articles')
def articles():
    return render_template('articles.html')


if __name__ == '__main__':
    app.run(debug=True)
