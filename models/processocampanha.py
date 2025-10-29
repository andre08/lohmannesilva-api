class ProcessoCampanha:
    """
    Classe: ProcessoCampanha
    Descrição: Classe utilizada para relacionar os processos da campanha
    """
    def __init__(self, idprocesso_campanha, idcampanha, idprocesso, idusuario_responsavel, dt_inicio_execucao, dt_final_execucao):
        self.idprocesso_campanha = idprocesso_campanha
        self.idcampanha = idcampanha
        self.idprocesso = idprocesso
        self.idusuario_responsavel = idusuario_responsavel
        self.dt_inicio_execucao = dt_inicio_execucao
        self.dt_final_execucao = dt_final_execucao

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
            processoCampanha  = cls(row["idprocesso_campanha"],row["idcampanha"],row["idprocesso"],row["idusuario_responsavel"],row["dt_inicio_execucao"],row["dt_final_execucao"])
        else:
            processoCampanha  = cls(row[0],row[1],row[2],row[3],row[4],row[5])
        return processoCampanha

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idcampanha, self.idprocesso, self.idusuario_responsavel, self.dt_inicio_execucao, self.dt_final_execucao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idcampanha, self.idprocesso, self.idusuario_responsavel, self.dt_inicio_execucao, self.dt_final_execucao, self.idprocesso_campanha)

    def to_dict(self):
        dt_inicio_execucao_formatada = self.dt_inicio_execucao.strftime("%d/%m/%Y %H:%M:%S")
        dt_final_execucao_formatada = self.dt_final_execucao.strftime("%d/%m/%Y %H:%M:%S")
        return {"idprocesso_campanha": self.idprocesso_campanha
                , "idcampanha": self.idcampanha
                , "idprocesso": self.idprocesso
                , "idusuario_responsavel": self.idusuario_responsavel
                , "dt_inicio_execucao": dt_inicio_execucao_formatada
                , "dt_final_execucao": dt_final_execucao_formatada}
