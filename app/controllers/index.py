from flask import render_template, request, redirect, url_for
from app import app, db
from app.model.subscribed_table import Subscribed
from app.forms.subscribe import Subscribe

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = Subscribe()
	if form.validate_on_submit():
		subscribed = Subscribed(name = form.name.data,
								fname = form.fname.data,
								email = form.email.data)
		db.session.add(subscribed)
		db.session.commit()
		return render_template('index.html', form = form, title = 'Home', just_subscribed = True)
	return render_template('index.html', form = form, title = 'Home', just_subscribed = False)
