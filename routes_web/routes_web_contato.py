# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from werkzeug.security import generate_password_hash

# Importando modulos
from services.contato_service import *
from util import montaNavegador

#registrando as rotas na aplicação
routes_web_contato = Blueprint('routes_web_contato', __name__)

#pagina de criação de nova conta
@routes_web_contato.route("/")
@routes_web_contato.route("/registrar_contato", methods=['GET'])
def registrar_contato():
    try:
        acao = request.args.get("tipo")
    except:
        acao = ""
    print(acao)
    return render_template('registro_contato.html', tipo=acao)

#pagina para criar uma nova conta de acesso
@routes_web_contato.route('/salvar_contato', methods=['POST'])
def salvar_contato():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    mensagem = dados.get("mensagem")
    tipo = dados.get("tipo")
    retorno = criar_contato(nome, email, telefone, mensagem, tipo)
    if retorno==True:
        mensagem = "Solicitação de contato enviado com sucesso, em breve entraremos em contato, Obrigado!"
    else:
        mensagem = "Erro ao salvar sua solicitação de contato, por favor tente novamente mais tarde"
    return jsonify({'success': retorno, 'mensagem':mensagem})

#pagina para listar os contatos
@routes_web_contato.route("/contatos")
def listar_contato():
    resultado = listar_contatos()
    return jsonify({"Contatos":resultado})
