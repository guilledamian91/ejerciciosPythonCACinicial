from os import system
system("cls")

# def holaclase():
#     print("hola clase")
    
# holaclase()
# b=0+7
# a=5+4
# print(a)

# print(b)

# print(type(holaclase))


# def suma(num1, num2):
#     resultado = num1 + num2
#     return resultado

# almacena_resultado = suma (5,7)
# print(almacena_resultado)

# print("hola mundo")
# def imprimir_suma():
#     a=5
#     b=6
#     z=a+b
#     print(z)
# imprimir_suma ()
# print("adios mundo")

# def saludo():
#     print("hola mundo")

# def repite_saludo():
#     saludo()
#     saludo()
    
# repite_saludo()

# ARGUMENTOS NOMBRADOS

# def saludar (nombre, profesion, edad=25, dni=1234567, nacionalidad="Argentina"):
#     print(f"Hola {nombre}, tu profesion es; {profesion}. tu edad es {edad}, tu dni es: {dni}, tu nacionalidad es: {nacionalidad}")

# CALCULOS EN FUNCIONES

# def doblarNumero(nro):
#     nro= nro*2
#     return nro

# miNumero = 3
# print(doblarNumero(miNumero))
# print(miNumero)

# def doblarNumeros2(nros):
#     for indice in range(len(nros)):
#         nros[indice] = nros[indice] * 2
#     return nros
# miNumeros =[10,20,5]
# print(doblarNumeros2(miNumeros))
# print(miNumeros)

# FUNCION CON REFERENCIA DICCIONARIO
 
# def CapitalizarProductos (productos):
#     for codigo in productos.keys():
#         productos[codigo] = productos[codigo].capitalize()

# datosProductos={
#     22345: "teclado",
#     22346: "mouse",
#     22347: "notebook",
#     22348: "monitor"
# }

# CapitalizarProductos(datosProductos)
# print(datosProductos)

# FUNCION DECORATIVA

def decorar():
    print("#"*50)
    print("."*50)
    print("#"*50)

while True:
    decorar()
    print('''
    \t ::: Menu:::
    [1] Cargar usuarios
    [2] Mostrar usuarios
    [3] Mostar listado de trabajadores activos
    [4] Mostar usuarios por profesion
    [5] Mostar usuarios por edad
    [0] Salir
        ''')
    decorar()
    opcion = int(input("seleccione una pocion " ))
    if opcion == 0:
      break
    elif opcion == 1:
        print ("Cargar usuarios")
    elif opcion == 2:
        print ("Mostar usuarios")
    elif opcion == 3:
        print ("Mostar listado de trabajadores activos")
    elif opcion == 4:
        print ("Mostar usuarios por profesion")
    elif opcion == 5:
        print ("Mostar usuarios por edad")
    else:
        print("Ingresa una opcion valida")

print ("Fin!!!")       
    