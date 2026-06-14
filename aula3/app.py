from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo à Aula 3"

@app.route("/sobre")
def sobre():
return "Exemplo de API Flask para CI/CD"

@app.route("/status")
def status():
    return {
        "status": "online",
        "aplicacao": "Aula 3"
    }

if __name__ == "__main__":
    app.run(debug=True)