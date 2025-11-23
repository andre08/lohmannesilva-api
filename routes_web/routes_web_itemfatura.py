# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.itemfatura_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_itemfatura = Blueprint('routes_web_itemfatura', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_itemfatura.route('/', methods=["GET"])
def rota_itemfatura_principal():
    return render_template("admin_itemfatura.html")

#rota para pagina visualização 
@routes_web_itemfatura.route('/ver/<int:id>', methods=["GET"])
def rota_itemfatura_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = itemfatura_lista_selecionado(id)
    if not resultado:
        resultado = ItemFatura(None).to_dict()

    return render_template("admin_itemfatura_detalhe.html", itemfatura=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_itemfatura.route('/editar/<int:id>', methods=["GET"])
def rota_itemfatura_pagina_editar(id):
    resultado, mensagem = itemfatura_lista_selecionado(id)
    if not resultado:
        resultado = ItemFatura(None).to_dict()
    return render_template("admin_itemfatura_editar.html", itemfatura=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_itemfatura.route('/itensfatura', methods=["GET"])
def rota_itemfatura_listar_todos():
    resultado, mensagem = itemfatura_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_itemfatura.route('/itemfatura/<int:id>', methods=["GET"])
def rota_itemfatura_listar_selecionado(id):
    resultado, mensagem = itemfatura_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_itemfatura.route('/itemfatura', methods=['POST'])
def rota_itemfatura_salvar_novo():
    dados = request.get_json()
    idfatura = dados.get("idfatura")
    idestudo = dados.get("idestudo")
    idplano_item = dados.get("idplano_item")
    descricao = dados.get("descricao")
    valor_unitario = dados.get("valor_unitario")
    campanha_parceiro_growth = dados.get("campanha_parceiro_growth")
    
    resultado, mensagem = itemfatura_salvar_novo(ItemFatura(None, idfatura, idestudo, idplano_item, descricao, valor_unitario, campanha_parceiro_growth))
    if resultado==True:
        mensagem = "Item da fatura salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o tem da fatura [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_itemfatura.route('/contrato', methods=["PUT"])
def rota_itemfatura_alterar_existente():
    dados = request.get_json()
    iditem_fatura = dados.get("iditem_fatura")
    idfatura = dados.get("idfatura")
    idestudo = dados.get("idestudo")
    idplano_item = dados.get("idplano_item")
    descricao = dados.get("descricao")
    valor_unitario = dados.get("valor_unitario")
    campanha_parceiro_growth = dados.get("campanha_parceiro_growth")

    resultado, mensagem = itemfatura_alterar_existente(ItemFatura(iditem_fatura, idfatura, idestudo, idplano_item, descricao, valor_unitario, campanha_parceiro_growth))
    if resultado==True:
        mensagem = "Item da fatura alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o item da fatura"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_itemfatura.route('/itemfatura/<int:id>', methods=["DELETE"])
def rota_itemfatura_excluir_existente(id):
    resultado, mensagem = itemfatura_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
