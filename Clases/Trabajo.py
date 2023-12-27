#Definición de atributos de la clase estudiante
Nombre = []
Modalidad = []
Resumen = []
Anotaciones = []
Etapa = []
NombrePro = []
Correos=[]
Fotos=[]
"""
NombresPro= [
    "Ing. Carlos Diaz",
    "Ing. Ricardo Troncoso",
    "Ing. Gustavo Martinez",
    "Ing. Celso Rodriguez",
    "Ing. Alexandra la Cruz",
    "Ing. Elizabeth Granados",
    "Ing. Juan Betancourt",
    ]

Correos = [
    "andres.diaz@unibague.edu.co",
    "ricador.troncoso@unibague.edu.co",
    "gustavo.martinez@unibague.edu.co",
    "celso.rodriguez@unibague.edu.co",
    "alexandra.lacruz@unibague.edu.co",
    "elizabeth.granados@unibague.edu.co",
    "juan.betancourt@unibague.edu.co",
    ]

Fotos = [
    "Andres_diaz.png",
    "Ricardo_troncoso.png",
    "Gustavo_martinez.png",
    "Celso_rodriguez.png",
    "Alexandra_lacruz.png",
    "Elizabeth_granados.png",
    "Juan_betancourt.png",
]
"""

def NombreProfesores():
    global NombresPro
    return NombresPro

def CorreoProfesores():
    global Correos
    return Correos

def FotosProfesores():
    global Fotos
    return Fotos

#Metodos de Asignación de datos

def asignarProfesores(pNombres,pCorreos,pFotos):
    global NombresPro, Correos, Fotos
    NombresPro = pNombres
    Correos = pCorreos
    Fotos = pFotos

def asignarNombre(pNombre):
    global Nombre
    Nombre = pNombre

def asignarModalidad(pModalidad):
    global Modalidad
    Modalidad = pModalidad

def asignarResumen(pResumen):
    global Resumen
    Resumen = pResumen

def asignarAnotaciones(pAnotaciones):
    global Anotaciones
    Anotaciones = pAnotaciones

def asignarEtapa(pEtapa):
    global Etapa
    Etapa = pEtapa

#Metodos de Buscar datos
def buscarNombre(pListaNombres,pNombres):
    Posicion=pListaNombres.index(pNombres)
    return Posicion

def buscarModalidad(pListaModalidad,pModalidad):
    Posicion=pListaModalidad.index(pModalidad)
    return Posicion

def buscarModalidadResumen(pListaModalidad,pModalidad):
    i=0
    Posicion=[]
    while(i<len(pListaModalidad)):
        if(pListaModalidad[i]==pModalidad):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscarAnotacionesResumen(pListaAnotaciones,pAnotacion):
    i=0
    Posicion=[]
    while(i<len(pListaAnotaciones)):
        if(pAnotacion in pListaAnotaciones[i]):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscarEtapasResumen(pListaEtapas,pEtapas):
    i=0
    Posicion=[]
    while(i<len(pListaEtapas)):
        if(pEtapas in pListaEtapas[i]):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscarEtapa(pListaEtapa,pEtapa):
    Posicion=pListaEtapa.index(pEtapa)
    return Posicion

#Metodos de Modificar datos
def modificarNombres(pListaNombres,pPosicion,pNombres):
    global Nombres
    pListaNombres[pPosicion] = pNombres
    Nombres=pListaNombres

def modificarModalidad(pListaModalidad,pPosicion,pModalidad):
    global Modalidad
    pListaModalidad[pPosicion] = pModalidad
    Modalidad = pListaModalidad

def modificarResumen(pListaResumen,pPosicion,pResumen):
    global Resumen
    pListaResumen[pPosicion] = pResumen
    Resumen = pListaResumen

def modificarAnotaciones(pListaAnotaciones,pPosicion,pAnotaciones):
    global Anotaciones
    pListaAnotaciones[pPosicion] = pAnotaciones
    Anotaciones = pListaAnotaciones

def modificarEtapa(pListaEtapa,pPosicion,pEtapa):
    global Etapa
    pListaEtapa[pPosicion] = pEtapa
    Etapa = pListaEtapa

#Metodos de Agregar datos
def agregarNombre(pLista_Nombre, pNombre):
    global Nombre
    pLista_Nombre.append(pNombre)
    Nombre = pLista_Nombre

def agregarModalidad(pListaModalidad, pModalidad):
    global Modalidad
    pListaModalidad.append(pModalidad)
    Modalidad = pListaModalidad

def agregarResumen(pListaResumen, pResumen):
    global Resumen
    pListaResumen.append(pResumen)
    Resumen = pListaResumen

def agregarAnotaciones(pListaAnotaciones, pAnotaciones):
    global Anotaciones
    pListaAnotaciones.append(pAnotaciones)
    Anotaciones = pListaAnotaciones

def agregarEtapa(pListaEtapa, pEtapa):
    global Etapa
    pListaEtapa.append(pEtapa)
    Etapa = pListaEtapa

def agregarProfesor(pNombre, pCorreo, pFoto):
    global NombresPro
    global Correos
    NombresPro.append(pNombre)
    Correos.append(pCorreo)
    Fotos.append(pFoto)

#Metodos de Retorno de datos
def devolverNombre():
    global Nombre
    return(Nombre)

def devolverModalidad():
    global Modalidad
    return(Modalidad)

def devolverResumen():
    global Resumen
    return(Resumen)

def devolverAnotaciones():
    global Anotaciones
    return(Anotaciones)

def devolverEtapa():
    global Etapa
    return(Etapa)
