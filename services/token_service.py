# Importando bibliotecas
from flask import current_app
import jwt
from datetime import datetime, timedelta

from conn import Conectar
from models.token import Token

def listar_token_usuario(id_usuario):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDTOKEN, IDUSUARIO, TOKEN, SECRET_KEY, DT_CRIACAO, DT_EXPIRACAO, ATIVO, DESATIVADO, DT_DESATIVADO FROM VW_TOKEN WHERE IDUSUARIO = %s ORDER BY IDUSUARIO, DT_EXPIRACAO DESC LIMIT 10", (id_usuario,))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [Token(id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado) for id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado in dados]

def listar_token_usuario_paginado(id_usuario, pagina, quantidade):
    
    offset = (pagina - 1) * quantidade
    
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) AS REGISTROS FROM VW_TOKEN WHERE IDUSUARIO = %s ", (id_usuario,))
    totalRegistros = cur.fetchone()[0]
    totalPaginas = (totalRegistros + quantidade - 1) // quantidade  # Arredonda pra cima
    
    cur.execute("SELECT IDTOKEN, IDUSUARIO, TOKEN, SECRET_KEY, DT_CRIACAO, DT_EXPIRACAO, ATIVO, DESATIVADO, DT_DESATIVADO FROM VW_TOKEN WHERE IDUSUARIO = %s ORDER BY IDUSUARIO, DT_EXPIRACAO DESC LIMIT %s OFFSET %s", (id_usuario, quantidade, offset))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    tokens = [Token(id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado) for id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado in dados]
    return {"tokens": tokens, "pagina_atual": pagina, "total_paginas": totalPaginas}

def detalhe_token(id):
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT IDTOKEN, IDUSUARIO, TOKEN, SECRET_KEY, DT_CRIACAO, DT_EXPIRACAO, ATIVO, DESATIVADO, DT_DESATIVADO FROM VW_TOKEN WHERE IDTOKEN = %s ORDER BY IDUSUARIO, DT_EXPIRACAO", (id,))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [Token(id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado) for id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado in dados]

def desabilitar_todos_tokens(id_usuario):
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("UPDATE TOKEN SET DESATIVADO = 'S', DT_DESATIVADO = NOW() WHERE IDUSUARIO = %s AND DESATIVADO = 'N' AND DT_EXPIRACAO > UTC_TIMESTAMP() ", (id_usuario,))
    conn.commit()
    
    cur.close()
    conn.close()
    
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
