# Importando bibliotecas
from conn import Conectar
from models.itemfatura import ItemFatura

# listar todos os registros
def itemfatura_listar_todos():
    #montando o comando SQL 
    builder = ItemFatura.get_SQLBuilder()
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
            resultado = [ItemFatura.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os itens da fatura [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os itens da fatura [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os itens da fatura [ValueError: {str(e)}]"
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()

    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def itemfatura_lista_selecionado(id):
    #montando o comando sql 
    builder = ItemFatura.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"iditem_fatura": id})

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
            resultado = ItemFatura.from_db(dados).to_dict(True)
            registrosAfetados = 1
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o item da fatura #{id} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o item da fatura #{id} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o item da fatura #{id} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# salva um novo registro
def itemfatura_salvar_novo(itemfatura):
    resultado = False
    if isinstance(itemfatura, ItemFatura):

        #montando o comando sql 
        builder = ItemFatura.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(itemfatura)

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
            mensagem = f"Erro ao salvar o item da fatura [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o item da fatura [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o item da fatura [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados do item da fatura inválido"
        resultado = False

    return resultado, mensagem

# alterar um registro existente
def itemfatura_alterar_existente(itemfatura):
    
    if isinstance(itemfatura, ItemFatura):
        #montando o comando sql 
        builder = ItemFatura.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(itemfatura)

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
            mensagem = f"Erro ao salvar o item da fatura [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o item da fatura [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o item da fatura [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados do item da fatura inválido"
        resultado = False
        
    return resultado, mensagem

# excluir um registro existente
def itemfatura_excluir_existente(id):
    builder = ItemFatura.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(ItemFatura(id))

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
        mensagem = f"Erro ao excluir o item da fatura #{id} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao excluir o item da fatura #{id} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao excluir o item da fatura #{id} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return resultado, mensagem
