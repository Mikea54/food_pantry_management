from flask import Flask
from flask_migrate import Migrate
from models import db, User
import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://localhost/food_pantry'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def index():
        return 'Food Pantry Management System'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

