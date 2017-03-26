from flask.ext.via.routers import default
from views import *

routes = [
    default.Functional('/user', profile)
]