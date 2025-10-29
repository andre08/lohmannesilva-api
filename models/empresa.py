class Processo:
    """
    Classe: Processo
    Descrição: Classe utilizada para montar a lista de processo disponiveis
    """
    def __init__(self, idempresa, nome, idplano_padrao, dt_primeiro_contato, dt_inicio_contrato, dt_final_contrato, status):
        self.idempresa = idempresa
        self.nome = nome
        self.idplano_padrao = idplano_padrao
        self.dt_primeiro_contato = dt_primeiro_contato
        self.dt_inicio_contrato = dt_inicio_contrato
        self.dt_final_contrato = dt_final_contrato
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
            empresa = cls(row["idempresa"], row["nome"], row["idplano_padrao"], row["dt_primeiro_contato"], row["dt_inicio_contrato"], row["dt_final_contrato"], row["status"])
        else:
            empresa = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return empresa

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.idplano_padrao, self.dt_primeiro_contato, self.dt_inicio_contrato, self.dt_final_contrato, self.status)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.idplano_padrao, self.dt_primeiro_contato, self.dt_inicio_contrato, self.dt_final_contrato, self.status, self.idempresa)

    def to_dict(self):
        dt_primeiro_contato_formatada = self.dt_primeiro_contato.strftime("%d/%m/%Y %H:%M:%S")
        dt_inicio_contrato_formatada = self.dt_inicio_contrato.strftime("%d/%m/%Y %H:%M:%S")
        dt_final_contrato_formatada = self.dt_final_contrato.strftime("%d/%m/%Y %H:%M:%S")
        return {"idempresa": self.idempresa
                , "nome": self.nome
                , "idplano_padrao": self.idplano_padrao
                , "dt_primeiro_contato": dt_primeiro_contato_formatada
                , "dt_inicio_contrato": dt_inicio_contrato_formatada
                , "dt_final_contrato": dt_final_contrato_formatada
                , "status": self.status}
