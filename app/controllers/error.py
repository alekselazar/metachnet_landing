from flask import render_template
from app import app

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', message='500 internal error'), 500
