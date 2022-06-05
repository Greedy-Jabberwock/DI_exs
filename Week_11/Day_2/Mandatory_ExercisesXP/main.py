from helper import header


def make_exercise1():
    import flask
    header('Exercise 1')
    print(dir(flask))


def make_exercise2():
    from flask import Flask, render_template, url_for
    header('Exercise 2')
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(debug=True)


def main():
    make_exercise1()
    make_exercise2()


if __name__ == '__main__':
    main()
