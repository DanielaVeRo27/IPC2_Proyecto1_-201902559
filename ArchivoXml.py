import xml.etree.ElementTree as ET
""" <listaOrganismos>
 <organismo>
 <codigo>[valorAlfanumérico]</codigo>
 <nombre>[valorAlfanumérico]</nombre>
 </organismo>

 </listaOrganismos>"""

#C:\Users\Luisa\Documents\2023\Primer Semestre\Ipc 2\Proyecto1\FilePrueba.XML
def LecturaArchivo(Ruta):
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

LecturaArchivo("HOI")

