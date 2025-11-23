from util.sqlbuilder import *

class ItemFatura:
    """
    Classe: ItemFatura
    Descrição: Classe utilizada para montar a lista de ItemFatura
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ITEM_FATURA"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "iditem_fatura": "IDITEM_FATURA"
        , "idfatura": "IDFATURA"
        , "idestudo": "IDESTUDO"
        , "idplano_item": "IDPLANO_ITEM"
        , "descricao": "DESCRICAO"
        , "valor_unitario": "VALOR_UNITARIO"
        , "campanha_parceiro_growth": "CAMPANHA_PARCEIRO_GROWTH"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["iditem_fatura"]

    def __init__(self, iditem_fatura, idfatura, idestudo, idplano_item, descricao, valor_unitario, campanha_parceiro_growth):
        self.iditem_fatura = iditem_fatura
        self.idfatura = idfatura
        self.idestudo = idestudo
        self.idplano_item = idplano_item
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.campanha_parceiro_growth = campanha_parceiro_growth

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
            itemFatura = cls(row["iditem_fatura"], row["idfatura"], row["idestudo"], row["idplano_item"], row["descricao"], row["valor_unitario"], row["campanha_parceiro_growth"])
        else:
            itemFatura = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return itemFatura

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idfatura, self.idestudo, self.idplano_item, self.descricao, self.valor_unitario, self.campanha_parceiro_growth)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idfatura, self.idestudo, self.idplano_item, self.descricao, self.valor_unitario, self.campanha_parceiro_growth, self.iditem_fatura)

    def to_dict(self, hieraquia=False):
        from services.estudo_service import estudo_lista_selecionado
        from services.fatura_service import fatura_lista_selecionado
        from services.plano_service import plano_lista_selecionado

        if hieraquia:
            fatura, mensagemFatura = fatura_lista_selecionado(self.idfatura)
            if not fatura:
                fatura = {}

            estudo, mensagemEstudo = estudo_lista_selecionado(self.idestudo)
            if not estudo:
                estudo = {}

            plano, mensagemPlano = plano_lista_selecionado(self.idplano_padrao)
            if not plano:
                plano = {}
        else:
            fatura = {}
            mensagemFatura = ""

            estudo = {}
            mensagemEstudo = ""

            plano = {}
            mensagemPlano = ""

        return {"iditem_fatura": self.iditem_fatura
                , "idfatura": self.idfatura
                , "fatura":fatura
                , "mensagemFatura":mensagemFatura
                , "idestudo": self.idestudo
                , "estudo": estudo
                , "mensagemEstudo": mensagemEstudo
                , "idplano_item": self.idplano_item
                , "plano": plano
                , "mensagemPlano": mensagemPlano
                , "descricao": self.descricao
                , "valor_unitario": self.valor_unitario
                , "campanha_parceiro_growth": self.campanha_parceiro_growth}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(ItemFatura.__tabela_banco__, ItemFatura.__campos_tabela__, ItemFatura.__campos_chave__, "?")