from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class FaturaForm(FlaskForm):

   # Identificador da fatura (chave primária)
   idfatura = HiddenField(
      "Identificador"
      , id="idfatura"
      , render_kw={"class": "form-control", "placeholder": "Identificador da fatura"}
   )

   # Identificador da empresa que gerou a fatura (chave estrangeira)
   idempresa = SelectField(
      "Empresa:"
      , coerce=int
      , validators=[DataRequired(message="Selecione a empresa")]
      , id="idempresa"
      , render_kw={"class": "form-control", "placeholder": "Selecione a empresa"}
   )

   # Nome da fatura (ex.: mês referência, cobrança específica)
   nome = StringField(
      "Nome da fatura:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome da fatura"}
   )

   # Período de referência da fatura
   dt_referencia = DateTimeField(
      "Data de referência:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_referencia"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Valor total da fatura
   valor = StringField(
      "Valor total:"
      , validators=[DataRequired(), Length(min=1, max=20)]
      , id="valor"
      , render_kw={"class": "form-control", "placeholder": "Informe o valor total da fatura"}
   )

   # Data de vencimento da fatura
   dt_vencimento = DateTimeField(
      "Data de vencimento:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_vencimento"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Valor pago da fatura
   valor_paga = StringField(
      "Valor pago:"
      , validators=[DataRequired(), Length(min=1, max=20)]
      , id="valor_paga"
      , render_kw={"class": "form-control", "placeholder": "Informe o valor pago"}
   )

   # Data do pagamento
   dt_pagamento = DateTimeField(
      "Data de pagamento:"
      , format="%d/%m/%Y %H:%M:%S"
      , validators=[DataRequired()]
      , id="dt_pagamento"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
