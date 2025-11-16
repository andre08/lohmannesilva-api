from util.sqlbuilder import *

class Registro:
    """
    Classe: Registro
    Descrição: Classe utilizada para registrar o log de acesso ao programa, deve registrar cada acesso e o token utilizado para acesso
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "REGISTRO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idregistro": "IDREGISTRO"
        , "idusuario": "IDUSUARIO"
        , "idtoken": "IDTOKEN"
        , "modelo": "MODULO"
        , "acao": "ACAO"
        , "dt_registro": "DT_REGISTRO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idregistro"]
    
    def __init__(self, idregistro, idusuario, idtoken, modelo, acao, dt_registro):
        self.idregistro = idregistro
        self.idusuario = idusuario
        self.idtoken = idtoken
        self.modelo = modelo
        self.acao = acao
        self.dt_registro = dt_registro

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
            registro = cls(row["idregistro"], row["idusuario"], row["idtoken"], row["modelo"], row["acao"], row["dt_registro"])
        else:
            registro = cls(row[0], row[1], row[2], row[3], row[4], row[5])
        return registro

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idusuario, self.idtoken, self.modelo, self.acao, self.dt_registro)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idusuario, self.idtoken, self.modelo, self.acao, self.dt_registro, self.idregistro)

    def to_dict(self):
        dt_registro_formatada = self.dt_registro.strftime("%d/%m/%Y %H:%M:%S")
        return {"idregistro": self.idregistro
                , "idusuario": self.idusuario
                , "idtoken": self.idtoken
                , "modelo": self.modelo
                , "acao": self.acao
                , "dt_registro": dt_registro_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Registro.__tabela_banco__, Registro.__campos_tabela__, Registro.__campos_chave__, "?")