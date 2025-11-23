# Importando bibliotecas
from conn import Conectar
from models.usuario import Usuario

# Localiza o usuario a partir do email para que seja realizao o login
def usuario_logon(email):
    #montando o comando sql 
    builder = Usuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"email": email})

    try:    
        conexao = Conectar()
        cursor = conexao.cursor()
        cursor.execute(comandoSQL, valoresFiltro)
        dados = cursor.fetchone()
        registrosAfetados = cursor.rowcount

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = Usuario.from_db(dados)
        else:
            resultado = None

        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os usuários [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar os usuários [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar os usuários [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()

    return resultado, mensagem

# retorno o numero total de registros na base
def usuario_base_total():
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de Usuario
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute("SELECT COUNT(*) AS REGISTROS FROM VW_USUARIO")
        totalRegistros = cursor.fetchone()[0]

        if not totalRegistros:
            totalRegistros = 0

    except Exception as e:
        mensagem = f"Erro ao localizar a quantidade de usuário [Exception: {str(e)}]"
        totalRegistros = 0
    except TypeError as e:
        mensagem = f"Erro ao localizar a quantidade de usuário [TypeError: {str(e)}]"
        totalRegistros = 0
    except ValueError as e:
        mensagem = f"Erro ao localizar a quantidade de usuário [ValueError: {str(e)}]"
        totalRegistros = 0
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return totalRegistros

# listar todos os registros
def usuario_listar_todos():
    #montando o comando SQL 
    builder = Usuario.get_SQLBuilder()
    comandoSQL = builder.build_select()

    resultado = []
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de usuário
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL)
        # buscando dados
        dados = cursor.fetchall()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # verificando se tem resultado e convertando em lista de dicionario
        if dados:
            resultado = [Usuario.from_db(item).to_dict(False) for item in dados]
            registrosAfetados = len(resultado)

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar os usuários [Exception: {str(e)}]"
    except TypeError as e:
        mensagem = f"Erro ao localizar os usuários [TypeError: {str(e)}]"
    except ValueError as e:
        mensagem = f"Erro ao localizar os usuários [ValueError: {str(e)}]"
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# listar apenas um registro filtrado pela PK
def usuario_lista_selecionado(idusuario):
    #montando o comando sql 
    builder = Usuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values({"idusuario": idusuario})

    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de usuário
        cursor = conexao.cursor()
        # a consulta deve trazer todos os cados e na ordem de criação que deve refletir a mesma ordem da classe
        cursor.execute(comandoSQL, valoresFiltro)
        # buscando dados
        dados = cursor.fetchone()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount

        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = Usuario.from_db(dados).to_dict(True)  
            registrosAfetados = 1          
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {registrosAfetados} registros"
    except Exception as e:
        mensagem = f"Erro ao localizar o usuário #{idusuario} [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o usuário #{idusuario} [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o usuário #{idusuario} [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, mensagem

# listar registros por filtrado e paginado
def usuario_lista_filtrado_paginado(filtro, ordem="", pagina=1, quantidade=10):

    # verificando se foi informado uma ordem de pagina, caso não tenho será usada a pk
    if ordem == "" or ordem == None:
        ordem = " ,".join(Usuario.__campos_chave__)
    
    #montando o comando sql 
    builder = Usuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.select_sql_and_values(filtro)

    try:
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de usuário
        cursor = conexao.cursor()
        # inicialmente a consulta vai trazer o numero total de registro do filtro
        cursor.execute(f"SELECT COUNT(1) AS TOTAL FROM ({comandoSQL}) AS X", valoresFiltro)
        # buscando o numero de registro
        totalRegistros = int(cursor.fetchone()[0])
        totalPagina = round(totalRegistros / quantidade, 0) + 1

        # executando a consulta ordenada e paginada
        cursor.execute(f" {comandoSQL} ORDER BY {ordem} OFFSET ({pagina} - 1) * {quantidade} ROWS FETCH NEXT {quantidade} ROWS ONLY ", valoresFiltro)
        # buscando dados
        dados = cursor.fetchall()
        # identificando a quantidade de registro retornado
        registrosAfetados = cursor.rowcount
        # pegando os dados do banco e convertendo para objeto
        if dados:
            resultado = [Usuario.from_db(item).to_dict(True) for item in dados]
            registrosAfetados = len(resultado)
        else:
            resultado = None

        # ajustando a mensagem para quando o comando foi executado com sucesso
        mensagem = f"Foram encontrados {totalRegistros} registros, mostrando {pagina} com {registrosAfetados}"
    except Exception as e:
        mensagem = f"Erro ao localizar o usuário pelo filtro indicado [Exception: {str(e)}]"
        resultado = None
    except TypeError as e:
        mensagem = f"Erro ao localizar o usuário pelo filtro indicado [TypeError: {str(e)}]"
        resultado = None
    except ValueError as e:
        mensagem = f"Erro ao localizar o usuário pelo filtro indicado [ValueError: {str(e)}]"
        resultado = None
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    # Retornando os dados e mensagem
    return resultado, totalRegistros, totalPagina, mensagem

# salva um novo registro
def usuario_salvar_novo(usuario):
    resultado = False
    if isinstance(usuario, Usuario):

        #montando o comando sql 
        builder = Usuario.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.insert_sql_and_values(usuario)

        try:    
            # criando conexão com o banco de dados
            conexao = Conectar()
            # criando cursor para buscar dados de usuário
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
            mensagem = f"Erro ao salvar o usuários [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o usuários [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o usuários [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados de usuários inválido"
        resultado = False

    print(mensagem)
    return resultado, mensagem

# alterar um registro existente
def usuario_alterar_existente(usuario):
    
    if isinstance(usuario, Usuario):
        #montando o comando sql 
        builder = Usuario.get_SQLBuilder()
        comandoSQL, valoresFiltro = builder.update_sql_and_values(usuario)

        try:    
            # criando conexão com o banco de dados
            conexao = Conectar()
            # criando cursor para buscar dados de usuário
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
            mensagem = f"Erro ao salvar o usuários [Exception: {str(e)}]"
            resultado = False
        except TypeError as e:
            mensagem = f"Erro ao salvar o usuários [TypeError: {str(e)}]"
            resultado = False
        except ValueError as e:
            mensagem = f"Erro ao salvar o usuários [ValueError: {str(e)}]"
            resultado = False
        finally:
            # fechando o cursor
            cursor.close()
            # fechando conexão com o banco de dados
            conexao.close()
    else:
        mensagem = f"Dados de usuário inválido"
        resultado = False
        
    return resultado, mensagem

# excluir um registro existente
def usuario_excluir_existente(idusuario):
    builder = Usuario.get_SQLBuilder()
    comandoSQL, valoresFiltro = builder.delete_sql_and_values(Usuario(idusuario, None, None, None))

    resultado = False
    try:    
        # criando conexão com o banco de dados
        conexao = Conectar()
        # criando cursor para buscar dados de Usuario
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
        mensagem = f"Erro ao excluir o usuário #{idusuario} [Exception: {str(e)}]"
        resultado = False
    except TypeError as e:
        mensagem = f"Erro ao excluir o usuário #{idusuario} [TypeError: {str(e)}]"
        resultado = False
    except ValueError as e:
        mensagem = f"Erro ao excluir o usuário #{idusuario} [ValueError: {str(e)}]"
        resultado = False
    finally:
        # fechando o cursor
        cursor.close()
        # fechando conexão com o banco de dados
        conexao.close()
    
    return resultado, mensagem
