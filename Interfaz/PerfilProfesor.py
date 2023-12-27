import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import PreguntaProfesor
from Clases import Director
from Clases import Jurado
from Clases import Trabajo
from Clases import MetodosCompletos

def VolverPregunta():
    global root
    root.destroy()
    PreguntaProfesor.Pantalla()


# if __name__ == '__main__':
def Pantalla(Seleccion):
    global root

    root = tk.Tk()

    root.title("Tesis")
    root.geometry("550x450")
    root.resizable(0, 0)

    try:
        ContarDirigiendo= Director.contarDirigiendo(Seleccion)
        if(ContarDirigiendo<0):
            ContarDirigiendo=0
    except:
        ContarDirigiendo = 0

    try:
        ContarDirigido= Director.contarDirigido(Seleccion)
        if(ContarDirigido<0):
            ContarDirigido=0
    except:
        ContarDirigido = 0

    try:
        ContarJuzgando= Jurado.contarJuzgando(Seleccion)
        if(ContarJuzgando<0):
            ContarJuzgando=0
    except:
        ContarJuzgando = 0

    try:
        ContarJuzgado= Jurado.contarJuzgado(Seleccion)
        if(ContarJuzgado<0):
            ContarJuzgado=0
    except:
        ContarJuzgado = 0

    Pos = MetodosCompletos.BuscarProfesor(Seleccion)

    NombrePro = tk.Label(root, text="Nombre profesor", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombrePro.place(x=10, y=10)
    ListaProfesores = Trabajo.NombreProfesores()
    ProfOnlyRead = tk.Text(root)
    ProfOnlyRead.insert(1.0, ListaProfesores[Pos])
    ProfOnlyRead.configure(width=25, height=1, state='disabled')
    ProfOnlyRead.place(x=10, y=40)

    CorreoPro = tk.Label(root, text="Correo profesor", font=('courier', 10, 'bold'), justify=tk.CENTER)
    CorreoPro.place(x=230, y=10)
    ListaCorreos = Trabajo.CorreoProfesores()
    CorOnlyRead = tk.Text(root)
    CorOnlyRead.insert(1.0, ListaCorreos[Pos])
    CorOnlyRead.configure(width=36, height=1, state='disabled')
    CorOnlyRead.place(x=230, y=40)

    ListaFotos = Trabajo.FotosProfesores()
    Li1 = PhotoImage(file="Interfaz/Fotos/"+ListaFotos[Pos])
    imagen_lipo1 = Li1.zoom(1)
    Li1 = Label(root, image=imagen_lipo1)
    Li1.place(x=135, y=60)

    Dirige = tk.Label(root, text="Es director", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Dirige.place(x=10, y=325)
    DirigeOnlyRead = tk.Text(root)
    DirigeOnlyRead.insert(1.0,ContarDirigiendo)
    DirigeOnlyRead.configure(width = 8, height=1,state='disabled')
    DirigeOnlyRead.place(x=10, y=355)

    JuradoTit = tk.Label(root, text="Es jurado", font=('courier', 10, 'bold'), justify=tk.CENTER)
    JuradoTit.place(x=150, y=325)
    JuradoOnlyRead = tk.Text(root)
    JuradoOnlyRead.insert(1.0, ContarJuzgando)
    JuradoOnlyRead.configure(width=8, height=1, state='disabled')
    JuradoOnlyRead.place(x=150, y=355)

    Dirigio = tk.Label(root, text="Fue director", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Dirigio.place(x=290, y=325)
    DirigioOnlyRead = tk.Text(root)
    DirigioOnlyRead.insert(1.0, ContarDirigido)
    DirigioOnlyRead.configure(width=8, height=1, state='disabled')
    DirigioOnlyRead.place(x=290, y=355)

    FueJurado = tk.Label(root, text="Fue jurado", font=('courier', 10, 'bold'), justify=tk.CENTER)
    FueJurado.place(x=430, y=325)
    FueJuradoOnlyRead = tk.Text(root)
    FueJuradoOnlyRead.insert(1.0, ContarJuzgado)
    FueJuradoOnlyRead.configure(width=8, height=1, state='disabled')
    FueJuradoOnlyRead.place(x=430, y=355)

    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPregunta)
    VO.place(x=200, y=390)
    root.mainloop()