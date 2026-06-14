from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo à Aula 4"

@app.route("/sobre")
def sobre():
    return "Exemplo de API Flask para o CI/CD"

@app.route("/status")
def status():
    return {
        "status": "online",
        "aplicacao": "Aula 4"
    

if __name__ == "__main__":
    app.run(debug=True)