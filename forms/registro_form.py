from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional

class RegistroForm(FlaskForm):

    # Identificador do registro de acesso (chave primária)
    idregistro = HiddenField(
        "Identificador"
        , id="idregistro"
        , render_kw={"class": "form-control", "placeholder": "Identificador do registro"}
    )

    # Identificador do usuário relacionado ao registro (chave estrangeira)
    idusuario = SelectField(
        "Usuário:"
        , coerce=int
        , validators=[DataRequired(message="Selecione o usuário")]
        , id="idusuario"
        , render_kw={"class": "form-control", "placeholder": "Selecione o usuário"}
    )

    # Token utilizado no acesso (chave estrangeira)
    idtoken = SelectField(
        "Token:"
        , coerce=int
        , validators=[Optional()]
        , id="idtoken"
        , render_kw={"class": "form-control", "placeholder": "Selecione o token utilizado"}
    )

    # Nome do módulo acessado
    modulo = StringField(
        "Módulo acessado:"
        , validators=[DataRequired(), Length(min=1, max=200)]
        , id="modulo"
        , render_kw={"class": "form-control", "placeholder": "Informe o módulo acessado"}
    )

    # Ação realizada no módulo
    acao = StringField(
        "Ação realizada:"
        , validators=[DataRequired(), Length(min=1, max=200)]
        , id="acao"
        , render_kw={"class": "form-control", "placeholder": "Informe a ação realizada"}
    )

    # Data e hora do registro de acesso
    dt_registro = DateTimeField(
        "Data do registro:"
        , format="%d/%m/%Y %H:%M:%S"
        , validators=[DataRequired()]
        , id="dt_registro"
        , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
    )
