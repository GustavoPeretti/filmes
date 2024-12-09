from flask import Blueprint, render_template, session, redirect, url_for

home = Blueprint('home', __name__)

@home.route('/')
def home_handler():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('pagina-principal.html')

@home.route('/lista')
def lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('nova-lista.html')

@home.route('/lista/<int:id>')
def gerenciar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('gerenciar-lista.html')