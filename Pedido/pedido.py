from DataBase.Database import DataBase as Db
from flask import Flask, request, json
from uuid import uuid4
from datetime import datetime
import pandas as pd

class Pedido(Db):
    
    def create(self, dicio):
        valor_total = f"{values['Quantidade']*values['Preco']}"

        try:
            self.cursor.execute(f"""INSERT INTO pedidos VALUES ({str(uuid4())[0:8]},
                                {values['Id_Usuario']}, {values['Descricao']}, 
                                {values['Quantidade']}, {values['Preco']},
                                {values['valor_total']}, default, default)""")
            
            return "Pedido realizado.",
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível realizar este pedido.", 400
    
    def update(self, dicio):
        sql_list = []
        
        for key, value in dicio.items():
            sql_list.append(f"{key}='{value}'")
        
        try:
            self.cursor.excecute(f"""UPDATE pedidos SET {', '.join(sql_list)}
                                 WHERE Id= '{dicio['Id']}'""")
            
            return "Atualizado com sucesso.", 200
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível atualizar.", 400
    
    def get_all(self):
        self.cursor.excecute("SELECT * FROM pedidos")
        columns = [i[0] for i in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
        
        return df.to_json(orient="records")
    
    def get_by_id(self, dicio):
        try:
            self.cursor.excecute(f"SELECT * FROM pedidos WHERE Id = {dicio['Id']}")
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
            
            return df.to_json(orient="records")
        
        except Exception as Error:
            return str(Error.args)
        return "Id inexistente ou inválido.", 404
    
    def delete(self, dicio):
        try:
            self.cursor.excecute(f"DELETE FROM pedidos WHERE Id = {dicio['Id']}")
            return "Deletado.", 204
            
        except Exception as Error:
            return str(Error.args)
        return "Pedido inexistente ou já deletado.", 400
    