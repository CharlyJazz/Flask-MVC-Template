from colorama import Fore, init
from flask_script import Manager, prompt
from flask_migrate import Migrate, MigrateCommand
from app import app, db, FinalUser, user_datastore
from flask_security import utils

import re
import os

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def createapp():
    path = prompt(Fore.BLUE + "Write the name of the blueprint")
    try:
        int(path)
        print (Fore.RED + "Name no valid")
        return
    except ValueError:
        pass
    folder = app.config['APP_FOLDER'] + path
    register_blueprint_str = "Blueprint('{0}', 'app.{0}', template_folder='templates')".format(path.lower())
    if not os.path.exists(folder):
        # Scaffold new blueprint
        os.makedirs(folder)
        python_files = ["forms", "routes", "utils", "views", "__init__.py"]
        for i, file in enumerate(python_files):
            with open(os.path.join(folder, file + ".py"), 'w') as temp_file:
                if i != 4:
                    if file is "routes":
                        temp_file.write("from flask.ext.via.routers import default\nfrom views import *\n")
                    if file is "forms":
                        temp_file.write("from wtforms import *\n")
                    if file is "views":
                        temp_file.write("from wtforms import from flask import jsonify, request, "
                                        "url_for, g, redirect, render_template, flash, make_response, Blueprint\n")
                else:
                    os.makedirs(folder + "/template/" + path)

        # Register blueprint in app/route.py
        route_path = os.path.join(app.config['APP_FOLDER'], "routes.py")
        with open(route_path, "r") as old_routes:
            data = old_routes.readlines()
            data[-2] = data[-2] + "    " + register_blueprint_str + ',\n'
            os.remove(os.path.join(app.config['APP_FOLDER'], "routes.py"))

        with open(route_path, 'w') as new_routes:
            new_routes.writelines(data)
    else:
        print (Fore.RED + "This path exist")

@manager.command
def createadmin():
    username = prompt(Fore.BLUE + "Username")
    query_username = db.session.query(FinalUser).filter_by(username=username).first()
    email = prompt(Fore.BLUE + "Write Email")
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) == None:
        print(Fore.RED + "Invalid email format")
        return
    query_email = db.session.query(FinalUser).filter_by(email=email).first()
    if query_username is None and query_email is None:
        password = prompt(Fore.BLUE + "Write password")
        repeat_password = prompt(Fore.BLUE + "Repeat password")
        if password == repeat_password:
            encrypted_password = utils.encrypt_password(password)
            user_datastore.create_user(username=username,
                                       password=encrypted_password,
                                       email=email)
            db.session.commit()
            user_datastore.add_role_to_user(email, 'admin')
            db.session.commit()
            print(Fore.GREEN + "Admin created")
        else:
            print(Fore.RED + "The password does not match")
            return
    else:
        print(Fore.RED + "The username or email are in use")
        return


if __name__ == '__main__':
    manager.run()