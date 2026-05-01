from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField
from wtforms.validators import DataRequired, Length

class AtalhoForm(FlaskForm):

   # Identificador do atalho (chave primária)
   idatalho = HiddenField(
      "Identificador"
      , id="idatalho"
      , render_kw={"class": "form-control", "placeholder": "Identificador do atalho"}
   )

   # Identificador do usuário proprietário do atalho (chave estrangeira)
   idusuario = SelectField(
      "Usuário:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o usuário")]
      , id="idusuario"
      , render_kw={"class": "form-control", "placeholder": "Selecione o usuário"}
   )

   # Grupo ao qual o atalho pertence
   grupo = StringField(
      "Grupo:"
      , validators=[DataRequired(), Length(min=1, max=100)]
      , id="grupo"
      , render_kw={"class": "form-control", "placeholder": "Informe o grupo do atalho"}
   )

   # Nome do atalho
   nome = StringField(
      "Nome:"
      , validators=[DataRequired(), Length(min=1, max=100)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome do atalho"}
   )

   # Rota URL que o atalho aponta
   rota = StringField(
      "Rota:"
      , validators=[DataRequired(), Length(min=1, max=250)]
      , id="rota"
      , render_kw={"class": "form-control", "placeholder": "Informe a rota que o atalho acessa"}
   )
