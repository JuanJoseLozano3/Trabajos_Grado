from datetime import date, time, datetime

Fecha_propuesta_recibida = []
Fecha_propuesta_jurado = []
Fecha_propuesta_observaciones = []
Fecha_propuesta_aceptada = []
Fecha_inicio_proyecto = []
Fecha_fin_proyecto = []
Fecha_propuesta_prorroga_recibida = []
Fecha_propuesta_prorroga_aceptada = []
Fecha_inicio_proyecto_prorroga = []
Fecha_fin_proyecto_prorroga = []


def contarFecha(Pos):
    global Fecha_fin_proyecto
    global Fecha_fin_proyecto_prorroga
    FechaFinPro=0
    for Posicion in Pos:
        if(Fecha_fin_proyecto[Posicion]!="-"):
            t = datetime(2022, 8, 26)
            hoy = t.today()
            proy = Fecha_fin_proyecto[Posicion]
            i = 0
            comas1 = []
            while (i < len(proy)):
                if (proy[i] == ','):
                    comas1.append(i)
                i = i + 1
            ano1 = proy[0:comas1[0]]
            mes1 = proy[comas1[0] + 1:comas1[1]]
            dia1 = proy[comas1[1] + 1:len(proy)]
            fin_sin = datetime(int(ano1), int(mes1), int(dia1))
            if(fin_sin<hoy):
                FechaFinPro+=1
        elif(Fecha_fin_proyecto_prorroga[Posicion]!="-"):
            t = datetime(2022, 8, 26)
            hoy = t.today()
            pror = Fecha_fin_proyecto_prorroga[Posicion]
            i = 0
            comas2 = []
            while (i < len(pror)):
                if (pror[i] == ','):
                    comas2.append(i)
                i = i + 1
            ano2 = pror[0:comas2[0]]
            mes2 = pror[comas2[0] + 1:comas2[1]]
            dia2 = pror[comas2[1] + 1:len(pror)]

            fin_con = datetime(int(ano2), int(mes2), int(dia2))
            if (fin_con < hoy):
                FechaFinPro += 1
    return FechaFinPro

#Metodos de Asignación de datos
def asignarFecha_propuesta_recibida(pLista_Fecha_propuesta_recibida):
    global Fecha_propuesta_recibida
    Fecha_propuesta_recibida = pLista_Fecha_propuesta_recibida

def asignarFecha_propuesta_jurado(pLista_Fecha_propuesta_jurado):
    global Fecha_propuesta_jurado
    Fecha_propuesta_jurado = pLista_Fecha_propuesta_jurado

def asignarFecha_propuesta_observaciones(pLista_Fecha_propuesta_observaciones):
    global Fecha_propuesta_observaciones
    Fecha_propuesta_observaciones = pLista_Fecha_propuesta_observaciones

def asignarFecha_propuesta_aceptada(pLista_Fecha_propuesta_aceptada):
    global Fecha_propuesta_aceptada
    Fecha_propuesta_aceptada = pLista_Fecha_propuesta_aceptada

def asignarFecha_inicio_proyecto(pLista_Fecha_inicio_proyecto):
    global Fecha_inicio_proyecto
    Fecha_inicio_proyecto = pLista_Fecha_inicio_proyecto

def asignarFecha_fin_proyecto(pLista_Fecha_fin_proyecto):
    global Fecha_fin_proyecto
    Fecha_fin_proyecto = pLista_Fecha_fin_proyecto

def asignarFecha_propuesta_prorroga_recibida(pLista_Fecha_propuesta_prorroga_recibida):
    global Fecha_propuesta_prorroga_recibida
    Fecha_propuesta_prorroga_recibida = pLista_Fecha_propuesta_prorroga_recibida

def asignarFecha_propuesta_prorroga_aceptada(pLista_Fecha_propuesta_prorroga_aceptada):
    global Fecha_propuesta_prorroga_aceptada
    Fecha_propuesta_prorroga_aceptada = pLista_Fecha_propuesta_prorroga_aceptada

