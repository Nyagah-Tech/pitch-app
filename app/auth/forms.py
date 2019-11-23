from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegForm(FlaskForm):
    email = StringField('Your Email Address ...',validators=[Required(),Email()])
    username = StringField('Enter username...',validators=[Required()])
    password = PasswordField('Password...',validators=[Required(),EqualTo('pass_confirm',message = 'password must match')])
    pass_confirm = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')
        
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')