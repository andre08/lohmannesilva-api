from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, DateTimeField
from wtforms.validators import DataRequired, Length

class RelatorioForm(FlaskForm):

   # Identificador do relatório (chave primária)
   idrelatorio = HiddenField(
      "Identificador"
      , id="idrelatorio"
      , render_kw={"class": "form-control", "placeholder": "Identificador do relatório"}
   )

   # Identificador do estudo relacionado (chave estrangeira)
   idestudo = SelectField(
      "Estudo:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o estudo")]
      , id="idestudo"
      , render_kw={"class": "form-control", "placeholder": "Selecione o estudo"}
   )

   # Nome do relatório
   nome = StringField(
      "Nome do relatório:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome do relatório"}
   )

   # Descrição do relatório
   descricao = StringField(
      "Descrição:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="descricao"
      , render_kw={"class": "form-control", "placeholder": "Informe a descrição do relatório"}
   )

   # Identificação interna do relatório
   identificacao = StringField(
      "Identificação:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="identificacao"
      , render_kw={"class": "form-control", "placeholder": "Informe a identificação interna"}
   )

   # Localização do arquivo no container (Azure/Blob/S3, etc.)
   localizacao_container = StringField(
      "Localização no container:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="localizacao_container"
      , render_kw={"class": "form-control", "placeholder": "Informe a localização do arquivo"}
   )

   # Data de geração do relatório
   dt_geracao = DateTimeField(
      "Data de geração:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_geracao"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
