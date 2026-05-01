from datetime import datetime
from util.sqlbuilder import *

class ProcessoEstudo:
    """
    Classe: ProcessoEstudo
    Descrição: Classe utilizada para relacionar os processos de estudos
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "PROCESSO_ESTUDO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idprocesso_estudo": "IDPROCESSO_ESTUDO"
        , "idestudo": "IDESTUDO"
        , "idprocesso": "IDPROCESSO"
        , "idusuario_responsavel": "IDUSUARIO_RESPONSAVEL"
        , "observacao": "OBSERVACAO"
        , "dt_inicio_execucao": "DT_INICIO_EXECUCAO"
        , "dt_final_execucao": "DT_FINAL_EXECUCAO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idprocesso_estudo"]

    def __init__(self, idprocesso_estudo, idestudo, idprocesso, idusuario_responsavel, observacao, dt_inicio_execucao, dt_final_execucao):
        self.idprocesso_campanha = idprocesso_estudo
        self.idestudo = idestudo
        self.idprocesso = idprocesso
        self.observacao = observacao
        self.idusuario_responsavel = idusuario_responsavel
        self.dt_inicio_execucao = dt_inicio_execucao
        self.dt_final_execucao = dt_final_execucao

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
            processoCampanha  = cls(row["idprocesso_estudo"],row["idestudo"],row["idprocesso"],row["idusuario_responsavel"], row["observacao"],row["dt_inicio_execucao"],row["dt_final_execucao"])
        else:
            processoCampanha  = cls(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        return processoCampanha

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idestudo, self.idprocesso, self.idusuario_responsavel, self.observacao, self.dt_inicio_execucao, self.dt_final_execucao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idestudo, self.idprocesso, self.idusuario_responsavel, self.observacao, self.dt_inicio_execucao, self.dt_final_execucao, self.idprocesso_estudo)

    def to_dict(self, hieraquia=False):
        from services.estudo_service import estudo_lista_selecionado
        from services.processo_service import processo_lista_selecionado
        from services.usuario_service import usuario_lista_selecionado

        if self.dt_inicio_execucao:
            dt_inicio_execucao_formatada = datetime.strftime(self.dt_inicio_execucao, "%d/%m/%Y %H:%M:%S") 
            dt_inicio_execucao_formatada2 = datetime.strftime(self.dt_inicio_execucao, "%d/%m/%Y")
        else:
            dt_inicio_execucao_formatada = None
            dt_inicio_execucao_formatada2 = None 

        if self.dt_final_execucao:
            dt_final_execucao_formatada = datetime.strftime(self.dt_final_execucao, "%d/%m/%Y %H:%M:%S") 
            dt_final_execucao_formatada2 = datetime.strftime(self.dt_iniciodt_final_execucao_execucao, "%d/%m/%Y")
        else:
            dt_final_execucao_formatada = None
            dt_final_execucao_formatada2 = None 

        if hieraquia:
            sucesso, estudo, mensagemEstudo = estudo_lista_selecionado(self.idestudo)
            if not estudo:
                estudo = {}

            sucesso, processso, mensagemProcesso = processo_lista_selecionado(self.idprocesso)
            if not estudo:
                estudo = {}

            sucesso, usuario, mensagemUsuario = usuario_lista_selecionado(self.idusuario_responsavel)
            if not estudo:
                estudo = {}
        else:
            estudo = {}
            mensagemEstudo = ""

            processso = {}
            mensagemProcesso = ""

            usuario = {}
            mensagemUsuario = ""

        return {"idprocesso_estudo": self.idprocesso_estudo
                , "idestudo": self.idestudo
                , "estudo": estudo
                , "mensagemEstudo": mensagemEstudo
                , "idprocesso": self.idprocesso
                , "processso": processso
                , "mensagemProcesso": mensagemProcesso
                , "idusuario_responsavel": self.idusuario_responsavel
                , "usuario": usuario
                , "mensagemUsuario": mensagemUsuario
                , "observacao": self.observacao
                , "dt_inicio_execucao": dt_inicio_execucao_formatada
                , "dt_inicio_execucao2": dt_inicio_execucao_formatada2
                , "dt_final_execucao": dt_final_execucao_formatada
                , "dt_final_execucao2": dt_final_execucao_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(ProcessoEstudo.__tabela_banco__, ProcessoEstudo.__campos_tabela__, ProcessoEstudo.__campos_chave__, "?")