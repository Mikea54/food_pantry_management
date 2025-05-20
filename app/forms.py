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
