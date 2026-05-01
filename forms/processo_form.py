from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField
from wtforms.validators import DataRequired, Length

class ProcessoForm(FlaskForm):

    # Identificador do processo (chave primária)
    idprocesso = HiddenField(
        "Identificador",
        id="idprocesso",
        render_kw={"class": "form-control", "placeholder": "Identificador do processo"}
    )

    # Nome do processo
    nome = StringField(
        "Nome do processo:",
        validators=[DataRequired(), Length(min=1, max=100)],
        id="nome",
        render_kw={"class": "form-control", "placeholder": "Informe o nome do processo"}
    )

    # Descrição do processo
    descricao = StringField(
        "Descrição:",
        validators=[DataRequired(), Length(min=1, max=100)],
        id="descricao",
        render_kw={"class": "form-control", "placeholder": "Informe a descrição do processo"}
    )

    # Status do processo (A = ativo, D = desativado)
    status = SelectField(
        "Status:",
        choices=[
            ("A", "Ativo"),
            ("D", "Desativado")
        ],
        validators=[DataRequired()],
        id="status",
        render_kw={"class": "form-control", "placeholder": "Selecione o status do processo"}
    )
