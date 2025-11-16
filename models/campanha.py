class Campanha:
    """
    Classe: Campanha
    Descrição: Classe utilizada para montar a lista de Campanha
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "CAMPANHA"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idcampanha": "IDCAMPANHA"
        , "idempresa": "IDEMPRESA"
        , "idusuario_analista": "IDUSUARIO_ANALISTA"
        , "nome": "NOME"
        , "objetivo": "OBJETIVO"
        , "meta": "META"
        , "descricao": "DECRICAO"
        , "status": "STATUS"
        , "status_kambam": "STATUS_KAMBAM"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idcampanha"]

    def __init__(self, idcampanha, idempresa, idusuario_analista, nome, objetivo, meta, descricao, status, status_kambam):
        self.idcampanha = idcampanha
        self.idempresa = idempresa
        self.idusuario_analista = idusuario_analista
        self.nome = nome
        self.objetivo = objetivo
        self.meta = meta
        self.descricao = descricao
        self.status = status
        self.status_kambam = status_kambam

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
            empresaUsuario = cls(row["idcampanha"], row["idempresa"], row["idusuario_analista"], row["nome"], row["objetivo"], row["meta"], row["descricao"], row["status"], row["status_kambam"])
        else:
            empresaUsuario = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        return empresaUsuario

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idempresa, self.idusuario_analista, self.nome, self.objetivo, self.meta, self.descricao, self.status, self.status_kambam)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.idusuario_analista, self.nome, self.objetivo, self.meta, self.descricao, self.status, self.status_kambam, self.idcampanha)

    def to_dict(self):
        return {"idcampanha": self.idcampanha
                , "idempresa": self.idempresa
                , "idusuario_analista": self.idusuario_analista
                , "nome": self.nome
                , "objetivo": self.objetivo
                , "meta": self.meta
                , "descricao": self.descricao
                , "status": self.status
                , "status_kambam": self.status_kambam}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Campanha.__tabela_banco__, Campanha.__campos_tabela__, Campanha.__campos_chave__, "?")