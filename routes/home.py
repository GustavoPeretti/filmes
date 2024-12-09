from flask import Blueprint, render_template, session, redirect, url_for
from ..database.db import db

home = Blueprint('home', __name__)

@home.route('/')
def home_handler():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    listas = db.query('SELECT * FROM listas;')

    for lista in listas:
        lista['filmes'] = db.query('SELECT filmes.titulo, filmes.imagem FROM filmes_listas INNER JOIN filmes ON filmes_listas.id_filme = filmes.id WHERE id_lista = %s;', lista['id'])

    return render_template('pagina-principal.html', listas=listas)

@home.route('/lista')
def lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('nova-lista.html')

@home.route('/lista/<int:id>')
def gerenciar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    lista_especifica = db.query('SELECT * FROM listas WHERE id = %s;', id)[0]

    lista_especifica['filmes'] = db.query('SELECT filmes.titulo, filmes.imagem FROM filmes_listas INNER JOIN filmes ON filmes_listas.id_filme = filmes.id WHERE id_lista = %s;', id)
    
    filmes = db.query('SELECT * FROM filmes;')

    return render_template('gerenciar-lista.html', lista_especifica=lista_especifica, filmes=filmes, titulos=[filme['titulo'] for filme in lista_especifica['filmes']])