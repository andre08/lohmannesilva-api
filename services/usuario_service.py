# Importando bibliotecas
from werkzeug.security import check_password_hash

from conn import Conectar
from models.usuario import Usuario


def listar_usuarios():
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, NOME, EMAIL, ATIVO, DT_ATIVACAO, DESATIVADO, DT_DESATIVADO, DT_CADASTRO, DT_ATUALIZADO, TOKEN_ATIVO FROM VW_USUARIO")
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return [Usuario(id, nome, email, None, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo) for id, nome, email, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo in dados]

def detalhe_usuario(id):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, NOME, EMAIL, ATIVO, DT_ATIVACAO, DESATIVADO, DT_DESATIVADO, DT_CADASTRO, DT_ATUALIZADO, TOKEN_ATIVO FROM VW_USUARIO WHERE IDUSUARIO = %s", (id,))
    dados = cur.fetchall()
    cur.close()
    conn.close()
    lista = [Usuario(id, nome, email, None, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo) for id, nome, email, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo in dados]
    return lista[0]

def criar_usuario(nome, email, senha):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO USUARIO (NOME, EMAIL, SENHA) VALUES (%s, %s, %s)", (nome, email, senha))
    conn.commit()
    cur.close()
    conn.close()

def alterar_usuario(id, nome, email, senha):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("UPDATE USUARIO SET NOME = %s, EMAIL = %s, SENHA = %s WHERE IDUSUARIO = %s", (nome, email, senha, id))
    conn.commit()
    cur.close()
    conn.close()

def deletar_usuario(id):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM USUARIO WHERE IDUSUARIO = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def logon_usuario(email, senha):

    id = None

    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, EMAIL, SENHA FROM USUARIO WHERE EMAIL = %s ", (email,))
    usuarios = cur.fetchall()
    
    for item in usuarios:
        if item and check_password_hash(item[2], senha):
            id = item[0]
            
    cur.close()
    conn.close()

    return detalhe_usuario(id)
