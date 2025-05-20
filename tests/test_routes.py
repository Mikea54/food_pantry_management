import pytest
from app import create_app
from flask.testing import FlaskClient


def test_index_route_returns_200():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Food Pantry' in response.data or b'Hello' in response.data

