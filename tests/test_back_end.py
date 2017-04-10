import unittest

from flask_testing import TestCase

from faker import Factory
from faker.providers.misc import Provider

from app import create_app, user_datastore
from app.models import *

fake = Factory.create()


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        return app

    def setUp(self):
        email_admin = fake.email()
        db.session.commit()
        db.drop_all()
        db.create_all()

        user_datastore.create_user(email = fake.email(), username=fake.name(), password=Provider.password())
        user_datastore.create_user(email=email_admin, username=fake.name(), password=Provider.password())
        user_datastore.find_or_create_role(name='admin', description='Administrator')
        user_datastore.find_or_create_role(name='end-user', description='End user')
        user_datastore.add_role_to_user(email_admin, 'admin')
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestUserRoles(TestBase):

    def test_count_user(self):
        self.assertEqual(FinalUser.query.count(), 2)

    def test_find_admin_role(self):
        self.assertIsNotNone(user_datastore.find_role('admin'))

    def test_find_end_user_role(self):
        self.assertIsNotNone(user_datastore.find_role('end-user'))


if __name__ == '__main__':
    unittest.main()