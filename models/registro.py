class Registro:
    """
    Classe: Registro
    Descrição: Classe utilizada para registrar o log de acesso ao programa, deve registrar cada acesso e o token utilizado para acesso
    """
    def __init__(self, id, idusuario, idtoken, modelo, acao, dt_criacao):
        self.id = id
        self.idusuario = idusuario
        self.idtoken = idtoken
        self.modelo = modelo
        self.acao = acao
        self.dt_criacao = dt_criacao

    def to_dict(self):
        return {"id": self.id
                , "idusuario": self.idusuario
                , "idtoken": self.idtoken
                , "modelo": self.modelo
                , "acao": self.acao
                , "dt_criacao":self.dt_criacao}
