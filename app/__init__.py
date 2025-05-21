from flask import Flask
from .extensions import db, login_manager
from .models import User
from .routes import bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'dev'  # Optional if already set in Config

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .auth import auth_bp
    from .admin import admin_bp
    from .user import user_bp
    from .intake import intake_bp
    from .households import household_bp  # Use DB-backed version

    app.register_blueprint(bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(intake_bp)
    app.register_blueprint(household_bp)

    return app
