from datetime import datetime
from util.sqlbuilder import *

class Atividade:
    """
    Classe: Atividade
    Descrição: Classe utilizada para registrar as atividades realizadas
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ATIVIDADE"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idatividade": "IDATIVIDADE"
        , "idusuario": "IDUSUARIO"
        , "idempresa": "IDEMPRESA"
        , "idestudo": "IDESTUDO"
        , "nome": "NOME"
        , "descricao": "DESCRICAO"
        , "observacao": "OBSERVARCAO"
        , "prioridade": "PRIORIDADE"
        , "dh_inicio": "DH_INICIO"
        , "dh_termino": "DH_TERMINO"
        , "status": "STATUS"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idatividade"]

    def __init__(self, idatividade, idusuario, idempresa, idestudo, nome, descricao, observacao, prioridade, dh_inicio, dh_termino, status):
        self.idatividade = idatividade
        self.idusuario = idusuario
        self.idempresa = idempresa
        self.idestudo = idestudo
        self.nome = nome
        self.descricao = descricao
        self.observacao = observacao
        self.prioridade = prioridade
        self.dh_inicio = dh_inicio
        self.dh_termino = dh_termino
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
            arquivo  = cls(row["idatividade"], row["idusuario"], row["idempresa"], row["idestudo"], row["nome"], row["descricao"], row["observacao"], row["prioridade"], row["dh_inicio"], row["dh_termino"], row["status"])
        else:
            arquivo = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        return arquivo

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.idempresa, self.idestudo, self.nome, self.descricao, self.observacao, self.prioridade, self.dh_inicio, self.dh_termino, self.status)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idusuario, self.idempresa, self.idestudo, self.nome, self.descricao, self.observacao, self.prioridade, self.dh_inicio, self.dh_termino, self.status, self.idatividade)

    def to_dict(self, hieraquia=False):
        from services.usuario_service import usuario_lista_selecionado
        from services.empresa_service import empresa_lista_selecionado
        from services.estudo_service import estudo_lista_selecionado

        if self.dh_inicio:
            dh_inicio_formatada = datetime.strftime(self.dh_inicio, "%d/%m/%Y %H:%M:%S") 
            dh_inicio_formatada2 = datetime.strftime(self.dh_inicio, "%d/%m/%Y")
        else:
            dh_inicio_formatada = None
            dh_inicio_formatada2 = None
        
        if self.dh_termino:
            dh_termino_formatada = datetime.strftime(self.dh_termino, "%d/%m/%Y %H:%M:%S") 
            dh_termino_formatada2 = datetime.strftime(self.dh_termino, "%d/%m/%Y")
        else:
            dh_termino_formatada = None
            dh_termino_formatada2 = None

        if hieraquia:
            sucesso, usuario, mensagemUsuario = usuario_lista_selecionado(self.idusuario)
            if not usuario:
                usuario = {}

            sucesso, empresa, mensagemEmpresa = empresa_lista_selecionado(self.idempresa)
            if not empresa:
                empresa = {}

            sucesso, estudo, mensagemEstudo = estudo_lista_selecionado(self.idestudo)
            if not estudo:
                estudo = {}
        else:
            estudo = {}
            mensagemEstudo = ""
            
        return {"idatividade": self.idatividade
                , "idusuario": self.idusuario
                , "usuario": usuario
                , "mensagemUsuario": mensagemUsuario
                , "idempresa": self.idempresa
                , "empresa": empresa
                , "mensagemEmpresa": mensagemEmpresa
                , "idestudo": self.idestudo
                , "estudo": estudo
                , "mensagemEstudo": mensagemEstudo
                , "nome": self.nome
                , "descricao": self.descricao
                , "observacao": self.observacao
                , "prioridade": self.prioridade
                , "dh_inicio": dh_inicio_formatada
                , "dh_inicio2": dh_inicio_formatada2
                , "dh_termino": dh_termino_formatada
                , "dh_termino2": dh_termino_formatada2
                , "status": self.status
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Atividade.__tabela_banco__, Atividade.__campos_tabela__, Atividade.__campos_chave__, "?")