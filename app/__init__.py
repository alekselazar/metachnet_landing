from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config = True)

app.config.from_mapping(SECRET_KEY = 'dev',
                        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db',
                        SQLALCHEMY_TRACK_MODIFICATIONS = True
                        )

db = SQLAlchemy(app)
db.init_app(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
toolbar = DebugToolbarExtension(app)

from app.controllers import index, white_paper, error
