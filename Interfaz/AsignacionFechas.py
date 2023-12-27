import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import EditarTrabajo
from Interfaz import Pregunta
from Clases import MetodosCompletos
from Clases import Estudiante

def GuarInformacion():
    global rootsec
    global datoAgregaFecha
    global codigo
    global tipo

    Pos = MetodosCompletos.BuscarPosicion(2, codigo)
    MetodosCompletos.ModificarFecha(tipo, datoAgregaFecha.get(), Pos)
    MetodosCompletos.Guardar()
    rootsec.destroy()
    EditarTrabajo.Pantalla(2,"",codigo)

def VolverPregunta():
    global rootsec
    global codigo
    rootsec.destroy()
    EditarTrabajo.Pantalla(2, "", codigo)

#if __name__ == "__main__":
#    Fecha = "Solucion"
def Pantalla(Fecha,datoCodigo):
    global rootsec
    global variable
    global datoAgregaFecha
    global codigo
    global tipo

    codigo = datoCodigo
    rootsec = tk.Tk()
    rootsec.title("Fecha")
    rootsec.geometry("518x150")

    Titulo = tk.Label(rootsec, text=Fecha, font=('courier', 14, 'bold'), justify=tk.CENTER)
    Titulo.pack()
    tipo=Fecha
    #Titulo.place(x=50, y=10)

    datoAgregaFecha = tk.StringVar()
    entryAgregaFecha = tk.Entry(rootsec, textvariable=datoAgregaFecha)
    entryAgregaFecha.insert(0, "")
    entryAgregaFecha.config(width=50, font=('Helvetica', 12))
    entryAgregaFecha.pack()

    Esp = tk.Label(rootsec, text="Año, Mes, Dia.  Ejemplo 2022,8,26", font=('courier', 14, 'bold'), justify=tk.CENTER)
    Esp.place(x=75, y=70)
    RD = tk.Button(rootsec, text="Agregar", font=('courier', 18, 'bold'), command=GuarInformacion)
    RD.place(x=125, y=100)
    VO = tk.Button(rootsec, text="Volver", font=('courier', 18, 'bold'), command=VolverPregunta)
    VO.place(x=285, y=100)
    rootsec.mainloop()