from flask import Flask
from DataBase import Database
from usuario import Usuario

app = Flask(__name__)

@app.route("/cadastrar-usuario/", methods=["POST"])
def create(self):
    return Usuario().create()

@app.route("/atualizar-usuario/<id>", methods=["PUT"])
def update(self):
    return Usuario().update()

@app.route("/listar-usuarios/")
def get_all(self):
    return Usuario().get_all()

@app.route("/usuario/<id>")
def get_by_id(self):
    return Usuario().get_by_id(id)

@app.route("/deletar-usuario/<id>")
def delete(self):
    return Usuario().delete(id)

if __name__ == "__main__":
    app.run(debug=True)