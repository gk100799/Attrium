from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from contents.models import Users


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30, message="Name should be between 2 and 20 letters")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Enter a valid email address"), ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20, message="Password must be between 8 and 20 characters")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8, max=20, message="Password must be between 8 and 20 characters"), EqualTo('password', message="Passwords do not match")])
    sign_up = SubmitField('Sign Up')

    def validate_email(form, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address is already registered') 
    


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Enter a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    sign_in = SubmitField('Sign In')


