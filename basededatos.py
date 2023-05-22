import sqlite3

conexion=sqlite3.connect("bdadmlibreria.db")
conexion.execute("""create table if not exists articulos (codigo integer primary key AUTOINCREMENT, descripcion text, precio real)""")
# conexion.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER, email TEXT)")

conexion.close()