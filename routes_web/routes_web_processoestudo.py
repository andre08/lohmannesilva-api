# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.processoestudo_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_processoestudo = Blueprint('routes_web_processoestudo', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_processoestudo.route('/', methods=["GET"])
def rota_processoestudo_principal():
    return render_template("admin_processoestudo.html")

#rota para pagina visualização 
@routes_web_processoestudo.route('/ver/<int:id>', methods=["GET"])
def rota_processoestudo_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = processoestudo_lista_selecionado(id)
    if not resultado:
        resultado = ProcessoEstudo(None).to_dict()

    return render_template("admin_processoestudo_detalhe.html", processoestudo=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_processoestudo.route('/editar/<int:id>', methods=["GET"])
def rota_processoestudo_pagina_editar(id):
    sucesso, resultado, mensagem = processoestudo_lista_selecionado(id)
    if not resultado:
        resultado = ProcessoEstudo(None).to_dict()
    return render_template("admin_processoestudo_editar.html", processoestudo=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_processoestudo.route('/processosestudo', methods=["GET"])
def rota_processoestudo_listar_todos():
    sucesso, resultado, mensagem = processoestudo_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_processoestudo.route('/processoestudo/<int:id>', methods=["GET"])
def rota_processoestudo_listar_selecionado(id):
    sucesso, resultado, mensagem = processoestudo_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_processoestudo.route('/processoestudo', methods=['POST'])
def rota_processoestudo_salvar_novo():
    dados = request.get_json()
    idestudo = dados.get("idestudo")
    idprocesso = dados.get("idprocesso")
    idusuario_responsavel = dados.get("idusuario_responsavel")
    observacao = dados.get("observacao")
    dt_inicio_execucao = dados.get("dt_inicio_execucao")
    dt_final_execucao = dados.get("dt_final_execucao")
    
    sucesso, resultado, mensagem = processoestudo_salvar_novo(ProcessoEstudo(None, idestudo, idprocesso, idusuario_responsavel, observacao, dt_inicio_execucao, dt_final_execucao))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_processoestudo.route('/processoestudo', methods=["PUT"])
def rota_processoestudo_alterar_existente():
    dados = request.get_json()
    idprocesso_estudo = dados.get("idprocesso_estudo")
    idestudo = dados.get("idestudo")
    idprocesso = dados.get("idprocesso")
    idusuario_responsavel = dados.get("idusuario_responsavel")
    observacao = dados.get("observacao")
    dt_inicio_execucao = dados.get("dt_inicio_execucao")
    dt_final_execucao = dados.get("dt_final_execucao")

    sucesso, resultado, mensagem = processoestudo_alterar_existente(ProcessoEstudo(idprocesso_estudo, idestudo, idprocesso, idusuario_responsavel, observacao, dt_inicio_execucao, dt_final_execucao))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_processoestudo.route('/processoestudo/<int:id>', methods=["DELETE"])
def rota_processoestudo_excluir_existente(id):
    sucesso, resultado, mensagem = processoestudo_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
