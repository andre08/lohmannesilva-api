# Importando bibliotecas
from conn import Conectar
from models.contato import Contato

# listar todos os registros
def contato_listar_todos():
    #montando o comando SQL 
    builder = Contato.get_SQLBuilder()
    comandoSQL = builder.build_select()

    resultado = []
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de contato
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL)
        # buscando dados
        dados = cursor.fetchall()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # verificando se tem resultado e convertando em lista de dicionario
        if dados:
            resultado = [Contato.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os contatos [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os contatos [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os contatos [ValueError: {str(e)}]"
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def contato_lista_selecionado(idcontato):
    #montando o comando sql 
    builder = Contato.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idcontato": idcontato})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de contato
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL, valoresFiltro)
        # buscando dados
        dados = cursor.fetchone()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = Contato.from_db(dados).to_dict(True)
            registrosAfetados = 1
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o contato #{idcontato} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o contato #{idcontato} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o contato #{idcontato} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# salva um novo registro
def contato_salvar_novo(contato):
    resultado = False
    if isinstance(contato, Contato):

        #montando o comando sql 
        builder = Contato.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(contato)

        try:    
            # criando conexão com o banco de dados
            conexao = Conectar()
            # criando cursor para buscar dados de contato
            cursor = conexao.cursor()
            # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
            cursor.execute(comandoSQL, valoresFiltro)
            # identificando a quantidade de registro afetado pelo comando
            registrosAfetados = cursor.rowcount
            # gravando os dados no banco de dados
            conexao.commit()

            mensagem = f"Foram incluídos {registrosAfetados} registros"
            resultado = True
        except Exception as e:
            mensagem = f"Erro ao salvar o contato [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o contato [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o contato [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados de contato inválido"
        resultado = False

    return resultado, mensagem

# alterar um registro existente
def contato_alterar_existente(contato):
    
    if isinstance(contato, Contato):
        #montando o comando sql 
        builder = Contato.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(contato)

        try:    
            # criando conexão com o banco de dados
            conexao = Conectar()
            # criando cursor para buscar dados de contato
            cursor = conexao.cursor()
            # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
            cursor.execute(comandoSQL, valoresFiltro)
            # identificando a quantidade de registro afetado pelo comando
            registrosAfetados = cursor.rowcount
            # gravando os dados no banco de dados
            conexao.commit()

            mensagem = f"Foram alterados {registrosAfetados} registros"
            resultado = True
        except Exception as e:
            mensagem = f"Erro ao salvar o contato [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o contato [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o contato [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados de contato inválido"
        resultado = False
        
    return resultado, mensagem

# excluir um registro existente
def contato_excluir_existente(idcontato):
    builder = Contato.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Contato(idcontato, None, None, None))

    resultado = False
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de contato
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL, valoresFiltro)
        registrosAfetados = cursor.rowcount
        # identificando a quantidade de registro afetado pelo comando
        registrosAfetados = cursor.rowcount
        # gravando os dados no banco de dados
        conexao.commit()

        mensagem = f"Foram excluídos {registrosAfetados} registros"
        resultado = True
    except Exception as e:
        mensagem = f"Erro ao excluir o contato #{idcontato} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao excluir o contato #{idcontato} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao excluir o contato #{idcontato} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return resultado, mensagem
