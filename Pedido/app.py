from flask import Flask
from DataBase import Database
from pedido import Pedido

app = Flask(__name__)

@app.route("/cadastrar-pedido/", methods=["POST"])
def create(self):
    values = json.loads(request.data.decode("utf-8"))
    return Pedido().create(values)

@app.route("/atualizar-pedido/", methods=["PUT"])
def update(self):
    values = json.loads(request.data.decode("utf-8"))
    return Pedido().update(values)

@app.route("/listar-pedidos/")
def get_all(self):
    return Pedido().get_all()

@app.route("/pedido/")
def get_by_id(self):
    values = json.loads(request.data.decode("utf-8"))
    return Pedido().get_by_id(values)

@app.route("deletar-pedido/", methods=["DELETE"])
def delete(self):
    values = json.loads(request.data.decode("utf-8"))
    return Pedido().delete(values)

if __name__ == "__main__":
    app.run(debug=True)