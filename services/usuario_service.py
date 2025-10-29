# Importando bibliotecas
from werkzeug.security import check_password_hash

from conn import Conectar
from models.usuario import Usuario


def listar_usuarios():
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, NOME, EMAIL, ATIVO, DT_ATIVACAO, DESATIVADO, DT_DESATIVADO, DT_CADASTRO, DT_ATUALIZADO, TOKEN_ATIVO, TIPO FROM VW_USUARIO")
    dados = cur.fetchall()
    resultado = [Usuario.from_db(item).to_dict() for item in dados]
    cur.close()
    conn.close()
    return resultado

def total_usuario():
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) AS REGISTROS FROM VW_USUARIO")
    totalRegistros = cur.fetchone()[0]
    if not totalRegistros:
        totalRegistros = 0

    cur.close()
    conn.close()
    
    return totalRegistros

def listar_usuario_paginado(quantidade, offset):
    
    conn = Conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT IDUSUARIO, NOME, EMAIL, ATIVO, DT_ATIVACAO, DESATIVADO, DT_DESATIVADO, DT_CADASTRO, DT_ATUALIZADO, TOKEN_ATIVO, TIPO FROM VW_USUARIO ORDER BY IDUSUARIO LIMIT ? OFFSET ?", (quantidade, offset))
    dados = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [Usuario(id, nome, email, None, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo, tipo) for id, nome, email, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo, tipo in dados]

def detalhe_usuario(id):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, NOME, EMAIL, ATIVO, DT_ATIVACAO, DESATIVADO, DT_DESATIVADO, DT_CADASTRO, DT_ATUALIZADO, TOKEN_ATIVO, TIPO FROM VW_USUARIO WHERE IDUSUARIO = ?", (id,))
    dados = cur.fetchall()
    cur.close()
    conn.close()
    lista = [Usuario(id, nome, email, None, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo, tipo) for id, nome, email, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo, tipo in dados]
    return lista[0]

def criar_usuario(nome, email, senha):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO USUARIO (NOME, EMAIL, SENHA) VALUES (?, ?, ?)", (nome, email, senha))
    conn.commit()
    cur.close()
    conn.close()

def alterar_usuario(id, nome, email, senha):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("UPDATE USUARIO SET NOME = ?, EMAIL = ?, SENHA = ? WHERE IDUSUARIO = ?", (nome, email, senha, id))
    conn.commit()
    cur.close()
    conn.close()
    
def alterar_usuario_admin(id, nome, email, senha, tipo, ativo, desativado):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("UPDATE USUARIO SET NOME = ?, EMAIL = ?, SENHA = ?, TIPO = ?, ATIVO = ?, DESATIVADO = ? WHERE IDUSUARIO = ?", (nome, email, senha, tipo, ativo, desativado, id))
    conn.commit()
    cur.close()
    conn.close()

def deletar_usuario(id):
    conn = Conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM USUARIO WHERE IDUSUARIO = ?", (id,))
    conn.commit()
    cur.close()
    conn.close()

def logon_usuario(email, senha):

    id = None

    conn = Conectar()
    cur = conn.cursor()
    cur.execute("SELECT IDUSUARIO, EMAIL, SENHA FROM USUARIO WHERE EMAIL = ? ", (email,))
    usuarios = cur.fetchall()
    
    for item in usuarios:
        if item and check_password_hash(item[2], senha):
            id = item[0]
            
    cur.close()
    conn.close()
    if id:
        return detalhe_usuario(id)
    else:
        return []
