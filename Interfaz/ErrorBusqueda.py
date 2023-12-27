import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Interfaz import BuscarTrabajo

def VolverPrincipal():
    global root
    global Numero
    root.destroy()
    BuscarTrabajo.Pantalla()

#if __name__ == '__main__':
def Pantalla():
    global root
    root = tk.Tk()
    root.title("Tesis")
    root.geometry("518x108")
    root.resizable(0, 0)

    Creado = tk.Label(root, text="¡No se encontro!", justify=tk.CENTER)
    Creado.config(width=90, font=('Helvetica', 20))
    Creado.pack()
    VO = tk.Button(root, text="Volver", font=('courier', 18, 'bold'), command=VolverPrincipal)
    VO.place(x=200, y=50)
    root.mainloop()