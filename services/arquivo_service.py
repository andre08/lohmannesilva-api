# Importando bibliotecas
from conn import Conectar
from models.arquivo import Arquivo

# listar todos os registros
def arquivo_listar_todos():
    #montando o comando SQL 
    builder = Arquivo.get_SQLBuilder()
    comandoSQL = builder.build_select()

    resultado = []
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL)
        # buscando dados
        dados = cursor.fetchall()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # verificando se tem resultado e convertando em lista de dicionario
        if dados:
            resultado = [Arquivo.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os arquivos [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os arquivos [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os arquivos [ValueError: {str(e)}]"
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()

    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def arquivo_lista_selecionado(id):
    #montando o comando sql 
    builder = Arquivo.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idarquivo": id})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL, valoresFiltro)
        # buscando dados
        dados = cursor.fetchone()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = Arquivo.from_db(dados).to_dict(True)
            registrosAfetados = 1
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o arquivo #{id} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o arquivo #{id} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o arquivo #{id} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# salva um novo registro
def arquivo_salvar_novo(arquivo):
    resultado = False
    if isinstance(arquivo, Arquivo):

        #montando o comando sql 
        builder = Arquivo.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(arquivo)

        try:    
            # criando conexão com o banco de dados
            conexao = Conectar()
            # criando cursor para buscar dados
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
            mensagem = f"Erro ao salvar o arquivo [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o arquivo [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o arquivo [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados do arquivo inválido"
        resultado = False

    return resultado, mensagem

# alterar um registro existente
def arquivo_alterar_existente(arquivo):
    
    if isinstance(arquivo, Arquivo):
        #montando o comando sql 
        builder = Arquivo.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(arquivo)

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
            mensagem = f"Erro ao salvar o arquivo [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o arquivo [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o arquivo [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados de atalho inválido"
        resultado = False
        
    return resultado, mensagem

# excluir um registro existente
def arquivo_excluir_existente(id):
    builder = Arquivo.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Arquivo(id))

    resultado = False
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
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
        mensagem = f"Erro ao excluir arquivo #{id} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao excluir o arquivo #{id} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao excluir o arquivo #{id} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return resultado, mensagem
