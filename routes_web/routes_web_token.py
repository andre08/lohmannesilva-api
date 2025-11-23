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
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = token_lista_selecionado(id)
    if not resultado:
        resultado = Token(None).to_dict()

    return render_template("admin_token_detalhe.html", token=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_token.route('/editar/<int:id>', methods=["GET"])
def rota_token_pagina_editar(id):
    resultado, mensagem = token_lista_selecionado(id)
    if not resultado:
        resultado = Token(None).to_dict()
    return render_template("admin_token_editar.html", token=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_token.route('/tokens', methods=["GET"])
def rota_token_listar_todos():
    resultado, mensagem = token_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_token.route('/token/<int:id>', methods=["GET"])
def rota_token_listar_selecionado(id):
    resultado, mensagem = token_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

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
    resultado, mensagem = token_salvar_novo(Token(None, idusuario, token, secret_key, dt_criacao, dt_expiracao, desativado, dt_desativado, dt_atualizado))
    if resultado==True:
        mensagem = "Token salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o token [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

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
    resultado, mensagem = token_alterar_existente(Token(idtoken, idusuario, token, secret_key, dt_criacao, dt_expiracao, desativado, dt_desativado, dt_atualizado))
    if resultado==True:
        mensagem = "Token alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o token"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_token.route('/token/<int:id>', methods=["DELETE"])
def rota_token_excluir_existente(id):
    resultado, mensagem = token_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
