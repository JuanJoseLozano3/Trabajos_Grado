import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import BuscarTrabajo
from Interfaz import EditarTrabajo
from Interfaz import ResumenInformacion
from Clases import MetodosCompletos

def BuscarTrabajos1():
    global root
    global Cod1
    root.destroy()
    EditarTrabajo.Pantalla(2, str(Cod1), "")

def BuscarTrabajos2():
    global root
    global Cod2
    root.destroy()
    EditarTrabajo.Pantalla(2, str(Cod2), "")

def BuscarTrabajos3():
    global root
    global Cod3
    root.destroy()
    EditarTrabajo.Pantalla(2, str(Cod3), "")

def BuscarTrabajos4():
    global root
    global Cod4
    root.destroy()
    EditarTrabajo.Pantalla(2, str(Cod4), "")

def BuscarTrabajos5():
    global root
    global Cod5
    root.destroy()
    EditarTrabajo.Pantalla(2, str(Cod5), "")

def VolverPrincipal():
    global root
    root.destroy()
    ResumenInformacion.Pantalla()

def BotonSiguiente():
    global Valores
    global Poses
    global feces
    global root
    root.destroy()
    Pantalla(Valores+5,Poses)

def BotonAtras():
    global root
    global Valores
    global Poses
    global feces
    root.destroy()
    Pantalla(Valores-5,Poses)

