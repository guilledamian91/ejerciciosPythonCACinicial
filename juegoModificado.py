#MENU DE JUEGOS

# creado por
#     Guillermo Perez Maidana
#     Paula Carolina Serrano
#     Manuel Elias Rodriguez
#     Lucas Pasesrini

from os import system
system("cls")
import random

def juegodados():
    from random import randint
    dadosUsuario =[]
    totalUsuario = 0
    dadoParEncontrado = 0
    partidaActual = 1
    while partidaActual <= 5:
        print(f'..:: RONDA # {partidaActual} ::..')
        tirarDados = input("Tirar los dados (s/n): ")
        if tirarDados == "n":
         print("Dale tira esos dados!!!")
         continue
        
        for i in range (5): 
            dadosUsuario.append(randint(1,6))
        print("Sus dados: ", dadosUsuario)
        puntajeUsuario = 0
        trio= 0
        par1 = 0
        par2 = 0

        for dado in dadosUsuario:
         if dadosUsuario.count(dado) == 5:
            print (f"sacaste 5 vedes ek dado: {dado}")
            puntajeUsuario= puntajeUsuario + 15
         elif dadosUsuario.count(dado) == 4:
                print(f"Sacaste 4 veces el dado: {dado}")
                puntajeUsuario = puntajeUsuario + 10
         elif dadosUsuario == 3:
              if trio == 0:
               print(f"Sacaste 3 vecesw el dado: {dado}")
               trio= dado
         elif dadosUsuario.count(dado) == 2:
              if par1 == 0:
               print  (f"Sacaste un par de: {dado}")
               par1 = dado
              elif par1 != dado and par2 == 0:
               print(f"Sacaste un par de : {dado}")
               par2= dado
            
        if par1 != 0 and par2 !=0:
            print(">>> Doble par!! +5")
            puntajeUsuario = puntajeUsuario + 5
        elif par1 != 0 or par2 != 0:
            if trio !=0:
             print(f">>> Full!! +9")
             puntajeUsuario = puntajeUsuario + 9
            else:
              print(f">>> Par simple +2")
              puntajeUsuario = puntajeUsuario +2
        else:
            if trio !=0:
             print(f">>> trio de {trio} + 6")
            puntajeUsuario = puntajeUsuario + 6

        totalUsuario = totalUsuario + puntajeUsuario
        print(
        f'''
        Puntaje en esta tirada: {puntajeUsuario}
        ## MArcador general {totalUsuario} ###
        ''')

        partidaActual = partidaActual+ 1
        dadosUsuario.clear()
  

def mastermind():
    # el conjunto de simbolos validos en el codigo*
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    # "elegimos" el codigo
    cant_digitos = 5
    codigo = ''
    for i in range(cant_digitos):
        candidato = random.choice(digitos)
        # vamos eligiendo digitos no repetidos
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato

    # iniciamos interaccion con el usuario
    print ("Bienvenido/a al Mastermind!")
    print (f"Tienes que adivinar un número de {cant_digitos} cifras distintas. Para rendirte escribe <me doy>")
    propuesta = input("¿Que código propones?: ")

    # procesamos las propuestas e indicamos aciertos y coincidencias
    intentos = 1
    while propuesta != codigo and propuesta.lower() != "me doy":
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0

        # recorremos la propuesta y verificamos en el codigo
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] in codigo:
                coincidencias = coincidencias + 1
        print (f"Tu propuesta {propuesta} tiene {aciertos} aciertos y {coincidencias} coincidencias.")
        # pedimos siguiente propuesta
        propuesta = input("Propón otro código: ")

    if propuesta.lower() == "me doy":
        print (f"El código era {codigo}")
        print ("Suerte la próxima vez!")
    else:
        print (f"Felicitaciones! Adivinaste el código en {intentos} intentos.")

def ahorcado():


 escenario = \
     '''   
 ~~~~~~~~~|~
         |
 0123456 J    
 ~~~~~~~~~~~   
 '''

 simbolos = '><(((º>'


 def bienvenida():
      print('*' * 68)
      print('* Te doy la bienvenida al juego del ahorcado. *')
      print('*' * 68)


  # paso 1
 def inicializar_juego(diccionario):
     palabra = random.choice(diccionario).lower()
     tablero = ['_'] * len(palabra)
     return tablero, palabra, []


 # paso 2
 def mostrar_escenario(errores):
     escena = escenario
     for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
     print(escena)


 # paso 3
 def mostrar_tablero(tablero, letras_erroneas):
     for casilla in tablero:
        print(casilla, end=' ')
     print()
     print()
     if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()


 # paso 4
 def pedir_letra(tablero, letras_erroneas):
     valida = False
     while not valida:
        letra = input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, prueba con otra.')

     return letra


 # paso 5
 def procesar_letra(letra, palabra, tablero, letras_erroneas):
     if letra in palabra:
        print('Genial!!! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
     else:
        print('Has fallado!!!')
        letras_erroneas.append(letra)


 # paso 5 (auxiliar)
 def actualizar_tablero(letra, palabra, tablero):
     for indice, letra_palabra in enumerate(palabra):
         if letra == letra_palabra:
            tablero[indice] = letra


 # paso 6
 def comprobar_palabra(tablero):
     return '_' not in tablero


 # bucle principal de juego
 def jugar_al_ahorcado(diccionario):
      tablero, palabra, letras_erroneas = inicializar_juego(diccionario)  # paso 1
      while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
        mostrar_escenario(len(letras_erroneas))  # paso 2
        mostrar_tablero(tablero, letras_erroneas)  # paso 3
        letra = pedir_letra(tablero, letras_erroneas)  # paso 4
        procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
        if comprobar_palabra(tablero):  # paso 6
            print('Felicitaciones, lo has logrado!!!')
            break
      else:
        print(f'Lo siento!!! Has perdido!!! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))  # paso 7

      mostrar_tablero(tablero, letras_erroneas)


 def jugar_otra_vez():
     return input('Deseas jugar otra vez??? (introduce s para sí o n para no): ')


 def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado!!! Hasta pronto!!! *')
    print('*' * 68)


 if __name__ == '__main__':
     diccionario = ['python', 'programacion', 'developer', 'codigo', 'while', 'for', 'bucle', 'ejecutar']
     bienvenida()
 while True:
        jugar_al_ahorcado(diccionario)
        if jugar_otra_vez() != 's': break
 despedida()

#MENU PRINCIPAL   
def decorar():
 print("#"*50)
 print("."*50)
 print("#"*50)
while True:
    decorar()
    break
print('''
    \t ::: MENU PRINCIPAL :::''')
print("Bienvenido/a! Elige un juego:")
print("1: Mastermind --> adiviná el código secreto!")
print("2: Dados --> tira los dados y gana la con la mayor puntuacion")
print("3: Ahorcado --> adivine la palabra antes de ahorcarse")
while True:
    decorar()
    break
eleccion = input("Ingresá tu opción: ")
match eleccion:
    case "1":
        mastermind()
    case "2":
        juegodados()
    case "3":
        ahorcado()
    case _ :
        print("Opción no válida")