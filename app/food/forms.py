from wtforms import *
from flask_wtf.file import FileField, FileAllowed, FileRequired
from . import food_photo

# Form for demo of flask-upload

class FoodImageForm(Form):
    profile_photo = FileField('', validators=[FileRequired(), FileAllowed(food_photo, 'Images only!')])
    submit = SubmitField('Submit')