from util.sqlbuilder import *

class ProcessoCampanha:
    """
    Classe: ProcessoCampanha
    Descrição: Classe utilizada para relacionar os processos da campanha
    """

    # definição da tabela que vai salvar os dados 
    __tabela_banco__ = "PROCESSO_CAMPANHA"

    # relacionando nome da classe com o nome do campo na tabela
    __campos_tabela__ = {
        "idprocesso_campanha": "IDPROCESSO_CAMPANHA"
        , "idcampanha": "IDCAMPANHA"
        , "idprocesso": "IDPROCESSO"
        , "idusuario_responsavel": "IDUSUARIO_RESPONSAVEL"
        , "observacao": "OBSERVACAO"
        , "dt_inicio_execucao": "DT_INICIO_EXECUCAO"
        , "dt_final_execucao": "DT_FINAL_EXECUCAO"
    }

    # definição dos campos chave da tabela
    __campos_chave__ = ["idprocesso_campanha"]

    def __init__(self, idprocesso_campanha, idcampanha, idprocesso, idusuario_responsavel, observacao, dt_inicio_execucao, dt_final_execucao):
        self.idprocesso_campanha = idprocesso_campanha
        self.idcampanha = idcampanha
        self.idprocesso = idprocesso
        self.observacao = observacao
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
            processoCampanha  = cls(row["idprocesso_campanha"],row["idcampanha"],row["idprocesso"],row["idusuario_responsavel"], row["observacao"],row["dt_inicio_execucao"],row["dt_final_execucao"])
        else:
            processoCampanha  = cls(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        return processoCampanha

    def to_insert_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para insert do banco de dados, 
        deve retornar os campos na ordem do insert e não tem o id, porque o id é gerado pelo banco de dados
        """
        return (self.idcampanha, self.idprocesso, self.idusuario_responsavel, self.observacao, self.dt_inicio_execucao, self.dt_final_execucao)

    def to_update_db(self):
        """
        Esse metodo retorna um tupla com os valores a serem usado para update do banco de dados, 
        deve retornar os campos na ordem do update e o id no final, porque o id é usado no where que vem depois dos valores
        """
        return (self.idcampanha, self.idprocesso, self.idusuario_responsavel, self.observacao, self.dt_inicio_execucao, self.dt_final_execucao, self.idprocesso_campanha)

    def to_dict(self):
        dt_inicio_execucao_formatada = self.dt_inicio_execucao.strftime("%d/%m/%Y %H:%M:%S")
        dt_final_execucao_formatada = self.dt_final_execucao.strftime("%d/%m/%Y %H:%M:%S")
        return {"idprocesso_campanha": self.idprocesso_campanha
                , "idcampanha": self.idcampanha
                , "idprocesso": self.idprocesso
                , "idusuario_responsavel": self.idusuario_responsavel
                , "observacao": self.observacao
                , "dt_inicio_execucao": dt_inicio_execucao_formatada
                , "dt_final_execucao": dt_final_execucao_formatada}

    def get_SQLBuilder():
        """
        Esse metodo retorna objeto que monta os comandos sql de acordo com o nome da tabela e campos declarados no inicio da classe
        """
        return SQLBuilder(ProcessoCampanha.__tabela_banco__, ProcessoCampanha.__campos_tabela__, ProcessoCampanha.__campos_chave__, "?")