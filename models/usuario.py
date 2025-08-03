class Usuario:
    """
    Classe: Usuario
    Descrição: Classe utilizada para registrar o usuario
    """
    def __init__(self, id, nome, email, senha, ativo, dt_ativacao, desativado, dt_desativado, dt_cadastro, dt_atualizado, token_ativo):
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

    def to_dict(self):
        return {"id": self.id
                , "nome": self.nome
                , "email": self.email
                , "ativo":self.ativo
                , "dt_ativacao":self.dt_ativacao
                , "desativado":self.desativado
                , "dt_desativado":self.dt_desativado
                , "dt_cadastro":self.dt_cadastro
                , "dt_atualizado":self.dt_atualizado
                , "token_ativo": self.token_ativo}
