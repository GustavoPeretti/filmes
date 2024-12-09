from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def home_handler():
    return render_template('pagina-principal.html')

@home.route('/lista')
def lista():
    return render_template('nova-lista.html')

@home.route('/lista/<int:id>')
def gerenciar_lista(id):
    return render_template('gerenciar-lista.html')