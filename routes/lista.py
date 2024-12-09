from flask import Blueprint, jsonify, request, session, redirect, url_for
from ..database.db import db

lista = Blueprint('lista', __name__)

@lista.route('/', methods=['GET'])
def buscar_listas():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    try:
        resultado = db.query('SELECT * FROM listas;')
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    for lista in resultado:
        lista['filmes'] = db.query('SELECT filmes.titulo, filmes.imagem FROM filmes_listas INNER JOIN filmes ON filmes_listas.id_filme = filmes.id WHERE id_lista = %s;', lista['id'])
    
    return jsonify({'ok': True, 'resultado': resultado}), 200

@lista.route('/<int:id>', methods=['GET'])
def buscar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    try:
        resultado = db.query('SELECT * FROM listas WHERE id = %s;', id)
    except:
        return jsonify({'status': False, 'mensagem': 'Não foi possível processar os dados.'}), 500
    
    return jsonify({'ok': True, 'resultado': resultado[0]}), 200

@lista.route('/', methods=['POST'])
def cadastrar_lista():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    if ('titulo' not in dados) or ('privado' not in dados):
        return jsonify({'ok': False, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
    
    db.query('INSERT INTO listas (titulo, privado, usuario) VALUES (%s, %s, %s);', dados['titulo'], int(dados['privado']), session['usuario']['usuario'])

    if 'filmes' in dados:
        id = db.query('SELECT id FROM listas ORDER BY id DESC;')[0]['id']

        for filme in dados['filmes']:
            db.query('INSERT INTO filmes_listas VALUES (%s, %s);', id, filme)

    return jsonify({'ok': True, 'mensagem': 'Lista cadastrada.'}), 201

@lista.route('/<int:id>', methods=['PUT'])
def atualizar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    parametros = ['titulo', 'privado', 'filmes']

    if not any([parametro in dados for parametro in parametros]):
        return jsonify({'ok': False, 'mensagem': 'Ao menos um parâmetro deve ser informado.'}), 400
    
    lista = db.query('SELECT * FROM listas WHERE id = %s;', id)

    if not lista:
        return jsonify({'ok': False, 'mensagem': f'Não há lista com identificador "{id}".'}), 400

    if 'titulo' in dados:
        db.query('UPDATE listas SET titulo = %s WHERE id = %s;', dados['titulo'], id)

    if 'privado' in dados:
        db.query('UPDATE listas SET privado = %s WHERE id = %s;', int(dados['privado']), id)

    if 'filmes' in dados:
        db.query('DELETE FROM filmes_listas WHERE id_lista = %s;', id)

        for filme in dados['filmes']:
            db.query('INSERT INTO filmes_listas VALUES (%s, %s);', id, filme)

    return jsonify({'ok': True, 'mensagem': 'Lista atualizada.'}), 200
    
@lista.route('/<int:id>', methods=['DELETE'])
def deletar_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    lista = db.query('SELECT * FROM listas WHERE id = %s;', id)

    if not lista:
        return jsonify({'ok': False, 'mensagem': f'Não há lista com identificador "{id}".'}), 400
    
    db.query('DELETE FROM listas WHERE id = %s;', id)

    return jsonify({'ok': True, 'mensagem': 'Lista deletada.'}), 200

@lista.route('/<int:id>/filme', methods=['PUT'])
def filmes_lista(id):
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    if 'filmes' not in dados:
        return jsonify({'ok': False, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
        
    if not isinstance(dados['filmes'], list):
        return jsonify({'ok': False, 'mensagem': 'Argumento em formato inválido.'}), 400
    
    if not dados['filmes']:
        return jsonify({'ok': False, 'mensagem': 'Ao menos um filme deve ser informado.'}), 400
    
    db.query('DELETE FROM filmes_listas WHERE id_lista = id;')

    for filme in dados['filmes']:
        db.query('INSERT INTO filmes_listas VALUES (%s, %s);', id, filme)
    
    return jsonify({'ok': True, 'mensagem': 'Itens inseridos.'}), 200
