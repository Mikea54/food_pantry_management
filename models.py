from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Initialize SQLAlchemy instance

db = SQLAlchemy()

class User(db.Model):
    """User model for authentication and roles."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), default='staff')  # [admin, staff, volunteer]

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

