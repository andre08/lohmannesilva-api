from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class EmpresaForm(FlaskForm):

   # Identificador da empresa (chave primária)
   idempresa = HiddenField(
      "Identificador"
      , id="idempresa"
      , render_kw={"class": "form-control", "placeholder": "Identificador da empresa"}
   )

   # Nome da empresa
   nome = StringField(
      "Nome da empresa:"
      , validators=[DataRequired(), Length(min=1, max=200)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome da empresa"}
   )

   # Identificador do plano padrão associado (chave estrangeira)
   idplano_padrao = SelectField(
      "Plano padrão:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o plano padrão")]
      , id="idplano_padrao"
      , render_kw={"class": "form-control", "placeholder": "Selecione o plano padrão"}
   )

   # Data do primeiro contato com a empresa
   dt_primeiro_contato = DateTimeField(
      "Primeiro contato:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_primeiro_contato"
      , validators=[DataRequired()]
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Data de início do contrato vigente
   dt_inicio_contrato = DateTimeField(
      "Início do contrato:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_inicio_contrato"
      , validators=[DataRequired()]
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Data de término do contrato vigente
   dt_final_contrato = DateTimeField(
      "Final do contrato:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_final_contrato"
      , validators=[DataRequired()]
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Situação da empresa (A, P, D)
   status = SelectField(
      "Status:"
      , choices=[("A", "Ativa"), ("P", "Parceiro"), ("D", "Desativada")]
      , validators=[DataRequired()]
      , id="status"
      , render_kw={"class": "form-control", "placeholder": "Selecione o status da empresa"}
   )
