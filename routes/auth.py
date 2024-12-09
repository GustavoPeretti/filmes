from flask import Blueprint, render_template, request, jsonify
from ..database.db import db

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
        
        db.query('INSERT INTO usuarios VALUES (%s, %s, %s);', dados['usuario'], dados['email'], dados['senha'])

        return jsonify({'ok': True, 'mensagem': 'Usuário cadastrado.'})

    return render_template('cadastro.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/conta')
def conta():
    return render_template('conta.html')

