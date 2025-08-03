# Importando bibliotecas
from flask import current_app
import jwt
from datetime import datetime, timedelta

from conn import Conectar
from models.token import Token

def listar_token_usuario(id_usuario):
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT IDTOKEN, IDUSUARIO, TOKEN, SECRET_KEY, DT_CRIACAO, DT_EXPIRACAO, ATIVO FROM VW_TOKEN WHERE IDUSUARIO = ? ORDER BY IDUSUARIO, DT_EXPIRACAO", (id_usuario,))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [Token(id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo) for id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo in dados]

def detalhe_token(id):
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT IDTOKEN, IDUSUARIO, TOKEN, SECRET_KEY, DT_CRIACAO, DT_EXPIRACAO, ATIVO FROM VW_TOKEN WHERE IDTOKEN = ? ORDER BY IDUSUARIO, DT_EXPIRACAO", (id,))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [Token(id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo) for id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo in dados]

def criar_token(idusuario):
    secret_key = current_app.secret_key
    dt_expiracao = datetime.utcnow() + timedelta(hours=2)
    payload = {
        "sub": idusuario,
        "exp": dt_expiracao
    }
    token = jwt.encode(payload, current_app.secret_key, algorithm='HS256')
    data_formatada = dt_expiracao.strftime('%Y-%m-%d %H:%M:%S')

    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO TOKEN (IDUSUARIO, TOKEN, SECRET_KEY, DT_EXPIRACAO) VALUES (%s, %s, %s, %s)", (idusuario, token, secret_key, data_formatada))
    conn.commit()
    
    cur.close()
    conn.close()
