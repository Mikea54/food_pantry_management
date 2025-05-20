from flask_login import UserMixin
from werkzeug.security import check_password_hash
from .extensions import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


def get_user_by_email(email: str) -> 'User | None':
    return User.query.filter_by(email=email).first()


class Household(db.Model):
    """Represents a household registered during intake."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    members = db.relationship(
        "HouseholdMember",
        backref="household",
        cascade="all, delete-orphan",
    )


class HouseholdMember(db.Model):
    """Individual member belonging to a household."""

    id = db.Column(db.Integer, primary_key=True)
    household_id = db.Column(db.Integer, db.ForeignKey("household.id"), nullable=False)
    name = db.Column(db.String(150), nullable=False)
