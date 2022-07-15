'''
THIS FILE SETS THE APPLICATION GLOBAL CONFIGURATIONS
'''

import flask
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import secrets

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


migrate = Migrate(app, db)
login_manager = LoginManager(app)
from remotework.routes.public import routes
from remotework.routes.admin import routes