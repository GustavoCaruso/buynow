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