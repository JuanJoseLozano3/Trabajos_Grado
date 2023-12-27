import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import BuscarTrabajo
from Interfaz import AgregarTrabajo
from Interfaz import Principal

def BuscarTrabajos():
    global root
    root.destroy()
    BuscarTrabajo.Pantalla()

def AgregarTrabajos():
    global root
    root.destroy()
    AgregarTrabajo.Pantalla()

def VolverPrincipal():
    global root
    root.destroy()
    Principal.Pantalla()

#if __name__ == '__main__':
def Pantalla():
    global root
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x108")
    root.resizable(0, 0)
    TB = tk.Button(root,text="Buscar",font=('courier', 18, 'bold'), command=BuscarTrabajos)
    TB.place(x=50,y=30)
    RD = tk.Button(root,text="Agregar",font=('courier', 18, 'bold'), command=AgregarTrabajos)
    RD.place(x=200,y=30)
    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPrincipal)
    VO.place(x=360, y=30)
    root.mainloop()
