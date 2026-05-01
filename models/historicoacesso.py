from datetime import datetime
from util.sqlbuilder import *

class HistoricoAcesso:
    """
    Classe: HistoricoAcesso
    Descrição: Classe utilizada para montar a lista historica de acesso do usuario
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "HISTORICO_ACESSO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idhistorico_acesso": "IDHISTORICO_ACESSO"
        , "idusuario": "IDUSUARIO"
        , "rota": "ROTA"
        , "metodo": "METODO"
        , "ip": "IP"
        , "pathServer": "PATH_SERVER"
        , "fullUrl": "FULL_URL"
        , "queryString": "QUERY_STRING"
        , "formData": "FORM_DATA"
        , "jsonData": "JSON_DATA"
        , "dtAcesso": "DT_ACESSO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idhistorico_acesso"]

    def __init__(self, idhistorico_acesso, idusuario=None, rota=None, metodo=None, ip=None, pathServer=None, fullUrl=None, queryString=None, formData=None, jsonData=None, dtAcesso=None):
        self.idhistorico_acesso = idhistorico_acesso
        self.idusuario = idusuario
        self.rota = rota
        self.metodo = metodo
        self.ip = ip
        self.pathServer = pathServer
        self.fullUrl = fullUrl
        self.queryString = queryString
        self.formData = formData
        self.jsonData = jsonData
        self.dtAcesso = dtAcesso

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
            historicoAcesso = cls(row["IDHISTORICO_ACESSO"], row["IDUSUARIO"], row["ROTA"], row["METODO"], row["IP"], row["PATH_SERVER"], row["FULL_URL"], row["QUERY_STRING"], row["FORM_DATA"], row["JSON_DATA"], row["DT_ACESSO"])
        else:
            historicoAcesso = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        return historicoAcesso

    def to_dict(self, hieraquia=False):
        from services.usuario_service import usuario_lista_selecionado

        # formatando campos data
        if self.dtAcesso:
            dtAcesso_formatada = datetime.strftime(self.dtAcesso, "%d/%m/%Y %H:%M:%S") 
            dtAcesso_formatada2 = datetime.strftime(self.dtAcesso, "%d/%m/%Y")
        else:
            dtAcesso_formatada = None
            dtAcesso_formatada2 = None
        
        if hieraquia:
            sucesso, usuario, mensagemUsuario = usuario_lista_selecionado(self.idusuario)
            if not usuario:
                usuario = {}
        else:
            usuario = {}
            mensagemUsuario = ""

        return {"idhistorico_acesso": self.idhistorico_acesso
                , "idusuario": self.idusuario
                , "usuario": usuario
                , "usuarioMensagem": mensagemUsuario
                , "rota": self.rota
                , "metodo": self.metodo
                , "ip": self.ip
                , "pathServer": self.pathServer
                , "fullUrl": self.fullUrl
                , "queryString": self.queryString
                , "formData": self.formData
                , "jsonData": self.jsonData
                , "dtAcesso": dtAcesso_formatada
                , "dtAcesso2": dtAcesso_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(HistoricoAcesso.__tabela_banco__, HistoricoAcesso.__campos_tabela__, HistoricoAcesso.__campos_chave__, "?")