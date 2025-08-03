# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request

# Importando modulos
from services.token_service import listar_token_usuario, criar_token

#registrando as rotas na aplicação
routes_web_token = Blueprint('routes_web_token', __name__)

#Pagina de login
@routes_web_token.route('/admin_token')
def admin_token():
    return render_template('admin_token.html')

