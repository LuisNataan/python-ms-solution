from DataBase.Database import DataBase as Db
from flask import Flask, request, json
from bson.json_util import loads, dumps
from uuid import uuid4
from datetime import datetime
import pandas as pd

class Pedido(Db):
    
    def create(self):
        pass
    
    def update(self, id):
        pass
    
    def get_all(self):
        pass
    
    def get_by_id(self, id):
        pass
    
    def delete(self, id):
        pass
    