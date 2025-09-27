# Importando bibliotecas
from werkzeug.security import check_password_hash
from conn import Conectar
from models.contato import Contato


def listar_contatos():
    
    try:
        # criando conexão com o banco de dados
        conn = Conectar()
        # criando cursor para buscar dados de contato
        cur = conn.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cur.execute("SELECT * FROM CONTATO")
        # buscando dados
        dados = cur.fetchall()

        # convertendo o retorno da consulta em um objeto contato e transformando em dicionario e enviando para uma lista
        resultado = [Contato.from_db(item).to_dict() for item in dados]

        # fechando o cursor
        cur.close()
        # fechando conexão com o banco de dados
        conn.close()
    except:
        resultado = None
    
    return resultado

def criar_contato(nome, email, telefone, mensagem, tipo):

    try:
        # criando conexão com o banco de dados
        conn = Conectar()
        # criando cursor para buscar dados de contato
        cur = conn.cursor()
        # enviando dados para o banco de dados
        cur.execute("INSERT INTO CONTATO (NOME, EMAIL, TELEFONE, MENSAGEM, TIPO) VALUES (?, ?, ?, ?, ?)", (nome, email, telefone, mensagem, tipo))
        # salvando transação 
        conn.commit()

        resultado = True
    except Exception as e:
        print(f"Exception : {str(e)}")
        resultado = False
    except TypeError as e:
        print(f"TypeError: {str(e)}")
        resultado = False
    except ValueError as e:
        print(f"ValueError: {str(e)}")
        resultado = False
    finally:
        # fechando o cursor
        cur.close()
        # fechando conexão com o banco de dados
        conn.close()
    
    return resultado
