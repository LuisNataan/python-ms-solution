from DataBase.Database import DataBase as Db
from flask import Flask, request, json
from bson.json_util import loads, dumps
from uuid import uuid4
from datetime import datetime
import pandas as pd


class Usuario(Db):
    
    def create(self):
        values = json.loads(request.data.decode("utf-8"))
        try:
            self.cursor.execute(f"""INSERT INTO Usuarios VALUES('{str(uuid4())[0:8]}', '{values['Nome']}', 
                                '{values['Cpf'].replace(".", "").replace("-", "")}',
                                '{values['Email']}', '{values['Fone']}',
                                '{datetime.strftime(datetime.now(), '%d/%m/%Y  %H:%M:%S')}', '{'Never'}')""")
            return "Cadastrado com sucesso.", 201
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível cadastrar este usuário.", 400
    
    def update(self):
        values = json.loads(request.data.decode("utf-8"))
        sql_list = []
        
        for key, value in values['set'].items():
            sql_list.append(f"{key} = '{value}'")
        
        try:
            self.cursor.execute(f"""UPDATE Usuarios SET {', '.join(sql_list)},
                                Atualizado_em = '{datetime.strftime(datetime.now(), '%d/%m/%Y %H%M%S')}',
                                WHERE Id = '{value['Id']}'""")
            
            return "Atualizado com sucesso.", 200
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível atualizar este usuário.", 400
    
    def get_all(self):
        self.cursor.execute(f"SELECT * FROM Usuarios")
        columns = [i[0] for i in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
        
        return df.to_json(orient="records")
    
    def get_by_id(self, id):
        values = json.loads(request.data.decode("utf-8"))
        
        try:
            self.cursor.execute(f"SELECT * FROM Usuarios WHERE Id= {id}")
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetch_one(), columns=columns)
            
            return df.to_json(orient="records")
            
        except Exception as Error:
            return str(Error.args)
        return "Id inexistente ou inválido.", 404
    
    def delete(self, id):
        values = json.loads(request.data.decode("utf-8"))
        
        try:
            self.cursor.execute(f"DELETE * FROM Usuarios WHERE Id = {id}")
            return "Deletado.", 204
        
        except Exception as Error:
            return str(Error.args)
        return "Usuario inexistente ou já deletado.", 400
