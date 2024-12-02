from flask import Blueprint, jsonify
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
    return ''

@api.route('/lista', methods=['POST'])
def cadastrar_lista():
    return ''

@api.route('/lista/<int:id>', methods=['UPDATE'])
def atualizar_lista():
    return ''

@api.route('/lista/<int:id>', methods=['DELETE'])
def deletar_lista():
    return ''