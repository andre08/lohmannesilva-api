from datetime import datetime

class Token:
    """
    Classe: Token
    Descrição: Classe utilizada para registrar o tokem e associar ao usuario que está utilizando, bem como manter o historico de token gerado
    """
    def __init__(self, id, idusuario, token, secret_key, dt_criacao, dt_expiracao, ativo, desativado, dt_desativado):
        self.id = id
        self.idusuario = idusuario
        self.token = token
        self.secret_key = secret_key
        self.dt_criacao = dt_criacao
        self.dt_expiracao = dt_expiracao
        self.ativo = ativo
        self.desativado = desativado
        self.dt_desativado = dt_desativado

    def to_dict(self):
        dt_expiracao_formatada = self.dt_expiracao.strftime("%d/%m/%Y %H:%M:%S")
        dt_criacao_formatada = self.dt_criacao.strftime("%d/%m/%Y %H:%M:%S")
        if self.dt_desativado:
            dt_desativado_formatada = self.dt_desativado.strftime("%d/%m/%Y %H:%M:%S")
        else:
            dt_desativado_formatada = None
        
        return {"id": self.id
                , "idusuario": self.idusuario
                , "token": self.token
                , "secret_key": self.secret_key
                , "dt_criacao": dt_criacao_formatada
                , "dt_expiracao": dt_expiracao_formatada
                , "ativo": self.ativo
                , "desativado": self.desativado
                , "dt_desativado": dt_desativado_formatada}
