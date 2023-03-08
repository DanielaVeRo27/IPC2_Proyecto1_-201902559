import xml.etree.ElementTree as ET
from Organismos import Lista_Organismos
from Muestras import Lista_Muestra
from CeldasVivas import list_CeldasVivas

#C:\Users\Luisa\Documents\2023\Primer Semestre\Ipc 2\Proyecto1\FilePrueba.XML
#C:\Users\Luisa\Documents\2023\Primer Semestre\Ipc 2\Proyecto1\EntradaEjemplo.XML
OrganismosList =Lista_Organismos()
MuestraList = Lista_Muestra()
CeldaVivasList = list_CeldasVivas()
cont = 0
def LecturaArchivo(Ruta):
    #Organismos = Lista_Organismos()
    RutaL = input()
    Tree = ET.parse(RutaL)
    Raiz = Tree.getroot()           

    for hijo1 in Raiz.iter("listaOrganismos"):
        for subHijo1 in hijo1.iter("organismo"):
            for  subHijo1_1 in subHijo1.iter("codigo"):
                Codigo_Or = subHijo1_1.text
            for  subHijo1_1 in subHijo1.iter("nombre"):
                Nombre_Or = subHijo1_1.text
            
    for hijo1 in Raiz.iter("listamuestra"):
        for subHijo1 in hijo1.iter("Muestra"):
            for  subHijo1_1 in subHijo1.iter("codigo"):
                Codigo_Or = subHijo1_1.text
        
                
    
    print(Codigo_Or)
  

def Lectura():    

    global cont
    Ruta = input()
    Tree2 = ET.parse(Ruta)
    Raiz2 = Tree2.getroot()
    #for DatosMarte in Raiz.iter('datosMarte'):
    for listaOrganismo in Raiz2.iter('listaOrganismos'):
        for Organismo in listaOrganismo.iter('organismo'):
            cont += 1
            for Id_o in Organismo.iter('codigo'):
                Codigo_Or = Id_o.text
             # print(Codigo_Or)
            for nombre in Organismo.iter('nombre'):
                Nombre_Or = nombre.text
           #print(Nombre_Or)
            OrganismosList.Añadir(Codigo_Or,Nombre_Or,cont)            
    for listadoMuestra in Raiz2.iter('listadoMuestras'):
        for Muestra in listadoMuestra.iter('muestra'):
            for Id_Muestra in Muestra.iter('codigo'):
                Codigo_Mues = Id_Muestra.text
            for Des in Muestra.iter('descripcion'):
                Descrip_Muestra =   Des.text
            for Filas in Muestra.iter('filas'):
                N_Muestra = Filas.text
            for Columnas in Muestra.iter('columnas'):                
                M_Muestra = Columnas.text            
            MuestraList.Añadir(Codigo_Mues,Descrip_Muestra,N_Muestra,M_Muestra)
            for ListadoCeldaViva in Muestra.iter('listadoCeldasVivas'):  
                for CeldaViva in ListadoCeldaViva.iter('celdaViva'):
                    for fila in CeldaViva.iter('fila'):
                        filaV = fila.text
                    for Columna in CeldaViva.iter('columna'):
                        columnaV = Columna.text
                    for Codigo_OrVi in CeldaViva.iter("codigoOrganismo"):
                        Codi_OrgaVo = Codigo_OrVi.text
                    
                    CeldaVivasList.Añadir(Codigo_Mues,Codi_OrgaVo, filaV,columnaV)
                   
            
    """ OrganismosList.Imprimir()
    MuestraList.Imprimir()
    CeldaVivasList.imprimir()"""
    return {'Organismos' : OrganismosList,'Muestras':MuestraList,'CeldasVivas':CeldaVivasList} 

