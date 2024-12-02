from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/conta')
def conta():
    return render_template('conta.html')

