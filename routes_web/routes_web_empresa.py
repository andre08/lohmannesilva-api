# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.empresa_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_empresa = Blueprint('routes_web_empresa', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_empresa.route('/', methods=["GET"])
def rota_empresa_principal():
    return render_template("admin_empresa/admin_empresa.html")

#rota para pagina visualização 
@routes_web_empresa.route('/ver/<int:id>', methods=["GET"])
def rota_empresa_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = empresa_lista_selecionado(id)
    if not resultado:
        resultado = Empresa(None).to_dict()

    return render_template("admin_empresa_detalhe.html", empresa=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_empresa.route('/editar/<int:id>', methods=["GET"])
def rota_empresa_pagina_editar(id):
    sucesso, resultado, mensagem = empresa_lista_selecionado(id)
    if not resultado:
        resultado = Empresa(None).to_dict()
    return render_template("admin_empresa_editar.html", empresa=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_empresa.route('/empresas', methods=["GET"])
def rota_empresa_listar_todos():
    sucesso, resultado, mensagem = empresa_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_empresa.route('/empresa/<int:id>', methods=["GET"])
def rota_empresa_listar_selecionado(id):
    sucesso, resultado, mensagem = empresa_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_empresa.route('/empresa', methods=['POST'])
def rota_empresa_salvar_novo():
    dados = request.get_json()
    nome = dados.get("nome")
    idplano = dados.get("idplano")
    dt_primeiro_contrato = dados.get("dt_primeiro_contrato")
    dt_inicio_contrato = dados.get("dt_inicio_contrato")
    dt_final_contrato = dados.get("dt_final_contrato")
    
    sucesso, resultado, mensagem = empresa_salvar_novo(Empresa(None, nome, idplano, dt_primeiro_contrato, dt_inicio_contrato, dt_final_contrato))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_empresa.route('/empresa', methods=["PUT"])
def rota_empresa_alterar_existente():
    dados = request.get_json()
    idempresa = dados.get("id")
    nome = dados.get("nome")
    idplano = dados.get("idplano")
    dt_primeiro_contrato = dados.get("dt_primeiro_contrato")
    dt_inicio_contrato = dados.get("dt_inicio_contrato")
    dt_final_contrato = dados.get("dt_final_contrato")
    
    sucesso, resultado, mensagem = empresa_alterar_existente(Empresa(idempresa, nome, idplano, dt_primeiro_contrato, dt_inicio_contrato, dt_final_contrato))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_empresa.route('/empresa/<int:id>', methods=["DELETE"])
def rota_empresa_excluir_existente(id):
    sucesso, resultado, mensagem = empresa_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})


# ROTAS ESPECÍFICAS DO MODULO