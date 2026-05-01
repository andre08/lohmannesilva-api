from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class ArquivoForm(FlaskForm):

   # Identificador do arquivo (chave primária)
   idarquivo = HiddenField(
      "Identificador"
      , id="idarquivo"
      , render_kw={"class": "form-control", "placeholder": "Identificador do arquivo"}
   )

   # Identificador do estudo relacionado ao arquivo (chave estrangeira)
   idestudo = SelectField(
      "Estudo:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o estudo")]
      , id="idestudo"
      , render_kw={"class": "form-control", "placeholder": "Selecione o estudo"}
   )

   # Nome do arquivo
   nome = StringField(
      "Nome:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome do arquivo"}
   )

   # Descrição do arquivo
   decricao = StringField(
      "Descrição:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="decricao"
      , render_kw={"class": "form-control", "placeholder": "Informe uma descrição do arquivo"}
   )

   # Identificação do arquivo (ex: nome interno, tag, referência)
   identificacao = StringField(
      "Identificação:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="identificacao"
      , render_kw={"class": "form-control", "placeholder": "Informe a identificação do arquivo"}
   )

   # Localização do arquivo no storage/Bucket/Container
   localizacao_container = StringField(
      "Localização no container:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="localizacao_container"
      , render_kw={"class": "form-control", "placeholder": "Informe onde o arquivo está armazenado"}
   )

   # Data de importação do arquivo
   dt_importacao = DateTimeField(
      "Data de importação:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_importacao"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
