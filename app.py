# Importando bibliotecas
from flask import Flask, render_template, session, redirect, url_for, request
from flask_cors import CORS
import traceback
from conn import Conectar

# Importando rotas do front-end
from routes_web.routes_web_contato import routes_web_contato
from routes_web.routes_web_usuario import routes_web_usuario
#from routes_web.routes_web_token import routes_web_token

# Importando rotas da API
#from routes_api.routes_api_usuario import routes_api_usuario

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'
CORS(app)

# Registrando as rotas para os modulos WEB
app.register_blueprint(routes_web_contato, url_prefix='/contato/')
app.register_blueprint(routes_web_usuario, url_prefix='/')
#app.register_blueprint(routes_web_token, url_prefix='/')

# Registrando as rotas para os modulos API
#app.register_blueprint(routes_api_usuario, url_prefix='/api')

# Lista de rotas que não são necessárias para login
rotasWebPublicas = ['/'
                 , 'home'
                 , 'routes_web_contato.registrar_contato', 'routes_web_contato.salvar_contato', 'routes_web_contato.listar_contato'
                 , 'routes_web_usuario.login', 'routes_web_usuario.logon', 'routes_web_usuario.registro', 'routes_web_usuario.nova_conta'
                 , 'static']

# Interceptando as rotas para identificar uma rota restrita
@app.before_request
def verifica_rota_restrita():
    rota_solicitada = request.endpoint
    if (rota_solicitada not in rotasWebPublicas):
        if ('autenticado' not in session):
            return redirect(url_for('routes_web_usuario.login'))
        else:
            print(rota_solicitada)

# Página personalizada para erro 404
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404  # ou apenas return "<h1>Página não encontrada</h1>", 404

# Tratamento de erro 500 (erro interno do servidor)
@app.errorhandler(500)
def erro_interno(error):
    mensagem = str(error)
    tb_mensagem = traceback.format_exc()
    return render_template("500.html", erro=mensagem, tb=tb_mensagem), 500

# rota para a pagina principal
@app.route('/')
def home():
    conexao_db = False
    try:
        conn = Conectar()
        cur = conn.cursor()
        cur.close()
        conn.close()
        conexao_db = True
    except:
        conexao_db = False
    
    return render_template('index.html', conexao_db=conexao_db)

# rota para o panel de administração
@app.route('/admin')
def admin():
    return render_template('admin.html')

#iniciando a aplicação
if __name__ == "__main__":
    app.run(debug=True)
