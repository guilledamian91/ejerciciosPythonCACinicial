from argparse import BooleanOptionalAction
from os import system  
system ("cls")

class Miclase:
    x=5

prueba1=Miclase()
print(prueba1.x)

class Automovil:
    pintura =  "blanco"
    precio = 10000
    marca="Ford"
    motor= "V6"
    modelo ="Fiesta"
    cubiertas="Michelin"
    def acelerar(self):
        print("Acelerando")  
    def frenar(self):
        print("Frenando")
    def girarderecha(self):
        print("Girando a la derecha")
    def girarizquierda(self):
        print("Girando a la izquierda")  
auto1=Automovil()
print(auto1.pintura)
auto1.precio=15000
print(auto1.precio)
print(auto1.cubiertas)
auto1.modelo = "Focus"
print(auto1.modelo)

argumento_1 = auto1.precio
precio_mas_iva = argumento_1*1.21 
print(precio_mas_iva)

auto1.acelerar()
auto1.frenar()
auto1.girarderecha()
auto1.girarizquierda()