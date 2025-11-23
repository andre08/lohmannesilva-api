# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.registro_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_registro = Blueprint('routes_web_registro', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_registro.route('/', methods=["GET"])
def rota_registro_principal():
    return render_template("admin_registro.html")

#rota para pagina visualização 
@routes_web_registro.route('/ver/<int:id>', methods=["GET"])
def rota_registro_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = registro_lista_selecionado(id)
    if not resultado:
        resultado = Registro(None).to_dict()

    return render_template("admin_registro_detalhe.html", registro=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_registro.route('/editar/<int:id>', methods=["GET"])
def rota_registro_pagina_editar(id):
    resultado, mensagem = registro_lista_selecionado(id)
    if not resultado:
        resultado = Registro(None).to_dict()
    return render_template("admin_registro_editar.html", registro=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_registro.route('/registros', methods=["GET"])
def rota_registro_listar_todos():
    resultado, mensagem = registro_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_registro.route('/registro/<int:id>', methods=["GET"])
def rota_registro_listar_selecionado(id):
    resultado, mensagem = registro_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_registro.route('/registro', methods=['POST'])
def rota_registro_salvar_novo():
    dados = request.get_json()
    idusuario = dados.get("idusuario")
    idtoken = dados.get("idtoken")
    modelo = dados.get("modelo")
    acao = dados.get("acao")
    dt_registro = dados.get("dt_registro")    
    resultado, mensagem = registro_salvar_novo(Registro(None, idusuario, idtoken, modelo, acao, dt_registro))
    if resultado==True:
        mensagem = "Registro salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o registro [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_registro.route('/registro', methods=["PUT"])
def rota_registro_alterar_existente():
    dados = request.get_json()
    idregistro = dados.get("idregistro")
    idusuario = dados.get("idusuario")
    idtoken = dados.get("idtoken")
    modelo = dados.get("modelo")
    acao = dados.get("acao")
    dt_registro = dados.get("dt_registro")
    resultado, mensagem = registro_alterar_existente(Registro(idregistro, idusuario, idtoken, modelo, acao, dt_registro))
    if resultado==True:
        mensagem = "Registro alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o registro"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_registro.route('/registro/<int:id>', methods=["DELETE"])
def rota_registro_excluir_existente(id):
    resultado, mensagem = registro_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})


# ROTAS ESPECÍFICAS DO MODULO