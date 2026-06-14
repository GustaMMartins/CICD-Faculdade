from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Pagina Inicial"

    @app.route("/sobre")
def sobre():
    return "Pagina Sobre"

