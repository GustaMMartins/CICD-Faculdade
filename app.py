from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Projeto Flask funcionando!"

@app.route("/sobre")
def sobre():
    return "Página sobre" 

if __name__ == "__main__":
    app.run(debug=True)

   