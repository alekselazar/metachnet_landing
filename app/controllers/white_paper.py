from flask import render_template
from app import app


@app.route('/white_paper')
def white_paper():
	return render_template('white_paper.html', title = 'White Paper')
