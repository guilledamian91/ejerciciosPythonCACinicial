from os import system
system("cls")

print("MENU DE OPCIONNES")
print("1. Ventas")
print("2. Pagos")
print("3. Servicio Técnico")
print("4. Gerencia")
i=0
while i < 3:
    num= (input("Ingrese una opcion; \n"))
    match num.lower() :
        case 1:
         print ("Elegiste ventas")
        case 2:
            print ("Elegiste pagos")
        case 3:
            print("Elegiste servicio técnico")
        case 4:
            print("Elegiste gerencia")
        case _:
            print("Opción no válida")