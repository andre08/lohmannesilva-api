from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField
from wtforms.validators import DataRequired, Length

class EstudoForm(FlaskForm):

   # Identificador do estudo (chave primária)
   idestudo = HiddenField(
      "Identificador"
      , id="idestudo"
      , render_kw={"class": "form-control", "placeholder": "Identificador do estudo"}
   )

   # Identificador da empresa associada ao estudo (chave estrangeira)
   idempresa = SelectField(
      "Empresa:"
      , coerce=int
      , validators=[DataRequired(message="Selecione a empresa")]
      , id="idempresa"
      , render_kw={"class": "form-control", "placeholder": "Selecione a empresa"}
   )

   # Identificador do analista responsável pelo estudo (chave estrangeira)
   idusuario_analista = SelectField(
      "Analista responsável:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o analista")]
      , id="idusuario_analista"
      , render_kw={"class": "form-control", "placeholder": "Selecione o analista responsável"}
   )

   # Tipo do estudo (ex.: campanha, análise de desempenho etc.)
   tipo = StringField(
      "Tipo do estudo:"
      , validators=[DataRequired(), Length(min=1, max=150)]
      , id="tipo"
      , render_kw={"class": "form-control", "placeholder": "Informe o tipo do estudo"}
   )

   # Nome do estudo
   nome = StringField(
      "Nome do estudo:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome do estudo"}
   )

   # Objetivo do estudo
   objetivo = StringField(
      "Objetivo:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="objetivo"
      , render_kw={"class": "form-control", "placeholder": "Informe o objetivo do estudo"}
   )

   # Meta do estudo
   meta = StringField(
      "Meta:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="meta"
      , render_kw={"class": "form-control", "placeholder": "Informe a meta definida para o estudo"}
   )

   # Descrição do estudo
   decricao = StringField(
      "Descrição:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="decricao"
      , render_kw={"class": "form-control", "placeholder": "Descreva o estudo"}
   )

   # Situação do estudo (A/D)
   status = SelectField(
      "Status:"
      , choices=[("A", "Ativo"), ("D", "Desativado")]
      , validators=[DataRequired()]
      , id="status"
      , render_kw={"class": "form-control", "placeholder": "Selecione o status do estudo"}
   )

   # Status no kambam (A mover, em execução, concluído etc.)
   status_kambam = SelectField(
      "Status kanban:"
      , choices=[("A", "A fazer"), ("E", "Em execução"), ("C", "Concluído")]
      , validators=[DataRequired()]
      , id="status_kambam"
      , render_kw={"class": "form-control", "placeholder": "Selecione o status do kanban"}
   )
