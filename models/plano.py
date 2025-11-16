from util.sqlbuilder import *

class Plano:
    """
    Classe: Plano
    Descrição: Classe utilizada para montar a lista de planos disponiveis
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "PLANO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idplano": "IDPLANO"
        , "nome": "NOME"
        , "descricao": "DESCRICAO"
        , "parceiro_growth": "PARCEIRO_GROWTH"
        , "valor": "VALOR"
        , "status": "STATUS"
        , "dt_inicial_vigencia": "DT_INICIAL_VIGENCIA"
        , "dt_final_vigencia": "DT_FINAL_VIGENCIA"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idplano"]

    def __init__(self, idplano, nome, descricao, parceiro_growth, valor, status, dt_inicial_vigencia, dt_final_vigencia):
        self.idplano = idplano
        self.nome = nome
        self.descricao = descricao
        self.parceiro_growth = parceiro_growth
        self.valor = valor
        self.status = status
        self.dt_inicial_vigencia = dt_inicial_vigencia
        self.dt_final_vigencia = dt_final_vigencia

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
            plano = cls(row["idplano"], row["nome"], row["descricao"], row["parceiro_growth"], row["valor"], row["status"], row["dt_inicial_vigencia"], row["dt_final_vigencia"])
        else:
            plano = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return plano

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.descricao, self.parceiro_growth, self.valor, self.status, self.dt_inicial_vigencia, self.dt_final_vigencia)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.descricao, self.parceiro_growth, self.valor, self.status, self.dt_inicial_vigencia, self.dt_final_vigencia, self.idplano)

    def to_dict(self):
        dt_inicial_vigencia_formatada = self.dt_inicial_vigencia.strftime("%d/%m/%Y %H:%M:%S")
        dt_final_vigencia_formatada = self.dt_final_vigencia.strftime("%d/%m/%Y %H:%M:%S")
        return {"idplano": self.idplano
                , "nome": self.nome
                , "descricao": self.descricao
                , "parceiro_growth": self.parceiro_growth
                , "valor": self.valor
                , "status": self.status
                , "dt_inicial_vigencia": dt_inicial_vigencia_formatada
                , "dt_final_vigencia": dt_final_vigencia_formatada
                , "status": self.status}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Plano.__tabela_banco__, Plano.__campos_tabela__, Plano.__campos_chave__, "?")