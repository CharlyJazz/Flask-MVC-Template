from flask_via.routers.default import Pluggable
from .views import *

routes = [
    Pluggable('/food/', ProfileView, 'profile'),
    Pluggable('/food/upload', FoodUploadView, 'upload')
]