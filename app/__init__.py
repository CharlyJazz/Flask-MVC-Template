import sqlite3

from flask import Flask, render_template
from flask_assets import Environment
from flask_wtf import CSRFProtect
from flask_security import Security, SQLAlchemyUserDatastore, utils
from flask.ext.via import Via
from flask_uploads import configure_uploads

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

from assets import create_assets
from models import db, FinalUser, Role
from user.forms import SecurityRegisterForm


from admin import create_security_admin

import os.path

app = Flask(__name__)

app.config.from_object('config')

csrf = CSRFProtect()
csrf.init_app(app)

assets = Environment(app)
create_assets(assets)

via = Via()
via.init_app(app)

# Code for desmostration the flask upload in several models - - - -

from user import user_photo
from restaurant import restaurant_photo
from food import food_photo

configure_uploads(app, (restaurant_photo, food_photo, user_photo))

with app.app_context():
    db.init_app(app)
    db.create_all()

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not database_exists(engine.url):
    create_database(engine.url)

user_datastore = SQLAlchemyUserDatastore(db, FinalUser, Role)
security = Security(app, user_datastore, register_form=SecurityRegisterForm)

create_security_admin(app=app, path=os.path.join(os.path.dirname(__file__)))

@app.before_first_request
def before_first_request():
    # Create the Roles "admin" and "end-user" -- unless they already exist
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')

    # Create two Users for testing purposes -- unless they already exists.
    encrypted_password = utils.encrypt_password('password')
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(username='end_user',
                                   password=encrypted_password,
                                   email='someone@example.com')
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(username='admin_user',
                                   password=encrypted_password,
                                   email='admin@example.com')

    # Commit any database changes; the User and Roles must exist before we can add a Role to the User
    db.session.commit()

    # Give one User has the "end-user" role, while the other has the "admin" role. (This will have no effect if the
    # Users already have these Roles.) Again, commit any database changes.
    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'admin')
    db.session.commit()

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

from app import *