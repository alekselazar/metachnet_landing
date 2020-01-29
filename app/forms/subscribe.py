from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Email, ValidationError
from app.model.subscribed_table import Subscribed

class Subscribe(FlaskForm):
	email = TextField(description='Email address', validators=[DataRequired(), Email()])
	name = TextField(description="First Name", validators = [DataRequired()])
	fname = TextField(description="Family Name", validators = [DataRequired()])