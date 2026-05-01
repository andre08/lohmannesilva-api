# Importando bibliotecas
from flask import Flask, render_template, session, redirect, url_for, request, Blueprint
from flask_cors import CORS
from flask_wtf import CSRFProtect
import pyodbc
import traceback
from datetime import timedelta
import json

from conn import Conectar
from models.historicoacesso import HistoricoAcesso
from services.historicoacesso_service import historico_acesso_salvar_novo

# Importando rotas do front-end
from routes_web.routes_web_arquivo import routes_web_arquivo
from routes_web.routes_web_atalho import routes_web_atalho
from routes_web.routes_web_contato import routes_web_contato
from routes_web.routes_web_contrato import routes_web_contrato
from routes_web.routes_web_empresa import routes_web_empresa
from routes_web.routes_web_empresausuario import routes_web_empresausuario
from routes_web.routes_web_estudo import routes_web_estudo
from routes_web.routes_web_fatura import routes_web_fatura
from routes_web.routes_web_historicoacesso import routes_web_historicoacesso
from routes_web.routes_web_itemfatura import routes_web_itemfatura
from routes_web.routes_web_plano import routes_web_plano
from routes_web.routes_web_processo import routes_web_processo
from routes_web.routes_web_processoestudo import routes_web_processoestudo
from routes_web.routes_web_registro import routes_web_registro
from routes_web.routes_web_relatorio import routes_web_relatorio
from routes_web.routes_web_token import routes_web_token
from routes_web.routes_web_usuario import routes_web_usuario

# Importando rotas da API
#from routes_api.routes_api_usuario import routes_api_usuario

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'
app.permanent_session_lifetime = timedelta(minutes=15)
csrf = CSRFProtect(app)
CORS(app)

interceptador = Blueprint('interceptador', __name__)

# Registrando as rotas para os modulos WEB
app.register_blueprint(routes_web_arquivo, url_prefix='/arquivo/')
app.register_blueprint(routes_web_atalho, url_prefix='/atalho/')
app.register_blueprint(routes_web_contato, url_prefix='/contato/')
app.register_blueprint(routes_web_contrato, url_prefix='/contrato/')
app.register_blueprint(routes_web_empresa, url_prefix='/empresa/')
app.register_blueprint(routes_web_empresausuario, url_prefix='/empresausuario/')
app.register_blueprint(routes_web_estudo, url_prefix='/estudo/')
app.register_blueprint(routes_web_fatura, url_prefix='/fatura/')
app.register_blueprint(routes_web_historicoacesso, url_prefix='/historicoacesso/')
app.register_blueprint(routes_web_itemfatura, url_prefix='/itemfatura/')
app.register_blueprint(routes_web_plano, url_prefix='/plano/')
app.register_blueprint(routes_web_processo, url_prefix='/processo/')
app.register_blueprint(routes_web_processoestudo, url_prefix='/processoestudo/')
app.register_blueprint(routes_web_registro, url_prefix='/registro/')
app.register_blueprint(routes_web_relatorio, url_prefix='/relatorio/')
app.register_blueprint(routes_web_token, url_prefix='/token/')
app.register_blueprint(routes_web_usuario, url_prefix='/usuario/')

# Registrando as rotas para os modulos API
#app.register_blueprint(routes_api_usuario, url_prefix='/api')

# Lista de rotas que não são necessárias para login
rotasWebPublicas = [''
                    , None
                    ,'/'
                    , 'static'
                    , 'home'
                    , 'routes_web_contato.rota_contato_registrar_contato', 'routes_web_contato.rota_contato_salvar_novo'
                    , 'routes_web_usuario.rota_usuario_login', 'routes_web_usuario.rota_usuario_logon', 'routes_web_usuario.rota_usuario_logoff'
                    , 'routes_web_usuario.rota_usuario_registro', 'routes_web_usuario.rota_usuario_salvar_novo_publico'
                ]

# Interceptando as rotas para identificar uma rota restrita
@app.before_request
def verifica_rota_restrita():
    # recuperando a rota selecionada
    rota_solicitada = request.endpoint
    # verificando se é uma rota publica ou restrita, sendo restrita preciso estar autenticado
    if (rota_solicitada not in rotasWebPublicas):
        # verificando se a sessão está atutencidada
        if ('autenticado' not in session):
            # caso não seja atutenticado é redirecionado para o login
            return redirect(url_for('routes_web_usuario.rota_usuario_login'))
            
# Interceptando as rotas para gravar no log
@interceptador.before_app_request
def registra_rota():
    # recuperando a rota selecionada
    rota_solicitada = request.endpoint

    if (rota_solicitada not in ['/', None, 'home', 'static', 'routes_web_usuario.rota_usuario_salvar_novo']):

        # registrando acesso da rota
        method = request.method
        path = request.path
        full_url = request.url
        query = request.query_string.decode('utf-8')
        json_data = request.get_json(silent=True)
        json_data = json.dumps(json_data, ensure_ascii=False) if json_data else None
        form_data = request.form.to_dict() if request.form else None
        form_data = json.dumps(form_data, ensure_ascii=False) if form_data else None
        remote_addr = request.remote_addr
        
        # Raw body como fallback
        raw_body = None
        if not json_data and not form_data:
            raw_body = request.get_data(cache=True, as_text=True)

        if ('usuario_id' in session):
            idusuario = session["usuario_id"]
        else:
            idusuario = None

        log_msg = (
            f"USER: {idusuario} | "
            f"IP: {remote_addr} | "
            f"Method: {method} | "
            f"Path: {path} | "
            f"Full URL: {full_url} | "
            f"Query: {query} | "
            f"json_data: {json_data} | " 
            f"Form: {form_data}"
            f"raw_body: {raw_body}"            
        )

        #salvando historico de acesso
        sucesso, resultado, mensagem = historico_acesso_salvar_novo(HistoricoAcesso(None, idusuario, rota_solicitada, method, remote_addr, path, full_url, query, form_data, json_data))

app.register_blueprint(interceptador)

# Página personalizada para erro 404
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

# Tratamento de erro 500 (erro interno do servidor)
@app.errorhandler(500)
def erro_interno(error):
    mensagem = str(error)
    tb_mensagem = traceback.format_exc()
    return render_template("500.html", erro=mensagem, tb=tb_mensagem), 500

# rota para a pagina principal
@app.route('/')
def home():
    return render_template('index.html')

# rota para o panel de administração
@app.route('/admin')
def admin():
    return render_template('admin.html')

#iniciando a aplicação
if __name__ == "__main__":
    app.run(debug=True)
