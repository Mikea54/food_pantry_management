from flask import Blueprint, render_template
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin')
@login_required
def index():
    return render_template('admin_index.html')

from flask import request, redirect, url_for, flash
from pantry.decorators import admin_required
from .forms import UserRegistrationForm
from .models import User
from .extensions import db
from werkzeug.security import generate_password_hash


@admin_bp.route('/admin/users/new', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password_hash=generate_password_hash(form.password.data),
                    role=form.role.data)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('admin.index'))
    elif request.method == 'POST':
        flash('Please correct the errors in the form.', 'error')
    return render_template('admin_new_user.html', form=form)
