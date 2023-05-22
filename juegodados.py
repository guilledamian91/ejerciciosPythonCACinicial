from random import randint

dadosUsuario =[]
totalUsuario = 0
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
    dadoParEncontrado = 0
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
  