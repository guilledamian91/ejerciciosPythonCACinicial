import tkinter as tk
from tkinter import ttk
from os import system 
system("cls") 

def sumar():
    nro1= float(caja_numero_uno.get())
    nro2= float(caja_numero_dos.get())
    res= nro1 + nro2
    etiqueta_resultado.config (text=f"Resultado de la suma es: {res}",background="burlywood")

def restar():
    nro1= float(caja_numero_uno.get())
    nro2= float(caja_numero_dos.get())
    res= nro1 - nro2
    etiqueta_resultado.config (text=f"Resultado de la resta es: {res}",background="burlywood")    

def multiplicar():
    nro1= float(caja_numero_uno.get())
    nro2= float(caja_numero_dos.get())
    res= nro1 * nro2
    etiqueta_resultado.config (text=f"Resultado de la multiplicacion es: {res}",background="burlywood") 
    
def dividir():
    nro1= float(caja_numero_uno.get())
    nro2= float(caja_numero_dos.get())
    res= nro1 / nro2
    etiqueta_resultado.config (text=f"Resultado de la division es: {res}",background="burlywood") 

def salir():
    exit()
    
        
# VENTANA
ventana= tk.Tk()
ventana.title("Practica tinker") #titulo de la ventana
ventana.config(bg="burlywood", width=330, height=300)# color t tamaño de la ventana
ventana.resizable(0,0)# no permite cambiar de tamaño la ventana


# PRIMER NUMERO
etiqueta_numero_uno=ttk.Label(text="Ingrese un numero: ",background="burlywood")
etiqueta_numero_uno.place(x=20, y=20)
caja_numero_uno=ttk.Entry()
caja_numero_uno.place(x=140, y=20, width=60)

# SEGUNDO NUMERO
etiqueta_numero_dos=ttk.Label(text="Ingrese otro:",background="burlywood")
etiqueta_numero_dos.place(x=20, y=60)
caja_numero_dos=ttk.Entry()
caja_numero_dos.place(x=140, y=60, width=60)

# BOTONES
boton_sumar=tk.Button(text="Sumar", command= sumar)
boton_sumar.place(x=20,y=100)
boton_restar=tk.Button(text="Restar", command= restar)
boton_restar.place(x=100,y=100)
boton_multiplicar=tk.Button(text="Multiplicar", command= multiplicar)
boton_multiplicar.place(x=160,y=100)
boton_dividir=tk.Button(text="Dividir", command= dividir)
boton_dividir.place(x=260,y=100)
boton_salir=tk.Button(text="Salir", command= salir)
boton_salir.place(x=160,y=260)
etiqueta_resultado= ttk.Label(text="Resultado: ",background="burlywood")
etiqueta_resultado.place(x=20, y=190)

ventana.mainloop()  #mostrar ventana