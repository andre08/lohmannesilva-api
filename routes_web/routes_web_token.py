# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.token_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_token = Blueprint('routes_web_token', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_token.route('/', methods=["GET"])
def rota_token_principal():
    return render_template("admin_token.html")

#rota para pagina visualização 
@routes_web_token.route('/ver/<int:id>', methods=["GET"])
def rota_token_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = token_lista_selecionado(id)
    if not resultado:
        resultado = Token(None).to_dict()

    return render_template("admin_token_detalhe.html", token=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_token.route('/editar/<int:id>', methods=["GET"])
def rota_token_pagina_editar(id):
    sucesso, resultado, mensagem = token_lista_selecionado(id)
    if not resultado:
        resultado = Token(None).to_dict()
    return render_template("admin_token_editar.html", token=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_token.route('/tokens', methods=["GET"])
def rota_token_listar_todos():
    sucesso, resultado, mensagem = token_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_token.route('/token/<int:id>', methods=["GET"])
def rota_token_listar_selecionado(id):
    sucesso, resultado, mensagem = token_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_token.route('/token', methods=['POST'])
def rota_token_salvar_novo():
    dados = request.get_json()
    idusuario = dados.get("idusuario")
    token = dados.get("token")
    secret_key = dados.get("secret_key")
    dt_criacao = dados.get("dt_criacao")
    dt_expiracao = dados.get("dt_expiracao")
    desativado = dados.get("desativado")
    dt_desativado = dados.get("dt_desativado")
    dt_atualizado = dados.get("dt_atualizado")
    
    sucesso, resultado, mensagem = token_salvar_novo(Token(None, idusuario, token, secret_key, dt_criacao, dt_expiracao, desativado, dt_desativado, dt_atualizado))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_token.route('/token', methods=["PUT"])
def rota_token_alterar_existente():
    dados = request.get_json()
    idtoken = dados.get("id")
    idusuario = dados.get("idusuario")
    token = dados.get("token")
    secret_key = dados.get("secret_key")
    dt_criacao = dados.get("dt_criacao")
    dt_expiracao = dados.get("dt_expiracao")
    desativado = dados.get("desativado")
    dt_desativado = dados.get("dt_desativado")
    dt_atualizado = dados.get("dt_atualizado")
    
    sucesso, resultado, mensagem = token_alterar_existente(Token(idtoken, idusuario, token, secret_key, dt_criacao, dt_expiracao, desativado, dt_desativado, dt_atualizado))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_token.route('/token/<int:id>', methods=["DELETE"])
def rota_token_excluir_existente(id):
    sucesso, resultado, mensagem = token_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
