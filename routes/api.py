from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/lista', methods=['GET'])
def buscar_listas():
    return ''

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