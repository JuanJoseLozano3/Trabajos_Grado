import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import Pregunta
from Interfaz import EnProceso
from Interfaz import ResumenInformacion
from Interfaz import Calendario
from Interfaz import PreguntaProfesor

from Clases import MetodosCompletos

def TrabajoGrado():
    global root
    root.destroy()
    Pregunta.Pantalla()

def ResumenData():
    global root
    root.destroy()
    #EnProceso.Pantalla()
    ResumenInformacion.Pantalla()

def Cl():
    global root
    root.destroy()
    Calendario
    Calendario.Pantalla()

def Profesores():
    global root
    root.destroy()
    PreguntaProfesor.Pantalla()

#if __name__ == '__main__':
def Pantalla():
    global root
    #Inicializa leyendo la base de datos
    MetodosCompletos.Inicializar()
    #Inicializa asignando cada lista correspondiente
    MetodosCompletos.AsignarVariables()
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x438")
    root.resizable(0,0)
    Titulo = tk.Label(root, text="Sistema de Tesis de grado", font=('courier', 20, 'bold'), justify=tk.CENTER)
    #Pantalla.grid(row=0,column=1)
    Titulo.place(x=50,y=10)
    TB = tk.Button(root,text="Trabajos de grado",font=('courier', 18, 'bold'), command=TrabajoGrado)
    #TB.grid(row=3, column=1)
    TB.place(x=10,y=100)
    RD = tk.Button(root,text="Resumen data",font=('courier', 18, 'bold'), command=ResumenData)
    #RD.grid(row=4, column=1)
    RD.place(x=10,y=180)
    CA = tk.Button(root,text="Calendario",font=('courier', 18, 'bold'), command=Cl)
    #CA.grid(row=5, column=1)
    CA.place(x=10,y=260)
    PR = tk.Button(root,text="Profesores",font=('courier', 18, 'bold'), command=Profesores)
    #PR.grid(row=6, column=1)
    PR.place(x=10,y=340)
    #Li1 = PhotoImage(file = "Sistemas.png")
    Li1 = PhotoImage(file="Interfaz/Fotos/Sistemas.png")
    imagen_lipo1=Li1.subsample(2)
    Li1 = Label(root, image = imagen_lipo1)
    Li1.place(x=275,y=130)
    root.mainloop()
