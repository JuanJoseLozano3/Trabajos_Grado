#Definición de atributos de la clase estudiante
Numero_de_estudiantes = []
Nombres = []
Codigos = []
Documento_identificacion = []
Direccion = []
Telefono = []
Correo_personal = []

#Metodos de Asignación de datos
def asignarNumero_de_estudiantes(pListaNum):
    global Numero_de_estudiantes
    Numero_de_estudiantes = pListaNum

def asignarNombres(pListaNombres):
    global Nombres
    Nombres=pListaNombres

def asignarCodigos(pListaCodigos):
    global Codigos
    Codigos = pListaCodigos

def asignarDocumento_identificacion(pListaDoc):
    global Documento_identificacion
    Documento_identificacion = pListaDoc

def asignarDireccion(pListaDireccion):
    global Direccion
    Direccion = pListaDireccion

def asignarTelefono(pListaTelefono):
    global Telefono
    Telefono = pListaTelefono

def asignarCorreo_Personal(pLista_Correo):
    global Correo_personal
    Correo_personal = pLista_Correo

#Metodos de Buscar datos
def buscarNombres(pListaNombres,pNombres):
    Posicion=pListaNombres.index(pNombres)
    return Posicion

def buscarCodigos(pListaCodigos,pCodigos):
    Posicion=pListaCodigos.index(str(pCodigos))
    return Posicion

def buscarCodigosResumen(pListaCodigos,pCodigos):
    i = 0
    Posicion = []
    while (i < len(pListaCodigos)):
        if (pCodigos in pListaCodigos[i]):
            Posicion.append(i)
        i = i + 1
    return Posicion

def buscarDocumento_identificacion(pListaDoc,pDocumento_identificacion):
    Posicion=pListaDoc.index(pDocumento_identificacion)
    return Posicion

#Metodos de Modificar datos
def modificarNumero_de_estudiantes(pListaNum,pPosicion,pNumero_de_estudiantes):
    global Numero_de_estudiantes
    pListaNum[pPosicion] = pNumero_de_estudiantes
    Numero_de_estudiantes = pListaNum

def modificarNombres(pListaNombres,pPosicion,pNombres):
    global Nombres
    pListaNombres[pPosicion] = pNombres
    Nombres=pListaNombres

def modificarCodigos(pListaCodigos,pPosicion,pCodigos):
    global Codigos
    pListaCodigos[pPosicion] = str(pCodigos)
    Codigos = pListaCodigos

def modificarDocumento_identificacion(pListaDoc,pPosicion,pDocumento_identificacion):
    global Documento_identificacion
    pListaDoc[pPosicion] = pDocumento_identificacion
    Documento_identificacion = pListaDoc

def modificarDireccion(pListaDireccion,pPosicion,pDireccion):
    global Direccion
    pListaDireccion[pPosicion] = pDireccion
    Direccion = pListaDireccion

def modificarTelefono(pListaTelefono,pPosicion,pTelefono):
    global Telefono
    pListaTelefono[pPosicion] = pTelefono
    Telefono = pListaTelefono

def modificarCorreo_Personal(pLista_Correo,pPosicion,pCorreo_personal):
    global Correo_personal
    pLista_Correo = pCorreo_personal
    Correo_personal = pLista_Correo

#Metodos de Agregar datos
def agregarNumero_de_estudiantes(pListaNum,pNumero_de_estudiantes):
    global Numero_de_estudiantes
    pListaNum.append(pNumero_de_estudiantes)
    Numero_de_estudiantes = pListaNum

def agregarNombres(pListaNombres,pNombres):
    global Nombres
    pListaNombres.append(pNombres)
    Nombres=pListaNombres

def agregarCodigos(pListaCodigos,pCodigos):
    global Codigos
    pListaCodigos.append(str(pCodigos))
    Codigos = pListaCodigos

def agregarDocumento_identificacion(pListaDoc,pDocumento_identificacion):
    global Documento_identificacion
    pListaDoc.append(pDocumento_identificacion)
    Documento_identificacion = pListaDoc

def agregarDireccion(pListaDireccion,pDireccion):
    global Direccion
    pListaDireccion.append(pDireccion)
    Direccion = pListaDireccion

def agregarTelefono(pListaTelefono,pTelefono):
    global Telefono
    pListaTelefono.append(pTelefono)
    Telefono = pListaTelefono

def agregarCorreo_Personal(pLista_Correo,pCorreo_personal):
    global Correo_personal
    pLista_Correo.append(pCorreo_personal)
    Correo_personal = pLista_Correo

#Metodos de Retorno de datos
def devolverNumero_de_estudiantes():
    global Nombres
    return(Numero_de_estudiantes)

def devolverNombres():
    global Nombres
    return(Nombres)

def devolverCodigos():
    global Codigos
    return(Codigos)

def devolverDocumento_identificacion():
    global Documento_identificacion
    return(Documento_identificacion)

def devolverDireccion():
    global Direccion
    return(Direccion)

def devolverTelefono():
    global Telefono
    return(Telefono)

def devolverCorreo_Personal():
    global Correo_personal
    return(Correo_personal)
