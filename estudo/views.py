from estudo import app
from flask import render_template, url_for

@app.route('/')
def homePage():
    usuario = "Neto"
    return render_template('index.html', usuario=usuario)

@app.route("/dados")
def dados():
    return "Dados do servidor"