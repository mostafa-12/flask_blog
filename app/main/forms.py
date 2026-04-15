from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', render_kw={"rows": 3}, validators=[DataRequired()])
    submit = SubmitField('Submit')