Flask-MVC Template
------------------
[![Build Status](https://travis-ci.org/CharlyJazz/Flask-MVC-Template.svg?branch=master)](https://travis-ci.org/CharlyJazz/Flask-MVC-Template)

Flask-MVC Template It is a template with "batteries included" created for the fast development of applications in the microframework flask

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

[Flask-Testing](https://pythonhosted.org/Flask-Testing/)
Simple test unit with [Faker](https://github.com/joke2k/faker) for generate forget data and unittest
And Selenium webdriver for front end testing
- `python -m unittest discover -p <file.py>`: Test the specific file

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
* [x]  Testing with Flask-Testing
    * [x] Faker for generate forged data
    * [x] Front end test with Selenium webdriver
    * [x] Back end test
* [x]  Create command to create an admin
* [x]  Factory App
* [x]  HTTP Templates for error handling
* [x]  Create easy way for Unit Test

## :warning: Be carefull

Before use this for your projects keep in mind that this project is quite old, and it is preferable to create one with more modern tools and libraries. This project is useful if you want to read the source code and learn a little about the use of Flask on monolithic architectures.

## New version.

Since a lot of extensions of flask are outdated and bugged. We going write features with native flask code, add more features and make the project more clean and easy to use and scale. 

[Issue to track progress](https://github.com/CharlyJazz/Flask-MVC-Template/issues/18)



**REST API:**

- [ ] Endpoints
    - [ ] JWT with RSA2048
    - [ ] Login
    - [ ] Protected endpoint for admin
    - [ ] All users non-protected view
- [ ] API Documentation with [this](https://github.com/CharlyJazz/API-REST-Documentation-Generator) as npm package, more pretty than Swagger

**GRAPHQL API:**

- [ ] Endpoints
    - [ ] JWT with RSA2048
    - [ ] Login
    - [ ] Protected endpoint for admin
    - [ ] All users non-protected view
- [ ] API Documentation with ```graphiql```
