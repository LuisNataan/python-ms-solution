from DataBase.Database import DataBase as Db
from flask import Flask, request, json
from bson.json_util import loads, dumps
from uuid import uuid4
from datetime import datetime
import pandas as pd


class Usuario(Db):
    
    def create(self):
        
        try:
            sql = f"""INSERT INTO usuarios VALUES('{str(uuid4())[0:8]}', '{values['Nome']}', 
                                '{values['Cpf'].replace(".", "").replace("-", "")}',
                                '{values['Email']}', '{values['Fone']}', default, default)"""
            print(sql)
            self.cursor.execute(sql)
            return "Cadastrado com sucesso.", 201
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível cadastrar este usuário.", 400
    
    def update(self, dicio):
        sql_list = []
        
        for key, value in dicio.items():
            sql_list.append(f"{key}='{value}'")
        print(sql_list)
        
        try:
            self.cursor.execute(f"""UPDATE usuarios SET {','.join(sql_list)} WHERE Id = '{dicio['Id']}'""")
            
            return "Atualizado com sucesso.", 200
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível atualizar este usuário.", 400
    
    def get_all(self):
        self.cursor.execute(f"SELECT * FROM usuarios")
        columns = [i[0] for i in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
        
        return df.to_json(orient="records")
    
    def get_by_id(self, dicio):
        try:
            self.cursor.execute(f"SELECT * FROM usuarios WHERE Id= '{dicio['Id']}'")
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
            print(id)
            return df.to_json(orient="records")
            
        except Exception as Error:
            return str(Error.args)
        return "Id inexistente ou inválido.", 404
    
    def delete(self, dicio):
        try:
            self.cursor.execute(f"DELETE FROM usuarios WHERE Id = '{dicio['Id']}'")
            return "Deletado.", 204
        
        except Exception as Error:
            return str(Error.args)
        return "Usuario inexistente ou já deletado.", 400
