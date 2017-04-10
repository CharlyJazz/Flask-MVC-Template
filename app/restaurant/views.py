from flask import request, url_for, redirect, render_template, current_app
from flask.views import MethodView
from ..models import FinalUserImage, db
from forms import RestaurantImageForm
from flask_security import current_user
from . import restaurant_photo
# from .. import app

class ProfileView(MethodView):
    def get(self):
        return render_template('restaurant/profile.html')

class RestaurantUploadView(MethodView):
    def get(self):
        return render_template('restaurant/upload.html', form=RestaurantImageForm())

    def post(self):
        if 'restaurant_photo' in request.files:
            filename = restaurant_photo.save(request.files['restaurant_photo'])
            image = FinalUserImage(user_id=current_user.id,
                                             image_filename=filename,
                                             image_url=current_app.config['UPLOADED_RESTAURANT_DEST'][11:] + "/" + filename)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('restaurant.profile'))
        return redirect(url_for('restaurant.profile'))