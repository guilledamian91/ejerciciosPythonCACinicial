from os import system
system ("cls")

persona={"nombre":[], "apellido":[], "edad":[]}
for i in range (3):
    persona["nombre"].append(input("Ingrese nombre: "))
    persona["apellido"].append(input("Ingrese apellido: "))
    persona["edad"].append(int(input("ingrese edad: ")))
    
for i in range(3):
    print(persona["nombre"][i],", ",persona ["apellido"][i],", ",persona["edad"][i])