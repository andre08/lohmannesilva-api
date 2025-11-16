from util.sqlbuilder import *

class EmpresaUsuario:
    """
    Classe: EmpresaUsuario
    Descrição: Classe utilizada para montar a relação entre empresa e usuario
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "EMPRESA_USUARIO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idempresa_usuario": "IDEMPRESA_USUARIO"
        , "idempresa": "IDEMPRESA"
        , "idusuario": "IDUSUARIO"
        , "papel": "PAPEL"
        , "dt_cadastro": "DT_CADASTRO"
        , "status": "STATUS"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idempresa_usuario"]

    def __init__(self, idempresa_usuario, idempresa, idusuario, papel, dt_cadastro, status):
        self.idempresa_usuario = idempresa_usuario
        self.idempresa = idempresa
        self.idusuario = idusuario
        self.papel = papel
        self.dt_cadastro = dt_cadastro
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
            empresaUsuario = cls(row["idempresa_usuario"], row["idempresa"], row["idusuario"], row["papel"], row["dt_cadastro"], row["status"])
        else:
            empresaUsuario = cls(row[0], row[1], row[2], row[3], row[4], row[5])
        return empresaUsuario

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idempresa, self.idusuario, self.papel, self.dt_cadastro, self.status)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idempresa, self.idusuario, self.papel, self.dt_cadastro, self.status, self.idempresa_usuario)

    def to_dict(self):
        dt_cadastro_formatada = self.dt_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        return {"idempresa_usuario": self.idempresa_usuario
                , "idempresa": self.idempresa
                , "idusuario": self.idusuario
                , "papel": self.papel
                , "status": self.status
                , "dt_cadastro": dt_cadastro_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(EmpresaUsuario.__tabela_banco__, EmpresaUsuario.__campos_tabela__, EmpresaUsuario.__campos_chave__, "?")