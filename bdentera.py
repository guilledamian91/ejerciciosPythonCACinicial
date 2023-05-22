import sqlite3
conexion=sqlite3.connect("basededatos4.db")
conexion.execute("""create table if not exists articulos (codigo integer primary key AUTOINCREMENT, descripcion text, precio real)""")
# conexion.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER, email TEXT)")


conexion=sqlite3.connect("basededatos4.db")
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('Vasos', 75))
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('platos', 127))
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('cubiertos', 107))
conexion.commit()


conexion=sqlite3.connect("basededatos4.db")
cursor=conexion.execute("select * from articulos")
for fila in cursor:
    print(fila)


conexion.close()