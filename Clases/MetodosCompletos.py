#Librerias necesarias
import pandas as pd

#Objetos
from Clases import Estudiante
from Clases import Director
from Clases import Jurado
from Clases import Fecha
from Clases import Trabajo
from Clases import GuardarTot

def Inicializar():
    global Numero_de_estudiantes,Lista_Numero_Estudiantes,Nombres,Lista_Nombres
    global Codigos,Lista_Codigos,Documento_identificacion,Lista_Doc,Direccion
    global Lista_Direccion,Telefono,Lista_Telefonos,Correo_personal_estudiante
    global Lista_Correo_Estudiante,Lista_Nombre_proyecto,Nombre_proyecto
    global Modalidad,Lista_Modalidad,Resumen,Lista_Resumen
    global Anotacion,Lista_Anotacion,Etapa,Lista_Etapa,Nombre_director
    global Lista_Nombre_Director,Correo_personal_director,Lista_Correo_Director
    global Nombre_jurado,Lista_Nombre_Jurado,Correo_personal_jurado
    global Lista_Correo_Jurado,Fecha_propuesta_recibida,Lista_Fecha_propuesta_recibida
    global Fecha_propuesta_jurado,Lista_Fecha_propuesta_jurado,Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_observaciones,Fecha_propuesta_aceptada
    global Lista_Fecha_propuesta_aceptada,Fecha_inicio_proyecto,Lista_Fecha_inicio_proyecto
    global Fecha_fin_proyecto,Lista_Fecha_fin_proyecto,Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_recibida,Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_propuesta_prorroga_aceptada,Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_inicio_proyecto_prorroga,Fecha_fin_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga
    global Lista_Nombres_profesores, Lista_Correos_profesores, Lista_Fotos_profesores

    file_name2 = 'Clases/Profesores.csv'  # File name
    df = pd.read_csv(file_name2)
    Lista_Nombres_profesores = list(df["Nombre_profesores"])
    Lista_Correos_profesores = list(df["Correos"])
    Lista_Fotos_profesores = list(df["Fotos"])

    file_name = 'Clases/Base.csv' # File name
    df = pd.read_csv(file_name)
    Numero_de_estudiantes = 1
    Lista_Numero_Estudiantes = list(df["Numero_de_estudiantes"])
    Nombres = "Juan Antonio"
    Lista_Nombres = list(df["Nombres"])
    Codigos = str(2420151030)
    Lista_Codigos = list(df["Codigos"])
    Documento_identificacion = str(1110587580)
    Lista_Doc = list(df["Documento_identificacion"])
    Direccion = "Kra 7 # 64-77"
    Lista_Direccion = list(df["Direccion"])
    Telefono = str(3133352876)
    Lista_Telefonos = list(df["Telefonos"])
    Correo_personal_estudiante = "2420151030@estudiantesunibague.edu.co"
    Lista_Correo_Estudiante = list(df["Correo_personal_estudiante"])
    Nombre_proyecto = "Neurocisticercosis"
    Lista_Nombre_proyecto = list(df["Nombre_proyecto"])
    Modalidad = "Trabajo de grado"
    Lista_Modalidad = list(df["Modalidad"])
    Resumen = "PRUEBA SUPER MEGA LARGA"
    Lista_Resumen = list(df["Resumen"])
    Anotacion = "OTRA PRUEBA SUPER MEGA LARGA"
    Lista_Anotacion = list(df["Anotacion"])
    Etapa = "Aprobado"
    Lista_Etapa = list(df["Etapa"])
    Nombre_director = "Manuel Forero"
    Lista_Nombre_Director = list(df["Nombre_director"])
    Correo_personal_director="manuel.forero@unibague.edu.co"
    Lista_Correo_Director = list(df["Correo_personal_director"])
    Nombre_jurado="Elizabeth"
    Lista_Nombre_Jurado = list(df["Nombre_jurado"])
    Correo_personal_jurado="elizabeth@outlook.com"
    Lista_Correo_Jurado = list(df["Correo_personal_jurado"])
    Fecha_propuesta_recibida = "-"
    Lista_Fecha_propuesta_recibida = list(df["Fecha_propuesta_recibida"])
    Fecha_propuesta_jurado = "-"
    Lista_Fecha_propuesta_jurado = list(df["Fecha_propuesta_jurado"])
    Fecha_propuesta_observaciones = "-"
    Lista_Fecha_propuesta_observaciones = list(df["Fecha_propuesta_observaciones"])
    Fecha_propuesta_aceptada = "-"
    Lista_Fecha_propuesta_aceptada = list(df["Fecha_propuesta_aceptada"])
    Fecha_inicio_proyecto = "-"
    Lista_Fecha_inicio_proyecto = list(df["Fecha_inicio_proyecto"])
    Fecha_fin_proyecto = "-"
    Lista_Fecha_fin_proyecto = list(df["Fecha_fin_proyecto"])
    Fecha_propuesta_prorroga_recibida = "-"
    Lista_Fecha_propuesta_prorroga_recibida = list(df["Fecha_propuesta_prorroga_recibida"])
    Fecha_propuesta_prorroga_aceptada = "-"
    Lista_Fecha_propuesta_prorroga_aceptada = list(df["Fecha_propuesta_prorroga_aceptada"])
    Fecha_inicio_proyecto_prorroga = "-"
    Lista_Fecha_inicio_proyecto_prorroga = list(df["Fecha_inicio_proyecto_prorroga"])
    Fecha_fin_proyecto_prorroga = "-"
    Lista_Fecha_fin_proyecto_prorroga = list(df["Fecha_fin_proyecto_prorroga"])
    
    #Estudiante.modificarNombres(Lista_Nombres,Nombres)
    
    #ASIGNAR
