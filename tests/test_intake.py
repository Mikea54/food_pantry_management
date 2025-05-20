from app import create_app


def test_household_intake_get():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.get('/intake')
        assert response.status_code == 200


def test_household_intake_post():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        data = {
            'head_name': 'Jane Doe',
            'phone': '1234567890',
            'address': '1 Street',
            'eligibility': 'yes',
            'member1_name': 'Person One',
            'member2_name': '',
            'member3_name': ''
        }
        response = client.post('/intake', data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b'submitted' in response.data.lower()
