from flask import jsonify, request, url_for, g, redirect, render_template, flash, make_response, Blueprint


def profile():
    return render_template('restaurant/profile.html')

def upload():
    pass