def AsignarVariables():
    global Lista_Numero_Estudiantes,Lista_Nombres
    global Lista_Codigos,Lista_Doc
    global Lista_Direccion,Lista_Telefonos
    global Lista_Correo_Estudiante,Lista_Nombre_proyecto, Lista_Modalidad
    global Lista_Resumen
    global Lista_Anotacion,Lista_Etapa
    global Lista_Nombre_Director,Lista_Correo_Director
    global Lista_Nombre_Jurado
    global Lista_Correo_Jurado,Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada,Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga
    global Lista_Nombres_profesores, Lista_Correos_profesores, Lista_Fotos_profesores
    Estudiante.asignarNumero_de_estudiantes(Lista_Numero_Estudiantes)
    Estudiante.asignarNombres(Lista_Nombres)
    Estudiante.asignarCodigos(Lista_Codigos)
    Estudiante.asignarDocumento_identificacion(Lista_Doc)
    Estudiante.asignarDireccion(Lista_Direccion)
    Estudiante.asignarTelefono(Lista_Telefonos)
    Estudiante.asignarCorreo_Personal(Lista_Correo_Estudiante)
    Trabajo.asignarProfesores(Lista_Nombres_profesores,Lista_Correos_profesores,Lista_Fotos_profesores)
    Trabajo.asignarNombre(Lista_Nombre_proyecto)
    Trabajo.asignarModalidad(Lista_Modalidad)
    Trabajo.asignarResumen(Lista_Resumen)
    Trabajo.asignarAnotaciones(Lista_Anotacion)
    Trabajo.asignarEtapa(Lista_Etapa)
    Director.asignarNombres(Lista_Nombre_Director)
    Director.asignarCorreo_Personal(Lista_Correo_Director)
    Jurado.asignarNombres(Lista_Nombre_Jurado)
    Jurado.asignarCorreo_Personal(Lista_Correo_Jurado)
    Fecha.asignarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida)
    Fecha.asignarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado)
    Fecha.asignarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones)
    Fecha.asignarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada)
    Fecha.asignarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto)
    Fecha.asignarFecha_fin_proyecto(Lista_Fecha_fin_proyecto)
    Fecha.asignarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida)
    Fecha.asignarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada)
    Fecha.asignarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga)
    Fecha.asignarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga)


"""
    print("Puedes buscar con estas condiciones: ")
    print("Nombre estudiante: 1, Codigo estudiante: 2, Cedula estudiante: 3")
    print("Nombre del trabajo: 4, Modalidad del trabajo: 5, Etapa del trabajo: 6")
    print("Nombre del director: 7, Nombre del jurado: 8, Fecha propuesta recibida: 9")
    print("Fecha propuesta jurado: 10, Fecha propuesta observaciones: 11, Fecha propuesta aceptada: 12")
    print("Fecha inicio proyecto: 13, Fecha fin proyecto: 14, Fecha propuesta prorroga recibida: 15")
    print("Fecha propuesta prorroga aceptada: 16, Fecha inicio proyecto prorroga: 17, Fecha fin proyecto prorroga: 18")
    print("Cual desea?")

    try:
        Y=int(input())
    except:
        Y="19"
"""
def BuscarProfesor(nom):
    ListaProfesores = Trabajo.NombreProfesores()
    Posicion = ListaProfesores.index(nom)
    return Posicion

def BuscarPosicion(Y,nom):
    global Lista_Numero_Estudiantes, Lista_Nombres
    global Lista_Codigos, Lista_Doc
    global Lista_Direccion, Lista_Telefonos
    global Lista_Correo_Estudiante, Lista_Nombre_proyecto, Lista_Modalidad
    global Lista_Resumen
    global Lista_Anotacion, Lista_Etapa
    global Lista_Nombre_Director, Lista_Correo_Director
    global Lista_Nombre_Jurado
    global Lista_Correo_Jurado, Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga

    # Variable interna
    Posicion = 0

    if (Y == 1):
        # print("Por favor ingrese el Nombre del estudiante")
        # nom=str(input())
        try:
            Posicion = Estudiante.buscarNombres(Lista_Nombres, nom)
        except:
            print("Ese nombre no existe")
    elif (Y == 2):
        # print("Por favor ingrese el Codigo del estudiante")
        # cod=int(input())
        try:
            Posicion = Estudiante.buscarCodigos(Lista_Codigos, str(nom))
        except:
            print("Ese codigo no existe")
    elif (Y == 3):
        # print("Por favor ingrese el Documento del estudiante")
        # ID=int(input())
        try:
            Posicion = Estudiante.buscarDocumento_identificacion(Lista_Doc, str(nom))
        except:
            print("Ese documento no existe")
    elif (Y == 4):
        # print("Por favor ingrese el Nombre del proyecto")
        # nom=str(input())
        try:
            Posicion = Trabajo.buscarNombre(Lista_Nombre_proyecto, nom)
        except:
            print("Ese nombre no existe")
    elif (Y == 5):
        # print("Por favor ingrese el Modalidad del proyecto")
        # mod=str(input())
        try:
            Posicion = Trabajo.buscarModalidad(Lista_Modalidad, nom)
        except:
            print("Esa modalidad no existe")
    elif (Y == 6):
        # print("Por favor ingrese el Etapa del proyecto")
        # eta=str(input())
        try:
            Posicion = Trabajo.buscarEtapa(Lista_Etapa, nom)
        except:
            print("Esa etapa no existe")
    elif (Y == 7):
        # print("Por favor ingrese el Nombre del Director")
        # nom=str(input())
        try:
            Posicion = Director.buscarNombres(Lista_Nombre_Director, nom)
        except:
            print("Ese nombre no existe")
    elif (Y == 8):
        # print("Por favor ingrese el Nombre del Jurado")
        # nom=str(input())
        try:
            Posicion = Jurado.buscarNombres(Lista_Nombre_Jurado, nom)
        except:
            print("Ese nombre no existe")
    elif (Y == 9):
        # print("Por favor ingrese el Fecha_propuesta_recibida")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 10):
        # print("Por favor ingrese el echa_propuesta_jurado")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 11):
        # print("Por favor ingrese el Fecha_propuesta_observaciones")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 12):
        # print("Por favor ingrese el Fecha_propuesta_aceptada")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 13):
        # print("Por favor ingrese el Fecha_inicio_proyecto")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 14):
        # print("Por favor ingrese el Fecha_fin_proyecto")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_fin_proyecto(Lista_Fecha_fin_proyecto, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 15):
        # print("Por favor ingrese el Fecha_propuesta_prorroga_recibida")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 16):
        # print("Por favor ingrese el Fecha_propuesta_prorroga_aceptada")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 17):
        # print("Por favor ingrese el Fecha_inicio_proyecto_prorroga")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga, nom)
        except:
            print("Esa fecha no existe")
    elif (Y == 18):
        # print("Por favor ingrese el Fecha_fin_proyecto_prorroga")
        # num=str(input())
        try:
            Posicion = Fecha.buscarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga, nom)
        except:
            print("Esa fecha no existe")
    else:
        print("Se selecciono una variables errada")
    return Posicion

