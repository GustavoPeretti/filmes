from flask import Blueprint, redirect, url_for, session, request, jsonify
from ..database.db import db
from ..services.email_server import smtp_server
import os
import uuid

user = Blueprint('user', __name__)

@user.route('/', methods=['DELETE'])
def deletar_usuario():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    usuario = session['usuario']

    db.query('DELETE FROM usuarios WHERE usuario = %s;', usuario['usuario'])

    del session['usuario']

    return jsonify({'ok': True, 'mensagem': 'Conta deletada.'}), 200

@user.route('/usuario', methods=['PUT'])
def editar_usuario():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    if 'usuario' not in dados:
        return jsonify({'ok': True, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
    
    usuario = session['usuario']['usuario']

    db.query('UPDATE usuarios SET usuario = %s WHERE usuario = %s;', dados['usuario'], usuario)

    session['usuario']['usuario'] = dados['usuario']
    session.modified = True

    return jsonify({'ok': True, 'mensagem': 'Usuário atualizado.'}), 200
    
@user.route('/email', methods=['PUT'])
def editar_email():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    if 'email' not in dados:
        return jsonify({'ok': True, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
    
    usuario = session['usuario']['usuario']

    codigo = str(uuid.uuid4())

    db.query('UPDATE usuarios SET email = %s, verificado = false, codigo = %s WHERE usuario = %s;', dados['email'], codigo, usuario)

    del session['usuario']
    session.modified = True

    smtp_server.send_email('Verificar e-mail', f'<h1>Oi, verifique seu e-mail.</h1><p>Verifique seu e-mail com o link abaixo:</p><a href="{os.environ.get('WEBSITE_PREFIX')}/auth/verificar/{codigo}">Link</a>', dados['email'])

    return jsonify({'ok': True, 'mensagem': 'E-mail atualizado.'}), 200
    
@user.route('/senha', methods=['PUT'])
def editar_senha():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    dados = request.json

    if 'senha' not in dados:
        return jsonify({'ok': True, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
    
    usuario = session['usuario']['usuario']

    db.query('UPDATE usuarios SET senha = SHA2(%s, 256) WHERE usuario = %s;', dados['senha'], usuario)

    del session['usuario']

    return jsonify({'ok': True, 'mensagem': 'Senha atualizada.'}), 200