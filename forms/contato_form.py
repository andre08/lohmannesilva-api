from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, HiddenField, DateTimeField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class ContatoForm(FlaskForm):
   # configuração campo identificador
   idcontato = HiddenField(
      "Identificador:"
      , id="idcontato"
      , render_kw={"class": "form-control"}
   )

   # configuração campo nome
   nome = StringField(
      "Nome:"
      , validators=[DataRequired(), Length(min=3, max=20)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe seu nome para contato"}
   )

   # configuração campo email
   email = EmailField(
      "E-mail:"
      , validators=[DataRequired(), Email()]
      , id="email"
      , render_kw={"class": "form-control", "placeholder": "Informe um e-mail para contato"}
   )

   # configuração campo telefone
   telefone = StringField(
      "Telefone:"
      , validators=[DataRequired()]
      , id="telefone"
      , render_kw={"class": "form-control"}
   )

   # configuração campo mensagem
   mensagem = TextAreaField(
      "Mesangem:"
      , validators=[DataRequired(), Length(min=10, max=200)]
      , id="mensagem"
      , render_kw={"class": "form-control", "placeholder": "Digite aqui sua necessidade ou duvida"}
   )

   # configuração campo tipo de contato
   opcoesTipo= [
        (1, "Quero uma análise diagnóstica gratuita")
      , (2, "Analisar minha campanha")
      , (3, "Quero ser parceiro growth")
      , (4, "Quero uma apresentação agendada")
   ]
   tipo = SelectField(
      "Tipo de contato:"
      , validators=[DataRequired()]
      , id="tipo"
      , render_kw={"class": "form-control"}
      , choices=opcoesTipo
   )

   # configuração campo visualizado
   visualizado = BooleanField(
      "Contato visualizado:"
      , validators=[DataRequired()]
      , id="visualizado"
      , render_kw={"class": "form-check"}
   )

   # configuração campo respondido
   respondido = BooleanField(
      "Contato respondido?"
      , validators=[DataRequired()]
      , id="respondido"
      , render_kw={"class": "form-check"}
   )

   # configuração campo interesse
   interesse = BooleanField(
      "Ainda Interessado?"
      , validators=[DataRequired()]
      , id="interesse"
      , render_kw={"class": "form-check"}
   )

   # configuração campo cliente
   cliente = BooleanField(
      "Cliente?"
      , validators=[DataRequired()]
      , id="cliente"
      , render_kw={"class": "form-check"}
   )

   # configuração campo contato ativo
   ativo = BooleanField(
      "Ainda ativos?"
      , validators=[DataRequired()]
      , id="ativo"
      , render_kw={"class": "form-check"}
   )

   # configuração campo data de contato
   dt_contato = DateTimeField(
      "Data do contato:"
      , validators=[]
      , id="dt_contato"
      , format="%d/%m/%Y %H:%M:%S"
      , render_kw={"class": "form-control"}
   )
