Flask-MVC Template
------------------
Flask-MVC Template It is a template with "batteries included" created for the fast development of applications in the microframework flask


Status: **building** :construction:


Feature:
--------
[Flask-Via](http://flask-via.soon.build/en/latest/):
For create routes like a [Django Rest Framework](http://www.django-rest-framework.org) style using Blueprints!

[Flask-Security](https://pythonhosted.org/Flask-Security/):
To easily have login, logout, recovery password and to keep administrator views restricted.

This template has a sub folder in templates / security in which are the custom templates for flask-security. Already configured.

[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/):
A cool admin interface customizable for your models and assets recources.

**Add yours models in the file admin.py**

[Flask-Upload](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/):
This template brings an example of how to use flask-upload in different blueprints and how to save the url of file in the database

**Delete restaurant and food folders and rewrite app / __ init__.py for delete the pretty example**

[Flask-Script](https://flask-script.readthedocs.io/en/latest/):
Awesome commands for your projects, including the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) commands:
- `createadmin`: Create admin user
- `createapp`: Scaffold new  blueprint folder and register in the file app/routes.py

[Rauth](https://rauth.readthedocs.io/en/latest/)
Social Login with facebook, google and twitter

TODO:
-----

* [x] Flask-Script
    * [x] Admin command
    * [x] Create app command
* [x] Flask-Migrate
* [x] Flask-Uploads
    * [x] Create one instance of this in each blueprint
* [x] Oauth
    * [x] Facebook
    * [x] Twitter
    * [x] Google
* [x]  Create command to create an admin
* [x]  Factory App
* [ ]  HTTP Templates for error handling
* [ ]  Create server script
* [ ]  Create easy way for Unit Test and Front-End Test
* [ ]  Implement cool and easy use Flash Messages
* [ ]  Create utils macros
* [ ]  Create filters in filter.py and register this
