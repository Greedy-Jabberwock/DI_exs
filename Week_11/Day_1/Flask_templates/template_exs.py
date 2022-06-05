from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)



# view
@app.route('/')
def index():
    return redirect(url_for('blog'))


@app.route('/blog')
def blog():
    return render_template("homepage.html", firstname='John', lastname='Doe')


@app.route('/blog/articles')
def articles():
    articles_d = {'first': "News", 'second': "Links", 'third': "Help"}
    return render_template("articles.html",
                           article1=articles_d['first'],
                           article2=articles_d['second'],
                           article3=articles_d['third'])


@app.route('/profile')
def redirecting_view():
    return redirect(url_for('blog'))


if __name__ == '__main__':
    app.run(debug=True)
