from flask import jsonify, request, url_for, g, redirect, render_template, flash, make_response, Blueprint


def profile():
    return render_template('restaurant/profile.html')

# def all():
#     return render_template('restaurant/all.html')
#
# def add():
#     return render_template('restaurant/crud/add.html')
#
# def edit():
#     return render_template('restaurant/crud/edit.html')
#
# def delete():
#     return render_template('restaurant/crud/delete.html')