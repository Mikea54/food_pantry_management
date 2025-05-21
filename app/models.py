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
    """Model storing household information for pantry clients."""

    id = db.Column(db.Integer, primary_key=True)
    head_name = db.Column(db.String(150), nullable=False)
    contact_phone = db.Column(db.String(50))
    address = db.Column(db.String(200))
    eligibility_status = db.Column(db.String(50))
    member_count = db.Column(db.Integer, default=1)

    @property
    def name(self) -> str:
        """Alias for head_name to maintain backward compatibility."""
        return self.head_name

    @name.setter
    def name(self, value: str) -> None:
        self.head_name = value

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
