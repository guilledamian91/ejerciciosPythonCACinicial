def Menu():
    import os
    print("Menú Principal Veterinaria Pichichus")
    print("------------------------------------")
    print("0. Crear base de datos (Solo 1 vez)")
    print("1. Ingresar una nueva mascota")
    print("2. Cambiar datos de una mascota")
    print("3. Eliminar una mascota")
    print("4. Buscar datos de una mascota")
    print("5. Listar todas las mascotas")
    print("6. Salir")
    try:
        opcion=int(input("Ingrese una opcion: "))
    except ValueError:
        print("Opcion incorrecta")
        os.system("pause")
        os.system("cls")
        Menu()
    if opcion == 0:
        crearBD()
    elif opcion == 1:
        ingresarMAscota()
    elif opcion == 2:
        cambiarDatos ()
    elif opcion == 3:
        eliminarMAscota()
    elif opcion == 4:
        buscarMascota()
    elif opcion == 5:
        listarMascotas()
    elif opcion == 6:
        salir()
    else:
        print("Ingrese una opcion válida")
        print("--------------------------------")
        Menu()

def crearBD():
    import os, sqlite3
    con=sqlite3.connect("veterinaria.db")
    con.execute("CREATE TABLE if not exists mascotas (id integer primary key AUTOINCREMENT, Nombre TEXT, Edad TEXT, Raza TEXT, Peso TEXT, Dueño TEXT)")
    con.commit()
    con.close()
    print("Base de datos creada con exito")
    print("-------------------------------")
    os.system("pause")
    Menu()

def ingresarMAscota():
    import os, sqlite3
    con=sqlite3.connect("veterinaria.db")
    print("Ingresar nueva mascota")
    print("-------------------------------")
    nombre=input("Ingrese nombre de la mascota: ")
    edad=input("Ingrese la edad de la mascota: ")
    raza=input("Ingrese la raza de la mascota: ")
    peso=input("Ingrese el peso de la mascota: ")
    dueño=input("ingrese el nombre del dueño: ")
    os.system("cls")
    cursor=con.cursor()
    cursor.execute("INSERT INTO mascota (Nombre, Edad, Raza, Peso, Dueño) VALUES (?,?,?,?,?)",(nombre,edad,raza,peso,dueño))
    con.commit()
    con.close()
    print("Mascota ingresada con exito")
    print("-------------------------------")
    os.system("pause")
    Menu()

def cambiarDatos():
    import os, sqlite3
    i=0
    i=int(buscarMascota())
    con= sqlite3.connect("veterianaria.db")
    cursor=con.cursor()
    os.system("cls")
    print("\n\n\t\t¿que datos desea modificar?\n\n\t\t")
    print("1.Nombre de la mascota")
    print("2.Edad de la mascota: ")
    print("3.Raza de la mascota: ")
    print("4.Peso de la mascota: ")
    print("5.Nombre del dueño de la mascota: ")
    print("6.Volver al menu principal")
    print("-------------------------------")
    opcion = int(input(""))
    if opcion == 1:
        opcion = input ("Defina nuevo nombre de la mascota")
        cursor.execute("UPDATE mascotas SET Nombre = ? Where id = ?", (opcion,i))
    elif opcion == 2:
        opcion = input ("Defina nuevo Edad de la mascota")
        cursor.execute("UPDATE mascotas SET Edad = ? Where id = ?", (opcion,i))
    elif opcion == 3:
        opcion = input ("Defina nueva Raza de la mascota")
        cursor.execute("UPDATE mascotas SET Raza = ? Where id = ?", (opcion,i))
    elif opcion == 4:
        opcion = input ("Defina nuevo Peso de la mascota")
        cursor.execute("UPDATE mascotas SET Peso = ? Where id = ?", (opcion,i)) 
    elif opcion == 5:
        opcion = input ("Defina nuevo nombre del dueño de la mascota")
        cursor.execute("UPDATE mascotas SET Dueño = ? Where id = ?", (opcion,i))
    elif opcion == 6:
        Menu()
    else:
       print("selecciono una opcion incorrecta, reintente")
       os.system("pause")
       cambiarDatos() 
    print("Datos actualizados correctamente\n")
    os.system("pause")
    con.commit()
    con.close()
    Menu()

def eliminarMAscota():
    i=0
    i=int(buscarMascota())
    import os, sqlite3
    con=sqlite3.connect("veterianaria.db")
    cursor=con.cursor()
    os.system("cls")
    cursor.execute("DELETE FROM mascotas WHERE id=?",str(i))
    con.commit()
    con.close()
    print("\n\n\t\tLa mascota ha sido eliminada\n\n\t\tSerá redirigido al menu principal")
    os.system("pause")
    Menu()

def buscarMascota():
    import os, sqlite3
    con= sqlite3.connect("veterianaria.db")
    cursor=con.cursor()
    os.system("cls")
    print("Meú buscar mascota")
    print("-------------------------------")
    nombre=input("Ingresar nombre de la mascota: ")
    dueño=input("Ingresar nombre del dueño: ")
    
    cursor.execute("SELECT * FROM mascota WHERE Nombre=? AND Dueño=?", [nombre, dueño])
    variable=cursor.fetchone()
    if variable != None:
        print("se ha encontrado exitosamente")
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("","","","","","",""))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("iD","Nombre","Edad","Raza","Peso","Nombre dueño"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("","","","","","",""))
        for t in variable:
            print("|{:-<20}",format(t), end="")
        print("")
        os.system("pause")
    else:
        print("No se ha encontrado la mascota")
        os.system("pause")
        Menu()
    print("\n")
    con.commit()
    con.close()
    z=int(variable[0])
    return(z)
    

def listarMascotas():
    import os, sqlite3
    os.system("cls")
    con=sqlite3.connect("veterianaria.db")
    cursor=con.cursor()
    cursor.execute("select * from mascotas")
    elementos=cursor.fetchall()
    imprimirToda(elementos)
    con.close()
    Menu()

def salir():
    import os
    print("Gracias por utilizar el programa")
    os.system("pause")
    os.system("cls")
    exit()

def imprimirToda(elementos):
    import os
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("","","","","","",""))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("iD","Nombre","Edad","Raza","Peso","Nombre dueño"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("","","","","","",""))
    for id, Nombre, Edad, Raza, Peso, Dueño in elementos:
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("iD","Nombre","Edad","Raza","Peso","Nombre dueño"))
    os.system ("pause")

Menu()