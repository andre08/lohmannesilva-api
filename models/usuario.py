class Usuario:
    """
    Classe: Usuario
    Descrição: Classe utilizada para registrar o usuario
    """
    def __init__(self, id, nome, email, senha, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo, tipo):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.dt_ativacao = dt_ativacao
        self.desativado = desativado
        self.dt_desativado = dt_desativado
        self.dt_cadastro = dt_cadastro
        self.dt_atualizado = dt_atualizado
        self.token_ativo = token_ativo
        self.tipo = tipo

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
            usuario = cls(row["id"], row["nome"], row["email"], row["ativo"],row["dt_ativacao"], row["desativado"], row["dt_desativado"], row["dt_cadastro"], row["token_ativo"], row["tipo"])
        else:
            usuario = cls(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9])
        return usuario


    def to_dict(self):
        return {"id": self.id
                , "nome": self.nome
                , "email": self.email
                , "ativo": self.ativo
                , "dt_ativacao": self.dt_ativacao
                , "desativado": self.desativado
                , "dt_desativado": self.dt_desativado
                , "dt_cadastro": self.dt_cadastro
                , "dt_atualizado": self.dt_atualizado
                , "token_ativo": self.token_ativo
                , "tipo": self.tipo}
