from os import system
system ("cls")

# lista_nombres=['Alicia','Pablo','Juan','Pedro']

# contenido = open("C:/Users\guill\OneDrive\Escritorio\ejercicios pyhton\misDAtos.txt","w")
# for nombre in lista_nombres:
#     contenido.write(nombre + "\n")
# contenido.close

# lista_nombres=['Luciana','Celeste','Natalia','Lautaro']

# contenido = open("C:/Users\guill\OneDrive\Escritorio\ejercicios pyhton\misDAtos.txt","a")
# for nombre in lista_nombres:
#     contenido.write(nombre + "\n")
# contenido.close

print("ahora lo abrimos!")
contenido= open("misDatos.txt","r")

contador = 1
for linea in contenido:
    print("Linea", contador, ":", linea)
    contador = contador + 1
contenido.close()

