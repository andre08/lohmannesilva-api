# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.empresausuario_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_empresausuario = Blueprint('routes_web_empresausuario', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_empresausuario.route('/', methods=["GET"])
def rota_empresausuario_principal():
    return render_template("admin_empresausuario.html")

#rota para pagina visualização 
@routes_web_empresausuario.route('/ver/<int:id>', methods=["GET"])
def rota_empresausuario_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = empresausuario_lista_selecionado(id)
    if not resultado:
        resultado = EmpresaUsuario(None).to_dict()

    return render_template("admin_empresausuario_detalhe.html", empresausuario=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_empresausuario.route('/editar/<int:id>', methods=["GET"])
def rota_empresausuario_pagina_editar(id):
    resultado, mensagem = empresausuario_lista_selecionado(id)
    if not resultado:
        resultado = EmpresaUsuario(None).to_dict()
    return render_template("admin_empresausuario_editar.html", empresausuario=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_empresausuario.route('/empresausuario', methods=["GET"])
def rota_empresausuario_listar_todos():
    resultado, mensagem = empresausuario_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_empresausuario.route('/empresausuario/<int:id>', methods=["GET"])
def rota_empresausuario_listar_selecionado(id):
    resultado, mensagem = empresausuario_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_empresausuario.route('/empresausuario', methods=['POST'])
def rota_empresausuario_salvar_novo():
    dados = request.get_json()
    idempresa = dados.get("idusuario_ridempresaesponsavel")
    idusuario = dados.get("idusuario")
    papel = dados.get("papel")
    status = dados.get("status")
    dt_cadastro = dados.get("dt_cadastro")
    status = dados.get("status")
    
    resultado, mensagem = empresausuario_salvar_novo(EmpresaUsuario(None, idempresa, idusuario, papel, dt_cadastro, status))
    if resultado==True:
        mensagem = "Usuário da empresa salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o usuário da empresa [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_empresausuario.route('/empresausuario', methods=["PUT"])
def rota_empresausuario_alterar_existente():
    dados = request.get_json()
    idempresa_usuario  = dados.get("idempresa_usuario")
    idempresa = dados.get("idusuario_ridempresaesponsavel")
    idusuario = dados.get("idusuario")
    papel = dados.get("papel")
    status = dados.get("status")
    dt_cadastro = dados.get("dt_cadastro")
    status = dados.get("status")

    resultado, mensagem = empresausuario_alterar_existente(EmpresaUsuario(idempresa_usuario, idempresa, idusuario, papel, dt_cadastro, status))
    if resultado==True:
        mensagem = "Usuário da empresa alterada com sucesso"
    else:
        mensagem = "Erro ao alterar o usuário da empresa"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_empresausuario.route('/empresausuario/<int:id>', methods=["DELETE"])
def rota_empresausuario_excluir_existente(id):
    resultado, mensagem = empresausuario_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
