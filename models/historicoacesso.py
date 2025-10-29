class HistoricoAcesso:
    """
    Classe: HistoricoAcesso
    Descrição: Classe utilizada para montar a lista historica de acesso do usuario
    """
    def __init__(self, idhistorico_acesso, idusuario, rota, dt_acesso):
        self.idhistorico_acesso = idhistorico_acesso
        self.idusuario = idusuario
        self.rota = rota
        self.dt_acesso = dt_acesso

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
            historicoAcesso = cls(row["idhistorico_acesso"], row["idusuario"], row["rota"], row["dt_acesso"])
        else:
            historicoAcesso = cls(row[0], row[1], row[2], row[3])
        return historicoAcesso

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.rota, self.dt_acesso)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idusuario, self.rota, self.dt_acesso, self.idhistorico_acesso)

    def to_dict(self):
        dt_acesso_formatada = self.dt_acesso.strftime("%d/%m/%Y %H:%M:%S")
        return {"idhistorico_acesso": self.idhistorico_acesso
                , "idusuario": self.idusuario
                , "rota": self.rota
                , "dt_acesso": dt_acesso_formatada}
