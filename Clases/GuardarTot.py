import pandas as pd

#CREAR
def actualizarDatabase(pNum,pNom_est,pCodigos,pDoc,pDir,pTel,pCor_est,
                       pNom_tra,pMod,pRes,pAnot,pEta,
                       pNom_dir,pCor_dir,
                       pNom_jur,pCor_jur,
                       pFec_pro_rec,pFec_pro_jur,pFec_pro_obs,pFec_pro_acep,
                       pFec_ini_pro,pFec_fin_pro,pFec_pro_pro_rec,pFec_pro_pro_acep,
                       pFec_ini_pro_pro,pFec_fin_pro_pro):
    diccionario = {}
    diccionario={"Numero_de_estudiantes":pNum,
                 "Nombres":pNom_est,
                 "Codigos":pCodigos,
                 "Documento_identificacion":pDoc,
                 "Direccion":pDir,
                 "Telefonos":pTel,
                 "Correo_personal_estudiante":pCor_est,
                 "Nombre_proyecto":pNom_tra,
                 "Modalidad":pMod,
                 "Resumen":pRes,
                 "Anotacion":pAnot,
                 "Etapa":pEta,
                 "Nombre_director":pNom_dir,
                 "Correo_personal_director":pCor_dir,
                 "Nombre_jurado":pNom_jur,
                 "Correo_personal_jurado":pCor_jur,
                 "Fecha_propuesta_recibida":pFec_pro_rec,
                 "Fecha_propuesta_jurado":pFec_pro_jur,
                 "Fecha_propuesta_observaciones":pFec_pro_obs,
                 "Fecha_propuesta_aceptada":pFec_pro_acep,
                 "Fecha_inicio_proyecto":pFec_ini_pro,
                 "Fecha_fin_proyecto":pFec_fin_pro,
                 "Fecha_propuesta_prorroga_recibida":pFec_pro_pro_rec,
                 "Fecha_propuesta_prorroga_aceptada":pFec_pro_pro_acep,
                 "Fecha_inicio_proyecto_prorroga":pFec_ini_pro_pro,
                 "Fecha_fin_proyecto_prorroga":pFec_fin_pro_pro}

    lista=range(len(pNum))
    df = pd.DataFrame(data=diccionario,index=lista)
    df.to_csv("Clases\Base.csv",index=False)

def actualizarDatabaseProfesores(pNombres,pCorreos,pFotos):
    diccionario = {}
    diccionario={"Nombre_profesores":pNombres,
                 "Correos":pCorreos,
                 "Fotos":pFotos,}

    lista=range(len(pNombres))
    df = pd.DataFrame(data=diccionario,index=lista)
    df.to_csv("Clases\Profesores.csv",index=False)


#print(df)


"""
#LEERLO
file_name = 'Base.csv' # File name
#header = 0 # The header is the 2nd row

df = pd.read_csv(file_name)
url = list(df["Codigos"])
print(url)
#print(df.head()) # Prints first 5 rows from the top along with the header
#print(df.tail()) # Prints first 5 rows from the bottom along with the header
"""

"""
#AGREGAR
type(url)
url.append(1)
"""
