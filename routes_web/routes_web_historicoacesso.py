# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.historicoacesso_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_historicoacesso = Blueprint('routes_web_historicoacesso', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_historicoacesso.route('/', methods=["GET"])
def rota_hitoricoacesso_principal():
    return render_template("admin_historicoacesso.html")

#rota para pagina visualização 
@routes_web_historicoacesso.route('/ver/<int:id>', methods=["GET"])
def rota_hitoricoacesso_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = historico_acesso_lista_selecionado(id)
    if not resultado:
        resultado = HistoricoAcesso(None).to_dict()

    return render_template("admin_hitoricoacesso_detalhe.html", hitoricoacesso=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_historicoacesso.route('/editar/<int:id>', methods=["GET"])
def rota_hitoricoacesso_pagina_editar(id):
    resultado, mensagem = historico_acesso_lista_selecionado(id)
    if not resultado:
        resultado = HistoricoAcesso(None).to_dict()
    return render_template("admin_hitoricoacesso_editar.html", hitoricoacesso=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_historicoacesso.route('/historicosacesso', methods=["GET"])
def rota_historicoacesso_listar_todos():
    resultado, mensagem = historio_acesso_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_historicoacesso.route('/historicoacesso/<int:id>', methods=["GET"])
def rota_historicoacesso_listar_selecionado(id):
    resultado, mensagem = historico_acesso_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_historicoacesso.route('/historicoacesso', methods=['POST'])
def rota_historicoacesso_salvar_novo():
    dados = request.get_json()
    idusuario = dados.get("idusuario")
    rota = dados.get("rota")
    metodo = dados.get("metodo")
    ip = dados.get("ip")
    pathServer = dados.get("pathServer")
    fullUrl = dados.get("fullUrl")
    queryString = dados.get("queryString")
    formData = dados.get("formData")
    jsonData = dados.get("jsonData")
    dtAcesso = dados.get("dtAcesso")
    resultado, mensagem = historico_acesso_salvar_novo(HistoricoAcesso(None, idusuario, rota, metodo, ip, pathServer, fullUrl, queryString, formData, jsonData, dtAcesso))
    if resultado==True:
        mensagem = "Historico de acesso registro com sucesso"
    else:
        mensagem = f"Erro ao salvar o historico de acesso [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_historicoacesso.route('/historicoacesso', methods=["PUT"])
def rota_historicoacesso_alterar_existente():
    dados = request.get_json()
    idhistorico_acesso = dados.get("id")
    idusuario = dados.get("idusuario")
    rota = dados.get("rota")
    metodo = dados.get("metodo")
    ip = dados.get("ip")
    pathServer = dados.get("pathServer")
    fullUrl = dados.get("fullUrl")
    queryString = dados.get("queryString")
    formData = dados.get("formData")
    jsonData = dados.get("jsonData")
    dtAcesso = dados.get("dtAcesso")
    resultado, mensagem = historico_acesso_alterar_existente(HistoricoAcesso(idhistorico_acesso, idusuario, rota, metodo, ip, pathServer, fullUrl, queryString, formData, jsonData, dtAcesso))
    if resultado==True:
        mensagem = "Historico de acesso alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o historico de acesso"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_historicoacesso.route('/historicoacesso/<int:id>', methods=["DELETE"])
def rota_historicoacesso_excluir_existente(id):
    resultado, mensagem = historico_acesso_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO