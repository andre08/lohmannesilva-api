#import mysql.connector

#def Conectar():
#    return mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="123456",
#        database="DBFEATURESTORE"
#    )

import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env

connection_string = (
     "Driver={ODBC Driver 18 for SQL Server};"
    f"Server={os.getenv('DB_SERVER')};"
    f"Database={os.getenv('DB_NAME')};"
    f"Uid={os.getenv('DB_USER')};"
    f"Pwd={os.getenv('DB_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

def Conectar():
    return pyodbc.connect(connection_string)

