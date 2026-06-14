from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Pagina Inicial"

    @app.route("/sobre")
def sobre():
    return "Pagina Sobre"


@app.route("/livros")
def livros():
    return "Lista de Livros"


@app.route("/autores")
def autores():
    return "Lista de autores"

@app.route("/contato")
def contato():
    return "Pagina com erro"



if __name__ == "__main__":
    app.run(debug=True)
