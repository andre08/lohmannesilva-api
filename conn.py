import mysql.connector

def Conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="DBFEATURESTORE"
    )