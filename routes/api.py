from flask import Blueprint, jsonify, request
from ..database.db import db

api = Blueprint('api', __name__)

@api.route('/lista', methods=['GET'])
def buscar_listas():
    try:
        resultado = db.query('SELECT * FROM listas;')
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    return jsonify(resultado)

@api.route('/lista/<int:id>', methods=['GET'])
def buscar_lista(id):
    try:
        resultado = db.query('SELECT * FROM listas WHERE id = %s;', id)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    return jsonify(resultado[0])

@api.route('/lista', methods=['POST'])
def cadastrar_lista():
    dados = request.json

    # if 'titulo' not in dados

@api.route('/lista/<int:id>', methods=['UPDATE'])
def atualizar_lista():
    return ''

@api.route('/lista/<int:id>', methods=['DELETE'])
def deletar_lista():
    return ''