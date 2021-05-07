from DataBase.Database import DataBase as Db
from flask import Flask, request, json
from uuid import uuid4
from datetime import datetime
import pandas as pd

class Pedido(Db):
    
    def create(self):
        values = json.loads(request.data.decode("utf-8"))
        try:
            self.cursor.execute(f"""INSERT INTO Pedidos VALUES ({str(uuid4())[0:8]},
                                {values['Id_Usuario']}, {values['Descricao']}, 
                                {values['Quantidade']}, {values['Preco']},
                                {values['Quantidade']*values['Preco']},
                                {datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')}, "Never")""")
            return "Pedido realizado.",
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível realizar este pedido.", 400
    
    def update(self, id):
        values = json.loads(request.data.decode("utf-8"))
        sql_list = []
        
        for key, value in values['set'].items():
            sql_list.append(f"{key} = '{value}'")
        
        try:
            self.cursor.excecute(f"""UPDATE Pedidos SET {', '.join(sql_list)},
                                 Atualizado_em = '{datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')}',
                                 WHERE Id= '{value['Id']}'""")
            return "Atualizado com sucesso.", 200
            
        except Exception as Error:
            return str(Error.args)
        return "Não foi possível atualizar.", 400
    
    def get_all(self):
        self.cursor.excecute("SELECT * FROM Pedidos")
        columns = [i[0] for i in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
        
        return df.to_json(orient="records")
    
    def get_by_id(self, id):
        values = json.loads(request.data.decode("utf-8"))
        
        try:
            self.cursor.excecute(f"SELECT * FROM Pedidos WHERE Id = {id}")
        
        except Exception as Error:
            return str(Error.args)
        return "Id inexistente ou inválido.", 404
    
    def delete(self, id):
        values = json.loads(request.data.decode("utf-8"))
        
        try:
            self.cursor.excecute(f"DELETE * FROM Pedidos WHERE Id = {id}")
            return "Deletado.", 204
            
        except Exception as Error:
            return str(Error.args)
        return "Pedido inexistente ou já deletado.", 400
    