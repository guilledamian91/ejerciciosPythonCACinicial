import sqlite3
conexion=sqlite3.connect("bdadmlibreria.db")
cursor=conexion.execute("select * from articulos")
for fila in cursor:
    print(fila)
conexion.close()