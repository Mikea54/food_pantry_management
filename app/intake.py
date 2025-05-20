from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import HouseholdIntakeForm

intake_bp = Blueprint('intake', __name__)


@intake_bp.route('/intake', methods=['GET', 'POST'])
def household_intake():
    form = HouseholdIntakeForm()
    if form.validate_on_submit():
        flash('Household information submitted', 'success')
        return redirect(url_for('intake.household_intake'))
    return render_template('household_intake.html', form=form)
