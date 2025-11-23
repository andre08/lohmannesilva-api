from datetime import datetime
from util.sqlbuilder import *

class Empresa:
    """
    Classe: Empresa
    Descrição: Classe utilizada para montar a lista de empresas disponiveis
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "EMPRESA"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idempresa": "IDEMPRESA"
        , "nome": "NOME"
        , "idplano_padrao": "IDPLANO_PADRAO"
        , "dt_primeiro_contato": "DT_PRIMEIRO_CONTATO"
        , "dt_inicio_contrato": "DT_INICIO_CONTRATO"
        , "dt_final_contrato": "DT_FINAL_CONTRATO"
        , "status": "STATUS"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idempresa"]

    def __init__(self, idempresa, nome=None, idplano_padrao=None, dt_primeiro_contato=None, dt_inicio_contrato=None, dt_final_contrato=None, status=None):
        self.idempresa = idempresa
        self.nome = nome
        self.idplano_padrao = idplano_padrao
        self.dt_primeiro_contato = dt_primeiro_contato
        self.dt_inicio_contrato = dt_inicio_contrato
        self.dt_final_contrato = dt_final_contrato
        self.status = status

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
            empresa = cls(row["idempresa"], row["nome"], row["idplano_padrao"], row["dt_primeiro_contato"], row["dt_inicio_contrato"], row["dt_final_contrato"], row["status"])
        else:
            empresa = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return empresa

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.idplano_padrao, self.dt_primeiro_contato, self.dt_inicio_contrato, self.dt_final_contrato, self.status)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.idplano_padrao, self.dt_primeiro_contato, self.dt_inicio_contrato, self.dt_final_contrato, self.status, self.idempresa)

    def to_dict(self, hieraquia=False):
        from services.plano_service import plano_lista_selecionado
        
        # formatando campos data
        if self.dt_primeiro_contato:
            dt_primeiro_contato_formatada = datetime.strftime(self.dt_primeiro_contato, "%d/%m/%Y %H:%M:%S") 
            dt_primeiro_contato_formatada2 = datetime.strftime(self.dt_primeiro_contato, "%d/%m/%Y")
        else:
            dt_primeiro_contato_formatada = None
            dt_primeiro_contato_formatada2 = None        

        if self.dt_inicio_contrato:
            dt_inicio_contrato_formatada = datetime.strftime(self.dt_inicio_contrato, "%d/%m/%Y %H:%M:%S") 
            dt_inicio_contrato_formatada2 = datetime.strftime(self.dt_inicio_contrato, "%d/%m/%Y")
        else:
            dt_inicio_contrato_formatada = None
            dt_inicio_contrato_formatada2 = None        

        if self.dt_final_contrato:
            dt_final_contrato_formatada = datetime.strftime(self.dt_final_contrato, "%d/%m/%Y %H:%M:%S") 
            dt_final_contrato_formatada2 = datetime.strftime(self.dt_final_contrato, "%d/%m/%Y")
        else:
            dt_final_contrato_formatada = None
            dt_final_contrato_formatada2 = None 

        if hieraquia:
            plano, mensagemPlano = plano_lista_selecionado(self.idplano_padrao)
            if not plano:
                plano = {}
        else:
            plano = {}
            mensagemPlano = ""

        return {"idempresa": self.idempresa
                , "nome": self.nome
                , "idplano_padrao": self.idplano_padrao
                , "plano": plano
                , "plano_mensage": mensagemPlano
                , "dt_primeiro_contato": dt_primeiro_contato_formatada
                , "dt_primeiro_contato2": dt_primeiro_contato_formatada2
                , "dt_inicio_contrato": dt_inicio_contrato_formatada
                , "dt_inicio_contrato2": dt_inicio_contrato_formatada2
                , "dt_final_contrato": dt_final_contrato_formatada
                , "dt_final_contrato2": dt_final_contrato_formatada2
                , "status": self.status}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Empresa.__tabela_banco__, Empresa.__campos_tabela__, Empresa.__campos_chave__, "?")