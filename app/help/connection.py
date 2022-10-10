import mysql.connector
from mysql.connector import Error
import json

f = open('secrets.json')

data = json.load(f)

#classe que faz a conexão com o banco de dados
class Connection:

    """
        Método responsável por estabelecer a conexão com o banco de dados.
        return: cursor -> o cursor do nosso console mySql, pelo qual podemos inserir dados.
    """
    def conn():
        try:
            connection = mysql.connector.connect(host=data['host'],
                                                 database=data['database'],
                                                 user=data['user'],
                                                 password=data['password'])
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)