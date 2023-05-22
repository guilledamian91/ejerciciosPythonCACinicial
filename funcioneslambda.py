from os import system
system("cls")

'''podemos usar la funcion para ahorrar lineas de programacion'''
# def alCubo(x):
#     return x ** 3
# cubo= lambda x: x*x*x
# print(cubo(3))
# print(alCubo(3))

''' otro ejemplo para lambda'''
# enteros=[1,2,4,7]
# cuadrados1=[]
# for e in enteros:
#     cuadrados1.append(e**2)
# print(cuadrados1)
# enteros = [1,2,4,7]
# cuadrados= list(map(lambda x: x**2,enteros))
# print(cuadrados)

'''podemos combinar funciones lambda para llamar otras funciones'''
enteros = [1,2,4,7]
def cuadrado(x):
    return x**2
def cubo(x):
    return x**3
funciones=[cuadrado,cubo]
for e in enteros:
    valores=list(map(lambda x: x(e),funciones))
    print(valores)
