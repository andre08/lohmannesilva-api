class Arquivo:
    """
    Classe: Arquivo
    Descrição: Classe utilizada para registrar os Arquivos da campanha
    """
    def __init__(self, idarquivo, idcampanha, nome, decricao, identificacao, localizacao_container, dt_importacao):
        self.idarquivo = idarquivo
        self.idcampanha = idcampanha
        self.nome = nome
        self.decricao = decricao
        self.identificacao = identificacao
        self.localizacao_container = localizacao_container
        self.dt_importacao = dt_importacao

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
            arquivo  = cls(row["idarquivo"], row["idcampanha"], row["nome"], row["decricao"], row["identificacao"], row["localizacao_container"], row["dt_importacao"])
        else:
            arquivo = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return arquivo

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idcampanha, self.nome, self.decricao, self.identificacao, self.localizacao_container, self.dt_importacao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idcampanha, self.nome, self.decricao, self.identificacao, self.localizacao_container, self.dt_importacao, self.idarquivo)

    def to_dict(self):
        dt_importacao_formatada = self.dt_importacao.strftime("%d/%m/%Y %H:%M:%S")
        return {"idarquivo": self.idarquivo
                , "idcampanha": self.idcampanha
                , "nome": self.nome
                , "decricao": self.decricao
                , "identificacao": self.identificacao
                , "localizacao_container": self.localizacao_container
                , "dt_importacao": dt_importacao_formatada}
