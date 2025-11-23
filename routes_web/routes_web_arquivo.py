# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.arquivo_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_arquivo = Blueprint('routes_web_arquivo', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_arquivo.route('/', methods=["GET"])
def rota_arquivo_principal():
    return render_template("admin_arquivo.html")

#rota para pagina visualização 
@routes_web_arquivo.route('/ver/<int:id>', methods=["GET"])
def rota_arquivo_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = arquivo_lista_selecionado(id)
    if not resultado:
        resultado = Arquivo(None).to_dict()

    return render_template("admin_arquivo_detalhe.html", arquivo=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_arquivo.route('/editar/<int:id>', methods=["GET"])
def rota_arquivo_pagina_editar(id):
    resultado, mensagem = arquivo_lista_selecionado(id)
    if not resultado:
        resultado = Arquivo(None).to_dict()
    return render_template("admin_arquivo_editar.html", arquivo=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_arquivo.route('/arquivos', methods=["GET"])
def rota_arquivo_listar_todos():
    resultado, mensagem = arquivo_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_arquivo.route('/arquivo/<int:id>', methods=["GET"])
def rota_arquivo_listar_selecionado(id):
    resultado, mensagem = arquivo_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_arquivo.route('/arquivo', methods=['POST'])
def rota_arquivo_salvar_novo():
    dados = request.get_json()
    idestudo = dados.get("idestudo")
    nome = dados.get("nome")
    decricao = dados.get("decricao")
    identificacao = dados.get("identificacao")
    localizacao_container = dados.get("localizacao_container")
    dt_importacao = dados.get("dt_importacao")
    
    resultado, mensagem = arquivo_salvar_novo(Arquivo(None, idestudo, nome, decricao, identificacao, localizacao_container, dt_importacao))
    if resultado==True:
        mensagem = "Arquivo salvo com sucesso"
    else:
        mensagem = f"Erro ao salvar o arquivo [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_arquivo.route('/arquivo', methods=["PUT"])
def rota_arquivo_alterar_existente():
    dados = request.get_json()
    idarquivo = dados.get("idarquivo")
    idestudo = dados.get("idestudo")
    nome = dados.get("nome")
    decricao = dados.get("decricao")
    identificacao = dados.get("identificacao")
    localizacao_container = dados.get("localizacao_container")
    dt_importacao = dados.get("dt_importacao")


    resultado, mensagem = arquivo_alterar_existente(Arquivo(idarquivo, idestudo, nome, decricao, identificacao, localizacao_container, dt_importacao))
    if resultado==True:
        mensagem = "Arquivo alterado com sucesso"
    else:
        mensagem = "Erro ao alterar o arquivo"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_arquivo.route('/arquivo/<int:id>', methods=["DELETE"])
def rota_arquivo_excluir_existente(id):
    resultado, mensagem = arquivo_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
