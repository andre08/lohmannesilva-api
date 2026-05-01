from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import DataRequired, Length

class ProcessoEstudoForm(FlaskForm):

    # Identificador do vínculo processo-estudo (chave primária)
    idprocesso_estudo = HiddenField(
        "Identificador"
        , id="idprocesso_estudo"
        , render_kw={"class": "form-control", "placeholder": "Identificador do processo-estudo"}
    )

    # Identificador do processo (chave estrangeira)
    idprocesso = SelectField(
        "Processo:"
        , coerce=int
        , validators=[DataRequired(message="Selecione o processo")]
        , id="idprocesso"
        , render_kw={"class": "form-control", "placeholder": "Selecione o processo"}
    )

    # Identificador do estudo (chave estrangeira)
    idestudo = SelectField(
        "Estudo:"
        , coerce=int
        , validators=[DataRequired(message='Selecione o estudo')]
        , id="idestudo"
        , render_kw={"class": "form-control", "placeholder": "Selecione o estudo"}
    )

    # Ordem do processo no estudo
    ordem = StringField(
        "Ordem do processo:"
        , validators=[DataRequired(), Length(min=1, max=10)]
        , id="ordem"
        , render_kw={"class": "form-control", "placeholder": "Informe a ordem do processo"}
    )

    # Status da etapa (A = ativo, D = desativado)
    status = SelectField(
        "Status:"
        , choices=[("A", "Ativo"), ("D", "Desativado")]
        , validators=[DataRequired()]
        , id="status"
        , render_kw={"class": "form-control", "placeholder": "Selecione o status"}
    )