def BuscarFechaEspecifica(num,nom):
    global Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga
    Pos=[]
    Pal = []
    try:
        Posicion1 = Fecha.buscardiaFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, nom)
        Pos = Pos + Posicion1
        if (Pos[num-1] != "-"):
            p=0
            while p<len(Posicion1):
                Pal.append("Fecha_propuesta_recibida")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada=1
    try:
        Posicion2 = Fecha.buscardiaFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, nom)
        Pos = Pos + Posicion2
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion2):
                Pal.append("Fecha_propuesta_jurado")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1

    try:
        Posicion3 = Fecha.buscardiaFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, nom)
        Pos = Pos + Posicion3
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion3):
                Pal.append("Fecha_propuesta_observacion")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1

    try:
        Posicion4 = Fecha.buscardiaFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, nom)
        Pos = Pos + Posicion4
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion4):
                Pal.append("Fecha_propuesta_aceptada")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion5 = Fecha.buscardiaFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, nom)
        Pos = Pos + Posicion5
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion5):
                Pal.append("Fecha_inicio_proyecto")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion6 = Fecha.buscardiaFecha_fin_proyecto(Lista_Fecha_fin_proyecto, nom)
        Pos = Pos + Posicion6
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion6):
                Pal.append("Fecha_fin_proyecto")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion7 = Fecha.buscardiaFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida, nom)
        Pos = Pos + Posicion7
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion7):
                Pal.append("Fecha_propuesta_prorroga_recibida")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion8 = Fecha.buscardiaFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada, nom)
        Pos = Pos + Posicion8
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion8):
                Pal.append("Fecha_propuesta_prorroga_aceptada")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion9 = Fecha.buscardiaFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga, nom)
        Pos = Pos + Posicion9
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion9):
                Pal.append("Fecha_inicio_proyecto_prorroga")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    try:
        Posicion10 = Fecha.buscardiaFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga, nom)
        Pos = Pos + Posicion10
        if (Pos[num - 1] != "-"):
            p = 0
            while p < len(Posicion10):
                Pal.append("Fecha_fin_proyecto_prorrog")
                p=p+1
    except:
        #print("Esa fecha no existe")
        nada = 1
    return Pal,Pos


def BuscarFecha(nom):
    global Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga

    Pos=[]
    try:
        Posicion1 = Fecha.buscardiaFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion1
    try:
        Posicion2 = Fecha.buscardiaFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion2
    try:
        Posicion3 = Fecha.buscardiaFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion3
    try:
        Posicion4 = Fecha.buscardiaFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion4
    try:
        Posicion5 = Fecha.buscardiaFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion5
    try:
        Posicion6 = Fecha.buscardiaFecha_fin_proyecto(Lista_Fecha_fin_proyecto, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion6
    try:
        Posicion7 = Fecha.buscardiaFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion7
    try:
        Posicion8 = Fecha.buscardiaFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion8
    try:
        Posicion9 = Fecha.buscardiaFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion9
    try:
        Posicion10 = Fecha.buscardiaFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga, nom)
    except:
        print("Esa fecha no existe")
    Pos = Pos + Posicion10
    return Pos

def BuscarDesdePosicion(Posicion):
    global Lista_Numero_Estudiantes, Lista_Nombres
    global Lista_Codigos, Lista_Doc
    global Lista_Direccion, Lista_Telefonos
    global Lista_Correo_Estudiante, Lista_Nombre_proyecto, Lista_Modalidad
    global Lista_Resumen
    global Lista_Anotacion, Lista_Etapa
    global Lista_Nombre_Director, Lista_Correo_Director
    global Lista_Nombre_Jurado
    global Lista_Correo_Jurado, Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga

    return [Lista_Numero_Estudiantes[Posicion],
            Lista_Nombres[Posicion],
            Lista_Codigos[Posicion],
            Lista_Doc[Posicion],
            Lista_Direccion[Posicion],
            Lista_Telefonos[Posicion],
            Lista_Correo_Estudiante[Posicion],
            Lista_Nombre_proyecto[Posicion],
            Lista_Modalidad[Posicion],
            Lista_Resumen[Posicion],
            Lista_Anotacion[Posicion],
            Lista_Etapa[Posicion],
            Lista_Nombre_Director[Posicion],
            Lista_Correo_Director[Posicion],
            Lista_Nombre_Jurado[Posicion],
            Lista_Correo_Jurado[Posicion],
            Lista_Fecha_propuesta_recibida[Posicion],
            Lista_Fecha_propuesta_jurado[Posicion],
            Lista_Fecha_propuesta_observaciones[Posicion],
            Lista_Fecha_propuesta_aceptada[Posicion],
            Lista_Fecha_inicio_proyecto[Posicion],
            Lista_Fecha_fin_proyecto[Posicion],
            Lista_Fecha_propuesta_prorroga_recibida[Posicion],
            Lista_Fecha_propuesta_prorroga_aceptada[Posicion],
            Lista_Fecha_inicio_proyecto_prorroga[Posicion],
            Lista_Fecha_fin_proyecto_prorroga[Posicion]
            ]

