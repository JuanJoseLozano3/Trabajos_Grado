import tkinter as tk
from tkinter import filedialog
import shutil
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Clases import Trabajo
from Clases import MetodosCompletos
from Interfaz import PreguntaProfesor
from Interfaz import AsignacionFechas
from Clases import GuardarTot

def BuscarDir():
    global datoNombre
    global nombreFoto
    global root
    archivo_abierto = filedialog.askopenfilename(initialdir="/", title="Seleccion archivo",
                                                 filetypes=(("png files","*.png"),
                                                            ("all files","*.*")))
    i=len(archivo_abierto)
    while(i>0):
        if(archivo_abierto[i-1]=="."):
            break
        i=i-1
    extension=""
    while(i<len(archivo_abierto)):
        extension = extension + archivo_abierto[i]
        i=i+1
    NombreProfesor = datoNombre.get()
    NombreProfesor = NombreProfesor.replace(' ', '_')
    dir = "Interfaz/Fotos/" + NombreProfesor+"."+extension
    shutil.move(archivo_abierto, dir)
    nombreFoto = NombreProfesor+"."+extension
    Nom = datoNombre.get()
    Cor = datoCorreo.get()
    root.destroy()
    Pantalla(Nom,Cor,dir)


def AsignarAlProfesor():
    global datoNombre
    global datoCorreo
    global nombreFoto
    global root

    MetodosCompletos.AgregarDatosProfesor(datoNombre.get(),
                                          datoCorreo.get(),
                                          nombreFoto
                                          )
    Nombres = Trabajo.NombreProfesores()
    Correos = Trabajo.CorreoProfesores()
    Fotos = Trabajo.FotosProfesores()
    GuardarTot.actualizarDatabaseProfesores(Nombres, Correos, Fotos)
    MetodosCompletos.Inicializar()
    MetodosCompletos.AsignarVariables()
    root.destroy()
    PreguntaProfesor.Pantalla()

def VolverDatos():
    global root
    root.destroy()
    PreguntaProfesor.Pantalla()

def Pantalla(Nom,Cor,Dir):
    global root
    global datoNombre, datoCorreo

    root = tk.Tk()
    root.title("Tesis")
    root.geometry("618x126")

    Nombre = tk.Label(root, text="Nombre", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Nombre.place(x=20, y=10)
    datoNombre = tk.StringVar()
    entryNombre = tk.Entry(root, textvariable=datoNombre)
    entryNombre.insert(0, Nom)
    entryNombre.config(font=('Helvetica', 12))
    entryNombre.place(x=20, y=40)

    Correo = tk.Label(root, text="Correo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Correo.place(x=220, y=10)
    datoCorreo = tk.StringVar()
    entryCorreo = tk.Entry(root, textvariable=datoCorreo)
    entryCorreo.insert(0, Cor)
    entryCorreo.config(font=('Helvetica', 12))
    entryCorreo.place(x=220, y=40)

    Foto = tk.Label(root, text="Foto (.png)", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Foto.place(x=420, y=10)
    datoFoto = tk.StringVar()
    entryFoto = tk.Entry(root, textvariable=datoFoto)
    entryFoto.insert(0, Dir)
    entryFoto.config(font=('Helvetica', 12))
    entryFoto.place(x=420, y=40)

    RD = tk.Button(root, text="Abrir", font=('courier', 12, 'bold'), command=BuscarDir)
    RD.place(x=540, y=6)

    #Guardar = tk.Button(root, text="Guardar", font=('courier', 15, 'bold'), command=GuardarDatos)
    #Guardar.place(x=200, y=630)

    if(datoNombre.get()!="" and datoCorreo.get()!="" and datoFoto!=""):
        agregar = tk.Button(root, text="Guardar", font=('courier', 15, 'bold'), command=AsignarAlProfesor)
        agregar.place(x=160, y=80)

    Volver = tk.Button(root, text="Volver", font=('courier', 15, 'bold'), command=VolverDatos)
    Volver.place(x=370, y=80)
    root.mainloop()
