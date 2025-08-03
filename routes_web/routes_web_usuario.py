# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.usuario_service import criar_usuario, logon_usuario

#registrando as rotas na aplicação
routes_web_usuario = Blueprint('routes_web_usuario', __name__)

#Pagina de login
@routes_web_usuario.route('/login')
def login():
    return render_template('login.html')

#Rota para finalizar a sessão
@routes_web_usuario.route('/logout')
def logout():
    # Limpando a sessão
    session.clear()
    # Redirecionando para a pagina principal
    return redirect(url_for('routes_web_usuario.login'))

#Rota para validar usuário e senha e gerar sessão
@routes_web_usuario.route('/logon', methods=['POST'])
def logon():
    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")
    
    usuario = logon_usuario(email, senha)
    if usuario:

        session["usuario_id"] = usuario.id           # ID no banco
        session["usuario_nome"] = usuario.nome       # Nome para exibir na interface
        session["token_id"] = usuario.token_ativo    # ID do token que foi gerado (para controlar no banco)
        session["autenticado"] = True
        
        return jsonify({'success': True, 'mensagem':'Login realizado com sucesso!', 'redirect': url_for('home')})
    
    else:
        return jsonify({'success': False, 'mensagem':'Email e/ou senha invalído!.', 'redirect': url_for('routes_web_usuario.login')})

#pagina de criação de nova conta
@routes_web_usuario.route("/registro")
def registro():
    return render_template('registro.html')

#pagina para criar uma nova conta de acesso
@routes_web_usuario.route('/nova_conta', methods=['POST'])
def nova_conta():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    senha_hash = generate_password_hash(senha)
    
    criar_usuario(nome, email, senha_hash)
    return jsonify({'success': True, 'mensagem':'Conta criada com sucesso!', 'redirect': url_for('routes_web_usuario.login')})