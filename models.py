"""Database models used in the tests and example application."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model for authentication and roles."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), default='staff')  # [admin, staff, volunteer]

    def set_password(self, password: str) -> None:
        """Hash and store the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Return ``True`` if the given password matches this user."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:  # pragma: no cover - simple debug representation
        return f"<User {self.email}>"

def get_user_by_email(email: str) -> "User | None":
    """Convenience helper to fetch a ``User`` by email."""
    return User.query.filter_by(email=email).first()


class Household(db.Model):
    """Model storing household information for pantry clients."""

    id = db.Column(db.Integer, primary_key=True)
    head_name = db.Column(db.String(150), nullable=False)
    contact_phone = db.Column(db.String(50))
    address = db.Column(db.String(200))
    eligibility_status = db.Column(db.String(50))
    member_count = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    members = db.relationship('HouseholdMember', backref='household', lazy=True, cascade="all, delete-orphan")


class HouseholdMember(db.Model):
    """Individual member belonging to a household."""

    id = db.Column(db.Integer, primary_key=True)
    household_id = db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    relation = db.Column(db.String(50))
