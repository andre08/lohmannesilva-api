# Importando bibliotecas
from conn import Conectar
from models.atalho import Atalho

# listar todos os registros
def atalho_listar_todos():
    #montando o comando SQL 
    builder = Atalho.get_SQLBuilder()
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
            resultado = [Atalho.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os atalhos [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os atalhos [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os atalhos [ValueError: {str(e)}]"
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()

    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def atalho_lista_selecionado(id):
    #montando o comando sql 
    builder = Atalho.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idatalho": id})

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
            resultado = Atalho.from_db(dados).to_dict(True)
            registrosAfetados = 1
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o atalho #{id} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o atalho #{id} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o atalho #{id} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def atalho_lista_usuario_selecionado(idusuario):
    #montando o comando sql 
    builder = Atalho.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idusuario": idusuario})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(f" {comandoSQL} ORDER BY GRUPO, NOME" , valoresFiltro)
        # buscando dados
        dados = cursor.fetchall()
        registrosAfetados = cursor.rowcount

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = [Atalho.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# salva um novo registro
def atalho_salvar_novo(atalho):
    resultado = False
    if isinstance(atalho, Atalho):

        #montando o comando sql 
        builder = Atalho.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(atalho)

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
            mensagem = f"Erro ao salvar o atalho [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o atalho [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o atalho [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados do atalho inválido"
        resultado = False

    return resultado, mensagem

# alterar um registro existente
def atalho_alterar_existente(atalho):
    
    if isinstance(atalho, Atalho):
        #montando o comando sql 
        builder = Atalho.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(atalho)

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
            mensagem = f"Erro ao salvar o atalho [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o atalho [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o atalho [ValueError: {str(e)}]"
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
def atalho_excluir_existente(id):
    builder = Atalho.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Atalho(id))

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
        mensagem = f"Erro ao excluir atalho #{id} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao excluir o atalho #{id} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao excluir o atalho #{id} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def atalho_possui_usuario(idusuario, rota=None):
    #montando o comando sql 
    builder = Atalho.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idusuario": idusuario, "rota":rota})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(f" SELECT COUNT(IDATALHO) AS QTDE, MAX(IDATALHO) AS IDATALHO FROM ({comandoSQL} ) AS b" , valoresFiltro)
        # buscando dados
        dados = cursor.fetchone()

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = dados[0] >= 1 
            registrosAfetados = dados[0]
            idatalho = dados[1]
        else:
            resultado = False
            idatalho = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [Exception: {str(e)}]"
        resultado = False
        idatalho = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [TypeError: {str(e)}]"
        resultado = False
        idatalho = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o atalho do usuario #{idusuario} [ValueError: {str(e)}]"
        resultado = False
        idatalho = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, idatalho, mensagem

# listar apenas os grupos de atalho do usuario
def atalho_grupos_usuario(idusuario):
    #montando o comando sql 
    builder = Atalho.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idusuario": idusuario})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(f" SELECT GRUPO, COUNT(IDATALHO) AS QTDE FROM ({comandoSQL} ) AS B GROUP BY GRUPO" , valoresFiltro)
        # buscando dados
        dados = cursor.fetchall()

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = [{"grupo":item[0],"quantidade":item[1]} for item in dados]
            registrosAfetados = len(resultado)
        else:
            resultado = False

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o grupo de atalho do usuario #{idusuario} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao localizar o grupo de atalho do usuario #{idusuario} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao localizar o grupo de atalho do usuario #{idusuario} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem