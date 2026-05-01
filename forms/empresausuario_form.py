from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class EmpresaUsuarioForm(FlaskForm):

   # Identificador do vínculo empresa-usuário (chave primária)
   idempresa_usuario = HiddenField(
      "Identificador"
      , id="idempresa_usuario"
      , render_kw={"class": "form-control", "placeholder": "Identificador do vínculo"}
   )

   # Identificador da empresa (chave estrangeira)
   idempresa = SelectField(
      "Empresa:"
      , coerce=int
      , validators=[DataRequired(message="Selecione a empresa")]
      , id="idempresa"
      , render_kw={"class": "form-control", "placeholder": "Selecione a empresa"}
   )

   # Identificador do usuário associado (chave estrangeira)
   idusuario = SelectField(
      "Usuário:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o usuário")]
      , id="idusuario"
      , render_kw={"class": "form-control", "placeholder": "Selecione o usuário"}
   )

   # Papel do usuário na empresa
   papel = StringField(
      "Papel:"
      , validators=[DataRequired(), Length(min=1, max=50)]
      , id="papel"
      , render_kw={"class": "form-control", "placeholder": "Informe o papel do usuário na empresa"}
   )

   # Data de cadastro do vínculo
   dt_cadastro = DateTimeField(
      "Data de cadastro:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_cadastro"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Situação do vínculo (A/D)
   status = SelectField(
      "Status:"
      , choices=[("A", "Ativo"), ("D", "Desativado")]
      , validators=[DataRequired()]
      , id="status"
      , render_kw={"class": "form-control", "placeholder": "Selecione o status do vínculo"}
   )
