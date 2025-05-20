from flask import Blueprint, render_template
from flask_login import login_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user_dashboard.html')
