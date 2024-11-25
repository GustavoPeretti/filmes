from flask import Blueprint, render_template

auth = Blueprint('auth')

@auth.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@auth.route('/login')
def login():
    return render_template('login.html')