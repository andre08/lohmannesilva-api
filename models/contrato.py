from datetime import datetime
from util.sqlbuilder import *

class Contrato:
    """
    Classe: Contrato
    Descrição: Classe utilizada para registrar os contrato com as empresas
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "CONTRATO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idcontrato": "IDCONTRATO"
        , "idempresa": "IDEMPRESA"
        , "idusuario_responsavel": "IDUSUARIO_RESPONSAVEL"
        , "idusuario_vendedor": "IDUSUARIO_VENDEDOR_RESPONSAVEL"
        , "descricao": "DESCRICAO"
        , "status": "STATUS"
        , "dt_cadastro": "DT_CADASTRO"
        , "dt_assinatura": "DT_ASSINATURA"
        , "dt_atualizacao": "DT_ATUALIZACAO"
        , "dt_inicial_vigencia": "DT_INICIAL_VIGENCIA"
        , "dt_final_vigencia": "DT_FINAL_VIGENCIA"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idcontrato"]

    def __init__(self, idcontrato, idempresa=None, idusuario_responsavel=None, idusuario_vendedor=None, descricao=None, status=None, dt_cadastro=None, dt_assinatura=None, dt_atualizacao=None, dt_inicial_vigencia=None, dt_final_vigencia=None):
        self.idcontrato = idcontrato
        self.idempresa = idempresa
        self.idusuario_responsavel = idusuario_responsavel
        self.idusuario_vendedor = idusuario_vendedor
        self.descricao = descricao
        self.status = status
        self.dt_cadastro = dt_cadastro
        self.dt_assinatura = dt_assinatura
        self.dt_atualizacao = dt_atualizacao
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
            contato = cls(row["idcontrato"], row["idempresa"], row["idusuario_responsavel"], row["idusuario_vendedor"], row["descricao"], row["status"], row["dt_cadastro"], row["dt_assinatura"], row["dt_atualizacao"], row["dt_inicial_vigencia"], row["dt_final_vigencia"])
        else:
            contato = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        return contato

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idempresa, self.idusuario_responsavel, self.idusuario_vendedor, self.descricao, self.status, self.dt_cadastro, self.dt_assinatura, self.dt_atualizacao, self.dt_inicial_vigencia, self.dt_final_vigencia)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.idusuario_responsavel, self.idusuario_vendedor, self.descricao, self.status, self.dt_cadastro, self.dt_assinatura, self.dt_atualizacao, self.dt_inicial_vigencia, self.dt_final_vigencia, self.idcontrato)

    def to_dict(self, hieraquia=False):
        from services.usuario_service import usuario_lista_selecionado
        from services.empresa_service import empresa_lista_selecionado
        
        if self.dt_cadastro:
            dt_cadastro_formatada = datetime.strftime(self.dt_cadastro, "%d/%m/%Y %H:%M:%S") 
            dt_cadastro_formatada2 = datetime.strftime(self.dt_cadastro, "%d/%m/%Y")
        else:
            dt_cadastro_formatada = None
            dt_cadastro_formatada2 = None

        if self.dt_assinatura:
            dt_assinatura_formatada = datetime.strftime(self.dt_assinatura, "%d/%m/%Y %H:%M:%S") 
            dt_assinatura_formatada2 = datetime.strftime(self.dt_assinatura, "%d/%m/%Y")
        else:
            dt_assinatura_formatada = None
            dt_assinatura_formatada2 = None

        if self.dt_atualizacao:
            dt_atualizacao_formatada = datetime.strftime(self.dt_atualizacao, "%d/%m/%Y %H:%M:%S") 
            dt_atualizacao_formatada2 = datetime.strftime(self.dt_atualizacao, "%d/%m/%Y")
        else:
            dt_atualizacao_formatada = None
            dt_atualizacao_formatada2 = None

        if self.dt_inicial_vigencia:
            dt_inicial_vigencia_formatada = datetime.strftime(self.dt_inicial_vigencia, "%d/%m/%Y %H:%M:%S") 
            dt_inicial_vigencia_formatada2 = datetime.strftime(self.dt_inicial_vigencia, "%d/%m/%Y")
        else:
            dt_inicial_vigencia_formatada = None
            dt_inicial_vigencia_formatada2 = None

        if self.dt_final_vigencia:
            dt_final_vigencia_formatada = datetime.strftime(self.dt_final_vigencia, "%d/%m/%Y %H:%M:%S") 
            dt_final_vigencia_formatada2 = datetime.strftime(self.dt_final_vigencia, "%d/%m/%Y")
        else:
            dt_final_vigencia_formatada = None
            dt_final_vigencia_formatada2 = None

        if hieraquia:
            sucesso, usuarioResponsavel, mensagemUsuarioResponsavel = usuario_lista_selecionado(self.idusuario_responsavel)
            if not usuarioResponsavel:
                usuarioResponsavel = {}

            sucesso, usuarioVendedor, mensagemUsuarioVendedor = usuario_lista_selecionado(self.idusuario_responsavel)
            if not usuarioVendedor:
                usuarioVendedor = {}

            sucesso, empresa, mensagemEmpresa = empresa_lista_selecionado(self.idempresa)
            if not empresa:
                empresa = {}
        else:
            usuarioResponsavel = {}
            mensagemUsuarioResponsavel = ""

            usuarioVendedor = {}
            mensagemUsuarioVendedor = {}

            empresa = {}
            mensagemEmpresa = ""


        return {"idcontrato": self.idcontrato
                , "idempresa": self.idempresa
                , "empresa": empresa
                , "mensagemEmpresa": mensagemEmpresa
                , "idusuario_responsavel": self.idusuario_responsavel
                , "usuarioResponsavel": usuarioResponsavel
                , "mensagemUsuarioResponsavel": mensagemUsuarioResponsavel
                , "idusuario_vendedor": self.idusuario_vendedor
                , "usuarioVendedor": usuarioVendedor
                , "mensagemUsuarioVendedor": mensagemUsuarioVendedor
                , "descricao": self.descricao
                , "status": self.status
                , "dt_cadastro": dt_cadastro_formatada
                , "dt_cadastro2": dt_cadastro_formatada2
                , "dt_assinatura": dt_assinatura_formatada
                , "dt_assinatura2": dt_assinatura_formatada2
                , "dt_atualizacao": dt_atualizacao_formatada
                , "dt_atualizacao2": dt_atualizacao_formatada2
                , "dt_inicial_vigencia":dt_inicial_vigencia_formatada
                , "dt_inicial_vigencia2": dt_inicial_vigencia_formatada2
                , "dt_final_vigencia": dt_final_vigencia_formatada
                , "dt_final_vigencia2": dt_final_vigencia_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Contrato.__tabela_banco__, Contrato.__campos_tabela__, Contrato.__campos_chave__, "?")