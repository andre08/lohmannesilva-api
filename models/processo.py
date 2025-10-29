class Processo:
    """
    Classe: Processo
    Descrição: Classe utilizada para montar a lista de processo disponiveis
    """
    def __init__(self, idprocesso, nome, descricao, status):
        self.idprocesso = idprocesso
        self.nome = nome
        self.descricao = descricao
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
            processo = cls(row["idprocesso"], row["nome"], row["descricao"], row["status"])
        else:
            processo = cls(row[0], row[1], row[2], row[3])
        return processo

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.descricao, self.status)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.descricao, self.status, self.idprocesso)

    def to_dict(self):
        return {"idprocesso": self.idprocesso
                , "nome": self.nome
                , "descricao": self.descricao
                , "status": self.status}
