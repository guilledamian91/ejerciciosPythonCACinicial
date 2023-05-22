import sqlite3
conexion = sqlite3.connect("bdadmlibreria.db")
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('lapicera', 75))
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('cuaderno', 127))
conexion.execute("insert into articulos (descripcion, precio) values (?,?)", ('felpa', 107))
conexion.commit()
conexion.close()