def Buscar(Y,nom):
    global Lista_Numero_Estudiantes,Lista_Nombres
    global Lista_Codigos,Lista_Doc
    global Lista_Direccion,Lista_Telefonos
    global Lista_Correo_Estudiante,Lista_Nombre_proyecto, Lista_Modalidad
    global Lista_Resumen
    global Lista_Anotacion,Lista_Etapa
    global Lista_Nombre_Director,Lista_Correo_Director
    global Lista_Nombre_Jurado
    global Lista_Correo_Jurado,Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada,Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga

    #Variable interna
    Posicion=0

    if(Y==1):
        #print("Por favor ingrese el Nombre del estudiante")
        #nom=str(input())
        try:
            Posicion=Estudiante.buscarNombres(Lista_Nombres,nom)
        except:
            print("Ese nombre no existe")
    elif(Y==2):
        #print("Por favor ingrese el Codigo del estudiante")
        #cod=int(input())
        try:
            Posicion=Estudiante.buscarCodigos(Lista_Codigos,str(nom))
        except:
            print("Ese codigo no existe")
    elif(Y==3):
        #print("Por favor ingrese el Documento del estudiante")
        #ID=int(input())
        try:
            Posicion=Estudiante.buscarDocumento_identificacion(Lista_Doc,str(nom))
        except:
            print("Ese documento no existe")
    elif(Y==4):
        #print("Por favor ingrese el Nombre del proyecto")
        #nom=str(input())
        try:
            Posicion=Trabajo.buscarNombre(Lista_Nombre_proyecto,nom)
        except:
            print("Ese nombre no existe")
    elif(Y==5):
        #print("Por favor ingrese el Modalidad del proyecto")
        #mod=str(input())
        try:
            Posicion=Trabajo.buscarModalidad(Lista_Modalidad,nom)
        except:
            print("Esa modalidad no existe")
    elif(Y==6):
        #print("Por favor ingrese el Etapa del proyecto")
        #eta=str(input())
        try:
            Posicion=Trabajo.buscarEtapa(Lista_Etapa,nom)
        except:
            print("Esa etapa no existe")
    elif(Y==7):
        #print("Por favor ingrese el Nombre del Director")
        #nom=str(input())
        try:
            Posicion=Director.buscarNombres(Lista_Nombre_Director,nom)
        except:
            print("Ese nombre no existe")
    elif(Y==8):
        #print("Por favor ingrese el Nombre del Jurado")
        #nom=str(input())
        try:
            Posicion=Jurado.buscarNombres(Lista_Nombre_Jurado,nom)
        except:
            print("Ese nombre no existe")            
    elif(Y==9):
        #print("Por favor ingrese el Fecha_propuesta_recibida")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==10):
        #print("Por favor ingrese el echa_propuesta_jurado")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==11):
        #print("Por favor ingrese el Fecha_propuesta_observaciones")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==12):
        #print("Por favor ingrese el Fecha_propuesta_aceptada")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==13):
        #print("Por favor ingrese el Fecha_inicio_proyecto")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==14):
        #print("Por favor ingrese el Fecha_fin_proyecto")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_fin_proyecto(Lista_Fecha_fin_proyecto,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==15):
        #print("Por favor ingrese el Fecha_propuesta_prorroga_recibida")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==16):
        #print("Por favor ingrese el Fecha_propuesta_prorroga_aceptada")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==17):
        #print("Por favor ingrese el Fecha_inicio_proyecto_prorroga")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga,nom)
        except:
            print("Esa fecha no existe")
    elif(Y==18):
        #print("Por favor ingrese el Fecha_fin_proyecto_prorroga")
        #num=str(input())
        try:
            Posicion=Fecha.buscarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga,nom)
        except:
            print("Esa fecha no existe")
    else:
        print("Se selecciono una variables errada")

    if(Posicion!=0):
        """
        print(Lista_Numero_Estudiantes[Posicion])
        print(Lista_Nombres[Posicion])
        print(Lista_Codigos[Posicion])
        print(Lista_Doc[Posicion])
        print(Lista_Direccion[Posicion])
        print(Lista_Telefonos[Posicion])
        print(Lista_Correo_Estudiante[Posicion])
        print(Lista_Nombre_proyecto[Posicion])
        print(Lista_Modalidad[Posicion])
        print(Lista_Resumen[Posicion])
        print(Lista_Anotacion[Posicion])
        print(Lista_Etapa[Posicion])
        print(Lista_Nombre_Director[Posicion])
        print(Lista_Correo_Director[Posicion])
        print(Lista_Nombre_Jurado[Posicion])
        print(Lista_Correo_Jurado[Posicion])
        print(Lista_Fecha_propuesta_recibida[Posicion])
        print(Lista_Fecha_propuesta_jurado[Posicion])
        print(Lista_Fecha_propuesta_observaciones[Posicion])
        print(Lista_Fecha_propuesta_aceptada[Posicion])
        print(Lista_Fecha_inicio_proyecto[Posicion])
        print(Lista_Fecha_fin_proyecto[Posicion])
        print(Lista_Fecha_propuesta_prorroga_recibida[Posicion])
        print(Lista_Fecha_propuesta_prorroga_aceptada[Posicion])
        print(Lista_Fecha_inicio_proyecto_prorroga[Posicion])
        print(Lista_Fecha_fin_proyecto_prorroga[Posicion])
        """
        return [Lista_Numero_Estudiantes[Posicion],
                Lista_Nombres[Posicion],
                Lista_Codigos[Posicion],
                Lista_Doc[Posicion],
                Lista_Direccion[Posicion],
                Lista_Telefonos[Posicion],
                Lista_Correo_Estudiante[Posicion],
                Lista_Nombre_proyecto[Posicion],
                Lista_Modalidad[Posicion],
                Lista_Resumen[Posicion],
                Lista_Anotacion[Posicion],
                Lista_Etapa[Posicion],
                Lista_Nombre_Director[Posicion],
                Lista_Correo_Director[Posicion],
                Lista_Nombre_Jurado[Posicion],
                Lista_Correo_Jurado[Posicion],
                Lista_Fecha_propuesta_recibida[Posicion],
                Lista_Fecha_propuesta_jurado[Posicion],
                Lista_Fecha_propuesta_observaciones[Posicion],
                Lista_Fecha_propuesta_aceptada[Posicion],
                Lista_Fecha_inicio_proyecto[Posicion],
                Lista_Fecha_fin_proyecto[Posicion],
                Lista_Fecha_propuesta_prorroga_recibida[Posicion],
                Lista_Fecha_propuesta_prorroga_aceptada[Posicion],
                Lista_Fecha_inicio_proyecto_prorroga[Posicion],
                Lista_Fecha_fin_proyecto_prorroga[Posicion],
                ]
        

def ModificarFecha(Tipo,FechaPropuesta,Pos):
    global Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga

    global Fecha_propuesta_recibida
    global Fecha_propuesta_jurado, Fecha_propuesta_observaciones
    global Fecha_propuesta_aceptada
    global Fecha_inicio_proyecto
    global Fecha_fin_proyecto, Fecha_propuesta_prorroga_recibida
    global Fecha_propuesta_prorroga_aceptada
    global Fecha_inicio_proyecto_prorroga
    global Fecha_fin_proyecto_prorroga

    if(Tipo == "Propuesta de grado recibida"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_recibida = "-"
        else:
            Fecha_propuesta_recibida = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, Pos, Fecha_propuesta_recibida)
        #Fecha.agregarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, Fecha_propuesta_recibida)
    elif (Tipo == "Propuesta de grado enviada al jurado"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_jurado = "-"
        else:
            Fecha_propuesta_jurado = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, Pos, Fecha_propuesta_jurado)
    elif (Tipo == "Propuesta de grado enviada con observaciones"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_observaciones = "-"
        else:
            Fecha_propuesta_observaciones = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, Pos, Fecha_propuesta_observaciones)
    elif (Tipo == "Propuesta de grado aceptada"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_aceptada = "-"
        else:
            Fecha_propuesta_aceptada = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, Pos, Fecha_propuesta_aceptada)
    elif (Tipo == "Inicio del proyecto"):
        if (FechaPropuesta == ""):
            Fecha_inicio_proyecto = "-"
        else:
            Fecha_inicio_proyecto = str(FechaPropuesta)
        Fecha.modificarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, Pos, Fecha_inicio_proyecto)
    elif (Tipo == "Fin del proyecto"):
        if (FechaPropuesta == ""):
            Fecha_fin_proyecto = "-"
        else:
                Fecha_fin_proyecto = str(FechaPropuesta)
        Fecha.modificarFecha_fin_proyecto(Lista_Fecha_fin_proyecto, Pos, Fecha_fin_proyecto)
    elif (Tipo == "Propuesta de prorroga recibida"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_prorroga_recibida = "-"
        else:
            Fecha_propuesta_prorroga_recibida = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida, Pos,
                                                   Fecha_propuesta_prorroga_recibida)
    elif (Tipo == "Propuesta de prorroga aceptada"):
        if (FechaPropuesta == ""):
            Fecha_propuesta_prorroga_aceptada = "-"
        else:
            Fecha_propuesta_prorroga_aceptada = str(FechaPropuesta)
        Fecha.modificarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada, Pos,
                                                   Fecha_propuesta_prorroga_aceptada)
    elif (Tipo == "Inicio de proyecto con prorroga"):
        if (FechaPropuesta == ""):
            Fecha_inicio_proyecto_prorroga = "-"
        else:
            Fecha_inicio_proyecto_prorroga = str(FechaPropuesta)
        Fecha.modificarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga, Pos, Fecha_inicio_proyecto_prorroga)
    elif (Tipo == "Fin de proyecto con prorroga"):
        if (FechaPropuesta == ""):
            Fecha_fin_proyecto_prorroga = "-"
        else:
            Fecha_fin_proyecto_prorroga = str(FechaPropuesta)
        Fecha.modificarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga, Pos, Fecha_fin_proyecto_prorroga)

