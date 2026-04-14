from app.models import User
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_login import current_user

class EditProfileForm(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
    
    def validate(self, extra_validators = None):
        if not super().validate(extra_validators):
            return False
        if User.query.filter_by(username=self.username.data).first() and self.username.data != current_user.username:
            self.username.errors.append('Username already exists. Please choose a different one.')
            return False
        if User.query.filter_by(email=self.email.data).first() and self.email.data != current_user.email:
            self.email.errors.append('Email already exists. Please choose a different one.')
            return False
        return True

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=140)])
    content = TextAreaField('Content', validators=[DataRequired()])
    cover_image = FileField('Cover Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit')