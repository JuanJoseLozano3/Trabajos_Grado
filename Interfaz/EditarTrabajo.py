import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as MessageBox

from Clases import MetodosCompletos
from Clases import Trabajo
from Interfaz import Tesiscreada
from Interfaz import BuscarTrabajo
from Interfaz import EdicionFechas
from Interfaz import ErrorBusqueda

def AsignarfechaTrabajo():
    global root
    global datoNumEst, datoNombreEst, datoCodigo, datoId, datoDir
    global datoTel, datoCorEst, datoNombrePro
    global datoCorreoPro, datoNombreJur, datoCorreoJur
    global variablemodalidad, variableetapa, entryNombreProy
    global entryResumenProy, entryAnotacionesProy
    global variablefecha
    global NomProy, Res, Ano

    NomProyecto = entryNombreProy.get("1.0", "end")
    NomProyecto = NomProyecto.replace('\n', ' ')
    ResProyecto = entryResumenProy.get("1.0", "end")
    ResProyecto = ResProyecto.replace('\n', ' ')
    AnoProyecto = entryAnotacionesProy.get("1.0", "end")
    AnoProyecto = AnoProyecto.replace('\n', ' ')
    """
    MetodosCompletos.AgregarDatos(datoNumEst.get(),
                                  datoNombreEst.get(),
                                  datoCodigo.get(),
                                  datoId.get(),
                                  datoDir.get(),
                                  datoTel.get(),
                                  datoCorEst.get(),
                                  NomProyecto,
                                  variablemodalidad.get(),
                                  ResProyecto,
                                  AnoProyecto,
                                  variableetapa.get(),
                                  datoNombrePro.get(),
                                  datoCorreoPro.get(),
                                  datoNombreJur.get(),
                                  datoCorreoJur.get()
                                  )
    """
    Pos = MetodosCompletos.BuscarPosicion(2, datoCodigo.get())
    MetodosCompletos.ModificarDatos(Pos,datoNumEst.get(),
                                  datoNombreEst.get(),
                                  datoCodigo.get(),
                                  datoId.get(),
                                  datoDir.get(),
                                  datoTel.get(),
                                  datoCorEst.get(),
                                  NomProyecto,
                                  variablemodalidad.get(),
                                  ResProyecto,
                                  AnoProyecto,
                                  variableetapa.get(),
                                  datoNombrePro.get(),
                                  datoCorreoPro.get(),
                                  datoNombreJur.get(),
                                  datoCorreoJur.get()
                                  )
    MetodosCompletos.Guardar()
    MetodosCompletos.Inicializar()
    # Inicializa asignando cada lista correspondiente
    MetodosCompletos.AsignarVariables()
    root.destroy()
    # AsignacionFechas.Pantalla(variablefecha.get(),datoCodigo.get())
    global FecProRec, FecProjur, FecProObs, FecProAce, FecIniPro, FecFinPro, FecProProRec, FecProProAce, FecIniProPro, FecFinProPro
    EdicionFechas.Pantalla(variablefecha.get(),datoCodigo.get(),FecProRec,FecProjur,FecProObs,FecProAce,FecIniPro,FecFinPro,FecProProRec,FecProProAce,FecIniProPro,FecFinProPro)

def GuardarDatos():
    global root
    root.destroy()
    Tesiscreada.Pantalla()

def VolverDatos():
    global root
    root.destroy()
    BuscarTrabajo.Pantalla()

def Pantalla(Seleccion,Dato,CodigoPrub):
    global root
    global datoNumEst, datoNombreEst, datoCodigo, datoId, datoDir
    global datoTel, datoCorEst, datoNombrePro
    global datoCorreoPro, datoNombreJur, datoCorreoJur
    global variablemodalidad, variableetapa, entryNombreProy
    global entryResumenProy, entryAnotacionesProy
    global variablefecha
    global FecProRec,FecProjur,FecProObs,FecProAce,FecIniPro,FecFinPro,FecProProRec,FecProProAce,FecIniProPro,FecFinProPro
    root = tk.Tk()
    if(CodigoPrub==""):
        try:
            Pos = MetodosCompletos.BuscarPosicion(Seleccion, Dato)
            [NumEst,NomEst,Cod,Doc,Dir,Tel,CorEst,NomProy,Mod,Res,Ano,Eta,NomDir,CorDir,NomJur,CorJur,FecProRec,FecProjur,FecProObs,FecProAce,FecIniPro,FecFinPro,FecProProRec,FecProProAce,FecIniProPro,FecFinProPro]=MetodosCompletos.Buscar(Seleccion,Dato)
        except:
            root.destroy()
            ErrorBusqueda.Pantalla()
    else:
        try:
            Pos = MetodosCompletos.BuscarPosicion(Seleccion, CodigoPrub)
            [NumEst,NomEst,Cod,Doc,Dir,Tel,CorEst,NomProy,Mod,Res,Ano,Eta,NomDir,CorDir,NomJur,CorJur,FecProRec,FecProjur,FecProObs,FecProAce,FecIniPro,FecFinPro,FecProProRec,FecProProAce,FecIniProPro,FecFinProPro]=MetodosCompletos.Buscar(Seleccion,CodigoPrub)
        except:
            root.destroy()
            ErrorBusqueda.Pantalla()
    #print(b)
    root.title("Tesis")
    root.geometry("734x671")
    root.resizable(0, 0)

    NombreEstudiante = tk.Label(root, text="Nombre estudiante", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombreEstudiante.place(x=20, y=10)
    datoNombreEst = tk.StringVar()
    entryNombreEst = tk.Entry(root, textvariable=datoNombreEst)
    entryNombreEst.insert(0, NomEst)
    entryNombreEst.config(font=('Helvetica', 12))
    entryNombreEst.place(x=20, y=40)

    Codigo = tk.Label(root, text="Codigo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Codigo.place(x=20, y=70)
    datoCodigo = tk.StringVar()
    entryCodigo = tk.Entry(root, textvariable=datoCodigo)
    entryCodigo.insert(0, Cod)
    entryCodigo.config(font=('Helvetica', 12))
    entryCodigo.place(x=20, y=100)

    ID = tk.Label(root, text="Documento de identificacion", font=('courier', 10, 'bold'), justify=tk.CENTER)
    ID.place(x=20, y=130)
    datoId = tk.StringVar()
    entryId = tk.Entry(root, textvariable=datoId)
    entryId.insert(0, Doc)
    entryId.config(font=('Helvetica', 12))
    entryId.place(x=20, y=160)

    Direccion = tk.Label(root, text="Direccion", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Direccion.place(x=20, y=190)
    datoDir = tk.StringVar()
    entryDir = tk.Entry(root, textvariable=datoDir)
    entryDir.insert(0,Dir)
    entryDir.config(font=('Helvetica', 12))
    entryDir.place(x=20, y=220)

    Telefono = tk.Label(root, text="Telefono", font=('courier', 10, 'bold'), justify=tk.CENTER)
    Telefono.place(x=20, y=250)
    datoTel = tk.StringVar()
    entryTel = tk.Entry(root, textvariable=datoTel)
    entryTel.insert(0, Tel)
    entryTel.config(font=('Helvetica', 12))
    entryTel.place(x=20, y=280)

    CorreoEstudiante = tk.Label(root, text="Correo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    CorreoEstudiante.place(x=20, y=310)
    datoCorEst = tk.StringVar()
    entryCorEst = tk.Entry(root, textvariable=datoCorEst)
    entryCorEst.insert(0, CorEst)
    entryCorEst.config(font=('Helvetica', 12))
    entryCorEst.place(x=20, y=340)

    NombreProfesor = tk.Label(root, text="Nombre profesor", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombreProfesor.place(x=270, y=10)
    Profesores = Trabajo.NombreProfesores()
    datoNombrePro = tk.StringVar(root)
    datoNombrePro.set(NomDir)
    optPro = tk.OptionMenu(root, datoNombrePro, *Profesores)
    optPro.config(font=('Helvetica', 12))
    #opt.place(x=500,y=210)
    optPro.place(x=270, y=35)

    CorreoProfesor = tk.Label(root, text="Correo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    CorreoProfesor.place(x=270, y=70)
    datoCorreoPro = tk.StringVar()
    entryCorreoPro = tk.Entry(root, textvariable=datoCorreoPro)
    entryCorreoPro.insert(0, CorDir)
    entryCorreoPro.config(font=('Helvetica', 12))
    entryCorreoPro.place(x=270, y=100)

    NombreJurado = tk.Label(root, text="Nombre jurado", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombreJurado.place(x=500, y=10)
    datoNombreJur = tk.StringVar(root)
    datoNombreJur.set(NomJur)
    optJur = tk.OptionMenu(root, datoNombreJur, *Profesores)
    optJur.config(font=('Helvetica', 12))
    #opt.place(x=500,y=210)
    optJur.place(x=500, y=35)
    """
    datoNombreJur = tk.StringVar()
    entryNombreJur = tk.Entry(root, textvariable=datoNombreJur)
    entryNombreJur.insert(0, NomJur)
    entryNombreJur.config(font=('Helvetica', 12))
    entryNombreJur.place(x=500, y=40)
    """
    CorreoJurado = tk.Label(root, text="Correo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    CorreoJurado.place(x=500, y=70)
    datoCorreoJur = tk.StringVar()
    entryCorreoJur = tk.Entry(root, textvariable=datoCorreoJur)
    entryCorreoJur.insert(0, CorJur)
    entryCorreoJur.config(font=('Helvetica', 12))
    entryCorreoJur.place(x=500, y=100)

    TrabajoTit = tk.Label(root, text="Trabajo", font=('courier', 10, 'bold'), justify=tk.CENTER)
    TrabajoTit.place(x=430, y=130)

    NumeroTrabajo = tk.Label(root, text="Numero de estudiantes", font=('courier', 10, 'bold'), justify=tk.CENTER)
    # ModalidadTrabajo.place(x=280, y=190)
    NumeroTrabajo.place(x=375, y=155)
    datoNumEst = tk.StringVar()
    entryNumEst = tk.Entry(root, textvariable=datoNumEst)
    entryNumEst.insert(0, NumEst)
    entryNumEst.config(font=('Helvetica', 12))
    entryNumEst.place(x=375, y=175)

    ModalidadTrabajo = tk.Label(root, text="Modalidad", font=('courier', 10, 'bold'), justify=tk.CENTER)
    ModalidadTrabajo.place(x=280, y=200)
    Modalidad = [
        "Trabajo de grado",
        "Asistencia de investigacion",
        "Monografia",
        "Emprendimiento"
    ]
    variablemodalidad = tk.StringVar(root)
    variablemodalidad.set(Mod)
    opt = tk.OptionMenu(root, variablemodalidad, *Modalidad)
    opt.config(font=('Helvetica', 12))
    opt.place(x=270,y=220)
    #opt.pack()

    EtapaTrabajo = tk.Label(root, text="Etapa", font=('courier', 10, 'bold'), justify=tk.CENTER)
    EtapaTrabajo.place(x=510, y=200)
    Etapa = [
        "Propuesta",
        "Proyecto en desarrollo",
        "Proyecto en prorroga",
        "Proyecto finalizado",
    ]
    variableetapa = tk.StringVar(root)
    variableetapa.set(Eta)
    opt = tk.OptionMenu(root, variableetapa, *Etapa)
    opt.config(font=('Helvetica', 12))
    opt.place(x=500,y=220)

    NombreProyecto= tk.Label(root, text="Nombre del proyecto", font=('courier', 10, 'bold'), justify=tk.CENTER)
    NombreProyecto.place(x=270, y=270)
    entryNombreProy = tk.Text(root)
    entryNombreProy.insert(INSERT, NomProy)
    entryNombreProy.config(width = 46, height=3, font=('Helvetica', 12))
    entryNombreProy.place(x=270, y=303)

    ResumenProyecto= tk.Label(root, text="Resumen del proyecto", font=('courier', 10, 'bold'), justify=tk.CENTER)
    ResumenProyecto.place(x=20, y=380)
    entryResumenProy = tk.Text(root)
    entryResumenProy.insert(INSERT, Res)
    entryResumenProy.config(width = 74, height=4, font=('Helvetica', 12))
    entryResumenProy.place(x=20, y=410)

    AnotacionesProyecto = tk.Label(root, text="Anotaciones del proyecto", font=('courier', 10, 'bold'), justify=tk.CENTER)
    AnotacionesProyecto.place(x=20, y=490)
    entryAnotacionesProy = tk.Text(root)
    entryAnotacionesProy.insert(INSERT, Ano)
    entryAnotacionesProy.config(width=74, height=3, font=('Helvetica', 12))
    entryAnotacionesProy.place(x=20, y=520)

    Fecha = [
        "Propuesta de grado recibida",
        "Propuesta de grado enviada al jurado",
        "Propuesta de grado enviada con observaciones",
        "Propuesta de grado aceptada",
        "Inicio del proyecto",
        "Fin del proyecto",
        "Propuesta de prorroga recibida",
        "Propuesta de prorroga aceptada",
        "Inicio de proyecto con prorroga",
        "Fin de proyecto con prorroga"
    ]

    variablefecha = tk.StringVar(root)
    variablefecha.set(Fecha[0])
    opt = tk.OptionMenu(root, variablefecha, *Fecha)
    opt.config(font=('Helvetica', 12))
    opt.place(x=20, y=590)

    FechaAsignada = tk.Button(root, text="Fecha Asignada", font=('courier', 15, 'bold'), command=AsignarfechaTrabajo)
    FechaAsignada.place(x=450, y=585)

    Guardar = tk.Button(root, text="Guardar", font=('courier', 15, 'bold'), command=GuardarDatos)
    Guardar.place(x=200, y=630)

    Volver = tk.Button(root, text="Volver", font=('courier', 15, 'bold'), command=VolverDatos)
    Volver.place(x=400, y=630)
    root.mainloop()

