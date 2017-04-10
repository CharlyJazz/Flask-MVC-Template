import unittest
import os

from flask_testing import TestCase as FlaskTestCase

from app import app, db
from app.models import *


class TestBase(FlaskTestCase):
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