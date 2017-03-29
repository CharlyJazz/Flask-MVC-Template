from wtforms import *
from flask_security.forms import RegisterForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from . import user_photo


class SecurityRegisterForm(RegisterForm):
    username = StringField('Username',   [
        validators.Regexp('^\w+$', message="Regex: Username must contain only letters numbers or underscore"),
        validators.DataRequired(message='El campo esta vacio.'),
        validators.length(min=5, message='Min 5 letter, Try Again')])

# Form for demo of flask-upload

class UserImageForm(Form):
    profile_photo = FileField('', validators=[FileRequired(), FileAllowed(user_photo, 'Images only!')])
    submit = SubmitField('Submit')