from datetime import datetime
from util.sqlbuilder import *

class Fatura:
    """
    Classe: Fatura
    Descrição: Classe utilizada para montar a lista de Fatura
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ITEM_FATURA"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idfatura": "IDFATURA"
        , "idempresa": "IDEMPRESA"
        , "nome": "NOME"
        , "dt_referencia": "DT_REFERENCIA"
        , "valor": "VALOR"
        , "dt_vencimento": "DT_VENCIMENTO"
        , "valor_pago": "VALOR_PAGO"
        , "dt_pagamento": "DT_PAGAMENTO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idfatura"]

    def __init__(self, idfatura, idempresa, nome, dt_referencia, valor, dt_vencimento, valor_pago, dt_pagamento):
        self.idfatura = idfatura
        self.idempresa = idempresa
        self.nome = nome
        self.dt_referencia = dt_referencia
        self.valor = valor
        self.dt_vencimento = dt_vencimento
        self.valor_pago = valor_pago
        self.dt_pagamento = dt_pagamento

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
            fatura = cls(row["idfatura"], row["idempresa"], row["nome"], row["dt_referencia"], row["valor"], row["dt_vencimento"], row["valor_pago"], row["dt_pagamento"])
        else:
            fatura = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return fatura

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idempresa, self.nome, self.dt_referencia, self.valor, self.dt_vencimento, self.valor_pago, self.dt_pagamento)

    def to_update_db(self, hieraquia=False):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.nome, self.dt_referencia, self.valor, self.dt_vencimento, self.valor_pago, self.dt_pagamento, self.idfatura)

    def to_dict(self, hieraquia=False):
        from services.empresa_service import empresa_lista_selecionado
        
        # formatando campos data
        if self.dt_referencia:
            dt_referencia_formatada = datetime.strftime(self.dt_referencia, "%d/%m/%Y %H:%M:%S") 
            dt_referencia_formatada2 = datetime.strftime(self.dt_referencia, "%d/%m/%Y")
        else:
            dt_referencia_formatada = None
            dt_referencia_formatada2 = None  

        if self.dt_vencimento:
            dt_vencimento_formatada = datetime.strftime(self.dt_vencimento, "%d/%m/%Y %H:%M:%S") 
            dt_vencimento_formatada2 = datetime.strftime(self.dt_vencimento, "%d/%m/%Y")
        else:
            dt_vencimento_formatada = None
            dt_vencimento_formatada2 = None

        if self.dt_pagamento:
            dt_pagamento_formatada = datetime.strftime(self.dt_pagamento, "%d/%m/%Y %H:%M:%S") 
            dt_pagamento_formatada2 = datetime.strftime(self.dt_pagamento, "%d/%m/%Y")
        else:
            dt_pagamento_formatada = None
            dt_pagamento_formatada2 = None  

        if hieraquia:
            sucesso, empresa, mensagemEmpresa = empresa_lista_selecionado(self.idempresa)
            if not empresa:
                empresa = {}
        else:
            empresa = {}
            mensagemEmpresa = ""

        return {"idfatura": self.idfatura
                , "idempresa": self.idempresa
                , "empresa": empresa
                , "mensagemEmpresa": mensagemEmpresa
                , "nome": self.nome
                , "dt_referencia": dt_referencia_formatada
                , "dt_referencia2": dt_referencia_formatada2
                , "valor": self.valor
                , "dt_vencimento": dt_vencimento_formatada
                , "dt_vencimento2": dt_vencimento_formatada2
                , "valor_pago": self.valor_pago
                , "dt_pagamento": dt_pagamento_formatada
                , "dt_pagamento2": dt_pagamento_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Fatura.__tabela_banco__, Fatura.__campos_tabela__, Fatura.__campos_chave__, "?")