from flask import Flask
from DataBase import Database
from pedido import Pedido

app = Flask(__name__)

@app.route("/cadastrar-pedido/", methods=["POST"])
def create(self):
    return Pedido().create()

@app.route("/atualizar-pedido/<id>", methods=["PUT"])
def update(self):
    return Pedido().update(id)

@app.route("/listar-pedidos/")
def get_all(self):
    return Pedido().get_all()

@app.route("/pedido/<id>")
def get_by_id(self):
    return Pedido().get_by_id(id)

@app.route("deletar-pedido/<id>", methods=["DELETE"])
def delete(self):
    return Pedido().delete(id)

if __name__ == "__main__":
    app.run(debug=True)