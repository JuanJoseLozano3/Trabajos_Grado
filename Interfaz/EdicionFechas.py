import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import EditarTrabajo
from Interfaz import Pregunta
from Clases import MetodosCompletos

def GuarInformacion():
    global root
    global datoFecha
    global codigo
    global Tipo

    Pos = MetodosCompletos.BuscarPosicion(2, codigo)
    MetodosCompletos.ModificarFecha(Tipo, datoFecha.get(), Pos)
    MetodosCompletos.Guardar()
    root.destroy()
    EditarTrabajo.Pantalla(2, "", codigo)

def VolverPregunta():
    global root
    global codigo
    root.destroy()
    EditarTrabajo.Pantalla(2, "", codigo)

def Pantalla(Fecha,datoCodigo,FecProRec,FecProJur,FecProObs,FecProAce,FecIniPro,FecFinPro,FecProProRec,FecProProAce,FecIniProPro,FecFinProPro):
    global root
    global variable
    global datoFecha
    global codigo
    global Tipo

    codigo = datoCodigo
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x150")
    root.resizable(0, 0)

    Titulo = tk.Label(root, text=Fecha, font=('courier', 14, 'bold'), justify=tk.CENTER)
    Titulo.pack()
    Tipo=Fecha
    #Titulo.place(x=50, y=10)

    datoFecha = tk.StringVar()
    entry = tk.Entry(root, textvariable=datoFecha)

    if (Tipo == "Propuesta de grado recibida"):
        entry.insert(0, FecProRec)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Propuesta de grado enviada al jurado"):
        entry.insert(0, FecProJur)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Propuesta de grado enviada con observaciones"):
        entry.insert(0, FecProObs)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Propuesta de grado aceptada"):
        entry.insert(0, FecProAce)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Inicio del proyecto"):
        entry.insert(0, FecIniPro)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Fin del proyecto"):
        entry.insert(0, FecFinPro)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Propuesta de prorroga recibida"):
        entry.insert(0, FecProProRec)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Propuesta de prorroga aceptada"):
        entry.insert(0, FecProProAce)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Inicio de proyecto con prorroga"):
        entry.insert(0, FecIniProPro)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()
    elif (Tipo == "Fin de proyecto con prorroga"):
        entry.insert(0, FecFinProPro)
        entry.config(width=50, font=('Helvetica', 12))
        entry.pack()

    Esp = tk.Label(root, text="Año, Mes, Dia.  Ejemplo 2022,8,26", font=('courier', 14, 'bold'), justify=tk.CENTER)
    Esp.place(x=75, y=70)

    RD = tk.Button(root, text="Agregar", font=('courier', 18, 'bold'), command=GuarInformacion)
    RD.place(x=125, y=100)
    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPregunta)
    VO.place(x=285, y=100)
    root.mainloop()