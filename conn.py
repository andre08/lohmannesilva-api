#import mysql.connector

#def Conectar():
#    return mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="123456",
#        database="DBFEATURESTORE"
#    )

import pyodbc

connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:dw-powerbi.database.windows.net,1433;Database=app-feature-store;Uid=adminsitrador;Pwd=Lohmann@Silva2023;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
def Conectar():
    return pyodbc.connect(connection_string)