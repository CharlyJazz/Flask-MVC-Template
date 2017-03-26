from wtforms import *
from flask_security.forms import RegisterForm

class SecurityRegisterForm(RegisterForm):
    username = StringField('Username',   [
        validators.Regexp('^\w+$', message="Regex: Username must contain only letters numbers or underscore"),
        validators.DataRequired(message='El campo esta vacio.'),
        validators.length(min=5, message='Min 5 letter, Try Again')])