from util.sqlbuilder import *

class Estudo:
    """
    Classe: Estudo
    Descrição: Classe utilizada para montar a lista de estudo
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "ESTUDO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idestudo": "IDESTUDO"
        , "idempresa": "IDEMPRESA"
        , "idusuario_analista": "IDUSUARIO_ANALISTA"
        , "tipo": "TIPO"
        , "nome": "NOME"
        , "objetivo": "OBJETIVO"
        , "meta": "META"
        , "descricao": "DECRICAO"
        , "status": "STATUS"
        , "status_kambam": "STATUS_KAMBAM"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idestudo"]

    def __init__(self, idestudo, idempresa, idusuario_analista, tipo, nome, objetivo, meta, descricao, status, status_kambam):
        self.idestudo = idestudo
        self.idempresa = idempresa
        self.idusuario_analista = idusuario_analista
        self.tipo = tipo
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
            empresaUsuario = cls(row["idestudo"], row["idempresa"], row["idusuario_analista"], row["tipo"], row["nome"], row["objetivo"], row["meta"], row["descricao"], row["status"], row["status_kambam"])
        else:
            empresaUsuario = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        return empresaUsuario

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idempresa, self.idusuario_analista, self.tipo, self.nome, self.objetivo, self.meta, self.descricao, self.status, self.status_kambam)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.idusuario_analista, self.tipo, self.nome, self.objetivo, self.meta, self.descricao, self.status, self.status_kambam, self.idestudo)

    def to_dict(self, hieraquia=False):
        from services.empresa_service import empresa_lista_selecionado
        from services.usuario_service import usuario_lista_selecionado

        if hieraquia:
            empresa, mensagemEmpresa = empresa_lista_selecionado(self.idempresa)
            if not empresa:
                empresa = {}

            usuario, mensagemUsuario = usuario_lista_selecionado(self.idusuario_analista)
            if not usuario:
                usuario = {}
        else:
            empresa = {}
            mensagemEmpresa = ""
            
            usuario = {}
            mensagemUsuario = ""

        return {"idestudo": self.idestudo
                , "idempresa": self.idempresa
                , "empresa": empresa
                , "mensagemEmpresa": mensagemEmpresa
                , "idusuario_analista": self.idusuario_analista
                , "usuarioAnalista": usuario
                , "mensagemUsuarioAnalista": mensagemUsuario
                , "tipo": self.tipo
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
        return SQLBuilder(Estudo.__tabela_banco__, Estudo.__campos_tabela__, Estudo.__campos_chave__, "?")