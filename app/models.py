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
