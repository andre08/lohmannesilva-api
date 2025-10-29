from datetime import datetime

class Token:
    """
    Classe: Token
    Descrição: Classe utilizada para registrar o tokem e associar ao usuario que está utilizando, bem como manter o historico de token gerado
    """
    def __init__(self, idtoken, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado):
        self.idtoken = idtoken
        self.idusuario = idusuario
        self.token = token
        self.secret_key = secret_key
        self.dt_criacao = dt_criacao
        self.dt_expiracao = dt_expiracao
        self.ativo = ativo
        self.desativado = desativado
        self.dt_desativado = dt_desativado

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
            token = cls(row["idtoken"], row["idusuario"], row["token"], row["secret_key"], row["dt_criacao"], row["dt_expiracao"], row["ativo"], row["desativado"], row["dt_desativado"])
        else:
            token = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        return token

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.token, self.secret_key, self.dt_criacao, self.dt_expiracao, self.ativo, self.desativado, self.dt_desativado)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idtoken, self.idusuario, self.token, self.secret_key, self.dt_criacao, self.dt_expiracao, self.ativo, self.desativado, self.dt_desativado, self.idtoken)

    def to_dict(self):
        dt_expiracao_formatada = self.dt_expiracao.strftime("%d/%m/%Y %H:%M:%S")
        dt_criacao_formatada = self.dt_criacao.strftime("%d/%m/%Y %H:%M:%S")
        if self.dt_desativado:
            dt_desativado_formatada = self.dt_desativado.strftime("%d/%m/%Y %H:%M:%S")
        else:
            dt_desativado_formatada = None
        
        return {"idtoken": self.idtoken
                , "idusuario": self.idusuario
                , "token": self.token
                , "secret_key": self.secret_key
                , "dt_criacao": dt_criacao_formatada
                , "dt_expiracao": dt_expiracao_formatada
                , "ativo": self.ativo
                , "desativado": self.desativado
                , "dt_desativado": dt_desativado_formatada}
