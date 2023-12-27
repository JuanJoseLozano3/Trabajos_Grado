from tkcalendar import Calendar
from datetime import date, time, datetime
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import Principal
from Interfaz import VisualizacionTesis
from Interfaz import VisualizacionTesisMes
from Interfaz import ErrorMes
from Clases import MetodosCompletos

def VolverPrincipal():
    global root
    global Numero
    root.destroy()
    Principal.Pantalla()

#if __name__ == '__main__':
def Pantalla():
    global root
    global cal
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x408")
    root.resizable(0, 0)

    t = datetime(1,1,1)
    hoy = t.today()
    cal = Calendar(root, selectmode='day',
                   year=hoy.year, month=hoy.month,
                   day=hoy.day)

    cal.pack(pady=20)

    #Button(root, text="Get Date",command=grad_date).place(x=225, y=220)

    DI = tk.Button(root, text="Dia", font=('courier', 18, 'bold'), command=grad_date_dia)
    DI.place(x=225, y=250)

    ME = tk.Button(root, text="Mes", font=('courier', 18, 'bold'), command=grad_date_month)
    ME.place(x=225, y=300)

    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPrincipal)
    VO.place(x=200, y=350)
    root.mainloop()

def grad_date_dia():
    global cal
    global root
    #date.config(text="Selected Date is: " + cal.get_date())
    elegido = cal.get_date()
    i = 0
    comas = []
    while (i < len(elegido)):
        if (elegido[i] == '/'):
            comas.append(i)
        i = i + 1
    mes = elegido[0:comas[0]]
    dia = elegido[comas[0] + 1:comas[1]]
    ano = "20"+elegido[comas[1] + 1:len(elegido)]
    fec=ano+','+mes+','+dia
    Pos = []
    pos = MetodosCompletos.BuscarFecha(fec)
    Pos=Pos+pos
    root.destroy()
    VisualizacionTesis.Pantalla(0,Pos,fec)

def grad_date_month():
    global cal
    global root
    #date.config(text="Selected Date is: " + cal.get_date())
    elegido = cal.get_date()
    i = 0
    comas = []
    while (i < len(elegido)):
        if (elegido[i] == '/'):
            comas.append(i)
        i = i + 1
    mes = elegido[0:comas[0]]
    dia = elegido[comas[0] + 1:comas[1]]
    ano = "20"+elegido[comas[1] + 1:len(elegido)]
    Pos = []
    Fecha = []
    Cant = []
    for i in range(1,32):
        try:
            fec = ano + ',' + mes + ',' + str(i)
            pos = MetodosCompletos.BuscarFecha(fec)
            if(len(pos)>0):
                Fecha.append(fec)
                Cant.append(len(pos))
            Pos = Pos + pos
        except:
            aj=i
    if(len(Pos)>0):
        root.destroy()
        contador=0
        VisualizacionTesisMes.Pantalla(0, 0, Pos, Fecha, Cant, contador)
    else:
        root.destroy()
        ErrorMes.Pantalla()


def fech(pFecha):
    i = 0
    comas = []
    while (i < len(pFecha)):
        if (pFecha[i] == ','):
            comas.append(i)
        i = i + 1
    ano = pFecha[0:comas[0]]
    mes = pFecha[comas[0] + 1:comas[1]]
    dia = pFecha[comas[1] + 1:len(pFecha)]