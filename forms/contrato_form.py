from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class ContratoForm(FlaskForm):

   # Identificador do contrato (chave primária)
   idcontrato = HiddenField(
      "Identificador"
      , id="idcontrato"
      , render_kw={"class": "form-control", "placeholder": "Identificador do contrato"}
   )

   # Identificador da empresa vinculada ao contrato (chave estrangeira)
   idempresa = SelectField(
      "Empresa:"
      , coerce=int
      , validators=[DataRequired(message="Selecione a empresa")]
      , id="idempresa"
      , render_kw={"class": "form-control", "placeholder": "Selecione a empresa"}
   )

   # Identificador do usuário responsável pelo contrato (chave estrangeira)
   idusuario_responsavel = SelectField(
      "Usuário responsável:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o responsável")]
      , id="idusuario_responsavel"
      , render_kw={"class": "form-control", "placeholder": "Selecione o usuário responsável"}
   )

   # Identificador do vendedor responsável pelo contrato (chave estrangeira)
   idusuario_vendedor_responsavel = SelectField(
      "Vendedor responsável:"
      , coerce=int
      , validators=[DataRequired(message="Selecione o vendedor")]
      , id="idusuario_vendedor_responsavel"
      , render_kw={"class": "form-control", "placeholder": "Selecione o vendedor responsável"}
   )

   # Descrição do contrato
   descricao = StringField(
      "Descrição:"
      , validators=[DataRequired(), Length(min=1, max=300)]
      , id="descricao"
      , render_kw={"class": "form-control", "placeholder": "Informe uma descrição do contrato"}
   )

   # Status do contrato (P, S, V, T, R, C)
   status = SelectField(
      "Status:"
      , choices=[("P", "Pendente"),("S", "Assinado"),("V", "Vigência"),("T", "Término"),("R", "Rescindido"),("C", "Cancelado")]
      , id="status"
      , validators=[DataRequired()]
      , render_kw={"class": "form-control", "placeholder": "Selecione o status do contrato"}
   )

   # Data de cadastro do contrato
   dt_cadatro = DateTimeField(
      "Data de cadastro:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_cadatro"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Data da assinatura do contrato
   dt_assinatura = DateTimeField(
      "Data da assinatura:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_assinatura"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Data da última atualização do contrato
   dt_atualizacao = DateTimeField(
      "Última atualização:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_atualizacao"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Início da vigência do contrato
   dt_inicial_vigencia = DateTimeField(
      "Início de vigência:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_inicial_vigencia"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )

   # Fim da vigência do contrato
   dt_final_vigencia = DateTimeField(
      "Final de vigência:"
      , format="%d/%m/%Y %H:%M:%S"
      , id="dt_final_vigencia"
      , render_kw={"class": "form-control", "placeholder": "dd/mm/aaaa hh:mm:ss"}
   )
