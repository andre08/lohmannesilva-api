# Importando bibliotecas
import pyodbc
from conn import Conectar
from models.empresausuario import EmpresaUsuario

# listar todos os registros
def empresausuario_listar_todos():
    #montando o comando SQL 
    builder = EmpresaUsuario.get_SQLBuilder()
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
                    resultado = [EmpresaUsuario.from_db(item).to_dict(False) for item in dados]
                    registrosAfetados = len(resultado)
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar os usuarios da empresa [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os usuarios da empresa [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os usuarios da empresa [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"

    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# listar apenas um registro filtrado pela PK
def empresausuario_lista_selecionado(id):
    #montando o comando sql 
    builder = EmpresaUsuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idempresa_usuario": id})

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
                    resultado = EmpresaUsuario.from_db(dados).to_dict(True)
                    registrosAfetados = 1
                    # ajustando a mensagem para quando o comando foi executado com sucesso
                    mensagem = f"Foram encontrados {registrosAfetados} registros"
                    sucesso = True
    except Exception as e:
        mensagem = f"Erro ao localizar usuario da empresa #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar o usuario da empresa #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar o usuario da empresa #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    # Retornando os dados e mensagem
    return sucesso, resultado, mensagem

# salva um novo registro
def empresausuario_salvar_novo(empresausuario):
    
    if isinstance(empresausuario, EmpresaUsuario):
        #montando o comando sql 
        builder = EmpresaUsuario.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(empresausuario)

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
            mensagem = f"Erro ao salvar o usuario da empresa [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o usuario da empresa [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o usuario da empresa [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados do inválido"
        resultado = None
        sucesso = False

    return sucesso, resultado, mensagem

# alterar um registro existente
def empresausuario_alterar_existente(empresausuario):
    
    if isinstance(empresausuario, EmpresaUsuario):
        #montando o comando sql 
        builder = EmpresaUsuario.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(empresausuario)

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
            mensagem = f"Erro ao salvar o usuario da empresa [Exception: {str(e)}]"
        except TypeError as e:
            mensagem = f"Erro ao salvar o usuario da empresa [TypeError: {str(e)}]"
        except ValueError as e:
            mensagem = f"Erro ao salvar o usuario da empresa [ValueError: {str(e)}]"
        except pyodbc.Error as e:
            mensagem = f"Erro de banco de dados: {str(e)}"
    else:
        mensagem = f"Dados inválido"
        resultado = None
        sucesso = False
        
    return sucesso, resultado, mensagem

# excluir um registro existente
def empresausuario_excluir_existente(id):
    builder = EmpresaUsuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(EmpresaUsuario(id))

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
        mensagem = f"Erro ao excluir o usuario da empresa #{id} [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao excluir o usuario da empresa #{id} [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao excluir o usuario da empresa #{id} [ValueError: {str(e)}]"
    except pyodbc.Error as e:
        mensagem = f"Erro de banco de dados: {str(e)}"
    
    return sucesso, resultado, mensagem
