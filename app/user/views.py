from flask import request, url_for, redirect, render_template, session
from flask.views import MethodView
from ..models import FinalUserImage, db
from forms import UserImageForm
from flask_security import current_user
from . import user_photo
from .. import app

class ProfileView(MethodView):
    def get(self):
        return render_template('user/profile.html')

class UserUploadView(MethodView):
    def get(self):
        return render_template('user/upload.html', form=UserImageForm())

    def post(self):
        if 'profile_photo' in request.files:
            filename = user_photo.save(request.files['profile_photo'])
            image = FinalUserImage(user_id=current_user.id,
                                   image_filename=filename,
                                   image_url=app.config['UPLOADED_USER_DEST'] + filename)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('user.profile'))
        return redirect(url_for('user.profile'))