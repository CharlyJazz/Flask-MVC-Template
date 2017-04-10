from flask import request, url_for, redirect, render_template, flash, current_app
from flask.views import MethodView
from flask_security.utils import login_user
from flask_security import current_user
from flask_security.datastore import SQLAlchemyUserDatastore

from forms import UserImageForm
from oauth import OAuthSignIn

from ..models import FinalUser, FinalUserImage, Role, db
from . import user_photo
# from .. import app

user_datastore = SQLAlchemyUserDatastore(db, FinalUser, Role)

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
                                   image_url=current_app.config['UPLOADED_USER_DEST'][11:] + "/" + filename)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('user.profile'))
        return redirect(url_for('user.profile'))


class OauthAuthorize(MethodView):
    def get(self, provider):
        if not current_user.is_anonymous:
            return redirect(url_for('index'))
        oauth = OAuthSignIn.get_provider(provider)
        return oauth.authorize()

class OauthCallback(MethodView):
    def get(self, provider):
        if not current_user.is_anonymous:
            return redirect(url_for('index'))
        oauth = OAuthSignIn.get_provider(provider)
        social_id, username, email = oauth.callback()
        if social_id is None:
            flash('Authentication failed.')
            return redirect(url_for('index'))
        user = db.session.query(FinalUser).filter_by(email=email).first()
        if user is None:
            user_datastore.create_user(social_id=social_id, username=username, email=email)
            db.session.commit()
            user_datastore.add_role_to_user(email, 'user')
            db.session.commit()
        login_user(user)
        print current_user
        return redirect(url_for('index'))