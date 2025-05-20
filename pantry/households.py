from flask import Blueprint, render_template
from flask_login import login_required

# Example in-memory household records
HOUSEHOLDS = [
    {"head_name": "John Doe", "eligible": True, "members": 4},
    {"head_name": "Jane Smith", "eligible": False, "members": 2},
    {"head_name": "Bob Johnson", "eligible": True, "members": 6},
]

household_bp = Blueprint('households', __name__)


@household_bp.route('/households')
@login_required
def list_households():
    """Display households in a table."""
    return render_template('household_list.html', households=HOUSEHOLDS)
