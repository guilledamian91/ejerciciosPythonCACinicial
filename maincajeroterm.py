import sqlite3
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from time import localtime, asctime
# Creado por Andres Ordoñez
conexion = sqlite3.connect("cajero.db")
cursor=conexion.cursor()

cursor.execute("""create table if not exists cajero
                 (user_dni NUMERIC primary key NOT NULL,
                 name TEXT NOT NULL,
                 lastname TEXT NOT NULL,
                 pwd TEXT NOT NULL,
                 admin BOOL)""")

cursor.execute("""create table if not exists movimientos
                 (movement_id INTEGER NOT NULL PRIMARY KEY autoincrement,
                 movement_dni NUMERIC NOT NULL,
                 time TEXT,
                 typeOf TEXT NOT NULL,
                 amount NUMERIC,
                 FOREIGN KEY (movement_dni)
                 REFERENCES cajero(user_dni))""")

# Clases

class user():
    user_dni = 0
    name = ""
    lastname = ""
    pwd = ""
    admin = False
    
class movimientos():
    movement_id = 0
    movement_dni = 0
    typeOf = ""
    amount = 0

# Usuario activo

activeUser = user()

class App:
    def __init__(self, root):
        self.root = root
        self.root.config(background="white")
        self.login()
        self.createUser()
        self.userArea()
        self.depositArea()
        self.withdrawArea()
        self.movementsArea()
        self.changePassword()
        self.payServices()

        
    def login(self):
        self.loginFrame = tk.Frame(self.root, background="white")
        self.loginFrame.pack(fill=tk.BOTH, expand=1)
        
        self.loginText = tk.Label(self.loginFrame,background="white", text=f"Bienvenido/a\nPor favor ingresa tu DNI y contraseña\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",font="Arial 15")
        self.loginText.pack(fill=tk.BOTH, expand=1)
                
        self.dniText = tk.Label(self.loginFrame, text=f"DNI", background="white")
        self.dniText.place(x=120, y=250)
        
        self.dniLoginInput = tk.Entry(self.loginFrame)
        self.dniLoginInput.place(x=240, y=250)
        
        self.pwdText = tk.Label(self.loginFrame, text=f"Contraseña", background="white")
        self.pwdText.place(x=120, y=280)
        
        self.pwdLoginInput = tk.Entry(self.loginFrame, show="*")
        self.pwdLoginInput.place(x=240, y=280)
                
        self.loginButton = tk.Button(self.loginFrame, text="Ingresar", border=3, command=self.logInButtonCmd)
        self.loginButton.place(x=230, y= 350)
        
        self.createUserButton = tk.Button(self.loginFrame, text="Registrarse", border=3, command=self.createUserButtonCmd)
        self.createUserButton.place(x=222, y=380)
        
    def createUser(self):
        self.createUserFrame = tk.Frame(self.root, background="white")
        
        self.createUserText = tk.Label(self.createUserFrame,background="white", text=f"Por favor complete los campos.",font="Arial 15")
        self.createUserText.place(x=110,y=85)
        
        self.nameInput = tk.Entry(self.createUserFrame)

        self.lastNameInput = tk.Entry(self.createUserFrame)
        
        self.dniInput = tk.Entry(self.createUserFrame)
        
        self.pwdInput = tk.Entry(self.createUserFrame, show="*")

        self.pwdCheckInput = tk.Entry(self.createUserFrame, show="*")
        
        self.nameText = tk.Label(self.createUserFrame, text=f"Nombre", background="white")
        self.nameText.place(x=120, y=260)
        
        self.lastNameText = tk.Label(self.createUserFrame, text=f"Apellido", background="white")
        self.lastNameText.place(x=120, y=290)
        
        self.dniText = tk.Label(self.createUserFrame, text=f"DNI", background="white")
        self.dniText.place(x=120, y=320)
        
        self.pwdText = tk.Label(self.createUserFrame, text=f"Contraseña", background="white")
        self.pwdText.place(x=120, y=350)
    
        self.pwdCheckText = tk.Label(self.createUserFrame, text=f"Reingresar contraseña", background="white")
        self.pwdCheckText.place(x=120, y=380)
        
        self.validText = tk.Label(self.createUserFrame, text=f"*Todos los campos son obligatorios.",font="Arial 8", background="white")
        self.validText.place(x=300, y=550)
        
        self.createUserButtonOk = tk.Button(self.createUserFrame, text="Crear usuario", border=3,command=self.createUserButtonOk)
        self.createUserButtonOk.place(x=222, y=420)
        
        self.returnButton = tk.Button(self.createUserFrame, text="Volver", border=3, command = self.returnSignUptoLogin)
        self.returnButton.place(x=240,y=450)
    
    def userArea(self):
        self.userAreaFrame = tk.Frame(self.root, background="white")
        
        self.userAreaName = tk.Label(self.userAreaFrame, background="white", font="Arial 15")
        self.userAreaName.pack(fill=tk.BOTH, expand=1,side="top")
                
        self.depositButton = tk.Button(self.userAreaFrame, text=f"Depositar\ndinero", border=3, height=4,width=10, command=self.openDepositArea)
        self.depositButton.place(x=10,y=450) 
        
        self.withdrawButton = tk.Button(self.userAreaFrame, text=f"Retirar\ndinero", border=3,height=4,width=10,command=self.openWithdrawArea)
        self.withdrawButton.place(x=110,y=450) 
        
        self.movementsButton = tk.Button(self.userAreaFrame, text=f"Consultar\nmovimientos", border=3,height=4,width=10,command=self.loadMovementsArea)
        self.movementsButton.place(x=210,y=450) 
        
        self.pswdChangeButton = tk.Button(self.userAreaFrame, text=f"Cambiar\nclave", border=3,height=4,width=10,command=self.pswdChangeButtonCmd)
        self.pswdChangeButton.place(x=310,y=450) 
        
        self.payServicesButton = tk.Button(self.userAreaFrame, text=f"Pagar\nservicios", border=3,height=4,width=10, command=self.openpayServicesArea)
        self.payServicesButton.place(x=410,y=450) 
        
        self.logOutButton = tk.Button(self.userAreaFrame, text=f"Salir", border=3,command=self.logOutButtonCmd)
        self.logOutButton.place(x=450,y=10) 
        
    def depositArea(self):
        self.depositAreaFrame = tk.Frame(self.root, background="white")
        
        self.depositAreaText = tk.Label(self.depositAreaFrame, background="white", font="Arial 15",text="Por favor, ingrese la\ncantidad de dinero a depositar.\n\n\n Recuerde que el cajero solo acepta\nbilletes de $100, $200, $500 y $1000.\n\n\n\n\n\n\n\n\n\n")
        self.depositAreaText.pack(fill=tk.BOTH, expand=1,side="top")
        
        self.depositAreaEntry = tk.Entry(self.depositAreaFrame, font="Arial 15")
        self.depositAreaEntry.pack(expand=1)
        
        self.depositAreaButton = tk.Button(self.depositAreaFrame,text=f"Depositar", border=3, command=self.deposit)
        self.depositAreaButton.place(x=215,y=550)
        
        self.depositReturnButton = tk.Button(self.depositAreaFrame, text="Volver", border=3, command = self.returnDepositToUserData)
        self.depositReturnButton.place(x=450,y=10)
        
    def withdrawArea(self):
        self.withdrawAreaFrame = tk.Frame(self.root, background="white")
        
        self.withdrawAreaText = tk.Label(self.withdrawAreaFrame, background="white", font="Arial 15",text="Por favor, ingrese la\ncantidad de dinero a retirar.\n\n\n Recuerde que el cajero solo entrega\nbilletes de $100, $200, $500 y $1000.\n\n\n\n\n\n\n\n\n\n")
        self.withdrawAreaText.pack(fill=tk.BOTH, expand=1,side="top")
        
        self.withdrawAreaEntry = tk.Entry(self.withdrawAreaFrame, font="Arial 15")
        self.withdrawAreaEntry.pack(expand=1)
        
        self.withdrawAreaButton = tk.Button(self.withdrawAreaFrame,text=f"Retirar", border=3, command=self.withdraw)
        self.withdrawAreaButton.place(x=215,y=550)
        
        self.withdrawReturnButton = tk.Button(self.withdrawAreaFrame, text="Volver", border=3, command = self.returnWithdrawToUserData)
        self.withdrawReturnButton.place(x=450,y=10)
        
    def movementsArea(self):
        self.movementsAreaFrame = tk.Frame(self.root, background="white")
        
        self.movementsAreaText = tk.Label(self.root, background="white", font="Arial 15",text="A continuación se detallan los últimos\nmovimientos realizados.")
        
        self.movementsAreaButton = tk.Button(self.root, text="Volver", border=3, command = self.returnloadMovementsAreaToUserData)
        
    def changePassword(self):
        self.changePassFrame = tk.Frame(self.root, background="white")
        
        self.changePassText = tk.Label(self.changePassFrame,background="white", text=f"Por favor, ingrese su documento,\nclave actual y la clave nueva.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",font="Arial 15")
        self.changePassText.pack(fill=tk.BOTH, expand=1,side="top")
        
        self.dnichangePassInput = tk.Entry(self.changePassFrame)
               
        self.oldPassChangePassInput = tk.Entry(self.changePassFrame, show="*")
        
        self.pwdchangePassInput = tk.Entry(self.changePassFrame, show="*")

        self.pwdchangePassCheckInput = tk.Entry(self.changePassFrame, show="*")
              
        self.dniText = tk.Label(self.changePassFrame, text=f"DNI", background="white")
        self.dniText.place(x=120, y=290)
        
        self.oldPassChangePassText = tk.Label(self.changePassFrame, text=f"Contraseña anterior", background="white")
        self.oldPassChangePassText.place(x=120, y=320)
        
        self.pwdText = tk.Label(self.changePassFrame, text=f"Contraseña nueva", background="white")
        self.pwdText.place(x=120, y=350)
    
        self.pwdCheckText = tk.Label(self.changePassFrame, text=f"Reingresar contraseña", background="white")
        self.pwdCheckText.place(x=120, y=380)
        
        self.validText = tk.Label(self.changePassFrame, text=f"*Todos los campos son obligatorios.",font="Arial 8", background="white")
        self.validText.place(x=300, y=550)
        
        self.changePassButtonOk = tk.Button(self.changePassFrame, text="Cambiar clave", border=3,command=self.changePassButtonOk)
        self.changePassButtonOk.place(x=222, y=420)
        
        self.changePassreturnButton = tk.Button(self.changePassFrame, text="Volver", border=3, command = self.returnchangePasstoUserArea)
        self.changePassreturnButton.place(x=240,y=450)
        
    def payServices(self):
        self.payServicesAreaFrame = tk.Frame(self.root, background="white")
        
        self.payServicesAreaText = tk.Label(self.payServicesAreaFrame, background="white", font="Arial 15",text="Por favor, seleccione el servicio a pagar.\n\n\n\n\n\n\n\n\n\n")
        self.payServicesAreaText.pack(fill=tk.BOTH, expand=1,side="top")
        
        self.payServicesAreaEntry = tk.Entry(self.payServicesAreaFrame, font="Arial 15")
        self.payServicesAreaEntry.pack(expand=1)
        
        self.payServicesAreaSelectText = ttk.Combobox(self.payServicesAreaFrame, background="white", font="Arial 14",state="readonly",values=["Luz","Agua","Gas","Celular","Municipalidad","Internet"])
        self.payServicesAreaSelectText.place(x=127,y=450)
        
        self.payServicesAreaText2 = tk.Label(self.payServicesAreaFrame, background="white", font="Arial 10",text="Por favor, ingrese el monto a pagar.")
        self.payServicesAreaText2.place(x=145,y=530)
        
        self.payServicesAreaButton = tk.Button(self.payServicesAreaFrame,text=f"Pagar", border=3, command=self.payServicesCMD)
        self.payServicesAreaButton.place(x=230,y=550)
        
        self.payServicesReturnButton = tk.Button(self.payServicesAreaFrame, text="Volver", border=3, command = self.returnpayServicesToUserData)
        self.payServicesReturnButton.place(x=450,y=10)
        
    ### Funciones ###
    
    def payServicesCMD(self):
        try:
            cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
            baseData = cursor.fetchall()
            i=0
            actualBalance = []
            
            while(len(baseData) > i):
                actualBalanceList = baseData[i]
                actualBalance.append(actualBalanceList[4])
                i += 1
                
            suma = 0
            
            for x in actualBalance:
                suma += x
                

            if (suma - int(self.payServicesAreaEntry.get()) < 0):
                messagebox.showerror(title="Fondos insuficientes",message="No dispone de fondos suficientes para realizar esta operación.")
            else:    
                cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"PAY SERVICE: {self.payServicesAreaSelectText.get()}",f"{int(self.payServicesAreaEntry.get())-(int(self.payServicesAreaEntry.get())*2)}"))
                conexion.commit()
                cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
                baseData = cursor.fetchall()
                i=0
                actualBalance = []
                
                while(len(baseData) > i):
                    actualBalanceList = baseData[i]
                    actualBalance.append(actualBalanceList[4])
                    i += 1
                    
                suma = 0
                
                for x in actualBalance:
                    suma += x
                
                messagebox.showinfo(title="Pago realizado con éxito",message=f"Pago realizado con éxito, su nuevo balance es de ${suma}")
                self.payServicesAreaFrame.pack_forget()
                self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
                self.payServicesAreaEntry.delete(0,"end")
                self.userAreaName.config(text=f"Bienvenido/a \n{activeUser.name} {activeUser.lastname}.\n\n\nSaldo actual\n${suma}\n\n\n\n\n\n\n\n\n")
        except ValueError:
            messagebox.showerror(title="¡Error!",message=f"Por favor, ingrese solo números")
    
    def openpayServicesArea(self):
        self.payServicesAreaFrame.pack(fill=tk.BOTH, expand=1,side="top")
        self.userAreaFrame.pack_forget()
    
    def returnpayServicesToUserData(self):
        self.payServicesAreaFrame.pack_forget()
        self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
        self.payServicesAreaEntry.delete(0,"end")
    
    def changePassButtonOk(self):
        if(int(self.dnichangePassInput.get()) == int(activeUser.user_dni)):
            if(self.oldPassChangePassInput.get() == activeUser.pwd):
                if (self.pwdchangePassInput.get() == self.pwdchangePassCheckInput.get()):
                    cursor.execute(f"UPDATE cajero SET pwd = '{self.pwdchangePassInput.get()}' WHERE user_dni = '{activeUser.user_dni}'")
                    conexion.commit()
                    activeUser.pwd = self.pwdchangePassInput.get()
                    cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"USERCHANGEPASSWORD",0))
                    conexion.commit()
                    messagebox.showinfo(title=f"Contraseña modificada con éxito",message="Contraseña modificada con éxito")
                    self.dnichangePassInput.delete(0,"end")
                    self.oldPassChangePassInput.delete(0,"end")
                    self.pwdchangePassInput.delete(0,"end")
                    self.pwdchangePassCheckInput.delete(0,"end")
                    self.changePassFrame.pack_forget()
                    self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
                else: messagebox.showerror(title="¡Error!",message=f"Las claves no coinciden.")
            else: messagebox.showerror(title="¡Error!",message=f"La clave ingresada no coincide con el DNI.")
        else: messagebox.showerror(title="¡Error!",message=f"El DNI ingresado no coincide con el usuario actual.")
    
    def pswdChangeButtonCmd(self):
        self.changePassFrame.pack(fill=tk.BOTH, expand=1,side="top")
        self.userAreaFrame.pack_forget()
        self.dnichangePassInput.place(x=250, y=290)
        self.oldPassChangePassInput.place(x=250, y=320)
        self.pwdchangePassInput.place(x=250, y=350)
        self.pwdchangePassCheckInput.place(x=250, y=380)
        
    def returnchangePasstoUserArea(self):
        self.dnichangePassInput.delete(0,"end")
        self.oldPassChangePassInput.delete(0,"end")
        self.pwdchangePassInput.delete(0,"end")
        self.pwdchangePassCheckInput.delete(0,"end")
        self.changePassFrame.pack_forget()
        self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
    
    def returnloadMovementsAreaToUserData(self):
        self.movementsAreaFrame.place_forget()
        self.movementsAreaText.place_forget()
        self.movementsAreaButton.place_forget()
        self.movementsAreaGrid.grid_remove()
        self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
        cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}' AND amount <> '0' ORDER BY time DESC")
        baseData = cursor.fetchall()
        
        total_rows = len(baseData)
        total_columns = 3
                
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.movementsAreaGrid = tk.Entry(self.movementsAreaFrame, width=25, background="gray",font=('Arial',9))
                self.movementsAreaGrid.grid(row=i, column=j)
                self.movementsAreaGrid.insert(i, " ")
    
    def loadMovementsArea(self):
        self.movementsAreaFrame.place(x=0,y=100,width=500,height=500)
        self.movementsAreaText.place(x=10,y=20,width=500)
        self.movementsAreaButton.place(x=450,y=10)
        self.userAreaFrame.pack_forget()
        
        cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}' AND amount <> '0' ORDER BY time DESC")
        baseData = cursor.fetchall()
        
        total_rows = len(baseData)
        total_columns = 3
                
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.movementsAreaGrid = tk.Entry(self.movementsAreaFrame, width=25, background="lightgray",font=('Arial',9))
                self.movementsAreaGrid.grid(row=i, column=j)
                self.movementsAreaGrid.insert(i, baseData[i][j+2])
    
    def withdraw(self):
        try:
            cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
            baseData = cursor.fetchall()
            i=0
            actualBalance = []
            
            while(len(baseData) > i):
                actualBalanceList = baseData[i]
                actualBalance.append(actualBalanceList[4])
                i += 1
                
            suma = 0
            
            for x in actualBalance:
                suma += x
            if (int(self.withdrawAreaEntry.get()) % 100 == 0):
                if (suma - int(self.withdrawAreaEntry.get()) < 0):
                    messagebox.showerror(title="Fondos insuficientes",message="No dispone de fondos suficientes para realizar esta operación.")
                else:    
                    cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"WITHDRAW",f"{int(self.withdrawAreaEntry.get())-(int(self.withdrawAreaEntry.get())*2)}"))
                    conexion.commit()
                    cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
                    baseData = cursor.fetchall()
                    i=0
                    actualBalance = []
                    
                    while(len(baseData) > i):
                        actualBalanceList = baseData[i]
                        actualBalance.append(actualBalanceList[4])
                        i += 1
                        
                    suma = 0
                    
                    for x in actualBalance:
                        suma += x
                    
                    messagebox.showinfo(title="Retiro realizado con éxito",message=f"Retiro realizado con éxito, su nuevo balance es de ${suma}")
                    self.withdrawAreaEntry.delete(0,"end")
                    self.withdrawAreaFrame.pack_forget()
                    self.userAreaFrame.pack(fill=tk.BOTH, expand=1,side="top")
                    self.userAreaName.config(text=f"Bienvenido/a \n{activeUser.name} {activeUser.lastname}.\n\n\nSaldo actual\n${suma}\n\n\n\n\n\n\n\n\n")
                    
            else:
                messagebox.showerror(title="¡Error!",message=f"Por favor, ingrese solo números aceptados por billetes de $100, $200, $500 o $1000")
        except ValueError:
                messagebox.showerror(title="¡Error!",message=f"Por favor, ingrese solo números aceptados por billetes de $100, $200, $500 o $1000")
    
    def openWithdrawArea(self):
        self.withdrawAreaFrame.pack(fill=tk.BOTH, expand=1,side="top")
        self.userAreaFrame.pack_forget()
    
    def returnWithdrawToUserData(self):
        self.withdrawAreaFrame.pack_forget()
        self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
        self.withdrawAreaEntry.delete(0,"end")
    
    def deposit(self):
        try:
            if (int(self.depositAreaEntry.get()) % 100 == 0):
                cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"DEPOSIT",f"{self.depositAreaEntry.get()}"))
                conexion.commit()
                cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
                baseData = cursor.fetchall()
                i=0
                actualBalance = []
                
                while(len(baseData) > i):
                    actualBalanceList = baseData[i]
                    actualBalance.append(actualBalanceList[4])
                    i += 1
                    
                suma = 0
                
                for x in actualBalance:
                    suma += x
                
                messagebox.showinfo(title="Depósito realizado con éxito",message=f"Depósito realizado con éxito, su nuevo balance es de ${suma}")
                self.depositAreaEntry.delete(0,"end")
                self.depositAreaFrame.pack_forget()
                self.userAreaFrame.pack(fill=tk.BOTH, expand=1,side="top")
                self.userAreaName.config(text=f"Bienvenido/a \n{activeUser.name} {activeUser.lastname}.\n\n\nSaldo actual\n${suma}\n\n\n\n\n\n\n\n\n")
                
            else:
                messagebox.showerror(title="¡Error!",message=f"Por favor, ingrese solo números aceptados por billetes de $100, $200, $500 o $1000")
        except ValueError:
                messagebox.showerror(title="¡Error!",message=f"Por favor, ingrese solo números aceptados por billetes de $100, $200, $500 o $1000")
    
    def openDepositArea(self):
        self.depositAreaFrame.pack(fill=tk.BOTH, expand=1,side="top")
        self.userAreaFrame.pack_forget()
    
    def returnDepositToUserData(self):
        self.depositAreaFrame.pack_forget()
        self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
        self.depositAreaEntry.delete(0,"end")
    
    def logOutButtonCmd(self):
        self.userAreaFrame.pack_forget()
        cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"LOGOUT",0))
        conexion.commit()
        activeUser.name=""
        activeUser.lastname=""
        activeUser.user_dni=0
        activeUser.pwd=""
        self.dniLoginInput.delete(0,"end")
        self.pwdLoginInput.delete(0,"end")
        self.loginFrame.pack(fill=tk.BOTH, expand=1)
        messagebox.showinfo(title="Salida exitosa",message=f"Gracias por utilizar nuestros servicios")
        
    def logInButtonCmd(self):
        cursor.execute(f"SELECT * FROM cajero WHERE user_dni = '{self.dniLoginInput.get()}'")
        try:
            activeUserData = cursor.fetchall()
            activeUserData = activeUserData[0]
            if (activeUserData[3] == self.pwdLoginInput.get()):
                
                activeUser.user_dni = activeUserData[0]
                activeUser.name = activeUserData[1]
                activeUser.lastname = activeUserData[2]
                activeUser.pwd = activeUserData[3]
                
                cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{activeUser.user_dni}",f"{asctime(localtime())}",f"LOGIN",0))
                conexion.commit()
                
                messagebox.showinfo(title="Ingreso exitoso",message=f"Bienvenido/a {activeUser.name} {activeUser.lastname}")
                 
                #Calcular balance actual
                
                cursor.execute(f"SELECT * FROM movimientos WHERE movement_dni = '{activeUser.user_dni}'")
                baseData = cursor.fetchall()
                i=0
                actualBalance = []
                
                while(len(baseData) > i):
                    actualBalanceList = baseData[i]
                    actualBalance.append(actualBalanceList[4])
                    i += 1
                    
                suma = 0
                
                for x in actualBalance:
                    suma += x
                
                self.userAreaName.config(text=f"Bienvenido/a \n{activeUser.name} {activeUser.lastname}.\n\n\nSaldo actual\n${suma}\n\n\n\n\n\n\n\n\n")
                self.userAreaFrame.pack(fill=tk.BOTH, expand=1)
                self.loginFrame.pack_forget()
            else: 
                messagebox.showerror(title="Error al ingresar",message=f"El usuario o la clave son incorrectos")
        except IndexError:
            messagebox.showerror(title="Error al ingresar",message=f"El usuario o la clave son incorrectos")
                
    def createUserButtonCmd(self):
        self.loginFrame.pack_forget()
        self.createUserFrame.pack(fill=tk.BOTH, expand=1)
        self.nameInput.place(x=250, y=260)
        self.lastNameInput.place(x=250, y=290)
        self.dniInput.place(x=250, y=320)
        self.pwdInput.place(x=250, y=350)
        self.pwdCheckInput.place(x=250, y=380)
        
    def returnSignUptoLogin(self):
        self.createUserFrame.pack_forget()
        self.loginFrame.pack(fill=tk.BOTH, expand=1)
        self.dniInput.delete(0,"end")
        self.nameInput.delete(0,"end")
        self.lastNameInput.delete(0,"end")
        self.pwdInput.delete(0,"end")
        self.pwdCheckInput.delete(0,"end")
        
    def createUserButtonOk(self):
        if (self.pwdInput.get() == self.pwdCheckInput.get()):
            try:
                cursor.execute(f"insert into cajero values (?,?,?,?,?)",(f"{self.dniInput.get()}",f"{self.nameInput.get()}",f"{self.lastNameInput.get()}",f"{self.pwdInput.get()}",False))
                conexion.commit()
                cursor.execute(f"insert into movimientos (movement_dni, time, typeOf, amount) values (?,?,?,?)",(f"{self.dniInput.get()}",f"{asctime(localtime())}",f"USERCREATION",0))
                conexion.commit()
                messagebox.showinfo(title=f"Bienvenido/a {self.nameInput.get()} {self.lastNameInput.get()}",message="Cuenta creada con éxito, por favor ingresa tus datos en la pantalla principal.")
                self.createUserFrame.pack_forget()
                self.loginFrame.pack(fill=tk.BOTH, expand=1)
                self.dniInput.delete(0,"end")
                self.nameInput.delete(0,"end")
                self.lastNameInput.delete(0,"end")
                self.pwdInput.delete(0,"end")
                self.pwdCheckInput.delete(0,"end")
            except sqlite3.IntegrityError:
                messagebox.showerror(title="¡Error!",message=f"Ya existe un usuario con ese DNI.\nPor favor contacta con un asesor para ayudarte.")
        else: messagebox.showerror(title="¡Error!",message=f"Las claves no coinciden.")

root = tk.Tk()
root.geometry("500x600")
root.title("Cajero")
root.resizable(width=False, height=False)
app = App(root)
root.mainloop()