# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.estudo_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_estudo = Blueprint('routes_web_estudo', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_estudo.route('/', methods=["GET"])
def rota_estudo_principal():
    return render_template("admin_estudo.html")

#rota para pagina visualização 
@routes_web_estudo.route('/ver/<int:id>', methods=["GET"])
def rota_estudo_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = estudo_lista_selecionado(id)
    if not resultado:
        resultado = Estudo(None).to_dict()

    return render_template("admin_estudo_detalhe.html", estudo=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_estudo.route('/editar/<int:id>', methods=["GET"])
def rota_estudo_pagina_editar(id):
    sucesso, resultado, mensagem = estudo_lista_selecionado(id)
    if not resultado:
        resultado = Estudo(None).to_dict()
    return render_template("admin_estudo_editar.html", estudo=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_estudo.route('/estudos', methods=["GET"])
def rota_estudo_listar_todos():
    sucesso, resultado, mensagem = estudo_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_estudo.route('/estudo/<int:id>', methods=["GET"])
def rota_estudo_listar_selecionado(id):
    sucesso, resultado, mensagem = estudo_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_estudo.route('/estudo', methods=['POST'])
def rota_estudo_salvar_novo():
    dados = request.get_json()
    idempresa = dados.get("idempresa")
    idusuario_analista = dados.get("idusuario_analista")
    tipo = dados.get("tipo")
    nome = dados.get("nome")
    objetivo = dados.get("objetivo")
    meta = dados.get("meta")
    descricao = dados.get("descricao")
    status = dados.get("status")
    status_kambam = dados.get("status_kambam")
    
    sucesso, resultado, mensagem = estudo_salvar_novo(Estudo(None, idempresa, idusuario_analista, tipo, nome, objetivo, meta, descricao, status, status_kambam))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_estudo.route('/estudo', methods=["PUT"])
def rota_estudo_alterar_existente():
    dados = request.get_json()
    idestudo = dados.get("idestudo")
    idempresa = dados.get("idempresa")
    idusuario_analista = dados.get("idusuario_analista")
    tipo = dados.get("tipo")
    nome = dados.get("nome")
    objetivo = dados.get("objetivo")
    meta = dados.get("meta")
    descricao = dados.get("descricao")
    status = dados.get("status")
    status_kambam = dados.get("status_kambam")

    sucesso, resultado, mensagem = estudo_alterar_existente(Estudo(idestudo, idempresa, idusuario_analista, tipo, nome, objetivo, meta, descricao, status, status_kambam))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_estudo.route('/estudo/<int:id>', methods=["DELETE"])
def rota_estudo_excluir_existente(id):
    sucesso, resultado, mensagem = estudo_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
