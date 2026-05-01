# Importando bibliotecas
import pyodbc
from conn import Conectar
from flask import current_app
import jwt
from datetime import datetime, timedelta
from models.token import Token

# listar todos os registros
def token_listar_todos():
    #montando o comando SQL 
    builder = Token.get_SQLBuilder()
    comandoSQL = builder.build_select()

    resultado = []
    sucesso = False
    mensagem = f"Não foram localizados registros"
    try:    
        # criando conexão com o banco de dados
        with Conectar() as conexao:
            # criando cursor para buscar dados
            with conexao.cursor() as cursor:
                # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                cursor.execute(comandoSQL)
                # buscando dados
                dados = cursor.fetchall()
                # identificando a quantidade de registro retornado
                registrosAfetados = cursor.rowcount

                # verificando se tem resultado e convertando em lista de dicionario
                if dados:
                    resultado = [Token.from_db(item).to_dict(False) for item in dados]
                    registrosAfetados = len(resultado)
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar os token [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os token [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os token [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"

    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# listar apenas um registro filtrado pela PK
def token_lista_selecionado(id):
    #montando o comando sql 
    builder = Token.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idtoken": id})

    resultado = None
    sucesso = False
    mensagem = f"Não foram localizados registros"
    try:    
         # criando conexão com o banco de dados
        with Conectar() as conexao:
            # criando cursor para buscar dados
            with conexao.cursor() as cursor:
                # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                cursor.execute(comandoSQL, valoresFiltro)
                # buscando dados
                dados = cursor.fetchone()
                # identificando a quantidade de registro retornado
                registrosAfetados = cursor.rowcount

                # pegando os dados do banco e convertendo para objeto
                if dados:
                    resultado = Token.from_db(dados).to_dict(True)
                    registrosAfetados = 1
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar o token #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar o token #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar o token #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# salva um novo registro
def token_salvar_novo(token):

    token.secret_key = current_app.secret_key
    token.dt_expiracao = datetime.utcnow() + timedelta(hours=2)
    payload = {
        "sub": token.idusuario,
        "exp": token.dt_expiracao
    }
    token.token = jwt.encode(payload, current_app.secret_key, algorithm='HS256')
    token.dt_expiracao = token.dt_expiracao.strftime('%Y-%m-%d %H:%M:%S')
    
    if isinstance(token, Token):
        #montando o comando sql 
        builder = Token.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(token)

        resultado = None
        sucesso = False
        mensagem = f"Não foram localizados registros"
        try:    
            # criando conexão com o banco de dados
            with Conectar() as conexao:
                # criando cursor para buscar dados
                with conexao.cursor() as cursor:
                    # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                    cursor.execute(comandoSQL, valoresFiltro)
                    # identificando a quantidade de registro afetado pelo comando
                    registrosAfetados = cursor.rowcount
                    # gravando os dados no banco de dados
                    conexao.commit()
                    mensagem = f"Foram incluídos {registrosAfetados} registros"
                    sucesso = True
        except Exception as e:
            mensagem = f"Erro ao salvar o token [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o token [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o token [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados do inválido"
        resultado = None
        sucesso = False

    return sucesso, resultado, mensagem

# alterar um registro existente
def token_alterar_existente(token):
    
    if isinstance(token, Token):
        #montando o comando sql 
        builder = Token.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(token)

        resultado = None
        sucesso = False
        mensagem = f"Não foram localizados registros"
        try:    
            # criando conexão com o banco de dados
            with Conectar() as conexao:
                # criando cursor para buscar dados
                with conexao.cursor() as cursor:
                    # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                    cursor.execute(comandoSQL, valoresFiltro)
                    # identificando a quantidade de registro afetado pelo comando
                    registrosAfetados = cursor.rowcount
                    # gravando os dados no banco de dados
                    conexao.commit()
                    mensagem = f"Foram alterados {registrosAfetados} registros"
                    sucesso = True
        except Exception as e:
            mensagem = f"Erro ao salvar o token [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o token [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o token [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados inválido"
        resultado = None
        sucesso = False
        
    return sucesso, resultado, mensagem

# excluir um registro existente
def token_excluir_existente(id):
    builder = Token.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Token(id))

    resultado = None
    sucesso = False
    mensagem = f"Não foram localizados registros"
    try:    
        # criando conexão com o banco de dados
        with Conectar() as conexao:
            # criando cursor para buscar dados
            with conexao.cursor() as cursor:
                # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                cursor.execute(comandoSQL, valoresFiltro)
                registrosAfetados = cursor.rowcount
                # identificando a quantidade de registro afetado pelo comando
                registrosAfetados = cursor.rowcount
                # gravando os dados no banco de dados
                conexao.commit()
                mensagem = f"Foram excluídos {registrosAfetados} registros"
                sucesso = True
    except Exception as e:
        mensagem = f"Erro ao excluir o token #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao excluir o token #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao excluir o token #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    return sucesso, resultado, mensagem

def token_desabilitar_todos(id_usuario):
    try:    
        # criando conexão com o banco de dados
        with Conectar() as conexao:
            # criando cursor para buscar dados
            with conexao.cursor() as cursor:
                # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
                cursor.execute("UPDATE TOKEN SET DESATIVADO = 'S', DT_DESATIVADO = NOW() WHERE IDUSUARIO = %s AND DESATIVADO = 'N' AND DT_EXPIRACAO > UTC_TIMESTAMP() ", (id_usuario,))
                conexao.commit()
    except Exception as e:
        mensagem = f"Erro ao excluir o token #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao excluir o token #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao excluir o token #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    print(mensagem)
