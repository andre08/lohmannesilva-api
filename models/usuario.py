from util.sqlbuilder import *
from datetime import datetime

class Usuario:
    """
    Classe: Usuario
    Descrição: Classe utilizada para registrar o usuario
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "USUARIO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idusuario": "idusuario"
        , "nome": "nome"
        , "email": "email"
        , "senha": "senha"
        , "ativo": "ativo"
        , "dt_ativacao": "dt_ativacao"
        , "desativado": "desativado"
        , "dt_desativado": "dt_desativado"
        , "dt_cadastro": "dt_cadastro"
        , "dt_atualizado": "dt_atualizado"
        , "tipo": "tipo"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idusuario"]

    def __init__(self, idusuario, nome, email, senha, ativo = None, dt_ativacao = None, desativado = None, dt_desativado = None, dt_cadastro = None, dt_atualizado = None, tipo = None):
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.dt_ativacao = dt_ativacao
        self.desativado = desativado
        self.dt_desativado = dt_desativado
        self.dt_cadastro = dt_cadastro
        self.dt_atualizado = dt_atualizado
        self.tipo = tipo

    @classmethod
    def from_db(cls, row):
        """
        Esse metodo pega a linha do curso e converte um objeto
        cls é como se fosse o self
        row é a linha do fechall ou o resultado do fechone

        Podendo ainda usar um dic ou tupla
        exemplo (dic): {"id":1, "nome":"joao"}
        exemplo (tupla): (1, "joao")
        """
        if isinstance(row, dict):
            usuario = cls(row["idusuario"], row["nome"], row["email"], row["senha"], row["ativo"], row["dt_ativacao"], row["desativado"], row["dt_desativado"], row["dt_cadastro"], row["dt_atualizado"], row["tipo"])            
        else:
            usuario = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

        return usuario

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.email, self.senha, self.ativo, self.dt_ativacao, self.desativado, self.dt_desativado, self.dt_cadastro, self.dt_atualizado, self.tipo)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.email, self.senha, self.ativo, self.dt_ativacao, self.desativado, self.dt_desativado, self.dt_cadastro, self.dt_atualizado, self.tipo, self.idusuario)

    def to_dict(self):
        if self.dt_ativacao:
            dt_ativacao_formatada = datetime.strftime(self.dt_ativacao, "%Y-%m-%d %H:%M:%S")
        else:
            dt_ativacao_formatada = None
        
        if self.dt_desativado:
            dt_desativado_formatada = datetime.strftime(self.dt_desativado, "%Y-%m-%d %H:%M:%S")
        else:
            dt_desativado_formatada = None

        if self.dt_cadastro:
            dt_cadastro_formatada = datetime.strftime(self.dt_cadastro, "%Y-%m-%d %H:%M:%S")
        else:
            dt_cadastro_formatada = None
        
        if self.dt_atualizado:
            dt_atualizado_formatada = datetime.strftime(self.dt_atualizado, "%Y-%m-%d %H:%M:%S")
        else:
            dt_atualizado_formatada = None
            
        return {
                "idusuario": self.idusuario
                , "nome": self.nome
                , "email": self.email
                , "ativo": self.ativo
                , "dt_ativacao": dt_ativacao_formatada
                , "desativado": self.desativado
                , "dt_desativado": dt_desativado_formatada
                , "dt_cadastro": dt_cadastro_formatada
                , "dt_atualizado": dt_atualizado_formatada
                , "tipo": self.tipo
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Usuario.__tabela_banco__, Usuario.__campos_tabela__, Usuario.__campos_chave__, "?")