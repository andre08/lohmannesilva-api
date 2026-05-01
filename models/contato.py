from datetime import datetime
from util.sqlbuilder import *

class Contato:
    """
    Classe: Contato
    Descrição: Classe utilizada para registrar o contatos do site
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "CONTATO"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idcontato": "IDCONTATO"
        , "nome": "NOME"
        , "email": "EMAIL"
        , "telefone": "TELEFONE"
        , "mensagem": "MENSAGEM"
        , "tipo": "TIPO"
        , "visualizado": "VISUALIZADO"
        , "respondido": "RESPONDIDO"
        , "interesse": "INTERESSE"
        , "cliente": "CLIENTE"
        , "ativo": "ATIVO"
        , "dt_contato": "DT_CONTATO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idcontato"]

    def __init__(self, idcontato, nome=None, email=None, telefone=None, mensagem=None, tipo=None, visualizado=None, respondido=None, interesse=None, cliente=None, ativo=None, dt_contato=None):
        self.idcontato = idcontato
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.mensagem = mensagem
        self.tipo = tipo
        self.visualizado = visualizado
        self.respondido = respondido
        self.interesse = interesse
        self.cliente = cliente
        self.ativo = ativo
        self.dt_contato = dt_contato

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
            contato = cls(row["idcontato"], row["nome"], row["email"], row["telefone"], row["mensagem"], row["tipo"], row["visualizado"], row["respondido"], row["interesse"], row["cliente"], row["ativo"], row["dt_contato"])
        else:
            contato = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        return contato

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.nome, self.email, self.telefone, self.mensagem, self.tipo, self.visualizado, self.respondido, self.interesse, self.cliente, self.ativo, self.dt_contato)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.nome, self.email, self.telefone, self.mensagem, self.tipo, self.visualizado, self.respondido, self.interesse, self.cliente, self.ativo, self.dt_contato, self.idcontato)

    def to_dict(self, hieraquia=False):
        
        if self.dt_contato:
            dt_contato_formatada = datetime.strftime(self.dt_contato, "%Y-%m-%d") 
            dt_contato_formatada2 = datetime.strftime(self.dt_contato, "%d/%m/%Y")
        else:
            dt_contato_formatada = None
            dt_contato_formatada2 = None


        return {"idcontato": self.idcontato
                , "nome": self.nome
                , "email": self.email
                , "telefone": self.telefone
                , "mensagem": self.mensagem
                , "tipo": self.tipo
                , "visualizado": self.visualizado
                , "respondido": self.respondido
                , "interesse": self.interesse
                , "cliente": self.cliente
                , "ativo": self.ativo
                , "dt_contato": self.dt_contato
                , "dt_contato2": dt_contato_formatada2
            }

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(Contato.__tabela_banco__, Contato.__campos_tabela__, Contato.__campos_chave__, "?")