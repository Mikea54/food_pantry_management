import pytest
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

from models import db, User
from pantry.decorators import admin_required

@pytest.fixture
def create_user(app):
    def _create_user(email, password='secret', role='staff'):
        user = User(email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    return _create_user

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return True
    return False

@admin_required
def admin_view():
    return "admin"

def test_user_creation_unique_email(app, create_user):
    user = create_user('unique@example.com')
    assert user.id is not None


def test_user_creation_duplicate_email(app, create_user):
    create_user('dup@example.com')
    duplicate = User(email='dup@example.com', role='staff')
    duplicate.set_password('other')
    db.session.add(duplicate)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()


def test_password_hashing_and_verification(app, create_user):
    user = create_user('hash@example.com', 'mypassword')
    assert user.password_hash != 'mypassword'
    assert check_password_hash(user.password_hash, 'mypassword')


def test_login_valid_invalid_credentials(app, create_user):
    user = create_user('login@example.com', 'password123')
    with app.test_request_context():
        assert authenticate('login@example.com', 'password123') is True
        assert current_user.is_authenticated
        logout_user()
        assert authenticate('login@example.com', 'wrong') is False
        assert not current_user.is_authenticated


def test_role_based_access_restrictions(app, create_user):
    admin = create_user('admin@example.com', role='admin')
    staff = create_user('staff@example.com', role='staff')
    with app.test_request_context():
        login_user(admin)
        assert admin_view() == 'admin'
        logout_user()
        login_user(staff)
        with pytest.raises(Exception):
            admin_view()
