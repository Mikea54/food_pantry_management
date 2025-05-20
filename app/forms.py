from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserRegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    role = SelectField('Role', choices=[('admin', 'Admin'),
                                        ('user', 'User'),
                                        ('staff', 'Staff'),
                                        ('volunteer', 'Volunteer')],
                        validators=[DataRequired()])
    submit = SubmitField('Create User')


class HouseholdForm(FlaskForm):
    """Form for creating or editing a household."""

    name = StringField('Head of Household', validators=[DataRequired()])
    submit = SubmitField('Save')


class HouseholdMemberForm(FlaskForm):
    """Simple form to add a household member."""

    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Member')
