# Importando bibliotecas
from flask import Blueprint, jsonify, redirect, render_template, session, flash, url_for, request
from werkzeug.security import generate_password_hash
from flask import current_app
import jwt
from datetime import datetime, timedelta

from services.usuario_service import criar_usuario, logon_usuario, detalhe_usuario
from services.token_service import criar_token


#registrando as rotas na API
routes_api_usuario = Blueprint('routes_api_usuario', __name__)

#Pagina de login
@routes_api_usuario.route('/api/logon')
def login():
    return jsonify({"mensagem":"logon"})