def ModificarDatos(Pos,
            Numero_de_estudiantes,
            Nombres,
            Codigos,
            Documento_identificacion,
            Direccion,
            Telefono,
            Correo_personal_estudiante,
            Nombre_proyecto,
            Modalidad,
            Resumen,
            Anotacion,
            Etapa,
            Nombre_director,
            Correo_personal_director,
            Nombre_jurado,
            Correo_personal_jurado
            ):

    global Lista_Numero_Estudiantes,Lista_Nombres
    global Lista_Codigos,Lista_Doc
    global Lista_Direccion,Lista_Telefonos
    global Lista_Correo_Estudiante,Lista_Nombre_proyecto
    global Lista_Modalidad,Lista_Resumen
    global Lista_Anotacion,Lista_Etapa
    global Lista_Nombre_Director,Lista_Correo_Director
    global Lista_Nombre_Jurado, Lista_Correo_Jurado

    global Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga


    global Fecha_propuesta_recibida
    global Fecha_propuesta_jurado, Fecha_propuesta_observaciones
    global Fecha_propuesta_aceptada
    global Fecha_inicio_proyecto
    global Fecha_fin_proyecto, Fecha_propuesta_prorroga_recibida
    global Fecha_propuesta_prorroga_aceptada
    global Fecha_inicio_proyecto_prorroga
    global Fecha_fin_proyecto_prorroga

    if (Numero_de_estudiantes == ""):
        Numero_de_estudiantes = 1
    else:
        Numero_de_estudiantes = int(Numero_de_estudiantes)

    if (Nombres == ""):
        Nombres = "-"
    else:
        Nombres = str(Nombres)

    if (Codigos == ""):
        Codigos = "-"
    else:
        Codigos = str(Codigos)

    if (Documento_identificacion == ""):
        Documento_identificacion = "-"
    else:
        Documento_identificacion = str(Documento_identificacion)

    if (Direccion == ""):
        Direccion = "-"
    else:
        Direccion = str(Direccion)

    if (Telefono == ""):
        Telefono = "-"
    else:
        Telefono = str(Telefono)

    if (Correo_personal_estudiante == ""):
        Correo_personal_estudiante = "-"
    else:
        Correo_personal_estudiante = str(Correo_personal_estudiante)

    if (Nombre_proyecto == ""):
        Nombre_proyecto = "-"
    else:
        Nombre_proyecto = str(Nombre_proyecto)

    if (Modalidad == ""):
        Modalidad = "-"
    else:
        Modalidad = str(Modalidad)

    if (Resumen == ""):
        Resumen = "-"
    else:
        Resumen = str(Resumen)

    if (Anotacion == ""):
        Anotacion = "-"
    else:
        Anotacion = str(Anotacion)

    if (Etapa == ""):
        Etapa = "-"
    else:
        Etapa = str(Etapa)

    if (Nombre_director == ""):
        Nombre_director = "-"
    else:
        Nombre_director = str(Nombre_director)

    if (Correo_personal_director == ""):
        Correo_personal_director = "-"
    else:
        Correo_personal_director = str(Correo_personal_director)

    if (Nombre_jurado == ""):
        Nombre_jurado = "-"
    else:
        Nombre_jurado = str(Nombre_jurado)

    if (Correo_personal_jurado == ""):
        Correo_personal_jurado = "-"
    else:
        Correo_personal_jurado = str(Correo_personal_jurado)

    if (Fecha_propuesta_recibida == ""):
        Fecha_propuesta_recibida = "-"
    else:
        Fecha_propuesta_recibida = str(Fecha_propuesta_recibida)

    if (Fecha_propuesta_jurado == ""):
        Fecha_propuesta_jurado = "-"
    else:
        Fecha_propuesta_jurado = str(Fecha_propuesta_jurado)

    if (Fecha_propuesta_observaciones  == ""):
        Fecha_propuesta_observaciones = "-"
    else:
        Fecha_propuesta_observaciones = str(Fecha_propuesta_observaciones )

    if (Fecha_propuesta_aceptada == ""):
        Fecha_propuesta_aceptada = "-"
    else:
        Fecha_propuesta_aceptada = str(Fecha_propuesta_aceptada)

    if (Fecha_inicio_proyecto == ""):
        Fecha_inicio_proyecto = "-"
    else:
        Fecha_inicio_proyecto = str(Fecha_inicio_proyecto)

    if (Fecha_fin_proyecto == ""):
        Fecha_fin_proyecto = "-"
    else:
        Fecha_fin_proyecto = str(Fecha_fin_proyecto)

    if (Fecha_propuesta_prorroga_recibida == ""):
        Fecha_propuesta_prorroga_recibida = "-"
    else:
        Fecha_propuesta_prorroga_recibida = str(Fecha_propuesta_prorroga_recibida)

    if (Fecha_propuesta_prorroga_aceptada == ""):
        Fecha_propuesta_prorroga_aceptada = "-"
    else:
        Fecha_propuesta_prorroga_aceptada = str(Fecha_propuesta_prorroga_aceptada)

    if (Fecha_inicio_proyecto_prorroga == ""):
        Fecha_inicio_proyecto_prorroga = "-"
    else:
        Fecha_inicio_proyecto_prorroga = str(Fecha_inicio_proyecto_prorroga)

    if (Fecha_fin_proyecto_prorroga == ""):
        Fecha_fin_proyecto_prorroga = "-"
    else:
        Fecha_fin_proyecto_prorroga = str(Fecha_fin_proyecto_prorroga)

    #Variable para iterar debido a la cantidad de estudiantes
    i=1
    #while(i<=Numero_de_estudiantes):
    while(i<=1):
        Estudiante.modificarNumero_de_estudiantes(Lista_Numero_Estudiantes,Pos,Numero_de_estudiantes)
        Estudiante.modificarNombres(Lista_Nombres,Pos,Nombres)
        Estudiante.modificarCodigos(Lista_Codigos,Pos,Codigos)
        Estudiante.modificarDocumento_identificacion(Lista_Doc,Pos,Documento_identificacion)
        Estudiante.modificarDireccion(Lista_Direccion,Pos,Direccion)
        Estudiante.modificarTelefono(Lista_Telefonos,Pos,Telefono)
        Estudiante.modificarCorreo_Personal(Lista_Correo_Estudiante,Pos,Correo_personal_estudiante)
        Trabajo.modificarNombres(Lista_Nombre_proyecto,Pos,Nombre_proyecto)
        Trabajo.modificarModalidad(Lista_Modalidad,Pos,Modalidad)
        Trabajo.modificarResumen(Lista_Resumen,Pos,Resumen)
        Trabajo.modificarAnotaciones(Lista_Anotacion,Pos,Anotacion)
        Trabajo.modificarEtapa(Lista_Etapa,Pos,Etapa)
        Director.modificarNombres(Lista_Nombre_Director,Pos,Nombre_director)
        Director.modificarCorreo_Personal(Lista_Correo_Director,Pos,Correo_personal_director)
        Jurado.modificarNombres(Lista_Nombre_Jurado,Pos,Nombre_jurado)
        Jurado.modificarCorreo_Personal(Lista_Correo_Jurado,Pos,Correo_personal_jurado)
        #Fecha.modificarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, Pos,Fecha_propuesta_recibida)
        #Fecha.modificarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, Pos,Fecha_propuesta_jurado)
        #Fecha.modificarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, Pos,Fecha_propuesta_observaciones)
        #Fecha.modificarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, Pos,Fecha_propuesta_aceptada)
        #Fecha.modificarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, Pos,Fecha_inicio_proyecto)
        #Fecha.modificarFecha_fin_proyecto(Lista_Fecha_fin_proyecto,Pos, Fecha_fin_proyecto)
        #Fecha.modificarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida,Pos,
        #                                               Fecha_propuesta_prorroga_recibida)
        #Fecha.modificarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada,Pos,
        #                                               Fecha_propuesta_prorroga_aceptada)
        #Fecha.modificarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga,Pos,
        #                                            Fecha_inicio_proyecto_prorroga)
        #Fecha.modificarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga,Pos, Fecha_fin_proyecto_prorroga)
        if(i!=Numero_de_estudiantes):
            Parametros_varios_estudiantes()
        i=i+1

