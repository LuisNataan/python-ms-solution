from flask import Flask
from DataBase import Database
from pedido import Pedido

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)