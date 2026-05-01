from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField
from wtforms.validators import DataRequired, Length

class ItemFaturaForm(FlaskForm):

    # Identificador do item de fatura (chave primária)
    iditem_fatura = HiddenField(
        "Identificador"
        , id="iditem_fatura"
        , render_kw={"class": "form-control", "placeholder": "Identificador do item da fatura"}
    )

    # Identificador da fatura (chave estrangeira)
    idfatura = SelectField(
        "Fatura:"
        , coerce=int
        , validators=[DataRequired(message="Selecione a fatura")]
        , id="idfatura"
        , render_kw={"class": "form-control", "placeholder": "Selecione a fatura"}
    )

    # Identificador do estudo relacionado ao item (chave estrangeira)
    idestudo = SelectField(
        "Estudo:"
        , coerce=int
        , validators=[DataRequired(message="Selecione o estudo")]
        , id="idestudo"
        , render_kw={"class": "form-control", "placeholder": "Selecione o estudo"}
    )

    # Identificador do plano associado ao item (chave estrangeira)
    idplano_item = SelectField(
        "Plano do item:"
        , coerce=int
        , validators=[DataRequired(message="Selecione o plano")]
        , id="idplano_item"
        , render_kw={"class": "form-control", "placeholder": "Selecione o plano do item"}
    )

    # Descrição do item
    descricao = StringField(
        "Descrição:"
        , validators=[DataRequired(), Length(min=1, max=300)]
        , id="descricao"
        , render_kw={"class": "form-control", "placeholder": "Informe a descrição do item"}
    )

    # Valor unitário do item
    valor_unitario = StringField(
        "Valor unitário:"
        , validators=[DataRequired(), Length(min=1, max=20)]
        , id="valor_unitario"
        , render_kw={"class": "form-control", "placeholder": "Informe o valor unitário"}
    )

    # Indica se o estudo pertence a um parceiro growth (S/N)
    estudo_parceiro_growth = SelectField(
        "Parceiro Growth:"
        , choices=[("S", "Sim"),("N", "Não")]
        , validators=[DataRequired()]
        , id="estudo_parceiro_growth"
        , render_kw={"class": "form-control", "placeholder": "Informe se é parceiro Growth"}
    )
