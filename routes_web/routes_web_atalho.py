# Importando bibliotecas
from flask import Blueprint, jsonify, render_template, session, request

# Importando modulos
from services.atalho_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_atalho = Blueprint('routes_web_atalho', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_atalho.route('/', methods=["GET"])
def rota_atalho_principal():
    return render_template("admin_atalho.html")

#rota para pagina visualização 
@routes_web_atalho.route('/ver/<int:id>', methods=["GET"])
def rota_atalho_pagina_detalhe(id):
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = atalho_lista_selecionado(id)
    if not resultado:
        resultado = Atalho(None).to_dict()

    return render_template("admin_atalho_detalhe.html", atalho=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_atalho.route('/editar/<int:id>', methods=["GET"])
def rota_atalho_pagina_editar(id):
    resultado, mensagem = atalho_lista_selecionado(id)
    if not resultado:
        resultado = Atalho(None).to_dict()
    grupos, mensagemGrupo = atalho_grupos_usuario(session["usuario_id"])
    return render_template("admin_atalho_editar.html", atalho=resultado, grupos=grupos, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros a partir do filtro e paginação
@routes_web_atalho.route('/pesquisa', methods=["GET"])
def rota_atalho_listar_pesquisar():
    resultado, mensagem = atalho_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar todos os registros
@routes_web_atalho.route('/atalhos', methods=["GET"])
def rota_atalho_listar_todos():
    resultado, mensagem = atalho_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_atalho.route('/atalho/<int:id>', methods=["GET"])
def rota_atalho_listar_selecionado(id):
    resultado, mensagem = atalho_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_atalho.route('/atalho', methods=['POST'])
def rota_atalho_salvar_novo():

    dados = request.get_json()
    idusuario = dados.get("idusuario")
    grupo = dados.get("grupo")
    nome = dados.get("nome")
    rota = dados.get("rota")

    resultado, mensagem = atalho_salvar_novo(Atalho(None, idusuario, grupo, nome, rota))

    if resultado==True:
        mensagem = "Atalho salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o atalho [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_atalho.route('/atalho', methods=["PUT"])
def rota_atalho_alterar_existente():
    dados = request.get_json()
    idatalho = dados.get("id")
    idusuario = dados.get("idusuario")
    grupo = dados.get("grupo")
    nome = dados.get("nome")
    rota = dados.get("rota")
    resultado, mensagem = atalho_alterar_existente(Atalho(idatalho, idusuario, grupo, nome, rota))
    if resultado==True:
        mensagem = "Atalho alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o atalho"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_atalho.route('/atalho/<int:id>', methods=["DELETE"])
def rota_atalho_excluir_existente(id):
    resultado, mensagem = atalho_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})


# ROTAS ESPECÍFICAS DO MODULO

#rota para listar um registro selecionado
@routes_web_atalho.route('/usuario/<int:id>', methods=["GET"])
def rota_atalho_listar_usuario_selecionado(id):
    resultado, mensagem = atalho_lista_usuario_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_atalho.route('/grupos/<int:id>', methods=["GET"])
def rota_atalho_listar_grupos(id):
    resultado, mensagem = atalho_grupos_usuario(id)
    if resultado:
        return jsonify({"grupo":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

