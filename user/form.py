from flask_wtf import Form
from wtforms import StringField, validators, PasswordField
from wtforms.fields.html5 import EmailField
class ResgisterForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    username = StringField('Username', [
        validators.Required(),
        validators.length(min=4, max=25)
    ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.length(min=4, max=80),
        validators.EqualTo('confirm', message="Password must match")
    ])
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
        username = StringField('Username', [
            validators.Required(),
            validators.length(min=4, max=25)
        ])
        password = PasswordField('Password', [
            validators.Required(),
            validators.length(min=4, max=80),
        ])
