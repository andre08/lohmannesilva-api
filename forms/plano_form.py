from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField
from wtforms.validators import DataRequired, Length

class PlanoForm(FlaskForm):

   # Identificador do plano (chave primária)
   idplano = HiddenField(
      "Identificador"
      , id="idplano"
      , render_kw={"class": "form-control", "placeholder": "Identificador do plano"}
   )

   # Nome do plano
   nome = StringField(
      "Nome do plano:"
      , validators=[DataRequired(), Length(min=1, max=100)]
      , id="nome"
      , render_kw={"class": "form-control", "placeholder": "Informe o nome do plano"}
   )

   # Descrição do plano
   descricao = StringField(
      "Descrição:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="descricao"
      , render_kw={"class": "form-control", "placeholder": "Informe a descrição do plano"}
   )

   # Quantidade de estudos contemplados no plano
   qtd_estudos = StringField(
      "Quantidade de estudos:"
      , validators=[DataRequired(), Length(min=1, max=10)]
      , id="qtd_estudos"
      , render_kw={"class": "form-control", "placeholder": "Informe a quantidade de estudos"}
   )

   # Quantidade total de relatórios contemplados no plano
   qtd_relatorios = StringField(
      "Quantidade de relatórios:"
      , validators=[DataRequired(), Length(min=1, max=10)]
      , id="qtd_relatorios"
      , render_kw={"class": "form-control", "placeholder": "Informe a quantidade de relatórios"}
   )

   # Valor total do plano
   valor = StringField(
      "Valor do plano:"
      , validators=[DataRequired(), Length(min=1, max=20)]
      , id="valor"
      , render_kw={"class": "form-control", "placeholder": "Informe o valor do plano"}
   )

   # Status do plano (A = ativo, D = desativado)
   status = SelectField(
      "Status:"
      , choices=[("A", "Ativo"), ("D", "Desativado")]
      , validators=[DataRequired()]
      , id="status"
      , render_kw={"class": "form-control", "placeholder": "Selecione o status do plano"}
   )
