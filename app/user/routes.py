from flask_via.routers.default import Pluggable
from .views import *

routes = [
    Pluggable('/user/', ProfileView, 'profile'),
    Pluggable('/user/upload', UserUploadView, 'upload'),

    Pluggable('/authorize/<provider>', OauthAuthorize, 'oauth_authorize'),
    Pluggable('/callback/<provider>', OauthCallback, 'oauth_callback')

]