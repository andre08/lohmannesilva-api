# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.relatorio_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_relatorio = Blueprint('routes_web_relatorio', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_relatorio.route('/', methods=["GET"])
def rota_relatorio_principal():
    return render_template("admin_relatorio.html")

#rota para pagina visualização 
@routes_web_relatorio.route('/ver/<int:id>', methods=["GET"])
def rota_relatorio_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = relatorio_lista_selecionado(id)
    if not resultado:
        resultado = Relatorio(None).to_dict()

    return render_template("admin_relatorio_detalhe.html", relatorio=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_relatorio.route('/editar/<int:id>', methods=["GET"])
def rota_relatorio_pagina_editar(id):
    sucesso, resultado, mensagem = relatorio_lista_selecionado(id)
    if not resultado:
        resultado = Relatorio(None).to_dict()
    return render_template("admin_relatorio_editar.html", relatorio=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_relatorio.route('/relatorios', methods=["GET"])
def rota_relatorio_listar_todos():
    sucesso, resultado, mensagem = relatorio_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_relatorio.route('/relatorio/<int:id>', methods=["GET"])
def rota_relatorio_listar_selecionado(id):
    sucesso, resultado, mensagem = relatorio_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_relatorio.route('/relatorio', methods=['POST'])
def rota_relatorio_salvar_novo():
    dados = request.get_json()
    idestudo = dados.get("idestudo")
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    descricao = dados.get("descricao")
    identificacao = dados.get("identificacao")
    localizacao_container = dados.get("localizacao_container")
    dt_geracao = dados.get("dt_geracao")
    
    sucesso, resultado, mensagem = relatorio_salvar_novo(Relatorio(None, idestudo, nome, descricao, identificacao, localizacao_container, dt_geracao))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_relatorio.route('/relatorio', methods=["PUT"])
def rota_relatorio_alterar_existente():
    dados = request.get_json()
    idrelatorio = dados.get("idrelatorio")
    idestudo = dados.get("idestudo")
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    descricao = dados.get("descricao")
    identificacao = dados.get("identificacao")
    localizacao_container = dados.get("localizacao_container")
    dt_geracao = dados.get("dt_geracao")

    sucesso, resultado, mensagem = relatorio_alterar_existente(Relatorio(idrelatorio, idestudo, nome, descricao, identificacao, localizacao_container, dt_geracao))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_relatorio.route('/relatorio/<int:id>', methods=["DELETE"])
def rota_relatorio_excluir_existente(id):
    sucesso, resultado, mensagem = relatorio_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
