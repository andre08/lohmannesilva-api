# Importando bibliotecas
import pyodbc
from conn import Conectar
from models.processo import Processo

# listar todos os registros
def processo_listar_todos():
    #montando o comando SQL 
    builder = Processo.get_SQLBuilder()
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
                    resultado = [Processo.from_db(item).to_dict(False) for item in dados]
                    registrosAfetados = len(resultado)
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar os processos [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os processos [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os processos [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"

    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# listar apenas um registro filtrado pela PK
def processo_lista_selecionado(id):
    #montando o comando sql 
    builder = Processo.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idprocesso": id})

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
                    resultado = Processo.from_db(dados).to_dict(True)
                    registrosAfetados = 1
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar o processos #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar o processos #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar o processos #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# salva um novo registro
def processo_salvar_novo(processo):
    
    if isinstance(processo, Processo):
        #montando o comando sql 
        builder = Processo.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(processo)

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
            mensagem = f"Erro ao salvar o processo [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o processo [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o processo [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados do inválido"
        resultado = None
        sucesso = False

    return sucesso, resultado, mensagem

# alterar um registro existente
def processo_alterar_existente(processo):
    
    if isinstance(processo, Processo):
        #montando o comando sql 
        builder = Processo.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(processo)

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
            mensagem = f"Erro ao salvar o processo [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o processo [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o processo [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados inválido"
        resultado = None
        sucesso = False
        
    return sucesso, resultado, mensagem

# excluir um registro existente
def processo_excluir_existente(id):
    builder = Processo.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Processo(id))

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
        mensagem = f"Erro ao excluir processo #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao excluir o processo #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao excluir o processo #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    return sucesso, resultado, mensagem

