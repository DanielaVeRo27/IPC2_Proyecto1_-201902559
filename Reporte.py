from Organismos import Lista_Organismos
from Muestras import Lista_Muestra
from CeldasVivas import list_CeldasVivas
import xml.etree.ElementTree as ET
def Reporte(Ruta,Nombre,OrganismosL = Lista_Organismos, Muestra =Lista_Muestra,CeldasV=list_CeldasVivas):
    global arbol
    root = ET.Element("datosMarte")
    arbol = ET.ElementTree(root)
    doc = ET.SubElement(root, "listaOrganismo")
    def Or(self):
        Temporal = self.head        
        while Temporal != None:
            doc2 = ET.SubElement(doc, "organismo")
            
            nodo1 = ET.SubElement(doc2, "codigo")
            nodo1.text = str(Temporal.IdO)
            
            nodo2 = ET.SubElement(doc2, "nombre")
            nodo2.text = str(Temporal.Nombre)
            Temporal = Temporal.siguiente
    doc3 =ET.SubElement(root, "listadoMuestra")
    def Mues(self):
        global doc4
        Temporal = self.head
        while Temporal != None:
            doc4 =ET.SubElement(doc3, "muestra")
            nodo3 = ET.SubElement(doc4, "codigo")
            nodo3.text = str(Temporal.IdM)
            nodo4 = ET.SubElement(doc4, "descripcion")
            nodo4.text = str(Temporal.Des)
            nodo5 = ET.SubElement(doc4, "filas")
            nodo5.text = str(Temporal.N)
            nodo6 = ET.SubElement(doc4, "columnas")
            nodo6.text = str(Temporal.M)
            CeV(CeldasV,Temporal.IdM)
            Temporal = Temporal.siguiente
    def CeV(self, idm):
        Temporal = self.head
        while Temporal != None:
            if Temporal.IdM == idm:
                doc5 =ET.SubElement(doc4, "celdaViva")
                nodo7 = ET.SubElement(doc5, "fila")
                nodo7.text = str(Temporal.FilaV)
                nodo8 = ET.SubElement(doc4, "columna")
                nodo8.text = str(Temporal.ColumnaV)
                nodo9 = ET.SubElement(doc4, "columna")
                nodo9.text = str(Temporal.codigoOrganismo)
            Temporal = Temporal.siguiente
            
            
           
            ET.indent( arbol,'')
            arbol.write(Ruta+"/"+ Nombre + ".xml" )