def asignarFecha_inicio_proyecto_prorroga(pLista_Fecha_inicio_proyecto_prorroga):
    global Fecha_inicio_proyecto_prorroga
    Fecha_inicio_proyecto_prorroga = pLista_Fecha_inicio_proyecto_prorroga

def asignarFecha_fin_proyecto_prorroga(pLista_Fecha_fin_proyecto_prorroga):
    global Fecha_fin_proyecto_prorroga
    Fecha_fin_proyecto_prorroga = pLista_Fecha_fin_proyecto_prorroga

#Metodos de Buscar dia

def buscarFechaInternaResumen(pLista_Fecha_propuesta_recibida,
                       pLista_Fecha_propuesta_jurado,
                       pLista_Fecha_propuesta_observaciones,
                       pLista_Fecha_propuesta_aceptada,
                       pLista_Fecha_inicio_proyecto,
                       pLista_Fecha_fin_proyecto,
                       pLista_Fecha_propuesta_prorroga_recibida,
                       pLista_Fecha_propuesta_prorroga_aceptada,
                       pLista_Fecha_inicio_proyecto_prorroga,
                       pLista_Fecha_fin_proyecto_prorroga,
                       pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_recibida)):
        if(pLista_Fecha_propuesta_recibida[i]==pFecha):
            Posicion.append(i)
        i=i+1
    i = 0
    while (i < len(pLista_Fecha_propuesta_jurado)):
        if (pLista_Fecha_propuesta_jurado[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_propuesta_observaciones)):
        if (pLista_Fecha_propuesta_observaciones[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_propuesta_aceptada)):
        if (pLista_Fecha_propuesta_aceptada[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i = 0
    while (i < len(pLista_Fecha_inicio_proyecto)):
        if (pLista_Fecha_inicio_proyecto[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_fin_proyecto)):
        if (pLista_Fecha_fin_proyecto[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_propuesta_prorroga_recibida)):
        if (pLista_Fecha_propuesta_prorroga_recibida[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_propuesta_prorroga_aceptada)):
        if (pLista_Fecha_propuesta_prorroga_aceptada[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_inicio_proyecto_prorroga)):
        if (pLista_Fecha_inicio_proyecto_prorroga[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    i=0
    while (i < len(pLista_Fecha_fin_proyecto_prorroga)):
        if (pLista_Fecha_fin_proyecto_prorroga[i] == pFecha):
            Posicion.append(i)
        i = i + 1
    return Posicion

def buscarFechaResumen(pLista_Fecha_propuesta_recibida,
                       pLista_Fecha_propuesta_jurado,
                       pLista_Fecha_propuesta_observaciones,
                       pLista_Fecha_propuesta_aceptada,
                       pLista_Fecha_inicio_proyecto,
                       pLista_Fecha_fin_proyecto,
                       pLista_Fecha_propuesta_prorroga_recibida,
                       pLista_Fecha_propuesta_prorroga_aceptada,
                       pLista_Fecha_inicio_proyecto_prorroga,
                       pLista_Fecha_fin_proyecto_prorroga,
                       pFecha):
    i=0
    Posicion=[]
    if(pFecha == "Propuesta recibida"):
        while(i<len(pLista_Fecha_propuesta_recibida)):
            if(pLista_Fecha_propuesta_recibida[i]!="-"):
                Posicion.append(i)
            i=i+1
    if (pFecha == "Propuesta jurado"):
        while (i < len(pLista_Fecha_propuesta_jurado)):
            if (pLista_Fecha_propuesta_jurado[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Propuesta observaciones"):
        while (i < len(pLista_Fecha_propuesta_observaciones)):
            if (pLista_Fecha_propuesta_observaciones[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Propuesta aceptada"):
        while (i < len(pLista_Fecha_propuesta_aceptada)):
            if (pLista_Fecha_propuesta_aceptada[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Inicio proyecto"):
        while (i < len(pLista_Fecha_inicio_proyecto)):
            if (pLista_Fecha_inicio_proyecto[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Fin proyecto"):
        while (i < len(pLista_Fecha_fin_proyecto)):
            if (pLista_Fecha_fin_proyecto[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Propuesta prorroga recibida"):
        while (i < len(pLista_Fecha_propuesta_prorroga_recibida)):
            if (pLista_Fecha_propuesta_prorroga_recibida[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Propuesta prorroga aceptada"):
        while (i < len(pLista_Fecha_propuesta_prorroga_aceptada)):
            if (pLista_Fecha_propuesta_prorroga_aceptada[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Inicio proyecto con prorroga"):
        while (i < len(pLista_Fecha_inicio_proyecto_prorroga)):
            if (pLista_Fecha_inicio_proyecto_prorroga[i] != "-"):
                Posicion.append(i)
            i = i + 1
    if (pFecha == "Fin proyecto con prorroga"):
        while (i < len(pLista_Fecha_fin_proyecto_prorroga)):
            if (pLista_Fecha_fin_proyecto_prorroga[i] != "-"):
                Posicion.append(i)
            i = i + 1
    return Posicion

def buscardiaFecha_propuesta_recibida(pLista_Fecha_propuesta_recibida,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_recibida)):
        if(pLista_Fecha_propuesta_recibida[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_propuesta_jurado(pLista_Fecha_propuesta_jurado,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_jurado)):
        if(pLista_Fecha_propuesta_jurado[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_propuesta_observaciones(pLista_Fecha_propuesta_observaciones,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_observaciones)):
        if(pLista_Fecha_propuesta_observaciones[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_propuesta_aceptada(pLista_Fecha_propuesta_aceptada,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_aceptada)):
        if(pLista_Fecha_propuesta_aceptada[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_inicio_proyecto(pLista_Fecha_inicio_proyecto,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_inicio_proyecto)):
        if(pLista_Fecha_inicio_proyecto[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_fin_proyecto(pLista_Fecha_fin_proyecto,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_fin_proyecto)):
        if(pLista_Fecha_fin_proyecto[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_propuesta_prorroga_recibida(pLista_Fecha_propuesta_prorroga_recibida,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_prorroga_recibida)):
        if(pLista_Fecha_propuesta_prorroga_recibida[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_propuesta_prorroga_aceptada(pLista_Fecha_propuesta_prorroga_aceptada,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_propuesta_prorroga_aceptada)):
        if(pLista_Fecha_propuesta_prorroga_aceptada[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_inicio_proyecto_prorroga(pLista_Fecha_inicio_proyecto_prorroga,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_inicio_proyecto_prorroga)):
        if(pLista_Fecha_inicio_proyecto_prorroga[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

def buscardiaFecha_fin_proyecto_prorroga(pLista_Fecha_fin_proyecto_prorroga,pFecha):
    i=0
    Posicion=[]
    while(i<len(pLista_Fecha_fin_proyecto_prorroga)):
        if(pLista_Fecha_fin_proyecto_prorroga[i]==pFecha):
            Posicion.append(i)
        i=i+1
    return Posicion

#Metodos de Modificar datos
def modificarFecha_propuesta_recibida(pLista_Fecha_propuesta_recibida,pPosicion,pFecha):
    global Fecha_propuesta_recibida
    pLista_Fecha_propuesta_recibida[pPosicion] = pFecha
    Fecha_propuesta_recibida = pLista_Fecha_propuesta_recibida

def modificarFecha_propuesta_jurado(pLista_Fecha_propuesta_jurado,pPosicion,pFecha):
    global Fecha_propuesta_jurado
    pLista_Fecha_propuesta_jurado[pPosicion] = pFecha
    Fecha_propuesta_jurado = pLista_Fecha_propuesta_jurado

def modificarFecha_propuesta_observaciones(pLista_Fecha_propuesta_observaciones,pPosicion,pFecha):
    global Fecha_propuesta_observaciones
    pLista_Fecha_propuesta_observaciones[pPosicion] = pFecha
    Fecha_propuesta_observaciones = pLista_Fecha_propuesta_observaciones

def modificarFecha_propuesta_aceptada(pLista_Fecha_propuesta_aceptada,pPosicion,pFecha):
    global Fecha_propuesta_aceptada
    pLista_Fecha_propuesta_aceptada[pPosicion] = pFecha
    Fecha_propuesta_aceptada = pLista_Fecha_propuesta_aceptada

def modificarFecha_inicio_proyecto(pLista_Fecha_inicio_proyecto,pPosicion,pFecha):
    global Fecha_inicio_proyecto
    pLista_Fecha_inicio_proyecto[pPosicion] = pFecha
    Fecha_inicio_proyecto = pLista_Fecha_inicio_proyecto

def modificarFecha_fin_proyecto(pLista_Fecha_fin_proyecto,pPosicion,pFecha):
    global Fecha_fin_proyecto
    pLista_Fecha_fin_proyecto[pPosicion] = pFecha
    Fecha_fin_proyecto = pLista_Fecha_fin_proyecto

def modificarFecha_propuesta_prorroga_recibida(pLista_Fecha_propuesta_prorroga_recibida,pPosicion,pFecha):
    global Fecha_propuesta_prorroga_recibida
    pLista_Fecha_propuesta_prorroga_recibida[pPosicion] = pFecha
    Fecha_propuesta_prorroga_recibida = pLista_Fecha_propuesta_prorroga_recibida

def modificarFecha_propuesta_prorroga_aceptada(pLista_Fecha_propuesta_prorroga_aceptada,pPosicion,pFecha):
    global Fecha_propuesta_prorroga_aceptada
    pLista_Fecha_propuesta_prorroga_aceptada[pPosicion] = pFecha
    Fecha_propuesta_prorroga_aceptada = pLista_Fecha_propuesta_prorroga_aceptada

def modificarFecha_inicio_proyecto_prorroga(pLista_Fecha_inicio_proyecto_prorroga,pPosicion,pFecha):
    global Fecha_inicio_proyecto_prorroga
    pLista_Fecha_inicio_proyecto_prorroga[pPosicion] = pFecha
    Fecha_inicio_proyecto_prorroga = pLista_Fecha_inicio_proyecto_prorroga

def modificarFecha_fin_proyecto_prorroga(pLista_Fecha_fin_proyecto_prorroga,pPosicion,pFecha):
    global Fecha_fin_proyecto_prorroga
    pLista_Fecha_fin_proyecto_prorroga[pPosicion] = pFecha
    Fecha_fin_proyecto_prorroga = pLista_Fecha_fin_proyecto_prorroga

#Metodos de Agregar de datos
def agregarFecha_propuesta_recibida(pLista_Fecha_propuesta_recibida,pFecha):
    global Fecha_propuesta_recibida
    pLista_Fecha_propuesta_recibida.append(pFecha)
    Fecha_propuesta_recibida = pLista_Fecha_propuesta_recibida

def agregarFecha_propuesta_jurado(pLista_Fecha_propuesta_jurado,pFecha):
    global Fecha_propuesta_jurado
    pLista_Fecha_propuesta_jurado.append(pFecha)
    Fecha_propuesta_jurado = pLista_Fecha_propuesta_jurado

def agregarFecha_propuesta_observaciones(pLista_Fecha_propuesta_observaciones,pFecha):
    global Fecha_propuesta_observaciones
    pLista_Fecha_propuesta_observaciones.append(pFecha)
    Fecha_propuesta_observaciones = pLista_Fecha_propuesta_observaciones

def agregarFecha_propuesta_aceptada(pLista_Fecha_propuesta_aceptada,pFecha):
    global Fecha_propuesta_aceptada
    pLista_Fecha_propuesta_aceptada.append(pFecha)
    Fecha_propuesta_aceptada = pLista_Fecha_propuesta_aceptada

def agregarFecha_inicio_proyecto(pLista_Fecha_inicio_proyecto,pFecha):
    global Fecha_inicio_proyecto
    pLista_Fecha_inicio_proyecto.append(pFecha)
    Fecha_inicio_proyecto = pLista_Fecha_inicio_proyecto

def agregarFecha_fin_proyecto(pLista_Fecha_fin_proyecto,pFecha):
    global Fecha_fin_proyecto
    pLista_Fecha_fin_proyecto.append(pFecha)
    Fecha_fin_proyecto = pLista_Fecha_fin_proyecto

def agregarFecha_propuesta_prorroga_recibida(pLista_Fecha_propuesta_prorroga_recibida,pFecha):
    global Fecha_propuesta_prorroga_recibida
    pLista_Fecha_propuesta_prorroga_recibida.append(pFecha)
    Fecha_propuesta_prorroga_recibida = pLista_Fecha_propuesta_prorroga_recibida

def agregarFecha_propuesta_prorroga_aceptada(pLista_Fecha_propuesta_prorroga_aceptada,pFecha):
    global Fecha_propuesta_prorroga_aceptada
    pLista_Fecha_propuesta_prorroga_aceptada.append(pFecha)
    Fecha_propuesta_prorroga_aceptada = pLista_Fecha_propuesta_prorroga_aceptada

def agregarFecha_inicio_proyecto_prorroga(pLista_Fecha_inicio_proyecto_prorroga,pFecha):
    global Fecha_inicio_proyecto_prorroga
    pLista_Fecha_inicio_proyecto_prorroga.append(pFecha)
    Fecha_inicio_proyecto_prorroga = pLista_Fecha_inicio_proyecto_prorroga

def agregarFecha_fin_proyecto_prorroga(pLista_Fecha_fin_proyecto_prorroga,pFecha):
    global Fecha_fin_proyecto_prorroga
    pLista_Fecha_fin_proyecto_prorroga.append(pFecha)
    Fecha_fin_proyecto_prorroga = pLista_Fecha_fin_proyecto_prorroga

#Metodos de Retorno de datos
def devolverFecha_propuesta_recibida():
    global Fecha_propuesta_recibida
    return(Fecha_propuesta_recibida)

def devolverFecha_propuesta_jurado():
    global Fecha_propuesta_jurado
    return(Fecha_propuesta_jurado)

def devolverFecha_propuesta_observaciones():
    global Fecha_propuesta_observaciones
    return(Fecha_propuesta_observaciones)

def devolverFecha_propuesta_aceptada():
    global Fecha_propuesta_aceptada
    return(Fecha_propuesta_aceptada)

def devolverFecha_inicio_proyecto():
    global Fecha_inicio_proyecto
    return(Fecha_inicio_proyecto)

def devolverFecha_fin_proyecto():
    global Fecha_fin_proyecto
    return(Fecha_fin_proyecto)

def devolverFecha_propuesta_prorroga_recibida():
    global Fecha_propuesta_prorroga_recibida
    return(Fecha_propuesta_prorroga_recibida)

def devolverFecha_propuesta_prorroga_aceptada():
    global Fecha_propuesta_prorroga_aceptada
    return(Fecha_propuesta_prorroga_aceptada)

def devolverFecha_inicio_proyecto_prorroga():
    global Fecha_inicio_proyecto_prorroga
    return(Fecha_inicio_proyecto_prorroga)

def devolverFecha_fin_proyecto_prorroga():
    global Fecha_fin_proyecto_prorroga
    return(Fecha_fin_proyecto_prorroga)
