import os
import random, string

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig(object):
    # Flask

    SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0

    #Flask-Assets

    ASSETS_DEBUG = False

    # Flask-Via

    VIA_ROUTES_MODULE = "app.routes"

    #Flask-Security

    SECURITY_REGISTERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_LOGIN_URL = '/login/'
    SECURITY_LOGOUT_URL = '/logout/'
    SECURITY_REGISTER_URL = '/register/'
    SECURITY_POST_LOGIN_VIEW = "/"
    SECURITY_POST_LOGOUT_VIEW = "/"
    SECURITY_POST_REGISTER_VIEW = "/"
    SECURITY_LOGIN_USER_TEMPLATE = 'security/login.html'
    SECURITY_REGISTER_USER_TEMPLATE = 'security/register.html'

    #Flask-SQLAlchemy

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #Flask-Script

    APP_FOLDER = "app/"

    #Flask-Uploads

    UPLOADED_RESTAURANT_DEST  = APP_FOLDER + "static/img/restaurant"
    UPLOADED_RESTAURANT_URL = 'http://0.0.0.0:8000/restaurant/upload'
    UPLOADED_FOOD_DEST = APP_FOLDER + "static/img/food"
    UPLOADED_FOOD_URL = 'http://0.0.0.0:8000/food/upload'
    UPLOADED_USER_DEST = APP_FOLDER + "static/img/user"
    UPLOADED_USER_URL = 'http://0.0.0.0:8000/user/upload'

    #OAUTH LOGIN

    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '638111216387395',
            'secret': 'c374a53decb75c2043ccd0e4a0eb8c28'
        },
        'twitter': {
            'id': 't6nK168ytZ7w7Rj4uJD3bXi5L',
            'secret': 'L537M7QT810Qe0zMCB1od3bKe6ljx2nyDkxxF49gaHtSJrmHA1'
        },
        'google': {
            'id': '1080912678595-adm52eo5f78jru65923qia22itfasa7d.apps.googleusercontent.com',
            'secret': '1vq9zxw2rMiBtUVeLlAlNOVw'
        }
    }

class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'testing.db'))

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}