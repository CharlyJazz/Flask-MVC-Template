import unittest
import os
import urllib2

from flask import abort, url_for
from flask_testing import TestCase

from app import app, db
from app.models import *


class TestBase(unittest.TestCase):
    def setUp(self):
        """
        Will be called before every test
        """
        with app.app_context():
            db.init_app(app)
            app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(app.config['BASE_DIR'], 'unit_test.db')))
            db.session.commit()
            db.drop_all()
            db.create_all()
        return app

if __name__ == '__main__':
    unittest.main()