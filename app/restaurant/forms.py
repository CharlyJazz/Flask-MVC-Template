from wtforms import *
from flask_wtf.file import FileField, FileAllowed, FileRequired
from . import restaurant_photo

# Form for demo of flask-upload

class RestaurantImageForm(Form):
    profile_photo = FileField('', validators=[FileRequired(), FileAllowed(restaurant_photo, 'Images only!')])
    submit = SubmitField('Submit')