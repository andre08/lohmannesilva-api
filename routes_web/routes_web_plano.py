# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.plano_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_plano = Blueprint('routes_web_plano', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_plano.route('/', methods=["GET"])
def rota_plano_principal():
    return render_template("admin_plano/admin_plano.html")

#rota para pagina visualização 
@routes_web_plano.route('/ver/<int:id>', methods=["GET"])
def rota_plano_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = plano_lista_selecionado(id)
    if not resultado:
        resultado = Plano(None).to_dict()

    return render_template("admin_plano_detalhe.html", plano=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_plano.route('/editar/<int:id>', methods=["GET"])
def rota_plano_pagina_editar(id):
    sucesso, resultado, mensagem = plano_lista_selecionado(id)
    if not resultado:
        resultado = Plano(None).to_dict()
    return render_template("admin_plano_editar.html", plano=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_plano.route('/planos', methods=["GET"])
def rota_plano_listar_todos():
    sucesso, resultado, mensagem = plano_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_plano.route('/plano/<int:id>', methods=["GET"])
def rota_plano_listar_selecionado(id):
    sucesso, resultado, mensagem = plano_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_plano.route('/plano', methods=['POST'])
def rota_plano_salvar_novo():
    dados = request.get_json()
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    parceiro_growth = dados.get("parceiro_growth")
    valor = dados.get("valor")
    status = dados.get("status")
    dt_inicial_vigencia = dados.get("dt_inicial_vigencia")
    dt_final_vigencia = dados.get("dt_final_vigencia")
    
    sucesso, resultado, mensagem = plano_salvar_novo(Plano(None, nome, descricao, parceiro_growth, valor, status, dt_inicial_vigencia, dt_final_vigencia))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_plano.route('/plano', methods=["PUT"])
def rota_plano_alterar_existente():
    dados = request.get_json()
    idplano = dados.get("id")
    nome = dados.get("nome")
    descricao = dados.get("descricao")
    parceiro_growth = dados.get("parceiro_growth")
    valor = dados.get("valor")
    status = dados.get("status")
    dt_inicial_vigencia = dados.get("dt_inicial_vigencia")
    dt_final_vigencia = dados.get("dt_final_vigencia")
    
    sucesso, resultado, mensagem = plano_alterar_existente(Plano(idplano, nome, descricao, parceiro_growth, valor, status, dt_inicial_vigencia, dt_final_vigencia))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_plano.route('/plano/<int:id>', methods=["DELETE"])
def rota_plano_excluir_existente(id):
    sucesso, resultado, mensagem = plano_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
