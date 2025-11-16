from util.sqlbuilder import *

class Relatorio:
    """
    Classe: Relatorio
    Descrição: Classe utilizada para registrar os Relatorio da campanha
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "REALTORIO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idrelatorio": "IDRELATORIO"
        , "idcampanha": "IDCAMPANHA"
        , "nome": "NOME"
        , "descricao": "DESCRICAO"
        , "identificacao": "IDENTIFICACAO"
        , "localizacao_container": "LOCALIZACAO_CONTAINER"
        , "dt_geracao": "DT_GERACAO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idrelatorio"]

    def __init__(self, idrelatorio, idcampanha, nome, descricao, identificacao, localizacao_container, dt_geracao):
        self.idrelatorio = idrelatorio
        self.idcampanha = idcampanha
        self.nome = nome
        self.descricao = descricao
        self.identificacao = identificacao
        self.localizacao_container = localizacao_container
        self.dt_geracao = dt_geracao

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
            arquivo  = cls(row["idrelatorio"], row["idcampanha"], row["nome"], row["descricao"], row["identificacao"], row["localizacao_container"], row["dt_geracao"])
        else:
            arquivo = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return arquivo

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idcampanha, self.nome, self.descricao, self.identificacao, self.localizacao_container, self.dt_geracao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idcampanha, self.nome, self.descricao, self.identificacao, self.localizacao_container, self.dt_geracao, self.idrelatorio)

    def to_dict(self):
        dt_geracao_formatada = self.dt_geracao.strftime("%d/%m/%Y %H:%M:%S")
        return {"idrelatorio": self.idrelatorio
                , "idcampanha": self.idcampanha
                , "nome": self.nome
                , "descricao": self.descricao
                , "identificacao": self.identificacao
                , "localizacao_container": self.localizacao_container
                , "dt_geracao": dt_geracao_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Relatorio.__tabela_banco__, Relatorio.__campos_tabela__, Relatorio.__campos_chave__, "?")