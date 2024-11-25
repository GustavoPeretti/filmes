from flask import Blueprint, render_template

home = Blueprint('home')

@home.route('/')
def home_handler():
    return render_template('home.html')