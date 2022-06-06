import flask
import database_manager

app = flask.Flask(__name__)
database_manager.create_database()


@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()
    template_file = open('templates/products.jinja', 'r').read()
    css = open('static/style.css', 'r').read()
    return flask.render_template_string(template_file, products=data,
                                        additional_css=css)


if __name__ == '__main__':
    app.run(debug=True)
