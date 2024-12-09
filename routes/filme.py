from flask import Blueprint, jsonify, session, redirect, url_for
from ..database.db import db

filme = Blueprint('filme', __name__)

@filme.route('/')
def buscar_todos_filmes():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    resultado = db.query('SELECT * FROM filmes;')

    return jsonify({'ok': True, 'resultado': resultado})

@filme.route('/<pesquisa>')
def buscar_filmes(pesquisa):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    resultado = db.query('SELECT * FROM filmes WHERE titulo LIKE %s;', '%' + pesquisa + '%')

    return jsonify({'ok': True, 'resultado': resultado})
