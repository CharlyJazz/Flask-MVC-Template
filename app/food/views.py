from flask import request, url_for, redirect, render_template, current_app
from flask.views import MethodView
from ..models import FinalUserImage, db
from .forms import FoodImageForm
from flask_security import current_user
from . import food_photo
# from .. import app

class ProfileView(MethodView):
    def get(self):
        return render_template('food/profile.html')

class FoodUploadView(MethodView):
    def get(self):
        return render_template('food/upload.html', form=FoodImageForm())

    def post(self):
        if 'food_photo' in request.files:
            filename = food_photo.save(request.files['food_photo'])
            image = FinalUserImage(user_id=current_user.id,
                                   image_filename=filename,
                                   image_url=current_app.config['UPLOADED_FOOD_DEST'][11:] + "/" + filename)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('food.profile'))
        return redirect(url_for('food.profile'))