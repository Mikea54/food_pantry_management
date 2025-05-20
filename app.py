from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from models import db, User
import os

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://localhost/food_pantry'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'changeme'  # You should secure this in production

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'  # You can change this route name

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Routes
    @app.route('/')
    def index():
        return 'Food Pantry Management System'

    # Optional: re-add the login route if needed
    from flask_login import login_user
    @app.route('/login/<int:user_id>')
    def login(user_id):
        user = load_user(user_id)
        if not user:
            return 'Unknown user', 404
        login_user(user)
        return f'Logged in as {user.username}'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
