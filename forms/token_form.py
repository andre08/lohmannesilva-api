from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, DateTimeField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

class TokenForm(FlaskForm):
   # Campo identificador
   idtoken = HiddenField(  "Identificador:"
                           , id="idtoken"
                           , render_kw={"class": "form-control"}
                        )
   # Campo identificador do usuário
   idusuario = SelectField("Usuário:"
                           , id="idusuario"
                           , coerce=int
                           , validators=[DataRequired()]
                           , render_kw={"class": "form-control"}
                        )
   # Campo token de acesso
   token = StringField( "Token:"
                        , id="token"
                        , validators=[DataRequired(), Length(min=5, max=200)]
                        ,render_kw={"class": "form-control"}
                     )
   # Campo chave secreta usada no momento da criação do token
   secret_key = StringField(  "Chave Secreta:"
                              , id="secret_key"
                              , validators=[DataRequired(), Length(min=5, max=200)]
                              , render_kw={"class": "form-control"}
                           )
   # Campo data de criação do token
   dt_criacao = DateTimeField("Data de criação:"
                              , id="dt_criacao"
                              , format="%d/%m/%Y %H:%M:%S"
                              , render_kw={"class": "form-control"}
                           )

   dt_expiracao = DateTimeField("Data de expiração:",
                                 format="%d/%m/%Y %H:%M:%S",
                                 render_kw={"class": "form-control"})

   desativado = SelectField("Desativado:",
                             choices=[("S", "Sim"), ("N", "Não")],
                             render_kw={"class": "form-control"})

   dt_desativado = DateTimeField("Data de desativação:",
                                  format="%d/%m/%Y %H:%M:%S",
                                  render_kw={"class": "form-control"})

   dt_atualizado = DateTimeField("Última atualização:",
                                  format="%d/%m/%Y %H:%M:%S",
                                  render_kw={"class": "form-control"})
