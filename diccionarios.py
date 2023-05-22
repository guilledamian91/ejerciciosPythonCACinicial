from os import system
system ("cls")

dic1= {"cuadrado":4,"triangulo":3,"rectangulo":4,"hexagono":6,"rombo":4,}

dic2={4:["pepe",10], 2: (10,2,4),5: 42.98, 7:"hola!!",8:["pepe",10],10:["pepe",30]}

for clave in dic1.keys():
    print(clave)
print("")
for valor in dic1.values():
    print(valor)
    
print("")

for clave in dic2.keys():
    print (clave)

print("")

for valor in dic2.values():
    print(valor)
for clave,valor in dic1.items():
    print(clave,valor)
for clave, valor in dic2.items():
    print(clave,valor)

print(dic1["cuadrado"])
print(dic1.get("hexagono"))
print("")
print(dic2[4])
print(dic2.get(10))

dic1["cuadrado"] = 8
print(dic1["cuadrado"])
dic1["octagono"]=8
print(dic1["octagono"])

for clave, valor in dic1.items():
    print(clave,valor)
print("")
dic1.update({"cuadrado":4,"pentagono":5,"circulo":0})
print(dic1)
dic1.pop("cuadrado")
print("")
print(dic1)
dic2.clear()
print("")
print(dic2)

print("rombo" in dic1.keys())
print("decagono" in dic1.keys())

print(3 in dic1.values())
print(9 in dic1.values())