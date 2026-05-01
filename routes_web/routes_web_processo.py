# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.processo_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_processo = Blueprint('routes_web_processo', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_processo.route('/', methods=["GET"])
def rota_processo_principal():
    return render_template("admin_processo.html")

#rota para pagina visualização 
@routes_web_processo.route('/ver/<int:id>', methods=["GET"])
def rota_processo_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = processo_lista_selecionado(id)
    if not resultado:
        resultado = Processo(None).to_dict()

    return render_template("admin_processo_detalhe.html", processo=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_processo.route('/editar/<int:id>', methods=["GET"])
def rota_processo_pagina_editar(id):
    sucesso, resultado, mensagem = processo_lista_selecionado(id)
    if not resultado:
        resultado = Processo(None).to_dict()
    return render_template("admin_processo_editar.html", processo=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_processo.route('/processos', methods=["GET"])
def rota_processo_listar_todos():
    sucesso, resultado, mensagem = processo_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_processo.route('/processo/<int:id>', methods=["GET"])
def rota_processo_listar_selecionado(id):
    sucesso, resultado, mensagem = processo_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_processo.route('/processo', methods=['POST'])
def rota_processo_salvar_novo():
    dados = request.get_json()
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    status = dados.get("status")
    
    sucesso, resultado, mensagem = processo_salvar_novo(Processo(None, nome, descricao, status))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_processo.route('/processo', methods=["PUT"])
def rota_processo_alterar_existente():
    dados = request.get_json()
    idprocesso = dados.get("id")
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    status = dados.get("status")
    
    sucesso, resultado, mensagem = processo_alterar_existente(Processo(idprocesso, nome, descricao, status))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_processo.route('/processo/<int:id>', methods=["DELETE"])
def rota_processo_excluir_existente(id):
    sucesso, resultado, mensagem = processo_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})