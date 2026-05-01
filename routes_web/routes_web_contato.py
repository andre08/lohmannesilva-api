# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.contato_service import *
from util.paginacao import montaNavegador
from forms.contato_form import ContatoForm

#registrando as rotas na aplicação
routes_web_contato = Blueprint('routes_web_contato', __name__)

# ROTAS PARA PAGINAS DE DADOS

#pagina de criação de nova conta
@routes_web_contato.route("/registrar_contato", methods=['GET'])
def rota_contato_registrar_contato():
    form = ContatoForm()
    try:
        acao = request.args.get("tipo")
    except:
        acao = "1"
    form.tipo.data = acao
    return render_template('admin_contato/registro_contato.html', tipo=acao, form=form)

#rota para pagina principal de contato
@routes_web_contato.route('/', methods=["GET"])
def rota_contato_principal():
    return render_template("admin_contato/admin_contato.html")

#rota para pagina visualização 
@routes_web_contato.route('/ver/<int:id>', methods=["GET"])
def rota_contato_pagina_detalhe(id):
    #Obtendo as configurações dos campos para o formulario
    form = ContatoForm()

    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    sucesso, favorito, mensagemFavorito, idatalho = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    sucesso, resultado, mensagem = contato_lista_selecionado(id)
    if not resultado:
        resultado = Contato(None).to_dict()

    return render_template("admin_contato/admin_contato_detalhe.html", contato=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho, form=form)

#rota para pagina de edição
@routes_web_contato.route('/editar/<int:id>', methods=["GET"])
def rota_contato_pagina_editar(id):
    #Obtendo as configurações dos campos para o formulario
    form = ContatoForm()

    sucesso, resultado, mensagem = contato_lista_selecionado(id)
    if not resultado:
        resultado = Contato(None).to_dict()

    form.idcontato.data = resultado["idcontato"]
    form.nome.data = resultado["nome"]
    form.email.data = resultado["email"]
    form.telefone.data = resultado["telefone"]
    form.mensagem.data = resultado["mensagem"]
    form.tipo.data = resultado["tipo"]
    form.visualizado.data = resultado["visualizado"]
    form.respondido.data = resultado["respondido"]
    form.interesse.data = resultado["interesse"]
    form.cliente.data = resultado["cliente"]
    form.ativo.data = resultado["ativo"]
    form.dt_contato.data = resultado["dt_contato"]

    return render_template("admin_contato/admin_contato_editar.html", contato=resultado, mensagem=mensagem, form=form)

# ROTAS DO CRUD

#rota para listar todos os contatos
@routes_web_contato.route('/contatos', methods=["GET"])
def rota_contato_listar_todos():    
    sucesso, resultado, mensagem = contato_listar_todos()
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para listar um contato selecionado
@routes_web_contato.route('/contato/<int:id>', methods=["GET"])
def rota_contato_listar_selecionado(id):
    
    sucesso, resultado, mensagem = contato_lista_selecionado(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#pagina para criar um novo contato
@routes_web_contato.route('/contato', methods=['POST'])
def rota_contato_salvar_novo():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    mensagem = dados.get("mensagem")
    tipo = dados.get("tipo")
    
    sucesso, resultado, mensagem = contato_salvar_novo(Contato(None, nome, email, telefone, mensagem, tipo, None, None, None, None, None, None))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# rota alterar um registro existente
@routes_web_contato.route('/contato', methods=["PUT"])
def rota_contato_alterar_existente():

    dados = request.get_json()
    id = dados.get("id")
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    mensagem = dados.get("mensagem")
    tipo = dados.get("tipo")
    visualizado = dados.get("visualizado")
    respondido = dados.get("respondido")
    interesse = dados.get("interesse")
    cliente = dados.get("cliente")
    ativo = dados.get("ativo")
    dt_contato = dados.get("dt_contato")

    sucesso, resultado, mensagem = contato_alterar_existente(Contato(id, nome, email, telefone, mensagem, tipo, visualizado, respondido, interesse, cliente, ativo, dt_contato))
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

#rota para excluir um registro existente
@routes_web_contato.route('/contato/<int:id>', methods=["DELETE"])
def rota_contato_excluir_existente(id):
    sucesso, resultado, mensagem = contato_excluir_existente(id)
    return jsonify({"success":sucesso, "dados":resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
