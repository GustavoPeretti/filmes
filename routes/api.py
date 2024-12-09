from flask import Blueprint, jsonify, request, session, redirect, url_for
from ..database.db import db

api = Blueprint('api', __name__)

@api.route('/lista', methods=['GET'])
def buscar_listas():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    try:
        resultado = db.query('SELECT * FROM listas;')
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    return jsonify(resultado)

@api.route('/lista/<int:id>', methods=['GET'])
def buscar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    try:
        resultado = db.query('SELECT * FROM listas WHERE id = %s;', id)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    return jsonify(resultado[0])

@api.route('/lista', methods=['POST'])
def cadastrar_lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    # if 'titulo' not in dados

@api.route('/lista/<int:id>', methods=['UPDATE'])
def atualizar_lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return ''

@api.route('/lista/<int:id>', methods=['DELETE'])
def deletar_lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return ''