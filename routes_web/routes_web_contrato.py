# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.contrato_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_contrato = Blueprint('routes_web_contrato', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_contrato.route('/', methods=["GET"])
def rota_contrato_principal():
    return render_template("admin_contrato.html")

#rota para pagina visualização 
@routes_web_contrato.route('/ver/<int:id>', methods=["GET"])
def rota_contrato_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = contrato_lista_selecionado(id)
    if not resultado:
        resultado = Contrato(None).to_dict()

    return render_template("admin_contrato_detalhe.html", contrato=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_contrato.route('/editar/<int:id>', methods=["GET"])
def rota_contrato_pagina_editar(id):
    resultado, mensagem = contrato_lista_selecionado(id)
    if not resultado:
        resultado = Contrato(None).to_dict()
    return render_template("admin_contrato_editar.html", contrato=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_contrato.route('/contratos', methods=["GET"])
def rota_contrato_listar_todos():
    resultado, mensagem = contrato_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_contrato.route('/contrato/<int:id>', methods=["GET"])
def rota_contrato_listar_selecionado(id):
    resultado, mensagem = contrato_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_contrato.route('/contrato', methods=['POST'])
def rota_contrato_salvar_novo():
    dados = request.get_json()
    idempresa = dados.get("idempresa")
    idusuario_responsavel = dados.get("idusuario_responsavel")
    idusuario_vendedor = dados.get("idusuario_vendedor")
    descricao = dados.get("descricao")
    status = dados.get("status")
    dt_cadastro = dados.get("dt_cadastro")
    dt_assinatura = dados.get("dt_assinatura")
    dt_atualizacao = dados.get("dt_atualizacao")
    dt_inicial_vigencia = dados.get("dt_inicial_vigencia")
    dt_final_vigencia = dados.get("dt_final_vigencia")
    
    resultado, mensagem = contrato_salvar_novo(Contrato(None, idempresa, idusuario_responsavel, idusuario_vendedor, descricao, status, dt_cadastro, dt_assinatura, dt_atualizacao, dt_inicial_vigencia, dt_final_vigencia))
    if resultado==True:
        mensagem = "Contrato salva com sucesso"
    else:
        mensagem = f"Erro ao salvar a contrato [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_contrato.route('/contrato', methods=["PUT"])
def rota_contrato_alterar_existente():
    dados = request.get_json()
    idcontrato = dados.get("idcontrato")
    idempresa = dados.get("idempresa")
    idusuario_responsavel = dados.get("idusuario_responsavel")
    idusuario_vendedor = dados.get("idusuario_vendedor")
    descricao = dados.get("descricao")
    status = dados.get("status")
    dt_cadastro = dados.get("dt_cadastro")
    dt_assinatura = dados.get("dt_assinatura")
    dt_atualizacao = dados.get("dt_atualizacao")
    dt_inicial_vigencia = dados.get("dt_inicial_vigencia")
    dt_final_vigencia = dados.get("dt_final_vigencia")

    resultado, mensagem = contrato_alterar_existente(Contrato(idcontrato, idempresa, idusuario_responsavel, idusuario_vendedor, descricao, status, dt_cadastro, dt_assinatura, dt_atualizacao, dt_inicial_vigencia, dt_final_vigencia))
    if resultado==True:
        mensagem = "Contrato alterada com sucesso"
    else:
        mensagem = "Erro ao alterar a contrato"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_contrato.route('/contrato/<int:id>', methods=["DELETE"])
def rota_contrato_excluir_existente(id):
    resultado, mensagem = contrato_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
