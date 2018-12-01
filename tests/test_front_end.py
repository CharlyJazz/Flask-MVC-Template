import unittest
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import time

from faker import Factory
from faker.providers.misc import Provider

from flask import url_for
from flask_testing import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from app import create_app, user_datastore
from app.models import *

fake = Factory.create()

test_admin_email, test_admin_username, test_admin_password = fake.email(), fake.name(), Provider.password(),
test_user_final_email, test_user_final_username, test_user_final_password = fake.email(), fake.name(), Provider.password()

class CreateObjects(object):

    def login_admin_user(self):
        login_link = self.get_server_url() + url_for('security.login')
        self.driver.get(login_link)
        self.driver.find_element_by_id("email").send_keys(test_admin_email)
        self.driver.find_element_by_id("password").send_keys(test_admin_password)

    def login_final_user(self):
        login_link = self.get_server_url() + url_for('security.login')
        self.driver.get(login_link)
        self.driver.find_element_by_id("email").send_keys(test_user_final_email)
        self.driver.find_element_by_id("password").send_keys(test_user_final_password)


class TestBase(LiveServerTestCase):

    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            LIVESERVER_PORT=8000
        )
        return app

    def setUp(self):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        """Setup the test driver and create test users"""
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.get_server_url())

        email_admin = test_admin_email

        db.session.commit()
        db.drop_all()
        db.create_all()

        user_datastore.create_user(email=test_admin_email, username=test_admin_username, password=test_admin_password)
        user_datastore.create_user(email=test_user_final_email, username=test_user_final_username, password=test_user_final_password)
        user_datastore.find_or_create_role(name='admin', description='Administrator')
        user_datastore.find_or_create_role(name='end-user', description='End user')
        user_datastore.add_role_to_user(email_admin, 'admin')
        db.session.commit()

    def tearDown(self):
        self.driver.quit()


class TestRegistration(TestBase):

    def test_registration(self):
        # Click register menu link
        self.driver.find_element_by_link_text("Register").click()
        time.sleep(1)
        _password = Provider.password()
        _username = fake.profile()["username"]
        # Fill in registration form
        self.driver.find_element_by_id("email").send_keys(fake.email())
        self.driver.find_element_by_id("username").send_keys(_username)
        self.driver.find_element_by_id("password").send_keys(_password)
        self.driver.find_element_by_id("confirm_password").send_keys(_password)
        self.driver.find_element_by_css_selector('.btn-submit').click()
        time.sleep(1)

        welcome_message = self.driver.find_element_by_id("welcome-message").text
        assert "Hi, {0}!".format(_username) in welcome_message


class TestLogin(TestBase, CreateObjects):

    def test_login_final_user(self):
        self.driver.find_element_by_link_text("Login").click()
        self.login_final_user()
        self.driver.find_element_by_css_selector('.btn-submit').click()

        time.sleep(1)

        welcome_message = self.driver.find_element_by_id("welcome-message").text
        assert "Hi, {0}!".format(test_user_final_username) in welcome_message

    def test_login_admin_user(self):
        self.driver.find_element_by_link_text("Login").click()
        self.login_admin_user()
        self.driver.find_element_by_css_selector('.btn-submit').click()

        time.sleep(1)

        welcome_message = self.driver.find_element_by_id("welcome-message").text
        assert "Hi, {0}!".format(test_admin_username) in welcome_message

class TestAdminSecurity(TestBase, CreateObjects):
    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def test_final_user_access_admin(self):
        self.login_final_user()
        self.driver.find_element_by_css_selector('.btn-submit').click()

        time.sleep(1)

        self.driver.get(self.get_server_url() + url_for('admin.index'))
        self.assertEqual(self.check_exists_by_xpath('//a[text()="Final User"]'), False)

    def test_admin_user_access_admin(self):
        self.login_admin_user()
        self.driver.find_element_by_css_selector('.btn-submit').click()

        time.sleep(1)

        self.driver.get(self.get_server_url() + url_for('admin.index'))
        time.sleep(1)
        self.assertEqual(self.check_exists_by_xpath('//a[text()="Final User"]'), True)


if __name__ == '__main__':
    unittest.main()
