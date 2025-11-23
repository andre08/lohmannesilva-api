# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.fatura_service import *
from util.paginacao import montaNavegador

#registrando as rotas na aplicação
routes_web_fatura = Blueprint('routes_web_fatura', __name__)

# ROTAS PARA PAGINAS DE DADOS

#rota para pagina principal 
@routes_web_fatura.route('/', methods=["GET"])
def rota_fatura_principal():
    return render_template("admin_fatura.html")

#rota para pagina visualização 
@routes_web_fatura.route('/ver/<int:id>', methods=["GET"])
def rota_fatura_pagina_detalhe(id):
    from services.atalho_service import atalho_possui_usuario
    #nesta pagina deve ser possivel adicionar como favorito (atalho) e deve ser verificado se exite a pagina como favorito para o usuario logado
    rota = request.path
    favorito, idatalho, mensagemFavorito = atalho_possui_usuario(session["usuario_id"], rota)
    aceitaFavoritos = True

    #dados para a visualição
    resultado, mensagem = fatura_lista_selecionado(id)
    if not resultado:
        resultado = Fatura(None).to_dict()

    return render_template("admin_fatura_detalhe.html", fatura=resultado, mensagem=mensagem, aceitaFavoritos=aceitaFavoritos, favorito=favorito, rota=rota, idatalho=idatalho)

#rota para pagina de edição
@routes_web_fatura.route('/editar/<int:id>', methods=["GET"])
def rota_fatura_pagina_editar(id):
    resultado, mensagem = fatura_lista_selecionado(id)
    if not resultado:
        resultado = Fatura(None).to_dict()
    return render_template("admin_fatura_editar.html", fatura=resultado, mensagem=mensagem)

# ROTAS DO CRUD

#rota para listar todos os registros
@routes_web_fatura.route('/faturas', methods=["GET"])
def rota_fatura_listar_todos():
    resultado, mensagem = fatura_listar_todos()
    return jsonify({"dados":resultado, "mensagem":mensagem})

#rota para listar um registro selecionado
@routes_web_fatura.route('/fatura/<int:id>', methods=["GET"])
def rota_fatura_listar_selecionado(id):
    resultado, mensagem = fatura_lista_selecionado(id)
    if resultado:
        return jsonify({"dados":resultado, "mensagem":mensagem})
    else:
        return jsonify({"mensagem":mensagem})

#pagina para criar um novo registro
@routes_web_fatura.route('/fatura', methods=['POST'])
def rota_fatura_salvar_novo():
    dados = request.get_json()
    idempresa = dados.get("idempresa")
    nome = dados.get("nome")
    dt_referencia = dados.get("dt_referencia")
    valor = dados.get("valor")
    dt_vencimento = dados.get("dt_vencimento")
    valor_pago = dados.get("valor_pago")
    dt_pagamento = dados.get("dt_pagamento")
    
    resultado, mensagem = fatura_salvar_novo(Fatura(None, idempresa, nome, dt_referencia, valor, dt_vencimento, valor_pago, dt_pagamento))
    if resultado==True:
        mensagem = "Fatura salva com sucesso"
    else:
        mensagem = f"Erro ao salvar a fatura [{mensagem}]"
    return jsonify({'success': resultado, 'mensagem':mensagem})

# rota alterar um registro existente
@routes_web_fatura.route('/fatura', methods=["PUT"])
def rota_fatura_alterar_existente():
    dados = request.get_json()
    idfatura = dados.get("idfatura")
    idempresa = dados.get("idempresa")
    nome = dados.get("nome")
    dt_referencia = dados.get("dt_referencia")
    valor = dados.get("valor")
    dt_vencimento = dados.get("dt_vencimento")
    valor_pago = dados.get("valor_pago")
    dt_pagamento = dados.get("dt_pagamento")

    resultado, mensagem = fatura_alterar_existente(Fatura(idfatura, idempresa, nome, dt_referencia, valor, dt_vencimento, valor_pago, dt_pagamento))
    if resultado==True:
        mensagem = "Fatura alterada com sucesso"
    else:
        mensagem = "Erro ao alterar a fatura"
    return jsonify({'success': resultado, 'mensagem':mensagem})

#rota para excluir um registro existente
@routes_web_fatura.route('/fatura/<int:id>', methods=["DELETE"])
def rota_fatura_excluir_existente(id):
    resultado, mensagem = fatura_excluir_existente(id)
    return jsonify({'success': resultado, "mensagem":mensagem})

# ROTAS ESPECÍFICAS DO MODULO
