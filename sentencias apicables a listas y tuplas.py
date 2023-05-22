# sentencias apicables a listas y tuplas
from os import system
system ("cls")

paises=["Perú", "Chile","Argentina", "Bolivia"]
print (paises[:]) #imprime toda la lista
print (paises) # imprime toda la lista

paises.extend (["Ecuador", "Colombia", "Venezuela"]) # agrega elementos a la lista
print(paises)
print(paises[0]) # imprime el primer elemento de la lista
print(paises[3]) # imprime el 4 elemento de la lista

print(paises [-6]) # indice negativo cuenta de atras para adelante muestra en segundo elemento
print(paises[0:3]) # imprime desde el indice 0 hasta la posicion 3
print(paises[3:6]) # imprime desde el indice 3 hasta la posicion 7
print(paises[:4]) # imprime desde el indice 0 hasta la posicion 4
print(paises[4:]) # imprime desde el indice 4 hasta el final de la lista

paises.append("Brasil") #agrega un elemento al final de la lista
print(paises)
paises.insert(3, "Uruguay") #agrega a la posicion 3
print(paises[:])
print(f"Chile se encuentra en el indice", paises.index("Chile")) #imprimimos el indice del elemento Chile 

print("¿Esta brasil en la lista?") 
if "Brasil" in paises : # imprimimos true si brasil se enecuentra en la lista
    print ("si esta")
else:
    print ("no esta")    
print(paises [:])

paises.remove ("Brasil") # eliminamos un elemento de la lista
if "Brasil" in paises : # imprimimos true si brasil se enecuentra en la lista
    print ("si está")
else:
    print ("no está") 
print(paises [:])

datos_varios= ["Perú", 1 , 1.5 , True]
print (datos_varios [:])
paises.pop()# eliminamos un elemento 
print(paises[:])

Lista_Nueva= paises+datos_varios #concatenamos ambas listas en una
print (Lista_Nueva[:])
print (paises[2], paises [5]) #imprime los elementos de los indices 2 y 5