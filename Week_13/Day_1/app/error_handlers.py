from app import app
from flask import render_template


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404_error.html'), 404


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500_error.html'), 500