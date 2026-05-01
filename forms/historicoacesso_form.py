from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional

class HistoricoAcessoForm(FlaskForm):

   # Identificador do histórico de acesso (chave primária)
   idhistorico_acesso = HiddenField(
      "Identificador"
      , id="idhistorico_acesso"
      , render_kw={"class": "form-control", "placeholder": "Identificador do histórico"}
   )

   # Identificador do usuário relacionado ao acesso (chave estrangeira)
   idusuario = SelectField(
      "Usuário:"
      , coerce=int
      , validators=[Optional()]
      , id="idusuario"
      , render_kw={"class": "form-control", "placeholder": "Selecione o usuário"}
   )

   # Rota acessada
   rota = TextAreaField(
      "Rota acessada:"
      , validators=[Optional()]
      , id="rota"
      , render_kw={"class": "form-control", "placeholder": "Informe a rota acessada"}
   )

   # Método HTTP utilizado (GET, POST, PUT, etc.)
   metodo = StringField(
      "Método HTTP:"
      , validators=[Optional(), Length(max=10)]
      , id="metodo"
      , render_kw={"class": "form-control", "placeholder": "Informe o método HTTP"}
   )

   # Endereço IP do cliente
   ip = StringField(
      "Endereço IP:"
      , validators=[Optional()]
      , id="ip"
      , render_kw={"class": "form-control", "placeholder": "Informe o IP do acesso"}
   )

   # Caminho no servidor
   path_server = TextAreaField(
      "Path no servidor:"
      , validators=[Optional()]
      , id="path_server"
      , render_kw={"class": "form-control", "placeholder": "Informe o path no servidor"}
   )

   # URL completa acessada
   full_url = TextAreaField(
      "URL completa:"
      , validators=[Optional()]
      , id="full_url"
      , render_kw={"class": "form-control", "placeholder": "Informe a URL completa"}
   )

   # Query string utilizada na requisição
   query_string = TextAreaField(
      "Query string:"
      , validators=[Optional()]
      , id="query_string"
      , render_kw={"class": "form-control", "placeholder": "Informe a query string"}
   )

   # Dados enviados via formulário
   form_data = TextAreaField(
      "Form data:"
      , validators=[Optional()]
      , id="form_data"
      , render_kw={"class": "form-control", "placeholder": "Informe os dados do formulário"}
   )

   # Dados enviados como JSON
   json_data = TextAreaField(
      "JSON data:"
      , validators=[Optional()]
      , id="json_data"
      , render_kw={"class": "form-control", "placeholder": "Informe os dados JSON enviados"}
   )

   # Data e hora do acesso
   dt_acesso = DateTimeField(
      "Data do acesso:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_acesso"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
