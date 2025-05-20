from app import create_app
from app.extensions import db
from app.models import Household, HouseholdMember


def setup_app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['LOGIN_DISABLED'] = True
    return app


def test_household_creation_and_detail_retrieval():
    app = setup_app()
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            resp = client.post('/intake/new', data={'name': 'Doe Family', 'submit': 'Save'}, follow_redirects=True)
            assert resp.status_code == 200
            household = Household.query.first()
            assert household is not None
            assert household.name == 'Doe Family'
            detail_resp = client.get(f'/intake/{household.id}')
            assert detail_resp.status_code == 200
            assert b'Doe Family' in detail_resp.data


def test_household_member_creation():
    app = setup_app()
    with app.app_context():
        db.create_all()
        household = Household(head_name='Jane Doe')
        db.session.add(household)
        db.session.commit()
        member = HouseholdMember(name='John', household=household)
        db.session.add(member)
        db.session.commit()
        assert Household.query.count() == 1
        assert HouseholdMember.query.count() == 1
        assert HouseholdMember.query.first().household_id == household.id
