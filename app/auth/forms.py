from flask_login import current_user
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    def validate(self, extra_validators = None):
        if not super().validate(extra_validators):
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            self.email.errors.append("Email not found.")
            return False
        if user.verify_password(self.password.data) == False:
            self.password.errors.append("Incorrect password.")
            return False
        return True
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate(self, extra_validators = None):
        if not  super().validate(extra_validators):
            return False

        if User.query.filter_by(username=self.username.data).first():
            self.username.errors.append("Username is already taken.")
            return False
        if User.query.filter_by(email=self.email.data).first():
            self.email.errors.append("Email is already registered.")
            return False
        return True
    
    
class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')
    
    def validate_current_password(self, field):
        if current_user.verify_password(field.data) == False:
            raise ValidationError('Current password is incorrect.')
