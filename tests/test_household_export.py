from app import create_app
from app.extensions import db
from app.models import Household


def test_household_csv_export():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        h = Household(head_name='Jane Doe', contact_phone='555-1234', address='1 Main St', eligibility_status='eligible', member_count=4)
        db.session.add(h)
        db.session.commit()
        with app.test_client() as client:
            resp = client.get('/households/export')
            assert resp.status_code == 200
            assert resp.headers['Content-Type'].startswith('text/csv')
            data = resp.get_data(as_text=True)
            assert 'head_name' in data and 'Jane Doe' in data