def AgregarDatosProfesor(Nombre_profesor,
            Correo,
            Foto):

    global Lista_Nombres_profesores, Lista_Correos_profesores, Lista_Fotos_profesores

    if (Nombre_profesor == ""):
        Nombre_profesor = "-"
    else:
        Nombre_profesor = str(Nombre_profesor)

    if (Correo == ""):
        Correo = "-"
    else:
        Nombres = str(Correo)

    if (Foto == ""):
        Foto = "-"
    else:
        Foto = str(Foto)

    Trabajo.agregarProfesor(Nombre_profesor,Correo,Foto)


def AgregarDatos(Numero_de_estudiantes,
            Nombres,
            Codigos,
            Documento_identificacion,
            Direccion,
            Telefono,
            Correo_personal_estudiante,
            Nombre_proyecto,
            Modalidad,
            Resumen,
            Anotacion,
            Etapa,
            Nombre_director,
            Correo_personal_director,
            Nombre_jurado,
            Correo_personal_jurado
            ):

    global Lista_Numero_Estudiantes,Lista_Nombres
    global Lista_Codigos,Lista_Doc
    global Lista_Direccion,Lista_Telefonos
    global Lista_Correo_Estudiante,Lista_Nombre_proyecto
    global Lista_Modalidad,Lista_Resumen
    global Lista_Anotacion,Lista_Etapa
    global Lista_Nombre_Director,Lista_Correo_Director
    global Lista_Nombre_Jurado, Lista_Correo_Jurado

    global Fecha_propuesta_recibida
    global Fecha_propuesta_jurado, Fecha_propuesta_observaciones
    global Fecha_propuesta_aceptada
    global Fecha_inicio_proyecto
    global Fecha_fin_proyecto, Fecha_propuesta_prorroga_recibida
    global Fecha_propuesta_prorroga_aceptada
    global Fecha_inicio_proyecto_prorroga
    global Fecha_fin_proyecto_prorroga

    if (Numero_de_estudiantes == ""):
        Numero_de_estudiantes = 1
    else:
        Numero_de_estudiantes = int(Numero_de_estudiantes)

    if (Nombres == ""):
        Nombres = "-"
    else:
        Nombres = str(Nombres)

    if (Codigos == ""):
        Codigos = "-"
    else:
        Codigos = str(Codigos)

    if (Documento_identificacion == ""):
        Documento_identificacion = "-"
    else:
        Documento_identificacion = str(Documento_identificacion)

    if (Direccion == ""):
        Direccion = "-"
    else:
        Direccion = str(Direccion)

    if (Telefono == ""):
        Telefono = "-"
    else:
        Telefono = str(Telefono)

    if (Correo_personal_estudiante == ""):
        Correo_personal_estudiante = "-"
    else:
        Correo_personal_estudiante = str(Correo_personal_estudiante)

    if (Nombre_proyecto == ""):
        Nombre_proyecto = "-"
    else:
        Nombre_proyecto = str(Nombre_proyecto)

    if (Modalidad == ""):
        Modalidad = "-"
    else:
        Modalidad = str(Modalidad)

    if (Resumen == ""):
        Resumen = "-"
    else:
        Resumen = str(Resumen)

    if (Anotacion == ""):
        Anotacion = "-"
    else:
        Anotacion = str(Anotacion)

    if (Etapa == ""):
        Etapa = "-"
    else:
        Etapa = str(Etapa)

    if (Nombre_director == ""):
        Nombre_director = "-"
    else:
        Nombre_director = str(Nombre_director)

    if (Correo_personal_director == ""):
        Correo_personal_director = "-"
    else:
        Correo_personal_director = str(Correo_personal_director)

    if (Nombre_jurado == ""):
        Nombre_jurado = "-"
    else:
        Nombre_jurado = str(Nombre_jurado)

    if (Correo_personal_jurado == ""):
        Correo_personal_jurado = "-"
    else:
        Correo_personal_jurado = str(Correo_personal_jurado)

    if (Fecha_propuesta_recibida == ""):
        Fecha_propuesta_recibida = "-"
    else:
        Fecha_propuesta_recibida = str(Fecha_propuesta_recibida)

    if (Fecha_propuesta_jurado == ""):
        Fecha_propuesta_jurado = "-"
    else:
        Fecha_propuesta_jurado = str(Fecha_propuesta_jurado)

    if (Fecha_propuesta_observaciones  == ""):
        Fecha_propuesta_observaciones = "-"
    else:
        Fecha_propuesta_observaciones = str(Fecha_propuesta_observaciones )

    if (Fecha_propuesta_aceptada == ""):
        Fecha_propuesta_aceptada = "-"
    else:
        Fecha_propuesta_aceptada = str(Fecha_propuesta_aceptada)

    if (Fecha_inicio_proyecto == ""):
        Fecha_inicio_proyecto = "-"
    else:
        Fecha_inicio_proyecto = str(Fecha_inicio_proyecto)

    if (Fecha_fin_proyecto == ""):
        Fecha_fin_proyecto = "-"
    else:
        Fecha_fin_proyecto = str(Fecha_fin_proyecto)

    if (Fecha_propuesta_prorroga_recibida == ""):
        Fecha_propuesta_prorroga_recibida = "-"
    else:
        Fecha_propuesta_prorroga_recibida = str(Fecha_propuesta_prorroga_recibida)

    if (Fecha_propuesta_prorroga_aceptada == ""):
        Fecha_propuesta_prorroga_aceptada = "-"
    else:
        Fecha_propuesta_prorroga_aceptada = str(Fecha_propuesta_prorroga_aceptada)

    if (Fecha_inicio_proyecto_prorroga == ""):
        Fecha_inicio_proyecto_prorroga = "-"
    else:
        Fecha_inicio_proyecto_prorroga = str(Fecha_inicio_proyecto_prorroga)

    if (Fecha_fin_proyecto_prorroga == ""):
        Fecha_fin_proyecto_prorroga = "-"
    else:
        Fecha_fin_proyecto_prorroga = str(Fecha_fin_proyecto_prorroga)

    #Variable para iterar debido a la cantidad de estudiantes
    i=1
    #while(i<=Numero_de_estudiantes):
    while(i<=1):
        Estudiante.agregarNumero_de_estudiantes(Lista_Numero_Estudiantes,Numero_de_estudiantes)
        Estudiante.agregarNombres(Lista_Nombres,Nombres)
        Estudiante.agregarCodigos(Lista_Codigos,Codigos)
        Estudiante.agregarDocumento_identificacion(Lista_Doc,Documento_identificacion)
        Estudiante.agregarDireccion(Lista_Direccion,Direccion)
        Estudiante.agregarTelefono(Lista_Telefonos,Telefono)
        Estudiante.agregarCorreo_Personal(Lista_Correo_Estudiante,Correo_personal_estudiante)
        Trabajo.agregarNombre(Lista_Nombre_proyecto,Nombre_proyecto)
        Trabajo.agregarModalidad(Lista_Modalidad,Modalidad)
        Trabajo.agregarResumen(Lista_Resumen,Resumen)
        Trabajo.agregarAnotaciones(Lista_Anotacion,Anotacion)
        Trabajo.agregarEtapa(Lista_Etapa,Etapa)
        Director.agregarNombres(Lista_Nombre_Director,Nombre_director)
        Director.agregarCorreo_Personal(Lista_Correo_Director,Correo_personal_director)
        Jurado.agregarNombres(Lista_Nombre_Jurado,Nombre_jurado)
        Jurado.agregarCorreo_Personal(Lista_Correo_Jurado,Correo_personal_jurado)
        Fecha.agregarFecha_propuesta_recibida(Lista_Fecha_propuesta_recibida, Fecha_propuesta_recibida)
        Fecha.agregarFecha_propuesta_jurado(Lista_Fecha_propuesta_jurado, Fecha_propuesta_jurado)
        Fecha.agregarFecha_propuesta_observaciones(Lista_Fecha_propuesta_observaciones, Fecha_propuesta_observaciones)
        Fecha.agregarFecha_propuesta_aceptada(Lista_Fecha_propuesta_aceptada, Fecha_propuesta_aceptada)
        Fecha.agregarFecha_inicio_proyecto(Lista_Fecha_inicio_proyecto, Fecha_inicio_proyecto)
        Fecha.agregarFecha_fin_proyecto(Lista_Fecha_fin_proyecto, Fecha_fin_proyecto)
        Fecha.agregarFecha_propuesta_prorroga_recibida(Lista_Fecha_propuesta_prorroga_recibida,
                                                       Fecha_propuesta_prorroga_recibida)
        Fecha.agregarFecha_propuesta_prorroga_aceptada(Lista_Fecha_propuesta_prorroga_aceptada,
                                                       Fecha_propuesta_prorroga_aceptada)
        Fecha.agregarFecha_inicio_proyecto_prorroga(Lista_Fecha_inicio_proyecto_prorroga,
                                                    Fecha_inicio_proyecto_prorroga)
        Fecha.agregarFecha_fin_proyecto_prorroga(Lista_Fecha_fin_proyecto_prorroga, Fecha_fin_proyecto_prorroga)
        if(i!=Numero_de_estudiantes):
            Parametros_varios_estudiantes()
        i=i+1

