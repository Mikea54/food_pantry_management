"""Application entry point that seeds a default admin account."""

from werkzeug.security import generate_password_hash

from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

# Create the database tables and seed an initial admin user if none exist.
with app.app_context():
    db.create_all()
    if not User.query.filter_by(role="admin").first():
        admin = User(
            email="admin@example.com",
            password_hash=generate_password_hash("password"),
            role="admin",
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
