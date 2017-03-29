from flask.ext.via.routers import default
from views import *

routes = [
    default.Functional('/food', profile),
    default.Functional('/food/upload', upload)
]