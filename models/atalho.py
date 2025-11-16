from util.sqlbuilder import *

class Atalho:
    """
    Classe: Atalho
    Descrição: Classe utilizada para montar os atalhos salvos e acessados recentemente
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ATALHO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idatalho": "IDATALHO"
        , "idusuario": "IDUSUARIO"
        , "grupo": "GRUPO"
        , "nome": "NOME"
        , "rota": "ROTA"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idatalho"]

    def __init__(self, idatalho, idusuario, grupo, nome, rota):
        self.idatalho = idatalho
        self.idusuario = idusuario
        self.grupo = grupo
        self.nome = nome
        self.rota = rota

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
            atalho = cls(row["idatalho"], row["idusuario"], row["grupo"], row["nome"], row["rota"])
        else:
            atalho = cls(row[0], row[1], row[2], row[3], row[4])
        return atalho

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.grupo, self.nome, self.rota)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idusuario, self.grupo, self.nome, self.rota, self.idatalho)

    def to_dict(self):
        return {"idatalho": self.idatalho
                , "idusuario": self.idusuario
                , "grupo": self.grupo
                , "nome": self.nome
                , "rota": self.rota}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Atalho.__tabela_banco__, Atalho.__campos_tabela__, Atalho.__campos_chave__, "?")