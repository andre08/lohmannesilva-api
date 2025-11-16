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

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.nome, self.dt_referencia, self.valor, self.dt_vencimento, self.valor_pago, self.dt_pagamento, self.idfatura)

    def to_dict(self):
        dt_referencia_formatada = self.dt_referencia.strftime("%d/%m/%Y %H:%M:%S")
        dt_vencimento_formatada = self.dt_vencimento.strftime("%d/%m/%Y %H:%M:%S")
        dt_pagamento_formatada = self.dt_pagamento.strftime("%d/%m/%Y %H:%M:%S")
        return {"idfatura": self.idfatura
                , "idempresa": self.idempresa
                , "nome": self.nome
                , "dt_referencia": dt_referencia_formatada
                , "valor": self.valor
                , "dt_vencimento": dt_vencimento_formatada
                , "valor_pago": self.valor_pago
                , "dt_pagamento": dt_pagamento_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Fatura.__tabela_banco__, Fatura.__campos_tabela__, Fatura.__campos_chave__, "?")