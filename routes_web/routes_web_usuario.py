# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

# Importando modulos
from services.usuario_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_usuario = Blueprint('routes_web_usuario', __name__)

#Pagina de login
@routes_web_usuario.route('/login')
def rota_usuario_login():
    return render_template('login.html')

#Rota para validar usuário e senha e gerar sessão
@routes_web_usuario.route('/logon', methods=['POST'])
def rota_usuario_logon():

    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")
    
    usuario, mensagem = usuario_logon(email)
    if usuario:
        if check_password_hash(usuario.senha, senha):
            session["usuario_id"] = usuario.idusuario    # ID no banco
            session["usuario_nome"] = usuario.nome       # Nome para exibir na interface
            session["autenticado"] = True        
            return jsonify({'success': True, 'mensagem':'Login realizado com sucesso!', 'redirect': url_for('admin')})
        
        else:
            session.pop("usuario_id", None)    
            session.pop("usuario_nome", None)
            session.pop("autenticado", False)
            return jsonify({'success': False, 'mensagem':'Email e/ou senha inválido!.', 'redirect': url_for('routes_web_usuario.rota_usuario_login')})
    else:
        session.pop("usuario_id", None)    
        session.pop("usuario_nome", None)
        session.pop("autenticado", False)
        return jsonify({'success': False, 'mensagem':'Usuário não localizado!.', 'redirect': url_for('routes_web_usuario.rota_usuario_login')})

#rota para remover a sessão do usuario
@routes_web_usuario.route('/logoff', methods=["GET"])
def rota_usuario_logoff():
    # Limpando a sessão
    session.clear()
    session.pop("usuario_id", None)    
    session.pop("usuario_nome", None)
    session.pop("autenticado", False)
    # Redirecionando para a pagina principal
    return redirect(url_for('routes_web_usuario.rota_usuario_login'))

#pagina de criação de nova conta
@routes_web_usuario.route("/registro")
def rota_usuario_registro():
    return render_template('registro.html')

#pagina para criar uma nova conta de acesso
@routes_web_usuario.route('/nova_conta', methods=['POST'])
def rota_usuario_salvar_novo_publico():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    senha_hash = generate_password_hash(senha)

    usuario = Usuario(None, nome, email, senha_hash)
    resultado, mensagem = usuario_salvar_novo(usuario)

    if resultado:
        return jsonify({'success': resultado, 'mensagem':'Conta criada com sucesso!', 'redirect': url_for('routes_web_usuario.rota_usuario_login')})
    else:
        return jsonify({'success': resultado, "mensagem":mensagem})

#pagina administração de usuarios
@routes_web_usuario.route('/usuario')
def rota_usuario_principal():

    return render_template('admin_usuario.html')


#rota para listar todos os usuários
@routes_web_usuario.route('/usuarios', methods=["GET"])
def rota_usuario_listar_todos():    
    resultado, mensagem = usuario_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um usuário selecionado
@routes_web_usuario.route('/usuario/<int:id>', methods=["GET"])
def rota_usuario_listar_selecionado(id):
    resultado, mensagem = usuario_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})


#rota para listar todos os usuários
@routes_web_usuario.route('/filtro_paginado', methods=["GET"])
def rota_usuario_listar_filtro_paginado():    
    dados = request.get_json()
    ordem = dados.get("ordem")
    filtro = dados.get("filtro")
    pagina = int(dados.get("pagina"))
    quantidade = int(dados.get("quantidade"))

    resultado, totalRegistros, totalPagina, mensagem = usuario_lista_filtrado_paginado(filtro, ordem, pagina, quantidade)
    return jsonify({"dados":resultado, "pagina":pagina, "quantidade":quantidade, "ordem":ordem, "filtro":filtro, "totalRegistros":totalRegistros, "totalPagina":totalPagina, "mensagem":mensagem})

#pagina para criar um novo usuário
@routes_web_usuario.route('/usuario', methods=['POST'])
def rota_usuario_salvar_novo():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    senha_hash = generate_password_hash(senha)

    usuario = Usuario(None, nome, email, senha_hash)
    resultado, mensagem = usuario_salvar_novo(usuario)
    
    if resultado==True:
        mensagem = "Solicitação de contato enviado com sucesso, em breve entraremos em contato, Obrigado!"
    else:
        mensagem = "Erro ao salvar sua solicitação de contato, por favor tente novamente mais tarde"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_usuario.route('/usuario', methods=["PUT"])
def rota_usuario_alterar_existente():

    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    senha_hash = generate_password_hash(senha)

    usuario = Usuario(None, nome, email, senha_hash)
    resultado, mensagem = usuario_alterar_existente(usuario)

    return jsonify({'success': resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_usuario.route('/usuario/<int:id>', methods=["DELETE"])
def rota_contato_excluir_existente(id):
    resultado, mensagem = usuario_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