#if __name__ == '__main__':
def Pantalla(Valor,Pos):
    global root
    global Cod1
    global Cod2
    global Cod3
    global Cod4
    global Cod5
    global Valores
    global Poses
    global feces

    Valores = Valor
    Poses = Pos
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("818x518")
    root.resizable(0, 0)

    NombreEst = tk.Label(root, text="Nombre estudiante", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombreEst.place(x=10, y=10)

    Codigo = tk.Label(root, text="Codigo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Codigo.place(x=180, y=10)

    Nom = tk.Label(root, text="Nombre proyecto", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Nom.place(x=300, y=10)

    NombrePro = tk.Label(root, text="Nombre profesor", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombrePro.place(x=515, y=10)

    Informacion = tk.Label(root, text="Información", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Informacion.place(x=720, y=10)

    try:
        #1
        sum = 0
        [NumEst, NomEst1, Cod1, Doc, Dir, Tel, CorEst, NomProy, Mod, Res, Ano, Eta, NomDir1, CorDir, NomJur, CorJur, FecProRec,
        FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro,
        FecFinProPro] = MetodosCompletos.BuscarDesdePosicion(Pos[Valor+sum])

        #[Fechasa, Pos] = MetodosCompletos.BuscarFechaEspecifica(Valor + sum, fec)
        #Fech = Fechasa[Valor + sum]
        Nomb = tk.Text(root)
        Nomb.insert(1.0, NomProy)
        Nomb.configure(width=25, height=1, state='disabled')
        Nomb.place(x=300, y=60)

        Est = tk.Text(root)
        Est.insert(1.0, NomEst1)
        Est.configure(width=18, height=1,state='disabled')
        Est.place(x=10, y=60)

        Codi = tk.Text(root)
        Codi.insert(1.0, Cod1)
        Codi.configure(width=13, height=1,state='disabled')
        Codi.place(x=180, y=60)

        Pro = tk.Text(root)
        Pro.insert(1.0, NomDir1)
        Pro.configure(width=25, height=1,state='disabled')
        Pro.place(x=515, y=60)

        Inf = tk.Button(root, text="Info", font=('courier', 10, 'bold'), command=BuscarTrabajos1)
        Inf.place(x=735, y=55)

    except:
        no=1



    try:
        #2
        sum=1
        [NumEst, NomEst2, Cod2, Doc, Dir, Tel, CorEst, NomProy, Mod, Res, Ano, Eta, NomDir2, CorDir, NomJur, CorJur, FecProRec,
        FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro,
        FecFinProPro] = MetodosCompletos.BuscarDesdePosicion(Pos[Valor+sum])

        #[Fechasa, Pos] = MetodosCompletos.BuscarFechaEspecifica(Valor + sum, fec)
        Nomb = tk.Text(root)
        Nomb.insert(1.0, NomProy)
        Nomb.configure(width=25, height=1, state='disabled')
        Nomb.place(x=300, y=120)

        Est = tk.Text(root)
        Est.insert(1.0, NomEst2)
        Est.configure(width=18, height=1)
        Est.place(x=10, y=120)

        Codi = tk.Text(root)
        Codi.insert(1.0, Cod2)
        Codi.configure(width=13, height=1)
        Codi.place(x=180, y=120)

        Pro = tk.Text(root)
        Pro.insert(1.0, NomDir2)
        Pro.configure(width=25, height=1)
        Pro.place(x=515, y=120)

        Inf = tk.Button(root, text="Info", font=('courier', 10, 'bold'), command=BuscarTrabajos2)
        Inf.place(x=735, y=115)

    except:
        #print("No pude")
        nada=1


    try:
        # 3
        sum = 2
        [NumEst, NomEst3, Cod3, Doc, Dir, Tel, CorEst, NomProy, Mod, Res, Ano, Eta, NomDir3, CorDir, NomJur, CorJur,
         FecProRec,
         FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro,
         FecFinProPro] = MetodosCompletos.BuscarDesdePosicion(Pos[Valor + sum])

        #[Fechasa, Pos] = MetodosCompletos.BuscarFechaEspecifica(Valor + sum, fec)
        Nomb = tk.Text(root)
        Nomb.insert(1.0, NomProy)
        Nomb.configure(width=25, height=1, state='disabled')
        Nomb.place(x=300, y=180)

        Est = tk.Text(root)
        Est.insert(1.0, NomEst3)
        Est.configure(width=18, height=1)
        Est.place(x=10, y=180)

        Codi = tk.Text(root)
        Codi.insert(1.0, Cod3)
        Codi.configure(width=13, height=1)
        Codi.place(x=180, y=180)

        Pro = tk.Text(root)
        Pro.insert(1.0, NomDir3)
        Pro.configure(width=25, height=1)
        Pro.place(x=515, y=180)

        Inf = tk.Button(root, text="Info", font=('courier', 10, 'bold'), command=BuscarTrabajos3)
        Inf.place(x=735, y=175)

    except:
        no=1

    try:
        # 4
        sum = 3
        [NumEst, NomEst4, Cod4, Doc, Dir, Tel, CorEst, NomProy, Mod, Res, Ano, Eta, NomDir4, CorDir, NomJur, CorJur,
         FecProRec,
         FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro,
         FecFinProPro] = MetodosCompletos.BuscarDesdePosicion(Pos[Valor + sum])

        #[Fechasa, Pos] = MetodosCompletos.BuscarFechaEspecifica(Valor + sum, fec)
        Nomb = tk.Text(root)
        Nomb.insert(1.0, NomProy)
        Nomb.configure(width=25, height=1, state='disabled')
        Nomb.place(x=300, y=240)

        Est = tk.Text(root)
        Est.insert(1.0, NomEst4)
        Est.configure(width=18, height=1)
        Est.place(x=10, y=240)

        Codi = tk.Text(root)
        Codi.insert(1.0, Cod4)
        Codi.configure(width=13, height=1)
        Codi.place(x=180, y=240)

        Pro = tk.Text(root)
        Pro.insert(1.0, NomDir4)
        Pro.configure(width=25, height=1)
        Pro.place(x=515, y=240)

        Inf = tk.Button(root, text="Info", font=('courier', 10, 'bold'), command=BuscarTrabajos4)
        Inf.place(x=735, y=235)

    except:
        no=1

    try:
        # 5
        sum = 4
        [NumEst, NomEst5, Cod5, Doc, Dir, Tel, CorEst, NomProy, Mod, Res, Ano, Eta, NomDir5, CorDir, NomJur, CorJur,
         FecProRec,
         FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro,
         FecFinProPro] = MetodosCompletos.BuscarDesdePosicion(Pos[Valor + sum])

        #[Fechasa, Pos] = MetodosCompletos.BuscarFechaEspecifica(Valor + sum, fec)
        Nomb = tk.Text(root)
        Nomb.insert(1.0, NomProy)
        Nomb.configure(width=25, height=1, state='disabled')
        Nomb.place(x=300, y=300)

        Est = tk.Text(root)
        Est.insert(1.0, NomEst5)
        Est.configure(width=18, height=1)
        Est.place(x=10, y=300)

        Codi = tk.Text(root)
        Codi.insert(1.0, Cod5)
        Codi.configure(width=13, height=1)
        Codi.place(x=180, y=300)

        Pro = tk.Text(root)
        Pro.insert(1.0, NomDir5)
        Pro.configure(width=25, height=1)
        Pro.place(x=515, y=300)

        Inf = tk.Button(root, text="Info", font=('courier', 10, 'bold'), command=BuscarTrabajos5)
        Inf.place(x=735, y=295)

    except:
        no=1

    f = tk.Label(root, text=("Cumplen un total de: " + str(len(Pos))), font=('courier', 15, 'bold'), justify=tk.CENTER)
    f.place(x=270, y=400)

    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPrincipal)
    VO.place(x=350, y=450)

    Atras = tk.Button(root, text="Atras", font=('courier', 18, 'bold'), command=BotonAtras)
    Atras.place(x=30, y=350)


    Siguiente = tk.Button(root, text="Adelante", font=('courier', 18, 'bold'), command=BotonSiguiente)
    Siguiente.place(x=660, y=350)


    root.mainloop()