def Guardar():
    #print(Fecha.devolverFecha_propuesta_recibida())
    GuardarTot.actualizarDatabase(Estudiante.devolverNumero_de_estudiantes(),
                                    Estudiante.devolverNombres(),
                                    Estudiante.devolverCodigos(),
                                    Estudiante.devolverDocumento_identificacion(),
                                    Estudiante.devolverDireccion(),
                                    Estudiante.devolverTelefono(),
                                    Estudiante.devolverCorreo_Personal(),
                                    Trabajo.devolverNombre(),
                                    Trabajo.devolverModalidad(),
                                    Trabajo.devolverResumen(),
                                    Trabajo.devolverAnotaciones(),
                                    Trabajo.devolverEtapa(),
                                    Director.devolverNombres(),
                                    Director.devolverCorreo_Personal(),
                                    Jurado.devolverNombres(),
                                    Jurado.devolverCorreo_Personal(),
                                    Fecha.devolverFecha_propuesta_recibida(),
                                    Fecha.devolverFecha_propuesta_jurado(),
                                    Fecha.devolverFecha_propuesta_observaciones(),
                                    Fecha.devolverFecha_propuesta_aceptada(),
                                    Fecha.devolverFecha_inicio_proyecto(),
                                    Fecha.devolverFecha_fin_proyecto(),
                                    Fecha.devolverFecha_propuesta_prorroga_recibida(),
                                    Fecha.devolverFecha_propuesta_prorroga_aceptada(),
                                    Fecha.devolverFecha_inicio_proyecto_prorroga(),
                                    Fecha.devolverFecha_fin_proyecto_prorroga()
                                    )

