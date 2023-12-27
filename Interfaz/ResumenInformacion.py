from tkcalendar import Calendar
from datetime import date, time, datetime

import tkinter as tk
from tkinter import filedialog
import shutil
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Clases import Trabajo
from Clases import MetodosCompletos
from Interfaz import VisualizacionResumenTesis
from Interfaz import Principal
from Clases import GuardarTot

def BuscarDatos():
    global root
    global cal1, cal2
    global checkbox_value, datoTipo
    global datoCodigo, datoModalidad, datoEtapa
    global datoConcepto, datoDirector, datoLector
    UsarFecha = checkbox_value.get()
    elegido = cal1.get_date()
    i = 0
    comas = []
    while (i < len(elegido)):
        if (elegido[i] == '/'):
            comas.append(i)
        i = i + 1
    mes1 = elegido[0:comas[0]]
    dia1 = elegido[comas[0] + 1:comas[1]]
    ano1 = "20" + elegido[comas[1] + 1:len(elegido)]
    fec1 = ano1 + ',' + mes1 + ',' + dia1
    elegido2 = cal2.get_date()
    i = 0
    comas = []
    while (i < len(elegido2)):
        if (elegido2[i] == '/'):
            comas.append(i)
        i = i + 1
    mes2 = elegido2[0:comas[0]]
    dia2 = elegido2[comas[0] + 1:comas[1]]
    ano2 = "20" + elegido2[comas[1] + 1:len(elegido2)]
    fec2 = ano2 + ',' + mes2 + ',' + dia2
    Tipo = datoTipo.get()
    Modalidad = datoModalidad.get()
    Codigo = datoCodigo.get()
    Etapa = datoEtapa.get()
    Concepto = datoConcepto.get()
    Director = datoDirector.get()
    Lector = datoLector.get()
    Cumplen=MetodosCompletos.BuscarResumen(UsarFecha,ano1,mes1,dia1,ano2,mes2,dia2,Tipo,Modalidad,Codigo,Etapa,Concepto,Director,Lector)
    root.destroy()
    VisualizacionResumenTesis.Pantalla(0,Cumplen)
    #print(Cumplen)

def VolverDatos():
    global root
    root.destroy()
    Principal.Pantalla()

def Pantalla():
    global root
    global cal1, cal2
    global checkbox_value, datoTipo
    global datoCodigo, datoModalidad, datoEtapa
    global datoConcepto, datoDirector, datoLector
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x638")
    root.resizable(0, 0)

    checkbox_value = tk.BooleanVar(root)
    checkbox = tk.Checkbutton(root,variable=checkbox_value,text="Activar")
    checkbox.place(x=240, y=10)

    t = datetime(1, 1, 1)
    hoy = t.today()
    Fecha1 = tk.Label(root, text="Fecha Inicial", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Fecha1.place(x=55, y=10)
    cal1 = Calendar(root, selectmode='day',
                   year=hoy.year, month=hoy.month,
                   day=hoy.day)
    cal1.place(x=5, y=35)

    Fecha2 = tk.Label(root, text="Fecha Fin", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Fecha2.place(x=330, y=10)
    cal2 = Calendar(root, selectmode='day',
                   year=hoy.year, month=hoy.month,
                   day=hoy.day)
    cal2.place(x=260, y=35)

    Tipo = tk.Label(root, text="Tipo de fecha", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Tipo.place(x=20, y=230)
    datoTipo = tk.StringVar()
    entryTipo = tk.Entry(root, textvariable=datoTipo)
    entryTipo.insert(0, "")
    entryTipo.config(font=('Helvetica', 12))
    entryTipo.place(x=20, y=260)

    Codigo = tk.Label(root, text="Codigo", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Codigo.place(x=270, y=230)
    datoCodigo = tk.StringVar()
    entryCodigo = tk.Entry(root, textvariable=datoCodigo)
    entryCodigo.insert(0, "")
    entryCodigo.config(font=('Helvetica', 12))
    entryCodigo.place(x=270, y=260)

    Director = tk.Label(root, text="Director", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Director.place(x=20, y=330)
    datoDirector = tk.StringVar()
    entryDirector = tk.Entry(root, textvariable=datoDirector)
    entryDirector.insert(0, "")
    entryDirector.config(font=('Helvetica', 12))
    entryDirector.place(x=20, y=360)

    Lector = tk.Label(root, text="Lector", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Lector.place(x=270, y=330)
    datoLector = tk.StringVar()
    entryLector = tk.Entry(root, textvariable=datoLector)
    entryLector.insert(0, "")
    entryLector.config(font=('Helvetica', 12))
    entryLector.place(x=270, y=360)

    Modalidad = tk.Label(root, text="Modalidad", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Modalidad.place(x=20, y=430)
    datoModalidad = tk.StringVar()
    entryModalidad = tk.Entry(root, textvariable=datoModalidad)
    entryModalidad.insert(0, "")
    entryModalidad.config(font=('Helvetica', 12))
    entryModalidad.place(x=20, y=460)

    Etapa = tk.Label(root, text="Etapa", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Etapa.place(x=270, y=430)
    datoEtapa = tk.StringVar()
    entryEtapa = tk.Entry(root, textvariable=datoEtapa)
    entryEtapa.insert(0, "")
    entryEtapa.config(font=('Helvetica', 12))
    entryEtapa.place(x=270, y=460)

    Concepto = tk.Label(root, text="Concepto", font=('courier', 15, 'bold'), justify=tk.CENTER)
    Concepto.place(x=140, y=510)
    datoConcepto = tk.StringVar()
    entryConcepto = tk.Entry(root, textvariable=datoConcepto)
    entryConcepto.insert(0, "")
    entryConcepto.config(font=('Helvetica', 12))
    entryConcepto.place(x=140, y=540)

    Buscar = tk.Button(root, text="Buscar", font=('courier', 15, 'bold'), command=BuscarDatos)
    Buscar.place(x=70, y=580)

    Volver = tk.Button(root, text="Volver", font=('courier', 15, 'bold'), command=VolverDatos)
    Volver.place(x=320, y=580)
    root.mainloop()


