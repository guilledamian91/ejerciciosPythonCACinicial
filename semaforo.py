from os import system
system ("cls")

color = input(f"Ingrese color de semaforo (v/a/r) ")
while True :
    if color == "v" :
        print("pase tranquilo")
    else:
        if color == "a" :
            print("Espere por favor")
        else:
            if color == "r" :
                 print ("pare!")
            else:
                print("¡debe ingresar v/a/r!")
    break
