class Contato:
    """
    Classe: Contato
    Descrição: Classe utilizada para registrar o contatos do site
    """
    def __init__(self, idcontato, nome, email, telefone, mensagem, tipo, visualizado, respondido, interesse, cliente, ativo, dt_contato):
        self.idcontato = idcontato
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.mensagem = mensagem
        self.tipo = tipo
        self.visualizado = visualizado
        self.respondido = respondido
        self.interesse = interesse
        self.cliente = cliente
        self.ativo = ativo
        self.dt_contato = dt_contato

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
            usuario = cls(row["idcontato"], row["nome"], row["email"], row["telefone"], row["mensagem"], row["tipo"], row["visualizado"], row["respondido"], row["interesse"], row["cliente"], row["ativo"], row["dt_contato"])
        else:
            usuario = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        return usuario

    def to_dict(self):
        return {"idcontato": self.idcontato
                , "nome": self.nome
                , "email": self.email
                , "telefone": self.telefone
                , "mensagem": self.mensagem
                , "tipo": self.tipo
                , "visualizado": self.visualizado
                , "respondido": self.respondido
                , "interesse": self.interesse
                , "cliente": self.cliente
                , "ativo": self.ativo
                , "dt_contato": self.dt_contato}
