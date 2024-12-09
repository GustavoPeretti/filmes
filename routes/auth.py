from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from ..database.db import db
from ..services.email_server import smtp_server
import uuid
import os

auth = Blueprint('auth', __name__)

@auth.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.json

        if ('usuario' not in dados) or ('email' not in dados) or ('senha' not in dados):
            return jsonify({'ok': False, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400
        
        usuario_ja_existente = db.query('SELECT * FROM usuarios WHERE usuario = %s OR email = %s;', dados['usuario'], dados['email'])

        if usuario_ja_existente:
            return jsonify({'ok': False, 'mensagem': 'Nome de usuário ou e-mail já utilizado(s).'}), 400
        
        codigo = str(uuid.uuid4())

        db.query('INSERT INTO usuarios (usuario, email, senha, codigo) VALUES (%s, %s, SHA2(%s, 256), %s);', dados['usuario'], dados['email'], dados['senha'], codigo)

        smtp_server.send_email('Verificar e-mail', f'<h1>Oi, verifique seu e-mail.</h1><p>Verifique seu e-mail com o link abaixo:</p><a href="{os.environ.get('WEBSITE_PREFIX')}/auth/verificar/{codigo}">Link</a>', dados['email'])

        return jsonify({'ok': True, 'mensagem': 'Usuário cadastrado. Verificar e-mail.'})

    return render_template('cadastro.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        dados = request.json

        if ('email' not in dados) or ('senha' not in dados):
            return jsonify({'ok': False, 'mensagem': 'Parâmetro obrigatório sem argumento.'}), 400

        usuario = db.query('SELECT * FROM usuarios WHERE email = %s AND senha = SHA2(%s, 256);', dados['email'], dados['senha'])

        if not usuario:
            return jsonify({'ok': False, 'mensagem': 'Usuário não existente ou senha incorreta.'}), 400

        usuario = usuario[0]

        if not usuario['verificado']:
            return jsonify({'ok': False, 'mensagem': 'Usuário não verificado.'}), 400

        session['usuario'] = {
            'usuario': usuario['usuario'],
            'email': usuario['email']
        }
            
        return jsonify({'ok': True, 'mensagem': 'Usuário autenticado.'}), 200

    return render_template('login.html')

@auth.route('/conta')
def conta():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('conta.html')

@auth.route('/verificar')
def verificar():
    return render_template('verificar.html')

@auth.route('/verificar/<codigo>')
def verificar_codigo(codigo):
    usuario = db.query('SELECT * FROM usuarios WHERE codigo = %s;', codigo)

    if not usuario:
        return redirect(url_for('home.home_handler'))
    
    usuario = usuario[0]

    db.query('UPDATE usuarios SET verificado = true WHERE usuario = %s;', usuario['usuario'])
    
    session['usuario'] = {
        'usuario': usuario['usuario'],
        'email': usuario['email']
    }

    return redirect(url_for('home.home_handler'))
