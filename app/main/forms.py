from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField ,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitch(FlaskForm):
    title = StringField('pitch title',validators = [Required()])
    body = TextAreaField('write the pitch',validators = [Required()])
    category = StringField('input category, Business,Sport,Religious,Educational',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('write a comment', validators=[Required()])
    submit = SubmitField('Submit')