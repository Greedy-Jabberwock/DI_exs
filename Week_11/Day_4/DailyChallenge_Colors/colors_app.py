from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/colored/<color>')
def colored(color):
    return render_template('colored.html', color=color)


if __name__ == '__main__':
    app.run(debug=True)