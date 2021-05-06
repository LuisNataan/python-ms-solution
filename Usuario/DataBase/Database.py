import MySQLdb as sql

class DataBase:
    
    def __init__(self):
        self.connection = sql.connect(db="python-ms_db", user="root", host="localhost", port=3306)
        self.connection.autocommit(True)
        self.cursor = self.connection.cursor()
