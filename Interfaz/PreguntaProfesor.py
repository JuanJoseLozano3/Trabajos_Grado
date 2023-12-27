import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from plotly.graph_objs import Volume

from Interfaz import Principal
from Interfaz import AgregarProfesor
from Interfaz import PerfilProfesor
from Clases import GuardarTot
from Clases import Trabajo

def BuscarInformacion():
    global root
    global variable
    global dato
    root.destroy()
    Seleccion=variable.get()
    PerfilProfesor.Pantalla(Seleccion)

def VolverPregunta():
    global root
    root.destroy()
    Nombres = Trabajo.NombreProfesores()
    Correos = Trabajo.CorreoProfesores()
    Fotos = Trabajo.FotosProfesores()
    GuardarTot.actualizarDatabaseProfesores(Nombres,Correos,Fotos)
    Principal.Pantalla()

def AgregarPro():
    global root
    root.destroy()
    Nombres = Trabajo.NombreProfesores()
    Correos = Trabajo.CorreoProfesores()
    Fotos = Trabajo.FotosProfesores()
    GuardarTot.actualizarDatabaseProfesores(Nombres,Correos,Fotos)
    AgregarProfesor.Pantalla("","","")

#if __name__ == '__main__':
def Pantalla():
    global root
    global variable
    
    root = tk.Tk()
    Titulo = tk.Label(root, text="Seleccione docente", font=('courier', 20, 'bold'), justify=tk.CENTER)
    #Pantalla.grid(row=0,column=1)
    Titulo.config(width=90, font=('Helvetica', 18))
    Titulo.pack()
    Prof = Trabajo.NombreProfesores()
    root.title("Tesis")
    root.geometry("518x126")
    root.resizable(0, 0)
    variable = tk.StringVar(root)
    variable.set(Prof[0])
    opt = tk.OptionMenu(root, variable, *Prof)
    #opt.place(x=100,y=30)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    RD = tk.Button(root, text="Buscar", font=('courier', 18, 'bold'), command=BuscarInformacion)
    RD.place(x=75, y=70)

    agregar= tk.Button(root, text="Agregar", font=('courier', 18, 'bold'), command=AgregarPro)
    agregar.place(x=192, y=70)

    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPregunta)
    VO.place(x=325, y=70)
    root.mainloop()
