from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, current_user

from pantry.decorators import admin_required

app = Flask(__name__)
app.secret_key = 'changeme'
login_manager = LoginManager(app)

# Dummy user store
USERS = {
    'admin': {'id': 'admin', 'role': 'admin'},
    'staff': {'id': 'staff', 'role': 'staff'},
    'volunteer': {'id': 'volunteer', 'role': 'volunteer'},
}

class User(UserMixin):
    def __init__(self, user_id, role):
        self.id = user_id
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return None
    return User(user_id=user['id'], role=user['role'])

@app.route('/login/<user_id>')
def login(user_id):
    user = load_user(user_id)
    if not user:
        return 'Unknown user', 404
    login_user(user)
    return f'Logged in as {user_id}'

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    return 'Welcome to the admin dashboard'

if __name__ == '__main__':
    app.run(debug=True)
