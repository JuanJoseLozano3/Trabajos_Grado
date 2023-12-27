import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import EditarTrabajo
from Interfaz import Pregunta

def BuscarInformacion():
    global root
    global variable
    global dato
    root.destroy()
    Seleccion=variable.get()
    if(Seleccion=="Nombre de estudiante"):
        Seleccion = 1
    elif (Seleccion == "Codigo"):
        Seleccion = 2
    elif (Seleccion == "Documento de identificacion"):
        Seleccion = 3
    Dato=str(dato.get())
    EditarTrabajo.Pantalla(Seleccion,Dato,"")

def VolverPregunta():
    global root
    root.destroy()
    Pregunta.Pantalla()

#if __name__ == '__main__':
def Pantalla():
    global root
    global variable
    global dato
    root = tk.Tk()
    OptionList = [
    "Nombre de estudiante",
    "Codigo",
    "Documento de identificacion"
    ]
    root.title("Tesis")
    root.geometry("518x126")
    root.resizable(0, 0)
    variable = tk.StringVar(root)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(root, variable, *OptionList)
    #opt.place(x=100,y=30)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    dato = tk.StringVar()
    entry = tk.Entry(root, textvariable=dato)
    entry.insert(0, "")
    entry.config(width=50, font=('Helvetica', 12))
    entry.pack()

    RD = tk.Button(root, text="Buscar", font=('courier', 18, 'bold'), command=BuscarInformacion)
    RD.place(x=125, y=70)
    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPregunta)
    VO.place(x=285, y=70)
    root.mainloop()