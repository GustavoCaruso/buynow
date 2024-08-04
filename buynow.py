
from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

# Criação da rota
@app.route("/")
def index():
    return render_template('index.html')

# Criação da rota
@app.route("/sobre")
def sobre():
    return "<h1>Loja virtual para compra e venda de produtos.</h1>"

# Criação da rota
@app.route("/user/<username>")
def username(username):
    cok = make_response("<h2>cookie criado</h2>")
    cok.set_cookie('username', username)
    return cok


# @app.route("/teste")
# def teste():
#     return render_template('index.html')

@app.route("/user2/")
@app.route("/user2/<username>")
def username2(username=None):
    cokusername = request.cookies.get('username')
    return render_template('user.html', username=username, cokusername=cokusername)

@app.route("/cad/usuario")
def usuario():
    return render_template('usuario.html', titulo="Cadastro de Usuário")

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form

@app.route("/cad/anuncio")
def anuncio():
    return render_template('anuncio.html')

@app.route("/anuncio/pegunta")
def pergunta():
    return render_template('pergunta.html')


@app.route("/anuncios/compra")
def compra():
    print("anuncio comprado")
    return ""

@app.route("/anuncio/favoritos")
def favoritos():
    print("favorito inserido")
    return ""

@app.route("/config/catgeoria")
def categoria():
    return render_template('categoria.html')


@app.route("/relatorios/vendas")
def relVendas():
    return render_template('relVendas.html')

@app.route("/relatorios/compras")
def relCompras():
    return render_template('relCompras.html')