from flask.ext.via.routers.default import Pluggable
from views import *

routes = [
    Pluggable('/user/', ProfileView, 'profile'),
    Pluggable('/user/upload', UserUploadView, 'upload')
]