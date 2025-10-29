class ItemFatura:
    """
    Classe: ItemFatura
    Descrição: Classe utilizada para montar a lista de ItemFatura
    """
    def __init__(self, iditem_fatura, idfatura, idcampanha, idplano_item, descricao, valor_unitario, campanha_parceiro_growth):
        self.iditem_fatura = iditem_fatura
        self.idfatura = idfatura
        self.idcampanha = idcampanha
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
            itemFatura = cls(row["iditem_fatura"], row["idfatura"], row["idcampanha"], row["idplano_item"], row["descricao"], row["valor_unitario"], row["campanha_parceiro_growth"])
        else:
            itemFatura = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return itemFatura

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idfatura, self.idcampanha, self.idplano_item, self.descricao, self.valor_unitario, self.campanha_parceiro_growth)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idfatura, self.idcampanha, self.idplano_item, self.descricao, self.valor_unitario, self.campanha_parceiro_growth, self.iditem_fatura)

    def to_dict(self):
        return {"iditem_fatura": self.iditem_fatura
                , "idfatura": self.idfatura
                , "idcampanha": self.idcampanha
                , "idplano_item": self.idplano_item
                , "descricao": self.descricao
                , "valor_unitario": self.valor_unitario
                , "campanha_parceiro_growth": self.campanha_parceiro_growth}
