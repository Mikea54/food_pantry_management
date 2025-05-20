from app import create_app
from app.forms import HouseholdForm, HouseholdMemberForm


def test_household_form_requires_name():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_request_context('/intake/new', method='POST', data={'name': ''}):
        form = HouseholdForm()
        assert not form.validate()
        assert 'name' in form.errors


def test_household_member_form_requires_name():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_request_context('/intake/1', method='POST', data={'name': ''}):
        form = HouseholdMemberForm()
        assert not form.validate()
        assert 'name' in form.errors
