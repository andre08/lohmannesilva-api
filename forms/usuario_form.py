from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, HiddenField, DateTimeField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class UsuarioForm(FlaskForm):
   # configuração campo identificador
   idusuario = HiddenField(
      "Identificador:"
      , id="idusuario"
      , render_kw={"class": "form-control", "placeholder": "Identificador do usuário"}
   )
   
   # configuração campo nome
   nome = StringField(
      "Nome:"
      , validators=[DataRequired(), Length(min=3, max=20)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome para o usuário"}
   )
   
   # configuração campo email
   email = EmailField(
      "E-mail:"
      , validators=[DataRequired(), Email()]
      , id="email"
      , render_kw={"class": "form-control", "placeholder": "Informe o e-mail do usuário"}
   )
   
   # configuração campo senha
   senha = PasswordField(
      "Senha:"
      , validators=[DataRequired()]
      , id="senha"
      , render_kw={"class": "form-control", "placeholder": "Informe uma senha (mín. 6 caracteres)"}
   )
   
   # configuração campo ativação do usuário
   ativo = SelectField(
      "Ativado?"
      , validators=[DataRequired()]
      , choices=[("S", "Sim"), ("N", "Não")]
      , id="ativo"
      , render_kw={"class": "form-check", "placeholder": "Informe se o usuário está ativo"}
   )
   
   # configuração campo data de ativação
   dt_ativacao = DateTimeField(
      "Data de ativação do usuário:"
      , validators=[]
      , id="dt_ativacao"
      , format="%d/%m/%Y %H:%M:%S"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
   
   # configuração campo de desativação do usuário
   desativado = SelectField(
      "Desativado?"
      , validators=[DataRequired()]
      , choices=[("S", "Sim"), ("N", "Não")]
      , id="desativado"
      , render_kw={"class": "form-check", "placeholder": "Usuário desativado?"}
   )
   
   # configuração campo data de desativação
   dt_desativado = DateTimeField(
      "Data de desativação do usuário:"
      , validators=[]
      , id="dt_desativado"
      , format="%d/%m/%Y %H:%M:%S"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
   
   # configuração campo data de cadastro
   dt_cadastro = DateTimeField(
      "Data de cadastro do usuário:"
      , validators=[]
      , id="dt_cadastro"
      , format="%d/%m/%Y %H:%M:%S"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
   
   # configuração campo data de cadastro
   dt_atualizado = DateTimeField(
      "Data de atualização do usuário:"
      , validators=[]
      , id="dt_atualizado"
      , format="%d/%m/%Y %H:%M:%S"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
   
   # configuração campo tipo de usuário
   opcoesTipo= [  ("ADMIN", "Administrador")
                  , ("ADMINISTRATIVO", "Administrativo")
                  , ("CLIENTE", "Cliente")
                  , ("VENDEDOR", "Vendedor")
                  , ("ANALISTA", "Analista responsável")
                  , ("CIENTISTA", "Cientista responsável")
                  , ("NORMAL", "Normal")
               ]
   
   tipo = SelectField(
      "Tipo de usuário:"
      , validators=[DataRequired()]
      , id="tipo"
      , render_kw={"class": "form-control", "placeholder": "Selecione o tipo de usuário"}
      , choices=opcoesTipo
   )
