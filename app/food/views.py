from flask import jsonify, request, url_for, g, redirect, render_template, flash, make_response, Blueprint


def profile():
    return render_template('food/profile.html')

# def all():
#     return render_template('food/all.html')
#
# def add():
#     return render_template('food/crud/add.html')
#
# def edit():
#     return render_template('food/crud/edit.html')
#
# def delete():
#     return render_template('food/crud/delete.html')