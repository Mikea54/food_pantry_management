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


class HouseholdIntakeForm(FlaskForm):
    """Collect basic household information."""

    head_name = StringField('Head of Household', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    eligibility = StringField('Eligibility', validators=[DataRequired()])

    member1_name = StringField('Household Member 1')
    member2_name = StringField('Household Member 2')
    member3_name = StringField('Household Member 3')

    submit = SubmitField('Submit')
