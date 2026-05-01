# Importando bibliotecas
import pyodbc
from conn import Conectar
from models.historicoacesso import HistoricoAcesso

# listar todos os registros
def historio_acesso_listar_todos():
    #montando o comando SQL 
    builder = HistoricoAcesso.get_SQLBuilder()
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
                    resultado = [HistoricoAcesso.from_db(item).to_dict(False) for item in dados]
                    registrosAfetados = len(resultado)
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar os historicos de acesso [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os historicos de acesso [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os historicos de acesso [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"

    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# listar apenas um registro filtrado pela PK
def historico_acesso_lista_selecionado(idhistorico_acesso):
    #montando o comando sql 
    builder = HistoricoAcesso.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idhistorico_acesso": idhistorico_acesso})

    conexao = None
    cursor = None
    registrosAfetados = 0

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
                    resultado = HistoricoAcesso.from_db(dados).to_dict(True)
                    registrosAfetados = 1
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar o historico de acesso #{idhistorico_acesso} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar o historico de acesso #{idhistorico_acesso} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar o historico de acesso #{idhistorico_acesso} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# salva um novo registro
def historico_acesso_salvar_novo(historicoAcesso):
    
    if isinstance(historicoAcesso, HistoricoAcesso):
        #montando o comando sql 
        builder = HistoricoAcesso.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(historicoAcesso)

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
            mensagem = f"Erro ao salvar o historico de acesso [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o historico de acesso [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o historico de acesso [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados do inválido"
        resultado = None
        sucesso = False

    return sucesso, resultado, mensagem

# alterar um registro existente
def historico_acesso_alterar_existente(historicoAcesso):
    
    if isinstance(historicoAcesso, HistoricoAcesso):
        #montando o comando sql 
        builder = HistoricoAcesso.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(historicoAcesso)

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
            mensagem = f"Erro ao salvar o historico de acesso [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o historico de acesso [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o historico de acesso [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados inválido"
        resultado = None
        sucesso = False
        
    return sucesso, resultado, mensagem

# excluir um registro existente
def historico_acesso_excluir_existente(idhistorico_acesso):
    builder = HistoricoAcesso.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(HistoricoAcesso(idhistorico_acesso))

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
        mensagem = f"Erro ao excluir o historico de acesso #{idhistorico_acesso} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao excluir o historico de acesso #{idhistorico_acesso} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao excluir o historico de acesso #{idhistorico_acesso} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    return sucesso, resultado, mensagem

