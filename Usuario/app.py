from flask import Flask, json, request
from DataBase import Database
from usuario import Usuario

app = Flask(__name__)

@app.route("/cadastrar-usuario/", methods=["POST"])
def create():
    values = json.loads(request.data.decode("utf-8"))
    return Usuario().create(values)

@app.route("/atualizar-usuario/", methods=["PUT"])
def update():
    values = json.loads(request.data.decode("utf-8"))
    return Usuario().update(values)

@app.route("/listar-usuarios/")
def get_all():
    return Usuario().get_all()

@app.route("/usuario/")
def get_by_id():
    values = json.loads(request.data.decode("utf-8"))
    return Usuario().get_by_id(values)

@app.route("/deletar-usuario/", methods=["DELETE"])
def delete():
    values = json.loads(request.data.decode("utf-8"))
    return Usuario().delete(values)

if __name__ == "__main__":
    app.run(debug=True)