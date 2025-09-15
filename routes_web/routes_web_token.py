# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.token_service import listar_token_usuario, listar_token_usuario_paginado, criar_token, desabilitar_todos_tokens

#registrando as rotas na aplicação
routes_web_token = Blueprint('routes_web_token', __name__)

#Pagina de login
@routes_web_token.route('/admin_token')
def admin_token():
    return render_template('admin_token.html')

#Pagina de login
@routes_web_token.route('/tokens', methods=["GET"])
def lista_tokens():
    idusuario = session["usuario_id"]
    tokens = listar_token_usuario(idusuario)
    return jsonify([t.to_dict() for t in tokens])

#Lista de Token por usuario paginado
@routes_web_token.route('/tokens_paginado')
def lista_tokens_paginado():
    dados = request.get_json()
    pagina = dados.get("pagina")
    quantidade = dados.get("quantidade")

    idusuario = session["usuario_id"]
    resultado = listar_token_usuario_paginado(idusuario, pagina, quantidade)
    return jsonify(resultado)

@routes_web_token.route("/gerar_token", methods=["POST"])
def novo_token():
    dados = request.get_json()
    aceite = dados.get("aceite")
    print(aceite)
    if aceite:
        idusuario = session["usuario_id"]
        print('desabilitando')
        desabilitar_todos_tokens(idusuario)
        print('criando')
        criar_token(idusuario)
        print('pronto')
        return jsonify({'success': True, 'mensagem':'Token criado com sucesso!', 'redirect': ''})
    else:
        return jsonify({'success': True, 'mensagem':'Você deve aceitar os termos antes de continuar!', 'redirect': ''})
