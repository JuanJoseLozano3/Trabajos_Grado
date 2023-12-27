import numpy as np
from Clases import Fecha

#Definición de atributos de la clase estudiante
Nombre = []
Correo_personal = []

#Metodos de Asignación de datos
def asignarNombres(pLista_Nombres):
    global Nombres
    Nombres = pLista_Nombres

def asignarCorreo_Personal(pLista_Correo_personal):
    global Correo_personal
    Correo_personal = pLista_Correo_personal

#Metodos de Buscar datos
def contarJuzgando(pNombres):
    global Nombres
    Posicion=np.array(Nombres)
    pos = np.where(Posicion==pNombres)
    Finalizada=Fecha.contarFecha(pos[0])
    return len(pos[0])-Finalizada

def contarJuzgado(pNombres):
    global Nombres
    Posicion=np.array(Nombres)
    pos = np.where(Posicion==pNombres)
    Finalizada=Fecha.contarFecha(pos[0])
    return Finalizada

#Metodos de Buscar datos
def buscarNombres(pListaNombres,pNombres):
    Posicion=pListaNombres.index(pNombres)
    return Posicion

def buscarJuradoResumen(pListaNombres,pNombre):
    i=0
    Posicion=[]
    while(i<len(pListaNombres)):
        if(pNombre in pListaNombres[i]):
            Posicion.append(i)
        i=i+1
    return Posicion


#Metodos de Modificar datos
def modificarNombres(pListaNombres,pPosicion,pNombres):
    global Nombres
    pListaNombres[pPosicion] = pNombres
    Nombres=pListaNombres

def modificarCorreo_Personal(pLista_Correo,pPosicion,pCorreo_personal):
    global Correo_personal
    pLista_Correo[pPosicion] = pCorreo_personal
    Correo_personal = pLista_Correo


#Metodos de Agregar datos
def agregarNombres(pListaNombres,pNombres):
    global Nombres
    pListaNombres.append(pNombres)
    Nombres=pListaNombres

def agregarCorreo_Personal(pLista_Correo_personal,pCorreo_personal):
    global Correo_personal
    pLista_Correo_personal.append(pCorreo_personal)
    Correo_personal = pLista_Correo_personal

#Metodos de Retorno de datos
def devolverNombres():
    global Nombres
    return(Nombres)

def devolverCorreo_Personal():
    global Correo_personal
    return(Correo_personal)
