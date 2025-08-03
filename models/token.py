class Token:
    """
    Classe: Token
    Descrição: Classe utilizada para registrar o tokem e associar ao usuario que está utilizando, bem como manter o historico de token gerado
    """
    def __init__(self, id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo):
        self.id = id
        self.idusuario = idusuario
        self.token = token
        self.secret_key = secret_key
        self.dt_criacao = dt_criacao
        self.dt_expiracao = dt_expiracao
        self.ativo = ativo

    def to_dict(self):
        return {"id": self.id
                , "idusuario": self.idusuario
                , "token": self.token
                , "secret_key": self.secret_key
                , "dt_criacao":self.dt_criacao
                , "dt_expiracao": self.dt_expiracao
                , "ativo": self.ativo}
