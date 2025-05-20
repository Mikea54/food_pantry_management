from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from .extensions import db
from .models import Household, HouseholdMember
from .forms import HouseholdForm, HouseholdMemberForm

intake_bp = Blueprint('intake', __name__)

@intake_bp.route('/intake')
@login_required
def list_households():
    page = request.args.get('page', 1, type=int)
    households = Household.query.paginate(page=page, per_page=10)
    return render_template('intake_list.html', households=households)

@intake_bp.route('/intake/new', methods=['GET', 'POST'])
@login_required
def new_household():
    form = HouseholdForm()
    if form.validate_on_submit():
        household = Household(name=form.name.data)
        db.session.add(household)
        db.session.commit()
        flash('Household created', 'success')
        return redirect(url_for('intake.household_detail', household_id=household.id))
    elif request.method == 'POST':
        flash('Please correct the errors in the form.', 'error')
    return render_template('intake_new.html', form=form)

@intake_bp.route('/intake/<int:household_id>', methods=['GET', 'POST'])
@login_required
def household_detail(household_id):
    household = Household.query.get_or_404(household_id)
    form = HouseholdForm(obj=household)
    member_form = HouseholdMemberForm()
    if form.submit.data and form.validate_on_submit():
        household.name = form.name.data
        db.session.commit()
        flash('Household updated', 'success')
        return redirect(url_for('intake.household_detail', household_id=household.id))
    elif form.submit.data and request.method == 'POST':
        flash('Error updating household.', 'error')

    if member_form.submit.data and member_form.validate_on_submit():
        member = HouseholdMember(name=member_form.name.data, household=household)
        db.session.add(member)
        db.session.commit()
        flash('Member added', 'success')
        return redirect(url_for('intake.household_detail', household_id=household.id))
    elif member_form.submit.data and request.method == 'POST':
        flash('Error adding member.', 'error')
    members = HouseholdMember.query.filter_by(household_id=household.id).all()
    return render_template('intake_detail.html', form=form, member_form=member_form, household=household, members=members)
