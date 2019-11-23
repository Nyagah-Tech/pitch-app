from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegForm(FlaskForm):
    email = StringField('Your Email Address ...',validators=[Required(),Email()])
    username = StringField('Enter username...',validators=[Required()])
    password = PasswordField('Password...',validators=[Required(),EqualTo('pass_confirm',message = 'password must match')])
    pass_confirm = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Sign Up')