def BuscarResumen(UsarFecha, ano1,mes1,dia1,ano2,mes2,dia2,Tipo,Modalidad,Codigo,Etapa,Concepto,DirectorD,Lector):
    global Lista_Numero_Estudiantes, Lista_Nombres
    global Lista_Codigos, Lista_Doc
    global Lista_Direccion, Lista_Telefonos
    global Lista_Correo_Estudiante, Lista_Nombre_proyecto, Lista_Modalidad
    global Lista_Resumen
    global Lista_Anotacion, Lista_Etapa
    global Lista_Nombre_Director, Lista_Correo_Director
    global Lista_Nombre_Jurado
    global Lista_Correo_Jurado, Lista_Fecha_propuesta_recibida
    global Lista_Fecha_propuesta_jurado
    global Lista_Fecha_propuesta_observaciones
    global Lista_Fecha_propuesta_aceptada, Lista_Fecha_inicio_proyecto
    global Lista_Fecha_fin_proyecto
    global Lista_Fecha_propuesta_prorroga_recibida
    global Lista_Fecha_propuesta_prorroga_aceptada
    global Lista_Fecha_inicio_proyecto_prorroga
    global Lista_Fecha_fin_proyecto_prorroga
    global Lista_Nombres_profesores, Lista_Correos_profesores, Lista_Fotos_profesores

    if(Modalidad!=""):
        PosModalidad=Trabajo.buscarModalidadResumen(Lista_Modalidad,Modalidad)
    else:
        PosModalidad=range(0,len(Lista_Nombre_proyecto))
    if (Codigo != ""):
        PosCodigo = Estudiante.buscarCodigosResumen(Lista_Codigos, Codigo)
    else:
        PosCodigo=range(0,len(Lista_Nombre_proyecto))
    if (Etapa != ""):
        PosEtapa = Trabajo.buscarEtapasResumen(Lista_Etapa,Etapa)
    else:
        PosEtapa=range(0,len(Lista_Nombre_proyecto))
    if (Concepto != ""):
        PosConcepto = Trabajo.buscarAnotacionesResumen(Lista_Anotacion,Concepto)
    else:
        PosConcepto=range(0,len(Lista_Nombre_proyecto))
    if (DirectorD != ""):
        PosDirectorD = Director.buscarDirectorResumen(Lista_Nombre_Director,DirectorD)
    else:
        PosDirectorD = range(0, len(Lista_Nombre_proyecto))
    if (Lector != ""):
        PosJurado= Jurado.buscarJuradoResumen(Lista_Nombre_Jurado, Lector)
    else:
        PosJurado=range(0,len(Lista_Nombre_proyecto))
    if (Tipo != ""):
        PosTipo= Fecha.buscarFechaResumen(Lista_Fecha_propuesta_recibida,
                                            Lista_Fecha_propuesta_jurado,
                                            Lista_Fecha_propuesta_observaciones,
                                            Lista_Fecha_propuesta_aceptada,
                                            Lista_Fecha_inicio_proyecto,
                                            Lista_Fecha_fin_proyecto,
                                            Lista_Fecha_propuesta_prorroga_recibida,
                                            Lista_Fecha_propuesta_prorroga_aceptada,
                                            Lista_Fecha_inicio_proyecto_prorroga,
                                            Lista_Fecha_fin_proyecto_prorroga,
                                            Tipo)
    else:
        PosTipo=range(0,len(Lista_Nombre_proyecto))
    if (UsarFecha==True):
        añoIni = int(ano1)
        mesIni = int(mes1)
        diaIni = int(dia1)
        añoFin = int(ano2)
        mesFin = int(mes2)
        diaFin = int(dia2)
        contAño = añoIni
        contMes = mesIni
        contDia = diaIni
        fecFin = str(añoFin) + ',' + str(mesFin) + ',' + str(diaFin)
        PosFechas=[]
        while(contAño<=añoFin):
            if(contDia>=32):
                contMes=contMes+1
                contDia=1
            if (contMes >= 13):
                contMes = 1
                contAño = contAño+1
            fec = str(contAño) + ',' + str(contMes) + ',' + str(contDia)
            Bus = Fecha.buscarFechaInternaResumen(Lista_Fecha_propuesta_recibida,
                                            Lista_Fecha_propuesta_jurado,
                                            Lista_Fecha_propuesta_observaciones,
                                            Lista_Fecha_propuesta_aceptada,
                                            Lista_Fecha_inicio_proyecto,
                                            Lista_Fecha_fin_proyecto,
                                            Lista_Fecha_propuesta_prorroga_recibida,
                                            Lista_Fecha_propuesta_prorroga_aceptada,
                                            Lista_Fecha_inicio_proyecto_prorroga,
                                            Lista_Fecha_fin_proyecto_prorroga,
                                            fec)
            PosFechas = PosFechas + Bus
            if(fec==fecFin):
                break
            contDia=contDia+1
    else:
        PosFechas = range(0, len(Lista_Nombre_proyecto))

    Cumplieron=[]
    for i in range(0, len(Lista_Nombre_proyecto)):
        if(i in PosModalidad and i in PosCodigo and i in PosEtapa and i in PosTipo and
        i in PosConcepto and i in PosDirectorD and i in PosJurado and i in PosFechas):
            Cumplieron.append(i)
    return Cumplieron

def Parametros_varios_estudiantes():
    global Nombres
    global Codigos,Documento_identificacion,Direccion
    global Telefono,Correo_personal_estudiante

    print("Ingrese nombre del estudiante")
    Nombres = input()
    if(Nombres==""):
        Nombres = "-"
    else:
        Nombres = str(Nombres)

    print("Ingrese codigo del estudiante")
    Codigos = input()
    if(Codigos==""):
        Codigos = "-"
    else:
        Codigos = str(Codigos)

    print("Ingrese documento de identificacion")
    Documento_identificacion = input()
    if(Documento_identificacion==""):
        Documento_identificacion = "-"
    else:
        Documento_identificacion = str(Documento_identificacion)

    print("Ingrese direccion")
    Direccion = input()
    if(Direccion==""):
        Direccion = "-"
    else:
        Direccion = str(Direccion)

    print("Ingrese numero telefonico")
    Telefono = input()
    if(Telefono==""):
        Telefono = "-"
    else:
        Telefono = str(Telefono)

    print("Ingrese correo personal del estudiante")
    Correo_personal_estudiante = input()
    if(Correo_personal_estudiante==""):
        Correo_personal_estudiante = "-"
    else:
        Correo_personal_estudiante = str(Correo_personal_estudiante)
