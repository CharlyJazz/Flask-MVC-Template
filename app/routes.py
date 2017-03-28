from flask.ext.via.routers.default import Blueprint

routes = [
    Blueprint('user', 'app.user', template_folder="templates"),
    Blueprint('restaurant', 'app.restaurant',  template_folder="templates"),
    Blueprint('food', 'app.food', template_folder="templates"),
]