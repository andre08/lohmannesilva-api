from util.sqlbuilder import *
from datetime import datetime

class Token:
    """
    Classe: Token
    Descrição: Classe utilizada para registrar o tokem e associar ao usuario que está utilizando, bem como manter o historico de token gerado
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "TOKEN"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idtoken": "IDTOKEN"
        , "idusuario": "IDUSUARIO"
        , "token": "TOKEN"
        , "secret_key": "SECRET_KEY"
        , "dt_criacao": "DT_CRIACAO"
        , "dt_expiracao": "DT_EXPIRACAO"
        , "desativado": "DESATIVADO"
        , "dt_desativado": "DT_DESATIVADO"
        , "dt_atualizado": "DT_ATUALIZADO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idtoken"]

    def __init__(self, idtoken, idusuario, token, secret_key, dt_criacao, dt_expiracao, desativado, dt_desativado, dt_atualizado):
        self.idtoken = idtoken
        self.idusuario = idusuario
        self.token = token
        self.secret_key = secret_key
        self.dt_criacao = dt_criacao
        self.dt_expiracao = dt_expiracao
        self.desativado = desativado
        self.dt_desativado = dt_desativado
        self.dt_atualizado = dt_atualizado

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
            token = cls(row["idtoken"], row["idusuario"], row["token"], row["secret_key"], row["dt_criacao"], row["dt_expiracao"], row["desativado"], row["dt_desativado"], row["dt_atualizado"])
        else:
            token = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        return token

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.token, self.secret_key, self.dt_criacao, self.dt_expiracao, self.desativado, self.dt_desativado, self.dt_atualizado)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idtoken, self.idusuario, self.token, self.secret_key, self.dt_criacao, self.dt_expiracao, self.desativado, self.dt_desativado, self.dt_atualizado, self.idtoken)

    def to_dict(self):
        dt_expiracao_formatada = self.dt_expiracao.strftime("%d/%m/%Y %H:%M:%S")
        dt_criacao_formatada = self.dt_criacao.strftime("%d/%m/%Y %H:%M:%S")
        dt_atualizado_formatada = self.dt_atualizado.strftime("%d/%m/%Y %H:%M:%S")
        if self.dt_desativado:
            dt_desativado_formatada = self.dt_desativado.strftime("%d/%m/%Y %H:%M:%S")
        else:
            dt_desativado_formatada = None
        
        return {"idtoken": self.idtoken
                , "idusuario": self.idusuario
                , "token": self.token
                , "secret_key": self.secret_key
                , "dt_criacao": dt_criacao_formatada
                , "dt_expiracao": dt_expiracao_formatada
                , "desativado": self.desativado
                , "dt_desativado": dt_desativado_formatada
                , "dt_atualizado": dt_atualizado_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Token.__tabela_banco__, Token.__campos_tabela__, Token.__campos_chave__)