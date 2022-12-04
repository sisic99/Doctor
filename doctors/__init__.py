from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import datetime 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctors_db.db'
app.config['SECRET_KEY'] = '00355475c0a17e0e686f150a7b3a132c'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
app.app_context().push()

from doctors import routes


