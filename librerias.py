from os import system # Importamos la función system de la librería os con el 2do y 4 método
system("cls")

import os    # Importamos el modulo os con el primer metodo
os.system ("cls")

from random import randint as rnd
from math import pi, e
lanzamiento = rnd(1, 6)
if lanzamiento < 4:
    print(pi* lanzamiento)
    print(lanzamiento)
else:
    print(e * lanzamiento)
    print(lanzamiento)