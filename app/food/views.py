from flask import jsonify, request, url_for, g, redirect, render_template, flash, make_response, Blueprint


def profile():
    return render_template('food/profile.html')

def upload():
    pass