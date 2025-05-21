from flask_login import LoginManager
from models import db as base_db

login_manager = LoginManager()
db = base_db
