from datetime import datetime
from util.sqlbuilder import *

class Arquivo:
    """
    Classe: Arquivo
    Descrição: Classe utilizada para registrar os Arquivos dos estudos
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ARQUIVO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idarquivo": "IDARQUIVO"
        , "idestudo": "IDESTUDO"
        , "nome": "NOME"
        , "decricao": "DECRICAO"
        , "identificacao": "IDENTIFICACAO"
        , "localizacao_container": "LOCALIZACAO_CONTAINER"
        , "dt_importacao": "DT_IMPORTACAO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idarquivo"]

    def __init__(self, idarquivo, idestudo, nome, decricao, identificacao, localizacao_container, dt_importacao):
        self.idarquivo = idarquivo
        self.idestudo = idestudo
        self.nome = nome
        self.decricao = decricao
        self.identificacao = identificacao
        self.localizacao_container = localizacao_container
        self.dt_importacao = dt_importacao

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
            arquivo  = cls(row["idarquivo"], row["idestudo"], row["nome"], row["decricao"], row["identificacao"], row["localizacao_container"], row["dt_importacao"])
        else:
            arquivo = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return arquivo

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idestudo, self.nome, self.decricao, self.identificacao, self.localizacao_container, self.dt_importacao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idestudo, self.nome, self.decricao, self.identificacao, self.localizacao_container, self.dt_importacao, self.idarquivo)

    def to_dict(self, hieraquia=False):
        from services.estudo_service import estudo_lista_selecionado

        if self.dt_importacao:
            dt_importacao_formatada = datetime.strftime(self.dt_importacao, "%d/%m/%Y %H:%M:%S") 
            dt_importacao_formatada2 = datetime.strftime(self.dt_importacao, "%d/%m/%Y")
        else:
            dt_importacao_formatada = None
            dt_importacao_formatada2 = None

        if hieraquia:
            estudo, mensagemEstudo = estudo_lista_selecionado(self.idestudo)
            if not estudo:
                estudo = {}
        else:
            estudo = {}
            mensagemEstudo = ""
            
        return {"idarquivo": self.idarquivo
                , "idestudo": self.idestudo
                , "estudo": estudo
                , "mensagemEstudo": mensagemEstudo
                , "nome": self.nome
                , "decricao": self.decricao
                , "identificacao": self.identificacao
                , "localizacao_container": self.localizacao_container
                , "dt_importacao": dt_importacao_formatada
                , "dt_importacao2": dt_importacao_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Arquivo.__tabela_banco__, Arquivo.__campos_tabela__, Arquivo.__campos_chave__, "?")